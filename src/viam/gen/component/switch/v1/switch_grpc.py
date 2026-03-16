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

class SwitchServiceBase(abc.ABC):

    @abc.abstractmethod
    async def SetPosition(self, stream: 'grpclib.server.Stream[component.switch.v1.switch_pb2.SetPositionRequest, component.switch.v1.switch_pb2.SetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[component.switch.v1.switch_pb2.GetPositionRequest, component.switch.v1.switch_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetNumberOfPositions(self, stream: 'grpclib.server.Stream[component.switch.v1.switch_pb2.GetNumberOfPositionsRequest, component.switch.v1.switch_pb2.GetNumberOfPositionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.switch.v1.SwitchService/SetPosition': grpclib.const.Handler(self.SetPosition, grpclib.const.Cardinality.UNARY_UNARY, component.switch.v1.switch_pb2.SetPositionRequest, component.switch.v1.switch_pb2.SetPositionResponse), '/viam.component.switch.v1.SwitchService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, component.switch.v1.switch_pb2.GetPositionRequest, component.switch.v1.switch_pb2.GetPositionResponse), '/viam.component.switch.v1.SwitchService/GetNumberOfPositions': grpclib.const.Handler(self.GetNumberOfPositions, grpclib.const.Cardinality.UNARY_UNARY, component.switch.v1.switch_pb2.GetNumberOfPositionsRequest, component.switch.v1.switch_pb2.GetNumberOfPositionsResponse), '/viam.component.switch.v1.SwitchService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedSwitchServiceBase(SwitchServiceBase):

    async def SetPosition(self, stream: 'grpclib.server.Stream[component.switch.v1.switch_pb2.SetPositionRequest, component.switch.v1.switch_pb2.SetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPosition(self, stream: 'grpclib.server.Stream[component.switch.v1.switch_pb2.GetPositionRequest, component.switch.v1.switch_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetNumberOfPositions(self, stream: 'grpclib.server.Stream[component.switch.v1.switch_pb2.GetNumberOfPositionsRequest, component.switch.v1.switch_pb2.GetNumberOfPositionsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class SwitchServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.switch.v1.SwitchService/SetPosition', component.switch.v1.switch_pb2.SetPositionRequest, component.switch.v1.switch_pb2.SetPositionResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.switch.v1.SwitchService/GetPosition', component.switch.v1.switch_pb2.GetPositionRequest, component.switch.v1.switch_pb2.GetPositionResponse)
        self.GetNumberOfPositions = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.switch.v1.SwitchService/GetNumberOfPositions', component.switch.v1.switch_pb2.GetNumberOfPositionsRequest, component.switch.v1.switch_pb2.GetNumberOfPositionsResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.switch.v1.SwitchService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)