from dataclasses import dataclass
from random import random
from typing import Any, Dict, List

from viam.components.arm import Arm
from viam.components.base import Base
from viam.components.imu import (IMU, Acceleration, AngularVelocity,
                                 EulerAngles, Orientation)
from viam.components.motor import Motor
from viam.components.pose_tracker import PoseTracker
from viam.components.sensor import Sensor
from viam.components.servo import Servo
from viam.proto.api.common import Pose, PoseInFrame
from viam.proto.api.component.arm import JointPositions


class MockArm(Arm):

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
        self.joint_positions = JointPositions(degrees=[0, 0, 0, 0, 0, 0])
        super().__init__(name)

    async def get_end_position(self) -> Pose:
        return self.position

    async def move_to_position(self, pose: Pose):
        self.position = pose

    async def get_joint_positions(self) -> JointPositions:
        return self.joint_positions

    async def move_to_joint_positions(self, positions: JointPositions):
        self.joint_positions = positions


class MockBase(Base):

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


class MockIMU(IMU):

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


class MockMotor(Motor):

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

    async def get_features(self) -> Motor.Features:
        return {'position_reporting': True}

    async def is_powered(self) -> bool:
        return self.powered


@dataclass
class MockPose:
    X: float
    Y: float
    Z: float
    o_X: float
    o_Y: float
    o_Z: float
    theta: float

    def to_pose_in_frame(self, frame_name: str):
        pose = Pose(
            x=self.X,
            y=self.Y,
            z=self.Z,
            o_x=self.o_X,
            o_y=self.o_Y,
            o_z=self.o_Z,
            theta=self.theta
        )
        return PoseInFrame(reference_frame=frame_name, pose=pose)


class MockPoseTracker(PoseTracker):

    def __init__(self, name: str, poses: List[MockPose]):
        pose_map: Dict[str, MockPose] = {}
        for idx, pose in enumerate(poses):
            pose_map[str(idx)] = pose
        self.poses_result = pose_map
        self.name = name

    async def get_poses(self, body_names: List[str]) -> Dict[str, PoseInFrame]:
        result: Dict[str, PoseInFrame] = {}
        for name, pose in self.poses_result.items():
            result[name] = pose.to_pose_in_frame(name)
        return result


class MockSensor(Sensor):

    def __init__(self, name: str, result: List[Any] = [
        0, {"foo": "bar"}, [1, 8, 2], "Hello world!"
    ]):
        self.readings = result
        super().__init__(name)

    async def get_readings(self) -> List[Any]:
        return self.readings


class MockServo(Servo):

    def __init__(self, name: str):
        self.angle = 0
        super().__init__(name)

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle
