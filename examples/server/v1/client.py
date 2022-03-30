import asyncio
import typing
from random import randint

from viam.components.camera import CameraClient
from viam.components.imu import IMUClient
from viam.components.servo import ServoClient
from viam.proto.api.service.metadata import (MetadataServiceStub,
                                             ResourcesRequest,
                                             ResourcesResponse)
from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           StatusServiceStub)
from viam.rpc.dial import DialOptions, dial_direct


async def client():
    opts = DialOptions(insecure=True)
    async with await dial_direct('localhost:9090', opts) as channel:

        response: typing.Any

        print('\n#### METADATA ####')
        service = MetadataServiceStub(channel)
        request = ResourcesRequest()
        response = await service.Resources(request)
        r = typing.cast(ResourcesResponse, response)
        print(f'Metadata response received: {r.resources}')

        print('\n#### ROBOT ####')
        service = StatusServiceStub(channel)
        request = GetStatusRequest()
        response = await service.GetStatus(request)
        r = typing.cast(GetStatusResponse, response)
        print(f'Robot status response received: {r.status}')

        print('\n#### IMU ####')
        client = IMUClient(name='imu0', channel=channel)

        acceleration = await client.read_acceleration()
        print(f'IMU response received: acceleration is {acceleration}')

        angular_velocity = await client.read_angular_velocity()
        print(
            f'IMU response received: angular velocity is {angular_velocity}')

        orientation = await client.read_orientation()
        print(f'IMU response received: orientation is {orientation}')

        print('\n#### SERVO ####')
        client = ServoClient(name='servo0', channel=channel)

        pos = randint(0, 180)
        await client.move(pos)
        print(f'Response received: moved to position {pos}')

        position_deg = await client.get_position()
        print(
            f'Response received: current position is {position_deg}'
        )

        print('\n#### CAMERA ####')
        client = CameraClient('camera0', channel)
        img = await client.get_frame()
        img.show()
        await asyncio.sleep(1)
        img.close()


if __name__ == '__main__':
    asyncio.run(client())
