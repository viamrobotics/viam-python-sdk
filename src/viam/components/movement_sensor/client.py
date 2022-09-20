from typing import Any, Dict, Mapping, Tuple

from grpclib.client import Channel

from viam.components.generic.client import do_command
from viam.components.movement_sensor.movement_sensor import MovementSensor
from viam.proto.common import GeoPoint, Orientation, Vector3
from viam.proto.component.movementsensor import (
    GetAccuracyRequest,
    GetAccuracyResponse,
    GetAngularVelocityRequest,
    GetAngularVelocityResponse,
    GetCompassHeadingRequest,
    GetCompassHeadingResponse,
    GetLinearVelocityRequest,
    GetLinearVelocityResponse,
    GetOrientationRequest,
    GetOrientationResponse,
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    MovementSensorServiceStub,
)


class MovementSensorClient(MovementSensor):
    """gRPC client for the MovementSensor component."""

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MovementSensorServiceStub(channel)
        super().__init__(name)

    async def get_position(self) -> Tuple[GeoPoint, float]:
        request = GetPositionRequest(name=self.name)
        response: GetPositionResponse = await self.client.GetPosition(request)
        return response.coordinate, response.altitude_mm

    async def get_linear_velocity(self) -> Vector3:
        request = GetLinearVelocityRequest(name=self.name)
        response: GetLinearVelocityResponse = await self.client.GetLinearVelocity(request)
        return response.linear_velocity

    async def get_angular_velocity(self) -> Vector3:
        request = GetAngularVelocityRequest(name=self.name)
        response: GetAngularVelocityResponse = await self.client.GetAngularVelocity(request)
        return response.angular_velocity

    async def get_compass_heading(self) -> float:
        request = GetCompassHeadingRequest(name=self.name)
        response: GetCompassHeadingResponse = await self.client.GetCompassHeading(request)
        return response.value

    async def get_orientation(self) -> Orientation:
        request = GetOrientationRequest(name=self.name)
        response: GetOrientationResponse = await self.client.GetOrientation(request)
        return response.orientation

    async def get_properties(self) -> MovementSensor.Properties:
        request = GetPropertiesRequest(name=self.name)
        response: GetPropertiesResponse = await self.client.GetProperties(request)
        return response

    async def get_accuracy(self) -> Mapping[str, float]:
        request = GetAccuracyRequest(name=self.name)
        response: GetAccuracyResponse = await self.client.GetAccuracy(request)
        return response.accuracy_mm

    async def get_readings(self) -> Mapping[str, Any]:
        return await super().get_readings()

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
