# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/detail_placement_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.detail_placement_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v9.services.detail_placement_view_service_pb2


class DetailPlacementViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetDetailPlacementView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.detail_placement_view_service_pb2.GetDetailPlacementViewRequest, google.ads.googleads.v9.resources.detail_placement_view_pb2.DetailPlacementView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.DetailPlacementViewService/GetDetailPlacementView': grpclib.const.Handler(
                self.GetDetailPlacementView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.detail_placement_view_service_pb2.GetDetailPlacementViewRequest,
                google.ads.googleads.v9.resources.detail_placement_view_pb2.DetailPlacementView,
            ),
        }


class DetailPlacementViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetDetailPlacementView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.DetailPlacementViewService/GetDetailPlacementView',
            google.ads.googleads.v9.services.detail_placement_view_service_pb2.GetDetailPlacementViewRequest,
            google.ads.googleads.v9.resources.detail_placement_view_pb2.DetailPlacementView,
        )
