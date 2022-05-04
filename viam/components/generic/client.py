from google.protobuf.struct_pb2 import Struct
from typing import Any, Dict
from grpclib.client import Channel
from viam.proto.api.component.generic import (
    GenericServiceStub,
    DoRequest, DoResponse
)
from viam.utils import value_to_primitive

from .generic import Generic


class GenericClient(Generic):
    """
    gRPC client for the Generic component.
    """

    def __init__(self, name: str, channel: Channel):
        self.client = GenericServiceStub(channel)
        super().__init__(name)

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        struct = Struct()
        struct.update(command)
        request = DoRequest(name=self.name, command=struct)
        response: DoResponse = await self.client.Do(request)
        return {key: value_to_primitive(value) for (key, value) in response.result.fields.items()}
