import asyncio
import logging
import time

from PIL.Image import Image

from viam.components.arm import Arm, Pose
from viam.components.base import Base, Vector3
from viam.components.camera import Camera
from viam.components.motor import Motor
from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions, Credentials


async def client():
    opts = RobotClient.Options(
        dial_options=DialOptions(
            credentials=Credentials(type="robot-location-secret", payload="pem1epjv07fq2cz2z5723gq6ntuyhue5t30boohkiz3iqht4")
        ),
        check_connection_interval=1,
        log_level=logging.DEBUG,
    )
    async with await RobotClient.at_address("naveed-pi-main.60758fe0f6.viam.cloud", opts) as robot:
        while True:
            print(time.time())
            await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(client())
