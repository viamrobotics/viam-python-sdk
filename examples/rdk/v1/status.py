import asyncio

from viam.gen.proto.api.v1.robot_grpc import RobotServiceStub
from viam.gen.proto.api.v1.robot_pb2 import StatusRequest

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
    service = RobotServiceStub(channel)
    resp = await service.Status(StatusRequest())
    print(resp)
    channel.close()


if __name__ == '__main__':
    asyncio.run(test())
