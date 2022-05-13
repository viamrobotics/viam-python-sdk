from multiprocessing import Pipe

from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.inputcontroller import (
    GetControlsRequest, GetControlsResponse, GetEventsRequest,
    GetEventsResponse, InputControllerServiceBase, StreamEventsRequest,
    StreamEventsResponse, TriggerEventRequest, TriggerEventResponse)
from viam.proto.api.component.inputcontroller import Event as PBEvent

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
        pb_events = [e.proto for e in events.values()]
        response = GetEventsResponse(events=pb_events)
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

        pipe_r, pipe_w = Pipe(duplex=False)

        def ctrlFunc(event: Event):
            pipe_w.send(event.proto)

        for event in request.events:
            triggers = [EventType(et) for et in event.events]
            print(event, triggers)
            if len(triggers):
                controller.register_control_callback(
                    Control(event.control), triggers, ctrlFunc)

            cancelled_triggers = [EventType(et)
                                  for et in event.cancelled_events]
            print(event, cancelled_triggers)
            if len(cancelled_triggers):
                controller.register_control_callback(
                    Control(event.control), cancelled_triggers, None)

        while True:
            print("In the while true")
            pb_event: PBEvent = pipe_r.recv()
            print("Received event")
            response = StreamEventsResponse(event=pb_event)
            print("Response created, awaiting send message")
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
            pb_event = request.event
            event = Event.from_proto(pb_event)
            await controller.trigger_event(event)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        response = TriggerEventResponse()
        await stream.send_message(response)
