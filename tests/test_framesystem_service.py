from typing import List

import pytest
from grpclib.server import Stream
from grpclib.testing import ChannelFor

from viam.errors import ResourceNotFoundError
from viam.proto.common import PoseInFrame, ResourceName, Transform
from viam.proto.robot import GetPoseRequest, GetPoseResponse, RobotServiceStub, TransformPCDRequest, TransformPCDResponse
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK_INTERNAL, RESOURCE_TYPE_COMPONENT, resource_name_from_string
from viam.robot.client import RobotClient
from viam.robot.service import RobotService
from viam.services.framesystem import FrameSystem, FrameSystemClient
from viam.utils import struct_to_dict

from . import expected_grpc_timeout
from .test_robot import CONFIG_RESPONSE, GET_POSE_RESPONSE, TRANSFORM_PCD_RESPONSE, TRANSFORM_RESPONSE
from .test_robot import service as robot_service  # noqa: F401

FRAME_SYSTEM_NAME = FrameSystem.get_resource_name(FrameSystem.PUBLIC_NAME)


class TestFrameSystem:
    def test_api_and_public_name(self):
        assert str(FrameSystem.API) == "rdk-internal:service:frame_system"
        assert FrameSystem.PUBLIC_NAME == "$framesystem"
        assert FRAME_SYSTEM_NAME == ResourceName(
            namespace=RESOURCE_NAMESPACE_RDK_INTERNAL, type="service", subtype="frame_system", name="$framesystem"
        )
        # the string form viam-server would send as a dependency parses back to the same name
        assert resource_name_from_string("rdk-internal:service:frame_system/$framesystem") == FRAME_SYSTEM_NAME
        assert API.from_resource_name(FRAME_SYSTEM_NAME) == FrameSystem.API

    async def test_from_dependencies(self, robot_service: RobotService):  # noqa: F811
        async with ChannelFor([robot_service]) as channel:
            client = FrameSystemClient(FrameSystem.PUBLIC_NAME, channel)
            assert FrameSystem.from_dependencies({FRAME_SYSTEM_NAME: client}) is client

            with pytest.raises(ResourceNotFoundError):
                FrameSystem.from_dependencies({})


