from typing import Dict, Mapping, Optional
from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.mlmodel import InferRequest, InferResponse, Metadata, MetadataRequest, MetadataResponse, MLModelServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from .mlmodel import MLModelService


class MLModelServiceClient(MLModelService, ReconfigurableResourceRPCClientBase):
    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MLModelServiceStub(channel)
        super().__init__(name)

    async def infer(self, *, timeout: Optional[float] = None) -> Dict:
        request = InferRequest(name=self.name)
        response: InferResponse = self.client.infer(request)
        return struct_to_dict(response.output_data)

    async def metadata(self, *, timeout: Optional[float] = None) -> Metadata:
        request = MetadataRequest(name=self.name)
        response: MetadataResponse = self.client.metadata(request)
        return response.metadata

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = self.client.do_command(request, tiemout=timeout)
        return struct_to_dict(response.result)
