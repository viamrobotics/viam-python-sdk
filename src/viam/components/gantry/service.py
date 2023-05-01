from grpclib.server import Stream

from viam.errors import ResourceNotFoundError
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.gantry import (
    GantryServiceBase,
    GetLengthsRequest,
    GetLengthsResponse,
    GetPositionRequest,
    GetPositionResponse,
    IsMovingRequest,
    IsMovingResponse,
    MoveToPositionRequest,
    MoveToPositionResponse,
    StopRequest,
    StopResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .gantry import Gantry


class GantryRPCService(GantryServiceBase, ResourceRPCServiceBase[Gantry]):
    """
    gRPC Service for a Gantry
    """

    RESOURCE_TYPE = Gantry

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gantry = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await gantry.get_position(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetPositionResponse(positions_mm=position)
        await stream.send_message(response)

    async def MoveToPosition(self, stream: Stream[MoveToPositionRequest, MoveToPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gantry = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await gantry.move_to_position(
            list(request.positions_mm), extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        response = MoveToPositionResponse()
        await stream.send_message(response)

    async def GetLengths(self, stream: Stream[GetLengthsRequest, GetLengthsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gantry = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        lengths = await gantry.get_lengths(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetLengthsResponse(lengths_mm=lengths)
        await stream.send_message(response)

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gantry = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await gantry.stop(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = StopResponse()
        await stream.send_message(response)

    async def IsMoving(self, stream: Stream[IsMovingRequest, IsMovingResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gantry = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        is_moving = await gantry.is_moving()
        response = IsMovingResponse(is_moving=is_moving)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            gantry = self.get_resource(request.name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await gantry.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
