import sys

if sys.version_info >= (3, 9):
    from collections.abc import AsyncIterator
else:
    from typing import AsyncIterator

from dataclasses import dataclass
from datetime import datetime, timedelta
from secrets import choice
from typing import Any, Dict, List, Mapping, Optional, Tuple

from google.protobuf.timestamp_pb2 import Timestamp

from viam.components.arm import Arm, JointPositions, KinematicsFileFormat
from viam.components.audio_input import AudioInput
from viam.components.base import Base
from viam.components.board import Board, Tick
from viam.components.button import Button
from viam.components.camera import Camera, DistortionParameters, IntrinsicParameters
from viam.components.encoder import Encoder
from viam.components.gantry import Gantry
from viam.components.generic import Generic as GenericComponent
from viam.components.gripper import Gripper
from viam.components.input import Control, ControlFunction, Controller, Event, EventType
from viam.components.motor import Motor
from viam.components.movement_sensor import MovementSensor
from viam.components.pose_tracker import PoseTracker
from viam.components.power_sensor import PowerSensor
from viam.components.sensor import Sensor
from viam.components.servo import Servo
from viam.components.switch import Switch
from viam.errors import ResourceNotFoundError
from viam.media.audio import Audio, AudioStream
from viam.media.video import CameraMimeType, NamedImage, ViamImage
from viam.proto.common import Capsule, Geometry, GeoPoint, Orientation, Pose, PoseInFrame, ResponseMetadata, Sphere, Vector3
from viam.proto.component.audioinput import AudioChunk, AudioChunkInfo, SampleFormat
from viam.proto.component.board import PowerMode
from viam.proto.component.encoder import PositionType
from viam.streams import StreamWithIterator
from viam.utils import SensorReading, ValueTypes

GEOMETRIES = [
    Geometry(center=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20), sphere=Sphere(radius_mm=2)),
    Geometry(center=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20), capsule=Capsule(radius_mm=3, length_mm=8)),
]


