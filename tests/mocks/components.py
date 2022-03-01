from dataclasses import dataclass
from random import random

from viam.components.imu import (
    IMUBase,
    Orientation, AngularVelocity, Acceleration, EulerAngles
)
from viam.components.motor import MotorBase
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


class MockMotor(MotorBase):

    def __init__(self, name: str):
        self.position: float = 0
        self.power = 0
        self.powered = False
        super().__init__(name)

    async def set_power(self, power: float):
        self.power = power
        self.powered = power != 0

    async def go_for(self, rpm: float, revolutions: float):
        if rpm > 0:
            self.position += revolutions
        if rpm < 0:
            self.position -= revolutions
        self.powered = False

    async def go_to(self, rpm: float, position_revolutions: float):
        if rpm != 0:
            self.position = position_revolutions
        self.powered = False

    async def reset_zero_position(self, offset: float):
        self.offset = offset
        self.powered = False

    async def get_position(self) -> float:
        return self.position

    async def get_features(self) -> MotorBase.Features:
        return {'position_reporting': True}

    async def is_powered(self) -> bool:
        return self.powered


class MockServo(ServoBase):

    def __init__(self, name: str):
        self.angle = 0
        super().__init__(name)

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle
