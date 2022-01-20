# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/campaign_draft_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v9/errors/campaign_draft_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xc8\x03\n\x16\x43\x61mpaignDraftErrorEnum\"\xad\x03\n\x12\x43\x61mpaignDraftError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x18\n\x14\x44UPLICATE_DRAFT_NAME\x10\x02\x12*\n&INVALID_STATUS_TRANSITION_FROM_REMOVED\x10\x03\x12+\n\'INVALID_STATUS_TRANSITION_FROM_PROMOTED\x10\x04\x12\x31\n-INVALID_STATUS_TRANSITION_FROM_PROMOTE_FAILED\x10\x05\x12 \n\x1c\x43USTOMER_CANNOT_CREATE_DRAFT\x10\x06\x12 \n\x1c\x43\x41MPAIGN_CANNOT_CREATE_DRAFT\x10\x07\x12\x18\n\x14INVALID_DRAFT_CHANGE\x10\x08\x12\x1d\n\x19INVALID_STATUS_TRANSITION\x10\t\x12-\n)MAX_NUMBER_OF_DRAFTS_PER_CAMPAIGN_REACHED\x10\n\x12\'\n#LIST_ERRORS_FOR_PROMOTED_DRAFT_ONLY\x10\x0b\x42\xf2\x01\n\"com.google.ads.googleads.v9.errorsB\x17\x43\x61mpaignDraftErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3')



_CAMPAIGNDRAFTERRORENUM = DESCRIPTOR.message_types_by_name['CampaignDraftErrorEnum']
_CAMPAIGNDRAFTERRORENUM_CAMPAIGNDRAFTERROR = _CAMPAIGNDRAFTERRORENUM.enum_types_by_name['CampaignDraftError']
CampaignDraftErrorEnum = _reflection.GeneratedProtocolMessageType('CampaignDraftErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNDRAFTERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.campaign_draft_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.CampaignDraftErrorEnum)
  })
_sym_db.RegisterMessage(CampaignDraftErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.errorsB\027CampaignDraftErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors'
  _CAMPAIGNDRAFTERRORENUM._serialized_start=124
  _CAMPAIGNDRAFTERRORENUM._serialized_end=580
  _CAMPAIGNDRAFTERRORENUM_CAMPAIGNDRAFTERROR._serialized_start=151
  _CAMPAIGNDRAFTERRORENUM_CAMPAIGNDRAFTERROR._serialized_end=580
# @@protoc_insertion_point(module_scope)
