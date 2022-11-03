import asyncio
from datetime import datetime, timedelta
from time import time

import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericService
from viam.components.input import Control, Event, EventType
from viam.components.input.client import ControllerClient
from viam.components.input.service import InputControllerService
from viam.components.resource_manager import ResourceManager
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

from . import loose_approx
from .mocks.components import MockInputController


@pytest.fixture(scope="function")
def controller() -> MockInputController:
    return MockInputController(name="controller")


@pytest.fixture(scope="function")
def service(controller: MockInputController) -> InputControllerService:
    manager = ResourceManager([controller])
    return InputControllerService(manager)


@pytest.fixture(scope="function")
def generic_service(controller: MockInputController) -> GenericService:
    manager = ResourceManager([controller])
    return GenericService(manager)


class TestInputController:
    @pytest.mark.asyncio
    async def test_get_controls(self, controller: MockInputController):
        controls = await controller.get_controls(timeout=4.4)
        assert controls == [
            Control.ABSOLUTE_X,
            Control.ABSOLUTE_Y,
            Control.ABSOLUTE_Z,
            Control.ABSOLUTE_RX,
            Control.ABSOLUTE_RY,
            Control.ABSOLUTE_RZ,
            Control.ABSOLUTE_HAT0_X,
            Control.ABSOLUTE_HAT0_Y,
            Control.BUTTON_SOUTH,
            Control.BUTTON_EAST,
            Control.BUTTON_WEST,
            Control.BUTTON_NORTH,
            Control.BUTTON_LT,
            Control.BUTTON_RT,
            Control.BUTTON_L_THUMB,
            Control.BUTTON_R_THUMB,
            Control.BUTTON_SELECT,
            Control.BUTTON_START,
            Control.BUTTON_MENU,
            Control.BUTTON_RECORD,
            Control.BUTTON_E_STOP,
        ]
        assert controller.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_events(self, controller: MockInputController):
        events = await controller.get_events(timeout=1.82)
        assert len(events) == 0
        assert controller.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_trigger_event(self, controller: MockInputController):
        assert len(controller.events) == 0
        event = Event(time(), EventType.CONNECT, Control.ABSOLUTE_X, 0)
        await controller.trigger_event(event, timeout=7.86)
        assert controller.timeout == loose_approx(7.86)
        events = await controller.get_events()
        assert events[Control.ABSOLUTE_X] == event
        assert controller.timeout is None

    def test_register_control_callback(self, controller: MockInputController):
        assert len(controller.callbacks) == 0
        controller.register_control_callback(Control.ABSOLUTE_X, [EventType.BUTTON_PRESS, EventType.BUTTON_RELEASE], lambda ev: print(ev))
        assert len(controller.callbacks) == 1
        assert len(controller.callbacks[Control.ABSOLUTE_X]) == 2

    @pytest.mark.asyncio
    async def test_do(self, controller: MockInputController):
        with pytest.raises(NotImplementedError):
            await controller.do_command({"command": "args"})


class TestService:
    @pytest.mark.asyncio
    async def test_get_controls(self, controller: MockInputController, service: InputControllerService):
        async with ChannelFor([service]) as channel:
            client = InputControllerServiceStub(channel)
            request = GetControlsRequest(controller=controller.name)
            response: GetControlsResponse = await client.GetControls(request, timeout=1.23)
            controls = list(response.controls)
            assert controls == [
                Control.ABSOLUTE_X,
                Control.ABSOLUTE_Y,
                Control.ABSOLUTE_Z,
                Control.ABSOLUTE_RX,
                Control.ABSOLUTE_RY,
                Control.ABSOLUTE_RZ,
                Control.ABSOLUTE_HAT0_X,
                Control.ABSOLUTE_HAT0_Y,
                Control.BUTTON_SOUTH,
                Control.BUTTON_EAST,
                Control.BUTTON_WEST,
                Control.BUTTON_NORTH,
                Control.BUTTON_LT,
                Control.BUTTON_RT,
                Control.BUTTON_L_THUMB,
                Control.BUTTON_R_THUMB,
                Control.BUTTON_SELECT,
                Control.BUTTON_START,
                Control.BUTTON_MENU,
                Control.BUTTON_RECORD,
                Control.BUTTON_E_STOP,
            ]
            assert controller.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_events(self, controller: MockInputController, service: InputControllerService):
        async with ChannelFor([service]) as channel:
            client = InputControllerServiceStub(channel)
            request = GetEventsRequest(controller=controller.name)
            response: GetEventsResponse = await client.GetEvents(request, timeout=2.34)
            events = list(response.events)
            assert events == list(controller.events.values())
            assert controller.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_trigger_event(self, controller: MockInputController, service: InputControllerService):
        event = Event(time(), EventType.CONNECT, Control.ABSOLUTE_X, 0)
        async with ChannelFor([service]) as channel:
            client = InputControllerServiceStub(channel)
            request = TriggerEventRequest(controller=controller.name, event=event.proto)
            await client.TriggerEvent(request, timeout=3.45)
            assert controller.events[Control.ABSOLUTE_X].control == event.control
            assert controller.events[Control.ABSOLUTE_X].event == event.event
            assert controller.events[Control.ABSOLUTE_X].value == event.value
            # timestamp nanos conversion can result in differences in the 1e-7 scale
            assert abs(controller.events[Control.ABSOLUTE_X].time - event.time) < 0.000001
            assert controller.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_stream_events(selc, controller: MockInputController, service: InputControllerService):
        async with ChannelFor([service]) as channel:

            def trigger_event():
                asyncio.get_running_loop().create_task(
                    controller.trigger_event(Event(time(), EventType.BUTTON_RELEASE, Control.BUTTON_START, 0))
                )

            asyncio.get_running_loop().call_later(0.1, trigger_event)
            client = InputControllerServiceStub(channel)
            request = StreamEventsRequest(
                controller=controller.name,
                events=[StreamEventsRequest.Events(control=Control.BUTTON_START, events=[EventType.BUTTON_RELEASE])],
            )
            async with client.StreamEvents.open(timeout=1) as stream:
                await stream.send_message(request, end=True)
                response: StreamEventsResponse
                async for response in stream:
                    event = Event.from_proto(response.event)
                    assert event.control == Control.BUTTON_START
                    assert event.event == EventType.BUTTON_RELEASE
                    assert event.value == 0
                    break
                await stream.cancel()

            await controller.trigger_event(Event(time(), EventType.BUTTON_RELEASE, Control.BUTTON_START, 0))
            await asyncio.sleep(0.1)
            assert controller.callbacks[Control.BUTTON_START][EventType.BUTTON_RELEASE] is None


