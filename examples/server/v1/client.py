import asyncio
from random import randint

from viam.components.camera import Camera
from viam.components.imu import IMU
from viam.components.servo import Servo
from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions
from viam.services.types import ServiceType


async def client():
    opts = RobotClient.Options(dial_options=DialOptions(insecure=True))
    async with await RobotClient.at_address('localhost:9090', opts) as robot:

        print('\n#### RESOURCES ####')
        print(f'Resources: {robot.resource_names}')

        print('\n#### STATUS ####')
        service = robot.get_service(ServiceType.STATUS)
        print(f'Robot status response received: {service.get_status()}')

        print('\n#### IMU ####')
        imu = IMU.from_robot(robot, 'imu0')
        acceleration = await imu.read_acceleration()
        print(f'IMU response received: acceleration is {acceleration}')

        angular_velocity = await imu.read_angular_velocity()
        print(f'IMU response received: angular velocity is {angular_velocity}')

        orientation = await imu.read_orientation()
        print(f'IMU response received: orientation is {orientation}')

        print('\n#### SERVO ####')
        servo = Servo.from_robot(robot, 'servo0')

        pos = randint(0, 180)
        await servo.move(pos)
        print(f'Response received: moved to position {pos}')

        position_deg = await servo.get_position()
        print(f'Response received: current position is {position_deg}')

        print('\n#### CAMERA ####')
        camera = Camera.from_robot(robot, 'camera0')
        img = await camera.get_frame()
        img.show()
        await asyncio.sleep(1)
        img.close()


if __name__ == '__main__':
    asyncio.run(client())
