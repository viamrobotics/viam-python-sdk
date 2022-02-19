import asyncio

from viam.rpc.dial import DialOptions, dial_direct
from viam.proto.api.component.servo import (
    ServoServiceStub,
    ServoServiceMoveRequest,
    ServoServiceGetPositionRequest, ServoServiceGetPositionResponse
)


async def client():
    opts = DialOptions(insecure=True)
    async with await dial_direct("localhost:9090", opts) as channel:

        """
        #### SERVO ####
        """
        service = ServoServiceStub(channel)

        request = ServoServiceMoveRequest(name="servo0", angle_deg=20)
        response = await service.Move(request)
        print('Response received')

        request = ServoServiceGetPositionRequest(name="servo0")
        response: ServoServiceGetPositionResponse \
            = await service.GetPosition(request)
        print(f'Response received: {response.position_deg}')


if __name__ == '__main__':
    asyncio.run(client())
