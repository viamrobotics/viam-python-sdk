#!/usr/bin/env python3

import asyncio
from viam.components.motor import Motor
from viam.resource.easy_resource import EasyResource, stub_model
from viam.module.module import Module


@stub_model
class MyMotor(Motor, EasyResource):
    MODEL = "viam:motor:easy-resource-example"

    async def is_moving(self) -> bool:
        return False

    async def stop(self, **kwargs):
        pass


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
