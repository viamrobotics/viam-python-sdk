from grpclib.client import Channel
import asyncio
from typing import Any, Dict, Optional, Tuple

import pytest
from google.protobuf.struct_pb2 import Struct, Value
from grpclib.exceptions import GRPCError
from grpclib.server import Stream
from grpclib.testing import ChannelFor

from viam.components.arm import Arm, KinematicsFileFormat
from viam.components.movement_sensor import MovementSensor
from viam.components.arm.client import ArmClient
from viam.components.motor import Motor
from viam.resource.manager import ResourceManager
from viam.errors import ResourceNotFoundError
from viam.proto.common import Pose, PoseInFrame, ResourceName, Transform, GeoPoint, Vector3, Orientation
from viam.proto.component.arm import JointPositions
from viam.proto.component.arm import Status as ArmStatus
from viam.proto.component.motor import Status as MotorStatus
from viam.proto.robot import (
    BlockForOperationRequest,
    BlockForOperationResponse,
    CancelOperationRequest,
    CancelOperationResponse,
    DiscoverComponentsRequest,
    DiscoverComponentsResponse,
    Discovery,
    DiscoveryQuery,
    FrameSystemConfig,
    FrameSystemConfigRequest,
    FrameSystemConfigResponse,
    GetOperationsRequest,
    GetOperationsResponse,
    GetStatusRequest,
    GetStatusResponse,
    Operation,
    ResourceNamesRequest,
    ResourceNamesResponse,
    RobotServiceStub,
    Status,
    StopAllRequest,
    StopExtraParameters,
    TransformPoseRequest,
    TransformPoseResponse,
)
from viam.resource.registry import Registry
from viam.resource.rpc_client_base import ResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, RESOURCE_TYPE_SERVICE
from viam.robot.client import RobotClient
from viam.robot.service import RobotService
from viam.services.motion.client import MotionClient
from viam.utils import dict_to_struct, message_to_struct, struct_to_message

from .mocks.components import MockArm, MockCamera, MockMotor, MockMovementSensor, MockSensor
from .mocks.services import MockMLModel

RESOURCE_NAMES = [
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="arm", name="arm1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="camera", name="camera1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="motor", name="motor1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="movement_sensor", name="movement_sensor1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="sensor", name="movement_sensor1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_SERVICE, subtype="mlmodel", name="mlmodel1"),
]

ARM_STATUS = ArmStatus(
    end_position=Pose(
        x=1,
        y=2,
        z=3,
        o_x=2,
        o_y=3,
        o_z=4,
        theta=20,
    ),
    joint_positions=JointPositions(values=[0, 0, 0, 0, 0, 0]),
    is_moving=False,
)

ARM_STATUS_MSG = Status(
    name=ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="arm", name="arm1"),
    status=message_to_struct(ARM_STATUS),
)

CAMERA_STATUS_MSG = Status(
    name=ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="camera", name="camera1"), status=Struct()
)

STATUSES = [
    ARM_STATUS_MSG,
    CAMERA_STATUS_MSG,
    Status(
        name=ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="motor", name="motor1"),
        status=message_to_struct(MotorStatus(is_powered=False, position=0, is_moving=False)),
    ),
    Status(
        name=ResourceName(
            namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="movement_sensor", name="movement_sensor1"
        ),
        status=Struct(),
    ),
    Status(
        name=ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_SERVICE, subtype="mlmodel", name="mlmodel1"),
        status=Struct(),
    ),
]

CONFIG_RESPONSE = [
    FrameSystemConfig(
        frame=Transform(
            reference_frame="frame0",
            pose_in_observer_frame=PoseInFrame(reference_frame="reference0", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)),
        )
    ),
    FrameSystemConfig(
        frame=Transform(
            reference_frame="frame1",
            pose_in_observer_frame=PoseInFrame(reference_frame="reference1", pose=Pose(x=2, y=3, z=4, o_x=3, o_y=4, o_z=5, theta=21)),
        )
    ),
]

TRANSFORM_RESPONSE = PoseInFrame(reference_frame="arm", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))

DISCOVERY_QUERY = DiscoveryQuery(subtype="camera", model="webcam")

DISCOVERY_RESPONSE = [
    Discovery(
        query=DISCOVERY_QUERY,
        results=Struct(
            fields={
                "foo": Value(string_value="bar"),
                "one": Value(number_value=1),
            }
        ),
    )
]

OPERATION_ID = "abc"

OPERATIONS_RESPONSE = [Operation(id=OPERATION_ID)]


@pytest.fixture(scope="function")
def service() -> RobotService:
    resources = [
        MockArm(name="arm1"),
        MockCamera(name="camera1"),
        MockMotor(name="motor1"),
        MockMovementSensor(
            name="movement_sensor1",
            coordinates=GeoPoint(latitude=40.664679865782624, longitude=-73.97668056188789),
            altitude=15,
            lin_vel=Vector3(x=1, y=2, z=3),
            ang_vel=Vector3(x=1, y=2, z=3),
            lin_acc=Vector3(x=1, y=2, z=3),
            heading=182,
            orientation=Orientation(o_x=1, o_y=2, o_z=3, theta=5),
            properties=MovementSensor.Properties(
                linear_acceleration_supported=False,
                linear_velocity_supported=False,
                angular_velocity_supported=True,
                orientation_supported=False,
                position_supported=True,
                compass_heading_supported=False,
            ),
            accuracy={"foo": 0.1, "bar": 2, "baz": 3.14},
        ),
        MockMLModel("mlmodel1"),
    ]

    async def Config(stream: Stream[FrameSystemConfigRequest, FrameSystemConfigResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = FrameSystemConfigResponse(frame_system_configs=CONFIG_RESPONSE)
        await stream.send_message(response)

    async def TransformPose(stream: Stream[TransformPoseRequest, TransformPoseResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = TransformPoseResponse(pose=TRANSFORM_RESPONSE)
        await stream.send_message(response)

    async def DiscoverComponents(stream: Stream[DiscoverComponentsRequest, DiscoverComponentsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = DiscoverComponentsResponse(discovery=DISCOVERY_RESPONSE)
        await stream.send_message(response)

    async def GetOperations(stream: Stream[GetOperationsRequest, GetOperationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetOperationsResponse(operations=OPERATIONS_RESPONSE)
        await stream.send_message(response)

    manager = ResourceManager(resources)
    service = RobotService(manager)
    service.FrameSystemConfig = Config
    service.TransformPose = TransformPose
    service.DiscoverComponents = DiscoverComponents
    service.GetOperations = GetOperations

    return service


class TestRobotService:
    @pytest.mark.asyncio
    async def test_resource_names(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = RobotServiceStub(channel)
            response: ResourceNamesResponse = await client.ResourceNames(ResourceNamesRequest())
            assert len(response.resources) == len(RESOURCE_NAMES)
            assert set(response.resources) == set(RESOURCE_NAMES)

    @pytest.mark.asyncio
    async def test_get_status(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = RobotServiceStub(channel)
            response: GetStatusResponse = await client.GetStatus(GetStatusRequest())
            assert list(response.status) == STATUSES

            request = GetStatusRequest(resource_names=[MockArm.get_resource_name("arm1"), MockCamera.get_resource_name("camera1")])
            response: GetStatusResponse = await client.GetStatus(request)
            assert list(response.status) == [ARM_STATUS_MSG, CAMERA_STATUS_MSG]

    @pytest.mark.asyncio
    async def test_stop_all(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = RobotServiceStub(channel)

            arm = service.manager.get_resource(Arm, Arm.get_resource_name("arm1"))
            assert isinstance(arm, MockArm)
            motor = service.manager.get_resource(Motor, Motor.get_resource_name("motor1"))
            assert isinstance(motor, MockMotor)

            # Test one with extra, one without
            await arm.move_to_position(Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            assert await arm.is_moving() is True
            await motor.set_power(1)
            assert await motor.is_moving() is True

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            param = StopExtraParameters(name=Arm.get_resource_name("arm1"), params=dict_to_struct(extra))
            request = StopAllRequest(extra=[param])
            await client.StopAll(request)

            assert await arm.is_moving() is False
            assert arm.extra == {"foo": "bar", "baz": [1, 2, 3]}

            assert await motor.is_moving() is False

            # Test passing extra where component's ``stop`` function doesn't take extra
            await arm.move_to_position(Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            assert await arm.is_moving() is True
            await motor.set_power(1)
            assert await motor.is_moving() is True

            extra = {"foo": "bar", "baz": [3, 2, 1]}
            param1 = StopExtraParameters(name=Arm.get_resource_name("arm1"), params=dict_to_struct(extra))
            param2 = StopExtraParameters(name=Motor.get_resource_name("motor1"), params=dict_to_struct(extra))
            request = StopAllRequest(extra=[param1, param2])
            await client.StopAll(request)

            assert await arm.is_moving() is False
            assert arm.extra == {"foo": "bar", "baz": [3, 2, 1]}

            assert await motor.is_moving() is False

            # Test that one error doesn't prevent other components from stopping
            await arm.move_to_position(Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            assert await arm.is_moving() is True
            await motor.set_power(1)
            assert await motor.is_moving() is True

            async def error_stop(extra: Optional[Dict[str, Any]] = None, **kwargs):
                raise Exception("Some random error")

            arm.stop = error_stop
            with pytest.raises(GRPCError):
                await client.StopAll(StopAllRequest())
            assert await arm.is_moving() is True
            assert await motor.is_moving() is False


class TestRobotClient:
    @pytest.mark.asyncio
    async def test_refresh(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert len(client._resource_names) == len(RESOURCE_NAMES)
            assert set(client._resource_names) == set(RESOURCE_NAMES)

            service.manager.register(MockSensor("sensor1"))
            await client.refresh()
            assert set(client._resource_names) == set(RESOURCE_NAMES + [MockSensor.get_resource_name("sensor1")])
            await client.close()

    @pytest.mark.asyncio
    async def test_refresh_task(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert client._refresh_task is None
            await client.close()

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
            assert client._channel._connected is True  # Robots created with ``with_channel`` do not close Channels automatically
            with pytest.raises(asyncio.CancelledError):
                await client._refresh_task

    @pytest.mark.asyncio
    async def test_resource_names(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert len(client._resource_names) == len(RESOURCE_NAMES)
            assert set(client._resource_names) == set(RESOURCE_NAMES)

            service.manager.register(MockSensor("sensor1"))
            await client.refresh()
            assert set(client._resource_names) == set(RESOURCE_NAMES + [MockSensor.get_resource_name("sensor1")])
            await client.close()

    @pytest.mark.asyncio
    async def test_get_component(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            component = client.get_component(MockArm.get_resource_name("arm1"))
            assert isinstance(component, Arm)

            with pytest.raises(ResourceNotFoundError):
                client.get_component(MockArm.get_resource_name("arm2"))

            with pytest.raises(ValueError):
                client.get_component(
                    ResourceName(
                        namespace=RESOURCE_NAMESPACE_RDK,
                        type="service",
                        subtype="vision",
                    )
                )

            # Test BaseComponent.from_robot(...)
            component = MockArm.from_robot(client, "arm1")
            assert isinstance(component, Arm)

            with pytest.raises(ResourceNotFoundError):
                MockArm.from_robot(client, "arm2")

            await client.close()

    @pytest.mark.asyncio
    async def test_get_status(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            statuses = await client.get_status()
            assert statuses == STATUSES

            statuses = await client.get_status([MockArm.get_resource_name("arm1"), MockCamera.get_resource_name("camera1")])
            assert statuses == [ARM_STATUS_MSG, CAMERA_STATUS_MSG]

            arm_status = statuses[0].status
            assert struct_to_message(arm_status, ArmStatus) == ARM_STATUS
            await client.close()

    @pytest.mark.asyncio
    async def test_get_service(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            client._resource_names.append(ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type="service", subtype="motion", name="motion1"))
            with pytest.raises(ResourceNotFoundError):
                MotionClient.from_robot(client)
            MotionClient.from_robot(client, "motion1")
            await client.close()

    @pytest.mark.asyncio
    async def test_get_frame_system_config(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            configs = await client.get_frame_system_config()
            assert configs == CONFIG_RESPONSE
            await client.close()

    @pytest.mark.asyncio
    async def test_transform_pose(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            pose = await client.transform_pose(PoseInFrame(), "some dest")
            assert pose == TRANSFORM_RESPONSE
            await client.close()

    @pytest.mark.asyncio
    async def test_discover_components(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            discoveries = await client.discover_components([DISCOVERY_QUERY])
            assert discoveries == DISCOVERY_RESPONSE
            await client.close()

    @pytest.mark.asyncio
    async def test_get_operations(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            ops = await client.get_operations()
            assert ops == OPERATIONS_RESPONSE
            await client.close()

    @pytest.mark.asyncio
    async def test_cancel_operation(self, service: RobotService):
        cancelled = None

        async def CancelOperation(stream: Stream[CancelOperationRequest, CancelOperationResponse]) -> None:
            request = await stream.recv_message()
            assert request is not None
            nonlocal cancelled
            cancelled = request.id
            await stream.send_message(CancelOperationResponse())

        service.CancelOperation = CancelOperation
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            await client.cancel_operation(id=OPERATION_ID)
            assert cancelled == OPERATION_ID
            await client.close()

    @pytest.mark.asyncio
    async def test_block_for_operation(self, service: RobotService):
        blocked = None

        async def BlockForOperation(stream: Stream[BlockForOperationRequest, BlockForOperationResponse]) -> None:
            request = await stream.recv_message()
            assert request is not None
            nonlocal blocked
            blocked = request.id
            await stream.send_message(BlockForOperationResponse())

        service.BlockForOperation = BlockForOperation
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            await client.block_for_operation(id=OPERATION_ID)
            assert blocked == OPERATION_ID
            await client.close()

    @pytest.mark.asyncio
    async def test_stop_all(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())

            arm = service.manager.get_resource(Arm, Arm.get_resource_name("arm1"))
            assert isinstance(arm, MockArm)
            motor = service.manager.get_resource(Motor, Motor.get_resource_name("motor1"))
            assert isinstance(motor, MockMotor)

            await arm.move_to_position(Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            assert await arm.is_moving() is True
            await motor.set_power(1)
            assert await motor.is_moving() is True

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await client.stop_all({arm.get_resource_name(arm.name): extra})

            assert await arm.is_moving() is False
            assert arm.extra == extra

            assert await motor.is_moving() is False
            await client.close()

    @pytest.mark.asyncio
    async def test_create_or_reset_client(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())

            # No change in channel
            arm_client = ArmClient.from_robot(client, "arm1")
            assert arm_client.channel is client._channel
            client._create_or_reset_client(Arm.get_resource_name(arm_client.name))
            assert arm_client is client.get_component(Arm.get_resource_name(arm_client.name))
            assert arm_client.channel is client._channel

            # Yes change in channel
            async with ChannelFor([service]) as channel2:
                arm_client.reset_channel(channel2)
                assert arm_client.channel is not client._channel
                client._create_or_reset_client(Arm.get_resource_name(arm_client.name))
                assert arm_client is client.get_component(Arm.get_resource_name(arm_client.name))
                assert arm_client.channel is client._channel

            await client.close()

            # Change in client
            class FakeArmClient(Arm, ResourceRPCClientBase):
                actual_client: ArmClient

                def __init__(self, name: str, channel: Channel):
                    super().__init__(name)
                    self.channel = channel
                    self.actual_client = ArmClient(name, channel)
                    self.client = self.actual_client.client

                async def get_end_position(
                    self,
                    *,
                    extra: Optional[Dict[str, Any]] = None,
                    timeout: Optional[float] = None,
                ) -> Pose:
                    return await self.actual_client.get_end_position(extra=extra, timeout=timeout)

                async def move_to_position(
                    self,
                    pose: Pose,
                    *,
                    extra: Optional[Dict[str, Any]] = None,
                    timeout: Optional[float] = None,
                ):
                    return await self.actual_client.move_to_position(pose, extra=extra, timeout=timeout)

                async def move_to_joint_positions(
                    self,
                    positions: JointPositions,
                    *,
                    extra: Optional[Dict[str, Any]] = None,
                    timeout: Optional[float] = None,
                ):
                    return await self.actual_client.move_to_joint_positions(positions, extra=extra, timeout=timeout)

                async def get_joint_positions(
                    self,
                    *,
                    extra: Optional[Dict[str, Any]] = None,
                    timeout: Optional[float] = None,
                ) -> JointPositions:
                    return await self.actual_client.get_joint_positions(extra=extra, timeout=timeout)

                async def stop(
                    self,
                    *,
                    extra: Optional[Dict[str, Any]] = None,
                    timeout: Optional[float] = None,
                ):
                    return await self.actual_client.stop(extra=extra, timeout=timeout)

                async def is_moving(self) -> bool:
                    return await self.actual_client.is_moving()

                async def get_kinematics(self, timeout: Optional[float] = None) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
                    return await self.actual_client.get_kinematics(timeout=timeout)

            old_create_client = Registry._SUBTYPES[Arm.SUBTYPE].create_rpc_client
            Registry._SUBTYPES[Arm.SUBTYPE].create_rpc_client = lambda name, channel: FakeArmClient(name, channel)

            client = await RobotClient.with_channel(channel, RobotClient.Options())

            async with ChannelFor([service]) as channel2:
                arm_client.channel = channel2
                assert arm_client.channel is not client._channel
                client._create_or_reset_client(Arm.get_resource_name(arm_client.name))
                assert arm_client is not client.get_component(Arm.get_resource_name(arm_client.name))  # Should be a new client now

            await client.close()
            Registry._SUBTYPES[Arm.SUBTYPE].create_rpc_client = old_create_client
