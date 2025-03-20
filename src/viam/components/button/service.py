from grpclib.server import Stream

from viam.gen.component.button.v1.button_pb2 import (
    PushRequest,
    PushResponse,
)
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
)
from viam.proto.component.button import ButtonServiceBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .button import Button


class ButtonRPCService(ButtonServiceBase, ResourceRPCServiceBase[Button]):
    """
    gRPC Service for a generic Button
    """

    RESOURCE_TYPE = Button

    async def Push(self, stream: Stream[PushRequest, PushResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        button = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await button.push(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(PushResponse())

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        button = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await button.do_command(
            command=struct_to_dict(request.command),
            timeout=timeout,
            metadata=stream.metadata,
        )
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
