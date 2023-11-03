import asyncio

from viam import logging
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.sensor import Sensor


async def connect():
    creds = Credentials(type="<your authentication type here>", payload="<your authentication payload here>")
    opts = RobotClient.Options(refresh_interval=0, dial_options=DialOptions(credentials=creds), log_level=logging.DEBUG)
    return await RobotClient.at_address("<your robot uri here>", opts)


async def main():
    robot = await connect()

    print("Resources:")
    print(robot.resource_names)

    sensor = Sensor.from_robot(robot, name="sensor1")
    reading = await sensor.get_readings()
    print(f"The reading is {reading}")

    response = await sensor.do_command({"hello": "world"})
    print(f"The response is {response}")

    await robot.close()


if __name__ == "__main__":
    asyncio.run(main())
