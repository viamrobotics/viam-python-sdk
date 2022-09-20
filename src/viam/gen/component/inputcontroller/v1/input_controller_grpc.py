import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.timestamp_pb2
from .... import component

class InputControllerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetControls(self, stream: 'grpclib.server.Stream[component.inputcontroller.v1.input_controller_pb2.GetControlsRequest, component.inputcontroller.v1.input_controller_pb2.GetControlsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetEvents(self, stream: 'grpclib.server.Stream[component.inputcontroller.v1.input_controller_pb2.GetEventsRequest, component.inputcontroller.v1.input_controller_pb2.GetEventsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamEvents(self, stream: 'grpclib.server.Stream[component.inputcontroller.v1.input_controller_pb2.StreamEventsRequest, component.inputcontroller.v1.input_controller_pb2.StreamEventsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TriggerEvent(self, stream: 'grpclib.server.Stream[component.inputcontroller.v1.input_controller_pb2.TriggerEventRequest, component.inputcontroller.v1.input_controller_pb2.TriggerEventResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.inputcontroller.v1.InputControllerService/GetControls': grpclib.const.Handler(self.GetControls, grpclib.const.Cardinality.UNARY_UNARY, component.inputcontroller.v1.input_controller_pb2.GetControlsRequest, component.inputcontroller.v1.input_controller_pb2.GetControlsResponse), '/viam.component.inputcontroller.v1.InputControllerService/GetEvents': grpclib.const.Handler(self.GetEvents, grpclib.const.Cardinality.UNARY_UNARY, component.inputcontroller.v1.input_controller_pb2.GetEventsRequest, component.inputcontroller.v1.input_controller_pb2.GetEventsResponse), '/viam.component.inputcontroller.v1.InputControllerService/StreamEvents': grpclib.const.Handler(self.StreamEvents, grpclib.const.Cardinality.UNARY_STREAM, component.inputcontroller.v1.input_controller_pb2.StreamEventsRequest, component.inputcontroller.v1.input_controller_pb2.StreamEventsResponse), '/viam.component.inputcontroller.v1.InputControllerService/TriggerEvent': grpclib.const.Handler(self.TriggerEvent, grpclib.const.Cardinality.UNARY_UNARY, component.inputcontroller.v1.input_controller_pb2.TriggerEventRequest, component.inputcontroller.v1.input_controller_pb2.TriggerEventResponse)}

class InputControllerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetControls = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.inputcontroller.v1.InputControllerService/GetControls', component.inputcontroller.v1.input_controller_pb2.GetControlsRequest, component.inputcontroller.v1.input_controller_pb2.GetControlsResponse)
        self.GetEvents = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.inputcontroller.v1.InputControllerService/GetEvents', component.inputcontroller.v1.input_controller_pb2.GetEventsRequest, component.inputcontroller.v1.input_controller_pb2.GetEventsResponse)
        self.StreamEvents = grpclib.client.UnaryStreamMethod(channel, '/viam.component.inputcontroller.v1.InputControllerService/StreamEvents', component.inputcontroller.v1.input_controller_pb2.StreamEventsRequest, component.inputcontroller.v1.input_controller_pb2.StreamEventsResponse)
        self.TriggerEvent = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.inputcontroller.v1.InputControllerService/TriggerEvent', component.inputcontroller.v1.input_controller_pb2.TriggerEventRequest, component.inputcontroller.v1.input_controller_pb2.TriggerEventResponse)