# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/apps/script/type/slides/slides_addon_manifest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/apps/script/type/slides/slides_addon_manifest.proto\x12\x1egoogle.apps.script.type.slides\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/apps/script/type/extension_point.proto\"\xe9\x01\n\x13SlidesAddOnManifest\x12Z\n\x10homepage_trigger\x18\x01 \x01(\x0b\x32/.google.apps.script.type.HomepageExtensionPointR\x0fhomepageTrigger\x12v\n\x1don_file_scope_granted_trigger\x18\x02 \x01(\x0b\x32\x34.google.apps.script.type.slides.SlidesExtensionPointR\x19onFileScopeGrantedTrigger\"?\n\x14SlidesExtensionPoint\x12\'\n\x0crun_function\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0brunFunctionB\xe6\x01\n\"com.google.apps.script.type.slidesB\x18SlidesAddOnManifestProtoP\x01Z=google.golang.org/genproto/googleapis/apps/script/type/slides\xaa\x02\x1eGoogle.Apps.Script.Type.Slides\xca\x02\x1eGoogle\\Apps\\Script\\Type\\Slides\xea\x02\"Google::Apps::Script::Type::Slidesb\x06proto3')



_SLIDESADDONMANIFEST = DESCRIPTOR.message_types_by_name['SlidesAddOnManifest']
_SLIDESEXTENSIONPOINT = DESCRIPTOR.message_types_by_name['SlidesExtensionPoint']
SlidesAddOnManifest = _reflection.GeneratedProtocolMessageType('SlidesAddOnManifest', (_message.Message,), {
  'DESCRIPTOR' : _SLIDESADDONMANIFEST,
  '__module__' : 'google.apps.script.type.slides.slides_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.slides.SlidesAddOnManifest)
  })
_sym_db.RegisterMessage(SlidesAddOnManifest)

SlidesExtensionPoint = _reflection.GeneratedProtocolMessageType('SlidesExtensionPoint', (_message.Message,), {
  'DESCRIPTOR' : _SLIDESEXTENSIONPOINT,
  '__module__' : 'google.apps.script.type.slides.slides_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.slides.SlidesExtensionPoint)
  })
_sym_db.RegisterMessage(SlidesExtensionPoint)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.apps.script.type.slidesB\030SlidesAddOnManifestProtoP\001Z=google.golang.org/genproto/googleapis/apps/script/type/slides\252\002\036Google.Apps.Script.Type.Slides\312\002\036Google\\Apps\\Script\\Type\\Slides\352\002\"Google::Apps::Script::Type::Slides'
  _SLIDESEXTENSIONPOINT.fields_by_name['run_function']._options = None
  _SLIDESEXTENSIONPOINT.fields_by_name['run_function']._serialized_options = b'\342A\001\002'
  _SLIDESADDONMANIFEST._serialized_start=175
  _SLIDESADDONMANIFEST._serialized_end=408
  _SLIDESEXTENSIONPOINT._serialized_start=410
  _SLIDESEXTENSIONPOINT._serialized_end=473
# @@protoc_insertion_point(module_scope)
