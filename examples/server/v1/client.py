import asyncio
from random import randint
import typing

from viam.rpc.dial import DialOptions, dial_direct
from viam.proto.api.component.imu import (
    IMUServiceStub,
    ReadAccelerationRequest, ReadAccelerationResponse,
    ReadAngularVelocityRequest, ReadAngularVelocityResponse,
    ReadOrientationRequest, ReadOrientationResponse
)
from viam.proto.api.robot import (
    RobotServiceStub,
    StatusRequest, StatusResponse
)
from viam.proto.api.component.servo import (
    ServoServiceStub,
    MoveRequest,
    GetPositionRequest, GetPositionResponse
)
from viam.proto.api.service.metadata import (
    MetadataServiceStub,
    ResourcesRequest, ResourcesResponse
)


async def client():
    opts = DialOptions(insecure=True)
    async with await dial_direct("localhost:9090", opts) as channel:

        response: typing.Any

        print('\n#### METADATA ####')
        service = MetadataServiceStub(channel)
        request = ResourcesRequest()
        response = await service.Resources(request)
        r = typing.cast(ResourcesResponse, response)
        print(f'Metadata response received: {r.resources}')

        print('\n#### ROBOT ####')
        service = RobotServiceStub(channel)
        request = StatusRequest()
        response = await service.Status(request)
        r = typing.cast(StatusResponse, response)
        print(f'Robot status response received: {r.status}')

        print('\n#### IMU ####')
        service = IMUServiceStub(channel)
        request = ReadAccelerationRequest(name="imu0")
        response = await service.ReadAcceleration(request)
        r = typing.cast(ReadAccelerationResponse, response)
        print(f'IMU response received: acceleration is {r.acceleration}')

        request = ReadAngularVelocityRequest(name="imu0")
        response = await service.ReadAngularVelocity(request)
        r = typing.cast(ReadAngularVelocityResponse, response)
        print(
            f'IMU response received: angular velocity is {r.angular_velocity}')

        request = ReadOrientationRequest(name="imu0")
        response = await service.ReadOrientation(request)
        r = typing.cast(ReadOrientationResponse, response)
        print(f'IMU response received: orientation is {r.orientation}')

        print('\n#### SERVO ####')
        service = ServoServiceStub(channel)

        pos = randint(0, 180)
        request = MoveRequest(
            name="servo0",
            angle_deg=pos
        )
        _ = await service.Move(request)
        print(f'Response received: moved to position {pos}')

        request = GetPositionRequest(name="servo0")
        response = await service.GetPosition(request)
        r = typing.cast(GetPositionResponse, response)
        print(
            f'Response received: current position is {r.position_deg}'
        )


if __name__ == '__main__':
    asyncio.run(client())
