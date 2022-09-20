import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component

class GenericServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[component.generic.v1.generic_pb2.DoCommandRequest, component.generic.v1.generic_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.generic.v1.GenericService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, component.generic.v1.generic_pb2.DoCommandRequest, component.generic.v1.generic_pb2.DoCommandResponse)}

class GenericServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.generic.v1.GenericService/DoCommand', component.generic.v1.generic_pb2.DoCommandRequest, component.generic.v1.generic_pb2.DoCommandResponse)