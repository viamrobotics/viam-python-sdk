from grpclib.server import Stream

from viam.errors import ResourceNotFoundError
from viam.proto.service.mlmodel import InferRequest, InferResponse, MetadataRequest, MetadataResponse, MLModelServiceBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct

from .mlmodel import MLModel


class MLModelRPCService(MLModelServiceBase, ResourceRPCServiceBase):
    """
    gRPC service for a ML Model service
    """

    RESOURCE_TYPE = MLModel

    async def Infer(self, stream: Stream[InferRequest, InferResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            mlmodel = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        output_data = await mlmodel.infer(input_data=request.input_data, timeout=timeout)
        response = InferResponse(output_data=dict_to_struct(output_data))
        await stream.send_message(response)

    async def Metadata(self, stream: Stream[MetadataRequest, MetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            mlmodel = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        metadata = await mlmodel.metadata(timeout=timeout)
        response = MetadataResponse(metadata=metadata)
        await stream.send_message(response)
