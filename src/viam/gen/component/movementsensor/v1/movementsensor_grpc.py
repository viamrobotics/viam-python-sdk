import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
from .... import component

class MovementSensorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetLinearVelocity(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAngularVelocity(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCompassHeading(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOrientation(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, component.movementsensor.v1.movementsensor_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAccuracy(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.movementsensor.v1.MovementSensorService/GetLinearVelocity': grpclib.const.Handler(self.GetLinearVelocity, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetAngularVelocity': grpclib.const.Handler(self.GetAngularVelocity, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetCompassHeading': grpclib.const.Handler(self.GetCompassHeading, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetOrientation': grpclib.const.Handler(self.GetOrientation, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, component.movementsensor.v1.movementsensor_pb2.GetPositionResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetAccuracy': grpclib.const.Handler(self.GetAccuracy, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse)}

class MovementSensorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetLinearVelocity = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetLinearVelocity', component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse)
        self.GetAngularVelocity = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetAngularVelocity', component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse)
        self.GetCompassHeading = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetCompassHeading', component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse)
        self.GetOrientation = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetOrientation', component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetPosition', component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, component.movementsensor.v1.movementsensor_pb2.GetPositionResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetProperties', component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse)
        self.GetAccuracy = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetAccuracy', component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse)