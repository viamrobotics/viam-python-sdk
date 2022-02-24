import random
from viam.components.imu import (
    IMUBase,
    Orientation, AngularVelocity, Acceleration, EulerAngles
)
from viam.components.servo import ServoBase


class IMU(IMUBase):

    async def read_acceleration(self) -> Acceleration:
        return Acceleration(
            x_mm_per_sec_per_sec=random.random(),
            y_mm_per_sec_per_sec=random.random(),
            z_mm_per_sec_per_sec=random.random()
        )

    async def read_angular_velocity(self) -> AngularVelocity:
        return AngularVelocity(
            x_degs_per_sec=random.random(),
            y_degs_per_sec=random.random(),
            z_degs_per_sec=random.random()
        )

    async def read_orientation(self) -> Orientation:
        angles = EulerAngles(
            roll_deg=random.random(),
            pitch_deg=random.random(),
            yaw_deg=random.random()
        )
        return Orientation(euler_angles=angles)


class Servo(ServoBase):

    angle: int = 0

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle
