# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/common/tag_snippet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import tracking_code_page_format_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_tracking__code__page__format__pb2
from google.ads.googleads.v9.enums import tracking_code_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_tracking__code__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/googleads/v9/common/tag_snippet.proto\x12\x1egoogle.ads.googleads.v9.common\x1a=google/ads/googleads/v9/enums/tracking_code_page_format.proto\x1a\x36google/ads/googleads/v9/enums/tracking_code_type.proto\x1a\x1cgoogle/api/annotations.proto\"\xd6\x02\n\nTagSnippet\x12X\n\x04type\x18\x01 \x01(\x0e\x32\x44.google.ads.googleads.v9.enums.TrackingCodeTypeEnum.TrackingCodeTypeR\x04type\x12q\n\x0bpage_format\x18\x02 \x01(\x0e\x32P.google.ads.googleads.v9.enums.TrackingCodePageFormatEnum.TrackingCodePageFormatR\npageFormat\x12+\n\x0fglobal_site_tag\x18\x05 \x01(\tH\x00R\rglobalSiteTag\x88\x01\x01\x12(\n\revent_snippet\x18\x06 \x01(\tH\x01R\x0c\x65ventSnippet\x88\x01\x01\x42\x12\n\x10_global_site_tagB\x10\n\x0e_event_snippetB\xea\x01\n\"com.google.ads.googleads.v9.commonB\x0fTagSnippetProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Common\xea\x02\"Google::Ads::GoogleAds::V9::Commonb\x06proto3')



_TAGSNIPPET = DESCRIPTOR.message_types_by_name['TagSnippet']
TagSnippet = _reflection.GeneratedProtocolMessageType('TagSnippet', (_message.Message,), {
  'DESCRIPTOR' : _TAGSNIPPET,
  '__module__' : 'google.ads.googleads.v9.common.tag_snippet_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.common.TagSnippet)
  })
_sym_db.RegisterMessage(TagSnippet)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.commonB\017TagSnippetProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Common\312\002\036Google\\Ads\\GoogleAds\\V9\\Common\352\002\"Google::Ads::GoogleAds::V9::Common'
  _TAGSNIPPET._serialized_start=234
  _TAGSNIPPET._serialized_end=576
# @@protoc_insertion_point(module_scope)
