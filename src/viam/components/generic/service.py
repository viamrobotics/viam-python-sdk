from grpclib import GRPCError, Status
from grpclib.server import Stream

from viam.components.component_base import ComponentBase
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.generic import GenericServiceBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

# from .generic import Generic


class GenericRPCService(GenericServiceBase, ResourceRPCServiceBase):
    """
    gRPC Service for a Generic component
    """

    RESOURCE_TYPE = ComponentBase

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        component = self.get_resource(name)
        try:
            timeout = stream.deadline.time_remaining() if stream.deadline else None
            result = await component.do_command(struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        except NotImplementedError:
            raise GRPCError(Status.UNIMPLEMENTED, f"``DO`` command is unimplemented for component named: {name}")
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        component = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await component.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
