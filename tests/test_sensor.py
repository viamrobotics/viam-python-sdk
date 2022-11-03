import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericService
from viam.components.resource_manager import ResourceManager
from viam.components.sensor import SensorClient
from viam.components.sensor.service import SensorService
from viam.proto.component.sensor import (
    GetReadingsRequest,
    GetReadingsResponse,
    SensorServiceStub,
)
from viam.utils import primitive_to_value

from . import loose_approx
from .mocks.components import MockSensor


class TestSensor:

    sensor = MockSensor(name="sensor", result={"a": 1, "b": 2, "c": 3})

    @pytest.mark.asyncio
    async def test_get_readings(self):
        readings = await self.sensor.get_readings(timeout=1.23)
        assert readings == {"a": 1, "b": 2, "c": 3}
        assert self.sensor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_do(self):
        with pytest.raises(NotImplementedError):
            await self.sensor.do_command({"command": "args"})


class TestService:

    name = "sensor"
    readings = {"a": 1, "b": 2, "c": 3}
    sensor = MockSensor(name=name, result=readings)
    manager = ResourceManager([sensor])
    service = SensorService(manager)

    @pytest.mark.asyncio
    async def test_get_readings(self):
        async with ChannelFor([self.service]) as channel:
            client = SensorServiceStub(channel)
            request = GetReadingsRequest(name=self.name)
            result: GetReadingsResponse = await client.GetReadings(request, timeout=2.34)
            assert result.readings == {key: primitive_to_value(value) for (key, value) in self.readings.items()}
            assert self.sensor.timeout == loose_approx(2.34)


class TestClient:

    name = "sensor"
    readings = {"a": 1, "b": 2, "c": 3}
    sensor = MockSensor(name=name, result=readings)
    manager = ResourceManager([sensor])
    service = SensorService(manager)

    @pytest.mark.asyncio
    async def test_get_readings(self):
        async with ChannelFor([self.service]) as channel:
            client = SensorClient(self.name, channel)
            value_readings = await client.get_readings(timeout=3.45)
            assert self.readings == value_readings
            assert self.sensor.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service, GenericService(self.manager)]) as channel:
            client = SensorClient(self.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do_command({"command": "args"})
