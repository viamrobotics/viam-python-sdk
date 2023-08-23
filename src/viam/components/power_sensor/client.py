from typing import Any, Dict, Mapping, Optional, Tuple

from grpclib.client import Channel

from viam.components.power_sensor.power_sensor import PowerSensor
from viam.proto.common import DoCommandRequest, DoCommandResponse
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
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict


class PowerSensorClient(PowerSensor, ReconfigurableResourceRPCClientBase):
    """gRPC client for the PowerSensor component."""

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = PowerSensorServiceStub(channel)
        super().__init__(name)

    async def get_voltage(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Tuple[float, bool]:
        if extra is None:
            extra = {}
        request = GetVoltageRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetVoltageResponse = await self.client.GetVoltage(request, timeout=timeout)
        return response.volts, response.is_ac

    async def get_current(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Tuple[float, bool]:
        if extra is None:
            extra = {}
        request = GetCurrentRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetCurrentResponse = await self.client.GetCurrent(request, timeout=timeout)
        return response.amperes, response.is_ac

    async def get_power(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> float:
        if extra is None:
            extra = {}
        request = GetPowerRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPowerResponse = await self.client.GetPower(request, timeout=timeout)
        return response.watts

    async def get_readings(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Mapping[str, Any]:
        if extra is None:
            extra = {}
        return await super().get_readings(extra=extra, timeout=timeout)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
