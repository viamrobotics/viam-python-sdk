import asyncio
import os

from PIL.Image import Image

from viam.components.arm import Arm, Pose
from viam.components.audio_in import AudioIn
from viam.components.audio_out import AudioOut, AudioInfo
from viam.components.base import Base, Vector3
from viam.components.camera import Camera
from viam.components.encoder import Encoder
from viam.components.motor import Motor
from viam.media.video import CameraMimeType
from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions


async def client():
    opts = RobotClient.Options(dial_options=DialOptions(insecure=True))
    async with await RobotClient.at_address("localhost:9090", opts) as robot:
        print("\n#### RESOURCES ####")
        print(f"Resources: {robot.resource_names}")

        # print("\n#### STATUS ####")
        # print(f"Robot status response received: {await robot.get_status()}")


        audio = AudioIn.from_robot(robot, "audio_in0")

        try:
            stream = await audio.get_audio("pcm16", 10, 0)
            with open("audio.raw", "wb") as f:
                async for chunk in stream:
                    data = chunk.audio.audio_data
                    f.write(data)
                    f.flush()
            print("audio.raw written to", os.path.abspath("audio.raw"))
        except Exception as e:
            print("EXCEPYION")
            print(e)


        with open("output.wav", "rb") as f:
                audio_bytes = f.read()


        audioout = AudioOut.from_robot(robot, "audio_out0")
        await audioout.play(audio_bytes, AudioInfo(codec="pcm16", sample_rate_hz=44100, num_channels=2))


        print("here stream done")

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
        img = await camera.get_image(mime_type=CameraMimeType.PNG)
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
