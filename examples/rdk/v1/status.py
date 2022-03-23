import asyncio

from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           StatusServiceStub)
from viam.rpc.dial import Credentials, DialOptions, dial_direct


async def test():
    creds = Credentials(
        "api-key",
        "supersecretkey"
    )
    opts = DialOptions(
        credentials=creds,
        allow_insecure_with_creds_downgrade=True
    )
    channel = await dial_direct("localhost:8080", opts)
    service = StatusServiceStub(channel)
    resp: GetStatusResponse = await service.GetStatus(GetStatusRequest())
    print(resp)
    channel.close()


if __name__ == '__main__':
    asyncio.run(test())
