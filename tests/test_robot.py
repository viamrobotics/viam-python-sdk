import asyncio

import pytest
from grpclib.testing import ChannelFor
from viam.components.arm import Arm
from viam.components.resource_manager import ResourceManager
from viam.errors import (ComponentNotFoundError, ServiceNotImplementedError,
                         ViamError)
from viam.proto.api.common import ResourceName
from viam.proto.api.robot import (ResourceNamesRequest, ResourceNamesResponse,
                                  RobotServiceStub)
from viam.robot.client import RobotClient
from viam.robot.service import RobotService
from viam.services import ServiceType

from .mocks.components import MockArm, MockCamera, MockMotor, MockSensor

RESOURCE_NAMES = [
    ResourceName(
        namespace='rdk',
        type='service',
        subtype='status',
    ),
    ResourceName(
        namespace='rdk',
        type='component',
        subtype='arm',
        name='arm1'
    ),
    ResourceName(
        namespace='rdk',
        type='component',
        subtype='camera',
        name='camera1'
    ),
    ResourceName(
        namespace='rdk',
        type='component',
        subtype='motor',
        name='motor1'
    ),
]


@pytest.fixture(scope='function')
def service() -> RobotService:
    resources = [
        MockArm(name='arm1'),
        MockCamera(name='camera1'),
        MockMotor(name='motor1'),
    ]

    manager = ResourceManager(resources)
    return RobotService(manager)


class TestRobotService:
    @pytest.mark.asyncio
    async def test_resource_names(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = RobotServiceStub(channel)
            response: ResourceNamesResponse = await client.ResourceNames(ResourceNamesRequest())
            assert list(response.resources) == RESOURCE_NAMES


class TestRobotClient:

    @pytest.mark.asyncio
    async def test_refresh(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert client._resource_names == RESOURCE_NAMES

            service.manager.register(MockSensor('sensor1'))
            await client.refresh()
            assert client._resource_names == RESOURCE_NAMES + [
                MockSensor.get_resource_name('sensor1')
            ]

    @pytest.mark.asyncio
    async def test_refresh_task(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert client._refresh_task is None

            client = await RobotClient.with_channel(channel, RobotClient.Options(refresh_interval=100))
            assert client._refresh_task is not None
            await client.close()

    @pytest.mark.asyncio
    async def test_close(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options(refresh_interval=100))
            assert client._channel._connected is True
            assert client._refresh_task is not None and client._refresh_task.cancelled() is False

            await client.close()
            assert client._channel._connected is True  # Robots created with `with_channel` do not close Channels automatically
            with pytest.raises(asyncio.CancelledError):
                await client._refresh_task

    @pytest.mark.asyncio
    async def test_resource_names(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert client.resource_names == RESOURCE_NAMES

            service.manager.register(MockSensor('sensor1'))
            await client.refresh()
            assert client._resource_names == RESOURCE_NAMES + [
                MockSensor.get_resource_name('sensor1')
            ]

    @pytest.mark.asyncio
    async def test_get_component(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            component = client.get_component(MockArm.get_resource_name('arm1'))
            assert isinstance(component, Arm)

            with pytest.raises(ComponentNotFoundError):
                client.get_component(MockArm.get_resource_name('arm2'))

            with pytest.raises(ViamError):
                client.get_component(
                    ResourceName(
                        namespace='rdk',
                        type='service',
                        subtype='vision',
                    )
                )

            # Test BaseComponent.from_robot(...)
            component = MockArm.from_robot(client, 'arm1')
            assert isinstance(component, Arm)

            with pytest.raises(ComponentNotFoundError):
                MockArm.from_robot(client, 'arm2')

    @pytest.mark.asyncio
    async def test_get_service(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            with pytest.raises(ServiceNotImplementedError):
                client.get_service(ServiceType.FRAME_SYSTEM)
