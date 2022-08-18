from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.arm import (
    ArmServiceBase,
    GetEndPositionRequest,
    GetEndPositionResponse,
    GetJointPositionsRequest,
    GetJointPositionsResponse,
    MoveToJointPositionsRequest,
    MoveToJointPositionsResponse,
    MoveToPositionRequest,
    MoveToPositionResponse,
    StopRequest,
    StopResponse,
)
from viam.utils import struct_to_dict

from .arm import Arm


class ArmService(ArmServiceBase, ComponentServiceBase[Arm]):
    """
    gRPC Service for an Arm
    """

    RESOURCE_TYPE = Arm

    async def GetEndPosition(self, stream: Stream[GetEndPositionRequest, GetEndPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        position = await self.run_with_operation(arm.get_end_position, extra=struct_to_dict(request.extra))
        response = GetEndPositionResponse(pose=position)
        await stream.send_message(response)

    async def MoveToPosition(self, stream: Stream[MoveToPositionRequest, MoveToPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await self.run_with_operation(arm.move_to_position, request.to, request.world_state, extra=struct_to_dict(request.extra))
        response = MoveToPositionResponse()
        await stream.send_message(response)

    async def GetJointPositions(self, stream: Stream[GetJointPositionsRequest, GetJointPositionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        positions = await self.run_with_operation(arm.get_joint_positions, extra=struct_to_dict(request.extra))
        response = GetJointPositionsResponse(positions=positions)
        await stream.send_message(response)

    async def MoveToJointPositions(self, stream: Stream[MoveToJointPositionsRequest, MoveToJointPositionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await self.run_with_operation(arm.move_to_joint_positions, request.positions, extra=struct_to_dict(request.extra))
        response = MoveToJointPositionsResponse()
        await stream.send_message(response)

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await self.run_with_operation(arm.stop, extra=struct_to_dict(request.extra))
        response = StopResponse()
        await stream.send_message(response)
