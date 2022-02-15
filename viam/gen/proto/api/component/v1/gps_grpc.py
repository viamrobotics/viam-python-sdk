import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ..... import proto
from ..... import proto

class GPSServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ReadLocation(self, stream: 'grpclib.server.Stream[proto.api.component.v1.gps_pb2.GPSServiceReadLocationRequest, proto.api.component.v1.gps_pb2.GPSServiceReadLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadAltitude(self, stream: 'grpclib.server.Stream[proto.api.component.v1.gps_pb2.GPSServiceReadAltitudeRequest, proto.api.component.v1.gps_pb2.GPSServiceReadAltitudeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadSpeed(self, stream: 'grpclib.server.Stream[proto.api.component.v1.gps_pb2.GPSServiceReadSpeedRequest, proto.api.component.v1.gps_pb2.GPSServiceReadSpeedResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.GPSService/ReadLocation': grpclib.const.Handler(self.ReadLocation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.gps_pb2.GPSServiceReadLocationRequest, proto.api.component.v1.gps_pb2.GPSServiceReadLocationResponse), '/proto.api.component.v1.GPSService/ReadAltitude': grpclib.const.Handler(self.ReadAltitude, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.gps_pb2.GPSServiceReadAltitudeRequest, proto.api.component.v1.gps_pb2.GPSServiceReadAltitudeResponse), '/proto.api.component.v1.GPSService/ReadSpeed': grpclib.const.Handler(self.ReadSpeed, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.gps_pb2.GPSServiceReadSpeedRequest, proto.api.component.v1.gps_pb2.GPSServiceReadSpeedResponse)}

class GPSServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ReadLocation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.GPSService/ReadLocation', proto.api.component.v1.gps_pb2.GPSServiceReadLocationRequest, proto.api.component.v1.gps_pb2.GPSServiceReadLocationResponse)
        self.ReadAltitude = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.GPSService/ReadAltitude', proto.api.component.v1.gps_pb2.GPSServiceReadAltitudeRequest, proto.api.component.v1.gps_pb2.GPSServiceReadAltitudeResponse)
        self.ReadSpeed = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.GPSService/ReadSpeed', proto.api.component.v1.gps_pb2.GPSServiceReadSpeedRequest, proto.api.component.v1.gps_pb2.GPSServiceReadSpeedResponse)