import asyncio
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


async def delay(coro, seconds):
    await asyncio.sleep(seconds)
    await coro


class SessionsClient:
    """
    A Session allows a client to express that it is actively connected and
    supports stopping actuating components when it's not.
    """

    _current_id: str = ""
    _disabled: bool = False
    _lock = asyncio.Lock()
    _supported: Optional[bool] = None
    _heartbeat_interval: Optional[timedelta] = None

    def __init__(self, channel: Channel, *, disabled: bool = False):
        self.channel = channel
        self.client = RobotServiceStub(channel)
        self._disabled = disabled

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

        if event.method_name in [self.client.StartSession.name]:
            return

        event.metadata.update(await self.metadata)

    async def _recv_trailers(self, event: RecvTrailingMetadata):
        if event.status == Status.INVALID_ARGUMENT and event.status_message == "SESSION_EXPIRED":
            LOGGER.debug("session expired")
            self.reset()

    @property
    def session_id(self):
        return self._current_id

    @property
    def supported(self):
        return self._supported

    @property
    async def metadata(self) -> _MetadataLike:
        if self._disabled:
            return self._metadata

        if self._supported:
            return self._metadata

        async with self._lock:
            if self._supported is False:
                return self._metadata

            request = StartSessionRequest(resume=self.session_id)
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
                    raise GRPCError(status=Status.INTERNAL, message="expected response to start session")

                if response.heartbeat_window is None:
                    raise GRPCError(status=Status.INTERNAL, message="expected heartbeat window in response to start session")

                self._supported = True
                self._heartbeat_interval = response.heartbeat_window.ToTimedelta()
                self._current_id = response.id

        await self._heartbeat_tick()

        return self._metadata

    async def _heartbeat_tick(self):
        if not self._supported:
            return

        while self._lock.locked():
            pass

        request = SendSessionHeartbeatRequest(id=self.session_id)

        if self._heartbeat_interval is None:
            raise GRPCError(status=Status.INTERNAL, message="expected heartbeat window in response to start session")

        try:
            await self.client.SendSessionHeartbeat(request)
        except (GRPCError, StreamTerminatedError):
            LOGGER.debug("heartbeat terminated", exc_info=True)
            self.reset()
        else:
            LOGGER.debug("sent heartbeat successfully")
            # We send heartbeats slightly faster than the interval window to
            # ensure that we don't fall outside of it and expire the session.
            wait = self._heartbeat_interval.total_seconds() / 5
            asyncio.create_task(delay(self._heartbeat_tick(), wait), name=f"{_TASK_PREFIX}-heartbeat")

    @property
    def _metadata(self) -> _MetadataLike:
        if self._supported and self.session_id != "":
            return {SESSION_METADATA_KEY: self.session_id}

        return {}
