import asyncio
import sys

from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions
from viam.components.sensor import Sensor


async def connect(machine_url: str, api_key_id: str, api_key: str, local: bool = False):
    if local:
        opts = RobotClient.Options(dial_options=DialOptions(insecure=True, disable_webrtc=True))
    else:
        opts = RobotClient.Options.with_api_key(api_key=api_key, api_key_id=api_key_id)
    return await RobotClient.at_address(machine_url, opts)


async def main(machine_url: str, api_key_id: str, api_key: str, local: bool = False):
    robot = await connect(machine_url, api_key_id, api_key, local)

    print("Resources:")
    print(robot.resource_names)

    sensor = Sensor.from_robot(robot, name="sensor1")
    reading = await sensor.get_readings()
    print(f"The reading is {reading}")

    response = await sensor.do_command({"hello": "world"})
    print(f"The response is {response}")

    await robot.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) >= 3:
        asyncio.run(main(args[0], args[1], args[2], local=True))
    else:
        # Update these values with your app.viam.com credentials
        asyncio.run(main(
            "<your machine url>",
            "<your api key id>",
            "<your api key>",
        ))
