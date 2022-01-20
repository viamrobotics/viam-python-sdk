# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/common/bidding.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import target_impression_share_location_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_target__impression__share__location__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/ads/googleads/v9/common/bidding.proto\x12\x1egoogle.ads.googleads.v9.common\x1a\x44google/ads/googleads/v9/enums/target_impression_share_location.proto\x1a\x1cgoogle/api/annotations.proto\"b\n\nCommission\x12\x39\n\x16\x63ommission_rate_micros\x18\x02 \x01(\x03H\x00R\x14\x63ommissionRateMicros\x88\x01\x01\x42\x19\n\x17_commission_rate_micros\"\r\n\x0b\x45nhancedCpc\"[\n\tManualCpc\x12\x35\n\x14\x65nhanced_cpc_enabled\x18\x02 \x01(\x08H\x00R\x12\x65nhancedCpcEnabled\x88\x01\x01\x42\x17\n\x15_enhanced_cpc_enabled\"\x0b\n\tManualCpm\"\x0b\n\tManualCpv\"\x9a\x01\n\x13MaximizeConversions\x12\x1d\n\ntarget_cpa\x18\x01 \x01(\x03R\ttargetCpa\x12\x33\n\x16\x63pc_bid_ceiling_micros\x18\x02 \x01(\x03R\x13\x63pcBidCeilingMicros\x12/\n\x14\x63pc_bid_floor_micros\x18\x03 \x01(\x03R\x11\x63pcBidFloorMicros\"\xa0\x01\n\x17MaximizeConversionValue\x12\x1f\n\x0btarget_roas\x18\x02 \x01(\x01R\ntargetRoas\x12\x33\n\x16\x63pc_bid_ceiling_micros\x18\x03 \x01(\x03R\x13\x63pcBidCeilingMicros\x12/\n\x14\x63pc_bid_floor_micros\x18\x04 \x01(\x03R\x11\x63pcBidFloorMicros\"\xf6\x01\n\tTargetCpa\x12/\n\x11target_cpa_micros\x18\x04 \x01(\x03H\x00R\x0ftargetCpaMicros\x88\x01\x01\x12\x38\n\x16\x63pc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01R\x13\x63pcBidCeilingMicros\x88\x01\x01\x12\x34\n\x14\x63pc_bid_floor_micros\x18\x06 \x01(\x03H\x02R\x11\x63pcBidFloorMicros\x88\x01\x01\x42\x14\n\x12_target_cpa_microsB\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_cpc_bid_floor_micros\"\x0b\n\tTargetCpm\"\xc4\x02\n\x15TargetImpressionShare\x12z\n\x08location\x18\x01 \x01(\x0e\x32^.google.ads.googleads.v9.enums.TargetImpressionShareLocationEnum.TargetImpressionShareLocationR\x08location\x12=\n\x18location_fraction_micros\x18\x04 \x01(\x03H\x00R\x16locationFractionMicros\x88\x01\x01\x12\x38\n\x16\x63pc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01R\x13\x63pcBidCeilingMicros\x88\x01\x01\x42\x1b\n\x19_location_fraction_microsB\x19\n\x17_cpc_bid_ceiling_micros\"\xe6\x01\n\nTargetRoas\x12$\n\x0btarget_roas\x18\x04 \x01(\x01H\x00R\ntargetRoas\x88\x01\x01\x12\x38\n\x16\x63pc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01R\x13\x63pcBidCeilingMicros\x88\x01\x01\x12\x34\n\x14\x63pc_bid_floor_micros\x18\x06 \x01(\x03H\x02R\x11\x63pcBidFloorMicros\x88\x01\x01\x42\x0e\n\x0c_target_roasB\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_cpc_bid_floor_micros\"\xb3\x01\n\x0bTargetSpend\x12\x37\n\x13target_spend_micros\x18\x03 \x01(\x03\x42\x02\x18\x01H\x00R\x11targetSpendMicros\x88\x01\x01\x12\x38\n\x16\x63pc_bid_ceiling_micros\x18\x04 \x01(\x03H\x01R\x13\x63pcBidCeilingMicros\x88\x01\x01\x42\x16\n\x14_target_spend_microsB\x19\n\x17_cpc_bid_ceiling_micros\"\xb1\x01\n\nPercentCpc\x12\x38\n\x16\x63pc_bid_ceiling_micros\x18\x03 \x01(\x03H\x00R\x13\x63pcBidCeilingMicros\x88\x01\x01\x12\x35\n\x14\x65nhanced_cpc_enabled\x18\x04 \x01(\x08H\x01R\x12\x65nhancedCpcEnabled\x88\x01\x01\x42\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_enhanced_cpc_enabledB\xe7\x01\n\"com.google.ads.googleads.v9.commonB\x0c\x42iddingProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Common\xea\x02\"Google::Ads::GoogleAds::V9::Commonb\x06proto3')



_COMMISSION = DESCRIPTOR.message_types_by_name['Commission']
_ENHANCEDCPC = DESCRIPTOR.message_types_by_name['EnhancedCpc']
_MANUALCPC = DESCRIPTOR.message_types_by_name['ManualCpc']
_MANUALCPM = DESCRIPTOR.message_types_by_name['ManualCpm']
_MANUALCPV = DESCRIPTOR.message_types_by_name['ManualCpv']
_MAXIMIZECONVERSIONS = DESCRIPTOR.message_types_by_name['MaximizeConversions']
_MAXIMIZECONVERSIONVALUE = DESCRIPTOR.message_types_by_name['MaximizeConversionValue']
_TARGETCPA = DESCRIPTOR.message_types_by_name['TargetCpa']
_TARGETCPM = DESCRIPTOR.message_types_by_name['TargetCpm']
_TARGETIMPRESSIONSHARE = DESCRIPTOR.message_types_by_name['TargetImpressionShare']
_TARGETROAS = DESCRIPTOR.message_types_by_name['TargetRoas']
_TARGETSPEND = DESCRIPTOR.message_types_by_name['TargetSpend']
_PERCENTCPC = DESCRIPTOR.message_types_by_name['PercentCpc']
Commission = _reflection.GeneratedProtocolMessageType('Commission', (_message.Message,), {
  'DESCRIPTOR' : _COMMISSION,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.Commission)
  })
