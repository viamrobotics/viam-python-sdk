import asyncio
from random import randint

from viam.rpc.dial import DialOptions, dial_direct
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

        """
        #### METADATA ####
        """
        service = MetadataServiceStub(channel)
        request = ResourcesRequest()
        resources_response: ResourcesResponse = \
            await service.Resources(request)
        print(f'Response received: {resources_response.resources}')

        """
        #### SERVO ####
        """
        service = ServoServiceStub(channel)

        pos = randint(0, 180)
        request = MoveRequest(
            name="servo0",
            angle_deg=pos
        )
        _ = await service.Move(request)
        print(f'Response received: moved to position {pos}')

        request = GetPositionRequest(name="servo0")
        servo_get_pos_response: GetPositionResponse = \
            await service.GetPosition(request)
        print(
            'Response received: current position is '
            f'{servo_get_pos_response.position_deg}'
        )


if __name__ == '__main__':
    asyncio.run(client())
