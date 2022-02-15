import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.timestamp_pb2
from ..... import proto

class InputControllerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetControls(self, stream: 'grpclib.server.Stream[proto.api.component.v1.input_controller_pb2.InputControllerServiceGetControlsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceGetControlsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetEvents(self, stream: 'grpclib.server.Stream[proto.api.component.v1.input_controller_pb2.InputControllerServiceGetEventsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceGetEventsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamEvents(self, stream: 'grpclib.server.Stream[proto.api.component.v1.input_controller_pb2.InputControllerServiceStreamEventsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceStreamEventsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TriggerEvent(self, stream: 'grpclib.server.Stream[proto.api.component.v1.input_controller_pb2.InputControllerServiceTriggerEventRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceTriggerEventResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.InputControllerService/GetControls': grpclib.const.Handler(self.GetControls, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.input_controller_pb2.InputControllerServiceGetControlsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceGetControlsResponse), '/proto.api.component.v1.InputControllerService/GetEvents': grpclib.const.Handler(self.GetEvents, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.input_controller_pb2.InputControllerServiceGetEventsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceGetEventsResponse), '/proto.api.component.v1.InputControllerService/StreamEvents': grpclib.const.Handler(self.StreamEvents, grpclib.const.Cardinality.UNARY_STREAM, proto.api.component.v1.input_controller_pb2.InputControllerServiceStreamEventsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceStreamEventsResponse), '/proto.api.component.v1.InputControllerService/TriggerEvent': grpclib.const.Handler(self.TriggerEvent, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.input_controller_pb2.InputControllerServiceTriggerEventRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceTriggerEventResponse)}

class InputControllerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetControls = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.InputControllerService/GetControls', proto.api.component.v1.input_controller_pb2.InputControllerServiceGetControlsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceGetControlsResponse)
        self.GetEvents = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.InputControllerService/GetEvents', proto.api.component.v1.input_controller_pb2.InputControllerServiceGetEventsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceGetEventsResponse)
        self.StreamEvents = grpclib.client.UnaryStreamMethod(channel, '/proto.api.component.v1.InputControllerService/StreamEvents', proto.api.component.v1.input_controller_pb2.InputControllerServiceStreamEventsRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceStreamEventsResponse)
        self.TriggerEvent = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.InputControllerService/TriggerEvent', proto.api.component.v1.input_controller_pb2.InputControllerServiceTriggerEventRequest, proto.api.component.v1.input_controller_pb2.InputControllerServiceTriggerEventResponse)