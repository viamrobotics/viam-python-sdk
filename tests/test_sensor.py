import pytest
from grpclib import GRPCError
from grpclib.testing import ChannelFor

from viam.resource.manager import ResourceManager
from viam.components.sensor import SensorClient
from viam.components.sensor.service import SensorRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest
from viam.proto.component.sensor import (
    GetReadingsRequest,
    GetReadingsResponse,
    SensorServiceStub,
)
from viam.utils import dict_to_struct, struct_to_dict, primitive_to_value

from . import loose_approx
from .mocks.components import MockSensor

READINGS = {"a": 1, "b": 2, "c": 3}
EXTRA_PARAMS = {"foo": "bar", "baz": [1, 2, 3]}


@pytest.fixture(scope="function")
def sensor() -> MockSensor:
    return MockSensor(name="sensor", result=READINGS)


class TestSensor:
    @pytest.mark.asyncio
    async def test_get_readings(self, sensor):
        assert sensor.extra is None
        readings = await sensor.get_readings(extra=EXTRA_PARAMS, timeout=1.23)
        assert readings == READINGS
        assert sensor.extra == EXTRA_PARAMS
        assert sensor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_do(self, sensor):
        command = {"command": "args"}
        resp = await sensor.do_command(command)
        assert resp == {"command": command}


@pytest.fixture(scope="function")
def manager(sensor) -> ResourceManager:
    return ResourceManager([sensor])


@pytest.fixture(scope="function")
def service(manager) -> SensorRPCService:
    return SensorRPCService(manager)


class TestService:
    @pytest.mark.asyncio
    async def test_get_readings(self, sensor, service):
        async with ChannelFor([service]) as channel:
            client = SensorServiceStub(channel)
            request = GetReadingsRequest(name=sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert sensor.extra is None
            result: GetReadingsResponse = await client.GetReadings(request, timeout=2.34)
            assert result.readings == {key: primitive_to_value(value) for (key, value) in READINGS.items()}
            assert sensor.extra == EXTRA_PARAMS
            assert sensor.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_do(self, sensor: MockSensor, service: SensorRPCService):
        async with ChannelFor([service]) as channel:
            client = SensorServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=sensor.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    @pytest.mark.asyncio
    async def test_get_geometries(self, service: SensorRPCService):
        async with ChannelFor([service]) as channel:
            client = SensorServiceStub(channel)
            request = GetGeometriesRequest()
            with pytest.raises(GRPCError, match=r"Method [a-zA-Z]+ not implemented"):
                await client.GetGeometries(request)


class TestClient:
    @pytest.mark.asyncio
    async def test_get_readings(self, sensor, service):
        async with ChannelFor([service]) as channel:
            client = SensorClient(sensor.name, channel)
            assert sensor.extra is None
            value_readings = await client.get_readings(timeout=3.45, extra=EXTRA_PARAMS)
            assert READINGS == value_readings
            assert sensor.extra == EXTRA_PARAMS
            assert sensor.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_do(self, sensor, manager, service):
        async with ChannelFor([service]) as channel:
            client = SensorClient(sensor.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}
