import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
from .... import component

class BoardServiceBase(abc.ABC):

    @abc.abstractmethod
    async def SetGPIO(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.SetGPIORequest, component.board.v1.board_pb2.SetGPIOResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGPIO(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.GetGPIORequest, component.board.v1.board_pb2.GetGPIOResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PWM(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.PWMRequest, component.board.v1.board_pb2.PWMResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPWM(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.SetPWMRequest, component.board.v1.board_pb2.SetPWMResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PWMFrequency(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.PWMFrequencyRequest, component.board.v1.board_pb2.PWMFrequencyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPWMFrequency(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.SetPWMFrequencyRequest, component.board.v1.board_pb2.SetPWMFrequencyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadAnalogReader(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.ReadAnalogReaderRequest, component.board.v1.board_pb2.ReadAnalogReaderResponse]') -> None:
        pass

    @abc.abstractmethod
    async def WriteAnalog(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.WriteAnalogRequest, component.board.v1.board_pb2.WriteAnalogResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDigitalInterruptValue(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.GetDigitalInterruptValueRequest, component.board.v1.board_pb2.GetDigitalInterruptValueResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamTicks(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.StreamTicksRequest, component.board.v1.board_pb2.StreamTicksResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPowerMode(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.SetPowerModeRequest, component.board.v1.board_pb2.SetPowerModeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.board.v1.BoardService/SetGPIO': grpclib.const.Handler(self.SetGPIO, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.SetGPIORequest, component.board.v1.board_pb2.SetGPIOResponse), '/viam.component.board.v1.BoardService/GetGPIO': grpclib.const.Handler(self.GetGPIO, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.GetGPIORequest, component.board.v1.board_pb2.GetGPIOResponse), '/viam.component.board.v1.BoardService/PWM': grpclib.const.Handler(self.PWM, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.PWMRequest, component.board.v1.board_pb2.PWMResponse), '/viam.component.board.v1.BoardService/SetPWM': grpclib.const.Handler(self.SetPWM, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.SetPWMRequest, component.board.v1.board_pb2.SetPWMResponse), '/viam.component.board.v1.BoardService/PWMFrequency': grpclib.const.Handler(self.PWMFrequency, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.PWMFrequencyRequest, component.board.v1.board_pb2.PWMFrequencyResponse), '/viam.component.board.v1.BoardService/SetPWMFrequency': grpclib.const.Handler(self.SetPWMFrequency, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.SetPWMFrequencyRequest, component.board.v1.board_pb2.SetPWMFrequencyResponse), '/viam.component.board.v1.BoardService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.board.v1.BoardService/ReadAnalogReader': grpclib.const.Handler(self.ReadAnalogReader, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.ReadAnalogReaderRequest, component.board.v1.board_pb2.ReadAnalogReaderResponse), '/viam.component.board.v1.BoardService/WriteAnalog': grpclib.const.Handler(self.WriteAnalog, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.WriteAnalogRequest, component.board.v1.board_pb2.WriteAnalogResponse), '/viam.component.board.v1.BoardService/GetDigitalInterruptValue': grpclib.const.Handler(self.GetDigitalInterruptValue, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.GetDigitalInterruptValueRequest, component.board.v1.board_pb2.GetDigitalInterruptValueResponse), '/viam.component.board.v1.BoardService/StreamTicks': grpclib.const.Handler(self.StreamTicks, grpclib.const.Cardinality.UNARY_STREAM, component.board.v1.board_pb2.StreamTicksRequest, component.board.v1.board_pb2.StreamTicksResponse), '/viam.component.board.v1.BoardService/SetPowerMode': grpclib.const.Handler(self.SetPowerMode, grpclib.const.Cardinality.UNARY_UNARY, component.board.v1.board_pb2.SetPowerModeRequest, component.board.v1.board_pb2.SetPowerModeResponse), '/viam.component.board.v1.BoardService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedBoardServiceBase(BoardServiceBase):

    async def SetGPIO(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.SetGPIORequest, component.board.v1.board_pb2.SetGPIOResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGPIO(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.GetGPIORequest, component.board.v1.board_pb2.GetGPIOResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def PWM(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.PWMRequest, component.board.v1.board_pb2.PWMResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetPWM(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.SetPWMRequest, component.board.v1.board_pb2.SetPWMResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def PWMFrequency(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.PWMFrequencyRequest, component.board.v1.board_pb2.PWMFrequencyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetPWMFrequency(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.SetPWMFrequencyRequest, component.board.v1.board_pb2.SetPWMFrequencyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ReadAnalogReader(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.ReadAnalogReaderRequest, component.board.v1.board_pb2.ReadAnalogReaderResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def WriteAnalog(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.WriteAnalogRequest, component.board.v1.board_pb2.WriteAnalogResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetDigitalInterruptValue(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.GetDigitalInterruptValueRequest, component.board.v1.board_pb2.GetDigitalInterruptValueResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StreamTicks(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.StreamTicksRequest, component.board.v1.board_pb2.StreamTicksResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetPowerMode(self, stream: 'grpclib.server.Stream[component.board.v1.board_pb2.SetPowerModeRequest, component.board.v1.board_pb2.SetPowerModeResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class BoardServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetGPIO = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/SetGPIO', component.board.v1.board_pb2.SetGPIORequest, component.board.v1.board_pb2.SetGPIOResponse)
        self.GetGPIO = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/GetGPIO', component.board.v1.board_pb2.GetGPIORequest, component.board.v1.board_pb2.GetGPIOResponse)
        self.PWM = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/PWM', component.board.v1.board_pb2.PWMRequest, component.board.v1.board_pb2.PWMResponse)
        self.SetPWM = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/SetPWM', component.board.v1.board_pb2.SetPWMRequest, component.board.v1.board_pb2.SetPWMResponse)
        self.PWMFrequency = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/PWMFrequency', component.board.v1.board_pb2.PWMFrequencyRequest, component.board.v1.board_pb2.PWMFrequencyResponse)
        self.SetPWMFrequency = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/SetPWMFrequency', component.board.v1.board_pb2.SetPWMFrequencyRequest, component.board.v1.board_pb2.SetPWMFrequencyResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.ReadAnalogReader = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/ReadAnalogReader', component.board.v1.board_pb2.ReadAnalogReaderRequest, component.board.v1.board_pb2.ReadAnalogReaderResponse)
        self.WriteAnalog = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/WriteAnalog', component.board.v1.board_pb2.WriteAnalogRequest, component.board.v1.board_pb2.WriteAnalogResponse)
        self.GetDigitalInterruptValue = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/GetDigitalInterruptValue', component.board.v1.board_pb2.GetDigitalInterruptValueRequest, component.board.v1.board_pb2.GetDigitalInterruptValueResponse)
        self.StreamTicks = grpclib.client.UnaryStreamMethod(channel, '/viam.component.board.v1.BoardService/StreamTicks', component.board.v1.board_pb2.StreamTicksRequest, component.board.v1.board_pb2.StreamTicksResponse)
        self.SetPowerMode = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/SetPowerMode', component.board.v1.board_pb2.SetPowerModeRequest, component.board.v1.board_pb2.SetPowerModeResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.board.v1.BoardService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)