import asyncio
from typing import Any, Dict, List, Optional, Tuple
from unittest import mock

import pytest
from grpclib.client import Channel
from grpclib.exceptions import GRPCError
from grpclib.server import Stream
from grpclib.testing import ChannelFor

from viam.components.arm import Arm, KinematicsFileFormat
from viam.components.arm.client import ArmClient
from viam.components.motor import Motor
from viam.components.movement_sensor import MovementSensor
from viam.errors import ResourceNotFoundError
from viam.proto.common import Geometry, GeoPoint, Orientation, Pose, PoseInFrame, ResourceName, Transform, Vector3
from viam.proto.component.arm import JointPositions
from viam.proto.robot import (
    BlockForOperationRequest,
    BlockForOperationResponse,
    CancelOperationRequest,
    CancelOperationResponse,
    FrameSystemConfig,
    FrameSystemConfigRequest,
    FrameSystemConfigResponse,
    GetCloudMetadataRequest,
    GetCloudMetadataResponse,
    GetMachineStatusRequest,
    GetMachineStatusResponse,
    GetOperationsRequest,
    GetOperationsResponse,
    GetVersionRequest,
    GetVersionResponse,
    Operation,
    RestartModuleRequest,
    RestartModuleResponse,
    ResourceNamesRequest,
    ResourceNamesResponse,
    ResourceStatus,
    RobotServiceStub,
    ShutdownRequest,
    ShutdownResponse,
    StopAllRequest,
    StopExtraParameters,
    TransformPoseRequest,
    TransformPoseResponse,
)
from viam.resource.manager import ResourceManager
from viam.resource.registry import Registry
from viam.resource.rpc_client_base import ResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, RESOURCE_TYPE_SERVICE
from viam.robot.client import RobotClient
from viam.robot.service import RobotService
from viam.services.mlmodel.client import MLModelClient
from viam.utils import dict_to_struct

from .mocks.components import MockArm, MockCamera, MockMotor, MockMovementSensor, MockSensor
from .mocks.services import MockMLModel

RESOURCE_NAMES = [
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="arm", name="arm1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="camera", name="camera1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="motor", name="motor1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="movement_sensor", name="movement_sensor1"),
    ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_SERVICE, subtype="mlmodel", name="mlmodel1"),
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

OPERATION_ID = "abc"

OPERATIONS_RESPONSE = [Operation(id=OPERATION_ID)]

GET_CLOUD_METADATA_RESPONSE = GetCloudMetadataResponse(
    robot_part_id="the-machine-id",
    primary_org_id="the-primary-org",
    location_id="the-location",
    machine_id="the-machine-id",
    machine_part_id="the-machine-part-id",
)

MODULE_ID = "id"
MODULE_NAME = "name"

GET_VERVSION_RESPONSE = GetVersionResponse(
    platform="rdk",
    version="0.2.0",
    api_version="0.3.0",
)

