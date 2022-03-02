import asyncio
import random
from typing import Any, List
from viam.components.base import BaseBase
from viam.components.imu import (
    IMUBase,
    Orientation, AngularVelocity, Acceleration, EulerAngles
)
from viam.components.motor import MotorBase
from viam.components.sensor import SensorBase
from viam.components.servo import ServoBase


class Base(BaseBase):

    def __init__(self, name: str):
        self.position = 0
        self.angle = 0
        self.stopped = True
        super().__init__(name)

    async def move_straight(
        self,
        distance: int,
        velocity: float,
        blocking: bool
    ):
        if distance == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
        else:
            self.position -= distance

        self.stopped = False

    async def move_arc(
        self,
        distance: int,
        velocity: float,
        angle: float,
        blocking: bool
    ):
        if distance == 0:
            return await self.spin(angle, velocity, blocking)

        if velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
            self.angle += angle
        else:
            self.position -= distance
            self.angle -= angle

        self.stopped = False

    async def spin(self, angle: float, velocity: float, blocking: bool):
        if angle == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.angle += angle
        else:
            self.angle -= angle

        self.stopped = False

    async def stop(self):
        self.stopped = True


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
        self.task = None
        super().__init__(name)

    async def run_continuously(self, rpm: float):
        rps = rpm/60
        while True:
            await asyncio.sleep(1)
            self.position += rps

    async def set_power(self, power: float):
        self.power = power
        self.powered = power != 0
        if self.powered:
            self.task = asyncio.create_task(self.run_continuously(power))
        else:
            if self.task:
                self.task.cancel()

    async def go_for(self, rpm: float, revolutions: float):
        if self.task:
            self.task.cancel()
        target = 0
        rps = rpm/60
        if rpm > 0:
            target = self.position + revolutions
        if rpm < 0:
            target = self.position - revolutions
        self.powered = True
        while abs(self.position-target) > 0.01:
            await asyncio.sleep(1)
            self.position += rps
        self.powered = False

    async def go_to(self, rpm: float, position_revolutions: float):
        if self.task:
            self.task.cancel()
        distance = position_revolutions - self.position
        rps = rpm/60
        self.powered = True
        while distance > 0:
            await asyncio.sleep(1)
            distance -= abs(rps)
            self.position += rps
        self.powered = False

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


class Sensor(SensorBase):

    def __init__(self, name: str):
        self.num_readings = random.randint(1, 10)
        super().__init__(name)

    async def get_readings(self) -> List[Any]:
        return [random.random() for _ in range(self.num_readings)]


class Servo(ServoBase):

    def __init__(self, name: str):
        self.angle = 0
        super().__init__(name)

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle
