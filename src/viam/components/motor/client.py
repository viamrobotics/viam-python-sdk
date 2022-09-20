from typing import Any, Dict, Optional

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.component.motor import (
    GetPropertiesRequest,
    GetPropertiesResponse,
    GetPositionRequest,
    GetPositionResponse,
    GoForRequest,
    GoToRequest,
    IsPoweredRequest,
    IsPoweredResponse,
    MotorServiceStub,
    ResetZeroPositionRequest,
    SetPowerRequest,
    StopRequest,
)
from viam.utils import dict_to_struct

from .motor import Motor


class MotorClient(Motor):
    """
    gRPC client for the Motor component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MotorServiceStub(channel)
        super().__init__(name)

    async def set_power(self, power: float, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = SetPowerRequest(name=self.name, power_pct=power, extra=dict_to_struct(extra))
        await self.client.SetPower(request)

    async def go_for(self, rpm: float, revolutions: float, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = GoForRequest(name=self.name, rpm=rpm, revolutions=revolutions, extra=dict_to_struct(extra))
        await self.client.GoFor(request)

    async def go_to(self, rpm: float, position_revolutions: float, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = GoToRequest(name=self.name, rpm=rpm, position_revolutions=position_revolutions, extra=dict_to_struct(extra))
        await self.client.GoTo(request)

    async def reset_zero_position(self, offset: float, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = ResetZeroPositionRequest(name=self.name, offset=offset, extra=dict_to_struct(extra))
        await self.client.ResetZeroPosition(request)

    async def get_position(self, extra: Optional[Dict[str, Any]] = None) -> float:
        if extra is None:
            extra = {}
        request = GetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request)
        return response.position

    async def get_properties(self, extra: Optional[Dict[str, Any]] = None) -> Motor.Properties:
        if extra is None:
            extra = {}
        request = GetPropertiesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPropertiesResponse = await self.client.GetProperties(request)
        return Motor.Properties(position_reporting=response.position_reporting)

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request)

    async def is_powered(self, extra: Optional[Dict[str, Any]] = None) -> bool:
        if extra is None:
            extra = {}
        request = IsPoweredRequest(name=self.name, extra=dict_to_struct(extra))
        response: IsPoweredResponse = await self.client.IsPowered(request)
        return response.is_on

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
