from typing import cast
import pytest
from grpclib import GRPCError
from grpclib.testing import ChannelFor
from viam.components.board import Board, BoardClient
from viam.components.board.service import BoardService
from viam.components.generic.service import GenericService
from viam.components.resource_manager import ResourceManager
from viam.errors import ComponentNotFoundError
from viam.proto.api.common import (AnalogStatus, BoardStatus,
                                   DigitalInterruptStatus)
from viam.proto.api.component.board import (BoardServiceStub,
                                            GetDigitalInterruptValueRequest,
                                            GetDigitalInterruptValueResponse,
                                            GetGPIORequest, GetGPIOResponse,
                                            PWMFrequencyRequest,
                                            PWMFrequencyResponse, PWMRequest,
                                            PWMResponse,
                                            ReadAnalogReaderRequest,
                                            ReadAnalogReaderResponse,
                                            SetGPIORequest,
                                            SetPWMFrequencyRequest,
                                            SetPWMRequest, StatusRequest,
                                            StatusResponse)

from .mocks.components import (MockAnalogReader, MockBoard,
                               MockDigitalInterrupt, MockGPIOPin)


@pytest.fixture(scope='function')
def board() -> MockBoard:
    return MockBoard(
        name='board',
        analog_readers={
            'reader1': MockAnalogReader('reader1', 3),
        },
        digital_interrupts={
            'interrupt1': MockDigitalInterrupt('interrupt1'),
        },
        gpio_pins={
            'pin1': MockGPIOPin('pin1')
        }
    )


@pytest.fixture(scope='function')
def service(board: MockBoard) -> BoardService:
    manager = ResourceManager([board])
    return BoardService(manager)


@pytest.fixture(scope='function')
def generic_service(board: MockBoard) -> GenericService:
    manager = ResourceManager([board])
    return GenericService(manager)


class TestBoard:
    @pytest.mark.asyncio
    async def test_analog_reader_by_name(self, board: MockBoard):
        with pytest.raises(ComponentNotFoundError):
            await board.analog_reader_by_name('does not exist')

        reader = await board.analog_reader_by_name('reader1')
        assert reader.name == 'reader1'

    @pytest.mark.asyncio
    async def test_digital_interrupt_by_name(self, board: MockBoard):
        with pytest.raises(ComponentNotFoundError):
            await board.digital_interrupt_by_name('does not exist')

        interrupt = await board.digital_interrupt_by_name('interrupt1')
        assert interrupt.name == 'interrupt1'

    @pytest.mark.asyncio
    async def test_gpio_pin_by_name(self, board: MockBoard):
        with pytest.raises(ComponentNotFoundError):
            await board.digital_interrupt_by_name('does not exist')

        pin = await board.gpio_pin_by_name('pin1')
        assert pin.name == 'pin1'

    @pytest.mark.asyncio
    async def test_analog_reader_names(self, board: MockBoard):
        names = await board.analog_reader_names()
        assert names == ['reader1']

    @pytest.mark.asyncio
    async def test_digital_interrupt_names(self, board: MockBoard):
        names = await board.digital_interrupt_names()
        assert names == ['interrupt1']

    @pytest.mark.asyncio
    async def test_status(self, board: MockBoard):
        status = await board.status()
        assert status == BoardStatus(
            analogs={
                'reader1': AnalogStatus(value=3)
            },
            digital_interrupts={
                'interrupt1': DigitalInterruptStatus(value=0)
            },
        )

    @pytest.mark.asyncio
    async def test_model_attributes(self, board: MockBoard):
        attrs = await board.model_attributes()
        assert attrs == Board.Attributes(remote=True)

    @pytest.mark.asyncio
    async def test_do(self, board: MockBoard):
        with pytest.raises(NotImplementedError):
            await board.do({'command': 'args'})


