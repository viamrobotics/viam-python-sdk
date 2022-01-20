# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/smart_campaign_setting_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.enums.response_content_type_pb2
import google.ads.googleads.v8.resources.smart_campaign_setting_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v8.services.smart_campaign_setting_service_pb2


class SmartCampaignSettingServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetSmartCampaignSetting(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.GetSmartCampaignSettingRequest, google.ads.googleads.v8.resources.smart_campaign_setting_pb2.SmartCampaignSetting]') -> None:
        pass

    @abc.abstractmethod
    async def MutateSmartCampaignSettings(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.MutateSmartCampaignSettingsRequest, google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.MutateSmartCampaignSettingsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.SmartCampaignSettingService/GetSmartCampaignSetting': grpclib.const.Handler(
                self.GetSmartCampaignSetting,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.GetSmartCampaignSettingRequest,
                google.ads.googleads.v8.resources.smart_campaign_setting_pb2.SmartCampaignSetting,
            ),
            '/google.ads.googleads.v8.services.SmartCampaignSettingService/MutateSmartCampaignSettings': grpclib.const.Handler(
                self.MutateSmartCampaignSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.MutateSmartCampaignSettingsRequest,
                google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.MutateSmartCampaignSettingsResponse,
            ),
        }


class SmartCampaignSettingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSmartCampaignSetting = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.SmartCampaignSettingService/GetSmartCampaignSetting',
            google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.GetSmartCampaignSettingRequest,
            google.ads.googleads.v8.resources.smart_campaign_setting_pb2.SmartCampaignSetting,
        )
        self.MutateSmartCampaignSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.SmartCampaignSettingService/MutateSmartCampaignSettings',
            google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.MutateSmartCampaignSettingsRequest,
            google.ads.googleads.v8.services.smart_campaign_setting_service_pb2.MutateSmartCampaignSettingsResponse,
        )
