import asyncio
from threading import Lock
from time import time
from typing import Any, Dict, List, Optional
from grpclib import GRPCError, Status

from grpclib.client import Channel
import viam
from viam.components.generic.client import do_command
from viam.errors import NotSupportedError
from viam.logging import getLogger
from viam.proto.component.inputcontroller import (
    GetControlsRequest,
    GetControlsResponse,
    GetEventsRequest,
    GetEventsResponse,
    InputControllerServiceStub,
    StreamEventsRequest,
    StreamEventsResponse,
    TriggerEventRequest,
)

from .input import Control, ControlFunction, Controller, Event, EventType

LOGGER = getLogger(__name__)


class ControllerClient(Controller):
    """gRPC client for an Input Controller"""

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = InputControllerServiceStub(channel)
        self.callbacks: Dict[Control, Dict[EventType, Optional[ControlFunction]]] = {}
        self._lock = Lock()
        self._stream_lock = Lock()
        self._is_streaming = False
        self._is_stream_ready = False
        super().__init__(name)

    async def get_controls(self) -> List[Control]:
        request = GetControlsRequest(controller=self.name)
        response: GetControlsResponse = await self.client.GetControls(request)
        return [Control(control) for control in response.controls]

    async def get_events(self) -> Dict[Control, Event]:
        request = GetEventsRequest(controller=self.name)
        response: GetEventsResponse = await self.client.GetEvents(request)
        return {Control(event.control): Event.from_proto(event) for (event) in response.events}

    def register_control_callback(self, control: Control, triggers: List[EventType], function: Optional[ControlFunction]):
        with self._lock:
            callbacks = self.callbacks.get(control, {})
            for trigger in triggers:
                if trigger == EventType.BUTTON_CHANGE:
                    callbacks[EventType.BUTTON_PRESS] = function
                    callbacks[EventType.BUTTON_RELEASE] = function
                else:
                    callbacks[trigger] = function
            self.callbacks[control] = callbacks

        def handle_task_result(task: asyncio.Task):
            try:
                result = task.result()
                LOGGER.debug(f"Task {task.get_name()} returned with result {result}")
            except asyncio.CancelledError:
                pass
            except Exception:
                LOGGER.exception("Exception raised by task = %r", task)

        task = asyncio.create_task(self._stream_events(), name=f"{viam._TASK_PREFIX}-input_stream_events")
        task.add_done_callback(handle_task_result)

    async def trigger_event(self, event: Event):
        request = TriggerEventRequest(controller=self.name, event=event.proto)
        try:
            await self.client.TriggerEvent(request)
        except GRPCError as e:
            if e.status == Status.UNIMPLEMENTED and ("does not support triggering events" in e.message if e.message else False):
                raise NotSupportedError(f"Input controller named {self.name} does not support triggering events")

    async def _stream_events(self):
        with self._stream_lock:
            if self._is_streaming:
                return
            self._is_streaming = True

        if not self.callbacks:
            return

        request = StreamEventsRequest(controller=self.name, events=[])
        with self._lock:
            for (control, callbacks) in self.callbacks.items():
                event = StreamEventsRequest.Events(
                    control=control,
                    events=[et for (et, func) in callbacks.items() if func is not None],
                    cancelled_events=[et for (et, func) in callbacks.items() if func is None],
                )
                request.events.append(event)

        try:
            async with self.client.StreamEvents.open() as stream:
                await stream.send_message(request, end=True)
                self._send_connection_status(True)
                reply: StreamEventsResponse
                async for reply in stream:
                    event = reply.event
                    self._execute_callback(Event.from_proto(event))
        except Exception as e:
            LOGGER.error(e)
        finally:
            self._send_connection_status(False)
            with self._stream_lock:
                self._is_streaming = False
                self._is_stream_ready = False

    def _send_connection_status(self, connected: bool):
        for control in self.callbacks.keys():
            event = Event(time=time(), event=EventType.CONNECT if connected else EventType.DISCONNECT, control=control, value=0)
            self._execute_callback(event)

    def _execute_callback(self, event: Event):
        try:
            callbacks = self.callbacks[event.control]
            callback = callbacks.get(event.event, None)
            all_callback = callbacks.get(EventType.ALL_EVENTS, None)
        except KeyError:
            return

        if callback is not None:
            callback(event)
        if all_callback is not None:
            all_callback(event)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
