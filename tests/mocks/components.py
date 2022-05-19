from dataclasses import dataclass
from multiprocessing import Queue
from random import random
from secrets import choice
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image
from viam.components.arm import Arm, JointPositions
from viam.components.base import Base
from viam.components.board import Board
from viam.components.board.board import PostProcessor
from viam.components.camera import Camera
from viam.components.gantry import Gantry
from viam.components.generic import Generic as GenericComponent
from viam.components.gps import GPS
from viam.components.gripper import Gripper
from viam.components.imu import (IMU, Acceleration, AngularVelocity,
                                 EulerAngles, Magnetometer, Orientation)
from viam.components.input import (Control, ControlFunction, Controller, Event,
                                   EventType)
from viam.components.motor import Motor
from viam.components.pose_tracker import PoseTracker
from viam.components.sensor import Sensor
from viam.components.servo import Servo
from viam.components.types import CameraMimeType
from viam.errors import ComponentNotFoundError
from viam.proto.api.common import (AnalogStatus, BoardStatus,
                                   DigitalInterruptStatus, Pose, PoseInFrame,
                                   Vector3, WorldState)


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

    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None
    ):
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
        self.linear = Vector3(x=0, y=0, z=0)
        self.angular = Vector3(x=0, y=0, z=0)
        super().__init__(name)

    async def move_straight(
        self,
        distance: int,
        velocity: float,
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
    ):
        if distance == 0:
            return await self.spin(angle, velocity)

        if velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
            self.angle += angle
        else:
            self.position -= distance
            self.angle -= angle

        self.stopped = False

    async def spin(self, angle: float, velocity: float, ):
        if angle == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.angle += angle
        else:
            self.angle -= angle

        self.stopped = False

    async def set_power(self, linear: Vector3, angular: Vector3):
        self.linear = linear
        self.angular = angular

    async def stop(self):
        self.stopped = True


class MockAnalogReader(Board.AnalogReader):

    def __init__(self, name: str, value: int):
        self.value = value
        super().__init__(name)

    async def read(self) -> int:
        return self.value


class MockDigitalInterrupt(Board.DigitalInterrupt):

    def __init__(self, name: str):
        self.high = False
        self.last_tick = 0
        self.num_ticks = 0
        self.callbacks: List[Queue] = []
        self.post_processors: List[PostProcessor] = []
        super().__init__(name)

    async def value(self) -> int:
        return self.num_ticks

    async def tick(self, high: bool, nanos: int):
        self.high = high
        self.last_tick = nanos
        self.num_ticks += 1

    async def add_callback(self, queue: Queue):
        self.callbacks.append(queue)

    async def add_post_processor(self, processor: PostProcessor):
        self.post_processors.append(processor)


class MockGPIOPin(Board.GPIOPin):

    def __init__(self, name: str):
        self.high = False
        self.pwm = 0.0
        self.pwm_freq = 0
        super().__init__(name)

    async def get(self) -> bool:
        return self.high

    async def set(self, high: bool):
        self.high = high

    async def get_pwm(self) -> float:
        return self.pwm

    async def set_pwm(self, duty_cycle: float):
        self.pwm = duty_cycle

    async def get_pwm_frequency(self) -> int:
        return self.pwm_freq

    async def set_pwm_frequency(self, frequency: int):
        self.pwm_freq = frequency


class MockBoard(Board):

    def __init__(self,
                 name: str,
                 analog_readers: Dict[str, Board.AnalogReader],
                 digital_interrupts: Dict[str, Board.DigitalInterrupt],
                 gpio_pins: Dict[str, Board.GPIOPin]
                 ):
        self.analog_readers = analog_readers
        self.digital_interrupts = digital_interrupts
        self.gpios = gpio_pins
        super().__init__(name)

    async def analog_reader_by_name(self, name: str) -> Board.AnalogReader:
        try:
            return self.analog_readers[name]
        except KeyError:
            raise ComponentNotFoundError('Board.AnalogReader', name)

    async def digital_interrupt_by_name(
        self,
        name: str
    ) -> Board.DigitalInterrupt:
        try:
            return self.digital_interrupts[name]
        except KeyError:
            raise ComponentNotFoundError('Board.DigitalInterrupt', name)

    async def gpio_pin_by_name(self, name: str) -> Board.GPIOPin:
        try:
            return self.gpios[name]
        except KeyError:
            raise ComponentNotFoundError('Board.GPIOPin', name)

    async def analog_reader_names(self) -> List[str]:
        return [key for key in self.analog_readers.keys()]

    async def digital_interrupt_names(self) -> List[str]:
        return [key for key in self.digital_interrupts.keys()]

    async def status(self) -> BoardStatus:
        return BoardStatus(
            analogs={
                name: AnalogStatus(value=await analog.read())
                for (name, analog) in self.analog_readers.items()
            },
            digital_interrupts={
                name: DigitalInterruptStatus(value=await di.value())
                for (name, di) in self.digital_interrupts.items()
            }
        )

    async def model_attributes(self) -> Board.Attributes:
        return Board.Attributes(remote=True)


