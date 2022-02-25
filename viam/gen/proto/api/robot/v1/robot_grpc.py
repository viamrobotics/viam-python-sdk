import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.struct_pb2
import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
import google.api.annotations_pb2
from ..... import proto
from ..... import proto

class RobotServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Status(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.StatusRequest, proto.api.robot.v1.robot_pb2.StatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StatusStream(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.StatusStreamRequest, proto.api.robot.v1.robot_pb2.StatusStreamResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Config(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ConfigRequest, proto.api.robot.v1.robot_pb2.ConfigResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoAction(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.DoActionRequest, proto.api.robot.v1.robot_pb2.DoActionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ExecuteFunction(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ExecuteFunctionRequest, proto.api.robot.v1.robot_pb2.ExecuteFunctionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ExecuteSource(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ExecuteSourceRequest, proto.api.robot.v1.robot_pb2.ExecuteSourceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResourceRunCommand(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigationServiceMode(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.NavigationServiceModeRequest, proto.api.robot.v1.robot_pb2.NavigationServiceModeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigationServiceSetMode(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.NavigationServiceSetModeRequest, proto.api.robot.v1.robot_pb2.NavigationServiceSetModeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigationServiceLocation(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.NavigationServiceLocationRequest, proto.api.robot.v1.robot_pb2.NavigationServiceLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigationServiceWaypoints(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.NavigationServiceWaypointsRequest, proto.api.robot.v1.robot_pb2.NavigationServiceWaypointsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigationServiceAddWaypoint(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.NavigationServiceAddWaypointRequest, proto.api.robot.v1.robot_pb2.NavigationServiceAddWaypointResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigationServiceRemoveWaypoint(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.NavigationServiceRemoveWaypointRequest, proto.api.robot.v1.robot_pb2.NavigationServiceRemoveWaypointResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.robot.v1.RobotService/Status': grpclib.const.Handler(self.Status, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.StatusRequest, proto.api.robot.v1.robot_pb2.StatusResponse), '/proto.api.robot.v1.RobotService/StatusStream': grpclib.const.Handler(self.StatusStream, grpclib.const.Cardinality.UNARY_STREAM, proto.api.robot.v1.robot_pb2.StatusStreamRequest, proto.api.robot.v1.robot_pb2.StatusStreamResponse), '/proto.api.robot.v1.RobotService/Config': grpclib.const.Handler(self.Config, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ConfigRequest, proto.api.robot.v1.robot_pb2.ConfigResponse), '/proto.api.robot.v1.RobotService/DoAction': grpclib.const.Handler(self.DoAction, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.DoActionRequest, proto.api.robot.v1.robot_pb2.DoActionResponse), '/proto.api.robot.v1.RobotService/ExecuteFunction': grpclib.const.Handler(self.ExecuteFunction, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ExecuteFunctionRequest, proto.api.robot.v1.robot_pb2.ExecuteFunctionResponse), '/proto.api.robot.v1.RobotService/ExecuteSource': grpclib.const.Handler(self.ExecuteSource, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ExecuteSourceRequest, proto.api.robot.v1.robot_pb2.ExecuteSourceResponse), '/proto.api.robot.v1.RobotService/ResourceRunCommand': grpclib.const.Handler(self.ResourceRunCommand, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse), '/proto.api.robot.v1.RobotService/NavigationServiceMode': grpclib.const.Handler(self.NavigationServiceMode, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.NavigationServiceModeRequest, proto.api.robot.v1.robot_pb2.NavigationServiceModeResponse), '/proto.api.robot.v1.RobotService/NavigationServiceSetMode': grpclib.const.Handler(self.NavigationServiceSetMode, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.NavigationServiceSetModeRequest, proto.api.robot.v1.robot_pb2.NavigationServiceSetModeResponse), '/proto.api.robot.v1.RobotService/NavigationServiceLocation': grpclib.const.Handler(self.NavigationServiceLocation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.NavigationServiceLocationRequest, proto.api.robot.v1.robot_pb2.NavigationServiceLocationResponse), '/proto.api.robot.v1.RobotService/NavigationServiceWaypoints': grpclib.const.Handler(self.NavigationServiceWaypoints, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.NavigationServiceWaypointsRequest, proto.api.robot.v1.robot_pb2.NavigationServiceWaypointsResponse), '/proto.api.robot.v1.RobotService/NavigationServiceAddWaypoint': grpclib.const.Handler(self.NavigationServiceAddWaypoint, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.NavigationServiceAddWaypointRequest, proto.api.robot.v1.robot_pb2.NavigationServiceAddWaypointResponse), '/proto.api.robot.v1.RobotService/NavigationServiceRemoveWaypoint': grpclib.const.Handler(self.NavigationServiceRemoveWaypoint, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.NavigationServiceRemoveWaypointRequest, proto.api.robot.v1.robot_pb2.NavigationServiceRemoveWaypointResponse)}

class RobotServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Status = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/Status', proto.api.robot.v1.robot_pb2.StatusRequest, proto.api.robot.v1.robot_pb2.StatusResponse)
        self.StatusStream = grpclib.client.UnaryStreamMethod(channel, '/proto.api.robot.v1.RobotService/StatusStream', proto.api.robot.v1.robot_pb2.StatusStreamRequest, proto.api.robot.v1.robot_pb2.StatusStreamResponse)
        self.Config = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/Config', proto.api.robot.v1.robot_pb2.ConfigRequest, proto.api.robot.v1.robot_pb2.ConfigResponse)
        self.DoAction = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/DoAction', proto.api.robot.v1.robot_pb2.DoActionRequest, proto.api.robot.v1.robot_pb2.DoActionResponse)
        self.ExecuteFunction = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ExecuteFunction', proto.api.robot.v1.robot_pb2.ExecuteFunctionRequest, proto.api.robot.v1.robot_pb2.ExecuteFunctionResponse)
        self.ExecuteSource = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ExecuteSource', proto.api.robot.v1.robot_pb2.ExecuteSourceRequest, proto.api.robot.v1.robot_pb2.ExecuteSourceResponse)
        self.ResourceRunCommand = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ResourceRunCommand', proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse)
        self.NavigationServiceMode = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/NavigationServiceMode', proto.api.robot.v1.robot_pb2.NavigationServiceModeRequest, proto.api.robot.v1.robot_pb2.NavigationServiceModeResponse)
        self.NavigationServiceSetMode = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/NavigationServiceSetMode', proto.api.robot.v1.robot_pb2.NavigationServiceSetModeRequest, proto.api.robot.v1.robot_pb2.NavigationServiceSetModeResponse)
        self.NavigationServiceLocation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/NavigationServiceLocation', proto.api.robot.v1.robot_pb2.NavigationServiceLocationRequest, proto.api.robot.v1.robot_pb2.NavigationServiceLocationResponse)
        self.NavigationServiceWaypoints = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/NavigationServiceWaypoints', proto.api.robot.v1.robot_pb2.NavigationServiceWaypointsRequest, proto.api.robot.v1.robot_pb2.NavigationServiceWaypointsResponse)
        self.NavigationServiceAddWaypoint = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/NavigationServiceAddWaypoint', proto.api.robot.v1.robot_pb2.NavigationServiceAddWaypointRequest, proto.api.robot.v1.robot_pb2.NavigationServiceAddWaypointResponse)
        self.NavigationServiceRemoveWaypoint = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/NavigationServiceRemoveWaypoint', proto.api.robot.v1.robot_pb2.NavigationServiceRemoveWaypointRequest, proto.api.robot.v1.robot_pb2.NavigationServiceRemoveWaypointResponse)