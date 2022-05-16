from typing import Any, Dict

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.api.common import Vector3
from viam.proto.api.component.base import (BaseServiceStub, MoveArcRequest,
                                           MoveStraightRequest,
                                           SetPowerRequest, SpinRequest,
                                           StopRequest)

from .base import Base


class BaseClient(Base):
    """
    gRPC client for the Base component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = BaseServiceStub(channel)
        super().__init__(name)

    async def move_straight(
        self,
        distance: int,
        velocity: float,
    ):
        request = MoveStraightRequest(
            name=self.name,
            distance_mm=distance,
            mm_per_sec=velocity,
        )
        await self.client.MoveStraight(request)

    async def move_arc(
        self,
        distance: int,
        velocity: float,
        angle: float,
    ):
        request = MoveArcRequest(
            name=self.name,
            distance_mm=distance,
            mm_per_sec=velocity,
            angle_deg=angle,
        )
        await self.client.MoveArc(request)

    async def spin(self, angle: float, velocity: float):
        request = SpinRequest(
            name=self.name,
            angle_deg=angle,
            degs_per_sec=velocity,
        )
        await self.client.Spin(request)

    async def set_power(self, linear: Vector3, angular: Vector3):
        request = SetPowerRequest(
            name=self.name,
            linear=linear,
            angular=angular
        )
        await self.client.SetPower(request)

    async def stop(self):
        request = StopRequest(name=self.name)
        await self.client.Stop(request)

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
