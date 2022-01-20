# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas/v1/upgrade.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from grafeas.v1 import package_pb2 as grafeas_dot_v1_dot_package__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18grafeas/v1/upgrade.proto\x12\ngrafeas.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18grafeas/v1/package.proto\"\xdf\x01\n\x0bUpgradeNote\x12\x18\n\x07package\x18\x01 \x01(\tR\x07package\x12-\n\x07version\x18\x02 \x01(\x0b\x32\x13.grafeas.v1.VersionR\x07version\x12\x45\n\rdistributions\x18\x03 \x03(\x0b\x32\x1f.grafeas.v1.UpgradeDistributionR\rdistributions\x12@\n\x0ewindows_update\x18\x04 \x01(\x0b\x32\x19.grafeas.v1.WindowsUpdateR\rwindowsUpdate\"\x84\x01\n\x13UpgradeDistribution\x12\x17\n\x07\x63pe_uri\x18\x01 \x01(\tR\x06\x63peUri\x12&\n\x0e\x63lassification\x18\x02 \x01(\tR\x0e\x63lassification\x12\x1a\n\x08severity\x18\x03 \x01(\tR\x08severity\x12\x10\n\x03\x63ve\x18\x04 \x03(\tR\x03\x63ve\"\xee\x03\n\rWindowsUpdate\x12>\n\x08identity\x18\x01 \x01(\x0b\x32\".grafeas.v1.WindowsUpdate.IdentityR\x08identity\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x42\n\ncategories\x18\x04 \x03(\x0b\x32\".grafeas.v1.WindowsUpdate.CategoryR\ncategories\x12$\n\x0ekb_article_ids\x18\x05 \x03(\tR\x0ckbArticleIds\x12\x1f\n\x0bsupport_url\x18\x06 \x01(\tR\nsupportUrl\x12T\n\x18last_published_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x16lastPublishedTimestamp\x1a\x43\n\x08Identity\x12\x1b\n\tupdate_id\x18\x01 \x01(\tR\x08updateId\x12\x1a\n\x08revision\x18\x02 \x01(\x05R\x08revision\x1a?\n\x08\x43\x61tegory\x12\x1f\n\x0b\x63\x61tegory_id\x18\x01 \x01(\tR\ncategoryId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\xf0\x01\n\x11UpgradeOccurrence\x12\x18\n\x07package\x18\x01 \x01(\tR\x07package\x12:\n\x0eparsed_version\x18\x03 \x01(\x0b\x32\x13.grafeas.v1.VersionR\rparsedVersion\x12\x43\n\x0c\x64istribution\x18\x04 \x01(\x0b\x32\x1f.grafeas.v1.UpgradeDistributionR\x0c\x64istribution\x12@\n\x0ewindows_update\x18\x05 \x01(\x0b\x32\x19.grafeas.v1.WindowsUpdateR\rwindowsUpdateBQ\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3')



_UPGRADENOTE = DESCRIPTOR.message_types_by_name['UpgradeNote']
_UPGRADEDISTRIBUTION = DESCRIPTOR.message_types_by_name['UpgradeDistribution']
_WINDOWSUPDATE = DESCRIPTOR.message_types_by_name['WindowsUpdate']
_WINDOWSUPDATE_IDENTITY = _WINDOWSUPDATE.nested_types_by_name['Identity']
_WINDOWSUPDATE_CATEGORY = _WINDOWSUPDATE.nested_types_by_name['Category']
_UPGRADEOCCURRENCE = DESCRIPTOR.message_types_by_name['UpgradeOccurrence']
UpgradeNote = _reflection.GeneratedProtocolMessageType('UpgradeNote', (_message.Message,), {
  'DESCRIPTOR' : _UPGRADENOTE,
  '__module__' : 'grafeas.v1.upgrade_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.UpgradeNote)
  })
_sym_db.RegisterMessage(UpgradeNote)

UpgradeDistribution = _reflection.GeneratedProtocolMessageType('UpgradeDistribution', (_message.Message,), {
  'DESCRIPTOR' : _UPGRADEDISTRIBUTION,
  '__module__' : 'grafeas.v1.upgrade_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.UpgradeDistribution)
  })
_sym_db.RegisterMessage(UpgradeDistribution)

WindowsUpdate = _reflection.GeneratedProtocolMessageType('WindowsUpdate', (_message.Message,), {

  'Identity' : _reflection.GeneratedProtocolMessageType('Identity', (_message.Message,), {
    'DESCRIPTOR' : _WINDOWSUPDATE_IDENTITY,
    '__module__' : 'grafeas.v1.upgrade_pb2'
    # @@protoc_insertion_point(class_scope:grafeas.v1.WindowsUpdate.Identity)
    })
  ,

  'Category' : _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
    'DESCRIPTOR' : _WINDOWSUPDATE_CATEGORY,
    '__module__' : 'grafeas.v1.upgrade_pb2'
    # @@protoc_insertion_point(class_scope:grafeas.v1.WindowsUpdate.Category)
    })
  ,
  'DESCRIPTOR' : _WINDOWSUPDATE,
  '__module__' : 'grafeas.v1.upgrade_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.WindowsUpdate)
  })
_sym_db.RegisterMessage(WindowsUpdate)
_sym_db.RegisterMessage(WindowsUpdate.Identity)
_sym_db.RegisterMessage(WindowsUpdate.Category)

UpgradeOccurrence = _reflection.GeneratedProtocolMessageType('UpgradeOccurrence', (_message.Message,), {
  'DESCRIPTOR' : _UPGRADEOCCURRENCE,
  '__module__' : 'grafeas.v1.upgrade_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.UpgradeOccurrence)
  })
_sym_db.RegisterMessage(UpgradeOccurrence)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA'
  _UPGRADENOTE._serialized_start=100
  _UPGRADENOTE._serialized_end=323
  _UPGRADEDISTRIBUTION._serialized_start=326
  _UPGRADEDISTRIBUTION._serialized_end=458
  _WINDOWSUPDATE._serialized_start=461
  _WINDOWSUPDATE._serialized_end=955
  _WINDOWSUPDATE_IDENTITY._serialized_start=823
  _WINDOWSUPDATE_IDENTITY._serialized_end=890
  _WINDOWSUPDATE_CATEGORY._serialized_start=892
  _WINDOWSUPDATE_CATEGORY._serialized_end=955
  _UPGRADEOCCURRENCE._serialized_start=958
  _UPGRADEOCCURRENCE._serialized_end=1198
# @@protoc_insertion_point(module_scope)
