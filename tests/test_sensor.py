from grpclib.testing import ChannelFor
import pytest

from viam.components.resource_manager import ResourceManager
from viam.components.sensor import SensorService
from viam.proto.api.component.sensor import (
    SensorServiceStub,
    GetReadingsRequest, GetReadingsResponse,
)
from viam.utils import new_value

from .mocks.components import MockSensor


class TestSensor:

    sensor = MockSensor(name='sensor', result=[1, 2, 3])

    @pytest.mark.asyncio
    async def test_get_readings(self):
        readings = await self.sensor.get_readings()
        assert readings == [1, 2, 3]


class TestService:

    name = 'sensor'
    readings = [1, 2, 3]
    sensor = MockSensor(name=name, result=readings)
    manager = ResourceManager([sensor])
    service = SensorService(manager)

    @pytest.mark.asyncio
    async def test_get_readings(self):
        async with ChannelFor([self.service]) as channel:
            client = SensorServiceStub(channel)
            request = GetReadingsRequest(name=self.name)
            result: GetReadingsResponse = await client.GetReadings(request)
            value_readings = []
            for reading in self.readings:
                value_readings.append(new_value(reading))
            assert list(result.readings) == value_readings
