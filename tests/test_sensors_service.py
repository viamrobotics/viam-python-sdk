import pytest
from grpclib.testing import ChannelFor

from viam.proto.common import GeoPoint, Orientation, ResourceName, Vector3
from viam.proto.service.sensors import Readings
from viam.services.sensors import SensorsServiceClient
from viam.utils import primitive_to_value

from .mocks.services import MockSensorsService

SENSORS = [
    ResourceName(namespace="test", type="component", subtype="sensor", name="sensor0"),
    ResourceName(namespace="test", type="component", subtype="sensor", name="sensor1"),
    ResourceName(namespace="test", type="component", subtype="sensor", name="sensor2"),
    ResourceName(namespace="test", type="component", subtype="sensor", name="sensor3"),
]

ANGVEL = Vector3(x=0.1, y=2.3, z=4.5)
VEC3 = Vector3(x=6.7, y=8.9, z=10.11)
POINT = GeoPoint(latitude=123.45, longitude=678.9)
ORIENTATION = Orientation(o_x=1, o_y=2, o_z=3, theta=4)

READINGS = [
    Readings(
        name=ResourceName(namespace="test", type="component", subtype="sensor", name="sensor0"),
        readings={"a": primitive_to_value({"_type": "angular_velocity", "x": ANGVEL.x, "y": ANGVEL.y, "z": ANGVEL.z})},
    ),
    Readings(
        name=ResourceName(namespace="test", type="component", subtype="sensor", name="sensor1"),
        readings={"b": primitive_to_value({"_type": "vector3", "x": VEC3.x, "y": VEC3.y, "z": VEC3.z})},
    ),
    Readings(
        name=ResourceName(namespace="test", type="component", subtype="sensor", name="sensor2"),
        readings={"c": primitive_to_value({"_type": "geopoint", "lat": POINT.latitude, "lng": POINT.longitude})},
    ),
    Readings(
        name=ResourceName(namespace="test", type="component", subtype="sensor", name="sensor3"),
        readings={
            "d": primitive_to_value(
                {
                    "ox": ORIENTATION.o_x,
                    "oy": ORIENTATION.o_y,
                    "oz": ORIENTATION.o_z,
                    "theta": ORIENTATION.theta,
                    "_type": "orientation_vector_degrees",
                }
            )
        },
    ),
]

SENSOR_SERVICE_NAME = "sensors1"


@pytest.fixture(scope="function")
def service() -> MockSensorsService:
    return MockSensorsService(SENSORS, READINGS)


class TestClient:
    @pytest.mark.asyncio
    async def test_get_sensors(self, service: MockSensorsService):
        async with ChannelFor([service]) as channel:
            client = SensorsServiceClient(SENSOR_SERVICE_NAME, channel)
            extra = {"foo": "get_sensors"}
            sensors = await client.get_sensors(extra=extra)
            assert sensors == SENSORS
            assert service.extra == extra

            sensors = await client.get_sensors()
            assert sensors == SENSORS
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_get_readings(self, service: MockSensorsService):
        async with ChannelFor([service]) as channel:
            client = SensorsServiceClient(SENSOR_SERVICE_NAME, channel)
            sensors = [
                ResourceName(namespace="test", type="component", subtype="sensor", name="sensor1"),
                ResourceName(namespace="test", type="component", subtype="sensor", name="sensor2"),
            ]
            extra = {"foo": "get_readings"}
            readings = await client.get_readings(sensors, extra=extra)
            assert readings == {
                ResourceName(namespace="test", type="component", subtype="sensor", name="sensor0"): {"a": ANGVEL},
                ResourceName(namespace="test", type="component", subtype="sensor", name="sensor1"): {"b": VEC3},
                ResourceName(namespace="test", type="component", subtype="sensor", name="sensor2"): {"c": POINT},
                ResourceName(namespace="test", type="component", subtype="sensor", name="sensor3"): {"d": ORIENTATION},
            }
            assert service.sensors_for_readings == sensors
            assert service.extra == extra
