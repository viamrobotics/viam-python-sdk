import pytest
from grpclib import GRPCError
from grpclib.testing import ChannelFor

from viam.components.arm import ArmClient, ArmStatus, KinematicsFileFormat, create_status
from viam.components.arm.service import ArmRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetKinematicsRequest, GetKinematicsResponse, Pose
from viam.proto.component.arm import (
    ArmServiceStub,
    GetEndPositionRequest,
    GetEndPositionResponse,
    GetJointPositionsRequest,
    GetJointPositionsResponse,
    IsMovingRequest,
    IsMovingResponse,
    JointPositions,
    MoveToJointPositionsRequest,
    MoveToPositionRequest,
    StopRequest,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, message_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockArm


class TestArm:
    arm = MockArm(name="arm")
    pose = Pose(x=5, y=5, z=5, o_x=5, o_y=5, o_z=5, theta=20)
    joint_pos = JointPositions(values=[1, 8, 2])
    kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        await self.arm.move_to_position(self.pose)
        assert self.arm.position == self.pose

    @pytest.mark.asyncio
    async def test_get_end_position(self):
        pos = await self.arm.get_end_position()
        assert pos == self.pose

    @pytest.mark.asyncio
    async def test_move_to_joint_positions(self):
        await self.arm.move_to_joint_positions(self.joint_pos)
        assert self.arm.joint_positions == self.joint_pos

    @pytest.mark.asyncio
    async def test_get_joint_positions(self):
        jp = await self.arm.get_joint_positions()
        assert jp == self.joint_pos

    @pytest.mark.asyncio
    async def test_stop(self):
        assert self.arm.is_stopped is False
        await self.arm.stop()
        assert self.arm.is_stopped is True

    @pytest.mark.asyncio
    async def test_is_moving(self):
        await self.arm.move_to_position(self.pose)
        assert await self.arm.is_moving()
        await self.arm.stop()
        assert not await self.arm.is_moving()

    @pytest.mark.asyncio
    async def test_get_kinematics(self):
        kd = await self.arm.get_kinematics()
        assert kd == self.kinematics

    @pytest.mark.asyncio
    async def test_do(self):
        command = {"command": "args"}
        resp = await self.arm.do_command(command)
        assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_status(self):
        await self.arm.move_to_position(self.pose)
        status = await create_status(self.arm)
        assert status.name == MockArm.get_resource_name(self.arm.name)
        assert status.status == message_to_struct(ArmStatus(end_position=self.pose, joint_positions=self.joint_pos, is_moving=True))

    @pytest.mark.asyncio
    async def test_extra(self):
        await self.arm.get_end_position(extra={"foo": "bar"})
        assert self.arm.extra == {"foo": "bar"}


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "arm"
        cls.arm = MockArm(name=cls.name)
        cls.manager = ResourceManager([cls.arm])
        cls.service = ArmRPCService(cls.manager)
        cls.pose = Pose(x=5, y=5, z=5, o_x=5, o_y=5, o_z=5, theta=20)
        cls.joint_pos = JointPositions(values=[1, 8, 2])
        cls.kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = MoveToPositionRequest(name=self.name, to=self.pose)
            await client.MoveToPosition(request)
            assert self.arm.position == self.pose

    @pytest.mark.asyncio
    async def test_get_end_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetEndPositionRequest(name=self.name)
            response: GetEndPositionResponse = await client.GetEndPosition(request)
            assert response.pose == self.pose

    @pytest.mark.asyncio
    async def test_move_to_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = MoveToJointPositionsRequest(name=self.name, positions=self.joint_pos)
            await client.MoveToJointPositions(request)
            assert self.arm.joint_positions == self.joint_pos

    @pytest.mark.asyncio
    async def test_get_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetJointPositionsRequest(name=self.name)
            response: GetJointPositionsResponse = await client.GetJointPositions(request)
            assert response.positions == self.joint_pos

    @pytest.mark.asyncio
    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.arm.is_stopped is False
            assert self.arm.timeout is None
            client = ArmServiceStub(channel)
            request = StopRequest(name=self.name)
            await client.Stop(request, timeout=4.4)
            assert self.arm.is_stopped is True
            assert self.arm.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            assert self.arm.is_stopped is True
            self.arm.is_stopped = False
            client = ArmServiceStub(channel)
            request = IsMovingRequest(name=self.arm.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is True

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    @pytest.mark.asyncio
    async def test_get_kinematics(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetKinematicsRequest(name=self.name)
            response: GetKinematicsResponse = await client.GetKinematics(request)
            assert (response.format, response.kinematics_data) == self.kinematics

    @pytest.mark.asyncio
    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetGeometriesRequest()
            with pytest.raises(GRPCError, match=r"Method [a-zA-Z]+ not implemented"):
                await client.GetGeometries(request)

    @pytest.mark.asyncio
    async def test_extra(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            extra = {"foo": "bar"}
            request = GetEndPositionRequest(name=self.name, extra=dict_to_struct(extra))
            await client.GetEndPosition(request)
            assert self.arm.extra == extra


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "arm"
        cls.arm = MockArm(name=cls.name)
        cls.manager = ResourceManager([cls.arm])
        cls.service = ArmRPCService(cls.manager)
        cls.pose = Pose(x=5, y=5, z=5, o_x=5, o_y=5, o_z=5, theta=20)
        cls.joint_pos = JointPositions(values=[1, 8, 2])
        cls.kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            await client.move_to_position(self.pose)
            assert self.arm.position == self.pose

    @pytest.mark.asyncio
    async def test_get_end_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            pos = await client.get_end_position()
            assert pos == self.pose

    @pytest.mark.asyncio
    async def test_move_to_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            await client.move_to_joint_positions(self.joint_pos)
            assert self.arm.joint_positions == self.joint_pos

    @pytest.mark.asyncio
    async def test_get_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            jp = await client.get_joint_positions()
            assert jp == self.joint_pos

    @pytest.mark.asyncio
    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.arm.is_stopped is False
            assert self.arm.timeout is None
            client = ArmClient(self.name, channel)
            await client.stop(timeout=1.82)
            assert self.arm.is_stopped is True
            assert self.arm.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            assert self.arm.is_stopped is True
            self.arm.is_stopped = False
            assert await client.is_moving() is True

    @pytest.mark.asyncio
    async def test_get_kinematics(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            kd = await client.get_kinematics()
            assert kd == self.kinematics

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_extra(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            await client.get_end_position(extra={"foo": "bar"})
            assert self.arm.extra == {"foo": "bar"}
