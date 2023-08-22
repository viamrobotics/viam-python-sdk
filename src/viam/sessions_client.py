import asyncio
from concurrent.futures import Future, ProcessPoolExecutor
from datetime import timedelta
from multiprocessing import Value
from typing import Optional

from grpclib import Status
from grpclib.client import Channel
from grpclib.events import RecvTrailingMetadata, SendRequest, listen
from grpclib.exceptions import GRPCError, StreamTerminatedError
from grpclib.metadata import _MetadataLike

from viam import logging
from viam.proto.robot import RobotServiceStub, SendSessionHeartbeatRequest, StartSessionRequest
from viam.rpc.dial import DialOptions, dial

LOGGER = logging.getLogger(__name__)
SESSION_METADATA_KEY = "viam-sid"

EXEMPT_METADATA_METHODS = frozenset(
    [
        "/grpc.reflection.v1alpha.ServerReflection/ServerReflectionInfo",
        "/proto.rpc.webrtc.v1.SignalingService/Call",
        "/proto.rpc.webrtc.v1.SignalingService/CallUpdate",
        "/proto.rpc.webrtc.v1.SignalingService/OptionalWebRTCConfig",
        "/proto.rpc.v1.AuthService/Authenticate",
        "/viam.robot.v1.RobotService/ResourceNames",
        "/viam.robot.v1.RobotService/ResourceRPCSubtypes",
        "/viam.robot.v1.RobotService/StartSession",
        "/viam.robot.v1.RobotService/SendSessionHeartbeat",
    ]
)


class SessionsClient:
    """
    A Session allows a client to express that it is actively connected and
    supports stopping actuating components when it's not.
    """

    _current_id: str = ""
    _disabled: bool = False
    _supported: Optional[bool] = None
    _heartbeat_interval: Optional[timedelta] = None
    _heartbeat_task: Optional[Future[asyncio.Task]] = None

    def __init__(self, channel: Channel, address: str, dial_options: Optional[DialOptions], *, disabled: bool = False):
        self.channel = channel
        self.client = RobotServiceStub(channel)
        self._disabled = disabled
        self._should_reset = Value("b", False)

        self._address = address
        self._dial_options = dial_options

        listen(self.channel, SendRequest, self._send_request)
        listen(self.channel, RecvTrailingMetadata, self._recv_trailers)

    def reset(self):
        LOGGER.debug("resetting session")
        self._supported = None
        self._should_reset.value = True

    async def _send_request(self, event: SendRequest):
        if self._disabled:
            return

        if event.method_name in EXEMPT_METADATA_METHODS:
            return

        event.metadata.update(await self.metadata)

    async def _recv_trailers(self, event: RecvTrailingMetadata):
        if event.status == Status.INVALID_ARGUMENT and event.status_message == "SESSION_EXPIRED":
            LOGGER.debug("Session expired")
            self.reset()

    @property
    async def metadata(self) -> _MetadataLike:
        if self._disabled:
            return self._metadata
        if self._supported is not None:
            return self._metadata

        request = StartSessionRequest(resume=self._current_id)

        try:
            response = await self.client.StartSession(request)
        except GRPCError as error:
            if error.status == Status.UNIMPLEMENTED:
                self._supported = False
                return self._metadata
            else:
                raise

        if response is None:
            raise GRPCError(status=Status.INTERNAL, message="Expected response to start session")

        if response.heartbeat_window is None:
            raise GRPCError(status=Status.INTERNAL, message="Expected heartbeat window in response to start session")

        self._supported = True
        self._heartbeat_interval = response.heartbeat_window.ToTimedelta()
        self._current_id = response.id

        # tick once to ensure heartbeats are supported
        try:
            await _heartbeat_tick(self.client, self._current_id)
        except Exception:
            self.reset()

        if self._supported:
            # We send heartbeats slightly faster than the interval window to
            # ensure that we don't fall outside of it and expire the session.
            wait = self._heartbeat_interval.total_seconds() / 5

            p = ProcessPoolExecutor(initializer=_init_process, initargs=(self._should_reset, logging.LOG_LEVEL))
            p.submit(_start_heartbeat_process, self._address, self._dial_options, self._current_id, wait)

        return self._metadata

    @property
    def _metadata(self) -> _MetadataLike:
        if self._supported and self._current_id != "":
            return {SESSION_METADATA_KEY: self._current_id}

        return {}


def _init_process(args, level):
    global should_restart
    should_restart = args
    logging.setLevel(level)


def _start_heartbeat_process(address: str, dial_options: DialOptions | None, id: str, wait: float):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(heartbeat_process(address, dial_options, id, wait))


async def _heartbeat_tick(client: RobotServiceStub, id: str):
    request = SendSessionHeartbeatRequest(id=id)

    try:
        await client.SendSessionHeartbeat(request)
    except (GRPCError, StreamTerminatedError):
        LOGGER.debug("Heartbeat terminated", exc_info=True)
        # should reset, not raise
        raise
    else:
        LOGGER.debug("Sent heartbeat successfully")


async def heartbeat_process(address: str, dial_options: DialOptions | None, id: str, wait: float):
    if dial_options is not None:
        dial_options.disable_webrtc = True
    channel = await dial(address=address, options=dial_options)
    client = RobotServiceStub(channel.channel)
    while not should_restart.value:
        await asyncio.sleep(wait)
        await _heartbeat_tick(client, id)

    # reset shared var
    should_restart.value = False
