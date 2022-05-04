from typing import Any, Dict, Optional

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.api.common import Pose, WorldState
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
    gRPC client for an Arm component.

    Used to communicate with an existing `Arm` implementation over gRPC.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = ArmServiceStub(channel)
        super().__init__(name)

    async def get_end_position(self) -> Pose:
        request = GetEndPositionRequest(name=self.name)
        response: GetEndPositionResponse = \
            await self.client.GetEndPosition(request)
        return response.pose

    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None
    ):
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

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
