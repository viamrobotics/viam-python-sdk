from typing import Any, Dict, Mapping, Optional, Tuple

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
from viam.utils import dict_to_struct


class MovementSensorClient(MovementSensor):
    """gRPC client for the MovementSensor component."""

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MovementSensorServiceStub(channel)
        super().__init__(name)

    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Tuple[GeoPoint, float]:
        if extra is None:
            extra = {}
        request = GetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout)
        return response.coordinate, response.altitude_mm

    async def get_linear_velocity(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Vector3:
        if extra is None:
            extra = {}
        request = GetLinearVelocityRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetLinearVelocityResponse = await self.client.GetLinearVelocity(request, timeout=timeout)
        return response.linear_velocity

    async def get_angular_velocity(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Vector3:
        if extra is None:
            extra = {}
        request = GetAngularVelocityRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetAngularVelocityResponse = await self.client.GetAngularVelocity(request, timeout=timeout)
        return response.angular_velocity

    async def get_compass_heading(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> float:
        if extra is None:
            extra = {}
        request = GetCompassHeadingRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetCompassHeadingResponse = await self.client.GetCompassHeading(request, timeout=timeout)
        return response.value

    async def get_orientation(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Orientation:
        if extra is None:
            extra = {}
        request = GetOrientationRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetOrientationResponse = await self.client.GetOrientation(request, timeout=timeout)
        return response.orientation

    async def get_properties(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> MovementSensor.Properties:
        if extra is None:
            extra = {}
        request = GetPropertiesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPropertiesResponse = await self.client.GetProperties(request, timeout=timeout)
        return response

    async def get_accuracy(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Mapping[str, float]:
        if extra is None:
            extra = {}
        request = GetAccuracyRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetAccuracyResponse = await self.client.GetAccuracy(request, timeout=timeout)
        return response.accuracy_mm

    async def get_readings(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> Mapping[str, Any]:
        if extra is None:
            extra = {}
        return await super().get_readings(extra=extra, timeout=timeout)

    async def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command, timeout=timeout)
