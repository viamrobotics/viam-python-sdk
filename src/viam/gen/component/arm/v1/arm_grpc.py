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

class ArmServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetEndPosition(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.GetEndPositionRequest, component.arm.v1.arm_pb2.GetEndPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveToPosition(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.MoveToPositionRequest, component.arm.v1.arm_pb2.MoveToPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetJointPositions(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.GetJointPositionsRequest, component.arm.v1.arm_pb2.GetJointPositionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveToJointPositions(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.MoveToJointPositionsRequest, component.arm.v1.arm_pb2.MoveToJointPositionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.StopRequest, component.arm.v1.arm_pb2.StopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IsMoving(self, stream: 'grpclib.server.Stream[component.arm.v1.arm_pb2.IsMovingRequest, component.arm.v1.arm_pb2.IsMovingResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetKinematics(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetKinematicsRequest, common.v1.common_pb2.GetKinematicsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.arm.v1.ArmService/GetEndPosition': grpclib.const.Handler(self.GetEndPosition, grpclib.const.Cardinality.UNARY_UNARY, component.arm.v1.arm_pb2.GetEndPositionRequest, component.arm.v1.arm_pb2.GetEndPositionResponse), '/viam.component.arm.v1.ArmService/MoveToPosition': grpclib.const.Handler(self.MoveToPosition, grpclib.const.Cardinality.UNARY_UNARY, component.arm.v1.arm_pb2.MoveToPositionRequest, component.arm.v1.arm_pb2.MoveToPositionResponse), '/viam.component.arm.v1.ArmService/GetJointPositions': grpclib.const.Handler(self.GetJointPositions, grpclib.const.Cardinality.UNARY_UNARY, component.arm.v1.arm_pb2.GetJointPositionsRequest, component.arm.v1.arm_pb2.GetJointPositionsResponse), '/viam.component.arm.v1.ArmService/MoveToJointPositions': grpclib.const.Handler(self.MoveToJointPositions, grpclib.const.Cardinality.UNARY_UNARY, component.arm.v1.arm_pb2.MoveToJointPositionsRequest, component.arm.v1.arm_pb2.MoveToJointPositionsResponse), '/viam.component.arm.v1.ArmService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, component.arm.v1.arm_pb2.StopRequest, component.arm.v1.arm_pb2.StopResponse), '/viam.component.arm.v1.ArmService/IsMoving': grpclib.const.Handler(self.IsMoving, grpclib.const.Cardinality.UNARY_UNARY, component.arm.v1.arm_pb2.IsMovingRequest, component.arm.v1.arm_pb2.IsMovingResponse), '/viam.component.arm.v1.ArmService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.arm.v1.ArmService/GetKinematics': grpclib.const.Handler(self.GetKinematics, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetKinematicsRequest, common.v1.common_pb2.GetKinematicsResponse), '/viam.component.arm.v1.ArmService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedArmServiceBase(ArmServiceBase):

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

class ArmServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetEndPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/GetEndPosition', component.arm.v1.arm_pb2.GetEndPositionRequest, component.arm.v1.arm_pb2.GetEndPositionResponse)
        self.MoveToPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/MoveToPosition', component.arm.v1.arm_pb2.MoveToPositionRequest, component.arm.v1.arm_pb2.MoveToPositionResponse)
        self.GetJointPositions = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/GetJointPositions', component.arm.v1.arm_pb2.GetJointPositionsRequest, component.arm.v1.arm_pb2.GetJointPositionsResponse)
        self.MoveToJointPositions = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/MoveToJointPositions', component.arm.v1.arm_pb2.MoveToJointPositionsRequest, component.arm.v1.arm_pb2.MoveToJointPositionsResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/Stop', component.arm.v1.arm_pb2.StopRequest, component.arm.v1.arm_pb2.StopResponse)
        self.IsMoving = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/IsMoving', component.arm.v1.arm_pb2.IsMovingRequest, component.arm.v1.arm_pb2.IsMovingResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetKinematics = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/GetKinematics', common.v1.common_pb2.GetKinematicsRequest, common.v1.common_pb2.GetKinematicsResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.arm.v1.ArmService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)