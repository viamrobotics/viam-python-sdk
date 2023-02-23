import asyncio
import sys

from viam.module.module import Module

from .gizmo import Gizmo, MyGizmo


async def main(address: str):

    module = Module(address)
    await module.start()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Need socket path as command line argument")

    asyncio.run(main(sys.argv[1]))
