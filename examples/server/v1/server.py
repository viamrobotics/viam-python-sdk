import asyncio
import logging
from viam.rpc.server import Server

from .components import (
    ExampleIMU,
    ExampleBase,
    ExampleMotor,
    ExamplePoseTracker,
    ExampleSensor,
    ExampleServo
)


async def run():
    my_base = ExampleBase('base0')
    my_imu = ExampleIMU('imu0')
    my_motor = ExampleMotor('motor0')
    my_pose_tracker = ExamplePoseTracker('pose_tracker0')
    my_sensor = ExampleSensor('sensor0')
    my_servo = ExampleServo('servo0')
    server = Server(components=[
        my_base,
        my_imu,
        my_motor,
        my_pose_tracker,
        my_sensor,
        my_servo,
    ])
    await server.serve(log_level=logging.DEBUG)


if __name__ == '__main__':
    asyncio.run(run())
