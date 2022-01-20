# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/resources/ad_group_extension_setting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.enums import extension_setting_device_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_extension__setting__device__pb2
from google.ads.googleads.v7.enums import extension_type_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_extension__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/ads/googleads/v7/resources/ad_group_extension_setting.proto\x12!google.ads.googleads.v7.resources\x1a<google/ads/googleads/v7/enums/extension_setting_device.proto\x1a\x32google/ads/googleads/v7/enums/extension_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x95\x05\n\x17\x41\x64GroupExtensionSetting\x12^\n\rresource_name\x18\x01 \x01(\tB9\xe2\x41\x01\x05\xfa\x41\x32\n0googleads.googleapis.com/AdGroupExtensionSettingR\x0cresourceName\x12k\n\x0e\x65xtension_type\x18\x02 \x01(\x0e\x32>.google.ads.googleads.v7.enums.ExtensionTypeEnum.ExtensionTypeB\x04\xe2\x41\x01\x05R\rextensionType\x12I\n\x08\x61\x64_group\x18\x06 \x01(\tB)\xe2\x41\x01\x05\xfa\x41\"\n googleads.googleapis.com/AdGroupH\x00R\x07\x61\x64Group\x88\x01\x01\x12\x61\n\x14\x65xtension_feed_items\x18\x07 \x03(\tB/\xfa\x41,\n*googleads.googleapis.com/ExtensionFeedItemR\x12\x65xtensionFeedItems\x12h\n\x06\x64\x65vice\x18\x05 \x01(\x0e\x32P.google.ads.googleads.v7.enums.ExtensionSettingDeviceEnum.ExtensionSettingDeviceR\x06\x64\x65vice:\x87\x01\xea\x41\x83\x01\n0googleads.googleapis.com/AdGroupExtensionSetting\x12Ocustomers/{customer_id}/adGroupExtensionSettings/{ad_group_id}~{extension_type}B\x0b\n\t_ad_groupB\x89\x02\n%com.google.ads.googleads.v7.resourcesB\x1c\x41\x64GroupExtensionSettingProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V7.Resources\xca\x02!Google\\Ads\\GoogleAds\\V7\\Resources\xea\x02%Google::Ads::GoogleAds::V7::Resourcesb\x06proto3')



_ADGROUPEXTENSIONSETTING = DESCRIPTOR.message_types_by_name['AdGroupExtensionSetting']
AdGroupExtensionSetting = _reflection.GeneratedProtocolMessageType('AdGroupExtensionSetting', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPEXTENSIONSETTING,
  '__module__' : 'google.ads.googleads.v7.resources.ad_group_extension_setting_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.resources.AdGroupExtensionSetting)
  })
_sym_db.RegisterMessage(AdGroupExtensionSetting)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v7.resourcesB\034AdGroupExtensionSettingProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V7.Resources\312\002!Google\\Ads\\GoogleAds\\V7\\Resources\352\002%Google::Ads::GoogleAds::V7::Resources'
  _ADGROUPEXTENSIONSETTING.fields_by_name['resource_name']._options = None
  _ADGROUPEXTENSIONSETTING.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A2\n0googleads.googleapis.com/AdGroupExtensionSetting'
  _ADGROUPEXTENSIONSETTING.fields_by_name['extension_type']._options = None
  _ADGROUPEXTENSIONSETTING.fields_by_name['extension_type']._serialized_options = b'\342A\001\005'
  _ADGROUPEXTENSIONSETTING.fields_by_name['ad_group']._options = None
  _ADGROUPEXTENSIONSETTING.fields_by_name['ad_group']._serialized_options = b'\342A\001\005\372A\"\n googleads.googleapis.com/AdGroup'
  _ADGROUPEXTENSIONSETTING.fields_by_name['extension_feed_items']._options = None
  _ADGROUPEXTENSIONSETTING.fields_by_name['extension_feed_items']._serialized_options = b'\372A,\n*googleads.googleapis.com/ExtensionFeedItem'
  _ADGROUPEXTENSIONSETTING._options = None
  _ADGROUPEXTENSIONSETTING._serialized_options = b'\352A\203\001\n0googleads.googleapis.com/AdGroupExtensionSetting\022Ocustomers/{customer_id}/adGroupExtensionSettings/{ad_group_id}~{extension_type}'
  _ADGROUPEXTENSIONSETTING._serialized_start=310
  _ADGROUPEXTENSIONSETTING._serialized_end=971
# @@protoc_insertion_point(module_scope)
