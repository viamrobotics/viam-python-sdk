# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/apps/drive/activity/v2/target.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.apps.drive.activity.v2 import actor_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_actor__pb2
from google.apps.drive.activity.v2 import common_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/apps/drive/activity/v2/target.proto\x12\x1dgoogle.apps.drive.activity.v2\x1a)google/apps/drive/activity/v2/actor.proto\x1a*google/apps/drive/activity/v2/common.proto\"\xb9\x02\n\x06Target\x12I\n\ndrive_item\x18\x01 \x01(\x0b\x32(.google.apps.drive.activity.v2.DriveItemH\x00R\tdriveItem\x12<\n\x05\x64rive\x18\x05 \x01(\x0b\x32$.google.apps.drive.activity.v2.DriveH\x00R\x05\x64rive\x12O\n\x0c\x66ile_comment\x18\x03 \x01(\x0b\x32*.google.apps.drive.activity.v2.FileCommentH\x00R\x0b\x66ileComment\x12K\n\nteam_drive\x18\x02 \x01(\x0b\x32(.google.apps.drive.activity.v2.TeamDriveB\x02\x18\x01R\tteamDriveB\x08\n\x06object\"\x8c\x02\n\x0fTargetReference\x12R\n\ndrive_item\x18\x01 \x01(\x0b\x32\x31.google.apps.drive.activity.v2.DriveItemReferenceH\x00R\tdriveItem\x12\x45\n\x05\x64rive\x18\x03 \x01(\x0b\x32-.google.apps.drive.activity.v2.DriveReferenceH\x00R\x05\x64rive\x12T\n\nteam_drive\x18\x02 \x01(\x0b\x32\x31.google.apps.drive.activity.v2.TeamDriveReferenceB\x02\x18\x01R\tteamDriveB\x08\n\x06object\"\xdb\x01\n\x0b\x46ileComment\x12*\n\x11legacy_comment_id\x18\x01 \x01(\tR\x0flegacyCommentId\x12\x30\n\x14legacy_discussion_id\x18\x02 \x01(\tR\x12legacyDiscussionId\x12,\n\x12link_to_discussion\x18\x03 \x01(\tR\x10linkToDiscussion\x12@\n\x06parent\x18\x04 \x01(\x0b\x32(.google.apps.drive.activity.v2.DriveItemR\x06parent\"\xec\x06\n\tDriveItem\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12\x45\n\x04\x66ile\x18\x03 \x01(\x0b\x32-.google.apps.drive.activity.v2.DriveItem.FileB\x02\x18\x01R\x04\x66ile\x12K\n\x06\x66older\x18\x04 \x01(\x0b\x32/.google.apps.drive.activity.v2.DriveItem.FolderB\x02\x18\x01R\x06\x66older\x12S\n\ndrive_file\x18\x08 \x01(\x0b\x32\x32.google.apps.drive.activity.v2.DriveItem.DriveFileH\x00R\tdriveFile\x12Y\n\x0c\x64rive_folder\x18\t \x01(\x0b\x32\x34.google.apps.drive.activity.v2.DriveItem.DriveFolderH\x00R\x0b\x64riveFolder\x12\x1b\n\tmime_type\x18\x06 \x01(\tR\x08mimeType\x12:\n\x05owner\x18\x07 \x01(\x0b\x32$.google.apps.drive.activity.v2.OwnerR\x05owner\x1a\n\n\x04\x46ile:\x02\x18\x01\x1a\xb5\x01\n\x06\x46older\x12H\n\x04type\x18\x06 \x01(\x0e\x32\x34.google.apps.drive.activity.v2.DriveItem.Folder.TypeR\x04type\"]\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMY_DRIVE_ROOT\x10\x01\x12\x13\n\x0fTEAM_DRIVE_ROOT\x10\x02\x12\x13\n\x0fSTANDARD_FOLDER\x10\x03\x1a\x02\x18\x01:\x02\x18\x01\x1a\x0b\n\tDriveFile\x1a\xb9\x01\n\x0b\x44riveFolder\x12M\n\x04type\x18\x06 \x01(\x0e\x32\x39.google.apps.drive.activity.v2.DriveItem.DriveFolder.TypeR\x04type\"[\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMY_DRIVE_ROOT\x10\x01\x12\x15\n\x11SHARED_DRIVE_ROOT\x10\x02\x12\x13\n\x0fSTANDARD_FOLDER\x10\x03\x42\x0b\n\titem_type\"\xa7\x02\n\x05Owner\x12\x39\n\x04user\x18\x01 \x01(\x0b\x32#.google.apps.drive.activity.v2.UserH\x00R\x04user\x12\x45\n\x05\x64rive\x18\x04 \x01(\x0b\x32-.google.apps.drive.activity.v2.DriveReferenceH\x00R\x05\x64rive\x12T\n\nteam_drive\x18\x02 \x01(\x0b\x32\x31.google.apps.drive.activity.v2.TeamDriveReferenceB\x02\x18\x01R\tteamDrive\x12=\n\x06\x64omain\x18\x03 \x01(\x0b\x32%.google.apps.drive.activity.v2.DomainR\x06\x64omainB\x07\n\x05owner\"w\n\tTeamDrive\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12<\n\x04root\x18\x03 \x01(\x0b\x32(.google.apps.drive.activity.v2.DriveItemR\x04root:\x02\x18\x01\"o\n\x05\x44rive\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12<\n\x04root\x18\x03 \x01(\x0b\x32(.google.apps.drive.activity.v2.DriveItemR\x04root\"\x8f\x03\n\x12\x44riveItemReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12\x45\n\x04\x66ile\x18\x03 \x01(\x0b\x32-.google.apps.drive.activity.v2.DriveItem.FileB\x02\x18\x01R\x04\x66ile\x12K\n\x06\x66older\x18\x04 \x01(\x0b\x32/.google.apps.drive.activity.v2.DriveItem.FolderB\x02\x18\x01R\x06\x66older\x12S\n\ndrive_file\x18\x08 \x01(\x0b\x32\x32.google.apps.drive.activity.v2.DriveItem.DriveFileH\x00R\tdriveFile\x12Y\n\x0c\x64rive_folder\x18\t \x01(\x0b\x32\x34.google.apps.drive.activity.v2.DriveItem.DriveFolderH\x00R\x0b\x64riveFolderB\x0b\n\titem_type\"B\n\x12TeamDriveReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title:\x02\x18\x01\":\n\x0e\x44riveReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\x02 \x01(\tR\x05titleB\xc0\x01\n!com.google.apps.drive.activity.v2B\x0bTargetProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2b\x06proto3')



