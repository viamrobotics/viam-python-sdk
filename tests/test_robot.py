import pytest
from grpclib.testing import ChannelFor
from viam.components.resource_manager import ResourceManager
from viam.gen.proto.api.robot.v1.robot_grpc import RobotServiceStub
from viam.gen.proto.api.robot.v1.robot_pb2 import ConfigRequest, ConfigResponse

from viam.robot.service import RobotService


@pytest.mark.asyncio
async def test_config():
    service = RobotService(manager=ResourceManager(components=[]))
    async with ChannelFor([service]) as channel:
        client = RobotServiceStub(channel)
        request = ConfigRequest()
        response: ConfigResponse = await client.Config(request)
        assert response == ConfigResponse()
