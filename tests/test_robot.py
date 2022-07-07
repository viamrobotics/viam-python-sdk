import asyncio

import pytest
from google.protobuf.struct_pb2 import Struct, Value
from grpclib.server import Stream
from grpclib.testing import ChannelFor
from viam.components.arm import Arm
from viam.components.resource_manager import ResourceManager
from viam.errors import (ComponentNotFoundError, ServiceNotImplementedError,
                         ViamError)
from viam.proto.api.common import Pose, PoseInFrame, ResourceName
from viam.proto.api.component.arm import JointPositions
from viam.proto.api.component.arm import Status as ArmStatus
from viam.proto.api.component.motor import Status as MotorStatus
from viam.proto.api.robot import (DiscoverComponentsRequest,
                                  DiscoverComponentsResponse, Discovery,
                                  DiscoveryQuery, FrameSystemConfig,
                                  FrameSystemConfigRequest,
                                  FrameSystemConfigResponse, GetStatusRequest,
                                  GetStatusResponse, ResourceNamesRequest,
                                  ResourceNamesResponse, RobotServiceStub,
                                  Status, TransformPoseRequest,
                                  TransformPoseResponse)
from viam.robot.client import RobotClient
from viam.robot.service import RobotService
from viam.services import ServiceType
from viam.utils import message_to_struct

from .mocks.components import MockArm, MockCamera, MockMotor, MockSensor

RESOURCE_NAMES = [
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

ARM_STATUS = Status(
    name=ResourceName(
        namespace='rdk',
        type='component',
        subtype='arm',
        name='arm1'
    ),
    status=message_to_struct(ArmStatus(
        end_position=Pose(
            x=1,
            y=2,
            z=3,
            o_x=2,
            o_y=3,
            o_z=4,
            theta=20,
        ),
        joint_positions=JointPositions(degrees=[0, 0, 0, 0, 0, 0]),
        is_moving=False
    ))
)

CAMERA_STATUS = Status(
    name=ResourceName(
        namespace='rdk',
        type='component',
        subtype='camera',
        name='camera1'
    ),
    status=Struct()
)

STATUSES = [
    ARM_STATUS,
    CAMERA_STATUS,
    Status(
        name=ResourceName(
            namespace='rdk',
            type='component',
            subtype='motor',
            name='motor1'
        ),
        status=message_to_struct(MotorStatus(
            is_powered=False,
            position=0,
            position_reporting=True,
            is_moving=False
        ))
    ),
]

CONFIG_RESPONSE = [
    FrameSystemConfig(
        name='config0',
        pose_in_parent_frame=PoseInFrame(
            reference_frame='reference0',
            pose=Pose(
                x=1,
                y=2,
                z=3,
                o_x=2,
                o_y=3,
                o_z=4,
                theta=20
            )
        ),
        model_json=b'some fake json'
    ),
    FrameSystemConfig(
        name='config1',
        pose_in_parent_frame=PoseInFrame(
            reference_frame='reference1',
            pose=Pose(
                x=2,
                y=3,
                z=4,
                o_x=3,
                o_y=4,
                o_z=5,
                theta=21
            )
        ),
        model_json=b'some fake json part 2'
    ),
]

TRANSFORM_RESPONSE = PoseInFrame(
    reference_frame='arm',
    pose=Pose(
        x=1,
        y=2,
        z=3,
        o_x=2,
        o_y=3,
        o_z=4,
        theta=20
    )
)

DISCOVERY_QUERY = DiscoveryQuery(
    subtype='camera',
    model='webcam'
)

DISCOVERY_RESPONSE = [
    Discovery(
        query=DISCOVERY_QUERY,
        results=Struct(fields={
            'foo': Value(string_value="bar"),
            'one': Value(number_value=1),
        })
    )
]


@pytest.fixture(scope='function')
def service() -> RobotService:
    resources = [
        MockArm(name='arm1'),
        MockCamera(name='camera1'),
        MockMotor(name='motor1'),
    ]

    async def Config(
        stream: Stream[FrameSystemConfigRequest, FrameSystemConfigResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = FrameSystemConfigResponse(frame_system_configs=CONFIG_RESPONSE)
        await stream.send_message(response)

    async def TransformPose(
        stream: Stream[TransformPoseRequest, TransformPoseResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = TransformPoseResponse(pose=TRANSFORM_RESPONSE)
        await stream.send_message(response)

    async def DiscoverComponents(
        stream: Stream[DiscoverComponentsRequest, DiscoverComponentsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = DiscoverComponentsResponse(discovery=DISCOVERY_RESPONSE)
        await stream.send_message(response)

    manager = ResourceManager(resources)
    service = RobotService(manager)
    service.FrameSystemConfig = Config
    service.TransformPose = TransformPose
    service.DiscoverComponents = DiscoverComponents
    return service


class TestRobotService:
    @pytest.mark.asyncio
    async def test_resource_names(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = RobotServiceStub(channel)
            response: ResourceNamesResponse = await client.ResourceNames(ResourceNamesRequest())
            assert list(response.resources) == RESOURCE_NAMES

    @pytest.mark.asyncio
    async def test_get_status(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = RobotServiceStub(channel)
            response: GetStatusResponse = await client.GetStatus(GetStatusRequest())
            assert list(response.status) == STATUSES

            request = GetStatusRequest(resource_names=[
                MockArm.get_resource_name('arm1'),
                MockCamera.get_resource_name('camera1')
            ])
            response: GetStatusResponse = await client.GetStatus(request)
            assert list(response.status) == [ARM_STATUS, CAMERA_STATUS]


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
    async def test_get_status(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            statuses = await client.get_status()
            assert statuses == STATUSES

            statuses = await client.get_status([
                MockArm.get_resource_name('arm1'),
                MockCamera.get_resource_name('camera1')
            ])
            assert statuses == [ARM_STATUS, CAMERA_STATUS]

    @ pytest.mark.asyncio
    async def test_get_service(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            with pytest.raises(ServiceNotImplementedError):
                client.get_service(ServiceType.VISION)

    @ pytest.mark.asyncio
    async def test_get_frame_system_config(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            configs = await client.get_frame_system_config()
            assert configs == CONFIG_RESPONSE

    @ pytest.mark.asyncio
    async def test_transform_pose(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            pose = await client.transform_pose(PoseInFrame(), 'some dest')
            assert pose == TRANSFORM_RESPONSE

    @ pytest.mark.asyncio
    async def test_discover_components(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            discoveries = await client.discover_components([DISCOVERY_QUERY])
            assert discoveries == DISCOVERY_RESPONSE
