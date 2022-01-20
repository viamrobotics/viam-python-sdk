# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/bidding_data_exclusion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_advertising__channel__type__pb2
from google.ads.googleads.v8.enums import device_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_device__pb2
from google.ads.googleads.v8.enums import seasonality_event_scope_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_seasonality__event__scope__pb2
from google.ads.googleads.v8.enums import seasonality_event_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_seasonality__event__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v8/resources/bidding_data_exclusion.proto\x12!google.ads.googleads.v8.resources\x1a<google/ads/googleads/v8/enums/advertising_channel_type.proto\x1a*google/ads/googleads/v8/enums/device.proto\x1a;google/ads/googleads/v8/enums/seasonality_event_scope.proto\x1a<google/ads/googleads/v8/enums/seasonality_event_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xa4\x07\n\x14\x42iddingDataExclusion\x12[\n\rresource_name\x18\x01 \x01(\tB6\xe2\x41\x01\x05\xfa\x41/\n-googleads.googleapis.com/BiddingDataExclusionR\x0cresourceName\x12\x30\n\x11\x64\x61ta_exclusion_id\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x03R\x0f\x64\x61taExclusionId\x12\x64\n\x05scope\x18\x03 \x01(\x0e\x32N.google.ads.googleads.v8.enums.SeasonalityEventScopeEnum.SeasonalityEventScopeR\x05scope\x12n\n\x06status\x18\x04 \x01(\x0e\x32P.google.ads.googleads.v8.enums.SeasonalityEventStatusEnum.SeasonalityEventStatusB\x04\xe2\x41\x01\x03R\x06status\x12,\n\x0fstart_date_time\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02R\rstartDateTime\x12(\n\rend_date_time\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x65ndDateTime\x12\x12\n\x04name\x18\x07 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12J\n\x07\x64\x65vices\x18\t \x03(\x0e\x32\x30.google.ads.googleads.v8.enums.DeviceEnum.DeviceR\x07\x64\x65vices\x12\x44\n\tcampaigns\x18\n \x03(\tB&\xfa\x41#\n!googleads.googleapis.com/CampaignR\tcampaigns\x12\x8c\x01\n\x19\x61\x64vertising_channel_types\x18\x0b \x03(\x0e\x32P.google.ads.googleads.v8.enums.AdvertisingChannelTypeEnum.AdvertisingChannelTypeR\x17\x61\x64vertisingChannelTypes:x\xea\x41u\n-googleads.googleapis.com/BiddingDataExclusion\x12\x44\x63ustomers/{customer_id}/biddingDataExclusions/{seasonality_event_id}B\x86\x02\n%com.google.ads.googleads.v8.resourcesB\x19\x42iddingDataExclusionProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_BIDDINGDATAEXCLUSION = DESCRIPTOR.message_types_by_name['BiddingDataExclusion']
BiddingDataExclusion = _reflection.GeneratedProtocolMessageType('BiddingDataExclusion', (_message.Message,), {
  'DESCRIPTOR' : _BIDDINGDATAEXCLUSION,
  '__module__' : 'google.ads.googleads.v8.resources.bidding_data_exclusion_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.BiddingDataExclusion)
  })
_sym_db.RegisterMessage(BiddingDataExclusion)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\031BiddingDataExclusionProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _BIDDINGDATAEXCLUSION.fields_by_name['resource_name']._options = None
  _BIDDINGDATAEXCLUSION.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A/\n-googleads.googleapis.com/BiddingDataExclusion'
  _BIDDINGDATAEXCLUSION.fields_by_name['data_exclusion_id']._options = None
  _BIDDINGDATAEXCLUSION.fields_by_name['data_exclusion_id']._serialized_options = b'\342A\001\003'
  _BIDDINGDATAEXCLUSION.fields_by_name['status']._options = None
  _BIDDINGDATAEXCLUSION.fields_by_name['status']._serialized_options = b'\342A\001\003'
  _BIDDINGDATAEXCLUSION.fields_by_name['start_date_time']._options = None
  _BIDDINGDATAEXCLUSION.fields_by_name['start_date_time']._serialized_options = b'\342A\001\002'
  _BIDDINGDATAEXCLUSION.fields_by_name['end_date_time']._options = None
  _BIDDINGDATAEXCLUSION.fields_by_name['end_date_time']._serialized_options = b'\342A\001\002'
  _BIDDINGDATAEXCLUSION.fields_by_name['campaigns']._options = None
  _BIDDINGDATAEXCLUSION.fields_by_name['campaigns']._serialized_options = b'\372A#\n!googleads.googleapis.com/Campaign'
  _BIDDINGDATAEXCLUSION._options = None
  _BIDDINGDATAEXCLUSION._serialized_options = b'\352Au\n-googleads.googleapis.com/BiddingDataExclusion\022Dcustomers/{customer_id}/biddingDataExclusions/{seasonality_event_id}'
  _BIDDINGDATAEXCLUSION._serialized_start=421
  _BIDDINGDATAEXCLUSION._serialized_end=1353
# @@protoc_insertion_point(module_scope)
