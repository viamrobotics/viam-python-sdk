from grpclib.server import Stream

from viam.components.movement_sensor.movement_sensor import MovementSensor
from viam.errors import ResourceNotFoundError
from viam.proto.common import DoCommandRequest, DoCommandResponse
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
    MovementSensorServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict


class MovementSensorService(MovementSensorServiceBase, ResourceRPCServiceBase[MovementSensor]):
    """
    gRPC Service for a MovementSensor
    """

    RESOURCE_TYPE = MovementSensor

    async def GetLinearVelocity(self, stream: Stream[GetLinearVelocityRequest, GetLinearVelocityResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        velocity = await sensor.get_linear_velocity(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetLinearVelocityResponse(linear_velocity=velocity)
        await stream.send_message(response)

    async def GetAngularVelocity(self, stream: Stream[GetAngularVelocityRequest, GetAngularVelocityResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        velocity = await sensor.get_angular_velocity(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetAngularVelocityResponse(angular_velocity=velocity)
        await stream.send_message(response)

    async def GetLinearAcceleration(self, stream: Stream[GetLinearAccelerationRequest, GetLinearAccelerationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        acceleration = await sensor.get_linear_acceleration(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetLinearAccelerationResponse(linear_acceleration=acceleration)
        await stream.send_message(response)

    async def GetCompassHeading(self, stream: Stream[GetCompassHeadingRequest, GetCompassHeadingResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        heading = await sensor.get_compass_heading(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetCompassHeadingResponse(value=heading)
        await stream.send_message(response)

    async def GetOrientation(self, stream: Stream[GetOrientationRequest, GetOrientationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        orientation = await sensor.get_orientation(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetOrientationResponse(orientation=orientation)
        await stream.send_message(response)

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        point, alt = await sensor.get_position(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetPositionResponse(coordinate=point, altitude_mm=alt)
        await stream.send_message(response)

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = await sensor.get_properties(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(response)

    async def GetAccuracy(self, stream: Stream[GetAccuracyRequest, GetAccuracyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        accuracy = await sensor.get_accuracy(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetAccuracyResponse(accuracy_mm=accuracy)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            sensor = self.get_resource(request.name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await sensor.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
