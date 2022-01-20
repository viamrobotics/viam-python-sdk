# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/smart_campaign_setting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v8/resources/smart_campaign_setting.proto\x12!google.ads.googleads.v8.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xdd\x05\n\x14SmartCampaignSetting\x12[\n\rresource_name\x18\x01 \x01(\tB6\xe2\x41\x01\x05\xfa\x41/\n-googleads.googleapis.com/SmartCampaignSettingR\x0cresourceName\x12\x46\n\x08\x63\x61mpaign\x18\x02 \x01(\tB*\xe2\x41\x01\x03\xfa\x41#\n!googleads.googleapis.com/CampaignR\x08\x63\x61mpaign\x12\x66\n\x0cphone_number\x18\x03 \x01(\x0b\x32\x43.google.ads.googleads.v8.resources.SmartCampaignSetting.PhoneNumberR\x0bphoneNumber\x12\x1b\n\tfinal_url\x18\x04 \x01(\tR\x08\x66inalUrl\x12:\n\x19\x61\x64vertising_language_code\x18\x07 \x01(\tR\x17\x61\x64vertisingLanguageCode\x12%\n\rbusiness_name\x18\x05 \x01(\tH\x00R\x0c\x62usinessName\x12\x32\n\x14\x62usiness_location_id\x18\x06 \x01(\x03H\x00R\x12\x62usinessLocationId\x1a\x7f\n\x0bPhoneNumber\x12&\n\x0cphone_number\x18\x01 \x01(\tH\x00R\x0bphoneNumber\x88\x01\x01\x12&\n\x0c\x63ountry_code\x18\x02 \x01(\tH\x01R\x0b\x63ountryCode\x88\x01\x01\x42\x0f\n\r_phone_numberB\x0f\n\r_country_code:o\xea\x41l\n-googleads.googleapis.com/SmartCampaignSetting\x12;customers/{customer_id}/smartCampaignSettings/{campaign_id}B\x12\n\x10\x62usiness_settingB\x86\x02\n%com.google.ads.googleads.v8.resourcesB\x19SmartCampaignSettingProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_SMARTCAMPAIGNSETTING = DESCRIPTOR.message_types_by_name['SmartCampaignSetting']
_SMARTCAMPAIGNSETTING_PHONENUMBER = _SMARTCAMPAIGNSETTING.nested_types_by_name['PhoneNumber']
SmartCampaignSetting = _reflection.GeneratedProtocolMessageType('SmartCampaignSetting', (_message.Message,), {

  'PhoneNumber' : _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
    'DESCRIPTOR' : _SMARTCAMPAIGNSETTING_PHONENUMBER,
    '__module__' : 'google.ads.googleads.v8.resources.smart_campaign_setting_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.SmartCampaignSetting.PhoneNumber)
    })
  ,
  'DESCRIPTOR' : _SMARTCAMPAIGNSETTING,
  '__module__' : 'google.ads.googleads.v8.resources.smart_campaign_setting_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.SmartCampaignSetting)
  })
_sym_db.RegisterMessage(SmartCampaignSetting)
_sym_db.RegisterMessage(SmartCampaignSetting.PhoneNumber)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\031SmartCampaignSettingProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _SMARTCAMPAIGNSETTING.fields_by_name['resource_name']._options = None
  _SMARTCAMPAIGNSETTING.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A/\n-googleads.googleapis.com/SmartCampaignSetting'
  _SMARTCAMPAIGNSETTING.fields_by_name['campaign']._options = None
  _SMARTCAMPAIGNSETTING.fields_by_name['campaign']._serialized_options = b'\342A\001\003\372A#\n!googleads.googleapis.com/Campaign'
  _SMARTCAMPAIGNSETTING._options = None
  _SMARTCAMPAIGNSETTING._serialized_options = b'\352Al\n-googleads.googleapis.com/SmartCampaignSetting\022;customers/{customer_id}/smartCampaignSettings/{campaign_id}'
  _SMARTCAMPAIGNSETTING._serialized_start=192
  _SMARTCAMPAIGNSETTING._serialized_end=925
  _SMARTCAMPAIGNSETTING_PHONENUMBER._serialized_start=665
  _SMARTCAMPAIGNSETTING_PHONENUMBER._serialized_end=792
# @@protoc_insertion_point(module_scope)
