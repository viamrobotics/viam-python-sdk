# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/keyword_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.keyword_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v8.services.keyword_view_service_pb2


class KeywordViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetKeywordView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.keyword_view_service_pb2.GetKeywordViewRequest, google.ads.googleads.v8.resources.keyword_view_pb2.KeywordView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.KeywordViewService/GetKeywordView': grpclib.const.Handler(
                self.GetKeywordView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.keyword_view_service_pb2.GetKeywordViewRequest,
                google.ads.googleads.v8.resources.keyword_view_pb2.KeywordView,
            ),
        }


class KeywordViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetKeywordView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.KeywordViewService/GetKeywordView',
            google.ads.googleads.v8.services.keyword_view_service_pb2.GetKeywordViewRequest,
            google.ads.googleads.v8.resources.keyword_view_pb2.KeywordView,
        )
