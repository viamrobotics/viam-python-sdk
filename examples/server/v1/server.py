import asyncio
import logging
import sys

from viam.proto.common import GeoPoint, Orientation, Vector3
from viam.rpc.server import Server

from .components import (
    ExampleAnalog,
    ExampleArm,
    ExampleAudioIn,
    ExampleAudioOut,
    ExampleBase,
    ExampleBoard,
    ExampleCamera,
    ExampleDigitalInterrupt,
    ExampleEncoder,
    ExampleGantry,
    ExampleGPIOPin,
    ExampleGripper,
    ExampleMotor,
    ExampleMovementSensor,
    ExamplePoseTracker,
    ExampleSensor,
    ExampleServo,
    MovementSensor,
)
from .services import ExampleMLModel, ExampleSLAM


async def run(host: str, port: int, log_level: int):
    my_arm = ExampleArm("arm0")
    my_audio_in = ExampleAudioIn("audio_in0")
    my_audio_out = ExampleAudioOut("audio_out0")
    my_base = ExampleBase("base0")
    my_board = ExampleBoard(
        name="board",
        analogs={
            "reader1": ExampleAnalog("reader1", 3),
        },
        digital_interrupts={
            "interrupt1": ExampleDigitalInterrupt("interrupt1"),
        },
        gpio_pins={
            "pin1": ExampleGPIOPin("pin1"),
        },
    )
    my_camera = ExampleCamera("camera0")
    my_encoder = ExampleEncoder("encoder0")
    my_gantry = ExampleGantry("gantry0", [1, 2, 3], [4, 5, 6])
    my_gripper = ExampleGripper("gripper0")
    my_mlmodel = ExampleMLModel("mlmodel0")
    my_motor = ExampleMotor("motor0")
    my_movement_sensor = ExampleMovementSensor(
        "movement_sensor0",
        GeoPoint(latitude=40.664679865782624, longitude=-73.97668056188789),
        15,
        Vector3(x=1, y=2, z=3),
        Vector3(x=1, y=2, z=3),
        Vector3(x=1, y=2, z=3),
        182,
        Orientation(o_x=1, o_y=2, o_z=3, theta=5),
        MovementSensor.Properties(
            linear_acceleration_supported=False,
            linear_velocity_supported=False,
            angular_velocity_supported=True,
            orientation_supported=False,
            position_supported=True,
            compass_heading_supported=False,
        ),
        {"foo": 0.1, "bar": 2.0, "baz": 3.14},
    )
    my_pose_tracker = ExamplePoseTracker("pose_tracker0")
    my_sensor = ExampleSensor("sensor0")
    my_servo = ExampleServo("servo0")
    my_slam = ExampleSLAM("slam0")
    server = Server(
        resources=[
            my_arm,
            my_audio_in,
            my_audio_out,
            my_base,
            my_board,
            my_camera,
            my_encoder,
            my_gantry,
            my_gripper,
            my_mlmodel,
            my_motor,
            my_movement_sensor,
            my_pose_tracker,
            my_sensor,
            my_servo,
            my_slam,
        ]
    )
    await server.serve(host=host, port=port, log_level=log_level)


if __name__ == "__main__":
    host = "localhost"
    port = 9090
    log_level = logging.DEBUG
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
        level = sys.argv[3]
        if level.lower() == "q" or level.lower() == "quiet":
            log_level = logging.FATAL
    except (IndexError, ValueError):
        pass
    asyncio.run(run(host, port, log_level))
