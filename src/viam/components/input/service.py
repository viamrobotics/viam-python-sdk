import asyncio
from multiprocessing import Pipe
from typing import Optional

from grpclib.server import Stream
from h2.exceptions import StreamClosedError

import viam
from viam.errors import NotSupportedError
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.inputcontroller import (
    GetControlsRequest,
    GetControlsResponse,
    GetEventsRequest,
    GetEventsResponse,
    InputControllerServiceBase,
    StreamEventsRequest,
    StreamEventsResponse,
    TriggerEventRequest,
    TriggerEventResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .input import Control, Controller, Event, EventType

LOGGER = viam.logging.getLogger(__name__)


class InputControllerRPCService(InputControllerServiceBase, ResourceRPCServiceBase[Controller]):
    """
    gRPC Service for an input controller
    """

    RESOURCE_TYPE = Controller

    async def GetControls(self, stream: Stream[GetControlsRequest, GetControlsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.controller
        controller = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        controls = await controller.get_controls(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetControlsResponse(controls=[c.value for c in controls])
        await stream.send_message(response)

    async def GetEvents(self, stream: Stream[GetEventsRequest, GetEventsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.controller
        controller = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        events = await controller.get_events(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        pb_events = [e.proto for e in events.values()]
        response = GetEventsResponse(events=pb_events)
        await stream.send_message(response)

    async def StreamEvents(self, stream: Stream[StreamEventsRequest, StreamEventsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.controller
        controller = self.get_resource(name)

        loop = asyncio.get_running_loop()
        # Using Pipes to send event data back to this function so it can be streamed to clients
        # The write pipe is added to the callbacks for a control, so whenever that control sends a watched event,
        # that event is sent through the pipe, where it will be read (further down) and sent over the stream
        pipe_r, pipe_w = Pipe(duplex=False)

        def ctrlFunc(event: Event):
            try:
                pipe_w.send(event)
            except Exception as e:
                LOGGER.error(e)
                cleanup(e)

        # Register the pipe callbacks
        for event in request.events:
            triggers = [EventType(et) for et in event.events]
            if len(triggers):
                controller.register_control_callback(
                    Control(event.control),
                    triggers,
                    ctrlFunc,
                    extra=struct_to_dict(request.extra),
                )

            cancelled_triggers = [EventType(et) for et in event.cancelled_events]
            if len(cancelled_triggers):
                controller.register_control_callback(
                    Control(event.control),
                    cancelled_triggers,
                    None,
                    extra=struct_to_dict(request.extra),
                )

        # Asynchronously wait for messages to come over the read pipe and run the READ function whenever the pipe is ready.
        def read():
            ev: Event = pipe_r.recv()
            pb_ev = ev.proto
            response = StreamEventsResponse(event=pb_ev)

            async def send_message():
                try:
                    stream._cancel_done = False  # Undo hack, see below
                    await stream.send_message(response)
                except StreamClosedError:
                    cleanup()
                except Exception as e:
                    cleanup(e)

            loop.create_task(send_message(), name=f"{viam._TASK_PREFIX}-input_send_event")

        loop.add_reader(pipe_r, read)

        # HACK: Keep the stream open when this function returns.
        # When the StreamEvents function returns, the Stream is closed. But we don't want the stream to close because we still need
        # to send events to any clients who have registered callbacks.
        # By setting ``stream._cancel_done`` to ``True``, this tricks grpclib into thinking it already closed the stream, so it doesn't
        # perform any cleanup (like removing the stream). We eventually do want to actually close this stream, so we undo this hack
        # every time we send a message. That way, the trailing metadata is sent when either the server closes or the client disconnects.
        stream._cancel_done = True

        # Remove ctrl functions when this stream is closed
        def cleanup(exc: Optional[Exception] = None):
            loop.remove_reader(pipe_r)
            pipe_w.close()
            pipe_r.close()
            unregister_pipe_callbacks()
            asyncio.create_task(stream.__aexit__(None, exc, None))

        def unregister_pipe_callbacks():
            for event in request.events:
                triggers = [EventType(et) for et in event.events]
                if len(triggers):
                    controller.register_control_callback(
                        Control(event.control),
                        triggers,
                        None,
                        extra=struct_to_dict(request.extra),
                    )

    async def TriggerEvent(self, stream: Stream[TriggerEventRequest, TriggerEventResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.controller
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        controller = self.get_resource(name)
        try:
            pb_event = request.event
            event = Event.from_proto(pb_event)
            await controller.trigger_event(event, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        except NotSupportedError as e:
            raise e.grpc_error

        response = TriggerEventResponse()
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        controller = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await controller.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        arm = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await arm.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
