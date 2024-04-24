import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component
from .powersensor_grpc import PowerSensorServiceBase as _PowerSensorServiceBase

class UnimplementedPowerSensorServiceBase(_PowerSensorServiceBase):

    async def GetVoltage(self, stream: 'grpclib.server.Stream[component.powersensor.v1.powersensor_pb2.GetVoltageRequest, component.powersensor.v1.powersensor_pb2.GetVoltageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetCurrent(self, stream: 'grpclib.server.Stream[component.powersensor.v1.powersensor_pb2.GetCurrentRequest, component.powersensor.v1.powersensor_pb2.GetCurrentResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPower(self, stream: 'grpclib.server.Stream[component.powersensor.v1.powersensor_pb2.GetPowerRequest, component.powersensor.v1.powersensor_pb2.GetPowerResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetReadings(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)