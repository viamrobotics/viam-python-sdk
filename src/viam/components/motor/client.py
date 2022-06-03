from typing import Any, Dict

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.api.component.motor import (GetFeaturesRequest,
                                            GetFeaturesResponse,
                                            GetPositionRequest,
                                            GetPositionResponse, GoForRequest,
                                            GoToRequest, IsPoweredRequest,
                                            IsPoweredResponse,
                                            MotorServiceStub,
                                            ResetZeroPositionRequest,
                                            SetPowerRequest, StopRequest)

from .motor import Motor


class MotorClient(Motor):
    """
    gRPC client for the Motor component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MotorServiceStub(channel)
        super().__init__(name)

    async def set_power(self, power: float):
        request = SetPowerRequest(name=self.name, power_pct=power)
        await self.client.SetPower(request)

    async def go_for(self, rpm: float, revolutions: float):
        request = GoForRequest(name=self.name, rpm=rpm,
                               revolutions=revolutions)
        await self.client.GoFor(request)

    async def go_to(self, rpm: float, position_revolutions: float):
        request = GoToRequest(name=self.name, rpm=rpm,
                              position_revolutions=position_revolutions)
        await self.client.GoTo(request)

    async def reset_zero_position(self, offset: float):
        request = ResetZeroPositionRequest(name=self.name, offset=offset)
        await self.client.ResetZeroPosition(request)

    async def get_position(self) -> float:
        request = GetPositionRequest(name=self.name)
        response: GetPositionResponse = await self.client.GetPosition(request)
        return response.position

    async def get_features(self) -> Motor.Features:
        request = GetFeaturesRequest(name=self.name)
        response: GetFeaturesResponse = await self.client.GetFeatures(request)
        return Motor.Features(position_reporting=response.position_reporting)

    async def stop(self):
        request = StopRequest(name=self.name)
        await self.client.Stop(request)

    async def is_powered(self) -> bool:
        request = IsPoweredRequest(name=self.name)
        response: IsPoweredResponse = await self.client.IsPowered(request)
        return response.is_on

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
