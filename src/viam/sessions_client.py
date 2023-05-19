import asyncio
from datetime import timedelta
from threading import Timer
from typing import Optional

from grpclib import Status
from grpclib.client import Channel
from grpclib.exceptions import GRPCError, StreamTerminatedError
from grpclib.metadata import _MetadataLike

from viam import logging
from viam.proto.robot import RobotServiceStub, SendSessionHeartbeatRequest, StartSessionRequest, StartSessionResponse

LOGGER = logging.getLogger(__name__)


async def delay(coro, seconds):
    await asyncio.sleep(seconds)
    await coro


class SessionsClient:
    """
    A Session allows a client to express that it is actively connected and
    supports stopping actuating components when it's not.
    """

    _current_id: str = ""
    _supported: Optional[bool] = None
    _heartbeat_interval: Optional[timedelta] = None

    def __init__(self, channel: Channel):
        self.channel = channel
        self.client = RobotServiceStub(channel)

    @property
    def session_id(self):
        return self._current_id

    @property
    def supported(self):
        return self._supported

    @property
    async def metadata(self) -> _MetadataLike:
        if self._supported is False:
            return await self._metadata

        request = StartSessionRequest(resume=self.session_id)
        response: Optional[StartSessionResponse] = None
        try:
            response = await self.client.StartSession(request)
        except GRPCError as error:
            if error.status == Status.UNIMPLEMENTED:
                self._supported = False
            else:
                raise

        if self._supported is False:
            return await self._metadata

        if response is None:
            raise GRPCError(status=Status.INTERNAL, message="expected response to start session")

        if response.heartbeat_window is None:
            raise GRPCError(status=Status.INTERNAL, message="expected heartbeat window in response to start session")

        self._supported = True
        self._heartbeat_interval = response.heartbeat_window.ToTimedelta()
        self._current_id = response.id

        await self._heartbeat_tick()

        return await self._metadata

    async def _heartbeat_tick(self):
        request = SendSessionHeartbeatRequest(id=self.session_id)

        if self._heartbeat_interval is None:
            raise GRPCError(status=Status.INTERNAL, message="expected heartbeat window in response to start session")

        try:
            await self.client.SendSessionHeartbeat(request)
            LOGGER.debug("got heartbeat")
        except (GRPCError, StreamTerminatedError):
            # reset
            self._supported = None
        else:
            wait = self._heartbeat_interval.total_seconds()
            asyncio.create_task(delay(self._heartbeat_tick(), wait), name="heartbeat")

    @property
    async def _metadata(self) -> _MetadataLike:
        if self._supported and self.session_id != "":
            return {"viam-sid": self.session_id}

        return {}
