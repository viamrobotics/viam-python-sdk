# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/common/frequency_cap.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.enums import frequency_cap_event_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_frequency__cap__event__type__pb2
from google.ads.googleads.v8.enums import frequency_cap_level_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_frequency__cap__level__pb2
from google.ads.googleads.v8.enums import frequency_cap_time_unit_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_frequency__cap__time__unit__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v8/common/frequency_cap.proto\x12\x1egoogle.ads.googleads.v8.common\x1a<google/ads/googleads/v8/enums/frequency_cap_event_type.proto\x1a\x37google/ads/googleads/v8/enums/frequency_cap_level.proto\x1a;google/ads/googleads/v8/enums/frequency_cap_time_unit.proto\x1a\x1cgoogle/api/annotations.proto\"u\n\x11\x46requencyCapEntry\x12\x41\n\x03key\x18\x01 \x01(\x0b\x32/.google.ads.googleads.v8.common.FrequencyCapKeyR\x03key\x12\x15\n\x03\x63\x61p\x18\x03 \x01(\x05H\x00R\x03\x63\x61p\x88\x01\x01\x42\x06\n\x04_cap\"\xff\x02\n\x0f\x46requencyCapKey\x12\\\n\x05level\x18\x01 \x01(\x0e\x32\x46.google.ads.googleads.v8.enums.FrequencyCapLevelEnum.FrequencyCapLevelR\x05level\x12m\n\nevent_type\x18\x03 \x01(\x0e\x32N.google.ads.googleads.v8.enums.FrequencyCapEventTypeEnum.FrequencyCapEventTypeR\teventType\x12i\n\ttime_unit\x18\x02 \x01(\x0e\x32L.google.ads.googleads.v8.enums.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnitR\x08timeUnit\x12$\n\x0btime_length\x18\x05 \x01(\x05H\x00R\ntimeLength\x88\x01\x01\x42\x0e\n\x0c_time_lengthB\xec\x01\n\"com.google.ads.googleads.v8.commonB\x11\x46requencyCapProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Common\xea\x02\"Google::Ads::GoogleAds::V8::Commonb\x06proto3')



_FREQUENCYCAPENTRY = DESCRIPTOR.message_types_by_name['FrequencyCapEntry']
_FREQUENCYCAPKEY = DESCRIPTOR.message_types_by_name['FrequencyCapKey']
FrequencyCapEntry = _reflection.GeneratedProtocolMessageType('FrequencyCapEntry', (_message.Message,), {
  'DESCRIPTOR' : _FREQUENCYCAPENTRY,
  '__module__' : 'google.ads.googleads.v8.common.frequency_cap_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.FrequencyCapEntry)
  })
_sym_db.RegisterMessage(FrequencyCapEntry)

FrequencyCapKey = _reflection.GeneratedProtocolMessageType('FrequencyCapKey', (_message.Message,), {
  'DESCRIPTOR' : _FREQUENCYCAPKEY,
  '__module__' : 'google.ads.googleads.v8.common.frequency_cap_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.FrequencyCapKey)
  })
_sym_db.RegisterMessage(FrequencyCapKey)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v8.commonB\021FrequencyCapProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Common\312\002\036Google\\Ads\\GoogleAds\\V8\\Common\352\002\"Google::Ads::GoogleAds::V8::Common'
  _FREQUENCYCAPENTRY._serialized_start=296
  _FREQUENCYCAPENTRY._serialized_end=413
  _FREQUENCYCAPKEY._serialized_start=416
  _FREQUENCYCAPKEY._serialized_end=799
# @@protoc_insertion_point(module_scope)
