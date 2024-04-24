import asyncio
from copy import deepcopy
from datetime import timedelta
from enum import IntEnum
from threading import Lock, Thread
from typing import Optional

from grpclib import Status
from grpclib.client import Channel
from grpclib.events import RecvTrailingMetadata, SendRequest, listen
from grpclib.exceptions import GRPCError, StreamTerminatedError
from grpclib.metadata import _MetadataLike

from viam import logging
from viam.proto.robot import RobotServiceStub, SendSessionHeartbeatRequest, StartSessionRequest, StartSessionResponse
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


class _SupportedState(IntEnum):
    UNKNOWN = 0
    TRUE = 1
    FALSE = 2


class SessionsClient:
    """
    A Session allows a client to express that it is actively connected and
    supports stopping actuating components when it's not.
    """

    channel: Channel
    client: RobotServiceStub
    _address: str
    _dial_options: DialOptions
    _disabled: bool
    _lock: Lock
    _current_id: str
    _heartbeat_interval: Optional[timedelta]
    _supported: _SupportedState
    _thread: Optional[Thread]

    def __init__(self, channel: Channel, direct_dial_address: str, dial_options: Optional[DialOptions], *, disabled: bool = False):
        self.channel = channel
        self.client = RobotServiceStub(channel)
        self._address = direct_dial_address
        self._disabled = disabled
        self._dial_options = deepcopy(dial_options) if dial_options is not None else DialOptions()
        self._dial_options.disable_webrtc = True
        self._lock = Lock()
        self._current_id = ""
        self._heartbeat_interval = None
        self._supported = _SupportedState.UNKNOWN
        self._thread = None

        listen(self.channel, SendRequest, self._send_request)
        listen(self.channel, RecvTrailingMetadata, self._recv_trailers)

    def reset(self):
        with self._lock:
            self._reset()

    def _reset(self):
        LOGGER.debug("resetting session")
        self._supported = _SupportedState.UNKNOWN
        self._current_id = ""
        self._heartbeat_interval = None
        if self._thread is not None:
            try:
                self._thread.join(timeout=1)
            except RuntimeError:
                LOGGER.debug("failed to join session heartbeat thread")
            self._thread = None

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
        with self._lock:
            if self._disabled or self._supported != _SupportedState.UNKNOWN:
                return self._metadata

        request = StartSessionRequest(resume=self._current_id)
        try:
            response: StartSessionResponse = await self.client.StartSession(request)
        except GRPCError as error:
            if error.status == Status.UNIMPLEMENTED:
                with self._lock:
                    self._reset()
                    self._supported = _SupportedState.FALSE
                    return self._metadata
            else:
                raise

        if response is None:
            raise GRPCError(status=Status.INTERNAL, message="Expected response to start session")

        if response.heartbeat_window is None:
            raise GRPCError(status=Status.INTERNAL, message="Expected heartbeat window in response to start session")

        with self._lock:
            self._supported = _SupportedState.TRUE
            self._heartbeat_interval = response.heartbeat_window.ToTimedelta()
            self._current_id = response.id

        # tick once to ensure heartbeats are supported
        await self._heartbeat_tick(self.client)

        with self._lock:
            if self._thread is not None:
                self._reset()
            if self._supported == _SupportedState.TRUE:
                # We send heartbeats faster than the interval window to
                # ensure that we don't fall outside of it and expire the session.
                wait = self._heartbeat_interval.total_seconds() / 5

                self._thread = Thread(
                    name="heartbeat-thread",
                    target=asyncio.run,
                    args=(self._heartbeat_process(wait),),
                    daemon=True,
                )
                self._thread.start()

            return self._metadata

    async def _heartbeat_tick(self, client: RobotServiceStub):
        with self._lock:
            if not self._current_id:
                LOGGER.debug("Failed to send heartbeat, session client reset")
                return
            request = SendSessionHeartbeatRequest(id=self._current_id)

        try:
            await client.SendSessionHeartbeat(request)
        except (GRPCError, StreamTerminatedError):
            LOGGER.debug("Heartbeat terminated", exc_info=True)
            self.reset()
        else:
            LOGGER.debug("Sent heartbeat successfully")

    async def _heartbeat_process(self, wait: float):
        channel = await dial(address=self._address, options=self._dial_options)
        client = RobotServiceStub(channel.channel)
        while True:
            with self._lock:
                if self._supported != _SupportedState.TRUE:
                    return
            await self._heartbeat_tick(client)
            await asyncio.sleep(wait)

    @property
    def _metadata(self) -> _MetadataLike:
        if self._supported == _SupportedState.TRUE and self._current_id != "":
            return {SESSION_METADATA_KEY: self._current_id}

        return {}
