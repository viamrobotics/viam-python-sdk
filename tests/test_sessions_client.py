import asyncio
from datetime import timedelta

import pytest
from google.protobuf.duration_pb2 import Duration
from grpclib import GRPCError, Status
from grpclib.server import Stream
from grpclib.testing import ChannelFor

from viam.proto.robot import SendSessionHeartbeatRequest, SendSessionHeartbeatResponse, StartSessionRequest, StartSessionResponse
from viam.resource.manager import ResourceManager
from viam.robot.service import RobotService
from viam.sessions_client import SessionsClient, SESSION_METADATA_KEY

SESSION_ID = "sid"
HEARTBEAT_INTERVAL = 2


@pytest.fixture(scope="function")
def service() -> RobotService:
    async def StartSession(stream: Stream[StartSessionRequest, StartSessionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        heartbeat_window = Duration()
        heartbeat_window.FromTimedelta(timedelta(seconds=HEARTBEAT_INTERVAL))
        response = StartSessionResponse(id=SESSION_ID, heartbeat_window=heartbeat_window)
        await stream.send_message(response)

    async def SendSessionHeartbeat(stream: Stream[SendSessionHeartbeatRequest, SendSessionHeartbeatResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = SendSessionHeartbeatResponse()
        await stream.send_message(response)

    manager = ResourceManager([])
    service = RobotService(manager)
    service.StartSession = StartSession
    service.SendSessionHeartbeat = SendSessionHeartbeat

    return service


@pytest.fixture(scope="function")
def service_without_session(service: RobotService) -> RobotService:
    del service.StartSession
    return service


@pytest.fixture(scope="function")
def service_without_heartbeat(service: RobotService) -> RobotService:
    del service.SendSessionHeartbeat
    return service


@pytest.mark.asyncio
async def test_init_client():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel)
        assert client.session_id == ""
        assert client.supported is None


@pytest.mark.asyncio
async def test_sessions_error():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel)

        with pytest.raises(GRPCError) as e_info:
            assert await client.metadata == {}

        assert e_info.value.status == Status.UNKNOWN


@pytest.mark.asyncio
async def test_sessions_not_supported():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel)
        client._supported = False
        assert await client.metadata == {}
        assert client.supported is False


@pytest.mark.asyncio
async def test_sessions_not_implemented(service_without_session: RobotService):
    async with ChannelFor([service_without_session]) as channel:
        client = SessionsClient(channel)
        assert await client.metadata == {}
        assert client.supported is False


@pytest.mark.asyncio
async def test_sessions_heartbeat_disconnect(service_without_heartbeat: RobotService):
    async with ChannelFor([service_without_heartbeat]) as channel:
        client = SessionsClient(channel)
        assert await client.metadata == {}
        assert client.supported is None
        # TODO: reset everything else too?


@pytest.mark.asyncio
async def test_sessions_heartbeat(service: RobotService):
    async with ChannelFor([service]) as channel:
        client = SessionsClient(channel)
        assert await client.metadata == {SESSION_METADATA_KEY: SESSION_ID}
        assert client.supported
        assert client._heartbeat_interval and client._heartbeat_interval.total_seconds() == HEARTBEAT_INTERVAL
        assert client.session_id == SESSION_ID

        # TODO: remove this sleep!
        await asyncio.sleep(HEARTBEAT_INTERVAL)
