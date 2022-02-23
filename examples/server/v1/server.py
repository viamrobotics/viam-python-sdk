import asyncio
import logging
from viam.rpc.server import Server

from .components import Servo


async def run():
    my_servo = Servo("servo0")
    server = Server(components=[my_servo])
    await server.serve(log_level=logging.DEBUG)


if __name__ == '__main__':
    asyncio.run(run())
