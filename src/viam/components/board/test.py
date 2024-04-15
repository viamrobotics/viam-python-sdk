import asyncio

import viam
from viam.components.board import Board, Tick
from viam.components.sensor import Sensor
from viam.robot.client import RobotClient


async def connect():
    opts = RobotClient.Options.with_api_key(api_key="fuz2myr6r1528mb6ayf5i3di17g6pevs", api_key_id="3074554d-dd14-4e53-98b4-510a1ca58fe5")
    return await RobotClient.at_address("penta-main.4hk6rzx88z.viam.cloud", opts)


async def main():
    machine = await connect()

    print("Resources:")
    print(machine.resource_names)

    async def callback(tick: Tick) -> bool:
        print("in callback!")
        return False

    # Note that the pin supplied is a placeholder. Please change this to a valid pin you are using.
    # local
    local = Board.from_robot(machine, "local")
    local.stream_ticks(interrupts=["11"], callback=callback)

    # sensor-1
    sensor_1 = Sensor.from_robot(machine, "sensor-1")
    sensor_1_return_value = await sensor_1.get_readings()
    print(f"sensor-1 get_readings return value: {sensor_1_return_value}")

    # Don't forget to close the machine when you're done!
    await machine.close()


if __name__ == "__main__":
    asyncio.run(main())