class MockArm(Arm):
    def __init__(self, name: str):
        self.position = Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)
        self.joint_positions = JointPositions(values=[0, 0, 0, 0, 0, 0])
        self.is_stopped = True
        self.kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")
        self.geometries = GEOMETRIES
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

    async def get_kinematics(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None
    ) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        self.extra = extra
        self.timeout = timeout
        return self.kinematics

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockAudioInput(AudioInput):
    def __init__(self, name: str, properties: AudioInput.Properties):
        super().__init__(name)
        self.geometries = GEOMETRIES
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
        return StreamWithIterator(read())

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> AudioInput.Properties:
        self.timeout = timeout
        return self.properties

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockBase(Base):
    def __init__(self, name: str):
        self.position = 0
        self.angle = 0
        self.stopped = True
        self.linear_pwr = Vector3(x=0, y=0, z=0)
        self.angular_pwr = Vector3(x=0, y=0, z=0)
        self.linear_vel = Vector3(x=0, y=0, z=0)
        self.angular_vel = Vector3(x=0, y=0, z=0)
        self.geometries = GEOMETRIES
        self.extra: Optional[Dict[str, Any]] = None
        self.timeout: Optional[float] = None
        self.props = Base.Properties(1.0, 2.0, 3.0)
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

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Base.Properties:
        self.timeout = timeout
        return self.props

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockAnalog(Board.Analog):
    def __init__(self, name: str, value: int, min_range: float, max_range: float, step_size: float):
        self.value = self.Value(value=value, min_range=min_range, max_range=max_range, step_size=step_size)
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def read(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Board.Analog.Value:
        self.extra = extra
        self.timeout = timeout
        return self.value

    async def write(self, value: int, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        self.extra = extra
        self.timeout = timeout
        self.value.value = value


class MockDigitalInterrupt(Board.DigitalInterrupt):
    def __init__(self, name: str):
        self.high = False
        self.val = 182
        super().__init__(name)

    async def value(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        return self.val


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
        analogs: Dict[str, Board.Analog],
        digital_interrupts: Dict[str, Board.DigitalInterrupt],
        gpio_pins: Dict[str, Board.GPIOPin],
    ):
        self.analogs = analogs
        self.digital_interrupts = digital_interrupts
        self.geometries = GEOMETRIES
        self.gpios = gpio_pins
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def analog_by_name(self, name: str) -> Board.Analog:
        try:
            return self.analogs[name]
        except KeyError:
            raise ResourceNotFoundError("Board.Analog", name)

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

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}

    async def set_power_mode(
        self, mode: PowerMode.ValueType, duration: Optional[timedelta] = None, *, timeout: Optional[float] = None, **kwargs
    ):
        self.timeout = timeout
        self.power_mode = mode
        self.power_mode_duration = duration

    async def stream_ticks(self, interrupts: List[Board.DigitalInterrupt], *, timeout: Optional[float] = None, **kwargs):
        async def read() -> AsyncIterator[Tick]:
            yield Tick(pin_name=interrupts[0].name, high=True, time=1000)

        return StreamWithIterator(read())


class MockCamera(Camera):
    def __init__(self, name: str):
        self.image = ViamImage(b"data", CameraMimeType.PNG)
        self.geometries = GEOMETRIES
        self.point_cloud = b"THIS IS A POINT CLOUD"
        self.extra = None
        self.props = Camera.Properties(
            supports_pcd=False,
            intrinsic_parameters=IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6),
            distortion_parameters=DistortionParameters(model="no_distortion"),
            mime_types=[CameraMimeType.PNG, CameraMimeType.JPEG],
            frame_rate=10.0,
        )
        self.timeout: Optional[float] = None
        ts = Timestamp()
        ts.FromDatetime(datetime(1970, 1, 1))
        self.metadata = ResponseMetadata(captured_at=ts)
        super().__init__(name)

    async def get_image(
        self, mime_type: str = "", extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> ViamImage:
        self.extra = extra
        self.timeout = timeout
        return self.image

    async def get_images(self, timeout: Optional[float] = None, **kwargs) -> Tuple[List[NamedImage], ResponseMetadata]:
        self.timeout = timeout
        return [NamedImage(self.name, self.image.data, self.image.mime_type)], self.metadata

    async def get_point_cloud(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Tuple[bytes, str]:
        self.extra = extra
        self.timeout = timeout
        return self.point_cloud, CameraMimeType.PCD

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Camera.Properties:
        self.timeout = timeout
        return self.props

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockEncoder(Encoder):
    def __init__(self, name: str):
        self.position: float = 0
        self.position_type = PositionType.POSITION_TYPE_TICKS_COUNT
        self.geometries = GEOMETRIES
        self.extra = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def reset_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        self.position = 0
        self.extra = extra
        self.timeout = timeout

    async def get_position(
        self,
        position_type: Optional[PositionType.ValueType] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[float, PositionType.ValueType]:
        self.extra = extra
        self.timeout = timeout
        return self.position, self.position_type

    async def get_properties(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Encoder.Properties:
        self.extra = extra
        self.timeout = timeout
        return Encoder.Properties(ticks_count_supported=True, angle_degrees_supported=False)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockGantry(Gantry):
    def __init__(self, name: str, position: List[float], lengths: List[float]):
        self.position = position
        self.lengths = lengths
        self.is_stopped = True
        self.extra = None
        self.homed = True
        self.speeds = Optional[List[float]]
        self.geometries = GEOMETRIES
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        self.extra = extra
        self.timeout = timeout
        return self.position

    async def move_to_position(
        self,
        positions: List[float],
        speeds: List[float],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        self.position = positions
        self.speeds = speeds
        self.is_stopped = False
        self.extra = extra
        self.timeout = timeout

    async def home(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> bool:
        self.homed = True
        self.extra = extra
        self.timeout = timeout
        return self.homed

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

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockGenericComponent(GenericComponent):
    timeout: Optional[float] = None
    geometries = GEOMETRIES

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        self.timeout = timeout
        return {key: True for key in command.keys()}


class MockGripper(Gripper):
    def __init__(self, name: str):
        self.opened = False
        self.geometries = GEOMETRIES
        self.kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")
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

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def get_kinematics(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        self.extra = extra
        self.timeout = timeout
        return self.kinematics

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockInputController(Controller):
    def __init__(self, name: str):
        super().__init__(name)
        self.events: Dict[Control, Event] = {}
        self.callbacks: Dict[Control, Dict[EventType, Optional[ControlFunction]]] = {}
        self.geometries = GEOMETRIES
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

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockMotor(Motor):
    def __init__(self, name: str):
        self.position: float = 0
        self.power = 0
        self.powered = False
        self.geometries = GEOMETRIES
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

    async def set_rpm(
        self,
        rpm: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        self.powered = True
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

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


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
        accuracy: MovementSensor.Accuracy,
        readings: Mapping[str, float],
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
        self.readings = readings
        self.geometries = GEOMETRIES
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
    ) -> MovementSensor.Accuracy:
        self.extra = extra
        self.timeout = timeout
        return self.accuracy

    async def get_readings(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, float]:
        self.extra = extra
        self.timeout = timeout
        return self.readings

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


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
        self.geometries = GEOMETRIES
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

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockPowerSensor(PowerSensor):
    def __init__(self, name: str, voltage: float, current: float, is_ac: bool, power: float, readings: Mapping[str, float]):
        super().__init__(name)
        self.voltage = voltage
        self.current = current
        self.is_ac = is_ac
        self.power = power
        self.readings = readings
        self.geometries = GEOMETRIES
        self.extra: Optional[Dict[str, Any]] = None
        self.timeout: Optional[float] = None

    async def get_voltage(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        self.extra = extra
        self.timeout = timeout
        return (self.voltage, self.is_ac)

    async def get_current(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        self.extra = extra
        self.timeout = timeout
        return (self.current, self.is_ac)

    async def get_power(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        self.extra = extra
        self.timeout = timeout
        return self.power

    async def get_readings(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, float]:
        self.extra = extra
        self.timeout = timeout
        return self.readings

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockSensor(Sensor):
    def __init__(self, name: str, result: Mapping[str, Any] = {"a": 0, "b": {"foo": "bar"}, "c": [1, 8, 2], "d": "Hello world!"}):
        self.readings = result
        self.geometries = GEOMETRIES
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        self.extra = extra
        self.timeout = timeout
        return self.readings

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockServo(Servo):
    def __init__(self, name: str):
        self.angle = 0
        self.is_stopped = True
        self.geometries = GEOMETRIES
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

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        self.extra = extra
        self.timeout = timeout
        return self.geometries

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockSwitch(Switch):
    def __init__(self, name: str, number_of_positions: int = 3, position: int = 0):
        self.number_of_positions = number_of_positions
        self.position = position
        self.timeout: Optional[float] = None
        self.extra: Optional[Mapping[str, Any]] = None
        super().__init__(name)

    async def get_position(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        self.extra = extra
        self.timeout = timeout
        return self.position

    async def get_number_of_positions(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        self.extra = extra
        self.timeout = timeout
        return self.number_of_positions

    async def set_position(
        self, position: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> None:
        self.extra = extra
        self.timeout = timeout
        self.position = position

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockButton(Button):
    def __init__(self, name: str):
        self.pushed = False
        self.timeout: Optional[float] = None
        self.extra: Optional[Mapping[str, Any]] = None
        super().__init__(name)

    async def push(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> None:
        self.extra = extra
        self.timeout = timeout
        self.pushed = True

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}
