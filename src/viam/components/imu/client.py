from typing import Any, Dict

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.api.component.imu import (IMUServiceStub,
                                          ReadAccelerationRequest,
                                          ReadAccelerationResponse,
                                          ReadAngularVelocityRequest,
                                          ReadAngularVelocityResponse,
                                          ReadMagnetometerRequest,
                                          ReadMagnetometerResponse,
                                          ReadOrientationRequest,
                                          ReadOrientationResponse)

from .imu import IMU, Acceleration, AngularVelocity, Magnetometer, Orientation


class IMUClient(IMU):
    """
    gRPC client for the IMU component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = IMUServiceStub(channel)
        super().__init__(name)

    async def read_acceleration(self) -> Acceleration:
        request = ReadAccelerationRequest(name=self.name)
        response: ReadAccelerationResponse = \
            await self.client.ReadAcceleration(request)
        return response.acceleration

    async def read_angular_velocity(self) -> AngularVelocity:
        request = ReadAngularVelocityRequest(name=self.name)
        response: ReadAngularVelocityResponse = \
            await self.client.ReadAngularVelocity(request)
        return response.angular_velocity

    async def read_orientation(self) -> Orientation:
        request = ReadOrientationRequest(name=self.name)
        response: ReadOrientationResponse = \
            await self.client.ReadOrientation(request)
        return Orientation(euler_angles=response.orientation)

    async def read_magnetometer(self) -> Magnetometer:
        request = ReadMagnetometerRequest(name=self.name)
        response: ReadMagnetometerResponse = \
            await self.client.ReadMagnetometer(request)
        return response.magnetometer

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
