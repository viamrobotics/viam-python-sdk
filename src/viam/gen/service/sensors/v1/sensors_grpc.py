import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service

class SensorsServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetSensors(self, stream: 'grpclib.server.Stream[service.sensors.v1.sensors_pb2.GetSensorsRequest, service.sensors.v1.sensors_pb2.GetSensorsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetReadings(self, stream: 'grpclib.server.Stream[service.sensors.v1.sensors_pb2.GetReadingsRequest, service.sensors.v1.sensors_pb2.GetReadingsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.sensors.v1.SensorsService/GetSensors': grpclib.const.Handler(self.GetSensors, grpclib.const.Cardinality.UNARY_UNARY, service.sensors.v1.sensors_pb2.GetSensorsRequest, service.sensors.v1.sensors_pb2.GetSensorsResponse), '/viam.service.sensors.v1.SensorsService/GetReadings': grpclib.const.Handler(self.GetReadings, grpclib.const.Cardinality.UNARY_UNARY, service.sensors.v1.sensors_pb2.GetReadingsRequest, service.sensors.v1.sensors_pb2.GetReadingsResponse), '/viam.service.sensors.v1.SensorsService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedSensorsServiceBase(SensorsServiceBase):

    async def GetSensors(self, stream: 'grpclib.server.Stream[service.sensors.v1.sensors_pb2.GetSensorsRequest, service.sensors.v1.sensors_pb2.GetSensorsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetReadings(self, stream: 'grpclib.server.Stream[service.sensors.v1.sensors_pb2.GetReadingsRequest, service.sensors.v1.sensors_pb2.GetReadingsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class SensorsServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSensors = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.sensors.v1.SensorsService/GetSensors', service.sensors.v1.sensors_pb2.GetSensorsRequest, service.sensors.v1.sensors_pb2.GetSensorsResponse)
        self.GetReadings = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.sensors.v1.SensorsService/GetReadings', service.sensors.v1.sensors_pb2.GetReadingsRequest, service.sensors.v1.sensors_pb2.GetReadingsResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.sensors.v1.SensorsService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)