# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/resources/call_view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.enums import call_tracking_display_location_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_call__tracking__display__location__pb2
from google.ads.googleads.v7.enums import call_type_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_call__type__pb2
from google.ads.googleads.v7.enums import google_voice_call_status_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_google__voice__call__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v7/resources/call_view.proto\x12!google.ads.googleads.v7.resources\x1a\x42google/ads/googleads/v7/enums/call_tracking_display_location.proto\x1a-google/ads/googleads/v7/enums/call_type.proto\x1a<google/ads/googleads/v7/enums/google_voice_call_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xae\x06\n\x08\x43\x61llView\x12O\n\rresource_name\x18\x01 \x01(\tB*\xe2\x41\x01\x03\xfa\x41#\n!googleads.googleapis.com/CallViewR\x0cresourceName\x12\x32\n\x12\x63\x61ller_region_code\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x10\x63\x61llerRegionCode\x12.\n\x10\x63\x61ller_area_code\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x0e\x63\x61llerAreaCode\x12\x38\n\x15\x63\x61ll_duration_seconds\x18\x04 \x01(\x03\x42\x04\xe2\x41\x01\x03R\x13\x63\x61llDurationSeconds\x12\x35\n\x14start_call_date_time\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\x11startCallDateTime\x12\x31\n\x12\x65nd_call_date_time\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03R\x0f\x65ndCallDateTime\x12\xa5\x01\n\x1e\x63\x61ll_tracking_display_location\x18\x07 \x01(\x0e\x32Z.google.ads.googleads.v7.enums.CallTrackingDisplayLocationEnum.CallTrackingDisplayLocationB\x04\xe2\x41\x01\x03R\x1b\x63\x61llTrackingDisplayLocation\x12N\n\x04type\x18\x08 \x01(\x0e\x32\x34.google.ads.googleads.v7.enums.CallTypeEnum.CallTypeB\x04\xe2\x41\x01\x03R\x04type\x12u\n\x0b\x63\x61ll_status\x18\t \x01(\x0e\x32N.google.ads.googleads.v7.enums.GoogleVoiceCallStatusEnum.GoogleVoiceCallStatusB\x04\xe2\x41\x01\x03R\ncallStatus:Z\xea\x41W\n!googleads.googleapis.com/CallView\x12\x32\x63ustomers/{customer_id}/callViews/{call_detail_id}B\xfa\x01\n%com.google.ads.googleads.v7.resourcesB\rCallViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V7.Resources\xca\x02!Google\\Ads\\GoogleAds\\V7\\Resources\xea\x02%Google::Ads::GoogleAds::V7::Resourcesb\x06proto3')



_CALLVIEW = DESCRIPTOR.message_types_by_name['CallView']
CallView = _reflection.GeneratedProtocolMessageType('CallView', (_message.Message,), {
  'DESCRIPTOR' : _CALLVIEW,
  '__module__' : 'google.ads.googleads.v7.resources.call_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.resources.CallView)
  })
_sym_db.RegisterMessage(CallView)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v7.resourcesB\rCallViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V7.Resources\312\002!Google\\Ads\\GoogleAds\\V7\\Resources\352\002%Google::Ads::GoogleAds::V7::Resources'
  _CALLVIEW.fields_by_name['resource_name']._options = None
  _CALLVIEW.fields_by_name['resource_name']._serialized_options = b'\342A\001\003\372A#\n!googleads.googleapis.com/CallView'
  _CALLVIEW.fields_by_name['caller_region_code']._options = None
  _CALLVIEW.fields_by_name['caller_region_code']._serialized_options = b'\342A\001\003'
  _CALLVIEW.fields_by_name['caller_area_code']._options = None
  _CALLVIEW.fields_by_name['caller_area_code']._serialized_options = b'\342A\001\003'
  _CALLVIEW.fields_by_name['call_duration_seconds']._options = None
  _CALLVIEW.fields_by_name['call_duration_seconds']._serialized_options = b'\342A\001\003'
  _CALLVIEW.fields_by_name['start_call_date_time']._options = None
  _CALLVIEW.fields_by_name['start_call_date_time']._serialized_options = b'\342A\001\003'
  _CALLVIEW.fields_by_name['end_call_date_time']._options = None
  _CALLVIEW.fields_by_name['end_call_date_time']._serialized_options = b'\342A\001\003'
  _CALLVIEW.fields_by_name['call_tracking_display_location']._options = None
  _CALLVIEW.fields_by_name['call_tracking_display_location']._serialized_options = b'\342A\001\003'
  _CALLVIEW.fields_by_name['type']._options = None
  _CALLVIEW.fields_by_name['type']._serialized_options = b'\342A\001\003'
  _CALLVIEW.fields_by_name['call_status']._options = None
  _CALLVIEW.fields_by_name['call_status']._serialized_options = b'\342A\001\003'
  _CALLVIEW._options = None
  _CALLVIEW._serialized_options = b'\352AW\n!googleads.googleapis.com/CallView\0222customers/{customer_id}/callViews/{call_detail_id}'
  _CALLVIEW._serialized_start=356
  _CALLVIEW._serialized_end=1170
# @@protoc_insertion_point(module_scope)
