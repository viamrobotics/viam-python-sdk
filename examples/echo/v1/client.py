import asyncio
import sys

from viam.proto.rpc.examples.echo import (
    EchoBiDiRequest,
    EchoMultipleRequest,
    EchoRequest,
    EchoServiceStub,
)
from viam.rpc.dial import DialOptions, dial


async def echo(msg: str):
    opts = DialOptions(insecure=True, disable_webrtc=True)
    async with await dial("127.0.0.1:8080", opts) as channel:
        service = EchoServiceStub(channel.channel)

        # Simple Echo
        request = EchoRequest(message=msg)
        response = await service.Echo(request)
        print(f"Echo response received: {response.message}")

        # Echo Multiple (Unary Stream)
        request = EchoMultipleRequest(message=msg)
        async with service.EchoMultiple.open() as stream:
            await stream.send_message(request, end=True)
            replies = [reply.message async for reply in stream]
            print(f"Echo Multiple response received: {replies}")

        # Echo BiDi (Stream Stream)
        requests = [EchoBiDiRequest(message=f"First message: {msg}"), EchoBiDiRequest(message=f"Second message: {msg}")]
        responses = await service.EchoBiDi(requests)
        print("Received Echo BiDi response: " + f"{[response.message for response in responses]}")


if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "foo"
    asyncio.run(echo(msg))
