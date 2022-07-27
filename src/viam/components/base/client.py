from typing import Any, Dict, Optional

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.api.common import Vector3
from viam.proto.api.component.base import (BaseServiceStub,
                                           MoveStraightRequest,
                                           SetPowerRequest, SetVelocityRequest,
                                           SpinRequest, StopRequest)

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
        extra: Optional[Dict[str, Any]] = None
    ):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = MoveStraightRequest(
            name=self.name,
            distance_mm=distance,
            mm_per_sec=velocity,
            extra=struct,
        )
        await self.client.MoveStraight(request)

    async def spin(self, angle: float, velocity: float, extra: Optional[Dict[str, Any]] = None):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = SpinRequest(
            name=self.name,
            angle_deg=angle,
            degs_per_sec=velocity,
            extra=struct,
        )
        await self.client.Spin(request)

    async def set_power(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = SetPowerRequest(
            name=self.name,
            linear=linear,
            angular=angular,
            extra=struct,
        )
        await self.client.SetPower(request)

    async def set_velocity(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = SetVelocityRequest(name=self.name, linear=linear, angular=angular, extra=struct)
        await self.client.SetVelocity(request)

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = StopRequest(name=self.name, extra=struct)
        await self.client.Stop(request)

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
