# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/search_term_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.search_term_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v8.services.search_term_view_service_pb2


class SearchTermViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetSearchTermView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.search_term_view_service_pb2.GetSearchTermViewRequest, google.ads.googleads.v8.resources.search_term_view_pb2.SearchTermView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.SearchTermViewService/GetSearchTermView': grpclib.const.Handler(
                self.GetSearchTermView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.search_term_view_service_pb2.GetSearchTermViewRequest,
                google.ads.googleads.v8.resources.search_term_view_pb2.SearchTermView,
            ),
        }


class SearchTermViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSearchTermView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.SearchTermViewService/GetSearchTermView',
            google.ads.googleads.v8.services.search_term_view_service_pb2.GetSearchTermViewRequest,
            google.ads.googleads.v8.resources.search_term_view_pb2.SearchTermView,
        )
