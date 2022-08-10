import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto

class MovementSensorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetLinearVelocity(self, stream: 'grpclib.server.Stream[proto.api.component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAngularVelocity(self, stream: 'grpclib.server.Stream[proto.api.component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCompassHeading(self, stream: 'grpclib.server.Stream[proto.api.component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOrientation(self, stream: 'grpclib.server.Stream[proto.api.component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[proto.api.component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[proto.api.component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAccuracy(self, stream: 'grpclib.server.Stream[proto.api.component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.movementsensor.v1.MovementSensorService/GetLinearVelocity': grpclib.const.Handler(self.GetLinearVelocity, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse), '/proto.api.component.movementsensor.v1.MovementSensorService/GetAngularVelocity': grpclib.const.Handler(self.GetAngularVelocity, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse), '/proto.api.component.movementsensor.v1.MovementSensorService/GetCompassHeading': grpclib.const.Handler(self.GetCompassHeading, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse), '/proto.api.component.movementsensor.v1.MovementSensorService/GetOrientation': grpclib.const.Handler(self.GetOrientation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse), '/proto.api.component.movementsensor.v1.MovementSensorService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetPositionResponse), '/proto.api.component.movementsensor.v1.MovementSensorService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse), '/proto.api.component.movementsensor.v1.MovementSensorService/GetAccuracy': grpclib.const.Handler(self.GetAccuracy, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse)}

class MovementSensorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetLinearVelocity = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.movementsensor.v1.MovementSensorService/GetLinearVelocity', proto.api.component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse)
        self.GetAngularVelocity = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.movementsensor.v1.MovementSensorService/GetAngularVelocity', proto.api.component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse)
        self.GetCompassHeading = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.movementsensor.v1.MovementSensorService/GetCompassHeading', proto.api.component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse)
        self.GetOrientation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.movementsensor.v1.MovementSensorService/GetOrientation', proto.api.component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.movementsensor.v1.MovementSensorService/GetPosition', proto.api.component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetPositionResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.movementsensor.v1.MovementSensorService/GetProperties', proto.api.component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse)
        self.GetAccuracy = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.movementsensor.v1.MovementSensorService/GetAccuracy', proto.api.component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, proto.api.component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse)