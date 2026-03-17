import pytest
from grpclib.testing import ChannelFor

from viam.components.sensor import SensorClient
from viam.components.sensor.service import SensorRPCService
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetReadingsRequest,
    GetReadingsResponse,
)
from viam.proto.component.sensor import SensorServiceStub
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, sensor_readings_value_to_native, struct_to_dict

from . import expected_grpc_timeout
from .mocks.components import GEOMETRIES, MockSensor

READINGS = {"a": 1, "b": 2, "c": 3}
EXTRA_PARAMS = {"foo": "bar", "baz": [1, 2, 3]}


@pytest.fixture(scope="function")
def sensor() -> MockSensor:
    return MockSensor(name="sensor", result=READINGS)


class TestSensor:
    async def test_get_readings(self, sensor):
        assert sensor.extra is None
        readings = await sensor.get_readings(extra=EXTRA_PARAMS, timeout=1.23)
        assert readings == READINGS
        assert sensor.extra == EXTRA_PARAMS
        assert sensor.timeout == expected_grpc_timeout(1.23)

    async def test_do(self, sensor):
        command = {"command": "args"}
        resp = await sensor.do_command(command)
        assert resp == {"command": command}

    async def test_get_geometries(self, sensor):
        geometries = await sensor.get_geometries()
        assert geometries == GEOMETRIES


@pytest.fixture(scope="function")
def manager(sensor) -> ResourceManager:
    return ResourceManager([sensor])


@pytest.fixture(scope="function")
def service(manager) -> SensorRPCService:
    return SensorRPCService(manager)


class TestService:
    async def test_get_readings(self, sensor, service):
        async with ChannelFor([service]) as channel:
            client = SensorServiceStub(channel)
            request = GetReadingsRequest(name=sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert sensor.extra is None
            result: GetReadingsResponse = await client.GetReadings(request, timeout=2.34)
            assert sensor_readings_value_to_native(result.readings) == READINGS
            assert sensor.extra == EXTRA_PARAMS
            assert sensor.timeout == expected_grpc_timeout(2.34)

    async def test_do(self, sensor: MockSensor, service: SensorRPCService):
        async with ChannelFor([service]) as channel:
            client = SensorServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=sensor.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_geometries(self, sensor: MockSensor, service: SensorRPCService):
        async with ChannelFor([service]) as channel:
            client = SensorServiceStub(channel)
            request = GetGeometriesRequest(name=sensor.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    async def test_get_readings(self, sensor, service):
        async with ChannelFor([service]) as channel:
            client = SensorClient(sensor.name, channel)
            assert sensor.extra is None
            value_readings = await client.get_readings(timeout=3.45, extra=EXTRA_PARAMS)
            assert READINGS == value_readings
            assert sensor.extra == EXTRA_PARAMS
            assert sensor.timeout == expected_grpc_timeout(3.45)

    async def test_do(self, sensor, manager, service):
        async with ChannelFor([service]) as channel:
            client = SensorClient(sensor.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    async def test_get_geometries(self, sensor, service):
        async with ChannelFor([service]) as channel:
            client = SensorClient(sensor.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES
