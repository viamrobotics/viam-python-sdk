import pytest
from grpclib.testing import ChannelFor
from viam.components.arm import ArmClient
from viam.components.arm.service import ArmService
from viam.components.generic.service import GenericService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.common import Pose
from viam.proto.api.component.arm import (ArmServiceStub,
                                          GetEndPositionRequest,
                                          GetEndPositionResponse,
                                          GetJointPositionsRequest,
                                          GetJointPositionsResponse,
                                          JointPositions,
                                          MoveToJointPositionsRequest,
                                          MoveToPositionRequest)

from .mocks.components import MockArm


class TestArm:

    arm = MockArm(name='arm')
    pose = Pose(
        x=5,
        y=5,
        z=5,
        o_x=5,
        o_y=5,
        o_z=5,
        theta=20
    )
    joint_pos = JointPositions(degrees=[1, 8, 2])

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
    async def test_do(self):
        with pytest.raises(NotImplementedError):
            await self.arm.do({'command': 'args'})


class TestService:

    name = 'arm'
    arm = MockArm(name=name)
    manager = ResourceManager([arm])
    service = ArmService(manager)
    pose = Pose(
        x=5,
        y=5,
        z=5,
        o_x=5,
        o_y=5,
        o_z=5,
        theta=20
    )
    joint_pos = JointPositions(degrees=[1, 8, 2])

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
            response: GetEndPositionResponse = \
                await client.GetEndPosition(request)
            assert response.pose == self.pose

    @pytest.mark.asyncio
    async def test_move_to_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = MoveToJointPositionsRequest(
                name=self.name, position_degs=self.joint_pos)
            await client.MoveToJointPositions(request)
            assert self.arm.joint_positions == self.joint_pos

    @pytest.mark.asyncio
    async def test_get_joint_positions(self):
        async with ChannelFor([self.service]) as channel:
            client = ArmServiceStub(channel)
            request = GetJointPositionsRequest(name=self.name)
            response: GetJointPositionsResponse = \
                await client.GetJointPositions(request)
            assert response.position_degs == self.joint_pos


class TestClient:

    name = 'arm'
    arm = MockArm(name=name)
    manager = ResourceManager([arm])
    service = ArmService(manager)
    pose = Pose(
        x=5,
        y=5,
        z=5,
        o_x=5,
        o_y=5,
        o_z=5,
        theta=20
    )
    joint_pos = JointPositions(degrees=[1, 8, 2])

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
    async def test_do(self):
        async with ChannelFor([self.service, GenericService(self.manager)]) as channel:
            client = ArmClient(self.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do({'command': 'args'})
