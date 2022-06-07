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
    async def Do(self, stream: 'grpclib.server.Stream[proto.api.component.generic.v1.generic_pb2.DoRequest, proto.api.component.generic.v1.generic_pb2.DoResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.generic.v1.GenericService/Do': grpclib.const.Handler(self.Do, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.generic.v1.generic_pb2.DoRequest, proto.api.component.generic.v1.generic_pb2.DoResponse)}

class GenericServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Do = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.generic.v1.GenericService/Do', proto.api.component.generic.v1.generic_pb2.DoRequest, proto.api.component.generic.v1.generic_pb2.DoResponse)