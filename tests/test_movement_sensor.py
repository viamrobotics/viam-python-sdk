import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericRPCService
from viam.components.movement_sensor import MovementSensor, MovementSensorClient, MovementSensorRPCService
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GeoPoint,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetReadingsRequest,
    GetReadingsResponse,
    Orientation,
    Vector3,
)
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
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, sensor_readings_value_to_native, struct_to_dict

from . import expected_grpc_timeout
from .mocks.components import GEOMETRIES, MockMovementSensor

COORDINATE = GeoPoint(latitude=40.664679865782624, longitude=-73.97668056188789)
ALTITUDE = 15
LINEAR_VELOCITY = Vector3(x=1, y=2, z=3)
ANGULAR_VELOCITY = Vector3(x=1, y=2, z=3)
LINEAR_ACCELERATION = Vector3(x=1, y=2, z=3)
HEADING = 182
ORIENTATION = Orientation(o_x=1, o_y=2, o_z=3, theta=5)
PROPERTIES = MovementSensor.Properties(
    linear_acceleration_supported=False,
    linear_velocity_supported=False,
    angular_velocity_supported=True,
    orientation_supported=False,
    position_supported=True,
    compass_heading_supported=False,
)
ACCURACY = MovementSensor.Accuracy(
    accuracy={"foo": 0.1, "bar": 2, "baz": 3.14},
    position_hdop=0.0,
    position_vdop=0.0,
    position_nmea_gga_fix=0,
    compass_degrees_error=0.0,
)
EXTRA_PARAMS = {"foo": "bar", "baz": [1, 2, 3]}
READINGS = {"a": 1, "b": 2, "c": 3}


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
        READINGS,
    )


@pytest.fixture(scope="function")
def service(movement_sensor: MovementSensor) -> MovementSensorRPCService:
    manager = ResourceManager([movement_sensor])
    return MovementSensorRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(movement_sensor: MovementSensor) -> GenericRPCService:
    manager = ResourceManager([movement_sensor])
    return GenericRPCService(manager)