GET_MACHINE_STATUS_RESPONSE = GetMachineStatusResponse(
    resources=[
        ResourceStatus(
            name=ResourceName(namespace=RESOURCE_NAMESPACE_RDK, type=RESOURCE_TYPE_COMPONENT, subtype="arm", name="arm1"),
            state=ResourceStatus.State.STATE_READY,
        )
    ]
)


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
            accuracy=MovementSensor.Accuracy(accuracy={"foo": 0.1, "bar": 2, "baz": 3.14}),
            readings={"a": 1, "b": 2, "c": 3},
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

    async def GetOperations(stream: Stream[GetOperationsRequest, GetOperationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetOperationsResponse(operations=OPERATIONS_RESPONSE)
        await stream.send_message(response)

    async def GetCloudMetadata(stream: Stream[GetCloudMetadataRequest, GetCloudMetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GET_CLOUD_METADATA_RESPONSE)

    async def GetVersion(stream: Stream[GetVersionRequest, GetVersionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GET_VERVSION_RESPONSE)

    async def GetMachineStatus(stream: Stream[GetMachineStatusRequest, GetMachineStatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GET_MACHINE_STATUS_RESPONSE)

    async def Shutdown(stream: Stream[ShutdownRequest, ShutdownResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = ShutdownResponse()
        await stream.send_message(response)

    async def RestartModule(stream: Stream[RestartModuleRequest, RestartModuleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        assert request.module_name == MODULE_NAME
        assert request.module_id == MODULE_ID
        await stream.send_message(RestartModuleResponse())

    manager = ResourceManager(resources)
    service = RobotService(manager)
    service.FrameSystemConfig = Config
    service.TransformPose = TransformPose
    service.GetOperations = GetOperations
    service.GetCloudMetadata = GetCloudMetadata
    service.Shutdown = Shutdown
    service.GetVersion = GetVersion
    service.GetMachineStatus = GetMachineStatus

    return service


class TestRobotService:
    async def test_resource_names(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = RobotServiceStub(channel)
            response: ResourceNamesResponse = await client.ResourceNames(ResourceNamesRequest())
            assert len(response.resources) == len(RESOURCE_NAMES)
            assert set(response.resources) == set(RESOURCE_NAMES)

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
    async def test_refresh(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert len(client._resource_names) == len(RESOURCE_NAMES)
            assert set(client._resource_names) == set(RESOURCE_NAMES)

            service.manager.register(MockSensor("sensor1"))
            await client.refresh()
            assert set(client._resource_names) == set(RESOURCE_NAMES + [MockSensor.get_resource_name("sensor1")])
            await client.close()

    async def test_refresh_task(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert client._refresh_task is None
            await client.close()

            client = await RobotClient.with_channel(channel, RobotClient.Options(refresh_interval=100))
            assert client._refresh_task is not None
            await client.close()

    async def test_close(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options(refresh_interval=100))
            assert client._channel._connected is True
            assert client._refresh_task is not None and client._refresh_task.cancelled() is False

            await client.close()
            assert client._channel._connected is True  # Robots created with ``with_channel`` do not close Channels automatically
            with pytest.raises(asyncio.CancelledError):
                await client._refresh_task

    async def test_resource_names(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            assert len(client._resource_names) == len(RESOURCE_NAMES)
            assert set(client._resource_names) == set(RESOURCE_NAMES)

            service.manager.register(MockSensor("sensor1"))
            await client.refresh()
            assert set(client._resource_names) == set(RESOURCE_NAMES + [MockSensor.get_resource_name("sensor1")])
            await client.close()

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

    async def test_get_service(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            with pytest.raises(ResourceNotFoundError):
                MLModelClient.from_robot(client, "mlmodel")
            MLModelClient.from_robot(client, "mlmodel1")
            await client.close()

    async def test_get_frame_system_config(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            configs = await client.get_frame_system_config()
            assert configs == CONFIG_RESPONSE
            await client.close()

    async def test_transform_pose(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            pose = await client.transform_pose(PoseInFrame(), "some dest")
            assert pose == TRANSFORM_RESPONSE
            await client.close()

    async def test_get_cloud_metadata(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            md = await client.get_cloud_metadata()
            assert md == GET_CLOUD_METADATA_RESPONSE
            await client.close()

    async def test_get_version(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            md = await client.get_version()
            assert md == GET_VERVSION_RESPONSE
            await client.close()

    async def test_get_machine_status(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            statuses = await client.get_machine_status()
            assert statuses == GET_MACHINE_STATUS_RESPONSE
            await client.close()

    async def test_get_operations(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())
            ops = await client.get_operations()
            assert ops == OPERATIONS_RESPONSE
            await client.close()

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
            await client.stop_all({arm.get_resource_name(arm.name): extra})  # type: ignore

            assert await arm.is_moving() is False
            assert arm.extra == extra

            assert await motor.is_moving() is False
            await client.close()

    async def test_create_or_reset_client(self, service: RobotService):
        async with ChannelFor([service]) as channel:
            client = await RobotClient.with_channel(channel, RobotClient.Options())

            # No change in channel
            arm_client = ArmClient.from_robot(client, "arm1")
            assert arm_client.channel is client._channel
            await client._create_or_reset_client(Arm.get_resource_name(arm_client.name))
            assert arm_client is client.get_component(Arm.get_resource_name(arm_client.name))
            assert arm_client.channel is client._channel

            # Yes change in channel
            async with ChannelFor([service]) as channel2:
                arm_client.reset_channel(channel2)
                assert arm_client.channel is not client._channel
                await client._create_or_reset_client(Arm.get_resource_name(arm_client.name))
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

                async def get_kinematics(
                    self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None
                ) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
                    return await self.actual_client.get_kinematics(timeout=timeout)

                async def get_geometries(
                    self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None
                ) -> List[Geometry]:
                    return await self.actual_client.get_geometries(timeout=timeout)

            old_create_client = Registry._APIS[Arm.API].create_rpc_client
            Registry._APIS[Arm.API].create_rpc_client = lambda name, channel: FakeArmClient(name, channel)

            client = await RobotClient.with_channel(channel, RobotClient.Options())

            async with ChannelFor([service]) as channel2:
                arm_client.channel = channel2
                assert arm_client.channel is not client._channel
                await client._create_or_reset_client(Arm.get_resource_name(arm_client.name))
                assert arm_client is not client.get_component(Arm.get_resource_name(arm_client.name))  # Should be a new client now

            await client.close()
            Registry._APIS[Arm.API].create_rpc_client = old_create_client

    async def test_shutdown(self, service: RobotService):
        async with ChannelFor([service]) as channel:

            async def shutdown_client_mock(self):
                return await self._client.Shutdown(ShutdownRequest())

            client = await RobotClient.with_channel(channel, RobotClient.Options())

            with mock.patch("viam.robot.client.RobotClient.shutdown") as shutdown_mock:
                shutdown_mock.return_value = await shutdown_client_mock(client)
                shutdown_response = await client.shutdown()

                assert shutdown_response == ShutdownResponse()
                shutdown_mock.assert_called_once()

                await client.close()

    async def test_restart_module(self, service: RobotService):
        async with ChannelFor([service]) as channel:

            client = await RobotClient.with_channel(channel, RobotClient.Options())

            with mock.patch("viam.robot.client.RobotClient.restart_module") as restart_module_mock:
                await client.restart_module(id=MODULE_ID, name=MODULE_NAME)
                restart_module_mock.assert_called_once()

                await client.close()
