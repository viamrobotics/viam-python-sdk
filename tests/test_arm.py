from grpclib.testing import ChannelFor

from viam.components.arm import ArmClient, KinematicsFileFormat
from viam.components.arm.service import ArmRPCService
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetKinematicsRequest,
    GetKinematicsResponse,
    Get3DModelsRequest,
    Get3DModelsResponse,
    Mesh,
    Pose,
)
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
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import GEOMETRIES, MockArm, MODELS


class TestArm:
    arm = MockArm(name="arm")
    pose = Pose(x=5, y=5, z=5, o_x=5, o_y=5, o_z=5, theta=20)
    joint_pos = JointPositions(values=[1, 8, 2])
    kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")
    _3d_models = MODELS

    async def test_move_to_position(self):
        await self.arm.move_to_position(self.pose)
        assert self.arm.position == self.pose

    async def test_get_end_position(self):
        pos = await self.arm.get_end_position()
        assert pos == self.pose

    async def test_move_to_joint_positions(self):
        await self.arm.move_to_joint_positions(self.joint_pos)
        assert self.arm.joint_positions == self.joint_pos

    async def test_get_joint_positions(self):
        jp = await self.arm.get_joint_positions()
        assert jp == self.joint_pos

    async def test_stop(self):
        assert self.arm.is_stopped is False
        await self.arm.stop()
        assert self.arm.is_stopped is True

    async def test_is_moving(self):
        await self.arm.move_to_position(self.pose)
        assert await self.arm.is_moving()
        await self.arm.stop()
        assert not await self.arm.is_moving()

    async def test_get_kinematics(self):
        kd = await self.arm.get_kinematics(extra={"1": "2"})
        assert kd == self.kinematics
        assert self.arm.extra == {"1": "2"}

    async def test_get_geometries(self):
        geometries = await self.arm.get_geometries()
        assert geometries == GEOMETRIES

    async def test_get_3d_models(self):
        models = await self.arm.get_3d_models()
        assert models == self._3d_models
        assert self.arm.extra == {}

        models = await self.arm.get_3d_models(extra={"1": "2"})
        assert models == self._3d_models
        assert self.arm.extra == {"1": "2"}

    async def test_do(self):
        command = {"command": "args"}
        resp = await self.arm.do_command(command)
        assert resp == {"command": command}

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
        cls._3d_models = MODELS

    async def test_move_to_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = MoveToPositionRequest(name=self.name, to=self.pose)
            await client.MoveToPosition(request)
            assert self.arm.position == self.pose

    async def test_get_end_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetEndPositionRequest(name=self.name)
            response: GetEndPositionResponse = await client.GetEndPosition(request)
            assert response.pose == self.pose

    async def test_move_to_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = MoveToJointPositionsRequest(name=self.name, positions=self.joint_pos)
            await client.MoveToJointPositions(request)
            assert self.arm.joint_positions == self.joint_pos

    async def test_get_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetJointPositionsRequest(name=self.name)
            response: GetJointPositionsResponse = await client.GetJointPositions(request)
            assert response.positions == self.joint_pos

    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.arm.is_stopped is False
            assert self.arm.timeout is None
            client = ArmServiceStub(channel)
            request = StopRequest(name=self.name)
            await client.Stop(request, timeout=4.4)
            assert self.arm.is_stopped is True
            assert self.arm.timeout == loose_approx(4.4)

    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            assert self.arm.is_stopped is True
            self.arm.is_stopped = False
            client = ArmServiceStub(channel)
            request = IsMovingRequest(name=self.arm.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is True

    async def test_get_kinematics(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetKinematicsRequest(name=self.name)
            response: GetKinematicsResponse = await client.GetKinematics(request)
            assert (response.format, response.kinematics_data) == self.kinematics

    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetGeometriesRequest(name=self.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES

    async def test_get_3d_models(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = Get3DModelsRequest(name=self.name)
            response: Get3DModelsResponse = await client.Get3DModels(request)
            assert [mesh for mesh in response.meshes] == self._3d_models
            assert self.arm.extra == {}

            extra = {"1": "2"}
            request = Get3DModelsRequest(name=self.name, extra=dict_to_struct(extra))
            response: Get3DModelsResponse = await client.Get3DModels(request)
            assert [mesh for mesh in response.meshes] == self._3d_models
            assert self.arm.extra == extra

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

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
        cls._3d_models = MODELS

    async def test_move_to_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            await client.move_to_position(self.pose)
            assert self.arm.position == self.pose

    async def test_get_end_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            pos = await client.get_end_position()
            assert pos == self.pose

    async def test_move_to_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            await client.move_to_joint_positions(self.joint_pos)
            assert self.arm.joint_positions == self.joint_pos

    async def test_get_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            jp = await client.get_joint_positions()
            assert jp == self.joint_pos

    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.arm.is_stopped is False
            assert self.arm.timeout is None
            client = ArmClient(self.name, channel)
            await client.stop(timeout=1.82)
            assert self.arm.is_stopped is True
            assert self.arm.timeout == loose_approx(1.82)

    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            assert self.arm.is_stopped is True
            self.arm.is_stopped = False
            assert await client.is_moving() is True

    async def test_get_kinematics(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            kd = await client.get_kinematics(extra={"1": "2"})
            assert kd == self.kinematics
            assert self.arm.extra == {"1": "2"}

    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES

    async def test_get_3d_models(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            models = await client.get_3d_models()
            assert models == self._3d_models
            assert self.arm.extra == {}

            models = await client.get_3d_models(extra={"1": "2"})
            assert models == self._3d_models
            assert self.arm.extra == {"1": "2"}

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    async def test_extra(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmClient(self.name, channel)
            await client.get_end_position(extra={"foo": "bar"})
            assert self.arm.extra == {"foo": "bar"}
