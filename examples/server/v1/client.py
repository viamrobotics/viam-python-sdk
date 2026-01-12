import asyncio

from PIL.Image import Image

from viam.components.arm import Arm, Pose
from viam.components.base import Base, Vector3
from viam.components.camera import Camera
from viam.components.encoder import Encoder
from viam.components.motor import Motor
from viam.media.utils.pil import viam_to_pil_image
from viam.media.video import CameraMimeType
from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions


async def client():
    opts = RobotClient.Options(dial_options=DialOptions(insecure=True))
    async with await RobotClient.at_address("localhost:9090", opts) as robot:
        print("\n#### RESOURCES ####")
        print(f"Resources: {robot.resource_names}")

        print("\n#### STATUS ####")
        print(f"Robot status response received: {await robot.get_status()}")

        print("\n#### ARM ####")
        arm = Arm.from_robot(robot, "arm0")
        await arm.move_to_position(Pose(x=0, y=1, z=2, o_x=3, o_y=4, o_z=5, theta=6))
        position = await arm.get_end_position()
        print(f"Arm position is: {position}")

        print("\n#### BASE ####")
        base = Base.from_robot(robot, "base0")
        await base.set_velocity(Vector3(x=0, y=1, z=2), Vector3(x=3, y=4, z=5))
        await base.stop()

        print("\n#### CAMERA ####")
        camera = Camera.from_robot(robot, "camera0")
        images, _ = await camera.get_images()
        img = viam_to_pil_image(images[0])
        assert isinstance(img, Image)
        img.show()
        await asyncio.sleep(1)
        img.close()

        print("\n#### ENCODER ####")
        encoder = Encoder.from_robot(robot, "encoder0")
        await encoder.get_position()

        print("\n#### MOTOR ####")
        motor = Motor.from_robot(robot, "motor0")
        await motor.go_for(rpm=100, revolutions=10)
        await motor.stop()


if __name__ == "__main__":
    asyncio.run(client())
