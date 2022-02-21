import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.timestamp_pb2
from ...... import proto

class InputControllerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetControls(self, stream: 'grpclib.server.Stream[proto.api.component.inputcontroller.v1.input_controller_pb2.GetControlsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.GetControlsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetEvents(self, stream: 'grpclib.server.Stream[proto.api.component.inputcontroller.v1.input_controller_pb2.GetEventsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.GetEventsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamEvents(self, stream: 'grpclib.server.Stream[proto.api.component.inputcontroller.v1.input_controller_pb2.StreamEventsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.StreamEventsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TriggerEvent(self, stream: 'grpclib.server.Stream[proto.api.component.inputcontroller.v1.input_controller_pb2.TriggerEventRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.TriggerEventResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.inputcontroller.v1.InputControllerService/GetControls': grpclib.const.Handler(self.GetControls, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.inputcontroller.v1.input_controller_pb2.GetControlsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.GetControlsResponse), '/proto.api.component.inputcontroller.v1.InputControllerService/GetEvents': grpclib.const.Handler(self.GetEvents, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.inputcontroller.v1.input_controller_pb2.GetEventsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.GetEventsResponse), '/proto.api.component.inputcontroller.v1.InputControllerService/StreamEvents': grpclib.const.Handler(self.StreamEvents, grpclib.const.Cardinality.UNARY_STREAM, proto.api.component.inputcontroller.v1.input_controller_pb2.StreamEventsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.StreamEventsResponse), '/proto.api.component.inputcontroller.v1.InputControllerService/TriggerEvent': grpclib.const.Handler(self.TriggerEvent, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.inputcontroller.v1.input_controller_pb2.TriggerEventRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.TriggerEventResponse)}

class InputControllerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetControls = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.inputcontroller.v1.InputControllerService/GetControls', proto.api.component.inputcontroller.v1.input_controller_pb2.GetControlsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.GetControlsResponse)
        self.GetEvents = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.inputcontroller.v1.InputControllerService/GetEvents', proto.api.component.inputcontroller.v1.input_controller_pb2.GetEventsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.GetEventsResponse)
        self.StreamEvents = grpclib.client.UnaryStreamMethod(channel, '/proto.api.component.inputcontroller.v1.InputControllerService/StreamEvents', proto.api.component.inputcontroller.v1.input_controller_pb2.StreamEventsRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.StreamEventsResponse)
        self.TriggerEvent = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.inputcontroller.v1.InputControllerService/TriggerEvent', proto.api.component.inputcontroller.v1.input_controller_pb2.TriggerEventRequest, proto.api.component.inputcontroller.v1.input_controller_pb2.TriggerEventResponse)