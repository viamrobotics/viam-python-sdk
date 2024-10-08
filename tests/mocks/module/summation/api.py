import abc
from typing import Final, Sequence

from grpclib.client import Channel
from grpclib.server import Stream

from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_base import ServiceBase

from ..proto.summation_grpc import SummationServiceBase, SummationServiceStub
from ..proto.summation_pb2 import SumRequest, SumResponse


class SummationService(ServiceBase):
    """Example service to use with the example module"""

    SUBTYPE: Final = Subtype("acme", RESOURCE_TYPE_SERVICE, "summation")

    @abc.abstractmethod
    async def sum(self, nums: Sequence[float]) -> float: ...


class SummationRPCService(SummationServiceBase, ResourceRPCServiceBase):
    """Example gRPC service for the Summation service"""

    RESOURCE_TYPE = SummationService

    async def Sum(self, stream: Stream[SumRequest, SumResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.sum(request.numbers)
        await stream.send_message(SumResponse(sum=resp))


class SummationClient(SummationService):
    """Example gRPC client for the Summation Service"""

    def __init__(self, name: str, channel: Channel) -> None:
        self.channel = channel
        self.client = SummationServiceStub(channel)
        super().__init__(name)

    async def sum(self, nums: Sequence[float]) -> float:
        request = SumRequest(name=self.name, numbers=nums)
        response: SumResponse = await self.client.Sum(request)
        return response.sum
