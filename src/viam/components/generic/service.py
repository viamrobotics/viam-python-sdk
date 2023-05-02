from grpclib import GRPCError, Status
from grpclib.server import Stream

from viam.components.component_base import ComponentBase
from viam.errors import ResourceNotFoundError
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.generic import GenericServiceBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

# from .generic import Generic


class GenericRPCService(GenericServiceBase, ResourceRPCServiceBase[ComponentBase]):
    """
    gRPC Service for a Generic component
    """

    RESOURCE_TYPE = ComponentBase

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            component = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        try:
            timeout = stream.deadline.time_remaining() if stream.deadline else None
            result = await component.do_command(struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        except NotImplementedError:
            raise GRPCError(Status.UNIMPLEMENTED, f"``DO`` command is unimplemented for component named: {name}")
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
