from grpclib.testing import ChannelFor
import pytest

from viam.components.imu import (
    IMUBase,
    Orientation, AngularVelocity, Acceleration, EulerAngles
)
from viam.components.imu.service import IMUService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.component.imu import (
    IMUServiceStub,
    ReadAccelerationRequest, ReadAccelerationResponse,
    ReadAngularVelocityRequest, ReadAngularVelocityResponse,
    ReadOrientationRequest, ReadOrientationResponse
)


class MockIMU(IMUBase):

    async def read_acceleration(self) -> Acceleration:
        return Acceleration(
            x_mm_per_sec_per_sec=1,
            y_mm_per_sec_per_sec=2,
            z_mm_per_sec_per_sec=3
        )

    async def read_angular_velocity(self) -> AngularVelocity:
        return AngularVelocity(
            x_degs_per_sec=1,
            y_degs_per_sec=2,
            z_degs_per_sec=3
        )

    async def read_orientation(self) -> Orientation:
        angles = EulerAngles(
            roll_deg=1,
            pitch_deg=2,
            yaw_deg=3
        )
        return Orientation(euler_angles=angles)


class TestIMU:

    imu = MockIMU(name='imu')

    @pytest.mark.asyncio
    async def test_read_acceleration(self):
        acceleration = await self.imu.read_acceleration()
        assert acceleration == Acceleration(
            x_mm_per_sec_per_sec=1,
            y_mm_per_sec_per_sec=2,
            z_mm_per_sec_per_sec=3
        )

    @pytest.mark.asyncio
    async def test_read_angular_velocity(self):
        angular_velocity = await self.imu.read_angular_velocity()
        assert angular_velocity == AngularVelocity(
            x_degs_per_sec=1,
            y_degs_per_sec=2,
            z_degs_per_sec=3
        )

    @pytest.mark.asyncio
    async def test_read_orientation(self):
        angles = EulerAngles(
            roll_deg=1,
            pitch_deg=2,
            yaw_deg=3
        )
        orientation = await self.imu.read_orientation()
        assert orientation == Orientation(euler_angles=angles)


class TestService:

    name = 'imu'
    imu = MockIMU(name=name)
    manager = ResourceManager([imu])
    service = IMUService(manager)

    @pytest.mark.asyncio
    async def test_read_acceleration(self):
        async with ChannelFor([self.service]) as channel:
            client = IMUServiceStub(channel)
            request = ReadAccelerationRequest(name=self.name)
            response: ReadAccelerationResponse = \
                await client.ReadAcceleration(request)
            assert response.acceleration == Acceleration(
                x_mm_per_sec_per_sec=1,
                y_mm_per_sec_per_sec=2,
                z_mm_per_sec_per_sec=3
            )

    @pytest.mark.asyncio
    async def test_read_angular_velocity(self):
        async with ChannelFor([self.service]) as channel:
            client = IMUServiceStub(channel)
            request = ReadAngularVelocityRequest(name=self.name)
            response: ReadAngularVelocityResponse = \
                await client.ReadAngularVelocity(request)
            assert response.angular_velocity == AngularVelocity(
                x_degs_per_sec=1,
                y_degs_per_sec=2,
                z_degs_per_sec=3
            )

    @pytest.mark.asyncio
    async def test_read_orientation(self):
        async with ChannelFor([self.service]) as channel:
            client = IMUServiceStub(channel)
            request = ReadOrientationRequest(name=self.name)
            response: ReadOrientationResponse = \
                await client.ReadOrientation(request)
            assert response.orientation == EulerAngles(
                roll_deg=1,
                pitch_deg=2,
                yaw_deg=3
            )