_TARGET = DESCRIPTOR.message_types_by_name['Target']
_TARGETREFERENCE = DESCRIPTOR.message_types_by_name['TargetReference']
_FILECOMMENT = DESCRIPTOR.message_types_by_name['FileComment']
_DRIVEITEM = DESCRIPTOR.message_types_by_name['DriveItem']
_DRIVEITEM_FILE = _DRIVEITEM.nested_types_by_name['File']
_DRIVEITEM_FOLDER = _DRIVEITEM.nested_types_by_name['Folder']
_DRIVEITEM_DRIVEFILE = _DRIVEITEM.nested_types_by_name['DriveFile']
_DRIVEITEM_DRIVEFOLDER = _DRIVEITEM.nested_types_by_name['DriveFolder']
_OWNER = DESCRIPTOR.message_types_by_name['Owner']
_TEAMDRIVE = DESCRIPTOR.message_types_by_name['TeamDrive']
_DRIVE = DESCRIPTOR.message_types_by_name['Drive']
_DRIVEITEMREFERENCE = DESCRIPTOR.message_types_by_name['DriveItemReference']
_TEAMDRIVEREFERENCE = DESCRIPTOR.message_types_by_name['TeamDriveReference']
_DRIVEREFERENCE = DESCRIPTOR.message_types_by_name['DriveReference']
_DRIVEITEM_FOLDER_TYPE = _DRIVEITEM_FOLDER.enum_types_by_name['Type']
_DRIVEITEM_DRIVEFOLDER_TYPE = _DRIVEITEM_DRIVEFOLDER.enum_types_by_name['Type']
Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.Target)
  })
