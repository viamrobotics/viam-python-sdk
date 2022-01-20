# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dataqna/v1alpha/auto_suggestion_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.dataqna.v1alpha import annotated_string_pb2 as google_dot_cloud_dot_dataqna_dot_v1alpha_dot_annotated__string__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/dataqna/v1alpha/auto_suggestion_service.proto\x12\x1cgoogle.cloud.dataqna.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x33google/cloud/dataqna/v1alpha/annotated_string.proto\x1a\x17google/api/client.proto\"\xe2\x01\n\x15SuggestQueriesRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x16\n\x06scopes\x18\x02 \x03(\tR\x06scopes\x12\x14\n\x05query\x18\x03 \x01(\tR\x05query\x12W\n\x10suggestion_types\x18\x04 \x03(\x0e\x32,.google.cloud.dataqna.v1alpha.SuggestionTypeR\x0fsuggestionTypes\"\xdf\x01\n\nSuggestion\x12U\n\x0fsuggestion_info\x18\x01 \x01(\x0b\x32,.google.cloud.dataqna.v1alpha.SuggestionInfoR\x0esuggestionInfo\x12#\n\rranking_score\x18\x02 \x01(\x01R\x0crankingScore\x12U\n\x0fsuggestion_type\x18\x03 \x01(\x0e\x32,.google.cloud.dataqna.v1alpha.SuggestionTypeR\x0esuggestionType\"\x9e\x02\n\x0eSuggestionInfo\x12`\n\x14\x61nnotated_suggestion\x18\x01 \x01(\x0b\x32-.google.cloud.dataqna.v1alpha.AnnotatedStringR\x13\x61nnotatedSuggestion\x12[\n\rquery_matches\x18\x02 \x03(\x0b\x32\x36.google.cloud.dataqna.v1alpha.SuggestionInfo.MatchInfoR\x0cqueryMatches\x1aM\n\tMatchInfo\x12(\n\x10start_char_index\x18\x01 \x01(\x05R\x0estartCharIndex\x12\x16\n\x06length\x18\x02 \x01(\x05R\x06length\"d\n\x16SuggestQueriesResponse\x12J\n\x0bsuggestions\x18\x01 \x03(\x0b\x32(.google.cloud.dataqna.v1alpha.SuggestionR\x0bsuggestions*K\n\x0eSuggestionType\x12\x1f\n\x1bSUGGESTION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06\x45NTITY\x10\x01\x12\x0c\n\x08TEMPLATE\x10\x02\x32\xa5\x02\n\x15\x41utoSuggestionService\x12\xbf\x01\n\x0eSuggestQueries\x12\x33.google.cloud.dataqna.v1alpha.SuggestQueriesRequest\x1a\x34.google.cloud.dataqna.v1alpha.SuggestQueriesResponse\"B\x82\xd3\xe4\x93\x02<\"7/v1alpha/{parent=projects/*/locations/*}:suggestQueries:\x01*\x1aJ\xca\x41\x16\x64\x61taqna.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xe5\x01\n com.google.cloud.dataqna.v1alphaB\x1a\x41utoSuggestionServiceProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/dataqna/v1alpha;dataqna\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alphab\x06proto3')

_SUGGESTIONTYPE = DESCRIPTOR.enum_types_by_name['SuggestionType']
SuggestionType = enum_type_wrapper.EnumTypeWrapper(_SUGGESTIONTYPE)
SUGGESTION_TYPE_UNSPECIFIED = 0
ENTITY = 1
TEMPLATE = 2


_SUGGESTQUERIESREQUEST = DESCRIPTOR.message_types_by_name['SuggestQueriesRequest']
_SUGGESTION = DESCRIPTOR.message_types_by_name['Suggestion']
_SUGGESTIONINFO = DESCRIPTOR.message_types_by_name['SuggestionInfo']
_SUGGESTIONINFO_MATCHINFO = _SUGGESTIONINFO.nested_types_by_name['MatchInfo']
_SUGGESTQUERIESRESPONSE = DESCRIPTOR.message_types_by_name['SuggestQueriesResponse']
SuggestQueriesRequest = _reflection.GeneratedProtocolMessageType('SuggestQueriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTQUERIESREQUEST,
  '__module__' : 'google.cloud.dataqna.v1alpha.auto_suggestion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataqna.v1alpha.SuggestQueriesRequest)
  })
_sym_db.RegisterMessage(SuggestQueriesRequest)

Suggestion = _reflection.GeneratedProtocolMessageType('Suggestion', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTION,
  '__module__' : 'google.cloud.dataqna.v1alpha.auto_suggestion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataqna.v1alpha.Suggestion)
  })
_sym_db.RegisterMessage(Suggestion)

SuggestionInfo = _reflection.GeneratedProtocolMessageType('SuggestionInfo', (_message.Message,), {

  'MatchInfo' : _reflection.GeneratedProtocolMessageType('MatchInfo', (_message.Message,), {
    'DESCRIPTOR' : _SUGGESTIONINFO_MATCHINFO,
    '__module__' : 'google.cloud.dataqna.v1alpha.auto_suggestion_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dataqna.v1alpha.SuggestionInfo.MatchInfo)
    })
  ,
  'DESCRIPTOR' : _SUGGESTIONINFO,
  '__module__' : 'google.cloud.dataqna.v1alpha.auto_suggestion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataqna.v1alpha.SuggestionInfo)
  })
_sym_db.RegisterMessage(SuggestionInfo)
_sym_db.RegisterMessage(SuggestionInfo.MatchInfo)

SuggestQueriesResponse = _reflection.GeneratedProtocolMessageType('SuggestQueriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTQUERIESRESPONSE,
  '__module__' : 'google.cloud.dataqna.v1alpha.auto_suggestion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataqna.v1alpha.SuggestQueriesResponse)
  })
_sym_db.RegisterMessage(SuggestQueriesResponse)

_AUTOSUGGESTIONSERVICE = DESCRIPTOR.services_by_name['AutoSuggestionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.google.cloud.dataqna.v1alphaB\032AutoSuggestionServiceProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/dataqna/v1alpha;dataqna\252\002\034Google.Cloud.DataQnA.V1Alpha\312\002\034Google\\Cloud\\DataQnA\\V1alpha\352\002\037Google::Cloud::DataQnA::V1alpha'
  _SUGGESTQUERIESREQUEST.fields_by_name['parent']._options = None
  _SUGGESTQUERIESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _AUTOSUGGESTIONSERVICE._options = None
  _AUTOSUGGESTIONSERVICE._serialized_options = b'\312A\026dataqna.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _AUTOSUGGESTIONSERVICE.methods_by_name['SuggestQueries']._options = None
  _AUTOSUGGESTIONSERVICE.methods_by_name['SuggestQueries']._serialized_options = b'\202\323\344\223\002<\"7/v1alpha/{parent=projects/*/locations/*}:suggestQueries:\001*'
  _SUGGESTIONTYPE._serialized_start=1106
  _SUGGESTIONTYPE._serialized_end=1181
  _SUGGESTQUERIESREQUEST._serialized_start=261
  _SUGGESTQUERIESREQUEST._serialized_end=487
  _SUGGESTION._serialized_start=490
  _SUGGESTION._serialized_end=713
  _SUGGESTIONINFO._serialized_start=716
  _SUGGESTIONINFO._serialized_end=1002
  _SUGGESTIONINFO_MATCHINFO._serialized_start=925
  _SUGGESTIONINFO_MATCHINFO._serialized_end=1002
  _SUGGESTQUERIESRESPONSE._serialized_start=1004
  _SUGGESTQUERIESRESPONSE._serialized_end=1104
  _AUTOSUGGESTIONSERVICE._serialized_start=1184
  _AUTOSUGGESTIONSERVICE._serialized_end=1477
# @@protoc_insertion_point(module_scope)
