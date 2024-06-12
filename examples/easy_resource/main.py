#!/usr/bin/env python3

import asyncio
from viam.components.sensor import Sensor
from viam.resource.easy_resource import EasyResource
from viam.module.module import Module

class MySensor(Sensor, EasyResource):
    MODEL = "viam:sensor:easy-resource-example"

    async def get_readings(self, **kwargs):
        return {"ok": True}

if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
