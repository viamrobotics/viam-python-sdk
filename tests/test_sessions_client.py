from asyncio import futures
import asyncio
import socket
import time
from concurrent.futures import ProcessPoolExecutor

import pytest
from grpclib import GRPCError, Status
from grpclib.server import Server as GRPCServer
from grpclib.testing import ChannelFor

from viam.errors import MethodNotImplementedError
from viam.sessions_client import SESSION_METADATA_KEY, SessionsClient

from .mocks.robot import MockRobot
from viam.rpc.dial import DialOptions, dial


@pytest.fixture(scope="function")
def service() -> MockRobot:
    return MockRobot()


@pytest.fixture(scope="function")
def service_without_session(service: MockRobot) -> MockRobot:
    async def StartSession(stream) -> None:
        raise MethodNotImplementedError("StartSession").grpc_error

    service.StartSession = StartSession
    return service


@pytest.fixture(scope="function")
def service_without_heartbeat(service: MockRobot) -> MockRobot:
    async def SendSessionHeartbeat(stream) -> None:
        raise MethodNotImplementedError("SendSessionHeartbeat").grpc_error

    service.SendSessionHeartbeat = SendSessionHeartbeat
    return service


@pytest.mark.asyncio
async def test_init_client():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None)
        assert client._current_id == ""
        assert client._supported.value == 0


@pytest.mark.asyncio
async def test_sessions_error():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None)

        with pytest.raises(GRPCError) as e_info:
            assert await client.metadata == {}

        assert e_info.value.status == Status.UNKNOWN


async def start_server_in_background(sock: socket.socket):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(GRPCServer([MockRobot()]).start(sock=sock))


@pytest.mark.asyncio
async def test_sessions_not_supported():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None)
        client._supported.value = 2
        assert await client.metadata == {}
        assert client._supported.value == 2


@pytest.mark.asyncio
async def test_sessions_not_implemented(service_without_session: MockRobot):
    async with ChannelFor([service_without_session]) as channel:
        client = SessionsClient(channel, "", None)
        assert await client.metadata == {}
        assert client._supported.value == 2


@pytest.mark.asyncio
async def test_sessions_heartbeat_disconnect(service_without_heartbeat: MockRobot):
    async with ChannelFor([service_without_heartbeat]) as channel:
        client = SessionsClient(channel, "", None)
        assert await client.metadata == {}
        assert client._supported.value == 0


@pytest.mark.asyncio
async def test_sessions_heartbeat(service: MockRobot):
    sock = socket.socket()
    sock.bind(("", 0))

    p = ProcessPoolExecutor()
    p.submit(start_server_in_background, sock)
    print("gg")
    # start
    port = sock.getsockname()[1]

    channel = await dial(address=f"localhost:{port}", options=DialOptions(disable_webrtc=True))

    client = SessionsClient(channel.channel, f"localhost:{port}", None)
    assert await client.metadata == {SESSION_METADATA_KEY: MockRobot.SESSION_ID}
    assert client._supported
    assert client._heartbeat_interval and client._heartbeat_interval.total_seconds() == MockRobot.HEARTBEAT_INTERVAL
    assert client._current_id == MockRobot.SESSION_ID
    time.sleep(3)
    assert service.heartbeat_count == 3


@pytest.mark.asyncio
async def test_sessions_disabled(service: MockRobot):
    async with ChannelFor([service]) as channel:
        client = SessionsClient(channel, "", None, disabled=True)
        assert await client.metadata == {}
        assert client._supported.value == 0
        assert not client._heartbeat_interval
