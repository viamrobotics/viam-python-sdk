import asyncio
import logging

from viam.rpc.server import Server
from viam.components.gps import GPS

from .components import (ExampleAnalogReader, ExampleArm, ExampleBase,
                         ExampleBoard, ExampleCamera, ExampleDigitalInterrupt,
                         ExampleGantry, ExampleGPIOPin, ExampleGPS, ExampleIMU,
                         ExampleMotor, ExamplePoseTracker, ExampleSensor,
                         ExampleServo)


async def run():
    my_arm = ExampleArm('arm0')
    my_base = ExampleBase('base0')
    my_board = ExampleBoard(
        name="board",
        analog_readers={
            'reader1': ExampleAnalogReader('reader1', 3),
        },
        digital_interrupts={
            'interrupt1': ExampleDigitalInterrupt('interrupt1'),
        },
        gpio_pins={
            'pin1': ExampleGPIOPin('pin1'),
        },
    )
    my_camera = ExampleCamera('camera0')
    my_gantry = ExampleGantry('gantry0', [1, 2, 3], [4, 5, 6])
    my_gps = ExampleGPS(
        name='gps1',
        location=GPS.Point(40.664679865782624, -73.97668056188789),
        altitude=15,
        speed=1341.12
    )
    my_imu = ExampleIMU('imu0')
    my_motor = ExampleMotor('motor0')
    my_pose_tracker = ExamplePoseTracker('pose_tracker0')
    my_sensor = ExampleSensor('sensor0')
    my_servo = ExampleServo('servo0')
    server = Server(components=[
        my_arm,
        my_base,
        my_board,
        my_camera,
        my_gantry,
        my_gps,
        my_imu,
        my_motor,
        my_pose_tracker,
        my_sensor,
        my_servo,
    ])
    await server.serve(log_level=logging.DEBUG)


if __name__ == '__main__':
    asyncio.run(run())