class TestMovementSensor:
    async def test_get_position(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        (coord, alt) = await movement_sensor.get_position(extra=EXTRA_PARAMS)
        assert coord == COORDINATE
        assert alt == ALTITUDE
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_get_linear_velocity(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_linear_velocity(extra=EXTRA_PARAMS)
        assert value == LINEAR_VELOCITY
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_get_linear_acceleration(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_linear_acceleration(extra=EXTRA_PARAMS)
        assert value == LINEAR_ACCELERATION
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_get_angular_velocity(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_angular_velocity(extra=EXTRA_PARAMS)
        assert value == ANGULAR_VELOCITY
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_get_compass_heading(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_compass_heading(extra=EXTRA_PARAMS)
        assert value == HEADING
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_get_orientation(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_orientation(extra=EXTRA_PARAMS)
        assert value == ORIENTATION
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_get_properties(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_properties(extra=EXTRA_PARAMS)
        assert value == PROPERTIES
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_get_accuracy(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        value = await movement_sensor.get_accuracy(extra=EXTRA_PARAMS)
        assert value.accuracy == pytest.approx(ACCURACY.accuracy)
        assert value.position_hdop == pytest.approx(ACCURACY.position_hdop)
        assert value.position_vdop == pytest.approx(ACCURACY.position_vdop)
        assert value.position_nmea_gga_fix == pytest.approx(ACCURACY.position_nmea_gga_fix)
        assert value.compass_degrees_error == pytest.approx(ACCURACY.compass_degrees_error)
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_get_readings(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.extra is None
        readings = await movement_sensor.get_readings(extra=EXTRA_PARAMS)
        assert readings == READINGS
        assert movement_sensor.extra == EXTRA_PARAMS

    async def test_timeout(self, movement_sensor: MockMovementSensor):
        assert movement_sensor.timeout is None

        await movement_sensor.get_position(timeout=1.23)
        assert movement_sensor.timeout == expected_grpc_timeout(1.23)

        await movement_sensor.get_linear_velocity(timeout=2.34)
        assert movement_sensor.timeout == expected_grpc_timeout(2.34)

        await movement_sensor.get_angular_velocity(timeout=3.45)
        assert movement_sensor.timeout == expected_grpc_timeout(3.45)

        await movement_sensor.get_linear_acceleration(timeout=9.01)
        assert movement_sensor.timeout == expected_grpc_timeout(9.01)

        await movement_sensor.get_compass_heading(timeout=4.56)
        assert movement_sensor.timeout == expected_grpc_timeout(4.56)

        await movement_sensor.get_orientation(timeout=5.67)
        assert movement_sensor.timeout == expected_grpc_timeout(5.67)

        await movement_sensor.get_properties(timeout=6.78)
        assert movement_sensor.timeout == expected_grpc_timeout(6.78)

        await movement_sensor.get_accuracy(timeout=7.89)
        assert movement_sensor.timeout == expected_grpc_timeout(7.89)

        await movement_sensor.get_readings(timeout=8.90)
        assert movement_sensor.timeout == expected_grpc_timeout(8.90)

    async def test_do(self, movement_sensor: MovementSensor):
        command = {"command": "args"}
        resp = await movement_sensor.do_command(command)
        assert resp == {"command": command}

    async def test_get_geometries(self, movement_sensor: MockMovementSensor):
        geometries = await movement_sensor.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    async def test_get_position(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetPositionRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetPositionResponse = await client.GetPosition(request, timeout=1.23)
            assert response.coordinate == COORDINATE
            assert response.altitude_m == ALTITUDE
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(1.23)

    async def test_get_linear_velocity(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetLinearVelocityRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetLinearVelocityResponse = await client.GetLinearVelocity(request, timeout=2.34)
            assert response.linear_velocity == LINEAR_VELOCITY
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(2.34)

    async def test_get_angular_velocity(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetAngularVelocityRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetAngularVelocityResponse = await client.GetAngularVelocity(request, timeout=3.45)
            assert response.angular_velocity == ANGULAR_VELOCITY
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(3.45)

    async def test_get_linear_acceleration(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetLinearAccelerationRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetLinearAccelerationResponse = await client.GetLinearAcceleration(request, timeout=2.34)
            assert response.linear_acceleration == LINEAR_ACCELERATION
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(2.34)

    async def test_get_compass_heading(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetCompassHeadingRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            response: GetCompassHeadingResponse = await client.GetCompassHeading(request, timeout=4.56)
            assert response.value == HEADING
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(4.56)

    async def test_get_orientation(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetOrientationRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetOrientationResponse = await client.GetOrientation(request, timeout=5.67)
            assert response.orientation == ORIENTATION
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(5.67)

    async def test_get_properties(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetPropertiesRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=6.78)
            assert MovementSensor.Properties.from_proto(response) == PROPERTIES
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(6.78)

    async def test_get_accuracy(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetAccuracyRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetAccuracyResponse = await client.GetAccuracy(request, timeout=7.89)
            assert response.accuracy == pytest.approx(ACCURACY.accuracy)
            assert response.position_hdop == pytest.approx(ACCURACY.position_hdop)
            assert response.position_vdop == pytest.approx(ACCURACY.position_vdop)
            assert response.position_nmea_gga_fix == pytest.approx(ACCURACY.position_nmea_gga_fix)
            assert response.compass_degrees_error == pytest.approx(ACCURACY.compass_degrees_error)
            assert movement_sensor.timeout == expected_grpc_timeout(7.89)

    async def test_get_readings(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetReadingsRequest(name=movement_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert movement_sensor.extra is None
            response: GetReadingsResponse = await client.GetReadings(request, timeout=8.90)
            assert sensor_readings_value_to_native(response.readings) == READINGS
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(8.90)

    async def test_do(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=movement_sensor.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_geometries(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorServiceStub(channel)
            request = GetGeometriesRequest(name=movement_sensor.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    async def test_get_position(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            (coord, alt) = await client.get_position(extra=EXTRA_PARAMS, timeout=1.45)
            assert coord == COORDINATE
            assert alt == ALTITUDE
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(1.45)

    async def test_get_linear_velocity(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_linear_velocity(extra=EXTRA_PARAMS, timeout=2.34)
            assert value == LINEAR_VELOCITY
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(2.34)

    async def test_get_angular_velocity(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_angular_velocity(extra=EXTRA_PARAMS, timeout=3.45)
            assert value == ANGULAR_VELOCITY
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(3.45)

    async def test_get_linear_acceleration(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_linear_acceleration(extra=EXTRA_PARAMS, timeout=2.34)
            assert value == LINEAR_ACCELERATION
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(2.34)

    async def test_get_compass_heading(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_compass_heading(extra=EXTRA_PARAMS, timeout=4.56)
            assert value == HEADING
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(4.56)

    async def test_get_orientation(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_orientation(extra=EXTRA_PARAMS, timeout=5.67)
            assert value == ORIENTATION
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(5.67)

    async def test_get_properties(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_properties(extra=EXTRA_PARAMS, timeout=6.78)
            assert value == PROPERTIES
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(6.78)

    async def test_get_accuracy(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_accuracy(extra=EXTRA_PARAMS, timeout=7.89)
            assert value.accuracy == pytest.approx(ACCURACY.accuracy)
            assert value.position_hdop == pytest.approx(ACCURACY.position_hdop)
            assert value.position_vdop == pytest.approx(ACCURACY.position_vdop)
            assert value.position_nmea_gga_fix == pytest.approx(ACCURACY.position_nmea_gga_fix)
            assert value.compass_degrees_error == pytest.approx(ACCURACY.compass_degrees_error)
            assert movement_sensor.timeout == expected_grpc_timeout(7.89)

    async def test_get_readings(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            assert movement_sensor.extra is None
            value = await client.get_readings(extra=EXTRA_PARAMS, timeout=2.34)
            assert value == READINGS
            assert movement_sensor.extra == EXTRA_PARAMS
            assert movement_sensor.timeout == expected_grpc_timeout(2.34)

    async def test_do(self, movement_sensor: MovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    async def test_get_geometries(self, movement_sensor: MockMovementSensor, service: MovementSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = MovementSensorClient(movement_sensor.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES
