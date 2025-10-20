from grpclib.server import Stream

from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
)
from viam.proto.component.audioout import (
    AudioOutServiceBase,
    PlayRequest,
    PlayResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .audio_out import AudioOut


class AudioOutRPCService(AudioOutServiceBase, ResourceRPCServiceBase[AudioOut]):
    """gRPC service for AudioOut component."""

    RESOURCE_TYPE = AudioOut

    async def Play(self, stream: Stream[PlayRequest, PlayResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        audio_out = self.get_resource(name)
        extra = struct_to_dict(request.extra)
        await audio_out.play(request.audio_data, request.audio_info, extra=extra)
        await stream.send_message(PlayResponse())

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        audio_out = self.get_resource(name)
        extra = struct_to_dict(request.extra)
        properties = await audio_out.get_properties(extra=extra)
        await stream.send_message(properties)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        audio_out = self.get_resource(request.name)
        result = await audio_out.do_command(struct_to_dict(request.command))
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

