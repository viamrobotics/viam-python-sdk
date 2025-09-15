import asyncio
import socket
import time
from concurrent.futures import ThreadPoolExecutor
from typing import List

import pytest
from grpclib import GRPCError, Status
from grpclib._typing import IServable
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


async def test_init_client():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None)
        assert client._current_id == ""
        assert client._supported == _SupportedState.UNKNOWN


async def test_sessions_error():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None)

        with pytest.raises(GRPCError) as e_info:
            assert await client.metadata == {}

        assert e_info.value.status == Status.UNKNOWN


async def test_sessions_not_supported():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None)
        client._supported = _SupportedState.FALSE
        assert await client.metadata == {}
        assert client._supported == _SupportedState.FALSE


async def test_sessions_not_implemented(service_without_session: MockRobot):
    async with ChannelFor([service_without_session]) as channel:
        client = SessionsClient(channel, "", None)
        assert await client.metadata == {}
        assert client._supported == _SupportedState.FALSE


async def test_sessions_heartbeat_disconnect(service_without_heartbeat: MockRobot):
    async with ChannelFor([service_without_heartbeat]) as channel:
        client = SessionsClient(channel, "", None)
        assert await client.metadata == {}
        assert client._supported == _SupportedState.UNKNOWN


async def _run_server(sock: socket.socket, handlers: List[IServable], shutdown_signal: asyncio.Event):
    server = GRPCServer(handlers=handlers)
    await server.start(sock=sock)
    # shutdown_signal.wait() seems to be bugged <3.9 and blocks the thread,
    # so have to do a bit of a busy wait here
    while not shutdown_signal.is_set():
        await asyncio.sleep(0.1)
    server.close()


async def test_sessions_heartbeat_thread_blocked():
    sock = socket.socket()
    sock.bind(("", 0))

    shutdown_signal = asyncio.Event()
    m = MockRobot()
    t = ThreadPoolExecutor()
    t.submit(asyncio.run, _run_server(sock, [m], shutdown_signal))

    await asyncio.sleep(0.5)

    port = sock.getsockname()[1]
    addr = f"localhost:{port}"
    options = DialOptions(disable_webrtc=True, insecure=True)
    channel = await dial(address=addr, options=options)

    client = SessionsClient(channel.channel, addr, options)
    t1 = asyncio.create_task(client.metadata)
    t2 = asyncio.create_task(client.metadata)

    await asyncio.gather(t1,t2)
    assert t1.result() == {SESSION_METADATA_KEY: MockRobot.SESSION_ID}
    assert t2.result() == {SESSION_METADATA_KEY: MockRobot.SESSION_ID}

    assert client._supported == _SupportedState.TRUE
    assert client._heartbeat_interval and client._heartbeat_interval.total_seconds() == MockRobot.HEARTBEAT_INTERVAL

    time.sleep(3)
    shutdown_signal.set()
    client.reset()
    assert m.heartbeat_count >= 5


async def test_sessions_disabled(service: MockRobot):
    async with ChannelFor([service]) as channel:
        client = SessionsClient(channel, "", None, disabled=True)
        assert await client.metadata == {}
        assert client._supported == _SupportedState.UNKNOWN
        assert not client._heartbeat_interval


async def test_safete_heartbeat_monitored():
    async with ChannelFor([]) as channel:
        client = SessionsClient(channel, "", None, disabled=True)
        is_monitored = client._is_safety_heartbeat_monitored("/viam.component.arm.v1.ArmService/MoveToPosition")
        assert is_monitored is True

        is_monitored = client._is_safety_heartbeat_monitored("/viam.component.camera.v1.CameraService/GetImage")
        assert is_monitored is False
