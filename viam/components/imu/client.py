from grpclib.client import Channel
from viam.proto.api.component.imu import (IMUServiceStub,
                                          ReadAccelerationRequest,
                                          ReadAccelerationResponse,
                                          ReadAngularVelocityRequest,
                                          ReadAngularVelocityResponse,
                                          ReadOrientationRequest,
                                          ReadOrientationResponse)

from .imu import Acceleration, AngularVelocity, IMUBase, Orientation


class IMUClient(IMUBase):
    """
    gRPC client for the IMU component.
    """

    def __init__(self, name: str, channel: Channel):
        self.name = name
        self.client = IMUServiceStub(channel)

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
