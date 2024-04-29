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

class GripperServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Open(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.OpenRequest, component.gripper.v1.gripper_pb2.OpenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Grab(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.GrabRequest, component.gripper.v1.gripper_pb2.GrabResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.StopRequest, component.gripper.v1.gripper_pb2.StopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IsMoving(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.IsMovingRequest, component.gripper.v1.gripper_pb2.IsMovingResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.gripper.v1.GripperService/Open': grpclib.const.Handler(self.Open, grpclib.const.Cardinality.UNARY_UNARY, component.gripper.v1.gripper_pb2.OpenRequest, component.gripper.v1.gripper_pb2.OpenResponse), '/viam.component.gripper.v1.GripperService/Grab': grpclib.const.Handler(self.Grab, grpclib.const.Cardinality.UNARY_UNARY, component.gripper.v1.gripper_pb2.GrabRequest, component.gripper.v1.gripper_pb2.GrabResponse), '/viam.component.gripper.v1.GripperService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, component.gripper.v1.gripper_pb2.StopRequest, component.gripper.v1.gripper_pb2.StopResponse), '/viam.component.gripper.v1.GripperService/IsMoving': grpclib.const.Handler(self.IsMoving, grpclib.const.Cardinality.UNARY_UNARY, component.gripper.v1.gripper_pb2.IsMovingRequest, component.gripper.v1.gripper_pb2.IsMovingResponse), '/viam.component.gripper.v1.GripperService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.gripper.v1.GripperService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedGripperServiceBase(GripperServiceBase):

    async def Open(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.OpenRequest, component.gripper.v1.gripper_pb2.OpenResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Grab(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.GrabRequest, component.gripper.v1.gripper_pb2.GrabResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.StopRequest, component.gripper.v1.gripper_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def IsMoving(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.IsMovingRequest, component.gripper.v1.gripper_pb2.IsMovingResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class GripperServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Open = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/Open', component.gripper.v1.gripper_pb2.OpenRequest, component.gripper.v1.gripper_pb2.OpenResponse)
        self.Grab = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/Grab', component.gripper.v1.gripper_pb2.GrabRequest, component.gripper.v1.gripper_pb2.GrabResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/Stop', component.gripper.v1.gripper_pb2.StopRequest, component.gripper.v1.gripper_pb2.StopResponse)
        self.IsMoving = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/IsMoving', component.gripper.v1.gripper_pb2.IsMovingRequest, component.gripper.v1.gripper_pb2.IsMovingResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)