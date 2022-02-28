from dataclasses import dataclass
from random import random

from viam.components.imu import (
    IMUBase,
    Orientation, AngularVelocity, Acceleration, EulerAngles
)
from viam.components.servo import ServoBase


class MockIMU(IMUBase):

    @dataclass
    class Result:
        acceleration: Acceleration
        angular_velocity: AngularVelocity
        orentation: Orientation

    def __init__(self, name: str, result: Result = Result(
        Acceleration(
            x_mm_per_sec_per_sec=random(),
            y_mm_per_sec_per_sec=random(),
            z_mm_per_sec_per_sec=random()
        ),
        AngularVelocity(
            x_degs_per_sec=random(),
            y_degs_per_sec=random(),
            z_degs_per_sec=random()
        ),
        Orientation(
            euler_angles=EulerAngles(
                roll_deg=random(),
                pitch_deg=random(),
                yaw_deg=random()
            )
        )
    )):
        self.acceleration = result.acceleration
        self.angular_velocity = result.angular_velocity
        self.orientation = result.orentation
        super().__init__(name)

    async def read_acceleration(self) -> Acceleration:
        return self.acceleration

    async def read_angular_velocity(self) -> AngularVelocity:
        return self.angular_velocity

    async def read_orientation(self) -> Orientation:
        return self.orientation


class MockServo(ServoBase):

    angle: int = 0

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle
