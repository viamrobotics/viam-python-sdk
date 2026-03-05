import asyncio
import sys

from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions
from viam.components.sensor import Sensor


async def connect(machine_url: str, api_key_id: str, api_key: str):
    # opts = RobotClient.Options.with_api_key(api_key=api_key_id, api_key_id=api_key)
    opts = RobotClient.Options(dial_options=DialOptions(insecure=True, disable_webrtc=True))
    return await RobotClient.at_address(machine_url, opts)


async def main(machine_url: str,api_key_id: str, api_key: str):
    robot = await connect(machine_url, api_key_id, api_key)

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
    if len(args) < 3:
        raise ValueError("Usage: python client.py <machine_url> <api_key_id> <api_key>")
    asyncio.run(main(args[0], args[1], args[2]))