class TestService:
    @pytest.mark.asyncio
    async def test_read_analog_reader(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError, match=r'.*Status.NOT_FOUND.*'):
                request = ReadAnalogReaderRequest(
                    board_name=board.name, analog_reader_name='dne')
                await client.ReadAnalogReader(request)

            request = ReadAnalogReaderRequest(
                board_name=board.name, analog_reader_name='reader1')
            response: ReadAnalogReaderResponse = \
                await client.ReadAnalogReader(request)
            assert response.value == 3

    @pytest.mark.asyncio
    async def test_get_digital_interrupt_value(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError, match=r'.*Status.NOT_FOUND.*'):
                request = GetDigitalInterruptValueRequest(
                    board_name=board.name, digital_interrupt_name='dne')
                await client.GetDigitalInterruptValue(request)

            request = GetDigitalInterruptValueRequest(
                board_name=board.name, digital_interrupt_name='interrupt1')
            response: GetDigitalInterruptValueResponse = \
                await client.GetDigitalInterruptValue(request)
            assert response.value == 0

    @pytest.mark.asyncio
    async def test_set_gpio(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            request = SetGPIORequest(name=board.name, pin='pin1', high=True)
            await client.SetGPIO(request)

            assert cast(MockGPIOPin, board.gpios['pin1']).high is True

    @pytest.mark.asyncio
    async def test_get_gpio(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError):
                request = GetGPIORequest(name=board.name, pin='pin2')
                await client.GetGPIO(request)

            request = GetGPIORequest(name=board.name, pin='pin1')
            response: GetGPIOResponse = await client.GetGPIO(request)
            return response.high is False

    @pytest.mark.asyncio
    async def test_pwm(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            request = PWMRequest(name=board.name, pin='pin1')
            response: PWMResponse = await client.PWM(request)
            assert response.duty_cycle_pct == 0.0

    @pytest.mark.asyncio
    async def test_set_pwm(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            request = SetPWMRequest(
                name=board.name, pin='pin1', duty_cycle_pct=12.3)
            await client.SetPWM(request)

            assert cast(MockGPIOPin, board.gpios['pin1']).pwm == 12.3

    @pytest.mark.asyncio
    async def test_pwm_frequency(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            request = PWMFrequencyRequest(name=board.name, pin='pin1')
            response: PWMFrequencyResponse = await client.PWMFrequency(request)
            assert response.frequency_hz == 0

    @ pytest.mark.asyncio
    async def test_set_pwm_freq(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            request = SetPWMFrequencyRequest(
                name=board.name, pin='pin1', frequency_hz=123)
            await client.SetPWMFrequency(request)

            assert cast(MockGPIOPin, board.gpios['pin1']).pwm_freq == 123

    @ pytest.mark.asyncio
    async def test_status(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            request = StatusRequest(name=board.name)
            response: StatusResponse = await client.Status(request)

            assert response.status == BoardStatus(
                analogs={
                    'reader1': AnalogStatus(value=3)
                },
                digital_interrupts={
                    'interrupt1': DigitalInterruptStatus(value=0)
                },
            )


class TestClient:
    @pytest.mark.asyncio
    async def test_analog_reader_by_name(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            reader = await client.analog_reader_by_name('does not exist')
            assert reader.name == 'does not exist'
            with pytest.raises(GRPCError, match=r'.*Status.NOT_FOUND.*'):
                await reader.read()

            reader = await client.analog_reader_by_name('reader1')
            assert reader.name == 'reader1'

    @pytest.mark.asyncio
    async def test_digital_interrupt_by_name(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            interrupt = await client.digital_interrupt_by_name('dne')
            assert interrupt.name == 'dne'
            with pytest.raises(GRPCError, match=r'.*Status.NOT_FOUND.*'):
                await interrupt.value()

            interrupt = await client.digital_interrupt_by_name('interrupt1')
            assert interrupt.name == 'interrupt1'

    @pytest.mark.asyncio
    async def test_gpio_pin_by_name(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            pin = await client.gpio_pin_by_name('dne')
            assert pin.name == 'dne'
            with pytest.raises(GRPCError, match=r'.*Status.NOT_FOUND.*'):
                await pin.get()

            pin = await client.gpio_pin_by_name('pin1')
            assert pin.name == 'pin1'

    @pytest.mark.asyncio
    async def test_analog_reader_names(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            names = await client.analog_reader_names()
            assert names == ['reader1']

    @pytest.mark.asyncio
    async def test_digital_interrupt_names(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            names = await client.digital_interrupt_names()
            assert names == ['interrupt1']

    @pytest.mark.asyncio
    async def test_status(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            status = await client.status()
            assert status == BoardStatus(
                analogs={
                    'reader1': AnalogStatus(value=3)
                },
                digital_interrupts={
                    'interrupt1': DigitalInterruptStatus(value=0)
                },
            )

    @pytest.mark.asyncio
    async def test_model_attributes(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            attrs = await client.model_attributes()
            assert attrs == Board.Attributes(remote=True)


class TestGPIOPinClient:
    @pytest.mark.asyncio
    async def test_set(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name('pin1')

            await pin.set(True)
            assert cast(MockGPIOPin, board.gpios['pin1']).high is True

    @pytest.mark.asyncio
    async def test_get(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name('pin1')
            high = await pin.get()
            assert high is False

    @pytest.mark.asyncio
    async def test_set_pwm(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name('pin1')

            await pin.set_pwm(12.3)
            assert cast(MockGPIOPin, board.gpios['pin1']).pwm == 12.3

    @pytest.mark.asyncio
    async def test_get_pwm(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name('pin1')
            pwm = await pin.get_pwm()
            assert pwm == 0.0

    @pytest.mark.asyncio
    async def test_set_pwm_frequency(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name('pin1')

            await pin.set_pwm_frequency(123)
            assert cast(MockGPIOPin, board.gpios['pin1']).pwm_freq == 123

    @pytest.mark.asyncio
    async def test_get_pwm_freq(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)
            pin = await client.gpio_pin_by_name('pin1')
            freq = await pin.get_pwm_frequency()
            assert freq == 0

    @pytest.mark.asyncio
    async def test_do(self, board: MockBoard, service: BoardService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = BoardClient(board.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do({'command': 'args'})
