# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/parental_status_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.parental_status_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v9.services.parental_status_view_service_pb2


class ParentalStatusViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetParentalStatusView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.parental_status_view_service_pb2.GetParentalStatusViewRequest, google.ads.googleads.v9.resources.parental_status_view_pb2.ParentalStatusView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.ParentalStatusViewService/GetParentalStatusView': grpclib.const.Handler(
                self.GetParentalStatusView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.parental_status_view_service_pb2.GetParentalStatusViewRequest,
                google.ads.googleads.v9.resources.parental_status_view_pb2.ParentalStatusView,
            ),
        }


class ParentalStatusViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetParentalStatusView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.ParentalStatusViewService/GetParentalStatusView',
            google.ads.googleads.v9.services.parental_status_view_service_pb2.GetParentalStatusViewRequest,
            google.ads.googleads.v9.resources.parental_status_view_pb2.ParentalStatusView,
        )