class MockCamera(Camera):

    def __init__(self, name: str):
        self.image = Image.new('RGBA', (100, 100), '#AABBCCDD')
        self.point_cloud = b'THIS IS A POINT CLOUD'
        super().__init__(name)

    async def get_frame(self) -> Image.Image:
        return self.image

    async def get_point_cloud(self) -> Tuple[bytes, str]:
        return self.point_cloud, CameraMimeType.PCD.value


class MockGantry(Gantry):

    def __init__(
        self,
        name: str,
        position: List[float],
        lengths: List[float]
    ):
        self.position = position
        self.lengths = lengths
        super().__init__(name)

    async def get_position(self) -> List[float]:
        return self.position

    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None
    ):
        self.position = positions

    async def get_lengths(self) -> List[float]:
        return self.lengths


class MockGeneric(GenericComponent):

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return {key: True for key in command.keys()}


class MockGPS(GPS):

    def __init__(
        self,
        name: str,
        location: GPS.Point,
        altitude: float,
        speed: float
    ):
        self.location = location
        self.altitude = altitude
        self.speed = speed
        super().__init__(name)

    async def read_location(self) -> GPS.Point:
        return self.location

    async def read_altitude(self) -> float:
        return self.altitude

    async def read_speed(self) -> float:
        return self.speed


class MockGripper(Gripper):

    def __init__(self, name: str):
        self.opened = False
        super().__init__(name)

    async def open(self):
        self.opened = True

    async def grab(self) -> bool:
        self.opened = False
        return choice([True, False])


class MockIMU(IMU):

    @dataclass
    class Result:
        acceleration: Acceleration
        angular_velocity: AngularVelocity
        orentation: Orientation
        magnetometer: Magnetometer

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
        ),
        Magnetometer(
            x_gauss=random(),
            y_gauss=random(),
            z_gauss=random()
        )
    )):
        self.acceleration = result.acceleration
        self.angular_velocity = result.angular_velocity
        self.orientation = result.orentation
        self.magnetometer = result.magnetometer
        super().__init__(name)

    async def read_acceleration(self) -> Acceleration:
        return self.acceleration

    async def read_angular_velocity(self) -> AngularVelocity:
        return self.angular_velocity

    async def read_orientation(self) -> Orientation:
        return self.orientation

    async def read_magnetometer(self) -> Magnetometer:
        return self.magnetometer


class MockInputController(Controller):

    def __init__(self, name: str):
        super().__init__(name)
        self.events: Dict[Control, Event] = {}
        self.callbacks: Dict[Control, Dict[EventType, Optional[ControlFunction]]] = {}

    async def get_controls(self) -> List[Control]:
        return [
            Control.ABSOLUTE_X,
            Control.ABSOLUTE_Y,
            Control.ABSOLUTE_Z,
            Control.ABSOLUTE_RX,
            Control.ABSOLUTE_RY,
            Control.ABSOLUTE_RZ,
            Control.ABSOLUTE_HAT0_X,
            Control.ABSOLUTE_HAT0_Y,
            Control.BUTTON_SOUTH,
            Control.BUTTON_EAST,
            Control.BUTTON_WEST,
            Control.BUTTON_NORTH,
            Control.BUTTON_LT,
            Control.BUTTON_RT,
            Control.BUTTON_L_THUMB,
            Control.BUTTON_R_THUMB,
            Control.BUTTON_SELECT,
            Control.BUTTON_START,
            Control.BUTTON_MENU,
            Control.BUTTON_RECORD,
            Control.BUTTON_E_STOP,
        ]

    async def get_events(self) -> Dict[Control, Event]:
        return self.events

    def register_control_callback(self, control: Control, triggers: List[EventType], function: Optional[ControlFunction]):
        self.callbacks[control] = {trigger: function for trigger in triggers}

    async def trigger_event(self, event: Event):
        self.events[event.control] = event
        callback = self.callbacks.get(event.control, {}).get(event.event)
        if callback:
            callback(event)


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
        return Motor.Features(position_reporting=True)

    async def stop(self):
        await self.set_power(0)

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
