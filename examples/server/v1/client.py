import asyncio
from random import randint

from viam.rpc.dial import DialOptions, dial_direct
from viam.proto.api.component.servo import (
    ServoServiceStub,
    MoveRequest,
    GetPositionRequest, GetPositionResponse
)


async def client():
    opts = DialOptions(insecure=True)
    async with await dial_direct("localhost:9090", opts) as channel:

        """
        #### SERVO ####
        """
        service = ServoServiceStub(channel)

        pos = randint(0, 180)
        request = MoveRequest(
            name="servo0",
            angle_deg=pos
        )
        response = await service.Move(request)
        print(f'Response received: moved to position {pos}')

        request = GetPositionRequest(name="servo0")
        response: GetPositionResponse = await service.GetPosition(request)
        print(
            f'Response received: current position is {response.position_deg}'
        )


if __name__ == '__main__':
    asyncio.run(client())
