import pytest
from grpclib.testing import ChannelFor
from viam.components.generic.service import GenericService
from viam.components.imu import (Acceleration, AngularVelocity, EulerAngles,
                                 IMUClient, Magnetometer, Orientation)
from viam.components.imu.service import IMUService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.component.imu import (IMUServiceStub,
                                          ReadAccelerationRequest,
                                          ReadAccelerationResponse,
                                          ReadAngularVelocityRequest,
                                          ReadAngularVelocityResponse,
                                          ReadMagnetometerRequest,
                                          ReadMagnetometerResponse,
                                          ReadOrientationRequest,
                                          ReadOrientationResponse)

from .mocks.components import MockIMU

PASS_RESULT = MockIMU.Result(
    Acceleration(
        x_mm_per_sec_per_sec=1,
        y_mm_per_sec_per_sec=2,
        z_mm_per_sec_per_sec=3
    ),
    AngularVelocity(
        x_degs_per_sec=1,
        y_degs_per_sec=2,
        z_degs_per_sec=3
    ),
    Orientation(
        euler_angles=EulerAngles(
            roll_deg=1,
            pitch_deg=2,
            yaw_deg=3
        )
    ),
    Magnetometer(
        x_gauss=1,
        y_gauss=2,
        z_gauss=3
    )
)


class TestIMU:

    imu = MockIMU(name='imu', result=PASS_RESULT)

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

    @pytest.mark.asyncio
    async def test_read_magnetometer(self):
        magnetometer = await self.imu.read_magnetometer()
        assert magnetometer == Magnetometer(
            x_gauss=1,
            y_gauss=2,
            z_gauss=3
        )

    @pytest.mark.asyncio
    async def test_do(self):
        with pytest.raises(NotImplementedError):
            await self.imu.do({'command': 'args'})


class TestService:

    name = 'imu'
    imu = MockIMU(name=name, result=PASS_RESULT)
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

    @pytest.mark.asyncio
    async def test_read_magnetometer(self):
        async with ChannelFor([self.service]) as channel:
            client = IMUServiceStub(channel)
            request = ReadMagnetometerRequest(name=self.name)
            response: ReadMagnetometerResponse = \
                await client.ReadMagnetometer(request)
            assert response.magnetometer == Magnetometer(
                x_gauss=1,
                y_gauss=2,
                z_gauss=3
            )


class TestClient:

    name = 'imu'
    imu = MockIMU(name=name, result=PASS_RESULT)
    manager = ResourceManager([imu])
    service = IMUService(manager)

    @pytest.mark.asyncio
    async def test_read_acceleration(self):
        async with ChannelFor([self.service]) as channel:
            client = IMUClient(self.imu.name, channel)
            acceleration = await client.read_acceleration()
            assert acceleration == Acceleration(
                x_mm_per_sec_per_sec=1,
                y_mm_per_sec_per_sec=2,
                z_mm_per_sec_per_sec=3
            )

    @pytest.mark.asyncio
    async def test_read_angular_velocity(self):
        async with ChannelFor([self.service]) as channel:
            client = IMUClient(self.imu.name, channel)
            av = await client.read_angular_velocity()
            assert av == AngularVelocity(
                x_degs_per_sec=1,
                y_degs_per_sec=2,
                z_degs_per_sec=3
            )

    @pytest.mark.asyncio
    async def test_read_orientation(self):
        async with ChannelFor([self.service]) as channel:
            client = IMUClient(self.imu.name, channel)
            orientation = await client.read_orientation()
            assert orientation == Orientation(
                euler_angles=EulerAngles(
                    roll_deg=1,
                    pitch_deg=2,
                    yaw_deg=3
                )
            )

    @pytest.mark.asyncio
    async def test_read_magnetometer(self):
        async with ChannelFor([self.service]) as channel:
            client = IMUClient(self.imu.name, channel)
            magnetometer = await client.read_magnetometer()
            assert magnetometer == Magnetometer(
                x_gauss=1,
                y_gauss=2,
                z_gauss=3
            )

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service, GenericService(self.manager)]) as channel:
            client = IMUClient(self.imu.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do({'command': 'args'})
