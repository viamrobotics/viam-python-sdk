import pytest

from grpclib.testing import ChannelFor

from viam.app.app_client import AppClient
from viam.proto.app.robot import (
    RobotConfig,
)

from .mocks.services import MockRobot

METADATA = {"key": "value"}
ID = "id"

CONFIG = RobotConfig()
CERT = "cert"
KEY = "key"


@pytest.fixture(scope="function")
def service() -> MockRobot:
    return MockRobot(config=CONFIG, cert=CERT, key=KEY)


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
