import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component

class SensorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetReadings(self, stream: 'grpclib.server.Stream[component.sensor.v1.sensor_pb2.GetReadingsRequest, component.sensor.v1.sensor_pb2.GetReadingsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.sensor.v1.SensorService/GetReadings': grpclib.const.Handler(self.GetReadings, grpclib.const.Cardinality.UNARY_UNARY, component.sensor.v1.sensor_pb2.GetReadingsRequest, component.sensor.v1.sensor_pb2.GetReadingsResponse)}

class SensorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetReadings = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.sensor.v1.SensorService/GetReadings', component.sensor.v1.sensor_pb2.GetReadingsRequest, component.sensor.v1.sensor_pb2.GetReadingsResponse)