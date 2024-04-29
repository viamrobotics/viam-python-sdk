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

    @abc.abstractmethod
    async def GetLinearAcceleration(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetLinearAccelerationRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearAccelerationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetReadings(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.movementsensor.v1.MovementSensorService/GetLinearVelocity': grpclib.const.Handler(self.GetLinearVelocity, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetAngularVelocity': grpclib.const.Handler(self.GetAngularVelocity, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetCompassHeading': grpclib.const.Handler(self.GetCompassHeading, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetOrientation': grpclib.const.Handler(self.GetOrientation, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, component.movementsensor.v1.movementsensor_pb2.GetPositionResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetAccuracy': grpclib.const.Handler(self.GetAccuracy, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetLinearAcceleration': grpclib.const.Handler(self.GetLinearAcceleration, grpclib.const.Cardinality.UNARY_UNARY, component.movementsensor.v1.movementsensor_pb2.GetLinearAccelerationRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearAccelerationResponse), '/viam.component.movementsensor.v1.MovementSensorService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse), '/viam.component.movementsensor.v1.MovementSensorService/GetReadings': grpclib.const.Handler(self.GetReadings, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse)}

class UnimplementedMovementSensorServiceBase(MovementSensorServiceBase):

    async def GetLinearVelocity(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetAngularVelocity(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetCompassHeading(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetOrientation(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPosition(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, component.movementsensor.v1.movementsensor_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetAccuracy(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetLinearAcceleration(self, stream: 'grpclib.server.Stream[component.movementsensor.v1.movementsensor_pb2.GetLinearAccelerationRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearAccelerationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetReadings(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class MovementSensorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetLinearVelocity = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetLinearVelocity', component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearVelocityResponse)
        self.GetAngularVelocity = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetAngularVelocity', component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityRequest, component.movementsensor.v1.movementsensor_pb2.GetAngularVelocityResponse)
        self.GetCompassHeading = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetCompassHeading', component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingRequest, component.movementsensor.v1.movementsensor_pb2.GetCompassHeadingResponse)
        self.GetOrientation = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetOrientation', component.movementsensor.v1.movementsensor_pb2.GetOrientationRequest, component.movementsensor.v1.movementsensor_pb2.GetOrientationResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetPosition', component.movementsensor.v1.movementsensor_pb2.GetPositionRequest, component.movementsensor.v1.movementsensor_pb2.GetPositionResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetProperties', component.movementsensor.v1.movementsensor_pb2.GetPropertiesRequest, component.movementsensor.v1.movementsensor_pb2.GetPropertiesResponse)
        self.GetAccuracy = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetAccuracy', component.movementsensor.v1.movementsensor_pb2.GetAccuracyRequest, component.movementsensor.v1.movementsensor_pb2.GetAccuracyResponse)
        self.GetLinearAcceleration = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetLinearAcceleration', component.movementsensor.v1.movementsensor_pb2.GetLinearAccelerationRequest, component.movementsensor.v1.movementsensor_pb2.GetLinearAccelerationResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)
        self.GetReadings = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.movementsensor.v1.MovementSensorService/GetReadings', common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse)