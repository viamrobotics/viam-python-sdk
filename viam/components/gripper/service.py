from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.gripper import (GrabRequest, GrabResponse,
                                              GripperServiceBase, OpenRequest,
                                              OpenResponse)

from .gripper import Gripper


class GripperService(GripperServiceBase, ComponentServiceBase[Gripper]):
    """
    gRPC Service for a Gripper
    """

    RESOURCE_TYPE = Gripper

    async def Open(
        self,
        stream: Stream[OpenRequest, OpenResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gripper = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await gripper.open()
        response = OpenResponse()
        await stream.send_message(response)

    async def Grab(
        self,
        stream: Stream[GrabRequest, GrabResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gripper = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        grabbed = await gripper.grab()
        response = GrabResponse(success=grabbed)
        await stream.send_message(response)
