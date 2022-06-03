import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.struct_pb2
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class SensorsServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetSensors(self, stream: 'grpclib.server.Stream[proto.api.service.sensors.v1.sensors_pb2.GetSensorsRequest, proto.api.service.sensors.v1.sensors_pb2.GetSensorsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetReadings(self, stream: 'grpclib.server.Stream[proto.api.service.sensors.v1.sensors_pb2.GetReadingsRequest, proto.api.service.sensors.v1.sensors_pb2.GetReadingsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.sensors.v1.SensorsService/GetSensors': grpclib.const.Handler(self.GetSensors, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.sensors.v1.sensors_pb2.GetSensorsRequest, proto.api.service.sensors.v1.sensors_pb2.GetSensorsResponse), '/proto.api.service.sensors.v1.SensorsService/GetReadings': grpclib.const.Handler(self.GetReadings, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.sensors.v1.sensors_pb2.GetReadingsRequest, proto.api.service.sensors.v1.sensors_pb2.GetReadingsResponse)}

class SensorsServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSensors = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.sensors.v1.SensorsService/GetSensors', proto.api.service.sensors.v1.sensors_pb2.GetSensorsRequest, proto.api.service.sensors.v1.sensors_pb2.GetSensorsResponse)
        self.GetReadings = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.sensors.v1.SensorsService/GetReadings', proto.api.service.sensors.v1.sensors_pb2.GetReadingsRequest, proto.api.service.sensors.v1.sensors_pb2.GetReadingsResponse)