# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/hotel_group_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.hotel_group_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v9.services.hotel_group_view_service_pb2


class HotelGroupViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetHotelGroupView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.hotel_group_view_service_pb2.GetHotelGroupViewRequest, google.ads.googleads.v9.resources.hotel_group_view_pb2.HotelGroupView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.HotelGroupViewService/GetHotelGroupView': grpclib.const.Handler(
                self.GetHotelGroupView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.hotel_group_view_service_pb2.GetHotelGroupViewRequest,
                google.ads.googleads.v9.resources.hotel_group_view_pb2.HotelGroupView,
            ),
        }


class HotelGroupViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetHotelGroupView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.HotelGroupViewService/GetHotelGroupView',
            google.ads.googleads.v9.services.hotel_group_view_service_pb2.GetHotelGroupViewRequest,
            google.ads.googleads.v9.resources.hotel_group_view_pb2.HotelGroupView,
        )
