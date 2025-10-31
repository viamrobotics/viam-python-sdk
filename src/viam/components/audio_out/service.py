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
        # Check if audio_info was provided in the request
        audio_info = request.audio_info if request.HasField("audio_info") else None
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await audio_out.play(request.audio_data, audio_info, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(PlayResponse())

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        audio_out = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        properties = await audio_out.get_properties(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(properties)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        audio_out = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await audio_out.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        audio_out = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await audio_out.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
