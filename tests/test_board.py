from datetime import timedelta
from typing import cast

import pytest
from google.protobuf.duration_pb2 import Duration
from grpclib import GRPCError
from grpclib.testing import ChannelFor

from viam.components.board import BoardClient, BoardStatus, create_status
from viam.components.board.service import BoardRPCService
from viam.components.generic.service import GenericRPCService
from viam.errors import ResourceNotFoundError
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.board import (
    BoardServiceStub,
    GetDigitalInterruptValueRequest,
    GetDigitalInterruptValueResponse,
    GetGPIORequest,
    GetGPIOResponse,
    PowerMode,
    PWMFrequencyRequest,
    PWMFrequencyResponse,
    PWMRequest,
    PWMResponse,
    ReadAnalogReaderRequest,
    ReadAnalogReaderResponse,
    SetGPIORequest,
    SetPowerModeRequest,
    SetPowerModeResponse,
    SetPWMFrequencyRequest,
    SetPWMRequest,
    StreamTicksRequest,
    WriteAnalogRequest,
    WriteAnalogResponse,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, message_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import GEOMETRIES, MockAnalog, MockBoard, MockDigitalInterrupt, MockGPIOPin


@pytest.fixture(scope="function")
def board() -> MockBoard:
    return MockBoard(
        name="board",
        analogs={
            "reader1": MockAnalog("reader1", 3),
            "writer1": MockAnalog("writer1", 5),
        },
        digital_interrupts={
            "interrupt1": MockDigitalInterrupt("interrupt1"),
        },
        gpio_pins={"pin1": MockGPIOPin("pin1")},
    )


@pytest.fixture(scope="function")
def service(board: MockBoard) -> BoardRPCService:
    manager = ResourceManager([board])
    return BoardRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(board: MockBoard) -> GenericRPCService:
    manager = ResourceManager([board])
    return GenericRPCService(manager)


class TestBoard:
    @pytest.mark.asyncio
    async def test_analog_by_name(self, board: MockBoard):
        with pytest.raises(ResourceNotFoundError):
            await board.analog_by_name("does not exist")

        reader = await board.analog_by_name("reader1")
        assert reader.name == "reader1"

    @pytest.mark.asyncio
    async def test_digital_interrupt_by_name(self, board: MockBoard):
        with pytest.raises(ResourceNotFoundError):
            await board.digital_interrupt_by_name("does not exist")

        interrupt = await board.digital_interrupt_by_name("interrupt1")
        assert interrupt.name == "interrupt1"

    @pytest.mark.asyncio
    async def test_gpio_pin_by_name(self, board: MockBoard):
        with pytest.raises(ResourceNotFoundError):
            await board.digital_interrupt_by_name("does not exist")

        pin = await board.gpio_pin_by_name("pin1")
        assert pin.name == "pin1"

    @pytest.mark.asyncio
    async def test_analog_names(self, board: MockBoard):
        names = await board.analog_names()
        assert names == ["reader1", "writer1"]

    @pytest.mark.asyncio
    async def test_digital_interrupt_names(self, board: MockBoard):
        names = await board.digital_interrupt_names()
        assert names == ["interrupt1"]

    @pytest.mark.asyncio
    async def test_do(self, board: MockBoard):
        command = {"command": "args"}
        resp = await board.do_command(command)
        assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_status(self, board: MockBoard):
        status = await create_status(board)
        read1 = await board.analogs["reader1"].read()
        # Analog writers typically don't have read statuses, but the mock board
        # doesn't make that distinction.
        read2 = await board.analogs["writer1"].read()
        val = await board.digital_interrupts["interrupt1"].value()
        assert status.name == MockBoard.get_resource_name(board.name)
        assert status.status == message_to_struct(
            BoardStatus(
                analogs={"reader1": int(read1), "writer1": int(read2)},
                digital_interrupts={"interrupt1": val},
            )
        )

    @pytest.mark.asyncio
    async def test_set_power_mode(self, board: MockBoard):
        pm_mode = PowerMode.POWER_MODE_OFFLINE_DEEP
        pm_duration = timedelta(minutes=1)
        await board.set_power_mode(mode=pm_mode, duration=pm_duration, timeout=1.11)
        assert board.timeout == loose_approx(1.11)
        assert board.power_mode == pm_mode
        assert board.power_mode_duration == pm_duration

    @pytest.mark.asyncio
    async def test_get_geometries(self, board: MockBoard):
        geometries = await board.get_geometries()
        assert geometries == GEOMETRIES

    @pytest.mark.asyncio
    async def test_write_analog(self, board: MockBoard):
        value = 10
        pin = "writer1"
        writer = await board.analog_by_name(name=pin)
        await writer.write(value=value, timeout=1.11)
        assert writer.timeout == loose_approx(1.11)
        assert writer.value == value
        assert writer.name == pin

    @pytest.mark.asyncio
    async def test_stream_ticks(self, board: MockBoard):
        int1 = board.digital_interrupts["interrupt1"]
        async for tick in await board.stream_ticks([int1]):
            assert tick.pin_name == "interrupt1"
            assert tick.time == 1000
            assert tick.high is True


class TestService:
    @pytest.mark.asyncio
    async def test_read_analog(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                request = ReadAnalogReaderRequest(board_name=board.name, analog_reader_name="dne")
                await client.ReadAnalogReader(request)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = ReadAnalogReaderRequest(board_name=board.name, analog_reader_name="reader1", extra=dict_to_struct(extra))
            response: ReadAnalogReaderResponse = await client.ReadAnalogReader(request, timeout=4.4)
            assert response.value == 3

            reader = cast(MockAnalog, board.analogs["reader1"])
            assert reader.extra == extra
            assert reader.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_digital_interrupt_value(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            request = GetDigitalInterruptValueRequest(board_name=board.name, digital_interrupt_name="dne")
            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                await client.GetDigitalInterruptValue(request)

            request = GetDigitalInterruptValueRequest(board_name=board.name, digital_interrupt_name="interrupt1")
            response: GetDigitalInterruptValueResponse = await client.GetDigitalInterruptValue(request)
            assert response.value == 0

    @pytest.mark.asyncio
    async def test_set_gpio(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = SetGPIORequest(name=board.name, pin="pin1", high=True, extra=dict_to_struct(extra))
            await client.SetGPIO(request, timeout=4.1)

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.high is True
            assert pin.extra == extra
            assert pin.timeout == loose_approx(4.1)

    @pytest.mark.asyncio
    async def test_get_gpio(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError):
                request = GetGPIORequest(name=board.name, pin="pin2")
                await client.GetGPIO(request)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = GetGPIORequest(name=board.name, pin="pin1", extra=dict_to_struct(extra))
            response: GetGPIOResponse = await client.GetGPIO(request, timeout=1.82)
            assert response.high is False

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.extra == extra
            assert pin.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_pwm(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = PWMRequest(name=board.name, pin="pin1", extra=dict_to_struct(extra))
            response: PWMResponse = await client.PWM(request, timeout=7.86)
            assert response.duty_cycle_pct == 0.0

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.extra == extra
            assert pin.timeout == loose_approx(7.86)

    @pytest.mark.asyncio
    async def test_set_pwm(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = SetPWMRequest(name=board.name, pin="pin1", duty_cycle_pct=12.3, extra=dict_to_struct(extra))
            await client.SetPWM(request, timeout=1.213)

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.pwm == 12.3
            assert pin.extra == extra
            assert pin.timeout == loose_approx(1.213)

    @pytest.mark.asyncio
    async def test_pwm_frequency(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = PWMFrequencyRequest(name=board.name, pin="pin1", extra=dict_to_struct(extra))
            response: PWMFrequencyResponse = await client.PWMFrequency(request, timeout=182)
            assert response.frequency_hz == 0

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.extra == extra
            assert pin.timeout == loose_approx(182)

    @pytest.mark.asyncio
    async def test_set_pwm_freq(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = SetPWMFrequencyRequest(name=board.name, pin="pin1", frequency_hz=123, extra=dict_to_struct(extra))
            await client.SetPWMFrequency(request)

            pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert pin.pwm_freq == 123
            assert pin.extra == extra
            assert pin.timeout is None

    @pytest.mark.asyncio
    async def test_do(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=board.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    @pytest.mark.asyncio
    async def test_get_geometries(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)
            request = GetGeometriesRequest(name=board.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES

    @pytest.mark.asyncio
    async def test_set_power_mode(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)
            pm_mode = PowerMode.POWER_MODE_OFFLINE_DEEP
            pm_duration = Duration()
            pm_duration.FromTimedelta(timedelta(minutes=1))
            request = SetPowerModeRequest(name=board.name, power_mode=pm_mode, duration=pm_duration)
            response: SetPowerModeResponse = await client.SetPowerMode(request, timeout=6.66)
            assert response == SetPowerModeResponse()
            assert board.timeout == loose_approx(6.66)
            assert board.power_mode == PowerMode.POWER_MODE_OFFLINE_DEEP
            assert board.power_mode_duration == pm_duration.ToTimedelta()

    @pytest.mark.asyncio
    async def test_write_analog(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)
            pin = "writer1"
            value = 10
            request = WriteAnalogRequest(name=board.name, pin=pin, value=value)
            response: WriteAnalogResponse = await client.WriteAnalog(request, timeout=6.66)
            assert response == WriteAnalogResponse()
            mock_analog = cast(MockAnalog, board.analogs["writer1"])
            assert mock_analog.timeout == loose_approx(6.66)
            assert mock_analog.value == value
            assert mock_analog.name == pin

    # @pytest.mark.asyncio
    async def test_stream_ticks(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)
            interrupts = ["interrupt1"]
            extra = {"foo": "stream_ticks"}
            request = StreamTicksRequest(name=board.name, pin_names=interrupts, extra=dict_to_struct(extra))

            async with client.StreamTicks.open(timeout=1) as stream:
                await stream.send_message(request, end=True)
                resp = await stream.recv_message()
                assert resp is not None
                assert resp.pin_name == "interrupt1"
                assert resp.high is True
                assert resp.time == 1000


class TestClient:
    @pytest.mark.asyncio
    async def test_analog_by_name(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            reader = await client.analog_by_name("does not exist")
            assert reader.name == "does not exist"
            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                await reader.read()

            reader = await client.analog_by_name("reader1")
            assert reader.name == "reader1"

    @pytest.mark.asyncio
    async def test_digital_interrupt_by_name(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            interrupt = await client.digital_interrupt_by_name("dne")
            assert interrupt.name == "dne"
            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                await interrupt.value()

            interrupt = await client.digital_interrupt_by_name("interrupt1")
            assert interrupt.name == "interrupt1"

    @pytest.mark.asyncio
    async def test_gpio_pin_by_name(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            pin = await client.gpio_pin_by_name("dne")
            assert pin.name == "dne"
            with pytest.raises(GRPCError, match=r".*Status.NOT_FOUND.*"):
                await pin.get()

            pin = await client.gpio_pin_by_name("pin1")
            assert pin.name == "pin1"

    @pytest.mark.asyncio
    async def test_analog_names(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            reader = await client.analog_by_name("reader1")
            assert reader.name == "reader1"

            names = await client.analog_names()
            assert names == ["reader1"]

    @pytest.mark.asyncio
    async def test_digital_interrupt_names(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            interrupt = await client.digital_interrupt_by_name("interrupt1")
            assert interrupt.name == "interrupt1"

            names = await client.digital_interrupt_names()
            assert names == ["interrupt1"]

    @pytest.mark.asyncio
    async def test_do(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(board.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_set_power_mode(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pm_mode = PowerMode.POWER_MODE_OFFLINE_DEEP
            pm_timedelta = timedelta(minutes=1)
            await client.set_power_mode(mode=pm_mode, duration=pm_timedelta, timeout=1.1)
            assert board.timeout == loose_approx(1.1)
            assert board.power_mode == pm_mode
            pm_duration = Duration()
            pm_duration.FromTimedelta(pm_timedelta)
            assert board.power_mode_duration == pm_duration.ToTimedelta()

    @pytest.mark.asyncio
    async def test_extra(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(board.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES


class TestGPIOPinClient:
    @pytest.mark.asyncio
    async def test_set(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await pin.set(True, extra=extra, timeout=1.82)

            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.high is True
            assert mock_pin.extra == extra
            assert mock_pin.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_get(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            high = await pin.get(extra=extra)
            assert high is False
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.extra == extra
            assert mock_pin.timeout is None

    @pytest.mark.asyncio
    async def test_set_pwm(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await pin.set_pwm(12.3, extra=extra, timeout=3.23)
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.pwm == 12.3
            assert mock_pin.extra == extra
            assert mock_pin.timeout == loose_approx(3.23)

    @pytest.mark.asyncio
    async def test_get_pwm(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            pwm = await pin.get_pwm(extra=extra, timeout=1.2345)
            assert pwm == 0.0
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.extra == extra
            assert mock_pin.timeout == loose_approx(1.2345)

    @pytest.mark.asyncio
    async def test_set_pwm_frequency(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await pin.set_pwm_frequency(123, extra=extra, timeout=4.341)
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.pwm_freq == 123
            assert mock_pin.extra == extra
            assert mock_pin.timeout == loose_approx(4.341)

    @pytest.mark.asyncio
    async def test_get_pwm_freq(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name("pin1")
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            freq = await pin.get_pwm_frequency(extra=extra)
            assert freq == 0
            mock_pin = cast(MockGPIOPin, board.gpios["pin1"])
            assert mock_pin.extra == extra
            assert mock_pin.timeout is None

    @pytest.mark.asyncio
    async def test_write_analog(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            writer = await client.analog_by_name("writer1")
            value = 42
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await writer.write(value, extra=extra)
            mock_analog = cast(MockAnalog, board.analogs["writer1"])
            assert mock_analog.name == "writer1"
            assert mock_analog.value == 42
            assert mock_analog.extra == extra

    @pytest.mark.asyncio
    async def test_stream_ticks(self, board: MockBoard, service: BoardRPCService):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            di = await client.digital_interrupt_by_name("interrupt1")

            tick_stream = await client.stream_ticks(interrupts=[di])
            async for tick in tick_stream:
                assert tick.pin_name == "interrupt1"
                assert tick.high is True
                assert tick.time == 1000
                break
