import asyncio
from datetime import datetime, timedelta
from time import time

import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericRPCService
from viam.components.input import Control, Event, EventType
from viam.components.input.client import ControllerClient
from viam.components.input.service import InputControllerRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
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
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import expected_grpc_timeout
from .mocks.components import GEOMETRIES, MockInputController


@pytest.fixture(scope="function")
def controller() -> MockInputController:
    return MockInputController(name="controller")


@pytest.fixture(scope="function")
def service(controller: MockInputController) -> InputControllerRPCService:
    manager = ResourceManager([controller])
    return InputControllerRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(controller: MockInputController) -> GenericRPCService:
    manager = ResourceManager([controller])
    return GenericRPCService(manager)


class TestInputController:
    async def test_get_controls(self, controller: MockInputController):
        extra = {"foo": "get_detectors"}
        controls = await controller.get_controls(extra=extra, timeout=4.4)
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
        assert controller.extra == extra
        assert controller.timeout == expected_grpc_timeout(4.4)

    async def test_get_events(self, controller: MockInputController):
        extra = {"foo": "get_events"}
        events = await controller.get_events(extra=extra, timeout=1.82)
        assert len(events) == 0
        assert controller.extra == extra
        assert controller.timeout == expected_grpc_timeout(1.82)

    async def test_trigger_event(self, controller: MockInputController):
        assert len(controller.events) == 0
        event = Event(time(), EventType.CONNECT, Control.ABSOLUTE_X, 0)
        await controller.trigger_event(event, timeout=7.86)
        assert controller.timeout == expected_grpc_timeout(7.86)
        events = await controller.get_events()
        assert events[Control.ABSOLUTE_X] == event
        assert controller.extra is None
        assert controller.timeout is None

    def test_register_control_callback(self, controller: MockInputController):
        assert len(controller.callbacks) == 0
        extra = {"foo": "register_control_callback"}
        controller.register_control_callback(
            Control.ABSOLUTE_X, [EventType.BUTTON_PRESS, EventType.BUTTON_RELEASE], lambda ev: print(ev), extra=extra
        )
        assert len(controller.callbacks) == 1
        assert len(controller.callbacks[Control.ABSOLUTE_X]) == 2
        assert controller.reg_extra == extra

    async def test_do(self, controller: MockInputController):
        command = {"command": "args"}
        resp = await controller.do_command(command)
        assert resp == {"command": command}

    async def test_get_geometries(self, controller: MockInputController):
        geometries = await controller.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    async def test_get_controls(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = InputControllerServiceStub(channel)
            extra = {"foo": "get_controls"}
            request = GetControlsRequest(controller=controller.name, extra=dict_to_struct(extra))
            response: GetControlsResponse = await client.GetControls(request, timeout=2.23)
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
            assert controller.extra == extra
            assert controller.timeout == expected_grpc_timeout(2.23)

    async def test_get_events(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = InputControllerServiceStub(channel)
            extra = {"foo": "get_events"}
            request = GetEventsRequest(controller=controller.name, extra=dict_to_struct(extra))
            response: GetEventsResponse = await client.GetEvents(request, timeout=2.34)
            events = list(response.events)
            assert events == list(controller.events.values())
            assert controller.extra == extra
            assert controller.timeout == expected_grpc_timeout(2.34)

    async def test_trigger_event(self, controller: MockInputController, service: InputControllerRPCService):
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
            assert controller.extra == {}
            assert controller.timeout == expected_grpc_timeout(3.45)

    async def test_stream_events(selc, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:

            def trigger_event():
                asyncio.get_running_loop().create_task(
                    controller.trigger_event(Event(time(), EventType.BUTTON_RELEASE, Control.BUTTON_START, 0))
                )

            asyncio.get_running_loop().call_later(0.1, trigger_event)
            client = InputControllerServiceStub(channel)
            extra = {"foo": "stream_events"}
            request = StreamEventsRequest(
                controller=controller.name,
                events=[StreamEventsRequest.Events(control=Control.BUTTON_START, events=[EventType.BUTTON_RELEASE])],
                extra=dict_to_struct(extra),
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
            assert controller.reg_extra == extra

    async def test_do(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = InputControllerServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=controller.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_geometries(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = InputControllerServiceStub(channel)
            request = GetGeometriesRequest(name=controller.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    async def test_get_controls(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)
            extra = {"foo": "get_controls"}
            controls = await client.get_controls(extra=extra, timeout=4.56)
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
            assert controller.extra == extra
            assert controller.timeout == expected_grpc_timeout(4.56)

    async def test_get_events(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)
            extra = {"foo": "get_events"}
            events = await client.get_events(extra=extra, timeout=5.67)
            assert events == controller.events
            assert controller.extra == extra
            assert controller.timeout == expected_grpc_timeout(5.67)

    async def test_trigger_event(self, controller: MockInputController, service: InputControllerRPCService):
        event = Event(time(), EventType.CONNECT, Control.ABSOLUTE_X, 0)
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)
            await client.trigger_event(event, timeout=6.78)
            assert controller.events[Control.ABSOLUTE_X].control == event.control
            assert controller.events[Control.ABSOLUTE_X].event == event.event
            assert controller.events[Control.ABSOLUTE_X].value == event.value
            # timestamp nanos conversion can result in differences in the 1e-7 scale
            assert abs(controller.events[Control.ABSOLUTE_X].time - event.time) < 0.000001
            assert controller.timeout == expected_grpc_timeout(6.78)
            assert controller.extra == {}

    async def test_register_control_callback(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)

            self.callback_called = False
            self.event_equal = False

            def test_event(event: Event):
                self.callback_called = True
                self.event_equal = event.control == Control.BUTTON_START and event.event == EventType.BUTTON_RELEASE and event.value == 0

            extra = {"foo": "register_control_callback"}
            client.register_control_callback(Control.BUTTON_START, [EventType.BUTTON_RELEASE], test_event, extra=extra)

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
            assert controller.extra is None
            assert controller.reg_extra == extra

    async def test_do(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    async def test_channel_rest(self, controller: MockInputController, service: InputControllerRPCService):
        channel = await ChannelFor([service]).__aenter__()
        client = ControllerClient(controller.name, channel)
        assert client._is_streaming is False  # not streaming before callback registered

        client.register_control_callback(Control.BUTTON_START, [EventType.BUTTON_RELEASE], lambda x: print(x))
        await asyncio.sleep(0.1)
        assert client._is_streaming is True  # registering callback should start streaming

        await channel.__aexit__(None, None, None)
        await asyncio.sleep(0.1)
        assert client._is_streaming is False  # closing the channel should cancel the stream

        async with ChannelFor([service]) as channel2:
            client.reset_channel(channel2)
            await asyncio.sleep(0.1)
            assert client._is_streaming is True  # reset the channel should restart the callback stream

    async def test_get_geometries(self, controller: MockInputController, service: InputControllerRPCService):
        async with ChannelFor([service]) as channel:
            client = ControllerClient(controller.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES
