# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/custom_audience_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.custom_audience_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.ads.googleads.v9.services.custom_audience_service_pb2


class CustomAudienceServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCustomAudience(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.custom_audience_service_pb2.GetCustomAudienceRequest, google.ads.googleads.v9.resources.custom_audience_pb2.CustomAudience]') -> None:
        pass

    @abc.abstractmethod
    async def MutateCustomAudiences(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.custom_audience_service_pb2.MutateCustomAudiencesRequest, google.ads.googleads.v9.services.custom_audience_service_pb2.MutateCustomAudiencesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.CustomAudienceService/GetCustomAudience': grpclib.const.Handler(
                self.GetCustomAudience,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.custom_audience_service_pb2.GetCustomAudienceRequest,
                google.ads.googleads.v9.resources.custom_audience_pb2.CustomAudience,
            ),
            '/google.ads.googleads.v9.services.CustomAudienceService/MutateCustomAudiences': grpclib.const.Handler(
                self.MutateCustomAudiences,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.custom_audience_service_pb2.MutateCustomAudiencesRequest,
                google.ads.googleads.v9.services.custom_audience_service_pb2.MutateCustomAudiencesResponse,
            ),
        }


class CustomAudienceServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCustomAudience = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.CustomAudienceService/GetCustomAudience',
            google.ads.googleads.v9.services.custom_audience_service_pb2.GetCustomAudienceRequest,
            google.ads.googleads.v9.resources.custom_audience_pb2.CustomAudience,
        )
        self.MutateCustomAudiences = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.CustomAudienceService/MutateCustomAudiences',
            google.ads.googleads.v9.services.custom_audience_service_pb2.MutateCustomAudiencesRequest,
            google.ads.googleads.v9.services.custom_audience_service_pb2.MutateCustomAudiencesResponse,
        )
