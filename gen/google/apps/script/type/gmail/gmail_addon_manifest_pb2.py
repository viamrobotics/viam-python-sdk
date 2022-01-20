# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/apps/script/type/gmail/gmail_addon_manifest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.apps.script.type import addon_widget_set_pb2 as google_dot_apps_dot_script_dot_type_dot_addon__widget__set__pb2
from google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/apps/script/type/gmail/gmail_addon_manifest.proto\x12\x1dgoogle.apps.script.type.gmail\x1a.google/apps/script/type/addon_widget_set.proto\x1a-google/apps/script/type/extension_point.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xca\x03\n\x12GmailAddOnManifest\x12Z\n\x10homepage_trigger\x18\x0e \x01(\x0b\x32/.google.apps.script.type.HomepageExtensionPointR\x0fhomepageTrigger\x12\x61\n\x13\x63ontextual_triggers\x18\x03 \x03(\x0b\x32\x30.google.apps.script.type.gmail.ContextualTriggerR\x12\x63ontextualTriggers\x12[\n\x11universal_actions\x18\x04 \x03(\x0b\x32..google.apps.script.type.gmail.UniversalActionR\x10universalActions\x12V\n\x0f\x63ompose_trigger\x18\x0c \x01(\x0b\x32-.google.apps.script.type.gmail.ComposeTriggerR\x0e\x63omposeTrigger\x12@\n\x1c\x61uthorization_check_function\x18\x07 \x01(\tR\x1a\x61uthorizationCheckFunction\"x\n\x0fUniversalAction\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1d\n\topen_link\x18\x02 \x01(\tH\x00R\x08openLink\x12#\n\x0crun_function\x18\x03 \x01(\tH\x00R\x0brunFunctionB\r\n\x0b\x61\x63tion_type\"\xf1\x01\n\x0e\x43omposeTrigger\x12I\n\x07\x61\x63tions\x18\x05 \x03(\x0b\x32/.google.apps.script.type.MenuItemExtensionPointR\x07\x61\x63tions\x12\\\n\x0c\x64raft_access\x18\x04 \x01(\x0e\x32\x39.google.apps.script.type.gmail.ComposeTrigger.DraftAccessR\x0b\x64raftAccess\"6\n\x0b\x44raftAccess\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x0c\n\x08METADATA\x10\x02\"\xab\x01\n\x11\x43ontextualTrigger\x12[\n\runconditional\x18\x01 \x01(\x0b\x32\x33.google.apps.script.type.gmail.UnconditionalTriggerH\x00R\runconditional\x12.\n\x13on_trigger_function\x18\x04 \x01(\tR\x11onTriggerFunctionB\t\n\x07trigger\"\x16\n\x14UnconditionalTriggerB\xe0\x01\n!com.google.apps.script.type.gmailB\x17GmailAddOnManifestProtoP\x01Z<google.golang.org/genproto/googleapis/apps/script/type/gmail\xaa\x02\x1dGoogle.Apps.Script.Type.Gmail\xca\x02\x1dGoogle\\Apps\\Script\\Type\\Gmail\xea\x02!Google::Apps::Script::Type::Gmailb\x06proto3')



_GMAILADDONMANIFEST = DESCRIPTOR.message_types_by_name['GmailAddOnManifest']
_UNIVERSALACTION = DESCRIPTOR.message_types_by_name['UniversalAction']
_COMPOSETRIGGER = DESCRIPTOR.message_types_by_name['ComposeTrigger']
_CONTEXTUALTRIGGER = DESCRIPTOR.message_types_by_name['ContextualTrigger']
_UNCONDITIONALTRIGGER = DESCRIPTOR.message_types_by_name['UnconditionalTrigger']
_COMPOSETRIGGER_DRAFTACCESS = _COMPOSETRIGGER.enum_types_by_name['DraftAccess']
GmailAddOnManifest = _reflection.GeneratedProtocolMessageType('GmailAddOnManifest', (_message.Message,), {
  'DESCRIPTOR' : _GMAILADDONMANIFEST,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.GmailAddOnManifest)
  })
_sym_db.RegisterMessage(GmailAddOnManifest)

UniversalAction = _reflection.GeneratedProtocolMessageType('UniversalAction', (_message.Message,), {
  'DESCRIPTOR' : _UNIVERSALACTION,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.UniversalAction)
  })
_sym_db.RegisterMessage(UniversalAction)

ComposeTrigger = _reflection.GeneratedProtocolMessageType('ComposeTrigger', (_message.Message,), {
  'DESCRIPTOR' : _COMPOSETRIGGER,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.ComposeTrigger)
  })
_sym_db.RegisterMessage(ComposeTrigger)

ContextualTrigger = _reflection.GeneratedProtocolMessageType('ContextualTrigger', (_message.Message,), {
  'DESCRIPTOR' : _CONTEXTUALTRIGGER,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.ContextualTrigger)
  })
_sym_db.RegisterMessage(ContextualTrigger)

UnconditionalTrigger = _reflection.GeneratedProtocolMessageType('UnconditionalTrigger', (_message.Message,), {
  'DESCRIPTOR' : _UNCONDITIONALTRIGGER,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.UnconditionalTrigger)
  })
_sym_db.RegisterMessage(UnconditionalTrigger)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.apps.script.type.gmailB\027GmailAddOnManifestProtoP\001Z<google.golang.org/genproto/googleapis/apps/script/type/gmail\252\002\035Google.Apps.Script.Type.Gmail\312\002\035Google\\Apps\\Script\\Type\\Gmail\352\002!Google::Apps::Script::Type::Gmail'
  _GMAILADDONMANIFEST._serialized_start=217
  _GMAILADDONMANIFEST._serialized_end=675
  _UNIVERSALACTION._serialized_start=677
  _UNIVERSALACTION._serialized_end=797
  _COMPOSETRIGGER._serialized_start=800
  _COMPOSETRIGGER._serialized_end=1041
  _COMPOSETRIGGER_DRAFTACCESS._serialized_start=987
  _COMPOSETRIGGER_DRAFTACCESS._serialized_end=1041
  _CONTEXTUALTRIGGER._serialized_start=1044
  _CONTEXTUALTRIGGER._serialized_end=1215
  _UNCONDITIONALTRIGGER._serialized_start=1217
  _UNCONDITIONALTRIGGER._serialized_end=1239
# @@protoc_insertion_point(module_scope)
