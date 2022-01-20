import asyncio

from grpclib.utils import graceful_exit
from grpclib.server import Server, Stream

from gen.proto.rpc.examples.echo.v1.echo_pb2 import (
    EchoRequest, EchoResponse,
    EchoMultipleRequest, EchoMultipleResponse,
    EchoBiDiRequest, EchoBiDiResponse
)
from gen.proto.rpc.examples.echo.v1.echo_grpc import EchoServiceBase


class EchoServer(EchoServiceBase):

    # UNARY_UNARY - simple RPC
    async def Echo(
        self,
        stream: Stream[EchoRequest, EchoResponse],
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        message = request.message
        await stream.send_message(EchoResponse(message=message))

    # UNARY_STREAM - response streaming RPC
    async def EchoMultiple(
        self,
        stream: Stream[EchoMultipleRequest, EchoMultipleResponse],
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        for c in request.message:
            await stream.send_message(EchoMultipleResponse(message=c))

    # STREAM_STREAM - bidirectional streaming RPC
    async def EchoBiDi(
        self,
        stream: Stream[EchoBiDiRequest, EchoBiDiResponse],
    ) -> None:
        async for request in stream:
            for c in request.message:
                await stream.send_message(EchoBiDiResponse(message=c))


async def main(*, host: str = '127.0.0.1', port: int = 8080) -> None:
    server = Server([EchoServer()])
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
