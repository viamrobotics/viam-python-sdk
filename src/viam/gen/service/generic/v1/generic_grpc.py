import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
from .... import service

class GenericServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.generic.v1.GenericService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedGenericServiceBase(GenericServiceBase):

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class GenericServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.generic.v1.GenericService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)