import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto

class BoardServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Status(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.StatusRequest, proto.api.component.board.v1.board_pb2.StatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetGPIO(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.SetGPIORequest, proto.api.component.board.v1.board_pb2.SetGPIOResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGPIO(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.GetGPIORequest, proto.api.component.board.v1.board_pb2.GetGPIOResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PWM(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.PWMRequest, proto.api.component.board.v1.board_pb2.PWMResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPWM(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.SetPWMRequest, proto.api.component.board.v1.board_pb2.SetPWMResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PWMFrequency(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.PWMFrequencyRequest, proto.api.component.board.v1.board_pb2.PWMFrequencyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPWMFrequency(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.SetPWMFrequencyRequest, proto.api.component.board.v1.board_pb2.SetPWMFrequencyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadAnalogReader(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.ReadAnalogReaderRequest, proto.api.component.board.v1.board_pb2.ReadAnalogReaderResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDigitalInterruptValue(self, stream: 'grpclib.server.Stream[proto.api.component.board.v1.board_pb2.GetDigitalInterruptValueRequest, proto.api.component.board.v1.board_pb2.GetDigitalInterruptValueResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.board.v1.BoardService/Status': grpclib.const.Handler(self.Status, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.StatusRequest, proto.api.component.board.v1.board_pb2.StatusResponse), '/proto.api.component.board.v1.BoardService/SetGPIO': grpclib.const.Handler(self.SetGPIO, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.SetGPIORequest, proto.api.component.board.v1.board_pb2.SetGPIOResponse), '/proto.api.component.board.v1.BoardService/GetGPIO': grpclib.const.Handler(self.GetGPIO, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.GetGPIORequest, proto.api.component.board.v1.board_pb2.GetGPIOResponse), '/proto.api.component.board.v1.BoardService/PWM': grpclib.const.Handler(self.PWM, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.PWMRequest, proto.api.component.board.v1.board_pb2.PWMResponse), '/proto.api.component.board.v1.BoardService/SetPWM': grpclib.const.Handler(self.SetPWM, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.SetPWMRequest, proto.api.component.board.v1.board_pb2.SetPWMResponse), '/proto.api.component.board.v1.BoardService/PWMFrequency': grpclib.const.Handler(self.PWMFrequency, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.PWMFrequencyRequest, proto.api.component.board.v1.board_pb2.PWMFrequencyResponse), '/proto.api.component.board.v1.BoardService/SetPWMFrequency': grpclib.const.Handler(self.SetPWMFrequency, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.SetPWMFrequencyRequest, proto.api.component.board.v1.board_pb2.SetPWMFrequencyResponse), '/proto.api.component.board.v1.BoardService/ReadAnalogReader': grpclib.const.Handler(self.ReadAnalogReader, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.ReadAnalogReaderRequest, proto.api.component.board.v1.board_pb2.ReadAnalogReaderResponse), '/proto.api.component.board.v1.BoardService/GetDigitalInterruptValue': grpclib.const.Handler(self.GetDigitalInterruptValue, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.board.v1.board_pb2.GetDigitalInterruptValueRequest, proto.api.component.board.v1.board_pb2.GetDigitalInterruptValueResponse)}

class BoardServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Status = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/Status', proto.api.component.board.v1.board_pb2.StatusRequest, proto.api.component.board.v1.board_pb2.StatusResponse)
        self.SetGPIO = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/SetGPIO', proto.api.component.board.v1.board_pb2.SetGPIORequest, proto.api.component.board.v1.board_pb2.SetGPIOResponse)
        self.GetGPIO = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/GetGPIO', proto.api.component.board.v1.board_pb2.GetGPIORequest, proto.api.component.board.v1.board_pb2.GetGPIOResponse)
        self.PWM = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/PWM', proto.api.component.board.v1.board_pb2.PWMRequest, proto.api.component.board.v1.board_pb2.PWMResponse)
        self.SetPWM = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/SetPWM', proto.api.component.board.v1.board_pb2.SetPWMRequest, proto.api.component.board.v1.board_pb2.SetPWMResponse)
        self.PWMFrequency = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/PWMFrequency', proto.api.component.board.v1.board_pb2.PWMFrequencyRequest, proto.api.component.board.v1.board_pb2.PWMFrequencyResponse)
        self.SetPWMFrequency = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/SetPWMFrequency', proto.api.component.board.v1.board_pb2.SetPWMFrequencyRequest, proto.api.component.board.v1.board_pb2.SetPWMFrequencyResponse)
        self.ReadAnalogReader = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/ReadAnalogReader', proto.api.component.board.v1.board_pb2.ReadAnalogReaderRequest, proto.api.component.board.v1.board_pb2.ReadAnalogReaderResponse)
        self.GetDigitalInterruptValue = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.board.v1.BoardService/GetDigitalInterruptValue', proto.api.component.board.v1.board_pb2.GetDigitalInterruptValueRequest, proto.api.component.board.v1.board_pb2.GetDigitalInterruptValueResponse)