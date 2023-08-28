import asyncio
import socket
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value
from multiprocessing.sharedctypes import Synchronized

import pytest
from grpclib import GRPCError, Status
from grpclib.server import Server as GRPCServer
from grpclib.testing import ChannelFor

from viam.errors import MethodNotImplementedError
from viam.rpc.dial import DialOptions, dial
from viam.sessions_client import SESSION_METADATA_KEY, SessionsClient, _SupportedState

from .mocks.robot import MockRobot


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
        assert client._supported.value == _SupportedState.UNKNOWN


@pytest.mark.asyncio
async def test_sessions_error():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None)

        with pytest.raises(GRPCError) as e_info:
            assert await client.metadata == {}

        assert e_info.value.status == Status.UNKNOWN


@pytest.mark.asyncio
async def test_sessions_not_supported():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None)
        client._supported.value = _SupportedState.FALSE
        assert await client.metadata == {}
        assert client._supported.value == _SupportedState.FALSE


@pytest.mark.asyncio
async def test_sessions_not_implemented(service_without_session: MockRobot):
    async with ChannelFor([service_without_session]) as channel:
        client = SessionsClient(channel, "", None)
        assert await client.metadata == {}
        assert client._supported.value == _SupportedState.FALSE


@pytest.mark.asyncio
async def test_sessions_heartbeat_disconnect(service_without_heartbeat: MockRobot):
    async with ChannelFor([service_without_heartbeat]) as channel:
        client = SessionsClient(channel, "", None)
        assert await client.metadata == {}
        assert client._supported.value == _SupportedState.UNKNOWN


async def run_server(sock: socket.socket):
    server = GRPCServer([MockRobot(heartbeat_count)])
    await server.start(sock=sock)
    await asyncio.sleep(3)
    server.close()


def run_server_in_process(sock: socket.socket):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_server(sock))


def _init_process(count: Synchronized):
    global heartbeat_count
    heartbeat_count = count


@pytest.mark.asyncio
async def test_sessions_heartbeat_thread_blocked():
    sock = socket.socket()
    sock.bind(("", 0))
    count = Value("b", 0)

    p = ProcessPoolExecutor(initializer=_init_process, initargs=(count,))
    p.submit(run_server_in_process, sock)

    port = sock.getsockname()[1]
    addr = f"localhost:{port}"
    options = DialOptions(disable_webrtc=True, insecure=True)
    channel = await dial(address=addr, options=options)

    client = SessionsClient(channel.channel, addr, options)
    assert await client.metadata == {SESSION_METADATA_KEY: MockRobot.SESSION_ID}

    assert client._supported.value == _SupportedState.TRUE
    assert client._heartbeat_interval and client._heartbeat_interval.total_seconds() == MockRobot.HEARTBEAT_INTERVAL
    assert client._current_id == MockRobot.SESSION_ID
    time.sleep(3)

    assert count.value >= 5


@pytest.mark.asyncio
async def test_sessions_disabled(service: MockRobot):
    async with ChannelFor([service]) as channel:
        client = SessionsClient(channel, "", None, disabled=True)
        assert await client.metadata == {}
        assert client._supported.value == _SupportedState.UNKNOWN
        assert not client._heartbeat_interval
