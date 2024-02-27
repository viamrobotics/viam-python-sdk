from grpclib import GRPCError, Status
from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.generic import GenericServiceBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.services.service_base import ServiceBase
from viam.utils import dict_to_struct, struct_to_dict


class GenericRPCService(GenericServiceBase, ResourceRPCServiceBase):
    """
    gRPC Service for a Generic service
    """

    RESOURCE_TYPE = ServiceBase

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        try:
            timeout = stream.deadline.time_remaining() if stream.deadline else None
            result = await service.do_command(struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        except NotImplementedError:
            raise GRPCError(Status.UNIMPLEMENTED, f"``DO`` command is unimplemented for service named: {name}")
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
