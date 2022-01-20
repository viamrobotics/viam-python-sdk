# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/ad_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.common.policy_pb2
import google.ads.googleads.v8.enums.response_content_type_pb2
import google.ads.googleads.v8.resources.ad_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v8.services.ad_service_pb2


class AdServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAd(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.ad_service_pb2.GetAdRequest, google.ads.googleads.v8.resources.ad_pb2.Ad]') -> None:
        pass

    @abc.abstractmethod
    async def MutateAds(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.ad_service_pb2.MutateAdsRequest, google.ads.googleads.v8.services.ad_service_pb2.MutateAdsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.AdService/GetAd': grpclib.const.Handler(
                self.GetAd,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.ad_service_pb2.GetAdRequest,
                google.ads.googleads.v8.resources.ad_pb2.Ad,
            ),
            '/google.ads.googleads.v8.services.AdService/MutateAds': grpclib.const.Handler(
                self.MutateAds,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.ad_service_pb2.MutateAdsRequest,
                google.ads.googleads.v8.services.ad_service_pb2.MutateAdsResponse,
            ),
        }


class AdServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAd = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.AdService/GetAd',
            google.ads.googleads.v8.services.ad_service_pb2.GetAdRequest,
            google.ads.googleads.v8.resources.ad_pb2.Ad,
        )
        self.MutateAds = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.AdService/MutateAds',
            google.ads.googleads.v8.services.ad_service_pb2.MutateAdsRequest,
            google.ads.googleads.v8.services.ad_service_pb2.MutateAdsResponse,
        )
