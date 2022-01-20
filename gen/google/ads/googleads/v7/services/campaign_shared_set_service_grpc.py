# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/campaign_shared_set_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.enums.response_content_type_pb2
import google.ads.googleads.v7.resources.campaign_shared_set_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.rpc.status_pb2
import google.ads.googleads.v7.services.campaign_shared_set_service_pb2


class CampaignSharedSetServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCampaignSharedSet(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.campaign_shared_set_service_pb2.GetCampaignSharedSetRequest, google.ads.googleads.v7.resources.campaign_shared_set_pb2.CampaignSharedSet]') -> None:
        pass

    @abc.abstractmethod
    async def MutateCampaignSharedSets(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.campaign_shared_set_service_pb2.MutateCampaignSharedSetsRequest, google.ads.googleads.v7.services.campaign_shared_set_service_pb2.MutateCampaignSharedSetsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.CampaignSharedSetService/GetCampaignSharedSet': grpclib.const.Handler(
                self.GetCampaignSharedSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.campaign_shared_set_service_pb2.GetCampaignSharedSetRequest,
                google.ads.googleads.v7.resources.campaign_shared_set_pb2.CampaignSharedSet,
            ),
            '/google.ads.googleads.v7.services.CampaignSharedSetService/MutateCampaignSharedSets': grpclib.const.Handler(
                self.MutateCampaignSharedSets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.campaign_shared_set_service_pb2.MutateCampaignSharedSetsRequest,
                google.ads.googleads.v7.services.campaign_shared_set_service_pb2.MutateCampaignSharedSetsResponse,
            ),
        }


class CampaignSharedSetServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCampaignSharedSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.CampaignSharedSetService/GetCampaignSharedSet',
            google.ads.googleads.v7.services.campaign_shared_set_service_pb2.GetCampaignSharedSetRequest,
            google.ads.googleads.v7.resources.campaign_shared_set_pb2.CampaignSharedSet,
        )
        self.MutateCampaignSharedSets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.CampaignSharedSetService/MutateCampaignSharedSets',
            google.ads.googleads.v7.services.campaign_shared_set_service_pb2.MutateCampaignSharedSetsRequest,
            google.ads.googleads.v7.services.campaign_shared_set_service_pb2.MutateCampaignSharedSetsResponse,
        )
