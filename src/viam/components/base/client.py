from typing import Any, Dict, Optional

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.common import Vector3
from viam.proto.component.base import (
    BaseServiceStub,
    MoveStraightRequest,
    SetPowerRequest,
    SetVelocityRequest,
    SpinRequest,
    StopRequest,
)
from viam.utils import dict_to_struct

from .base import Base


class BaseClient(Base):
    """
    gRPC client for the Base component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = BaseServiceStub(channel)
        super().__init__(name)

    async def move_straight(self, distance: int, velocity: float, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = MoveStraightRequest(
            name=self.name,
            distance_mm=distance,
            mm_per_sec=velocity,
            extra=dict_to_struct(extra),
        )
        await self.client.MoveStraight(request)

    async def spin(self, angle: float, velocity: float, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = SpinRequest(
            name=self.name,
            angle_deg=angle,
            degs_per_sec=velocity,
            extra=dict_to_struct(extra),
        )
        await self.client.Spin(request)

    async def set_power(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = SetPowerRequest(
            name=self.name,
            linear=linear,
            angular=angular,
            extra=dict_to_struct(extra),
        )
        await self.client.SetPower(request)

    async def set_velocity(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = SetVelocityRequest(name=self.name, linear=linear, angular=angular, extra=dict_to_struct(extra))
        await self.client.SetVelocity(request)

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
