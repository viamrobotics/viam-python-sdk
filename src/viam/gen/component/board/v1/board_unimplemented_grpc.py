import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
from .... import component
from .board_grpc import BoardServiceBase as _BoardServiceBase

class UnimplementedBoardServiceBase(_BoardServiceBase):

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