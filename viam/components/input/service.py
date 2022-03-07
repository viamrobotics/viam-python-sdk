from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.inputcontroller import (
    GetControlsRequest, GetControlsResponse, GetEventsRequest,
    GetEventsResponse, InputControllerServiceBase, StreamEventsRequest,
    StreamEventsResponse, TriggerEventRequest, TriggerEventResponse,
    Event as PBEvent
)

from .input import Control, Controller, Event, EventType


class InputControllerService(InputControllerServiceBase, ComponentServiceBase[Controller]):
    """
    gRPC Service for an input controller
    """

    RESOURCE_TYPE = Controller

    async def GetControls(
        self,
        stream: Stream[GetControlsRequest, GetControlsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.controller
        try:
            controller = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        controls = await controller.get_controls()
        response = GetControlsResponse(controls=[c.value for c in controls])
        await stream.send_message(response)

    async def GetEvents(
        self,
        stream: Stream[GetEventsRequest, GetEventsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.controller
        try:
            controller = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        events = await controller.get_events()
        pb_events = []
        for (_, event) in events.items():
            seconds = int(event.time)
            nanos = int(event.time % 1 * 1e9)
            timestamp = Timestamp(seconds=seconds, nanos=nanos)
            pb_events.append(PBEvent(
                time=timestamp,
                event=event.event.value,
                control=event.control.value,
                value=event.value
            ))
        response = GetEventsResponse()
        await stream.send_message(response)

    async def StreamEvents(
        self,
        stream: Stream[StreamEventsRequest, StreamEventsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.controller
        try:
            controller = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()

        response = StreamEventsResponse()
        await stream.send_message(response)

    async def TriggerEvent(
        self,
        stream: Stream[TriggerEventRequest, TriggerEventResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.controller
        try:
            controller = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()

        response = TriggerEventResponse()
        await stream.send_message(response)
