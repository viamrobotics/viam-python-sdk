import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
from .... import component

class SensorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetReadings(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.sensor.v1.SensorService/GetReadings': grpclib.const.Handler(self.GetReadings, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse), '/viam.component.sensor.v1.SensorService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.sensor.v1.SensorService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedSensorServiceBase(SensorServiceBase):

    async def GetReadings(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class SensorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetReadings = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.sensor.v1.SensorService/GetReadings', common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.sensor.v1.SensorService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.sensor.v1.SensorService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)