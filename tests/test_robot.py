import pytest
from grpclib.testing import ChannelFor
from viam.components.resource_manager import ResourceManager
from viam.proto.api.robot import (ConfigRequest, ConfigResponse,
                                  RobotServiceStub)
from viam.robot.service import RobotService


@pytest.mark.asyncio
async def test_config():
    service = RobotService(manager=ResourceManager(components=[]))
    async with ChannelFor([service]) as channel:
        client = RobotServiceStub(channel)
        request = ConfigRequest()
        response: ConfigResponse = await client.Config(request)
        assert response == ConfigResponse()
