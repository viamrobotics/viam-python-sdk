import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import app

class EndUserServiceBase(abc.ABC):

    @abc.abstractmethod
    async def IsLegalAccepted(self, stream: 'grpclib.server.Stream[app.v1.end_user_pb2.IsLegalAcceptedRequest, app.v1.end_user_pb2.IsLegalAcceptedResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AcceptLegal(self, stream: 'grpclib.server.Stream[app.v1.end_user_pb2.AcceptLegalRequest, app.v1.end_user_pb2.AcceptLegalResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RegisterAuthApplication(self, stream: 'grpclib.server.Stream[app.v1.end_user_pb2.RegisterAuthApplicationRequest, app.v1.end_user_pb2.RegisterAuthApplicationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateAuthApplication(self, stream: 'grpclib.server.Stream[app.v1.end_user_pb2.UpdateAuthApplicationRequest, app.v1.end_user_pb2.UpdateAuthApplicationResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.v1.EndUserService/IsLegalAccepted': grpclib.const.Handler(self.IsLegalAccepted, grpclib.const.Cardinality.UNARY_UNARY, app.v1.end_user_pb2.IsLegalAcceptedRequest, app.v1.end_user_pb2.IsLegalAcceptedResponse), '/viam.app.v1.EndUserService/AcceptLegal': grpclib.const.Handler(self.AcceptLegal, grpclib.const.Cardinality.UNARY_UNARY, app.v1.end_user_pb2.AcceptLegalRequest, app.v1.end_user_pb2.AcceptLegalResponse), '/viam.app.v1.EndUserService/RegisterAuthApplication': grpclib.const.Handler(self.RegisterAuthApplication, grpclib.const.Cardinality.UNARY_UNARY, app.v1.end_user_pb2.RegisterAuthApplicationRequest, app.v1.end_user_pb2.RegisterAuthApplicationResponse), '/viam.app.v1.EndUserService/UpdateAuthApplication': grpclib.const.Handler(self.UpdateAuthApplication, grpclib.const.Cardinality.UNARY_UNARY, app.v1.end_user_pb2.UpdateAuthApplicationRequest, app.v1.end_user_pb2.UpdateAuthApplicationResponse)}

class EndUserServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.IsLegalAccepted = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.EndUserService/IsLegalAccepted', app.v1.end_user_pb2.IsLegalAcceptedRequest, app.v1.end_user_pb2.IsLegalAcceptedResponse)
        self.AcceptLegal = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.EndUserService/AcceptLegal', app.v1.end_user_pb2.AcceptLegalRequest, app.v1.end_user_pb2.AcceptLegalResponse)
        self.RegisterAuthApplication = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.EndUserService/RegisterAuthApplication', app.v1.end_user_pb2.RegisterAuthApplicationRequest, app.v1.end_user_pb2.RegisterAuthApplicationResponse)
        self.UpdateAuthApplication = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.EndUserService/UpdateAuthApplication', app.v1.end_user_pb2.UpdateAuthApplicationRequest, app.v1.end_user_pb2.UpdateAuthApplicationResponse)