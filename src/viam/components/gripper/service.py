from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.component.gripper import (
    GrabRequest,
    GrabResponse,
    GripperServiceBase,
    OpenRequest,
    OpenResponse,
    StopRequest,
    StopResponse,
)
from viam.utils import struct_to_dict

from .gripper import Gripper


class GripperService(GripperServiceBase, ComponentServiceBase[Gripper]):
    """
    gRPC Service for a Gripper
    """

    RESOURCE_TYPE = Gripper

    async def Open(self, stream: Stream[OpenRequest, OpenResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gripper = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await gripper.open(extra=struct_to_dict(request.extra), timeout=timeout)
        response = OpenResponse()
        await stream.send_message(response)

    async def Grab(self, stream: Stream[GrabRequest, GrabResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gripper = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        grabbed = await gripper.grab(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GrabResponse(success=grabbed)
        await stream.send_message(response)

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            gripper = self.get_component(request.name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await gripper.stop(extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(StopResponse())
