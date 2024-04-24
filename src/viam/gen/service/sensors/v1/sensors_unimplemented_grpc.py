import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service
from .sensors_grpc import SensorsServiceBase as _SensorsServiceBase

class UnimplementedSensorsServiceBase(_SensorsServiceBase):

    async def GetSensors(self, stream: 'grpclib.server.Stream[service.sensors.v1.sensors_pb2.GetSensorsRequest, service.sensors.v1.sensors_pb2.GetSensorsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetReadings(self, stream: 'grpclib.server.Stream[service.sensors.v1.sensors_pb2.GetReadingsRequest, service.sensors.v1.sensors_pb2.GetReadingsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)