class TestClient:
    @pytest.mark.asyncio
    async def test_get_controls(self, controller: MockInputController, service: InputControllerService):
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)
            controls = await client.get_controls(timeout=4.56)
            assert controls == [
                Control.ABSOLUTE_X,
                Control.ABSOLUTE_Y,
                Control.ABSOLUTE_Z,
                Control.ABSOLUTE_RX,
                Control.ABSOLUTE_RY,
                Control.ABSOLUTE_RZ,
                Control.ABSOLUTE_HAT0_X,
                Control.ABSOLUTE_HAT0_Y,
                Control.BUTTON_SOUTH,
                Control.BUTTON_EAST,
                Control.BUTTON_WEST,
                Control.BUTTON_NORTH,
                Control.BUTTON_LT,
                Control.BUTTON_RT,
                Control.BUTTON_L_THUMB,
                Control.BUTTON_R_THUMB,
                Control.BUTTON_SELECT,
                Control.BUTTON_START,
                Control.BUTTON_MENU,
                Control.BUTTON_RECORD,
                Control.BUTTON_E_STOP,
            ]
            assert controller.timeout == loose_approx(4.56)

    @pytest.mark.asyncio
    async def test_get_events(self, controller: MockInputController, service: InputControllerService):
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)
            events = await client.get_events(timeout=5.67)
            assert events == controller.events
            assert controller.timeout == loose_approx(5.67)

    @pytest.mark.asyncio
    async def test_trigger_event(self, controller: MockInputController, service: InputControllerService):
        event = Event(time(), EventType.CONNECT, Control.ABSOLUTE_X, 0)
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)
            await client.trigger_event(event, timeout=6.78)
            assert controller.events[Control.ABSOLUTE_X].control == event.control
            assert controller.events[Control.ABSOLUTE_X].event == event.event
            assert controller.events[Control.ABSOLUTE_X].value == event.value
            # timestamp nanos conversion can result in differences in the 1e-7 scale
            assert abs(controller.events[Control.ABSOLUTE_X].time - event.time) < 0.000001
            assert controller.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_register_control_callback(self, controller: MockInputController, service: InputControllerService):
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)

            self.callback_called = False
            self.event_equal = False

            def test_event(event: Event):
                self.callback_called = True
                self.event_equal = event.control == Control.BUTTON_START and event.event == EventType.BUTTON_RELEASE and event.value == 0

            client.register_control_callback(Control.BUTTON_START, [EventType.BUTTON_RELEASE], test_event)

            def trigger_event():
                asyncio.get_running_loop().create_task(
                    controller.trigger_event(Event(time(), EventType.BUTTON_RELEASE, Control.BUTTON_START, 0))
                )

            asyncio.get_running_loop().call_later(0.1, trigger_event)

            future = datetime.now() + timedelta(seconds=0.2)
            while datetime.now() < future:
                await asyncio.sleep(0.1)

            assert self.callback_called is True
            assert self.event_equal is True

    @pytest.mark.asyncio
    async def test_do(self, controller: MockInputController, service: InputControllerService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = ControllerClient(controller.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do_command({"command": "args"})
