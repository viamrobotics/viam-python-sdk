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
from .arm_grpc import ArmServiceBase as _ArmServiceBase

class UnimplementedArmServiceBase(_ArmServiceBase):

    async def GetEndPosition(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.GetEndPositionRequest, component.arm.v1.arm_pb2.GetEndPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def MoveToPosition(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.MoveToPositionRequest, component.arm.v1.arm_pb2.MoveToPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetJointPositions(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.GetJointPositionsRequest, component.arm.v1.arm_pb2.GetJointPositionsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def MoveToJointPositions(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.MoveToJointPositionsRequest, component.arm.v1.arm_pb2.MoveToJointPositionsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.StopRequest, component.arm.v1.arm_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def IsMoving(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.IsMovingRequest, component.arm.v1.arm_pb2.IsMovingResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetKinematics(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetKinematicsRequest, common.v1.common_pb2.GetKinematicsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)