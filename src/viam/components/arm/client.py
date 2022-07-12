from typing import Any, Dict, Optional

from google.protobuf.struct_pb2 import Struct
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

    async def get_end_position(self, extra: Optional[Dict[str, Any]] = None) -> Pose:
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = GetEndPositionRequest(name=self.name, extra=struct)
        response: GetEndPositionResponse = \
            await self.client.GetEndPosition(request)
        return response.pose

    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None,
        extra: Optional[Dict[str, Any]] = None
    ):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = MoveToPositionRequest(name=self.name, to=pose, world_state=world_state, extra=struct)
        await self.client.MoveToPosition(request)

    async def get_joint_positions(self, extra: Optional[Dict[str, Any]] = None) -> JointPositions:
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = GetJointPositionsRequest(name=self.name, extra=struct)
        response: GetJointPositionsResponse = \
            await self.client.GetJointPositions(request)
        return response.positions

    async def move_to_joint_positions(self, positions: JointPositions, extra: Optional[Dict[str, Any]] = None):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = MoveToJointPositionsRequest(name=self.name, positions=positions, extra=struct)
        await self.client.MoveToJointPositions(request)

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = StopRequest(name=self.name, extra=struct)
        await self.client.Stop(request)

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
