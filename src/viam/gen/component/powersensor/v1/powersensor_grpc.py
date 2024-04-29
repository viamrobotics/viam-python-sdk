import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component

class PowerSensorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetVoltage(self, stream: 'grpclib.server.Stream[component.powersensor.v1.powersensor_pb2.GetVoltageRequest, component.powersensor.v1.powersensor_pb2.GetVoltageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCurrent(self, stream: 'grpclib.server.Stream[component.powersensor.v1.powersensor_pb2.GetCurrentRequest, component.powersensor.v1.powersensor_pb2.GetCurrentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPower(self, stream: 'grpclib.server.Stream[component.powersensor.v1.powersensor_pb2.GetPowerRequest, component.powersensor.v1.powersensor_pb2.GetPowerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetReadings(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.powersensor.v1.PowerSensorService/GetVoltage': grpclib.const.Handler(self.GetVoltage, grpclib.const.Cardinality.UNARY_UNARY, component.powersensor.v1.powersensor_pb2.GetVoltageRequest, component.powersensor.v1.powersensor_pb2.GetVoltageResponse), '/viam.component.powersensor.v1.PowerSensorService/GetCurrent': grpclib.const.Handler(self.GetCurrent, grpclib.const.Cardinality.UNARY_UNARY, component.powersensor.v1.powersensor_pb2.GetCurrentRequest, component.powersensor.v1.powersensor_pb2.GetCurrentResponse), '/viam.component.powersensor.v1.PowerSensorService/GetPower': grpclib.const.Handler(self.GetPower, grpclib.const.Cardinality.UNARY_UNARY, component.powersensor.v1.powersensor_pb2.GetPowerRequest, component.powersensor.v1.powersensor_pb2.GetPowerResponse), '/viam.component.powersensor.v1.PowerSensorService/GetReadings': grpclib.const.Handler(self.GetReadings, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse), '/viam.component.powersensor.v1.PowerSensorService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedPowerSensorServiceBase(PowerSensorServiceBase):

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

class PowerSensorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetVoltage = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.powersensor.v1.PowerSensorService/GetVoltage', component.powersensor.v1.powersensor_pb2.GetVoltageRequest, component.powersensor.v1.powersensor_pb2.GetVoltageResponse)
        self.GetCurrent = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.powersensor.v1.PowerSensorService/GetCurrent', component.powersensor.v1.powersensor_pb2.GetCurrentRequest, component.powersensor.v1.powersensor_pb2.GetCurrentResponse)
        self.GetPower = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.powersensor.v1.PowerSensorService/GetPower', component.powersensor.v1.powersensor_pb2.GetPowerRequest, component.powersensor.v1.powersensor_pb2.GetPowerResponse)
        self.GetReadings = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.powersensor.v1.PowerSensorService/GetReadings', common.v1.common_pb2.GetReadingsRequest, common.v1.common_pb2.GetReadingsResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.powersensor.v1.PowerSensorService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)