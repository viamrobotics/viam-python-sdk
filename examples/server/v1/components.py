import asyncio
import random
from viam.components.imu import (
    IMUBase,
    Orientation, AngularVelocity, Acceleration, EulerAngles
)
from viam.components.motor import MotorBase
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


class Motor(MotorBase):

    def __init__(self, name: str):
        self.position: float = 0
        self.power = 0
        self.powered = False
        super().__init__(name)

    def get_seconds(self, rpm: float, revolutions: float) -> int:
        rps = rpm/60
        sec = revolutions/rps
        return int(sec)

    async def run_for(self, sec: int):
        self.powered = True
        await asyncio.sleep(sec)
        self.powered = False

    async def set_power(self, power: float):
        self.power = power
        self.powered = power != 0

    async def go_for(self, rpm: float, revolutions: float):
        if rpm > 0:
            self.position += revolutions
        if rpm < 0:
            self.position -= revolutions
        asyncio.create_task(self.run_for(self.get_seconds(rpm, revolutions)))

    async def go_to(self, rpm: float, position_revolutions: float):
        if rpm != 0:
            self.position = position_revolutions
        distance = position_revolutions - self.position
        distance = abs(distance)
        asyncio.create_task(self.run_for(self.get_seconds(rpm, distance)))

    async def reset_zero_position(self, offset: float):
        if (self.position > 0 and offset > 0) \
                or (self.position < 0 and offset < 0):
            self.position = offset
        else:
            self.position += offset
        self.powered = False

    async def get_position(self) -> float:
        return self.position

    async def get_features(self) -> MotorBase.Features:
        return {'position_reporting': True}

    async def is_powered(self) -> bool:
        return self.powered


class Servo(ServoBase):

    def __init__(self, name: str):
        self.angle = 0
        super().__init__(name)

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle
