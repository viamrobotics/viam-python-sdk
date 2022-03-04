from grpclib.client import Channel
from viam.proto.api.component.base import (BaseServiceStub, MoveArcRequest,
                                           MoveStraightRequest, SpinRequest,
                                           StopRequest)

from .base import Base


class BaseClient(Base):
    """
    gRPC client for the Base component.
    """

    def __init__(self, name: str, channel: Channel):
        self.client = BaseServiceStub(channel)
        super().__init__(name)

    async def move_straight(
        self,
        distance: int,
        velocity: float,
        blocking: bool
    ):
        request = MoveStraightRequest(
            name=self.name,
            distance_mm=distance,
            mm_per_sec=velocity,
            block=blocking
        )
        await self.client.MoveStraight(request)

    async def move_arc(
        self,
        distance: int,
        velocity: float,
        angle: float,
        blocking: bool
    ):
        request = MoveArcRequest(
            name=self.name,
            distance_mm=distance,
            mm_per_sec=velocity,
            angle_deg=angle,
            block=blocking
        )
        await self.client.MoveArc(request)

    async def spin(self, angle: float, velocity: float, blocking: bool):
        request = SpinRequest(
            name=self.name,
            angle_deg=angle,
            degs_per_sec=velocity,
            block=blocking
        )
        await self.client.Spin(request)

    async def stop(self):
        request = StopRequest(name=self.name)
        await self.client.Stop(request)
