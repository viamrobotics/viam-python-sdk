import asyncio
import sys
from datetime import timedelta
from typing import Optional

from grpclib import Status
from grpclib.client import Channel
from grpclib.events import RecvTrailingMetadata, SendRequest, listen
from grpclib.exceptions import GRPCError, StreamTerminatedError
from grpclib.metadata import _MetadataLike

from viam import _TASK_PREFIX, logging
from viam.proto.robot import RobotServiceStub, SendSessionHeartbeatRequest, StartSessionRequest, StartSessionResponse

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


def loop_kwargs():
    if sys.version_info <= (3, 9):
        return {"loop": asyncio.get_running_loop()}
    return {}


class SessionsClient:
    """
    A Session allows a client to express that it is actively connected and
    supports stopping actuating components when it's not.
    """

    _current_id: str = ""
    _disabled: bool = False
    _supported: Optional[bool] = None
    _heartbeat_interval: Optional[timedelta] = None

    def __init__(self, channel: Channel, *, disabled: bool = False):
        self.channel = channel
        self.client = RobotServiceStub(channel)
        self._disabled = disabled
        self._lock = asyncio.Lock(**loop_kwargs())

        listen(self.channel, SendRequest, self._send_request)
        listen(self.channel, RecvTrailingMetadata, self._recv_trailers)

    def reset(self):
        if self._lock.locked():
            return

        LOGGER.debug("resetting session")
        self._supported = None

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

        if self._supported:
            return self._metadata

        async with self._lock:
            if self._supported is False:
                return self._metadata

            request = StartSessionRequest(resume=self._current_id)
            response: Optional[StartSessionResponse] = None

            try:
                response = await self.client.StartSession(request)
            except GRPCError as error:
                if error.status == Status.UNIMPLEMENTED:
                    self._supported = False
                    return self._metadata
                else:
                    raise
            else:
                if response is None:
                    raise GRPCError(status=Status.INTERNAL, message="Expected response to start session")

                if response.heartbeat_window is None:
                    raise GRPCError(status=Status.INTERNAL, message="Expected heartbeat window in response to start session")

                self._supported = True
                self._heartbeat_interval = response.heartbeat_window.ToTimedelta()
                self._current_id = response.id

        # tick once to ensure heartbeats are supported
        await self._heartbeat_tick()

        if self._supported:
            # We send heartbeats slightly faster than the interval window to
            # ensure that we don't fall outside of it and expire the session.
            wait = self._heartbeat_interval.total_seconds() / 5
            asyncio.create_task(self._heartbeat_task(wait), name=f"{_TASK_PREFIX}-heartbeat")

        return self._metadata

    async def _heartbeat_task(self, wait: float):
        while self._supported:
            await asyncio.sleep(wait)
            await self._heartbeat_tick()

    async def _heartbeat_tick(self):
        if not self._supported:
            return

        while self._lock.locked():
            pass

        request = SendSessionHeartbeatRequest(id=self._current_id)

        if self._heartbeat_interval is None:
            raise GRPCError(status=Status.INTERNAL, message="Expected heartbeat window in response to start session")

        try:
            await self.client.SendSessionHeartbeat(request)
        except (GRPCError, StreamTerminatedError):
            LOGGER.debug("Heartbeat terminated", exc_info=True)
            self.reset()
        else:
            LOGGER.debug("Sent heartbeat successfully")

    @property
    def _metadata(self) -> _MetadataLike:
        if self._supported and self._current_id != "":
            return {SESSION_METADATA_KEY: self._current_id}

        return {}
