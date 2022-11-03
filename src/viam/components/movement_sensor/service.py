from grpclib.server import Stream

from viam.components.movement_sensor.movement_sensor import MovementSensor
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.component.movementsensor import (
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
    MovementSensorServiceBase,
)


class MovementSensorService(MovementSensorServiceBase, ComponentServiceBase[MovementSensor]):
    """
    gRPC Service for a MovementSensor
    """

    RESOURCE_TYPE = MovementSensor

    async def GetLinearVelocity(self, stream: Stream[GetLinearVelocityRequest, GetLinearVelocityResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        velocity = await sensor.get_linear_velocity(timeout=timeout)
        response = GetLinearVelocityResponse(linear_velocity=velocity)
        await stream.send_message(response)

    async def GetAngularVelocity(self, stream: Stream[GetAngularVelocityRequest, GetAngularVelocityResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        velocity = await sensor.get_angular_velocity(timeout=timeout)
        response = GetAngularVelocityResponse(angular_velocity=velocity)
        await stream.send_message(response)

    async def GetCompassHeading(self, stream: Stream[GetCompassHeadingRequest, GetCompassHeadingResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        heading = await sensor.get_compass_heading(timeout=timeout)
        response = GetCompassHeadingResponse(value=heading)
        await stream.send_message(response)

    async def GetOrientation(self, stream: Stream[GetOrientationRequest, GetOrientationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        orientation = await sensor.get_orientation(timeout=timeout)
        response = GetOrientationResponse(orientation=orientation)
        await stream.send_message(response)

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        point, alt = await sensor.get_position(timeout=timeout)
        response = GetPositionResponse(coordinate=point, altitude_mm=alt)
        await stream.send_message(response)

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = await sensor.get_properties(timeout=timeout)
        await stream.send_message(response)

    async def GetAccuracy(self, stream: Stream[GetAccuracyRequest, GetAccuracyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        accuracy = await sensor.get_accuracy(timeout=timeout)
        response = GetAccuracyResponse(accuracy_mm=accuracy)
        await stream.send_message(response)
