from google.protobuf.struct_pb2 import Struct
from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.generic import (DoRequest, DoResponse,
                                              GenericServiceBase)
from viam.utils import value_to_primitive

from .generic import Generic


class GenericService(GenericServiceBase, ComponentServiceBase[Generic]):
    """
    gRPC Service for a Generic component
    """

    RESOURCE_TYPE = Generic

    async def Do(self, stream: Stream[DoRequest, DoResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            component = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        result = await component.do({key: value_to_primitive(value) for (key, value) in request.command.fields.items()})
        struct = Struct()
        struct.update(result)
        response = DoResponse(result=struct)
        await stream.send_message(response)
