from typing import Any, Dict, Mapping, Optional, Tuple

from grpclib.client import Channel

from viam.components.power_sensor.power_sensor import PowerSensor
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetReadingsRequest, GetReadingsResponse
from viam.proto.component.powersensor import (
    GetCurrentRequest,
    GetCurrentResponse,
    GetPowerRequest,
    GetPowerResponse,
    GetVoltageRequest,
    GetVoltageResponse,
    PowerSensorServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import SensorReading, ValueTypes, dict_to_struct, sensor_readings_value_to_native, struct_to_dict


class PowerSensorClient(PowerSensor, ReconfigurableResourceRPCClientBase):
    """gRPC client for the PowerSensor component."""

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = PowerSensorServiceStub(channel)
        super().__init__(name)

    async def get_voltage(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[float, bool]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetVoltageRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetVoltageResponse = await self.client.GetVoltage(request, timeout=timeout, metadata=md)
        return response.volts, response.is_ac

    async def get_current(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[float, bool]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetCurrentRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetCurrentResponse = await self.client.GetCurrent(request, timeout=timeout, metadata=md)
        return response.amperes, response.is_ac

    async def get_power(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> float:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPowerRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPowerResponse = await self.client.GetPower(request, timeout=timeout, metadata=md)
        return response.watts

    async def get_readings(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, SensorReading]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetReadingsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetReadingsResponse = await self.client.GetReadings(request, timeout=timeout, metadata=md)
        return sensor_readings_value_to_native(response.readings)

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
