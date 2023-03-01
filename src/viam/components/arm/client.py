from typing import Any, SupportsBytes, Dict, SupportsFloat, SupportsInt, List, Mapping, Optional, Union

from grpclib.client import Channel

from viam.proto.common import Pose, WorldState, DoCommandRequest, DoCommandResponse
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
from viam.utils import dict_to_struct, struct_to_dict

from .arm import Arm


DoCommandTypes = Union[bool, SupportsBytes, SupportsFloat, SupportsInt, List, Mapping, str, None]


class ArmClient(Arm):
    """
    gRPC client for an Arm component.

    Used to communicate with an existing ``Arm`` implementation over gRPC.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = ArmServiceStub(channel)
        super().__init__(name)

    async def get_end_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Pose:
        if extra is None:
            extra = {}
        request = GetEndPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetEndPositionResponse = await self.client.GetEndPosition(request, timeout=timeout)
        return response.pose

    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = MoveToPositionRequest(name=self.name, to=pose, world_state=world_state, extra=dict_to_struct(extra))
        await self.client.MoveToPosition(request, timeout=timeout)

    async def get_joint_positions(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> JointPositions:
        if extra is None:
            extra = {}
        request = GetJointPositionsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetJointPositionsResponse = await self.client.GetJointPositions(request, timeout=timeout)
        return response.positions

    async def move_to_joint_positions(
        self,
        positions: JointPositions,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = MoveToJointPositionsRequest(name=self.name, positions=positions, extra=dict_to_struct(extra))
        await self.client.MoveToJointPositions(request, timeout=timeout)

    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request, timeout=timeout)

    async def is_moving(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> bool:
        if extra is None:
            extra = {}
        request = IsMovingRequest(name=self.name)
        response: IsMovingResponse = await self.client.IsMoving(request, timeout=timeout)
        return response.is_moving

    async def do_command(
        self,
        command: Dict[str, DoCommandTypes],
        *,
        timeout: Optional[float] = None,
    ) -> Dict[str, DoCommandTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
