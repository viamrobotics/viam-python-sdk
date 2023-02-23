import asyncio

from src.gizmo import Gizmo

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam import logging


async def connect():
    creds = Credentials(type="robot-location-secret", payload="pem1epjv07fq2cz2z5723gq6ntuyhue5t30boohkiz3iqht4")
    opts = RobotClient.Options(refresh_interval=0, dial_options=DialOptions(credentials=creds), log_level=logging.DEBUG)
    return await RobotClient.at_address("naveed-pi-main.60758fe0f6.viam.cloud", opts)


async def main():
    robot = await connect()

    print("Resources:")
    print(robot._manager.components)

    gizmo = Gizmo.from_robot(robot, name="gizmo1")
    print("gizmo: ", gizmo)
    resp = await gizmo.do_one("arg1")
    print(resp)

    # Don't forget to close the robot when you're done!
    await robot.close()


if __name__ == "__main__":
    asyncio.run(main())
