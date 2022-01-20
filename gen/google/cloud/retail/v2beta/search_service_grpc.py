# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/retail/v2beta/search_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.cloud.retail.v2beta.common_pb2
import google.cloud.retail.v2beta.product_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import google.cloud.retail.v2beta.search_service_pb2


class SearchServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Search(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2beta.search_service_pb2.SearchRequest, google.cloud.retail.v2beta.search_service_pb2.SearchResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.retail.v2beta.SearchService/Search': grpclib.const.Handler(
                self.Search,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2beta.search_service_pb2.SearchRequest,
                google.cloud.retail.v2beta.search_service_pb2.SearchResponse,
            ),
        }


class SearchServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Search = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2beta.SearchService/Search',
            google.cloud.retail.v2beta.search_service_pb2.SearchRequest,
            google.cloud.retail.v2beta.search_service_pb2.SearchResponse,
        )
