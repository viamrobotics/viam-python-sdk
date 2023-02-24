import sys

if sys.version_info.minor >= 9:
    from collections.abc import AsyncIterator
else:
    from typing import AsyncIterator

from dataclasses import dataclass
from multiprocessing import Queue
from secrets import choice
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

from PIL import Image

from viam.components.arm import Arm, JointPositions
from viam.components.audio_input import AudioInput
from viam.components.base import Base
from viam.components.board import Board
from viam.components.board.board import PostProcessor
from viam.components.camera import Camera, DistortionParameters, IntrinsicParameters
from viam.components.gantry import Gantry
from viam.components.generic import Generic as GenericComponent
from viam.components.gripper import Gripper
from viam.components.input import Control, ControlFunction, Controller, Event, EventType
from viam.components.motor import Motor
from viam.components.movement_sensor import MovementSensor
from viam.components.pose_tracker import PoseTracker
from viam.components.sensor import Sensor
from viam.components.servo import Servo
from viam.errors import ResourceNotFoundError
from viam.media import MediaStreamWithIterator
from viam.media.audio import Audio, AudioStream
from viam.media.video import CameraMimeType, RawImage
from viam.proto.common import (
    AnalogStatus,
    BoardStatus,
    DigitalInterruptStatus,
    GeoPoint,
    Orientation,
    Pose,
    PoseInFrame,
    Vector3,
    WorldState,
)
from viam.proto.component.audioinput import AudioChunk, AudioChunkInfo, SampleFormat


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
        self.joint_positions = JointPositions(values=[0, 0, 0, 0, 0, 0])
        self.is_stopped = True
        self.extra = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_end_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Pose:
        self.extra = extra
        self.timeout = timeout
        return self.position

    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        self.position = pose
        self.is_stopped = False
        self.extra = extra
        self.timeout = timeout

    async def get_joint_positions(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> JointPositions:
        self.extra = extra
        self.timeout = timeout
        return self.joint_positions

    async def move_to_joint_positions(
        self, positions: JointPositions, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ):
        self.joint_positions = positions
        self.is_stopped = False
        self.extra = extra
        self.timeout = timeout

    async def stop(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.is_stopped = True
        self.extra = extra
        self.timeout = timeout

    async def is_moving(self) -> bool:
        return not self.is_stopped

    async def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None, **kwargs) -> Dict[str, Any]:
        return {"hello": "world"}


class MockAudioInput(AudioInput):
    def __init__(self, name: str, properties: AudioInput.Properties):
        super().__init__(name)
        self.properties = properties
        self.timeout: Optional[float] = None

    async def stream(self, *, timeout: Optional[float] = None, **kwargs) -> AudioStream:
        async def read() -> AsyncIterator[Audio]:
            for i in range(10):
                yield Audio(
                    AudioChunkInfo(
                        sample_format=SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED,
                        channels=self.properties.channel_count,
                        sampling_rate=self.properties.sample_rate,
                    ),
                    AudioChunk(data=f"{i}".encode("utf-8"), length=182),
                )

        self.timeout = timeout
        return MediaStreamWithIterator(read())

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> AudioInput.Properties:
        self.timeout = timeout
        return self.properties


class MockBase(Base):
    def __init__(self, name: str):
        self.position = 0
        self.angle = 0
        self.stopped = True
        self.linear_pwr = Vector3(x=0, y=0, z=0)
        self.angular_pwr = Vector3(x=0, y=0, z=0)
        self.linear_vel = Vector3(x=0, y=0, z=0)
        self.angular_vel = Vector3(x=0, y=0, z=0)
        self.extra: Optional[Dict[str, Any]] = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def move_straight(
        self, distance: int, velocity: float, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ):
        if distance == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
        else:
            self.position -= distance

        self.stopped = False
        self.extra = extra
        self.timeout = timeout

    async def move_arc(
        self,
        distance: int,
        velocity: float,
        angle: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
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
        self.extra = extra
        self.timeout = timeout

    async def spin(
        self, angle: float, velocity: float, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ):
        if angle == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.angle += angle
        else:
            self.angle -= angle

        self.stopped = False
        self.extra = extra
        self.timeout = timeout

    async def set_velocity(
        self, linear: Vector3, angular: Vector3, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ):
        self.linear_vel = linear
        self.angular_vel = angular
        self.extra = extra
        self.timeout = timeout

    async def set_power(
        self, linear: Vector3, angular: Vector3, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ):
        self.linear_pwr = linear
        self.angular_pwr = angular
        self.extra = extra

    async def stop(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.stopped = True
        self.extra = extra
        self.timeout = timeout

    async def is_moving(self) -> bool:
        return not self.stopped


class MockAnalogReader(Board.AnalogReader):
    def __init__(self, name: str, value: int):
        self.value = value
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def read(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        self.extra = extra
        self.timeout = timeout
        return self.value


class MockDigitalInterrupt(Board.DigitalInterrupt):
    def __init__(self, name: str):
        self.high = False
        self.last_tick = 0
        self.num_ticks = 0
        self.callbacks: List[Queue] = []
        self.post_processors: List[PostProcessor] = []
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def value(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        self.extra = extra
        self.timeout = timeout
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
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> bool:
        self.extra = extra
        self.timeout = timeout
        return self.high

    async def set(self, high: bool, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.high = high
        self.extra = extra
        self.timeout = timeout

    async def get_pwm(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        self.extra = extra
        self.timeout = timeout
        return self.pwm

    async def set_pwm(self, duty_cycle: float, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.pwm = duty_cycle
        self.extra = extra
        self.timeout = timeout

    async def get_pwm_frequency(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        self.extra = extra
        self.timeout = timeout
        return self.pwm_freq

    async def set_pwm_frequency(self, frequency: int, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.pwm_freq = frequency
        self.extra = extra
        self.timeout = timeout


class MockBoard(Board):
    def __init__(
        self,
        name: str,
        analog_readers: Dict[str, Board.AnalogReader],
        digital_interrupts: Dict[str, Board.DigitalInterrupt],
        gpio_pins: Dict[str, Board.GPIOPin],
    ):
        self.analog_readers = analog_readers
        self.digital_interrupts = digital_interrupts
        self.gpios = gpio_pins
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def analog_reader_by_name(self, name: str) -> Board.AnalogReader:
        try:
            return self.analog_readers[name]
        except KeyError:
            raise ResourceNotFoundError("Board.AnalogReader", name)

    async def digital_interrupt_by_name(self, name: str) -> Board.DigitalInterrupt:
        try:
            return self.digital_interrupts[name]
        except KeyError:
            raise ResourceNotFoundError("Board.DigitalInterrupt", name)

    async def gpio_pin_by_name(self, name: str) -> Board.GPIOPin:
        try:
            return self.gpios[name]
        except KeyError:
            raise ResourceNotFoundError("Board.GPIOPin", name)

    async def analog_reader_names(self) -> List[str]:
        return [key for key in self.analog_readers.keys()]

    async def digital_interrupt_names(self) -> List[str]:
        return [key for key in self.digital_interrupts.keys()]

    async def status(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> BoardStatus:
        self.extra = extra
        self.timeout = timeout
        return BoardStatus(
            analogs={name: AnalogStatus(value=await analog.read()) for (name, analog) in self.analog_readers.items()},
            digital_interrupts={name: DigitalInterruptStatus(value=await di.value()) for (name, di) in self.digital_interrupts.items()},
        )

    async def model_attributes(self) -> Board.Attributes:
        return Board.Attributes(remote=True)


class MockCamera(Camera):
    def __init__(self, name: str):
        self.image = Image.new("RGBA", (100, 100), "#AABBCCDD")
        self.point_cloud = b"THIS IS A POINT CLOUD"
        self.props = Camera.Properties(
            True,
            IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6),
            DistortionParameters(model="no_distortion"),
        )
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_image(self, mime_type: str = "", timeout: Optional[float] = None, **kwargs) -> Union[Image.Image, RawImage]:
        self.timeout = timeout
        mime_type, is_lazy = CameraMimeType.from_lazy(mime_type)
        if is_lazy or (not CameraMimeType.is_supported(mime_type)):
            return RawImage(
                data=self.image.convert("RGBA").tobytes("raw", "RGBA"),
                mime_type=mime_type,
            )
        return self.image.copy()

    async def get_point_cloud(self, *, timeout: Optional[float] = None, **kwargs) -> Tuple[bytes, str]:
        self.timeout = timeout
        return self.point_cloud, CameraMimeType.PCD.value

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Camera.Properties:
        self.timeout = timeout
        return self.props


class MockGantry(Gantry):
    def __init__(self, name: str, position: List[float], lengths: List[float]):
        self.position = position
        self.lengths = lengths
        self.is_stopped = True
        self.extra = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        self.extra = extra
        self.timeout = timeout
        return self.position

    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        self.position = positions
        self.is_stopped = False
        self.extra = extra
        self.timeout = timeout

    async def get_lengths(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        self.extra = extra
        self.timeout = timeout
        return self.lengths

    async def stop(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.extra = extra
        self.is_stopped = True
        self.timeout = timeout

    async def is_moving(self) -> bool:
        return not self.is_stopped


class MockGeneric(GenericComponent):

    timeout: Optional[float] = None

    async def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None, **kwargs) -> Dict[str, Any]:
        self.timeout = timeout
        return {key: True for key in command.keys()}


class MockGripper(Gripper):
    def __init__(self, name: str):
        self.opened = False
        self.extra = None
        self.is_stopped = True
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def open(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.opened = True
        self.is_stopped = False
        self.extra = extra
        self.timeout = timeout

    async def grab(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> bool:
        self.opened = False
        self.is_stopped = False
        self.timeout = timeout
        self.extra = extra
        return choice([True, False])

    async def stop(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.is_stopped = True
        self.extra = extra
        self.timeout = timeout

    async def is_moving(self) -> bool:
        return not self.is_stopped


class MockInputController(Controller):
    def __init__(self, name: str):
        super().__init__(name)
        self.events: Dict[Control, Event] = {}
        self.callbacks: Dict[Control, Dict[EventType, Optional[ControlFunction]]] = {}
        self.timeout: Optional[float] = None
        self.extra = None
        self.reg_extra = None

    async def get_controls(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Control]:
        self.extra = extra
        self.timeout = timeout
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

    async def get_events(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Dict[Control, Event]:
        self.extra = extra
        self.timeout = timeout
        return self.events

    def register_control_callback(
        self,
        control: Control,
        triggers: List[EventType],
        function: Optional[ControlFunction],
        extra: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        self.callbacks[control] = {trigger: function for trigger in triggers}
        self.reg_extra = extra

    async def trigger_event(self, event: Event, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.events[event.control] = event
        self.extra = extra
        self.timeout = timeout
        callback = self.callbacks.get(event.control, {}).get(event.event)
        if callback:
            callback(event)


class MockMotor(Motor):
    def __init__(self, name: str):
        self.position: float = 0
        self.power = 0
        self.powered = False
        self.extra = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def set_power(
        self,
        power: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        self.power = power
        self.powered = power != 0
        self.extra = extra
        self.timeout = timeout

    async def go_for(
        self,
        rpm: float,
        revolutions: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        if rpm > 0:
            self.position += revolutions
        if rpm < 0:
            self.position -= revolutions
        self.powered = False
        self.extra = extra
        self.timeout = timeout

    async def go_to(
        self,
        rpm: float,
        position_revolutions: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        if rpm != 0:
            self.position = position_revolutions
        self.powered = False
        self.extra = extra
        self.timeout = timeout

    async def reset_zero_position(
        self,
        offset: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        self.offset = offset
        self.powered = False
        self.extra = extra
        self.timeout = timeout

    async def get_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> float:
        self.extra = extra
        self.timeout = timeout
        return self.position

    async def get_properties(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Motor.Properties:
        self.extra = extra
        self.timeout = timeout
        return Motor.Properties(position_reporting=True)

    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        await self.set_power(0)
        self.timeout = timeout
        self.extra = extra

    async def is_powered(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[bool, float]:
        self.extra = extra
        self.timeout = timeout
        return self.powered, self.power

    async def is_moving(self) -> bool:
        return self.powered


class MockMovementSensor(MovementSensor):
    def __init__(
        self,
        name: str,
        coordinates: GeoPoint,
        altitude: float,
        lin_vel: Vector3,
        ang_vel: Vector3,
        lin_acc: Vector3,
        heading: float,
        orientation: Orientation,
        properties: MovementSensor.Properties,
        accuracy: Mapping[str, float],
    ):
        super().__init__(name)
        self.coordinates = coordinates
        self.altitude = altitude
        self.lin_vel = lin_vel
        self.ang_vel = ang_vel
        self.lin_acc = lin_acc
        self.heading = heading
        self.orientation = orientation
        self.properties = properties
        self.accuracy = accuracy
        self.extra: Optional[Dict[str, Any]] = None
        self.timeout: Optional[float] = None

    async def get_position(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Tuple[GeoPoint, float]:
        self.extra = extra
        self.timeout = timeout
        return (self.coordinates, self.altitude)

    async def get_linear_velocity(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Vector3:
        self.extra = extra
        self.timeout = timeout
        return self.lin_vel

    async def get_angular_velocity(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Vector3:
        self.extra = extra
        self.timeout = timeout
        return self.ang_vel

    async def get_linear_acceleration(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Vector3:
        self.extra = extra
        self.timeout = timeout
        return self.lin_acc

    async def get_compass_heading(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        self.extra = extra
        self.timeout = timeout
        return self.heading

    async def get_orientation(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Orientation:
        self.extra = extra
        self.timeout = timeout
        return self.orientation

    async def get_properties(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> MovementSensor.Properties:
        self.extra = extra
        self.timeout = timeout
        return self.properties

    async def get_accuracy(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, float]:
        self.extra = extra
        self.timeout = timeout
        return self.accuracy


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
        pose = Pose(x=self.X, y=self.Y, z=self.Z, o_x=self.o_X, o_y=self.o_Y, o_z=self.o_Z, theta=self.theta)
        return PoseInFrame(reference_frame=frame_name, pose=pose)


class MockPoseTracker(PoseTracker):
    def __init__(self, name: str, poses: List[MockPose]):
        pose_map: Dict[str, MockPose] = {}
        for idx, pose in enumerate(poses):
            pose_map[str(idx)] = pose
        self.poses_result = pose_map
        self.name = name
        self.timeout: Optional[float] = None
        self.extra: Optional[Mapping[str, Any]] = None

    async def get_poses(
        self,
        body_names: List[str],
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Dict[str, PoseInFrame]:
        result: Dict[str, PoseInFrame] = {}
        for name, pose in self.poses_result.items():
            result[name] = pose.to_pose_in_frame(name)
        self.timeout = timeout
        self.extra = extra
        return result


class MockSensor(Sensor):
    def __init__(self, name: str, result: Mapping[str, Any] = {"a": 0, "b": {"foo": "bar"}, "c": [1, 8, 2], "d": "Hello world!"}):
        self.readings = result
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, Any]:
        self.extra = extra
        self.timeout = timeout
        return self.readings


class MockServo(Servo):
    def __init__(self, name: str):
        self.angle = 0
        self.is_stopped = True
        self.timeout: Optional[float] = None
        self.extra: Optional[Mapping[str, Any]] = None
        super().__init__(name)

    async def move(self, angle: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.extra = extra
        self.angle = angle
        self.is_stopped = False
        self.timeout = timeout

    async def get_position(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        self.extra = extra
        self.timeout = timeout
        return self.angle

    async def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.extra = extra
        self.is_stopped = True
        self.timeout = timeout

    async def is_moving(self) -> bool:
        return not self.is_stopped
