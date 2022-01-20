# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/artifactregistry/v1beta2/tag.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/devtools/artifactregistry/v1beta2/tag.proto\x12(google.devtools.artifactregistry.v1beta2\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\"3\n\x03Tag\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\"}\n\x0fListTagsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"}\n\x10ListTagsResponse\x12\x41\n\x04tags\x18\x01 \x03(\x0b\x32-.google.devtools.artifactregistry.v1beta2.TagR\x04tags\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"#\n\rGetTagRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\x82\x01\n\x10\x43reateTagRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x15\n\x06tag_id\x18\x02 \x01(\tR\x05tagId\x12?\n\x03tag\x18\x03 \x01(\x0b\x32-.google.devtools.artifactregistry.v1beta2.TagR\x03tag\"\x90\x01\n\x10UpdateTagRequest\x12?\n\x03tag\x18\x01 \x01(\x0b\x32-.google.devtools.artifactregistry.v1beta2.TagR\x03tag\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"&\n\x10\x44\x65leteTagRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04nameB\x8f\x02\n,com.google.devtools.artifactregistry.v1beta2B\x08TagProtoP\x01ZXgoogle.golang.org/genproto/googleapis/devtools/artifactregistry/v1beta2;artifactregistry\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3')



_TAG = DESCRIPTOR.message_types_by_name['Tag']
_LISTTAGSREQUEST = DESCRIPTOR.message_types_by_name['ListTagsRequest']
_LISTTAGSRESPONSE = DESCRIPTOR.message_types_by_name['ListTagsResponse']
_GETTAGREQUEST = DESCRIPTOR.message_types_by_name['GetTagRequest']
_CREATETAGREQUEST = DESCRIPTOR.message_types_by_name['CreateTagRequest']
_UPDATETAGREQUEST = DESCRIPTOR.message_types_by_name['UpdateTagRequest']
_DELETETAGREQUEST = DESCRIPTOR.message_types_by_name['DeleteTagRequest']
Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.tag_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.Tag)
  })
_sym_db.RegisterMessage(Tag)

ListTagsRequest = _reflection.GeneratedProtocolMessageType('ListTagsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTAGSREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.tag_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.ListTagsRequest)
  })
_sym_db.RegisterMessage(ListTagsRequest)

ListTagsResponse = _reflection.GeneratedProtocolMessageType('ListTagsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTAGSRESPONSE,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.tag_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.ListTagsResponse)
  })
_sym_db.RegisterMessage(ListTagsResponse)

GetTagRequest = _reflection.GeneratedProtocolMessageType('GetTagRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTAGREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.tag_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.GetTagRequest)
  })
_sym_db.RegisterMessage(GetTagRequest)

CreateTagRequest = _reflection.GeneratedProtocolMessageType('CreateTagRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETAGREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.tag_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.CreateTagRequest)
  })
_sym_db.RegisterMessage(CreateTagRequest)

UpdateTagRequest = _reflection.GeneratedProtocolMessageType('UpdateTagRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETAGREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.tag_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.UpdateTagRequest)
  })
_sym_db.RegisterMessage(UpdateTagRequest)

DeleteTagRequest = _reflection.GeneratedProtocolMessageType('DeleteTagRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETAGREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.tag_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.DeleteTagRequest)
  })
_sym_db.RegisterMessage(DeleteTagRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n,com.google.devtools.artifactregistry.v1beta2B\010TagProtoP\001ZXgoogle.golang.org/genproto/googleapis/devtools/artifactregistry/v1beta2;artifactregistry\252\002%Google.Cloud.ArtifactRegistry.V1Beta2\312\002%Google\\Cloud\\ArtifactRegistry\\V1beta2\352\002(Google::Cloud::ArtifactRegistry::V1beta2'
  _TAG._serialized_start=160
  _TAG._serialized_end=211
  _LISTTAGSREQUEST._serialized_start=213
  _LISTTAGSREQUEST._serialized_end=338
  _LISTTAGSRESPONSE._serialized_start=340
  _LISTTAGSRESPONSE._serialized_end=465
  _GETTAGREQUEST._serialized_start=467
  _GETTAGREQUEST._serialized_end=502
  _CREATETAGREQUEST._serialized_start=505
  _CREATETAGREQUEST._serialized_end=635
  _UPDATETAGREQUEST._serialized_start=638
  _UPDATETAGREQUEST._serialized_end=782
  _DELETETAGREQUEST._serialized_start=784
  _DELETETAGREQUEST._serialized_end=822
# @@protoc_insertion_point(module_scope)
