from typing import Any, Dict, Optional, Tuple

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

    async def set_power(
        self,
        power: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = SetPowerRequest(name=self.name, power_pct=power, extra=dict_to_struct(extra))
        await self.client.SetPower(request, timeout=timeout)

    async def go_for(
        self,
        rpm: float,
        revolutions: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = GoForRequest(name=self.name, rpm=rpm, revolutions=revolutions, extra=dict_to_struct(extra))
        await self.client.GoFor(request, timeout=timeout)

    async def go_to(
        self,
        rpm: float,
        position_revolutions: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = GoToRequest(name=self.name, rpm=rpm, position_revolutions=position_revolutions, extra=dict_to_struct(extra))
        await self.client.GoTo(request, timeout=timeout)

    async def reset_zero_position(
        self,
        offset: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = ResetZeroPositionRequest(name=self.name, offset=offset, extra=dict_to_struct(extra))
        await self.client.ResetZeroPosition(request, timeout=timeout)

    async def get_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> float:
        if extra is None:
            extra = {}
        request = GetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout)
        return response.position

    async def get_properties(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Motor.Properties:
        if extra is None:
            extra = {}
        request = GetPropertiesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPropertiesResponse = await self.client.GetProperties(request, timeout=timeout)
        return Motor.Properties(position_reporting=response.position_reporting)

    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request, timeout=timeout)

    async def is_powered(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Tuple[bool, float]:
        if extra is None:
            extra = {}
        request = IsPoweredRequest(name=self.name, extra=dict_to_struct(extra))
        response: IsPoweredResponse = await self.client.IsPowered(request, timeout=timeout)
        return response.is_on, response.power_pct

    async def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command, timeout=timeout)
