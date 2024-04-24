import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import app
from .end_user_grpc import EndUserServiceBase as _EndUserServiceBase

class UnimplementedEndUserServiceBase(_EndUserServiceBase):

    async def IsLegalAccepted(self, stream: 'grpclib.server.Stream[app.v1.end_user_pb2.IsLegalAcceptedRequest, app.v1.end_user_pb2.IsLegalAcceptedResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AcceptLegal(self, stream: 'grpclib.server.Stream[app.v1.end_user_pb2.AcceptLegalRequest, app.v1.end_user_pb2.AcceptLegalResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RegisterAuthApplication(self, stream: 'grpclib.server.Stream[app.v1.end_user_pb2.RegisterAuthApplicationRequest, app.v1.end_user_pb2.RegisterAuthApplicationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateAuthApplication(self, stream: 'grpclib.server.Stream[app.v1.end_user_pb2.UpdateAuthApplicationRequest, app.v1.end_user_pb2.UpdateAuthApplicationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)