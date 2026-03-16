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

class BaseServiceBase(abc.ABC):

    @abc.abstractmethod
    async def MoveStraight(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.MoveStraightRequest, component.base.v1.base_pb2.MoveStraightResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Spin(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SpinRequest, component.base.v1.base_pb2.SpinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPower(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SetPowerRequest, component.base.v1.base_pb2.SetPowerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetVelocity(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SetVelocityRequest, component.base.v1.base_pb2.SetVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.StopRequest, component.base.v1.base_pb2.StopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IsMoving(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.IsMovingRequest, component.base.v1.base_pb2.IsMovingResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.GetPropertiesRequest, component.base.v1.base_pb2.GetPropertiesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.base.v1.BaseService/MoveStraight': grpclib.const.Handler(self.MoveStraight, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.MoveStraightRequest, component.base.v1.base_pb2.MoveStraightResponse), '/viam.component.base.v1.BaseService/Spin': grpclib.const.Handler(self.Spin, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.SpinRequest, component.base.v1.base_pb2.SpinResponse), '/viam.component.base.v1.BaseService/SetPower': grpclib.const.Handler(self.SetPower, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.SetPowerRequest, component.base.v1.base_pb2.SetPowerResponse), '/viam.component.base.v1.BaseService/SetVelocity': grpclib.const.Handler(self.SetVelocity, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.SetVelocityRequest, component.base.v1.base_pb2.SetVelocityResponse), '/viam.component.base.v1.BaseService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.StopRequest, component.base.v1.base_pb2.StopResponse), '/viam.component.base.v1.BaseService/IsMoving': grpclib.const.Handler(self.IsMoving, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.IsMovingRequest, component.base.v1.base_pb2.IsMovingResponse), '/viam.component.base.v1.BaseService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.base.v1.BaseService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse), '/viam.component.base.v1.BaseService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.GetPropertiesRequest, component.base.v1.base_pb2.GetPropertiesResponse)}

class UnimplementedBaseServiceBase(BaseServiceBase):

    async def MoveStraight(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.MoveStraightRequest, component.base.v1.base_pb2.MoveStraightResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Spin(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SpinRequest, component.base.v1.base_pb2.SpinResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetPower(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SetPowerRequest, component.base.v1.base_pb2.SetPowerResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetVelocity(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SetVelocityRequest, component.base.v1.base_pb2.SetVelocityResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.StopRequest, component.base.v1.base_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def IsMoving(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.IsMovingRequest, component.base.v1.base_pb2.IsMovingResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.GetPropertiesRequest, component.base.v1.base_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class BaseServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.MoveStraight = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/MoveStraight', component.base.v1.base_pb2.MoveStraightRequest, component.base.v1.base_pb2.MoveStraightResponse)
        self.Spin = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/Spin', component.base.v1.base_pb2.SpinRequest, component.base.v1.base_pb2.SpinResponse)
        self.SetPower = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/SetPower', component.base.v1.base_pb2.SetPowerRequest, component.base.v1.base_pb2.SetPowerResponse)
        self.SetVelocity = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/SetVelocity', component.base.v1.base_pb2.SetVelocityRequest, component.base.v1.base_pb2.SetVelocityResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/Stop', component.base.v1.base_pb2.StopRequest, component.base.v1.base_pb2.StopResponse)
        self.IsMoving = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/IsMoving', component.base.v1.base_pb2.IsMovingRequest, component.base.v1.base_pb2.IsMovingResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/GetProperties', component.base.v1.base_pb2.GetPropertiesRequest, component.base.v1.base_pb2.GetPropertiesResponse)