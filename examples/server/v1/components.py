import asyncio
import math
import random
import struct
import sys

if sys.version_info >= (3, 9):
    from collections.abc import AsyncIterator
else:
    from typing import AsyncIterator

from datetime import timedelta
from io import BytesIO
from multiprocessing import Lock
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Tuple

from PIL import Image

from viam.components.arm import Arm
from viam.components.audio_in import AudioIn, AudioResponse
from viam.components.audio_out import AudioOut
from viam.components.base import Base
from viam.components.board import Board, TickStream
from viam.components.camera import Camera
from viam.components.encoder import Encoder
from viam.components.gantry import Gantry
from viam.components.gripper import Gripper
from viam.components.input import Control, ControlFunction, Controller, Event, EventType
from viam.components.motor import Motor
from viam.components.movement_sensor import MovementSensor
from viam.components.pose_tracker import PoseTracker
from viam.components.sensor import Sensor
from viam.components.servo import Servo
from viam.errors import ResourceNotFoundError
from viam.media.audio import Audio, AudioStream
from viam.media.video import CameraMimeType, NamedImage, ViamImage
from viam.operations import run_with_operation
from viam.proto.common import (
    AudioInfo,
    Capsule,
    Geometry,
    GeoPoint,
    KinematicsFileFormat,
    Orientation,
    Pose,
    PoseInFrame,
    ResponseMetadata,
    Sphere,
    Vector3,
)
from viam.proto.component.arm import JointPositions
<<<<<<< Updated upstream
from viam.proto.component.audioin import AudioChunk as AudioInChunk
from viam.proto.component.audioinput import AudioChunk, AudioChunkInfo, SampleFormat
=======
>>>>>>> Stashed changes
from viam.proto.component.encoder import PositionType
from viam.streams import StreamWithIterator
from viam.utils import SensorReading