_sym_db.RegisterMessage(Commission)

EnhancedCpc = _reflection.GeneratedProtocolMessageType('EnhancedCpc', (_message.Message,), {
  'DESCRIPTOR' : _ENHANCEDCPC,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.EnhancedCpc)
  })
_sym_db.RegisterMessage(EnhancedCpc)

ManualCpc = _reflection.GeneratedProtocolMessageType('ManualCpc', (_message.Message,), {
  'DESCRIPTOR' : _MANUALCPC,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.ManualCpc)
  })
_sym_db.RegisterMessage(ManualCpc)

ManualCpm = _reflection.GeneratedProtocolMessageType('ManualCpm', (_message.Message,), {
  'DESCRIPTOR' : _MANUALCPM,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.ManualCpm)
  })
_sym_db.RegisterMessage(ManualCpm)

ManualCpv = _reflection.GeneratedProtocolMessageType('ManualCpv', (_message.Message,), {
  'DESCRIPTOR' : _MANUALCPV,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.ManualCpv)
  })
_sym_db.RegisterMessage(ManualCpv)

MaximizeConversions = _reflection.GeneratedProtocolMessageType('MaximizeConversions', (_message.Message,), {
  'DESCRIPTOR' : _MAXIMIZECONVERSIONS,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.MaximizeConversions)
  })
_sym_db.RegisterMessage(MaximizeConversions)

MaximizeConversionValue = _reflection.GeneratedProtocolMessageType('MaximizeConversionValue', (_message.Message,), {
  'DESCRIPTOR' : _MAXIMIZECONVERSIONVALUE,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.MaximizeConversionValue)
  })
_sym_db.RegisterMessage(MaximizeConversionValue)

TargetCpa = _reflection.GeneratedProtocolMessageType('TargetCpa', (_message.Message,), {
  'DESCRIPTOR' : _TARGETCPA,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.TargetCpa)
  })
_sym_db.RegisterMessage(TargetCpa)

TargetCpm = _reflection.GeneratedProtocolMessageType('TargetCpm', (_message.Message,), {
  'DESCRIPTOR' : _TARGETCPM,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.TargetCpm)
  })
_sym_db.RegisterMessage(TargetCpm)

TargetImpressionShare = _reflection.GeneratedProtocolMessageType('TargetImpressionShare', (_message.Message,), {
  'DESCRIPTOR' : _TARGETIMPRESSIONSHARE,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.TargetImpressionShare)
  })
_sym_db.RegisterMessage(TargetImpressionShare)

TargetRoas = _reflection.GeneratedProtocolMessageType('TargetRoas', (_message.Message,), {
  'DESCRIPTOR' : _TARGETROAS,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.TargetRoas)
  })
_sym_db.RegisterMessage(TargetRoas)

TargetSpend = _reflection.GeneratedProtocolMessageType('TargetSpend', (_message.Message,), {
  'DESCRIPTOR' : _TARGETSPEND,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.TargetSpend)
  })
_sym_db.RegisterMessage(TargetSpend)

PercentCpc = _reflection.GeneratedProtocolMessageType('PercentCpc', (_message.Message,), {
  'DESCRIPTOR' : _PERCENTCPC,
  '__module__' : 'google.ads.googleads.v9.common.bidding_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.PercentCpc)
  })
_sym_db.RegisterMessage(PercentCpc)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.commonB\014BiddingProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Common\312\002\036Google\\Ads\\GoogleAds\\V9\\Common\352\002\"Google::Ads::GoogleAds::V9::Common'
  _TARGETSPEND.fields_by_name['target_spend_micros']._options = None
  _TARGETSPEND.fields_by_name['target_spend_micros']._serialized_options = b'\030\001'
  _COMMISSION._serialized_start=180
  _COMMISSION._serialized_end=278
  _ENHANCEDCPC._serialized_start=280
  _ENHANCEDCPC._serialized_end=293
  _MANUALCPC._serialized_start=295
  _MANUALCPC._serialized_end=386
  _MANUALCPM._serialized_start=388
  _MANUALCPM._serialized_end=399
  _MANUALCPV._serialized_start=401
  _MANUALCPV._serialized_end=412
  _MAXIMIZECONVERSIONS._serialized_start=415
  _MAXIMIZECONVERSIONS._serialized_end=569
  _MAXIMIZECONVERSIONVALUE._serialized_start=572
  _MAXIMIZECONVERSIONVALUE._serialized_end=732
  _TARGETCPA._serialized_start=735
  _TARGETCPA._serialized_end=981
  _TARGETCPM._serialized_start=983
  _TARGETCPM._serialized_end=994
  _TARGETIMPRESSIONSHARE._serialized_start=997
  _TARGETIMPRESSIONSHARE._serialized_end=1321
  _TARGETROAS._serialized_start=1324
  _TARGETROAS._serialized_end=1554
  _TARGETSPEND._serialized_start=1557
  _TARGETSPEND._serialized_end=1736
  _PERCENTCPC._serialized_start=1739
  _PERCENTCPC._serialized_end=1916
# @@protoc_insertion_point(module_scope)
