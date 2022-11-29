from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.operations import kwargs_from_metadata
from viam.proto.component.arm import (
    ArmServiceBase,
    GetEndPositionRequest,
    GetEndPositionResponse,
    GetJointPositionsRequest,
    GetJointPositionsResponse,
    MoveToJointPositionsRequest,
    MoveToJointPositionsResponse,
    MoveToPositionRequest,
    MoveToPositionResponse,
    StopRequest,
    StopResponse,
)
from viam.utils import struct_to_dict

from .arm import Arm


class ArmService(ArmServiceBase, ComponentServiceBase[Arm]):
    """
    gRPC Service for an Arm
    """

    RESOURCE_TYPE = Arm

    async def GetEndPosition(self, stream: Stream[GetEndPositionRequest, GetEndPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        kwargs = kwargs_from_metadata(stream.metadata)
        position = await arm.get_end_position(extra=struct_to_dict(request.extra), timeout=timeout, **kwargs)
        response = GetEndPositionResponse(pose=position)
        await stream.send_message(response)

    async def MoveToPosition(self, stream: Stream[MoveToPositionRequest, MoveToPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        kwargs = kwargs_from_metadata(stream.metadata)
        await arm.move_to_position(request.to, request.world_state, extra=struct_to_dict(request.extra), timeout=timeout, **kwargs)
        response = MoveToPositionResponse()
        await stream.send_message(response)

    async def GetJointPositions(self, stream: Stream[GetJointPositionsRequest, GetJointPositionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        kwargs = kwargs_from_metadata(stream.metadata)
        positions = await arm.get_joint_positions(extra=struct_to_dict(request.extra), timeout=timeout, **kwargs)
        response = GetJointPositionsResponse(positions=positions)
        await stream.send_message(response)

    async def MoveToJointPositions(self, stream: Stream[MoveToJointPositionsRequest, MoveToJointPositionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        kwargs = kwargs_from_metadata(stream.metadata)
        await arm.move_to_joint_positions(request.positions, extra=struct_to_dict(request.extra), timeout=timeout, **kwargs)
        response = MoveToJointPositionsResponse()
        await stream.send_message(response)

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            arm = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        kwargs = kwargs_from_metadata(stream.metadata)
        await arm.stop(extra=struct_to_dict(request.extra), timeout=timeout, **kwargs)
        response = StopResponse()
        await stream.send_message(response)
