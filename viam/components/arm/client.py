from typing import List

from grpclib.client import Channel
from viam.proto.api.common import GeometriesInFrame, Pose, WorldState
from viam.proto.api.component.arm import (ArmServiceStub,
                                          GetEndPositionRequest,
                                          GetEndPositionResponse,
                                          GetJointPositionsRequest,
                                          GetJointPositionsResponse,
                                          JointPositions,
                                          MoveToJointPositionsRequest,
                                          MoveToPositionRequest)

from .arm import Arm


class ArmClient(Arm):
    """
    gRPC client for the Arm component.
    """

    def __init__(self, name: str, channel: Channel):
        self.name = name
        self.client = ArmServiceStub(channel)

    async def get_end_position(self) -> Pose:
        request = GetEndPositionRequest(name=self.name)
        response: GetEndPositionResponse = \
            await self.client.GetEndPosition(request)
        return response.pose

    async def move_to_position(
        self,
        pose: Pose,
        obstacles: List[GeometriesInFrame]
    ):
        world_state = WorldState(obstacles=obstacles)
        request = MoveToPositionRequest(
            name=self.name, to=pose, world_state=world_state)
        await self.client.MoveToPosition(request)

    async def get_joint_positions(self) -> JointPositions:
        request = GetJointPositionsRequest(name=self.name)
        response: GetJointPositionsResponse = \
            await self.client.GetJointPositions(request)
        return response.position_degs

    async def move_to_joint_positions(self, positions: JointPositions):
        request = MoveToJointPositionsRequest(
            name=self.name, position_degs=positions)
        await self.client.MoveToJointPositions(request)