_sym_db.RegisterMessage(Target)

TargetReference = _reflection.GeneratedProtocolMessageType('TargetReference', (_message.Message,), {
  'DESCRIPTOR' : _TARGETREFERENCE,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.TargetReference)
  })
_sym_db.RegisterMessage(TargetReference)

FileComment = _reflection.GeneratedProtocolMessageType('FileComment', (_message.Message,), {
  'DESCRIPTOR' : _FILECOMMENT,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.FileComment)
  })
_sym_db.RegisterMessage(FileComment)

DriveItem = _reflection.GeneratedProtocolMessageType('DriveItem', (_message.Message,), {

  'File' : _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
    'DESCRIPTOR' : _DRIVEITEM_FILE,
    '__module__' : 'google.apps.drive.activity.v2.target_pb2'
    # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.DriveItem.File)
    })
  ,

  'Folder' : _reflection.GeneratedProtocolMessageType('Folder', (_message.Message,), {
    'DESCRIPTOR' : _DRIVEITEM_FOLDER,
    '__module__' : 'google.apps.drive.activity.v2.target_pb2'
    # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.DriveItem.Folder)
    })
  ,

  'DriveFile' : _reflection.GeneratedProtocolMessageType('DriveFile', (_message.Message,), {
    'DESCRIPTOR' : _DRIVEITEM_DRIVEFILE,
    '__module__' : 'google.apps.drive.activity.v2.target_pb2'
    # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.DriveItem.DriveFile)
    })
  ,

  'DriveFolder' : _reflection.GeneratedProtocolMessageType('DriveFolder', (_message.Message,), {
    'DESCRIPTOR' : _DRIVEITEM_DRIVEFOLDER,
    '__module__' : 'google.apps.drive.activity.v2.target_pb2'
    # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.DriveItem.DriveFolder)
    })
  ,
  'DESCRIPTOR' : _DRIVEITEM,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.DriveItem)
  })
_sym_db.RegisterMessage(DriveItem)
_sym_db.RegisterMessage(DriveItem.File)
_sym_db.RegisterMessage(DriveItem.Folder)
_sym_db.RegisterMessage(DriveItem.DriveFile)
_sym_db.RegisterMessage(DriveItem.DriveFolder)

Owner = _reflection.GeneratedProtocolMessageType('Owner', (_message.Message,), {
  'DESCRIPTOR' : _OWNER,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.Owner)
  })
_sym_db.RegisterMessage(Owner)

TeamDrive = _reflection.GeneratedProtocolMessageType('TeamDrive', (_message.Message,), {
  'DESCRIPTOR' : _TEAMDRIVE,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.TeamDrive)
  })
_sym_db.RegisterMessage(TeamDrive)

Drive = _reflection.GeneratedProtocolMessageType('Drive', (_message.Message,), {
  'DESCRIPTOR' : _DRIVE,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.Drive)
  })
_sym_db.RegisterMessage(Drive)

DriveItemReference = _reflection.GeneratedProtocolMessageType('DriveItemReference', (_message.Message,), {
  'DESCRIPTOR' : _DRIVEITEMREFERENCE,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.DriveItemReference)
  })
_sym_db.RegisterMessage(DriveItemReference)

TeamDriveReference = _reflection.GeneratedProtocolMessageType('TeamDriveReference', (_message.Message,), {
  'DESCRIPTOR' : _TEAMDRIVEREFERENCE,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.TeamDriveReference)
  })
_sym_db.RegisterMessage(TeamDriveReference)

DriveReference = _reflection.GeneratedProtocolMessageType('DriveReference', (_message.Message,), {
  'DESCRIPTOR' : _DRIVEREFERENCE,
  '__module__' : 'google.apps.drive.activity.v2.target_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.drive.activity.v2.DriveReference)
  })
