from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.encoder import (
    EncoderServiceBase,
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    ResetPositionRequest,
    ResetPositionResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .encoder import Encoder


class EncoderRPCService(EncoderServiceBase, ResourceRPCServiceBase[Encoder]):
    """
    gRPC Service for an Encoder
    """

    RESOURCE_TYPE = Encoder

    async def ResetPosition(self, stream: Stream[ResetPositionRequest, ResetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        encoder = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await encoder.reset_position(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(ResetPositionResponse())

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        encoder = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position, pos_type = await encoder.get_position(
            position_type=request.position_type, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(GetPositionResponse(value=position, position_type=pos_type))

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        encoder = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        properties = await encoder.get_properties(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetPropertiesResponse(**properties.__dict__)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        encoder = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await encoder.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        arm = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await arm.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
