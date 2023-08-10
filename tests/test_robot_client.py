import pytest

from grpclib.testing import ChannelFor
from google.protobuf.duration_pb2 import Duration

from viam.app.app_client import AppClient
from viam.proto.app.robot import (
    RobotConfig,
)
from viam.proto.app import (
    LogEntry
)

from .mocks.services import MockRobot

METADATA = {"key": "value"}
ID = "id"

CONFIG = RobotConfig()
CERT = "cert"
KEY = "key"

HOST = "host"
LEVEL = "level"
LOGGER_NAME = "logger_name"
MESSAGE = "message"
STACK = "stack"
LOG = LogEntry(
    host=HOST,
    level=LEVEL,
    time=None,
    logger_name=LOGGER_NAME,
    message=MESSAGE,
    caller=None,
    stack=STACK,
    fields=None
)
LOGS = [LOG]

NEEDS_RESTART = True
DURATION = Duration(
    seconds=1,
    nanos=1
)


@pytest.fixture(scope="function")
def service() -> MockRobot:
    return MockRobot(config=CONFIG, cert=CERT, key=KEY, needs_restart=NEEDS_RESTART, duration=DURATION)


class TestClient:
    @pytest.mark.asyncio
    async def test_config(self, service: MockRobot):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            config = await client.config(robot_part_id=ID)
            assert config == CONFIG
            assert service.robot_part_id == ID

    @pytest.mark.asyncio
    async def test_certificate(self, service: MockRobot):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            cert, key = await client.certificate(robot_part_id=ID)
            assert cert == CERT
            assert key == KEY
            assert service.robot_part_id == ID

    @pytest.mark.asyncio
    async def test_log(self, service: MockRobot):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.log(robot_part_id=ID, logs=LOGS)
            assert service.robot_part_id == ID
            assert service.logs == LOGS

    @pytest.mark.asyncio
    async def test_needs_restart(self, service: MockRobot):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            needs_restart, duration = await client.needs_restart(robot_part_id=ID)
            assert needs_restart == NEEDS_RESTART
            assert duration == DURATION
            assert service.robot_part_id == ID
