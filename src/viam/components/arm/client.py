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
                                          MoveToPositionRequest, StopRequest)
from viam.utils import dict_to_struct

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

    async def get_end_position(self, extra: Dict[str, Any] = {}) -> Pose:
        request = GetEndPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetEndPositionResponse = \
            await self.client.GetEndPosition(request)
        return response.pose

    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None,
        extra: Dict[str, Any] = {}
    ):
        request = MoveToPositionRequest(name=self.name, to=pose, world_state=world_state, extra=dict_to_struct(extra))
        await self.client.MoveToPosition(request)

    async def get_joint_positions(self, extra: Dict[str, Any] = {}) -> JointPositions:
        request = GetJointPositionsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetJointPositionsResponse = \
            await self.client.GetJointPositions(request)
        return response.positions

    async def move_to_joint_positions(self, positions: JointPositions, extra: Dict[str, Any] = {}):
        request = MoveToJointPositionsRequest(name=self.name, positions=positions, extra=dict_to_struct(extra))
        await self.client.MoveToJointPositions(request)

    async def stop(self, extra: Dict[str, Any] = {}):
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request)

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
