from typing import Any, Dict, List, Mapping, Optional, Tuple

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry
from viam.proto.component.motor import (
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    GoForRequest,
    GoToRequest,
    IsMovingRequest,
    IsMovingResponse,
    IsPoweredRequest,
    IsPoweredResponse,
    MotorServiceStub,
    ResetZeroPositionRequest,
    SetPowerRequest,
    SetRPMRequest,
    StopRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from .motor import Motor


class MotorClient(Motor, ReconfigurableResourceRPCClientBase):
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
        **__,
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
        **__,
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
        **__,
    ):
        if extra is None:
            extra = {}
        request = GoToRequest(name=self.name, rpm=rpm, position_revolutions=position_revolutions, extra=dict_to_struct(extra))
        await self.client.GoTo(request, timeout=timeout)

    async def set_rpm(
        self,
        rpm: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ):
        if extra is None:
            extra = {}
        request = SetRPMRequest(name=self.name, rpm=rpm, extra=dict_to_struct(extra))
        await self.client.SetRPM(request, timeout=timeout)

    async def reset_zero_position(
        self,
        offset: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
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
        **__,
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
        **__,
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
        **__,
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
        **__,
    ) -> Tuple[bool, float]:
        if extra is None:
            extra = {}
        request = IsPoweredRequest(name=self.name, extra=dict_to_struct(extra))
        response: IsPoweredResponse = await self.client.IsPowered(request, timeout=timeout)
        return response.is_on, response.power_pct

    async def is_moving(self, *, timeout: Optional[float] = None) -> bool:
        request = IsMovingRequest(name=self.name)
        response: IsMovingResponse = await self.client.IsMoving(request, timeout=timeout)
        return response.is_moving

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **__,
    ) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        return await get_geometries(self.client, self.name, extra, timeout)
