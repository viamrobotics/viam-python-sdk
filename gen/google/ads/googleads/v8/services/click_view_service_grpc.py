# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/click_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.click_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v8.services.click_view_service_pb2


class ClickViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetClickView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.click_view_service_pb2.GetClickViewRequest, google.ads.googleads.v8.resources.click_view_pb2.ClickView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.ClickViewService/GetClickView': grpclib.const.Handler(
                self.GetClickView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.click_view_service_pb2.GetClickViewRequest,
                google.ads.googleads.v8.resources.click_view_pb2.ClickView,
            ),
        }


class ClickViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetClickView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.ClickViewService/GetClickView',
            google.ads.googleads.v8.services.click_view_service_pb2.GetClickViewRequest,
            google.ads.googleads.v8.resources.click_view_pb2.ClickView,
        )
