from grpclib.server import Stream

from viam.components.power_sensor.power_sensor import PowerSensor
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetReadingsRequest, GetReadingsResponse
from viam.proto.component.powersensor import (
    GetCurrentRequest,
    GetCurrentResponse,
    GetPowerRequest,
    GetPowerResponse,
    GetVoltageRequest,
    GetVoltageResponse,
    PowerSensorServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, sensor_readings_native_to_value, struct_to_dict


class PowerSensorRPCService(PowerSensorServiceBase, ResourceRPCServiceBase[PowerSensor]):
    """
    gRPC Service for a PowerSensor
    """

    RESOURCE_TYPE = PowerSensor

    async def GetReadings(self, stream: Stream[GetReadingsRequest, GetReadingsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        sensor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        readings = await sensor.get_readings(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetReadingsResponse(readings=sensor_readings_native_to_value(readings))
        await stream.send_message(response)

    async def GetVoltage(self, stream: Stream[GetVoltageRequest, GetVoltageResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        sensor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        voltage, is_ac = await sensor.get_voltage(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetVoltageResponse(volts=voltage, is_ac=is_ac)
        await stream.send_message(response)

    async def GetCurrent(self, stream: Stream[GetCurrentRequest, GetCurrentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        sensor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        current, is_ac = await sensor.get_current(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetCurrentResponse(amperes=current, is_ac=is_ac)
        await stream.send_message(response)

    async def GetPower(self, stream: Stream[GetPowerRequest, GetPowerResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        sensor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        power = await sensor.get_power(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetPowerResponse(watts=power)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        sensor = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await sensor.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
