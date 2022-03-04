import asyncio
import random
from typing import Any, Dict, List
from viam.components.arm import Arm
from viam.components.base import Base
from viam.components.imu import (
    IMU,
    Orientation, AngularVelocity, Acceleration, EulerAngles
)
from viam.components.motor import Motor
from viam.components.pose_tracker import PoseTracker
from viam.components.sensor import Sensor
from viam.components.servo import Servo
from viam.proto.api.component.arm import ArmJointPositions
from viam.proto.api.common import Pose, PoseInFrame


class ExampleArm(Arm):

    def __init__(self, name: str):
        self.position = Pose(
            x=1,
            y=2,
            z=3,
            o_x=2,
            o_y=3,
            o_z=4,
            theta=20,
        )
        self.joint_positions = ArmJointPositions(degrees=[0, 0, 0, 0, 0, 0])
        super().__init__(name)

    async def get_end_position(self) -> Pose:
        return self.position

    async def move_to_position(self, pose: Pose):
        self.position = pose

    async def get_joint_positions(self) -> ArmJointPositions:
        return self.joint_positions

    async def move_to_joint_positions(self, positions: ArmJointPositions):
        self.joint_positions = positions


class ExampleBase(Base):

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


class ExampleIMU(IMU):

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


class ExampleMotor(Motor):

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

    async def get_features(self) -> Motor.Features:
        return {'position_reporting': True}

    async def is_powered(self) -> bool:
        return self.powered


class ExamplePoseTracker(PoseTracker):

    async def get_poses(self, body_names: List[str]) -> Dict[str, PoseInFrame]:
        all_poses = {
            "body1": PoseInFrame(
                reference_frame='0',
                pose=Pose(
                    x=1,
                    y=2,
                    z=3,
                    o_x=2,
                    o_y=3,
                    o_z=4,
                    theta=20
                )
            ),
            "body2": PoseInFrame(
                reference_frame='0',
                pose=Pose(
                    x=3,
                    y=2,
                    z=3,
                    o_x=4,
                    o_y=3,
                    o_z=4,
                    theta=40
                )
            )
        }
        return {k: v for k, v in all_poses.items() if k in body_names}


class ExampleSensor(Sensor):

    def __init__(self, name: str):
        self.num_readings = random.randint(1, 10)
        super().__init__(name)

    async def get_readings(self) -> List[Any]:
        return [random.random() for _ in range(self.num_readings)]


class ExampleServo(Servo):

    def __init__(self, name: str):
        self.angle = 0
        super().__init__(name)

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle
