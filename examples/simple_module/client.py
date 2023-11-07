import asyncio

from viam.robot.client import RobotClient
from viam.components.sensor import Sensor


async def connect():
    opts = RobotClient.Options.with_api_key(api_key="<your api key here>", api_key_id="<your api key ID here>")
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
