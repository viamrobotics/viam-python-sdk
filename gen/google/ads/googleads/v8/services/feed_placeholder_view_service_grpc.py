# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/feed_placeholder_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.feed_placeholder_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v8.services.feed_placeholder_view_service_pb2


class FeedPlaceholderViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetFeedPlaceholderView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.feed_placeholder_view_service_pb2.GetFeedPlaceholderViewRequest, google.ads.googleads.v8.resources.feed_placeholder_view_pb2.FeedPlaceholderView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.FeedPlaceholderViewService/GetFeedPlaceholderView': grpclib.const.Handler(
                self.GetFeedPlaceholderView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.feed_placeholder_view_service_pb2.GetFeedPlaceholderViewRequest,
                google.ads.googleads.v8.resources.feed_placeholder_view_pb2.FeedPlaceholderView,
            ),
        }


class FeedPlaceholderViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetFeedPlaceholderView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.FeedPlaceholderViewService/GetFeedPlaceholderView',
            google.ads.googleads.v8.services.feed_placeholder_view_service_pb2.GetFeedPlaceholderViewRequest,
            google.ads.googleads.v8.resources.feed_placeholder_view_pb2.FeedPlaceholderView,
        )
