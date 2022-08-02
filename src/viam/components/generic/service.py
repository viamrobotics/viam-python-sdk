from grpclib import GRPCError, Status
from grpclib.server import Stream
from viam.components.component_base import ComponentBase
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.generic import DoRequest, DoResponse, GenericServiceBase
from viam.utils import dict_to_struct, struct_to_dict

# from .generic import Generic


class GenericService(GenericServiceBase, ComponentServiceBase[ComponentBase]):
    """
    gRPC Service for a Generic component
    """

    RESOURCE_TYPE = ComponentBase

    async def Do(self, stream: Stream[DoRequest, DoResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            component = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        try:
            result = await component.do(struct_to_dict(request.command))
        except NotImplementedError:
            raise GRPCError(Status.UNIMPLEMENTED, f"`DO` command is unimplemented for component named: {name}")
        response = DoResponse(result=dict_to_struct(result))
        await stream.send_message(response)
