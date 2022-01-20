# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/topic_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.resources.topic_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v7.services.topic_view_service_pb2


class TopicViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetTopicView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.topic_view_service_pb2.GetTopicViewRequest, google.ads.googleads.v7.resources.topic_view_pb2.TopicView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.TopicViewService/GetTopicView': grpclib.const.Handler(
                self.GetTopicView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.topic_view_service_pb2.GetTopicViewRequest,
                google.ads.googleads.v7.resources.topic_view_pb2.TopicView,
            ),
        }


class TopicViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetTopicView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.TopicViewService/GetTopicView',
            google.ads.googleads.v7.services.topic_view_service_pb2.GetTopicViewRequest,
            google.ads.googleads.v7.resources.topic_view_pb2.TopicView,
        )
