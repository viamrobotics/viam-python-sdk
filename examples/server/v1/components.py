import asyncio
import random
import struct
from multiprocessing import Lock, Queue
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image
from viam.components.arm import Arm
from viam.components.base import Base
from viam.components.board import Board
from viam.components.board.board import PostProcessor
from viam.components.camera import Camera
from viam.components.gantry import Gantry
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
from viam.errors import ComponentNotFoundError
from viam.proto.api.common import (AnalogStatus, BoardStatus,
                                   DigitalInterruptStatus, Pose, PoseInFrame,
                                   Vector3, WorldState)
from viam.proto.api.component.arm import JointPositions


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
        super().__init__(name)

    async def get_end_position(self, extra: Optional[Dict[str, Any]] = None) -> Pose:
        return self.position

    async def move_to_position(
        self, pose: Pose,
        world_state: Optional[WorldState] = None
    ):
        self.is_stopped = False
        self.position = pose

    async def get_joint_positions(self, extra: Optional[Dict[str, Any]] = None) -> JointPositions:
        return self.joint_positions

    async def move_to_joint_positions(self, positions: JointPositions, extra: Optional[Dict[str, Any]] = None):
        self.is_stopped = False
        self.joint_positions = positions

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped


class ExampleBase(Base):

    def __init__(self, name: str):
        self.position = 0
        self.angle = 0
        self.is_stopped = True
        self.linear_pwr = Vector3(x=0, y=0, z=0)
        self.angular_pwr = Vector3(x=0, y=0, z=0)
        self.linear_vel = Vector3(x=0, y=0, z=0)
        self.angular_vel = Vector3(x=0, y=0, z=0)
        super().__init__(name)

    async def move_straight(
        self,
        distance: int,
        velocity: float,
        extra: Optional[Dict[str, Any]] = None
    ):
        if distance == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
        else:
            self.position -= distance

        self.is_stopped = False

    async def spin(self, angle: float, velocity: float, extra: Optional[Dict[str, Any]] = None):
        if angle == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.angle += angle
        else:
            self.angle -= angle

        self.is_stopped = False

    async def set_power(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None):
        self.linear_pwr = linear
        self.anglular_pwr = angular

    async def set_velocity(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None):
        self.linear_vel = linear
        self.anglular_vel = angular

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped


class ExampleAnalogReader(Board.AnalogReader):

    def __init__(self, name: str, value: int):
        self.value = value
        super().__init__(name)

    async def read(self) -> int:
        return self.value


class ExampleDigitalInterrupt(Board.DigitalInterrupt):

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


class ExampleGPIOPin(Board.GPIOPin):

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


class ExampleBoard(Board):

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


class ExampleCamera(Camera):
    def __init__(self, name: str):
        p = Path(__file__)
        self.image = Image.open(p.parent.absolute().joinpath("viam.webp"))
        super().__init__(name)

    async def get_frame(self) -> Image.Image:
        return self.image.copy()

    async def get_point_cloud(self) -> Tuple[bytes, str]:
        raise NotImplementedError()


class ExampleController(Controller):

    CONTROL_MAP: Dict[int, Control] = {
        0:   Control.ABSOLUTE_X,
        1:   Control.ABSOLUTE_Y,
        2:   Control.ABSOLUTE_Z,
        3:   Control.ABSOLUTE_RX,
        4:   Control.ABSOLUTE_RY,
        5:   Control.ABSOLUTE_RZ,
        16:  Control.ABSOLUTE_HAT0_X,
        17:  Control.ABSOLUTE_HAT0_Y,
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

        self.f = open('/dev/input/event0', 'rb')
        asyncio.get_running_loop().add_reader(self.f, self._read_input)

    def _read_input(self):
        data = self.f.read(24)
        raw = struct.unpack('4IHHI', data)
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
        event = Event(
            time=float(((secs*1e9)+nanos)/1e9),
            control=control,
            event=e_type,
            value=value
        )
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
        ]

    async def get_events(self) -> Dict[Control, Event]:
        with self.lock:
            return {key: value for (key, value) in self.last_events.items()}

    def register_control_callback(
        self,
        control: Control,
        triggers: List[EventType],
        function: Optional[ControlFunction]
    ):
        with self.lock:
            callbacks = self.callbacks.get(control, {})
            for trigger in triggers:
                if trigger == EventType.BUTTON_CHANGE:
                    callbacks[EventType.BUTTON_PRESS] = function
                    callbacks[EventType.BUTTON_RELEASE] = function
                else:
                    callbacks[trigger] = function
            self.callbacks[control] = callbacks


class ExampleGantry(Gantry):

    def __init__(
        self,
        name: str,
        position: List[float],
        lengths: List[float]
    ):
        self.position = position
        self.lengths = lengths
        self.is_stopped = True
        super().__init__(name)

    async def get_position(self) -> List[float]:
        return self.position

    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None
    ):
        self.position = positions
        self.is_stopped = False

    async def get_lengths(self) -> List[float]:
        return self.lengths

    async def stop(self):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped


class ExampleGPS(GPS):

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


class ExampleGripper(Gripper):

    def __init__(self, name: str):
        self.opened = False
        self.is_stopped = True
        super().__init__(name)

    async def open(self):
        self.opened = True
        self.is_stopped = False

    async def grab(self) -> bool:
        self.opened = False
        self.is_stopped = False
        return random.choice([True, False])

    async def stop(self):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped


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

    async def read_magnetometer(self) -> Magnetometer:
        return Magnetometer(
            x_gauss=random.random(),
            y_gauss=random.random(),
            z_gauss=random.random()
        )


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
        return Motor.Features(position_reporting=True)

    async def stop(self):
        await self.set_power(0)

    async def is_powered(self) -> bool:
        return self.powered

    async def is_moving(self):
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
        self.is_stopped = True
        super().__init__(name)

    async def move(self, angle: int):
        self.angle = angle
        self.is_stopped = False

    async def get_position(self) -> int:
        return self.angle

    async def stop(self):
        self.is_stopped = True

    async def is_moving(self):
        return not self.is_stopped
