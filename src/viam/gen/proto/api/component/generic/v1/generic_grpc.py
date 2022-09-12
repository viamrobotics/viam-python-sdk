import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from ...... import proto

class GenericServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[proto.api.component.generic.v1.generic_pb2.DoCommandRequest, proto.api.component.generic.v1.generic_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.generic.v1.GenericService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.generic.v1.generic_pb2.DoCommandRequest, proto.api.component.generic.v1.generic_pb2.DoCommandResponse)}

class GenericServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.generic.v1.GenericService/DoCommand', proto.api.component.generic.v1.generic_pb2.DoCommandRequest, proto.api.component.generic.v1.generic_pb2.DoCommandResponse)