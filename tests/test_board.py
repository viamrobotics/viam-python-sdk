import pytest
from grpclib import GRPCError
from grpclib.testing import ChannelFor
from viam.components.board import Board, BoardClient, BoardService
from viam.components.resource_manager import ResourceManager
from viam.errors import ComponentNotFoundError
from viam.proto.api.common import (AnalogStatus, BoardStatus,
                                   DigitalInterruptStatus)
from viam.proto.api.component.board import (BoardServiceStub,
                                            GetDigitalInterruptValueRequest,
                                            GetDigitalInterruptValueResponse,
                                            GetGPIORequest, GetGPIOResponse,
                                            ReadAnalogReaderRequest,
                                            ReadAnalogReaderResponse,
                                            SetGPIORequest,
                                            SetPWMFrequencyRequest,
                                            SetPWMRequest, StatusRequest,
                                            StatusResponse)

from .mocks.components import MockAnalogReader, MockBoard, MockDigitalInterrupt


@pytest.fixture(scope='function')
def board() -> MockBoard:
    return MockBoard(
        name="board",
        analog_readers={
            'reader1': MockAnalogReader('reader1', 3),
        },
        digital_interrupts={
            'interrupt1': MockDigitalInterrupt('interrupt1'),
        },
    )


@pytest.fixture(scope='function')
def service(board: MockBoard) -> BoardService:
    manager = ResourceManager([board])
    return BoardService(manager)


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
    async def test_analog_reader_names(self, board: MockBoard):
        names = await board.analog_reader_names()
        assert names == ['reader1']

    @pytest.mark.asyncio
    async def test_digital_interrupt_names(self, board: MockBoard):
        names = await board.digital_interrupt_names()
        assert names == ['interrupt1']

    @pytest.mark.asyncio
    async def test_set_gpio(self, board: MockBoard):
        await board.set_gpio('pin1', True)
        await board.set_gpio('pin2', False)
        assert board.gpios == {'pin1': True, 'pin2': False}

    @pytest.mark.asyncio
    async def test_get_gpio(self, board: MockBoard):
        with pytest.raises(KeyError):
            await board.get_gpio('pin1')

        await board.set_gpio('pin1', True)
        high = await board.get_gpio('pin1')
        return high is True

    @pytest.mark.asyncio
    async def test_set_pwm(self, board: MockBoard):
        await board.set_pwm('pin1', 12.3)
        await board.set_pwm('pin2', 45.6)
        assert board.pwms == {'pin1': 12.3, 'pin2': 45.6}

    @pytest.mark.asyncio
    async def test_set_pwm_freq(self, board: MockBoard):
        await board.set_pwm_freq('pin1', 123)
        await board.set_pwm_freq('pin2', 456)
        assert board.pwm_freqs == {'pin1': 123, 'pin2': 456}

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
            request = SetGPIORequest(name=board.name, pin='pin2', high=False)
            await client.SetGPIO(request)

            assert board.gpios == {'pin1': True, 'pin2': False}

    @pytest.mark.asyncio
    async def test_get_gpio(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardServiceStub(channel)

            with pytest.raises(GRPCError):
                request = GetGPIORequest(name=board.name, pin='pin1')
                await client.GetGPIO(request)

            request = SetGPIORequest(name=board.name, pin='pin1', high=True)
            await client.SetGPIO(request)

            request = GetGPIORequest(name=board.name, pin='pin1')
            response: GetGPIOResponse = await client.GetGPIO(request)
            return response.high is True

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
            request = SetPWMRequest(
                name=board.name, pin='pin2', duty_cycle_pct=45.6)
            await client.SetPWM(request)

            assert board.pwms == {'pin1': 12.3, 'pin2': 45.6}

    @pytest.mark.asyncio
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
            request = SetPWMFrequencyRequest(
                name=board.name, pin='pin2', frequency_hz=456)
            await client.SetPWMFrequency(request)

            assert board.pwm_freqs == {'pin1': 123, 'pin2': 456}

    @pytest.mark.asyncio
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
    async def test_set_gpio(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            await client.set_gpio('pin1', True)
            await client.set_gpio('pin2', False)
            assert board.gpios == {'pin1': True, 'pin2': False}

    @pytest.mark.asyncio
    async def test_get_gpio(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            with pytest.raises(GRPCError):
                await client.get_gpio('pin1')

            await client.set_gpio('pin1', True)
            high = await client.get_gpio('pin1')
            return high is True

    @pytest.mark.asyncio
    async def test_set_pwm(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            await client.set_pwm('pin1', 12.3)
            await client.set_pwm('pin2', 45.6)
            assert board.pwms == {'pin1': 12.3, 'pin2': 45.6}

    @pytest.mark.asyncio
    async def test_set_pwm_freq(
        self,
        board: MockBoard,
        service: BoardService
    ):
        async with ChannelFor([service]) as channel:
            client = BoardClient(name=board.name, channel=channel)

            await client.set_pwm_freq('pin1', 123)
            await client.set_pwm_freq('pin2', 456)
            assert board.pwm_freqs == {'pin1': 123, 'pin2': 456}

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
