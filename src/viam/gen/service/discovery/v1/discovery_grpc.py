import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import app
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service

class DiscoveryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DiscoverResources(self, stream: 'grpclib.server.Stream[service.discovery.v1.discovery_pb2.DiscoverResourcesRequest, service.discovery.v1.discovery_pb2.DiscoverResourcesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.discovery.v1.DiscoveryService/DiscoverResources': grpclib.const.Handler(self.DiscoverResources, grpclib.const.Cardinality.UNARY_UNARY, service.discovery.v1.discovery_pb2.DiscoverResourcesRequest, service.discovery.v1.discovery_pb2.DiscoverResourcesResponse), '/viam.service.discovery.v1.DiscoveryService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedDiscoveryServiceBase(DiscoveryServiceBase):

    async def DiscoverResources(self, stream: 'grpclib.server.Stream[service.discovery.v1.discovery_pb2.DiscoverResourcesRequest, service.discovery.v1.discovery_pb2.DiscoverResourcesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class DiscoveryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DiscoverResources = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.discovery.v1.DiscoveryService/DiscoverResources', service.discovery.v1.discovery_pb2.DiscoverResourcesRequest, service.discovery.v1.discovery_pb2.DiscoverResourcesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.discovery.v1.DiscoveryService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)