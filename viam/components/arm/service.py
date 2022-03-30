from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.arm import (
    ArmServiceBase,
    GetEndPositionRequest, GetEndPositionResponse,
    MoveToPositionRequest, MoveToPositionResponse,
    GetJointPositionsRequest, GetJointPositionsResponse,
    MoveToJointPositionsRequest, MoveToJointPositionsResponse,
)

from .arm import Arm


class ArmService(ArmServiceBase, ComponentServiceBase[Arm]):
    """
    gRPC Service for an Arm
    """

    RESOURCE_TYPE = Arm

    async def GetEndPosition(
        self,
        stream: Stream[GetEndPositionRequest, GetEndPositionResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        position = await arm.get_end_position()
        response = GetEndPositionResponse(pose=position)
        await stream.send_message(response)

    async def MoveToPosition(
        self,
        stream: Stream[MoveToPositionRequest, MoveToPositionResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        obstacles = list(
            request.world_state.obstacles) if request.world_state else []
        await arm.move_to_position(request.to, obstacles)
        response = MoveToPositionResponse()
        await stream.send_message(response)

    async def GetJointPositions(
        self,
        stream: Stream[GetJointPositionsRequest, GetJointPositionsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        positions = await arm.get_joint_positions()
        response = GetJointPositionsResponse(position_degs=positions)
        await stream.send_message(response)

    async def MoveToJointPositions(
        self,
        stream: Stream[MoveToJointPositionsRequest,
                       MoveToJointPositionsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await arm.move_to_joint_positions(request.position_degs)
        response = MoveToJointPositionsResponse()
        await stream.send_message(response)
