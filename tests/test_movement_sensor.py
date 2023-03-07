import pytest
from grpclib.testing import ChannelFor
from grpclib import GRPCError, Status
from typing import Any, Dict, Optional

from viam.components.generic.service import GenericService
from viam.components.movement_sensor import (
    MovementSensor,
    MovementSensorClient,
    MovementSensorService,
)
from viam.components.resource_manager import ResourceManager
from viam.proto.common import GeoPoint, Orientation, Vector3, DoCommandRequest, DoCommandResponse
from viam.proto.component.movementsensor import (
    GetAccuracyRequest,
    GetAccuracyResponse,
    GetAngularVelocityRequest,
    GetAngularVelocityResponse,
    GetCompassHeadingRequest,
    GetCompassHeadingResponse,
    GetLinearAccelerationRequest,
    GetLinearAccelerationResponse,
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
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockMovementSensor

COORDINATE = GeoPoint(latitude=40.664679865782624, longitude=-73.97668056188789)
ALTITUDE = 15
LINEAR_VELOCITY = Vector3(x=1, y=2, z=3)
ANGULAR_VELOCITY = Vector3(x=1, y=2, z=3)
LINEAR_ACCELERATION = Vector3(x=1, y=2, z=3)
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
EXTRA_PARAMS = {"foo": "bar", "baz": [1, 2, 3]}


@pytest.fixture(scope="function")
def movement_sensor() -> MovementSensor:
    return MockMovementSensor(
        "movement_sensor",
        COORDINATE,
        ALTITUDE,
        LINEAR_VELOCITY,
        ANGULAR_VELOCITY,
        LINEAR_ACCELERATION,
        HEADING,
        ORIENTATION,
        PROPERTIES,
        ACCURACY,
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
    async def test_get_position(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        (coord, alt) = await movement_sensor.get_position(extra=EXTRA_PARAMS)
        assert coord == COORDINATE
        assert alt == ALTITUDE
        assert movement_sensor.extra == EXTRA_PARAMS

    @pytest.mark.asyncio
    async def test_get_linear_velocity(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_linear_velocity(extra=EXTRA_PARAMS)
        assert value == LINEAR_VELOCITY
        assert movement_sensor.extra == EXTRA_PARAMS

    @pytest.mark.asyncio
    async def test_get_linear_acceleration(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_linear_acceleration(extra=EXTRA_PARAMS)
        assert value == LINEAR_ACCELERATION
        assert movement_sensor.extra == EXTRA_PARAMS

    @pytest.mark.asyncio
    async def test_get_angular_velocity(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_angular_velocity(extra=EXTRA_PARAMS)
        assert value == ANGULAR_VELOCITY
        assert movement_sensor.extra == EXTRA_PARAMS

    @pytest.mark.asyncio
    async def test_get_compass_heading(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_compass_heading(extra=EXTRA_PARAMS)
        assert value == HEADING
        assert movement_sensor.extra == EXTRA_PARAMS

    @pytest.mark.asyncio
    async def test_get_orientation(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_orientation(extra=EXTRA_PARAMS)
        assert value == ORIENTATION
        assert movement_sensor.extra == EXTRA_PARAMS

    @pytest.mark.asyncio
    async def test_get_properties(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_properties(extra=EXTRA_PARAMS)
        assert value == PROPERTIES
        assert movement_sensor.extra == EXTRA_PARAMS

    @pytest.mark.asyncio
    async def test_get_accuracy(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_accuracy(extra=EXTRA_PARAMS)
        assert value == ACCURACY
        assert movement_sensor.extra == EXTRA_PARAMS

    @pytest.mark.asyncio
    async def test_get_readings(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_readings(extra=EXTRA_PARAMS)
        assert value == {
            "position": COORDINATE,
            "altitude": ALTITUDE,
            "linear_velocity": LINEAR_VELOCITY,
            "angular_velocity": ANGULAR_VELOCITY,
            "linear_acceleration": LINEAR_ACCELERATION,
            "compass": HEADING,
            "orientation": ORIENTATION,
        }
        assert movement_sensor.extra == EXTRA_PARAMS

        # A mock method to replace some get functions just for testing
        async def get_reading(*, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Vector3:
            raise GRPCError(Status(2))

        async def get_compass_heading(*, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
            raise GRPCError(Status(2))

        movement_sensor.get_linear_velocity = get_reading
        movement_sensor.get_linear_acceleration = get_reading
        movement_sensor.get_angular_velocity = get_reading
        movement_sensor.get_compass_heading = get_compass_heading

        value = await movement_sensor.get_readings(extra=EXTRA_PARAMS)
        assert value == {
            "position": COORDINATE,
            "altitude": ALTITUDE,
            "orientation": ORIENTATION,
        }

    @pytest.mark.asyncio
    async def test_timeout(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.timeout is None

        await movement_sensor.get_position(timeout=1.23)
        assert movement_sensor.timeout == loose_approx(1.23)

        await movement_sensor.get_linear_velocity(timeout=2.34)
        assert movement_sensor.timeout == loose_approx(2.34)

        await movement_sensor.get_angular_velocity(timeout=3.45)
        assert movement_sensor.timeout == loose_approx(3.45)

        await movement_sensor.get_linear_acceleration(timeout=9.01)
        assert movement_sensor.timeout == loose_approx(9.01)

        await movement_sensor.get_compass_heading(timeout=4.56)
        assert movement_sensor.timeout == loose_approx(4.56)

        await movement_sensor.get_orientation(timeout=5.67)
        assert movement_sensor.timeout == loose_approx(5.67)

        await movement_sensor.get_properties(timeout=6.78)
        assert movement_sensor.timeout == loose_approx(6.78)

        await movement_sensor.get_accuracy(timeout=7.89)
        assert movement_sensor.timeout == loose_approx(7.89)

        await movement_sensor.get_readings(timeout=8.90)
        assert movement_sensor.timeout == loose_approx(8.90)

    @pytest.mark.asyncio
    async def test_do(self, movement_sensor: MovementSensor):
        command = {"command": "args"}
        resp = await movement_sensor.do_command(command)
        assert resp == {"command": command}


class TestService:
    @pytest.mark.asyncio
    async def test_get_position(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetPositionRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetPositionResponse = await client.GetPosition(request, timeout=1.23)
            assert response.coordinate == COORDINATE
            assert response.altitude_mm == ALTITUDE
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_linear_velocity(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetLinearVelocityRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetLinearVelocityResponse = await client.GetLinearVelocity(request, timeout=2.34)
            assert response.linear_velocity == LINEAR_VELOCITY
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_get_angular_velocity(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetAngularVelocityRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetAngularVelocityResponse = await client.GetAngularVelocity(request, timeout=3.45)
            assert response.angular_velocity == ANGULAR_VELOCITY
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_get_linear_acceleration(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetLinearAccelerationRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetLinearAccelerationResponse = await client.GetLinearAcceleration(request, timeout=2.34)
            assert response.linear_acceleration == LINEAR_ACCELERATION
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_get_compass_heading(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetCompassHeadingRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            response: GetCompassHeadingResponse = await client.GetCompassHeading(request, timeout=4.56)
            assert response.value == HEADING
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(4.56)

    @pytest.mark.asyncio
    async def test_get_orientation(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetOrientationRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetOrientationResponse = await client.GetOrientation(request, timeout=5.67)
            assert response.orientation == ORIENTATION
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(5.67)

    @pytest.mark.asyncio
    async def test_get_properties(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetPropertiesRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=6.78)
            assert response == PROPERTIES
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_get_accuracy(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetAccuracyRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetAccuracyResponse = await client.GetAccuracy(request, timeout=7.89)
            assert response.accuracy_mm == pytest.approx(ACCURACY)
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(7.89)

    @pytest.mark.asyncio
    async def test_do(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=movement_sensor.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}


class TestClient:
    @pytest.mark.asyncio
    async def test_get_position(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            (coord, alt) = await client.get_position(extra=EXTRA_PARAMS, timeout=1.45)
            assert coord == COORDINATE
            assert alt == ALTITUDE
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(1.45)

    @pytest.mark.asyncio
    async def test_get_linear_velocity(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_linear_velocity(extra=EXTRA_PARAMS, timeout=2.34)
            assert value == LINEAR_VELOCITY
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_get_angular_velocity(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_angular_velocity(extra=EXTRA_PARAMS, timeout=3.45)
            assert value == ANGULAR_VELOCITY
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_get_linear_acceleration(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_linear_acceleration(extra=EXTRA_PARAMS, timeout=2.34)
            assert value == LINEAR_ACCELERATION
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_get_compass_heading(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_compass_heading(extra=EXTRA_PARAMS, timeout=4.56)
            assert value == HEADING
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(4.56)

    @pytest.mark.asyncio
    async def test_get_orientation(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_orientation(extra=EXTRA_PARAMS, timeout=5.67)
            assert value == ORIENTATION
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(5.67)

    @pytest.mark.asyncio
    async def test_get_properties(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_properties(extra=EXTRA_PARAMS, timeout=6.78)
            assert value == PROPERTIES
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_get_accuracy(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_accuracy(extra=EXTRA_PARAMS, timeout=7.89)
            assert value == pytest.approx(ACCURACY)
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(7.89)

    @pytest.mark.asyncio
    async def test_get_readings(self, movement_sensor: MockMovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_readings(extra=EXTRA_PARAMS, timeout=8.90)
            assert value == {
                "position": COORDINATE,
                "altitude": ALTITUDE,
                "linear_velocity": LINEAR_VELOCITY,
                "angular_velocity": ANGULAR_VELOCITY,
                "linear_acceleration": LINEAR_ACCELERATION,
                "compass": HEADING,
                "orientation": ORIENTATION,
            }
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == loose_approx(8.90)

    @pytest.mark.asyncio
    async def test_do(self, movement_sensor: MovementSensor, service: MovementSensorService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}
