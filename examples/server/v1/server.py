import asyncio
import logging
from viam.rpc.server import Server

from .components import (
    IMU,
    Motor,
    Sensor,
    Servo
)


async def run():
    my_imu = IMU('imu0')
    my_motor = Motor('motor0')
    my_sensor = Sensor('sensor0')
    my_servo = Servo('servo0')
    server = Server(components=[
        my_imu,
        my_motor,
        my_sensor,
        my_servo,
    ])
    await server.serve(log_level=logging.DEBUG)


if __name__ == '__main__':
    asyncio.run(run())