class TestFrameSystemClient:
    async def test_get_frame_system_config(self, robot_service: RobotService):  # noqa: F811
        async with ChannelFor([robot_service]) as channel:
            client = FrameSystemClient(FrameSystem.PUBLIC_NAME, channel)
            assert await client.get_frame_system_config() == CONFIG_RESPONSE

    async def test_get_pose(self, robot_service: RobotService):  # noqa: F811
        received: List[GetPoseRequest] = []
        timeout = 4.4

        async def GetPose(stream: Stream[GetPoseRequest, GetPoseResponse]) -> None:
            request = await stream.recv_message()
            assert request is not None
            assert stream.deadline is not None
            assert stream.deadline.time_remaining() == expected_grpc_timeout(timeout)
            received.append(request)
            await stream.send_message(GetPoseResponse(pose=GET_POSE_RESPONSE))

        robot_service.GetPose = GetPose
        transforms = [Transform(reference_frame="extra_frame", pose_in_observer_frame=PoseInFrame(reference_frame="world"))]
        async with ChannelFor([robot_service]) as channel:
            client = FrameSystemClient(FrameSystem.PUBLIC_NAME, channel)
            pose = await client.get_pose("my_gripper", "my_arm", transforms, extra={"foo": "bar"}, timeout=timeout)
            assert pose == GET_POSE_RESPONSE

            pose = await client.get_pose("my_gripper", timeout=timeout)
            assert pose == GET_POSE_RESPONSE

        assert len(received) == 2
        assert received[0].component_name == "my_gripper"
        assert received[0].destination_frame == "my_arm"
        assert list(received[0].supplemental_transforms) == transforms
        assert struct_to_dict(received[0].extra) == {"foo": "bar"}
        assert received[1].destination_frame == ""
        assert len(received[1].supplemental_transforms) == 0

    async def test_transform_pose(self, robot_service: RobotService):  # noqa: F811
        async with ChannelFor([robot_service]) as channel:
            client = FrameSystemClient(FrameSystem.PUBLIC_NAME, channel)
            pose = await client.transform_pose(PoseInFrame(reference_frame="world"), "arm")
            assert pose == TRANSFORM_RESPONSE

    async def test_transform_pcd(self, robot_service: RobotService):  # noqa: F811
        received: List[TransformPCDRequest] = []

        async def TransformPCD(stream: Stream[TransformPCDRequest, TransformPCDResponse]) -> None:
            request = await stream.recv_message()
            assert request is not None
            received.append(request)
            await stream.send_message(TransformPCDResponse(point_cloud_pcd=TRANSFORM_PCD_RESPONSE))

        robot_service.TransformPCD = TransformPCD
        async with ChannelFor([robot_service]) as channel:
            client = FrameSystemClient(FrameSystem.PUBLIC_NAME, channel)
            pcd = await client.transform_pcd(b"raw pcd", "my_camera", "world")
            assert pcd == TRANSFORM_PCD_RESPONSE

        assert len(received) == 1
        assert received[0].point_cloud_pcd == b"raw pcd"
        assert received[0].source == "my_camera"
        assert received[0].destination == "world"

    async def test_reset_channel(self, robot_service: RobotService):  # noqa: F811
        async with ChannelFor([robot_service]) as channel:
            async with ChannelFor([robot_service]) as other_channel:
                client = FrameSystemClient(FrameSystem.PUBLIC_NAME, channel)
                old_stub = client.client
                client.reset_channel(other_channel)
                assert client.channel is other_channel
                assert isinstance(client.client, RobotServiceStub)
                assert client.client is not old_stub
                assert await client.get_frame_system_config() == CONFIG_RESPONSE


class TestRobotClientFrameSystem:
    async def test_get_service_special_case(self, robot_service: RobotService):  # noqa: F811
        async with ChannelFor([robot_service]) as channel:
            async with await RobotClient.with_channel(channel, RobotClient.Options()) as robot:
                # viam-server never lists the frame system, so the lookup has to work without it being in resource_names
                assert FRAME_SYSTEM_NAME not in robot.resource_names

                frame_system = robot.get_service(FRAME_SYSTEM_NAME)
                assert isinstance(frame_system, FrameSystemClient)
                assert frame_system.name == FrameSystem.PUBLIC_NAME
                assert frame_system.channel is channel
                assert robot.get_service(FRAME_SYSTEM_NAME) is frame_system
                assert await frame_system.get_frame_system_config() == CONFIG_RESPONSE
                assert await frame_system.get_pose("my_gripper") == GET_POSE_RESPONSE

                # only the reserved name is special cased
                with pytest.raises(ResourceNotFoundError):
                    robot.get_service(FrameSystem.get_resource_name("some_other_frame_system"))
                with pytest.raises(ValueError):
                    robot.get_service(
                        ResourceName(
                            namespace=RESOURCE_NAMESPACE_RDK_INTERNAL,
                            type=RESOURCE_TYPE_COMPONENT,
                            subtype="frame_system",
                            name=FrameSystem.PUBLIC_NAME,
                        )
                    )

    async def test_from_robot(self, robot_service: RobotService):  # noqa: F811
        async with ChannelFor([robot_service]) as channel:
            async with await RobotClient.with_channel(channel, RobotClient.Options()) as robot:
                frame_system = FrameSystem.from_robot(robot)
                assert isinstance(frame_system, FrameSystemClient)
                assert frame_system is robot.get_service(FRAME_SYSTEM_NAME)
                assert FrameSystemClient.from_robot(robot) is frame_system
                assert await frame_system.transform_pose(PoseInFrame(reference_frame="world"), "arm") == TRANSFORM_RESPONSE
