import asyncio
from multiprocessing import Pipe

from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.inputcontroller import (
    GetControlsRequest, GetControlsResponse, GetEventsRequest,
    GetEventsResponse, InputControllerServiceBase, StreamEventsRequest,
    StreamEventsResponse, TriggerEventRequest, TriggerEventResponse)

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

        # Using Pipes to send event data back to this function so it can be streamed to clients
        # The write pipe is added to the callbacks for a control, so whenever that control sends a watched event,,
        # that event is sent through the pipe, where it will be read (further down) and sent over the stream
        pipe_r, pipe_w = Pipe(duplex=False)

        def ctrlFunc(event: Event):
            pipe_w.send(event)

        # Register the pipe callbacks
        for event in request.events:
            triggers = [EventType(et) for et in event.events]
            if len(triggers):
                controller.register_control_callback(
                    Control(event.control), triggers, ctrlFunc)

            cancelled_triggers = [EventType(et)
                                  for et in event.cancelled_events]
            if len(cancelled_triggers):
                controller.register_control_callback(
                    Control(event.control), cancelled_triggers, None)

        # Asynchronously wait for messages to come over the read pipe and run the READ function whenever the pipe is ready.
        loop = asyncio.get_running_loop()

        def read():
            ev: Event = pipe_r.recv()
            pb_ev = ev.proto
            response = StreamEventsResponse(event=pb_ev)

            async def send_message():
                stream._cancel_done = False  # Undo hack, see below
                await stream.send_message(response)

            loop.create_task(send_message())

        loop.add_reader(pipe_r, read)

        # HACK: Keep the stream open when this function returns.
        # When the StreamEvents function returns, the Stream is closed. But we don't want the stream to close because we still need
        # to send events to any clients who have registered callbacks.
        # By setting `stream._cancel_done` to `True`, this tricks grpclib into thinking it already closed the stream, so it doesn't
        # perform any cleanup (like removing the stream). We eventually do want to actually close this stream, so we undo this hack
        # every time we send a message. That way, the trailing metadata is sent when either the server closes or the client disconnects.
        stream._cancel_done = True

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
