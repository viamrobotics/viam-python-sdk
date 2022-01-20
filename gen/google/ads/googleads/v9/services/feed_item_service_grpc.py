# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/feed_item_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.feed_item_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v9.services.feed_item_service_pb2


class FeedItemServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetFeedItem(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.feed_item_service_pb2.GetFeedItemRequest, google.ads.googleads.v9.resources.feed_item_pb2.FeedItem]') -> None:
        pass

    @abc.abstractmethod
    async def MutateFeedItems(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.feed_item_service_pb2.MutateFeedItemsRequest, google.ads.googleads.v9.services.feed_item_service_pb2.MutateFeedItemsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.FeedItemService/GetFeedItem': grpclib.const.Handler(
                self.GetFeedItem,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.feed_item_service_pb2.GetFeedItemRequest,
                google.ads.googleads.v9.resources.feed_item_pb2.FeedItem,
            ),
            '/google.ads.googleads.v9.services.FeedItemService/MutateFeedItems': grpclib.const.Handler(
                self.MutateFeedItems,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.feed_item_service_pb2.MutateFeedItemsRequest,
                google.ads.googleads.v9.services.feed_item_service_pb2.MutateFeedItemsResponse,
            ),
        }


class FeedItemServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetFeedItem = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.FeedItemService/GetFeedItem',
            google.ads.googleads.v9.services.feed_item_service_pb2.GetFeedItemRequest,
            google.ads.googleads.v9.resources.feed_item_pb2.FeedItem,
        )
        self.MutateFeedItems = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.FeedItemService/MutateFeedItems',
            google.ads.googleads.v9.services.feed_item_service_pb2.MutateFeedItemsRequest,
            google.ads.googleads.v9.services.feed_item_service_pb2.MutateFeedItemsResponse,
        )
