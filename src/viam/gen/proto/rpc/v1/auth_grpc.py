import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from .... import proto

class AuthServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Authenticate(self, stream: 'grpclib.server.Stream[proto.rpc.v1.auth_pb2.AuthenticateRequest, proto.rpc.v1.auth_pb2.AuthenticateResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.rpc.v1.AuthService/Authenticate': grpclib.const.Handler(self.Authenticate, grpclib.const.Cardinality.UNARY_UNARY, proto.rpc.v1.auth_pb2.AuthenticateRequest, proto.rpc.v1.auth_pb2.AuthenticateResponse)}

class AuthServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Authenticate = grpclib.client.UnaryUnaryMethod(channel, '/proto.rpc.v1.AuthService/Authenticate', proto.rpc.v1.auth_pb2.AuthenticateRequest, proto.rpc.v1.auth_pb2.AuthenticateResponse)

class ExternalAuthServiceBase(abc.ABC):

    @abc.abstractmethod
    async def AuthenticateTo(self, stream: 'grpclib.server.Stream[proto.rpc.v1.auth_pb2.AuthenticateToRequest, proto.rpc.v1.auth_pb2.AuthenticateToResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.rpc.v1.ExternalAuthService/AuthenticateTo': grpclib.const.Handler(self.AuthenticateTo, grpclib.const.Cardinality.UNARY_UNARY, proto.rpc.v1.auth_pb2.AuthenticateToRequest, proto.rpc.v1.auth_pb2.AuthenticateToResponse)}

class ExternalAuthServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AuthenticateTo = grpclib.client.UnaryUnaryMethod(channel, '/proto.rpc.v1.ExternalAuthService/AuthenticateTo', proto.rpc.v1.auth_pb2.AuthenticateToRequest, proto.rpc.v1.auth_pb2.AuthenticateToResponse)