"""
This file outlines the general structure for the API around a custom, modularized service.

It defines the abstract class definition that all concrete implementations must follow,
the gRPC service that will handle calls to the service,
and the gRPC client that will be able to make calls to this service.

In this example, the ``Summation`` abstract class defines what functionality is required for all Summation services.
It extends ``ServiceBase``, as all service types must.
It also defines its specific ``SUBTYPE``, which is used internally to keep track of supported types.

The ``SummationRPCService`` implements the gRPC service for the Summation service. This will allow other robots and clients to make
requests of the Summation service. It extends both from ``SummationServiceBase`` and ``RPCServiceBase``.
The former is the gRPC service as defined by the proto, and the latter is the class that all gRPC services must inherit from.

Finally, the ``SummationClient`` is the gRPC client for a Summation service. It inherits from SummationService since it implements
 all the same functions. The implementations are simply gRPC calls to some remote Summation service.

To see how this custom modular service is registered, see the __init__.py file.
To see the custom implementation of this service, see the my_summation.py file.
"""

import abc
from typing import Final, Sequence

from grpclib.client import Channel
from grpclib.server import Stream

from viam.errors import ResourceNotFoundError
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_base import ServiceBase

from ..proto.summation_grpc import SummationServiceBase, SummationServiceStub
from ..proto.summation_pb2 import SumRequest, SumResponse


class SummationService(ServiceBase):
    """Example service to use with the example module"""

    SUBTYPE: Final = Subtype("acme", RESOURCE_TYPE_SERVICE, "summation")

    @abc.abstractmethod
    async def sum(self, nums: Sequence[float]) -> float:
        ...


class SummationRPCService(SummationServiceBase, ResourceRPCServiceBase[SummationService]):
    """Example gRPC service for the Summation service"""

    RESOURCE_TYPE = SummationService

    async def Sum(self, stream: Stream[SumRequest, SumResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            service = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
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
