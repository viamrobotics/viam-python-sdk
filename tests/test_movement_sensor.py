import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericService
from viam.components.movement_sensor import (
    MovementSensor,
    MovementSensorClient,
    MovementSensorService,
)
from viam.components.resource_manager import ResourceManager
from viam.proto.api.common import GeoPoint, Orientation, Vector3
from viam.proto.api.component.movementsensor import (
    GetAccuracyRequest,
    GetAccuracyResponse,
    GetAngularVelocityRequest,
    GetAngularVelocityResponse,
    GetCompassHeadingRequest,
    GetCompassHeadingResponse,
    GetLinearVelocityRequest,
    GetLinearVelocityResponse,
    GetOrientationRequest,
    GetOrientationResponse,
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    MovementSensorServiceStub,
)

from .mocks.components import MockMovementSensor

COORDINATE = GeoPoint(latitude=40.664679865782624, longitude=-73.97668056188789)
ALTITUDE = 15
LINEAR_VELOCITY = Vector3(x=1, y=2, z=3)
ANGULAR_VELOCITY = Vector3(x=1, y=2, z=3)
HEADING = 182
ORIENTATION = Orientation(o_x=1, o_y=2, o_z=3, theta=5)
PROPERTIES = MovementSensor.Properties(
    linear_velocity_supported=False,
    angular_velocity_supported=True,
    orientation_supported=False,
    position_supported=True,
    compass_heading_supported=False,
)
ACCURACY = {"foo": 0.1, "bar": 2, "baz": 3.14}


@pytest.fixture(scope="function")
def movement_sensor() -> MovementSensor:
    return MockMovementSensor(
        "movement_sensor", COORDINATE, ALTITUDE, LINEAR_VELOCITY, ANGULAR_VELOCITY, HEADING, ORIENTATION, PROPERTIES, ACCURACY
    )


@pytest.fixture(scope="function")
def service(movement_sensor: MovementSensor) -> MovementSensorService:
    manager = ResourceManager([movement_sensor])
    return MovementSensorService(manager)


@pytest.fixture(scope="function")
def generic_service(movement_sensor: MovementSensor) -> GenericService:
    manager = ResourceManager([movement_sensor])
    return GenericService(manager)


class TestMovementSensor:
    @pytest.mark.asyncio
    async def test_get_position(self, movement_sensor: MovementSensor):
        (coord, alt) = await movement_sensor.get_position()
        assert coord == COORDINATE
        assert alt == ALTITUDE

    @pytest.mark.asyncio
    async def test_get_linear_velocity(self, movement_sensor: MovementSensor):
        value = await movement_sensor.get_linear_velocity()
        assert value == LINEAR_VELOCITY

    @pytest.mark.asyncio
    async def test_get_angular_velocity(self, movement_sensor: MovementSensor):
        value = await movement_sensor.get_angular_velocity()
        assert value == ANGULAR_VELOCITY

    @pytest.mark.asyncio
    async def test_get_compass_heading(self, movement_sensor: MovementSensor):
        value = await movement_sensor.get_compass_heading()
        assert value == HEADING

    @pytest.mark.asyncio
    async def test_get_orientation(self, movement_sensor: MovementSensor):
        value = await movement_sensor.get_orientation()
        assert value == ORIENTATION

    @pytest.mark.asyncio
    async def test_get_properties(self, movement_sensor: MovementSensor):
        value = await movement_sensor.get_properties()
        assert value == PROPERTIES

    @pytest.mark.asyncio
    async def test_get_accuracy(self, movement_sensor: MovementSensor):
        value = await movement_sensor.get_accuracy()
        assert value == ACCURACY


class TestService:
    @pytest.mark.asyncio
    async def test_get_position(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetPositionRequest(name=movement_sensor.name)
            response: GetPositionResponse = await client.GetPosition(request)
            assert response.coordinate == COORDINATE
            assert response.altitude_mm == ALTITUDE

    @pytest.mark.asyncio
    async def test_get_linear_velocity(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetLinearVelocityRequest(name=movement_sensor.name)
            response: GetLinearVelocityResponse = await client.GetLinearVelocity(request)
            assert response.linear_velocity == LINEAR_VELOCITY

    @pytest.mark.asyncio
    async def test_get_angular_velocity(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetAngularVelocityRequest(name=movement_sensor.name)
            response: GetAngularVelocityResponse = await client.GetAngularVelocity(request)
            assert response.angular_velocity == ANGULAR_VELOCITY

    @pytest.mark.asyncio
    async def test_get_compass_heading(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetCompassHeadingRequest(name=movement_sensor.name)
            response: GetCompassHeadingResponse = await client.GetCompassHeading(request)
            assert response.value == HEADING

    @pytest.mark.asyncio
    async def test_get_orientation(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetOrientationRequest(name=movement_sensor.name)
            response: GetOrientationResponse = await client.GetOrientation(request)
            assert response.orientation == ORIENTATION

    @pytest.mark.asyncio
    async def test_get_properties(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetPropertiesRequest(name=movement_sensor.name)
            response: GetPropertiesResponse = await client.GetProperties(request)
            assert response == PROPERTIES

    @pytest.mark.asyncio
    async def test_get_accuracy(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetAccuracyRequest(name=movement_sensor.name)
            response: GetAccuracyResponse = await client.GetAccuracy(request)
            assert response.accuracy_mm == pytest.approx(ACCURACY)


class TestClient:
    @pytest.mark.asyncio
    async def test_get_position(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            (coord, alt) = await client.get_position()
            assert coord == COORDINATE
            assert alt == ALTITUDE

    @pytest.mark.asyncio
    async def test_get_linear_velocity(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            value = await client.get_linear_velocity()
            assert value == LINEAR_VELOCITY

    @pytest.mark.asyncio
    async def test_get_angular_velocity(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            value = await client.get_angular_velocity()
            assert value == ANGULAR_VELOCITY

    @pytest.mark.asyncio
    async def test_get_compass_heading(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            value = await client.get_compass_heading()
            assert value == HEADING

    @pytest.mark.asyncio
    async def test_get_orientation(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            value = await client.get_orientation()
            assert value == ORIENTATION

    @pytest.mark.asyncio
    async def test_get_properties(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            value = await client.get_properties()
            assert value == PROPERTIES

    @pytest.mark.asyncio
    async def test_get_accuracy(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            value = await client.get_accuracy()
            assert value == pytest.approx(ACCURACY)

    @pytest.mark.asyncio
    async def test_do(self, movement_sensor: MovementSensor, service: MovementSensorService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do({"command": "args"})
