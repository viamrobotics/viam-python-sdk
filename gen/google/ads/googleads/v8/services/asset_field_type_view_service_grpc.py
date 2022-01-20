# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/asset_field_type_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.asset_field_type_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v8.services.asset_field_type_view_service_pb2


class AssetFieldTypeViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAssetFieldTypeView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.asset_field_type_view_service_pb2.GetAssetFieldTypeViewRequest, google.ads.googleads.v8.resources.asset_field_type_view_pb2.AssetFieldTypeView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.AssetFieldTypeViewService/GetAssetFieldTypeView': grpclib.const.Handler(
                self.GetAssetFieldTypeView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.asset_field_type_view_service_pb2.GetAssetFieldTypeViewRequest,
                google.ads.googleads.v8.resources.asset_field_type_view_pb2.AssetFieldTypeView,
            ),
        }


class AssetFieldTypeViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAssetFieldTypeView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.AssetFieldTypeViewService/GetAssetFieldTypeView',
            google.ads.googleads.v8.services.asset_field_type_view_service_pb2.GetAssetFieldTypeViewRequest,
            google.ads.googleads.v8.resources.asset_field_type_view_pb2.AssetFieldTypeView,
        )
