import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from ... import tagger
from ... import app

class AppServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListOrganizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListOrganizationsRequest, app.v1.app_pb2.ListOrganizationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListLocations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListLocationsRequest, app.v1.app_pb2.ListLocationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def LocationAuth(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.LocationAuthRequest, app.v1.app_pb2.LocationAuthResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotRequest, app.v1.app_pb2.GetRobotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotParts(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartsRequest, app.v1.app_pb2.GetRobotPartsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartRequest, app.v1.app_pb2.GetRobotPartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotPartLogs(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartLogsRequest, app.v1.app_pb2.GetRobotPartLogsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TailRobotPartLogs(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.TailRobotPartLogsRequest, app.v1.app_pb2.TailRobotPartLogsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotPartHistory(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartHistoryRequest, app.v1.app_pb2.GetRobotPartHistoryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateRobotPartRequest, app.v1.app_pb2.UpdateRobotPartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NewRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.NewRobotPartRequest, app.v1.app_pb2.NewRobotPartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRobotPartRequest, app.v1.app_pb2.DeleteRobotPartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MarkPartAsMain(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.MarkPartAsMainRequest, app.v1.app_pb2.MarkPartAsMainResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FindRobots(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.FindRobotsRequest, app.v1.app_pb2.FindRobotsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NewRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.NewRobotRequest, app.v1.app_pb2.NewRobotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateRobotRequest, app.v1.app_pb2.UpdateRobotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRobotRequest, app.v1.app_pb2.DeleteRobotResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.v1.AppService/ListOrganizations': grpclib.const.Handler(self.ListOrganizations, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListOrganizationsRequest, app.v1.app_pb2.ListOrganizationsResponse), '/viam.app.v1.AppService/ListLocations': grpclib.const.Handler(self.ListLocations, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListLocationsRequest, app.v1.app_pb2.ListLocationsResponse), '/viam.app.v1.AppService/LocationAuth': grpclib.const.Handler(self.LocationAuth, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.LocationAuthRequest, app.v1.app_pb2.LocationAuthResponse), '/viam.app.v1.AppService/GetRobot': grpclib.const.Handler(self.GetRobot, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotRequest, app.v1.app_pb2.GetRobotResponse), '/viam.app.v1.AppService/GetRobotParts': grpclib.const.Handler(self.GetRobotParts, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotPartsRequest, app.v1.app_pb2.GetRobotPartsResponse), '/viam.app.v1.AppService/GetRobotPart': grpclib.const.Handler(self.GetRobotPart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotPartRequest, app.v1.app_pb2.GetRobotPartResponse), '/viam.app.v1.AppService/GetRobotPartLogs': grpclib.const.Handler(self.GetRobotPartLogs, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotPartLogsRequest, app.v1.app_pb2.GetRobotPartLogsResponse), '/viam.app.v1.AppService/TailRobotPartLogs': grpclib.const.Handler(self.TailRobotPartLogs, grpclib.const.Cardinality.UNARY_STREAM, app.v1.app_pb2.TailRobotPartLogsRequest, app.v1.app_pb2.TailRobotPartLogsResponse), '/viam.app.v1.AppService/GetRobotPartHistory': grpclib.const.Handler(self.GetRobotPartHistory, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotPartHistoryRequest, app.v1.app_pb2.GetRobotPartHistoryResponse), '/viam.app.v1.AppService/UpdateRobotPart': grpclib.const.Handler(self.UpdateRobotPart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateRobotPartRequest, app.v1.app_pb2.UpdateRobotPartResponse), '/viam.app.v1.AppService/NewRobotPart': grpclib.const.Handler(self.NewRobotPart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.NewRobotPartRequest, app.v1.app_pb2.NewRobotPartResponse), '/viam.app.v1.AppService/DeleteRobotPart': grpclib.const.Handler(self.DeleteRobotPart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteRobotPartRequest, app.v1.app_pb2.DeleteRobotPartResponse), '/viam.app.v1.AppService/MarkPartAsMain': grpclib.const.Handler(self.MarkPartAsMain, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.MarkPartAsMainRequest, app.v1.app_pb2.MarkPartAsMainResponse), '/viam.app.v1.AppService/FindRobots': grpclib.const.Handler(self.FindRobots, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.FindRobotsRequest, app.v1.app_pb2.FindRobotsResponse), '/viam.app.v1.AppService/NewRobot': grpclib.const.Handler(self.NewRobot, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.NewRobotRequest, app.v1.app_pb2.NewRobotResponse), '/viam.app.v1.AppService/UpdateRobot': grpclib.const.Handler(self.UpdateRobot, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateRobotRequest, app.v1.app_pb2.UpdateRobotResponse), '/viam.app.v1.AppService/DeleteRobot': grpclib.const.Handler(self.DeleteRobot, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteRobotRequest, app.v1.app_pb2.DeleteRobotResponse)}

class AppServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListOrganizations = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListOrganizations', app.v1.app_pb2.ListOrganizationsRequest, app.v1.app_pb2.ListOrganizationsResponse)
        self.ListLocations = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListLocations', app.v1.app_pb2.ListLocationsRequest, app.v1.app_pb2.ListLocationsResponse)
        self.LocationAuth = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/LocationAuth', app.v1.app_pb2.LocationAuthRequest, app.v1.app_pb2.LocationAuthResponse)
        self.GetRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobot', app.v1.app_pb2.GetRobotRequest, app.v1.app_pb2.GetRobotResponse)
        self.GetRobotParts = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotParts', app.v1.app_pb2.GetRobotPartsRequest, app.v1.app_pb2.GetRobotPartsResponse)
        self.GetRobotPart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotPart', app.v1.app_pb2.GetRobotPartRequest, app.v1.app_pb2.GetRobotPartResponse)
        self.GetRobotPartLogs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotPartLogs', app.v1.app_pb2.GetRobotPartLogsRequest, app.v1.app_pb2.GetRobotPartLogsResponse)
        self.TailRobotPartLogs = grpclib.client.UnaryStreamMethod(channel, '/viam.app.v1.AppService/TailRobotPartLogs', app.v1.app_pb2.TailRobotPartLogsRequest, app.v1.app_pb2.TailRobotPartLogsResponse)
        self.GetRobotPartHistory = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotPartHistory', app.v1.app_pb2.GetRobotPartHistoryRequest, app.v1.app_pb2.GetRobotPartHistoryResponse)
        self.UpdateRobotPart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateRobotPart', app.v1.app_pb2.UpdateRobotPartRequest, app.v1.app_pb2.UpdateRobotPartResponse)
        self.NewRobotPart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/NewRobotPart', app.v1.app_pb2.NewRobotPartRequest, app.v1.app_pb2.NewRobotPartResponse)
        self.DeleteRobotPart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteRobotPart', app.v1.app_pb2.DeleteRobotPartRequest, app.v1.app_pb2.DeleteRobotPartResponse)
        self.MarkPartAsMain = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/MarkPartAsMain', app.v1.app_pb2.MarkPartAsMainRequest, app.v1.app_pb2.MarkPartAsMainResponse)
        self.FindRobots = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/FindRobots', app.v1.app_pb2.FindRobotsRequest, app.v1.app_pb2.FindRobotsResponse)
        self.NewRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/NewRobot', app.v1.app_pb2.NewRobotRequest, app.v1.app_pb2.NewRobotResponse)
        self.UpdateRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateRobot', app.v1.app_pb2.UpdateRobotRequest, app.v1.app_pb2.UpdateRobotResponse)
        self.DeleteRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteRobot', app.v1.app_pb2.DeleteRobotRequest, app.v1.app_pb2.DeleteRobotResponse)