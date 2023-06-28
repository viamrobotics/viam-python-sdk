import asyncio
from viam.rpc.server import Server

from module_arm import ModuleArm


async def main():
    srv = Server([ModuleArm("moduleArm")])
    await srv.serve()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        pass
