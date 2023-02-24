import asyncio

from src.gizmo import Gizmo

from viam import logging
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions


async def connect():
    creds = Credentials(type="robot-location-secret", payload="<ROBOT_LOCATION_SECRET>")
    opts = RobotClient.Options(refresh_interval=0, dial_options=DialOptions(credentials=creds), log_level=logging.DEBUG)
    return await RobotClient.at_address("<ROBOT_ADDRESS>", opts)


async def main():
    robot = await connect()

    print("Resources:")
    print(robot.resource_names)

    gizmo = Gizmo.from_robot(robot, name="gizmo1")
    resp = await gizmo.do_one("arg1")
    print("do_one result:", resp)

    resp = await gizmo.do_one_client_stream(["arg1", "arg2", "arg3"])
    print("do_one_client_stream result:", resp)

    resp = await gizmo.do_two(False)
    print("do_two result:", resp)

    # Certain types of streams are not currently supported by the viam-rust-utils library that python uses internally.
    # If you are not using WebRTC, you can uncomment the following lines.

    # resp = await gizmo.do_one_server_stream("arg1")
    # print("do_one_server_stream result:", resp)

    # resp = await gizmo.do_one_bidi_stream(["arg1", "arg2", "arg3"])
    # print("do_one_bidi_stream result:", resp)

    await robot.close()


if __name__ == "__main__":
    asyncio.run(main())