_sym_db.RegisterMessage(DriveReference)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.apps.drive.activity.v2B\013TargetProtoP\001ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\242\002\004GADA\252\002\035Google.Apps.Drive.Activity.V2\312\002\035Google\\Apps\\Drive\\Activity\\V2'
  _TARGET.fields_by_name['team_drive']._options = None
  _TARGET.fields_by_name['team_drive']._serialized_options = b'\030\001'
  _TARGETREFERENCE.fields_by_name['team_drive']._options = None
  _TARGETREFERENCE.fields_by_name['team_drive']._serialized_options = b'\030\001'
  _DRIVEITEM_FILE._options = None
  _DRIVEITEM_FILE._serialized_options = b'\030\001'
  _DRIVEITEM_FOLDER_TYPE._options = None
  _DRIVEITEM_FOLDER_TYPE._serialized_options = b'\030\001'
  _DRIVEITEM_FOLDER._options = None
  _DRIVEITEM_FOLDER._serialized_options = b'\030\001'
  _DRIVEITEM.fields_by_name['file']._options = None
  _DRIVEITEM.fields_by_name['file']._serialized_options = b'\030\001'
  _DRIVEITEM.fields_by_name['folder']._options = None
  _DRIVEITEM.fields_by_name['folder']._serialized_options = b'\030\001'
  _OWNER.fields_by_name['team_drive']._options = None
  _OWNER.fields_by_name['team_drive']._serialized_options = b'\030\001'
  _TEAMDRIVE._options = None
  _TEAMDRIVE._serialized_options = b'\030\001'
  _DRIVEITEMREFERENCE.fields_by_name['file']._options = None
  _DRIVEITEMREFERENCE.fields_by_name['file']._serialized_options = b'\030\001'
  _DRIVEITEMREFERENCE.fields_by_name['folder']._options = None
  _DRIVEITEMREFERENCE.fields_by_name['folder']._serialized_options = b'\030\001'
  _TEAMDRIVEREFERENCE._options = None
  _TEAMDRIVEREFERENCE._serialized_options = b'\030\001'
  _TARGET._serialized_start=165
  _TARGET._serialized_end=478
  _TARGETREFERENCE._serialized_start=481
  _TARGETREFERENCE._serialized_end=749
  _FILECOMMENT._serialized_start=752
  _FILECOMMENT._serialized_end=971
  _DRIVEITEM._serialized_start=974
  _DRIVEITEM._serialized_end=1850
  _DRIVEITEM_FILE._serialized_start=1442
  _DRIVEITEM_FILE._serialized_end=1452
  _DRIVEITEM_FOLDER._serialized_start=1455
  _DRIVEITEM_FOLDER._serialized_end=1636
  _DRIVEITEM_FOLDER_TYPE._serialized_start=1539
  _DRIVEITEM_FOLDER_TYPE._serialized_end=1632
  _DRIVEITEM_DRIVEFILE._serialized_start=1638
  _DRIVEITEM_DRIVEFILE._serialized_end=1649
  _DRIVEITEM_DRIVEFOLDER._serialized_start=1652
  _DRIVEITEM_DRIVEFOLDER._serialized_end=1837
  _DRIVEITEM_DRIVEFOLDER_TYPE._serialized_start=1746
  _DRIVEITEM_DRIVEFOLDER_TYPE._serialized_end=1837
  _OWNER._serialized_start=1853
  _OWNER._serialized_end=2148
  _TEAMDRIVE._serialized_start=2150
  _TEAMDRIVE._serialized_end=2269
  _DRIVE._serialized_start=2271
  _DRIVE._serialized_end=2382
  _DRIVEITEMREFERENCE._serialized_start=2385
  _DRIVEITEMREFERENCE._serialized_end=2784
  _TEAMDRIVEREFERENCE._serialized_start=2786
  _TEAMDRIVEREFERENCE._serialized_end=2852
  _DRIVEREFERENCE._serialized_start=2854
  _DRIVEREFERENCE._serialized_end=2912
# @@protoc_insertion_point(module_scope)
