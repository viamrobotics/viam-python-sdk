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

class ButtonServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Push(self, stream: 'grpclib.server.Stream[component.button.v1.button_pb2.PushRequest, component.button.v1.button_pb2.PushResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.button.v1.ButtonService/Push': grpclib.const.Handler(self.Push, grpclib.const.Cardinality.UNARY_UNARY, component.button.v1.button_pb2.PushRequest, component.button.v1.button_pb2.PushResponse), '/viam.component.button.v1.ButtonService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedButtonServiceBase(ButtonServiceBase):

    async def Push(self, stream: 'grpclib.server.Stream[component.button.v1.button_pb2.PushRequest, component.button.v1.button_pb2.PushResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class ButtonServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Push = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.button.v1.ButtonService/Push', component.button.v1.button_pb2.PushRequest, component.button.v1.button_pb2.PushResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.button.v1.ButtonService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)