GEOMETRIES = [
    Geometry(center=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20), sphere=Sphere(radius_mm=2)),
    Geometry(center=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20), capsule=Capsule(radius_mm=3, length_mm=8)),
]


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
        self.joint_positions = JointPositions(values=[0, 0, 0, 0, 0, 0])
        self.is_stopped = True
        self.kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")
        super().__init__(name)

    async def get_end_position(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Pose:
        return self.position

    async def move_to_position(
        self,
        pose: Pose,
        extra: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        self.is_stopped = False
        self.position = pose

    async def get_joint_positions(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> JointPositions:
        return self.joint_positions

    async def move_to_joint_positions(self, positions: JointPositions, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.is_stopped = False
        self.joint_positions = positions

    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped

    async def get_kinematics(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        return self.kinematics

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES

class ExampleAudioIn(AudioIn):
    def __init__(self, name: str):
        super().__init__(name)
        self.sample_rate = 44100
        self.num_channels = 2
        self.supported_codecs = ["pcm16"]
        self.chunk_count = 0
        self.latency = timedelta(milliseconds=20)
        self.volume_scale = 0.2
        self.frequency_hz = 440

    async def get_audio(
        self, codec: str, duration_seconds: float, previous_timestamp_ns: int, *, timeout: Optional[float] = None, **kwargs
    ) -> AudioIn.AudioStream:
        async def read() -> AsyncIterator[AudioIn.AudioResponse]:
            # Generate chunks based on duration
            chunk_duration_ms = 100  # 100ms per chunk
            chunks_to_generate = max(1, int((duration_seconds * 1000) / chunk_duration_ms))

            for i in range(chunks_to_generate):
                # Generate audio data (sine wave pattern)
                chunk_data = b""
                samples_per_chunk = int(self.sample_rate * (chunk_duration_ms / 1000))

                for sample in range(samples_per_chunk):
                    # Calculate the timing in seconds of this audio sample
                    time_offset = (i * chunk_duration_ms / 1000) + (sample / self.sample_rate)
                    # Generate one 16-bit PCM audio sample for a sine wave
                    # 32767 scales the value from (-1,1) to full 16 bit signed range (-32768,32767)
                    amplitude = int(32767 * self.volume_scale * math.sin(2 * math.pi * self.frequency_hz * time_offset))

                    # Convert to 16-bit PCM stereo
                    sample_bytes = amplitude.to_bytes(2, byteorder="little", signed=True)
                    chunk_data += sample_bytes * self.num_channels

                chunk_start_time = previous_timestamp_ns + (i * chunk_duration_ms * 1000000)  # Convert ms to ns
                chunk_end_time = chunk_start_time + (chunk_duration_ms * 1000000)

                audio_chunk = AudioInChunk(
                    audio_data=bytes(chunk_data),
                    audio_info=AudioInfo(codec=codec, sample_rate_hz=int(self.sample_rate), num_channels=self.num_channels),
                    sequence=i,
                    start_timestamp_nanoseconds=chunk_start_time,
                    end_timestamp_nanoseconds=chunk_end_time,
                )
                audio_response = AudioResponse(audio=audio_chunk)
                yield audio_response

                await asyncio.sleep(self.latency.total_seconds())

        return StreamWithIterator(read())

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> AudioIn.Properties:
        """Return the audio input device properties."""
        return AudioIn.Properties(supported_codecs=self.supported_codecs, sample_rate_hz=self.sample_rate, num_channels=self.num_channels)

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleAudioOut(AudioOut):
    def __init__(self, name: str):
        super().__init__(name)
        self.sample_rate = 44100
        self.num_channels = 2
        self.supported_codecs = ["pcm16", "mp3", "wav"]
        self.volume = 1.0
        self.is_playing = False

    async def play(
        self,
        data: bytes,
        info: Optional[AudioInfo] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> None:
        """Play the given audio data."""

        # Simulate playing audio
        self.is_playing = True
        if info:
            print(
                f"Playing audio: {len(data)} bytes, codec={info.codec}, " f"sample_rate={info.sample_rate_hz}, channels={info.num_channels}"
            )
        else:
            print(f"Playing audio: {len(data)} bytes (no audio info provided)")

        await asyncio.sleep(0.1)

        self.is_playing = False

    async def get_properties(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> AudioOut.Properties:
        """Return the audio output device properties."""

        return AudioOut.Properties(supported_codecs=self.supported_codecs, sample_rate_hz=self.sample_rate, num_channels=self.num_channels)

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleBase(Base):
    def __init__(self, name: str):
        self.position = 0
        self.angle = 0
        self.is_stopped = True
        self.linear_pwr = Vector3(x=0, y=0, z=0)
        self.angular_pwr = Vector3(x=0, y=0, z=0)
        self.linear_vel = Vector3(x=0, y=0, z=0)
        self.angular_vel = Vector3(x=0, y=0, z=0)
        self.props = Base.Properties(1.0, 1.0, 1.0)
        super().__init__(name)

    async def move_straight(self, distance: int, velocity: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        if distance == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
        else:
            self.position -= distance

        self.is_stopped = False

    async def spin(self, angle: float, velocity: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        if angle == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.angle += angle
        else:
            self.angle -= angle

        self.is_stopped = False

    async def set_power(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.linear_pwr = linear
        self.angular_pwr = angular

    async def set_velocity(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.linear_vel = linear
        self.angular_vel = angular

    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Base.Properties:
        return self.props

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleAnalog(Board.Analog):
    def __init__(self, name: str, value: int):
        self.value = value
        super().__init__(name)

    async def read(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> int:
        return self.value

    async def write(self, value: int, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float], **kwargs):
        self.value = value


class ExampleDigitalInterrupt(Board.DigitalInterrupt):
    def __init__(self, name: str):
        self.num_ticks = 0
        super().__init__(name)

    async def value(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> int:
        return self.num_ticks


class ExampleGPIOPin(Board.GPIOPin):
    def __init__(self, name: str):
        self.high = False
        self.pwm = 0.0
        self.pwm_freq = 0
        super().__init__(name)

    async def get(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> bool:
        return self.high

    async def set(self, high: bool, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.high = high

    async def get_pwm(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> float:
        return self.pwm

    async def set_pwm(self, duty_cycle: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.pwm = duty_cycle

    async def get_pwm_frequency(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> int:
        return self.pwm_freq

    async def set_pwm_frequency(self, frequency: int, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.pwm_freq = frequency


class ExampleBoard(Board):
    def __init__(
        self,
        name: str,
        analogs: Dict[str, Board.Analog],
        digital_interrupts: Dict[str, Board.DigitalInterrupt],
        gpio_pins: Dict[str, Board.GPIOPin],
    ):
        self.analogs = analogs
        self.digital_interrupts = digital_interrupts
        self.gpios = gpio_pins
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

    async def set_power_mode(self, **kwargs):
        raise NotImplementedError()

    async def stream_ticks(self, interrupts: List[Board.DigitalInterrupt], *, timeout: Optional[float] = None, **kwargs) -> TickStream:
        raise NotImplementedError()

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleCamera(Camera):
    def __init__(self, name: str):
        p = Path(__file__)
        img = Image.open(p.parent.absolute().joinpath("viam.jpeg"))
        buf = BytesIO()
        img.copy().save(buf, format="JPEG")
        self.image = ViamImage(buf.getvalue(), CameraMimeType.JPEG)
        img.close()
        super().__init__(name)

    async def get_image(self, mime_type: str = "", extra: Optional[Dict[str, Any]] = None, **kwargs) -> ViamImage:
        return self.image

    async def get_images(self, timeout: Optional[float] = None, **kwargs) -> Tuple[List[NamedImage], ResponseMetadata]:
        raise NotImplementedError()

    async def get_point_cloud(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Tuple[bytes, str]:
        raise NotImplementedError()

    async def get_properties(self, **kwargs) -> Camera.Properties:
        raise NotImplementedError()

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleController(Controller):
    CONTROL_MAP: Dict[int, Control] = {
        0: Control.ABSOLUTE_X,
        1: Control.ABSOLUTE_Y,
        2: Control.ABSOLUTE_Z,
        3: Control.ABSOLUTE_RX,
        4: Control.ABSOLUTE_RY,
        5: Control.ABSOLUTE_RZ,
        16: Control.ABSOLUTE_HAT0_X,
        17: Control.ABSOLUTE_HAT0_Y,
        304: Control.BUTTON_SOUTH,
        305: Control.BUTTON_EAST,
        307: Control.BUTTON_WEST,
        308: Control.BUTTON_NORTH,
        310: Control.BUTTON_LT,
        311: Control.BUTTON_RT,
        314: Control.BUTTON_SELECT,
        315: Control.BUTTON_START,
        317: Control.BUTTON_L_THUMB,
        318: Control.BUTTON_R_THUMB,
        316: Control.BUTTON_MENU,
    }

    def __init__(self, name: str):
        super().__init__(name)
        self.last_events: Dict[Control, Event] = {}
        self.callbacks: Dict[Control, Dict[EventType, Optional[ControlFunction]]] = {}
        self.lock = Lock()

        self.f = open("/dev/input/event0", "rb")
        asyncio.get_running_loop().add_reader(self.f, self._read_input)

    def _read_input(self):
        data = self.f.read(24)
        raw = struct.unpack("4IHHI", data)
        if raw[4:] == (0, 0, 0):
            return
        secs = raw[0]
        nanos = raw[2]
        control = ExampleController.CONTROL_MAP[raw[5]]
        value = raw[6]
        e_type: EventType
        if raw[5] < 20:
            e_type = EventType.POSITION_CHANGE_ABSOLUTE
        else:
            e_type = EventType.BUTTON_RELEASE
            if value == 1:
                e_type = EventType.BUTTON_PRESS
        if value == 4294967295:
            value = -1
        event = Event(time=float(((secs * 1e9) + nanos) / 1e9), control=control, event=e_type, value=value)
        with self.lock:
            self.last_events[control] = event

        self._execute_callback(event)

    def _execute_callback(self, event):
        with self.lock:
            callback = self.callbacks.get(event.control, {}).get(event.event, None)
            if callback:
                callback(event)

            callback = self.callbacks.get(event.control, {}).get(EventType.ALL_EVENTS, None)
            if callback:
                callback(event)

    async def get_controls(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Control]:
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
        ]

    async def get_events(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[Control, Event]:
        with self.lock:
            return {key: value for (key, value) in self.last_events.items()}

    def register_control_callback(self, control: Control, triggers: List[EventType], function: Optional[ControlFunction]):
        with self.lock:
            callbacks = self.callbacks.get(control, {})
            for trigger in triggers:
                if trigger == EventType.BUTTON_CHANGE:
                    callbacks[EventType.BUTTON_PRESS] = function
                    callbacks[EventType.BUTTON_RELEASE] = function
                else:
                    callbacks[trigger] = function
            self.callbacks[control] = callbacks

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleEncoder(Encoder):
    def __init__(self, name: str):
        self.position: float = 0
        self.position_type = PositionType.POSITION_TYPE_TICKS_COUNT
        self.powered = False
        self.task = None
        super().__init__(name)

    async def reset_position(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.position = 0

    async def get_position(
        self, position_type: Optional[PositionType.ValueType], extra: Optional[Dict[str, Any]] = None, **kwargs
    ) -> Tuple[float, PositionType.ValueType]:
        return self.position, self.position_type

    async def get_properties(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Encoder.Properties:
        return Encoder.Properties(ticks_count_supported=True, angle_degrees_supported=False)

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleGantry(Gantry):
    def __init__(self, name: str, position: List[float], lengths: List[float]):
        self.position = position
        self.lengths = lengths
        self.is_stopped = True
        super().__init__(name)

    async def get_position(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[float]:
        return self.position

    async def move_to_position(
        self,
        positions: List[float],
        speeds: List[float],
        extra: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        self.position = positions
        self.is_stopped = False

    async def get_lengths(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[float]:
        return self.lengths

    async def home(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> bool:
        return True

    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES

    async def get_kinematics(self, *, extra=None, timeout=None, **kwargs) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        return (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_UNSPECIFIED, b"abc")


class ExampleGripper(Gripper):
    def __init__(self, name: str):
        self.opened = False
        self.is_stopped = True
        self.holding_something = False
        self.kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")
        super().__init__(name)

    async def open(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.opened = True
        self.is_stopped = False
        self.holding_something = False

    async def grab(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> bool:
        self.opened = False
        self.is_stopped = False
        self.holding_something = random.choice([True, False])
        return self.holding_something

    async def is_holding_something(self, *, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Gripper.HoldingStatus:
        return Gripper.HoldingStatus(self.holding_something)

    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES

    async def get_kinematics(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        return self.kinematics


class ExampleMotor(Motor):
    def __init__(self, name: str):
        self.position: float = 0
        self.power = 0
        self.powered = False
        self.task = None
        super().__init__(name)

    async def run_continuously(self, rpm: float):
        rps = rpm / 60
        while True:
            await asyncio.sleep(1)
            self.position += rps

    async def set_power(self, power: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.power = power
        self.powered = power != 0
        if self.powered:
            self.task = asyncio.create_task(self.run_continuously(power))
        else:
            if self.task:
                self.task.cancel()

    async def go_for(self, rpm: float, revolutions: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        if self.task:
            self.task.cancel()
        target = 0
        rps = rpm / 60
        if rpm > 0:
            target = self.position + revolutions
        if rpm < 0:
            target = self.position - revolutions
        self.powered = True
        while abs(self.position - target) > 0.01:
            await asyncio.sleep(1)
            self.position += rps
        self.powered = False

    async def go_to(self, rpm: float, position_revolutions: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        if self.task:
            self.task.cancel()
        distance = position_revolutions - self.position
        rps = rpm / 60
        self.powered = True
        while distance > 0:
            await asyncio.sleep(1)
            distance -= abs(rps)
            self.position += rps
        self.powered = False

    async def set_rpm(self, rpm: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        if self.task:
            self.task.cancel()
        self.powered = True
        self.task = asyncio.create_task(self.run_continuously(rpm))

    async def reset_zero_position(self, offset: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        if (self.position > 0 and offset > 0) or (self.position < 0 and offset < 0):
            self.position = offset
        else:
            self.position += offset
        self.powered = False

    async def get_position(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> float:
        return self.position

    async def get_properties(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Motor.Properties:
        return Motor.Properties(position_reporting=True)

    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        await self.set_power(0)

    async def is_powered(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Tuple[bool, float]:
        return self.powered, self.power

    async def is_moving(self):
        return self.powered

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleMovementSensor(MovementSensor):
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
        self.num_readings = random.randint(1, 10)
        self.coordinates = coordinates
        self.altitude = altitude
        self.lin_vel = lin_vel
        self.ang_vel = ang_vel
        self.lin_acc = lin_acc
        self.heading = heading
        self.orientation = orientation
        self.properties = properties
        self.accuracy = accuracy

    async def get_readings(self, **kwargs) -> Mapping[str, SensorReading]:
        return {"abcdefghij"[idx]: random.random() for idx in range(self.num_readings)}

    async def get_position(self, **kwargs) -> Tuple[GeoPoint, float]:
        return (self.coordinates, self.altitude)

    async def get_linear_velocity(self, **kwargs) -> Vector3:
        return self.lin_vel

    async def get_angular_velocity(self, **kwargs) -> Vector3:
        return self.ang_vel

    async def get_linear_acceleration(self, **kwargs) -> Vector3:
        return self.lin_acc

    async def get_compass_heading(self, **kwargs) -> float:
        return self.heading

    async def get_orientation(self, **kwargs) -> Orientation:
        return self.orientation

    async def get_properties(self, **kwargs) -> MovementSensor.Properties:
        return self.properties

    async def get_accuracy(self, **kwargs) -> Mapping[str, float]:
        return self.accuracy

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExamplePoseTracker(PoseTracker):
    async def get_poses(self, body_names: List[str], **kwargs) -> Dict[str, PoseInFrame]:
        all_poses = {
            "body1": PoseInFrame(reference_frame="0", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)),
            "body2": PoseInFrame(reference_frame="0", pose=Pose(x=3, y=2, z=3, o_x=4, o_y=3, o_z=4, theta=40)),
        }
        return {k: v for k, v in all_poses.items() if k in body_names}

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleSensor(Sensor):
    def __init__(self, name: str):
        self.num_readings = random.randint(1, 10)
        super().__init__(name)

    async def get_readings(self, **kwargs) -> Mapping[str, SensorReading]:
        return {"abcdefghij"[idx]: random.random() for idx in range(self.num_readings)}

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES


class ExampleServo(Servo):
    def __init__(self, name: str):
        self.angle = 0
        self.is_stopped = True
        super().__init__(name)

    async def move(self, angle: int, **kwargs):
        self.angle = angle
        self.is_stopped = False

    async def get_position(self, **kwargs) -> int:
        return self.angle

    async def stop(self, **kwargs):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped

    async def get_geometries(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> List[Geometry]:
        return GEOMETRIES
