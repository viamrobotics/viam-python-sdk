import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component
from .movementsensor_grpc import MovementSensorServiceBase as _MovementSensorServiceBase

class UnimplementedMovementSensorServiceBase(_MovementSensorServiceBase):

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