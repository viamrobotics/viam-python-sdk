from typing import Dict, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.mlmodel import InferRequest, InferResponse, MetadataRequest, MetadataResponse, MLModelServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import (
    ValueTypes,
    dict_to_struct,
    struct_to_dict,
    flat_tensors_to_ndarrays,
    ndarrays_to_flat_tensors,
)

try:
    from numpy.typing import NDArray
except ImportError:
    import warnings

    warnings.warn(
        (
            "MLModel support in Viam Python SDK requires the installation of optional "
            "dependencies: specifically, numpy.  Update your package using the extra [mlmodel]"
            "e.g. `pip install viam-sdk[mlmode]` or the equivalent update in your dependency manager"
        )  # will want to replace the e.g. suggestion with a link to docs when that is available
    )
    raise


from .mlmodel import Metadata, MLModel


class MLModelClient(MLModel, ReconfigurableResourceRPCClientBase):
    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MLModelServiceStub(channel)
        super().__init__(name)

    async def infer(self, input_tensors: Dict[str, NDArray], *, timeout: Optional[float] = None) -> Dict[str, NDArray]:
        request = InferRequest(name=self.name, input_tensors=ndarrays_to_flat_tensors(input_tensors))
        response: InferResponse = await self.client.Infer(request)
        return flat_tensors_to_ndarrays(response.output_tensors)

    async def metadata(self, *, timeout: Optional[float] = None) -> Metadata:
        request = MetadataRequest(name=self.name)
        response: MetadataResponse = await self.client.Metadata(request)
        return response.metadata

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
