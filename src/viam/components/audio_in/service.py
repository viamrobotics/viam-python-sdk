from grpclib.server import Stream
from h2.exceptions import StreamClosedError

from viam.logging import getLogger
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
)
from viam.proto.component.audioin import AudioInServiceBase, GetAudioRequest, GetAudioResponse
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .audio_in import AudioIn

LOGGER = getLogger(__name__)


class AudioInRPCService(AudioInServiceBase, ResourceRPCServiceBase[AudioIn]):
    """
    gRPC Service for a generic audio in.
    """

    RESOURCE_TYPE = AudioIn

    async def GetAudio(self, stream: Stream[GetAudioRequest, GetAudioResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        audio_in = self.get_resource(name)
        audio_stream = await audio_in.get_audio(
            codec=request.codec,
            duration_seconds=request.duration_seconds,
            previous_timestamp_ns=request.previous_timestamp_nanoseconds,
            metadata=stream.metadata,
        )
        async for response in audio_stream:
            try:
                response.request_id = request.request_id
                await stream.send_message(response)
            except StreamClosedError:
                return
            except Exception as e:
                LOGGER.error(e)
                return

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        audio_in = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        properties = await audio_in.get_properties(
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(properties)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        audio_in = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await audio_in.do_command(
            command=struct_to_dict(request.command),
            timeout=timeout,
            metadata=stream.metadata,
        )
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
