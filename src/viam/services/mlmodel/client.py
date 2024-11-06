from typing import Dict, Mapping, Optional

from grpclib.client import Channel
from numpy.typing import NDArray

from viam.proto.service.mlmodel import InferRequest, InferResponse, MetadataRequest, MetadataResponse, MLModelServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.services.mlmodel.utils import flat_tensors_to_ndarrays, ndarrays_to_flat_tensors
from viam.utils import ValueTypes, dict_to_struct

from .mlmodel import Metadata, MLModel


class MLModelClient(MLModel, ReconfigurableResourceRPCClientBase):
    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MLModelServiceStub(channel)
        super().__init__(name)

    async def infer(
        self,
        input_tensors: Dict[str, NDArray],
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Dict[str, NDArray]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = InferRequest(name=self.name, input_tensors=ndarrays_to_flat_tensors(input_tensors), extra=dict_to_struct(extra))
        response: InferResponse = await self.client.Infer(request, timeout=timeout, metadata=md)
        return flat_tensors_to_ndarrays(response.output_tensors)

    async def metadata(self, *, extra: Optional[Mapping[str, ValueTypes]] = None, timeout: Optional[float] = None, **kwargs) -> Metadata:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = MetadataRequest(name=self.name, extra=dict_to_struct(extra))
        response: MetadataResponse = await self.client.Metadata(request, timeout=timeout, metadata=md)
        return response.metadata
