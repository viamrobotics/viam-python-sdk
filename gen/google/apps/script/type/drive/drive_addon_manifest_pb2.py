# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/apps/script/type/drive/drive_addon_manifest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/apps/script/type/drive/drive_addon_manifest.proto\x12\x1dgoogle.apps.script.type.drive\x1a-google/apps/script/type/extension_point.proto\"\xdf\x01\n\x12\x44riveAddOnManifest\x12Z\n\x10homepage_trigger\x18\x01 \x01(\x0b\x32/.google.apps.script.type.HomepageExtensionPointR\x0fhomepageTrigger\x12m\n\x19on_items_selected_trigger\x18\x02 \x01(\x0b\x32\x32.google.apps.script.type.drive.DriveExtensionPointR\x16onItemsSelectedTrigger\"8\n\x13\x44riveExtensionPoint\x12!\n\x0crun_function\x18\x01 \x01(\tR\x0brunFunctionB\xe0\x01\n!com.google.apps.script.type.driveB\x17\x44riveAddOnManifestProtoP\x01Z<google.golang.org/genproto/googleapis/apps/script/type/drive\xaa\x02\x1dGoogle.Apps.Script.Type.Drive\xca\x02\x1dGoogle\\Apps\\Script\\Type\\Drive\xea\x02!Google::Apps::Script::Type::Driveb\x06proto3')



_DRIVEADDONMANIFEST = DESCRIPTOR.message_types_by_name['DriveAddOnManifest']
_DRIVEEXTENSIONPOINT = DESCRIPTOR.message_types_by_name['DriveExtensionPoint']
DriveAddOnManifest = _reflection.GeneratedProtocolMessageType('DriveAddOnManifest', (_message.Message,), {
  'DESCRIPTOR' : _DRIVEADDONMANIFEST,
  '__module__' : 'google.apps.script.type.drive.drive_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.drive.DriveAddOnManifest)
  })
_sym_db.RegisterMessage(DriveAddOnManifest)

DriveExtensionPoint = _reflection.GeneratedProtocolMessageType('DriveExtensionPoint', (_message.Message,), {
  'DESCRIPTOR' : _DRIVEEXTENSIONPOINT,
  '__module__' : 'google.apps.script.type.drive.drive_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.drive.DriveExtensionPoint)
  })
_sym_db.RegisterMessage(DriveExtensionPoint)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.apps.script.type.driveB\027DriveAddOnManifestProtoP\001Z<google.golang.org/genproto/googleapis/apps/script/type/drive\252\002\035Google.Apps.Script.Type.Drive\312\002\035Google\\Apps\\Script\\Type\\Drive\352\002!Google::Apps::Script::Type::Drive'
  _DRIVEADDONMANIFEST._serialized_start=139
  _DRIVEADDONMANIFEST._serialized_end=362
  _DRIVEEXTENSIONPOINT._serialized_start=364
  _DRIVEEXTENSIONPOINT._serialized_end=420
# @@protoc_insertion_point(module_scope)
