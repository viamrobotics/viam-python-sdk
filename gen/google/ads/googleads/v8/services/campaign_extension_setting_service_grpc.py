# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/campaign_extension_setting_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.enums.response_content_type_pb2
import google.ads.googleads.v8.resources.campaign_extension_setting_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v8.services.campaign_extension_setting_service_pb2


class CampaignExtensionSettingServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCampaignExtensionSetting(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.GetCampaignExtensionSettingRequest, google.ads.googleads.v8.resources.campaign_extension_setting_pb2.CampaignExtensionSetting]') -> None:
        pass

    @abc.abstractmethod
    async def MutateCampaignExtensionSettings(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingsRequest, google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.CampaignExtensionSettingService/GetCampaignExtensionSetting': grpclib.const.Handler(
                self.GetCampaignExtensionSetting,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.GetCampaignExtensionSettingRequest,
                google.ads.googleads.v8.resources.campaign_extension_setting_pb2.CampaignExtensionSetting,
            ),
            '/google.ads.googleads.v8.services.CampaignExtensionSettingService/MutateCampaignExtensionSettings': grpclib.const.Handler(
                self.MutateCampaignExtensionSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingsRequest,
                google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingsResponse,
            ),
        }


class CampaignExtensionSettingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCampaignExtensionSetting = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.CampaignExtensionSettingService/GetCampaignExtensionSetting',
            google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.GetCampaignExtensionSettingRequest,
            google.ads.googleads.v8.resources.campaign_extension_setting_pb2.CampaignExtensionSetting,
        )
        self.MutateCampaignExtensionSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.CampaignExtensionSettingService/MutateCampaignExtensionSettings',
            google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingsRequest,
            google.ads.googleads.v8.services.campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingsResponse,
        )
