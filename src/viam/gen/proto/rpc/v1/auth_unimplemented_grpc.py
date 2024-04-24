import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from .... import proto
from .auth_grpc import AuthServiceBase as _AuthServiceBase

class UnimplementedAuthServiceBase(_AuthServiceBase):

    async def Authenticate(self, stream: 'grpclib.server.Stream[proto.rpc.v1.auth_pb2.AuthenticateRequest, proto.rpc.v1.auth_pb2.AuthenticateResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)
from .auth_grpc import ExternalAuthServiceBase as _ExternalAuthServiceBase

class UnimplementedExternalAuthServiceBase(_ExternalAuthServiceBase):

    async def AuthenticateTo(self, stream: 'grpclib.server.Stream[proto.rpc.v1.auth_pb2.AuthenticateToRequest, proto.rpc.v1.auth_pb2.AuthenticateToResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)