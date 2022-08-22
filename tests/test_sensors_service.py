import pytest
from grpclib.testing import ChannelFor

from viam.proto.api.common import ResourceName
from viam.proto.api.service.sensors import Readings
from viam.services.sensors import SensorsServiceClient
from viam.utils import primitive_to_value

from .mocks.services import MockSensorsService

SENSORS = [
    ResourceName(namespace="test", type="component", subtype="sensor", name="sensor0"),
    ResourceName(namespace="test", type="component", subtype="sensor", name="sensor1"),
    ResourceName(namespace="test", type="component", subtype="sensor", name="sensor2"),
    ResourceName(namespace="test", type="component", subtype="sensor", name="sensor3"),
]

READINGS = [
    Readings(
        name=ResourceName(namespace="test", type="component", subtype="sensor", name="sensor0"), readings={"a": primitive_to_value(1)}
    ),
    Readings(
        name=ResourceName(namespace="test", type="component", subtype="sensor", name="sensor1"), readings={"b": primitive_to_value(2)}
    ),
    Readings(
        name=ResourceName(namespace="test", type="component", subtype="sensor", name="sensor2"), readings={"c": primitive_to_value(3)}
    ),
    Readings(
        name=ResourceName(namespace="test", type="component", subtype="sensor", name="sensor3"), readings={"d": primitive_to_value(4)}
    ),
]


@pytest.fixture(scope="function")
def service() -> MockSensorsService:
    return MockSensorsService(SENSORS, READINGS)


class TestClient:
    @pytest.mark.asyncio
    async def test_get_sensors(self, service: MockSensorsService):
        async with ChannelFor([service]) as channel:
            client = SensorsServiceClient(channel)
            sensors = await client.get_sensors()
            assert sensors == SENSORS

    @pytest.mark.asyncio
    async def test_get_readings(self, service: MockSensorsService):
        async with ChannelFor([service]) as channel:
            client = SensorsServiceClient(channel)
            sensors = [
                ResourceName(namespace="test", type="component", subtype="sensor", name="sensor1"),
                ResourceName(namespace="test", type="component", subtype="sensor", name="sensor2"),
            ]
            readings = await client.get_readings(sensors)
            assert readings == READINGS
            assert service.sensors_for_readings == sensors
