# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/gaming/v1/game_server_configs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.gaming.v1 import common_pb2 as google_dot_cloud_dot_gaming_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/gaming/v1/game_server_configs.proto\x12\x16google.cloud.gaming.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/gaming/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xf4\x01\n\x1cListGameServerConfigsRequest\x12M\n\x06parent\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\x12,gameservices.googleapis.com/GameServerConfigR\x06parent\x12!\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\x12\x1c\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\x06\x66ilter\x12\x1f\n\x08order_by\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01R\x07orderBy\"\xc3\x01\n\x1dListGameServerConfigsResponse\x12X\n\x13game_server_configs\x18\x01 \x03(\x0b\x32(.google.cloud.gaming.v1.GameServerConfigR\x11gameServerConfigs\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x04 \x03(\tR\x0bunreachable\"g\n\x1aGetGameServerConfigRequest\x12I\n\x04name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,gameservices.googleapis.com/GameServerConfigR\x04name\"\xef\x01\n\x1d\x43reateGameServerConfigRequest\x12M\n\x06parent\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\x12,gameservices.googleapis.com/GameServerConfigR\x06parent\x12!\n\tconfig_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x63onfigId\x12\\\n\x12game_server_config\x18\x03 \x01(\x0b\x32(.google.cloud.gaming.v1.GameServerConfigB\x04\xe2\x41\x01\x02R\x10gameServerConfig\"j\n\x1d\x44\x65leteGameServerConfigRequest\x12I\n\x04name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,gameservices.googleapis.com/GameServerConfigR\x04name\"\xe8\x01\n\rScalingConfig\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\x38\n\x15\x66leet_autoscaler_spec\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x13\x66leetAutoscalerSpec\x12\x43\n\tselectors\x18\x04 \x03(\x0b\x32%.google.cloud.gaming.v1.LabelSelectorR\tselectors\x12>\n\tschedules\x18\x05 \x03(\x0b\x32 .google.cloud.gaming.v1.ScheduleR\tschedules\"@\n\x0b\x46leetConfig\x12\x1d\n\nfleet_spec\x18\x01 \x01(\tR\tfleetSpec\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\x83\x05\n\x10GameServerConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x41\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12L\n\x06labels\x18\x04 \x03(\x0b\x32\x34.google.cloud.gaming.v1.GameServerConfig.LabelsEntryR\x06labels\x12H\n\rfleet_configs\x18\x05 \x03(\x0b\x32#.google.cloud.gaming.v1.FleetConfigR\x0c\x66leetConfigs\x12N\n\x0fscaling_configs\x18\x06 \x03(\x0b\x32%.google.cloud.gaming.v1.ScalingConfigR\x0escalingConfigs\x12 \n\x0b\x64\x65scription\x18\x07 \x01(\tR\x0b\x64\x65scription\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:\x8f\x01\xea\x41\x8b\x01\n,gameservices.googleapis.com/GameServerConfig\x12[projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}B\\\n\x1a\x63om.google.cloud.gaming.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/gaming/v1;gamingb\x06proto3')



_LISTGAMESERVERCONFIGSREQUEST = DESCRIPTOR.message_types_by_name['ListGameServerConfigsRequest']
_LISTGAMESERVERCONFIGSRESPONSE = DESCRIPTOR.message_types_by_name['ListGameServerConfigsResponse']
_GETGAMESERVERCONFIGREQUEST = DESCRIPTOR.message_types_by_name['GetGameServerConfigRequest']
_CREATEGAMESERVERCONFIGREQUEST = DESCRIPTOR.message_types_by_name['CreateGameServerConfigRequest']
_DELETEGAMESERVERCONFIGREQUEST = DESCRIPTOR.message_types_by_name['DeleteGameServerConfigRequest']
_SCALINGCONFIG = DESCRIPTOR.message_types_by_name['ScalingConfig']
_FLEETCONFIG = DESCRIPTOR.message_types_by_name['FleetConfig']
_GAMESERVERCONFIG = DESCRIPTOR.message_types_by_name['GameServerConfig']
_GAMESERVERCONFIG_LABELSENTRY = _GAMESERVERCONFIG.nested_types_by_name['LabelsEntry']
ListGameServerConfigsRequest = _reflection.GeneratedProtocolMessageType('ListGameServerConfigsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTGAMESERVERCONFIGSREQUEST,
  '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.ListGameServerConfigsRequest)
  })
_sym_db.RegisterMessage(ListGameServerConfigsRequest)

ListGameServerConfigsResponse = _reflection.GeneratedProtocolMessageType('ListGameServerConfigsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTGAMESERVERCONFIGSRESPONSE,
  '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.ListGameServerConfigsResponse)
  })
_sym_db.RegisterMessage(ListGameServerConfigsResponse)

GetGameServerConfigRequest = _reflection.GeneratedProtocolMessageType('GetGameServerConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGAMESERVERCONFIGREQUEST,
  '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.GetGameServerConfigRequest)
  })
_sym_db.RegisterMessage(GetGameServerConfigRequest)

CreateGameServerConfigRequest = _reflection.GeneratedProtocolMessageType('CreateGameServerConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGAMESERVERCONFIGREQUEST,
  '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.CreateGameServerConfigRequest)
  })
_sym_db.RegisterMessage(CreateGameServerConfigRequest)

DeleteGameServerConfigRequest = _reflection.GeneratedProtocolMessageType('DeleteGameServerConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGAMESERVERCONFIGREQUEST,
  '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.DeleteGameServerConfigRequest)
  })
_sym_db.RegisterMessage(DeleteGameServerConfigRequest)

ScalingConfig = _reflection.GeneratedProtocolMessageType('ScalingConfig', (_message.Message,), {
  'DESCRIPTOR' : _SCALINGCONFIG,
  '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.ScalingConfig)
  })
_sym_db.RegisterMessage(ScalingConfig)

FleetConfig = _reflection.GeneratedProtocolMessageType('FleetConfig', (_message.Message,), {
  'DESCRIPTOR' : _FLEETCONFIG,
  '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.FleetConfig)
  })
_sym_db.RegisterMessage(FleetConfig)

GameServerConfig = _reflection.GeneratedProtocolMessageType('GameServerConfig', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GAMESERVERCONFIG_LABELSENTRY,
    '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.GameServerConfig.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _GAMESERVERCONFIG,
  '__module__' : 'google.cloud.gaming.v1.game_server_configs_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.GameServerConfig)
  })
_sym_db.RegisterMessage(GameServerConfig)
_sym_db.RegisterMessage(GameServerConfig.LabelsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.google.cloud.gaming.v1P\001Z<google.golang.org/genproto/googleapis/cloud/gaming/v1;gaming'
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['parent']._options = None
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A.\022,gameservices.googleapis.com/GameServerConfig'
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['page_size']._options = None
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['page_token']._options = None
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['filter']._options = None
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['order_by']._options = None
  _LISTGAMESERVERCONFIGSREQUEST.fields_by_name['order_by']._serialized_options = b'\342A\001\001'
  _GETGAMESERVERCONFIGREQUEST.fields_by_name['name']._options = None
  _GETGAMESERVERCONFIGREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A.\n,gameservices.googleapis.com/GameServerConfig'
  _CREATEGAMESERVERCONFIGREQUEST.fields_by_name['parent']._options = None
  _CREATEGAMESERVERCONFIGREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A.\022,gameservices.googleapis.com/GameServerConfig'
  _CREATEGAMESERVERCONFIGREQUEST.fields_by_name['config_id']._options = None
  _CREATEGAMESERVERCONFIGREQUEST.fields_by_name['config_id']._serialized_options = b'\342A\001\002'
  _CREATEGAMESERVERCONFIGREQUEST.fields_by_name['game_server_config']._options = None
  _CREATEGAMESERVERCONFIGREQUEST.fields_by_name['game_server_config']._serialized_options = b'\342A\001\002'
  _DELETEGAMESERVERCONFIGREQUEST.fields_by_name['name']._options = None
  _DELETEGAMESERVERCONFIGREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A.\n,gameservices.googleapis.com/GameServerConfig'
  _SCALINGCONFIG.fields_by_name['name']._options = None
  _SCALINGCONFIG.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _SCALINGCONFIG.fields_by_name['fleet_autoscaler_spec']._options = None
  _SCALINGCONFIG.fields_by_name['fleet_autoscaler_spec']._serialized_options = b'\342A\001\002'
  _GAMESERVERCONFIG_LABELSENTRY._options = None
  _GAMESERVERCONFIG_LABELSENTRY._serialized_options = b'8\001'
  _GAMESERVERCONFIG.fields_by_name['create_time']._options = None
  _GAMESERVERCONFIG.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _GAMESERVERCONFIG.fields_by_name['update_time']._options = None
  _GAMESERVERCONFIG.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _GAMESERVERCONFIG._options = None
  _GAMESERVERCONFIG._serialized_options = b'\352A\213\001\n,gameservices.googleapis.com/GameServerConfig\022[projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}'
  _LISTGAMESERVERCONFIGSREQUEST._serialized_start=237
  _LISTGAMESERVERCONFIGSREQUEST._serialized_end=481
  _LISTGAMESERVERCONFIGSRESPONSE._serialized_start=484
  _LISTGAMESERVERCONFIGSRESPONSE._serialized_end=679
  _GETGAMESERVERCONFIGREQUEST._serialized_start=681
  _GETGAMESERVERCONFIGREQUEST._serialized_end=784
  _CREATEGAMESERVERCONFIGREQUEST._serialized_start=787
  _CREATEGAMESERVERCONFIGREQUEST._serialized_end=1026
  _DELETEGAMESERVERCONFIGREQUEST._serialized_start=1028
  _DELETEGAMESERVERCONFIGREQUEST._serialized_end=1134
  _SCALINGCONFIG._serialized_start=1137
  _SCALINGCONFIG._serialized_end=1369
  _FLEETCONFIG._serialized_start=1371
  _FLEETCONFIG._serialized_end=1435
  _GAMESERVERCONFIG._serialized_start=1438
  _GAMESERVERCONFIG._serialized_end=2081
  _GAMESERVERCONFIG_LABELSENTRY._serialized_start=1878
  _GAMESERVERCONFIG_LABELSENTRY._serialized_end=1935
# @@protoc_insertion_point(module_scope)
