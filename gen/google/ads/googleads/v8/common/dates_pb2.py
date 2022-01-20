# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/common/dates.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.enums import month_of_year_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_month__of__year__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/ads/googleads/v8/common/dates.proto\x12\x1egoogle.ads.googleads.v8.common\x1a\x31google/ads/googleads/v8/enums/month_of_year.proto\x1a\x1cgoogle/api/annotations.proto\"k\n\tDateRange\x12\"\n\nstart_date\x18\x03 \x01(\tH\x00R\tstartDate\x88\x01\x01\x12\x1e\n\x08\x65nd_date\x18\x04 \x01(\tH\x01R\x07\x65ndDate\x88\x01\x01\x42\r\n\x0b_start_dateB\x0b\n\t_end_date\"\x8e\x01\n\x0eYearMonthRange\x12?\n\x05start\x18\x01 \x01(\x0b\x32).google.ads.googleads.v8.common.YearMonthR\x05start\x12;\n\x03\x65nd\x18\x02 \x01(\x0b\x32).google.ads.googleads.v8.common.YearMonthR\x03\x65nd\"q\n\tYearMonth\x12\x12\n\x04year\x18\x01 \x01(\x03R\x04year\x12P\n\x05month\x18\x02 \x01(\x0e\x32:.google.ads.googleads.v8.enums.MonthOfYearEnum.MonthOfYearR\x05monthB\xe5\x01\n\"com.google.ads.googleads.v8.commonB\nDatesProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Common\xea\x02\"Google::Ads::GoogleAds::V8::Commonb\x06proto3')



_DATERANGE = DESCRIPTOR.message_types_by_name['DateRange']
_YEARMONTHRANGE = DESCRIPTOR.message_types_by_name['YearMonthRange']
_YEARMONTH = DESCRIPTOR.message_types_by_name['YearMonth']
DateRange = _reflection.GeneratedProtocolMessageType('DateRange', (_message.Message,), {
  'DESCRIPTOR' : _DATERANGE,
  '__module__' : 'google.ads.googleads.v8.common.dates_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.DateRange)
  })
_sym_db.RegisterMessage(DateRange)

YearMonthRange = _reflection.GeneratedProtocolMessageType('YearMonthRange', (_message.Message,), {
  'DESCRIPTOR' : _YEARMONTHRANGE,
  '__module__' : 'google.ads.googleads.v8.common.dates_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.YearMonthRange)
  })
_sym_db.RegisterMessage(YearMonthRange)

YearMonth = _reflection.GeneratedProtocolMessageType('YearMonth', (_message.Message,), {
  'DESCRIPTOR' : _YEARMONTH,
  '__module__' : 'google.ads.googleads.v8.common.dates_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.YearMonth)
  })
_sym_db.RegisterMessage(YearMonth)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v8.commonB\nDatesProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Common\312\002\036Google\\Ads\\GoogleAds\\V8\\Common\352\002\"Google::Ads::GoogleAds::V8::Common'
  _DATERANGE._serialized_start=159
  _DATERANGE._serialized_end=266
  _YEARMONTHRANGE._serialized_start=269
  _YEARMONTHRANGE._serialized_end=411
  _YEARMONTH._serialized_start=413
  _YEARMONTH._serialized_end=526
# @@protoc_insertion_point(module_scope)
