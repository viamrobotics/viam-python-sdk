# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/resourcemanager/v3/folders.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/resourcemanager/v3/folders.proto\x12\x1fgoogle.cloud.resourcemanager.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x99\x04\n\x06\x46older\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x1c\n\x06parent\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12!\n\x0c\x64isplay_name\x18\x03 \x01(\tR\x0b\x64isplayName\x12I\n\x05state\x18\x04 \x01(\x0e\x32-.google.cloud.resourcemanager.v3.Folder.StateB\x04\xe2\x41\x01\x03R\x05state\x12\x41\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12\x41\n\x0b\x64\x65lete_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ndeleteTime\x12\x18\n\x04\x65tag\x18\x08 \x01(\tB\x04\xe2\x41\x01\x03R\x04\x65tag\"@\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x14\n\x10\x44\x45LETE_REQUESTED\x10\x02:D\xea\x41\x41\n*cloudresourcemanager.googleapis.com/Folder\x12\x10\x66olders/{folder}R\x01\x01\"[\n\x10GetFolderRequest\x12G\n\x04name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*cloudresourcemanager.googleapis.com/FolderR\x04name\"\xa9\x01\n\x12ListFoldersRequest\x12\"\n\x06parent\x18\x01 \x01(\tB\n\xe2\x41\x01\x02\xfa\x41\x03\x12\x01*R\x06parent\x12!\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\x12\'\n\x0cshow_deleted\x18\x04 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x0bshowDeleted\"\x80\x01\n\x13ListFoldersResponse\x12\x41\n\x07\x66olders\x18\x01 \x03(\x0b\x32\'.google.cloud.resourcemanager.v3.FolderR\x07\x66olders\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"z\n\x14SearchFoldersRequest\x12!\n\tpage_size\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\x12\x1a\n\x05query\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\x05query\"\x82\x01\n\x15SearchFoldersResponse\x12\x41\n\x07\x66olders\x18\x01 \x03(\x0b\x32\'.google.cloud.resourcemanager.v3.FolderR\x07\x66olders\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\\\n\x13\x43reateFolderRequest\x12\x45\n\x06\x66older\x18\x02 \x01(\x0b\x32\'.google.cloud.resourcemanager.v3.FolderB\x04\xe2\x41\x01\x02R\x06\x66older\"Q\n\x14\x43reateFolderMetadata\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x16\n\x06parent\x18\x02 \x01(\tR\x06parent\"\x9f\x01\n\x13UpdateFolderRequest\x12\x45\n\x06\x66older\x18\x01 \x01(\x0b\x32\'.google.cloud.resourcemanager.v3.FolderB\x04\xe2\x41\x01\x02R\x06\x66older\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"\x16\n\x14UpdateFolderMetadata\"\x97\x01\n\x11MoveFolderRequest\x12G\n\x04name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*cloudresourcemanager.googleapis.com/FolderR\x04name\x12\x39\n\x12\x64\x65stination_parent\x18\x02 \x01(\tB\n\xe2\x41\x01\x02\xfa\x41\x03\x12\x01*R\x11\x64\x65stinationParent\"\x8b\x01\n\x12MoveFolderMetadata\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12#\n\rsource_parent\x18\x02 \x01(\tR\x0csourceParent\x12-\n\x12\x64\x65stination_parent\x18\x03 \x01(\tR\x11\x64\x65stinationParent\"^\n\x13\x44\x65leteFolderRequest\x12G\n\x04name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*cloudresourcemanager.googleapis.com/FolderR\x04name\"\x16\n\x14\x44\x65leteFolderMetadata\"`\n\x15UndeleteFolderRequest\x12G\n\x04name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*cloudresourcemanager.googleapis.com/FolderR\x04name\"\x18\n\x16UndeleteFolderMetadata2\xde\x0f\n\x07\x46olders\x12\x8c\x01\n\tGetFolder\x12\x31.google.cloud.resourcemanager.v3.GetFolderRequest\x1a\'.google.cloud.resourcemanager.v3.Folder\"#\xda\x41\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v3/{name=folders/*}\x12\x96\x01\n\x0bListFolders\x12\x33.google.cloud.resourcemanager.v3.ListFoldersRequest\x1a\x34.google.cloud.resourcemanager.v3.ListFoldersResponse\"\x1c\xda\x41\x06parent\x82\xd3\xe4\x93\x02\r\x12\x0b/v3/folders\x12\xa2\x01\n\rSearchFolders\x12\x35.google.cloud.resourcemanager.v3.SearchFoldersRequest\x1a\x36.google.cloud.resourcemanager.v3.SearchFoldersResponse\"\"\xda\x41\x05query\x82\xd3\xe4\x93\x02\x14\x12\x12/v3/folders:search\x12\xaa\x01\n\x0c\x43reateFolder\x12\x34.google.cloud.resourcemanager.v3.CreateFolderRequest\x1a\x1d.google.longrunning.Operation\"E\xca\x41\x1e\n\x06\x46older\x12\x14\x43reateFolderMetadata\xda\x41\x06\x66older\x82\xd3\xe4\x93\x02\x15\"\x0b/v3/folders:\x06\x66older\x12\xc6\x01\n\x0cUpdateFolder\x12\x34.google.cloud.resourcemanager.v3.UpdateFolderRequest\x1a\x1d.google.longrunning.Operation\"a\xca\x41\x1e\n\x06\x46older\x12\x14UpdateFolderMetadata\xda\x41\x12\x66older,update_mask\x82\xd3\xe4\x93\x02%2\x1b/v3/{folder.name=folders/*}:\x06\x66older\x12\xbe\x01\n\nMoveFolder\x12\x32.google.cloud.resourcemanager.v3.MoveFolderRequest\x1a\x1d.google.longrunning.Operation\"]\xca\x41\x1c\n\x06\x46older\x12\x12MoveFolderMetadata\xda\x41\x17name,destination_parent\x82\xd3\xe4\x93\x02\x1e\"\x19/v3/{name=folders/*}:move:\x01*\x12\xa9\x01\n\x0c\x44\x65leteFolder\x12\x34.google.cloud.resourcemanager.v3.DeleteFolderRequest\x1a\x1d.google.longrunning.Operation\"D\xca\x41\x1e\n\x06\x46older\x12\x14\x44\x65leteFolderMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02\x16*\x14/v3/{name=folders/*}\x12\xbb\x01\n\x0eUndeleteFolder\x12\x36.google.cloud.resourcemanager.v3.UndeleteFolderRequest\x1a\x1d.google.longrunning.Operation\"R\xca\x41 \n\x06\x46older\x12\x16UndeleteFolderMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02\"\"\x1d/v3/{name=folders/*}:undelete:\x01*\x12\x86\x01\n\x0cGetIamPolicy\x12\".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy\";\xda\x41\x08resource\x82\xd3\xe4\x93\x02*\"%/v3/{resource=folders/*}:getIamPolicy:\x01*\x12\x8d\x01\n\x0cSetIamPolicy\x12\".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy\"B\xda\x41\x0fresource,policy\x82\xd3\xe4\x93\x02*\"%/v3/{resource=folders/*}:setIamPolicy:\x01*\x12\xb8\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse\"M\xda\x41\x14resource,permissions\x82\xd3\xe4\x93\x02\x30\"+/v3/{resource=folders/*}:testIamPermissions:\x01*\x1a\x90\x01\xca\x41#cloudresourcemanager.googleapis.com\xd2\x41ghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xee\x01\n#com.google.cloud.resourcemanager.v3B\x0c\x46oldersProtoP\x01ZNgoogle.golang.org/genproto/googleapis/cloud/resourcemanager/v3;resourcemanager\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02\"Google::Cloud::ResourceManager::V3b\x06proto3')



_FOLDER = DESCRIPTOR.message_types_by_name['Folder']
_GETFOLDERREQUEST = DESCRIPTOR.message_types_by_name['GetFolderRequest']
_LISTFOLDERSREQUEST = DESCRIPTOR.message_types_by_name['ListFoldersRequest']
_LISTFOLDERSRESPONSE = DESCRIPTOR.message_types_by_name['ListFoldersResponse']
_SEARCHFOLDERSREQUEST = DESCRIPTOR.message_types_by_name['SearchFoldersRequest']
_SEARCHFOLDERSRESPONSE = DESCRIPTOR.message_types_by_name['SearchFoldersResponse']
_CREATEFOLDERREQUEST = DESCRIPTOR.message_types_by_name['CreateFolderRequest']
_CREATEFOLDERMETADATA = DESCRIPTOR.message_types_by_name['CreateFolderMetadata']
_UPDATEFOLDERREQUEST = DESCRIPTOR.message_types_by_name['UpdateFolderRequest']
_UPDATEFOLDERMETADATA = DESCRIPTOR.message_types_by_name['UpdateFolderMetadata']
_MOVEFOLDERREQUEST = DESCRIPTOR.message_types_by_name['MoveFolderRequest']
_MOVEFOLDERMETADATA = DESCRIPTOR.message_types_by_name['MoveFolderMetadata']
_DELETEFOLDERREQUEST = DESCRIPTOR.message_types_by_name['DeleteFolderRequest']
_DELETEFOLDERMETADATA = DESCRIPTOR.message_types_by_name['DeleteFolderMetadata']
_UNDELETEFOLDERREQUEST = DESCRIPTOR.message_types_by_name['UndeleteFolderRequest']
_UNDELETEFOLDERMETADATA = DESCRIPTOR.message_types_by_name['UndeleteFolderMetadata']
_FOLDER_STATE = _FOLDER.enum_types_by_name['State']
Folder = _reflection.GeneratedProtocolMessageType('Folder', (_message.Message,), {
  'DESCRIPTOR' : _FOLDER,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.Folder)
  })
_sym_db.RegisterMessage(Folder)

GetFolderRequest = _reflection.GeneratedProtocolMessageType('GetFolderRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFOLDERREQUEST,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.GetFolderRequest)
  })
_sym_db.RegisterMessage(GetFolderRequest)

ListFoldersRequest = _reflection.GeneratedProtocolMessageType('ListFoldersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFOLDERSREQUEST,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.ListFoldersRequest)
  })
_sym_db.RegisterMessage(ListFoldersRequest)

ListFoldersResponse = _reflection.GeneratedProtocolMessageType('ListFoldersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFOLDERSRESPONSE,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.ListFoldersResponse)
  })
_sym_db.RegisterMessage(ListFoldersResponse)

SearchFoldersRequest = _reflection.GeneratedProtocolMessageType('SearchFoldersRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHFOLDERSREQUEST,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.SearchFoldersRequest)
  })
_sym_db.RegisterMessage(SearchFoldersRequest)

SearchFoldersResponse = _reflection.GeneratedProtocolMessageType('SearchFoldersResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHFOLDERSRESPONSE,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.SearchFoldersResponse)
  })
_sym_db.RegisterMessage(SearchFoldersResponse)

CreateFolderRequest = _reflection.GeneratedProtocolMessageType('CreateFolderRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFOLDERREQUEST,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.CreateFolderRequest)
  })
_sym_db.RegisterMessage(CreateFolderRequest)

CreateFolderMetadata = _reflection.GeneratedProtocolMessageType('CreateFolderMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFOLDERMETADATA,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.CreateFolderMetadata)
  })
_sym_db.RegisterMessage(CreateFolderMetadata)

UpdateFolderRequest = _reflection.GeneratedProtocolMessageType('UpdateFolderRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFOLDERREQUEST,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.UpdateFolderRequest)
  })
_sym_db.RegisterMessage(UpdateFolderRequest)

UpdateFolderMetadata = _reflection.GeneratedProtocolMessageType('UpdateFolderMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFOLDERMETADATA,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.UpdateFolderMetadata)
  })
_sym_db.RegisterMessage(UpdateFolderMetadata)

MoveFolderRequest = _reflection.GeneratedProtocolMessageType('MoveFolderRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVEFOLDERREQUEST,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.MoveFolderRequest)
  })
_sym_db.RegisterMessage(MoveFolderRequest)

MoveFolderMetadata = _reflection.GeneratedProtocolMessageType('MoveFolderMetadata', (_message.Message,), {
  'DESCRIPTOR' : _MOVEFOLDERMETADATA,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.MoveFolderMetadata)
  })
_sym_db.RegisterMessage(MoveFolderMetadata)

DeleteFolderRequest = _reflection.GeneratedProtocolMessageType('DeleteFolderRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFOLDERREQUEST,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.DeleteFolderRequest)
  })
_sym_db.RegisterMessage(DeleteFolderRequest)

DeleteFolderMetadata = _reflection.GeneratedProtocolMessageType('DeleteFolderMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFOLDERMETADATA,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.DeleteFolderMetadata)
  })
_sym_db.RegisterMessage(DeleteFolderMetadata)

UndeleteFolderRequest = _reflection.GeneratedProtocolMessageType('UndeleteFolderRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNDELETEFOLDERREQUEST,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.UndeleteFolderRequest)
  })
_sym_db.RegisterMessage(UndeleteFolderRequest)

UndeleteFolderMetadata = _reflection.GeneratedProtocolMessageType('UndeleteFolderMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UNDELETEFOLDERMETADATA,
  '__module__' : 'google.cloud.resourcemanager.v3.folders_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.resourcemanager.v3.UndeleteFolderMetadata)
  })
_sym_db.RegisterMessage(UndeleteFolderMetadata)

_FOLDERS = DESCRIPTOR.services_by_name['Folders']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.resourcemanager.v3B\014FoldersProtoP\001ZNgoogle.golang.org/genproto/googleapis/cloud/resourcemanager/v3;resourcemanager\252\002\037Google.Cloud.ResourceManager.V3\312\002\037Google\\Cloud\\ResourceManager\\V3\352\002\"Google::Cloud::ResourceManager::V3'
  _FOLDER.fields_by_name['name']._options = None
  _FOLDER.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _FOLDER.fields_by_name['parent']._options = None
  _FOLDER.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _FOLDER.fields_by_name['state']._options = None
  _FOLDER.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _FOLDER.fields_by_name['create_time']._options = None
  _FOLDER.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _FOLDER.fields_by_name['update_time']._options = None
  _FOLDER.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _FOLDER.fields_by_name['delete_time']._options = None
  _FOLDER.fields_by_name['delete_time']._serialized_options = b'\342A\001\003'
  _FOLDER.fields_by_name['etag']._options = None
  _FOLDER.fields_by_name['etag']._serialized_options = b'\342A\001\003'
  _FOLDER._options = None
  _FOLDER._serialized_options = b'\352AA\n*cloudresourcemanager.googleapis.com/Folder\022\020folders/{folder}R\001\001'
  _GETFOLDERREQUEST.fields_by_name['name']._options = None
  _GETFOLDERREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A,\n*cloudresourcemanager.googleapis.com/Folder'
  _LISTFOLDERSREQUEST.fields_by_name['parent']._options = None
  _LISTFOLDERSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\003\022\001*'
  _LISTFOLDERSREQUEST.fields_by_name['page_size']._options = None
  _LISTFOLDERSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTFOLDERSREQUEST.fields_by_name['page_token']._options = None
  _LISTFOLDERSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTFOLDERSREQUEST.fields_by_name['show_deleted']._options = None
  _LISTFOLDERSREQUEST.fields_by_name['show_deleted']._serialized_options = b'\342A\001\001'
  _SEARCHFOLDERSREQUEST.fields_by_name['page_size']._options = None
  _SEARCHFOLDERSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _SEARCHFOLDERSREQUEST.fields_by_name['page_token']._options = None
  _SEARCHFOLDERSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _SEARCHFOLDERSREQUEST.fields_by_name['query']._options = None
  _SEARCHFOLDERSREQUEST.fields_by_name['query']._serialized_options = b'\342A\001\001'
  _CREATEFOLDERREQUEST.fields_by_name['folder']._options = None
  _CREATEFOLDERREQUEST.fields_by_name['folder']._serialized_options = b'\342A\001\002'
  _UPDATEFOLDERREQUEST.fields_by_name['folder']._options = None
  _UPDATEFOLDERREQUEST.fields_by_name['folder']._serialized_options = b'\342A\001\002'
  _UPDATEFOLDERREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEFOLDERREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _MOVEFOLDERREQUEST.fields_by_name['name']._options = None
  _MOVEFOLDERREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A,\n*cloudresourcemanager.googleapis.com/Folder'
  _MOVEFOLDERREQUEST.fields_by_name['destination_parent']._options = None
  _MOVEFOLDERREQUEST.fields_by_name['destination_parent']._serialized_options = b'\342A\001\002\372A\003\022\001*'
  _DELETEFOLDERREQUEST.fields_by_name['name']._options = None
  _DELETEFOLDERREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A,\n*cloudresourcemanager.googleapis.com/Folder'
  _UNDELETEFOLDERREQUEST.fields_by_name['name']._options = None
  _UNDELETEFOLDERREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A,\n*cloudresourcemanager.googleapis.com/Folder'
  _FOLDERS._options = None
  _FOLDERS._serialized_options = b'\312A#cloudresourcemanager.googleapis.com\322Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
  _FOLDERS.methods_by_name['GetFolder']._options = None
  _FOLDERS.methods_by_name['GetFolder']._serialized_options = b'\332A\004name\202\323\344\223\002\026\022\024/v3/{name=folders/*}'
  _FOLDERS.methods_by_name['ListFolders']._options = None
  _FOLDERS.methods_by_name['ListFolders']._serialized_options = b'\332A\006parent\202\323\344\223\002\r\022\013/v3/folders'
  _FOLDERS.methods_by_name['SearchFolders']._options = None
  _FOLDERS.methods_by_name['SearchFolders']._serialized_options = b'\332A\005query\202\323\344\223\002\024\022\022/v3/folders:search'
  _FOLDERS.methods_by_name['CreateFolder']._options = None
  _FOLDERS.methods_by_name['CreateFolder']._serialized_options = b'\312A\036\n\006Folder\022\024CreateFolderMetadata\332A\006folder\202\323\344\223\002\025\"\013/v3/folders:\006folder'
  _FOLDERS.methods_by_name['UpdateFolder']._options = None
  _FOLDERS.methods_by_name['UpdateFolder']._serialized_options = b'\312A\036\n\006Folder\022\024UpdateFolderMetadata\332A\022folder,update_mask\202\323\344\223\002%2\033/v3/{folder.name=folders/*}:\006folder'
  _FOLDERS.methods_by_name['MoveFolder']._options = None
  _FOLDERS.methods_by_name['MoveFolder']._serialized_options = b'\312A\034\n\006Folder\022\022MoveFolderMetadata\332A\027name,destination_parent\202\323\344\223\002\036\"\031/v3/{name=folders/*}:move:\001*'
  _FOLDERS.methods_by_name['DeleteFolder']._options = None
  _FOLDERS.methods_by_name['DeleteFolder']._serialized_options = b'\312A\036\n\006Folder\022\024DeleteFolderMetadata\332A\004name\202\323\344\223\002\026*\024/v3/{name=folders/*}'
  _FOLDERS.methods_by_name['UndeleteFolder']._options = None
  _FOLDERS.methods_by_name['UndeleteFolder']._serialized_options = b'\312A \n\006Folder\022\026UndeleteFolderMetadata\332A\004name\202\323\344\223\002\"\"\035/v3/{name=folders/*}:undelete:\001*'
  _FOLDERS.methods_by_name['GetIamPolicy']._options = None
  _FOLDERS.methods_by_name['GetIamPolicy']._serialized_options = b'\332A\010resource\202\323\344\223\002*\"%/v3/{resource=folders/*}:getIamPolicy:\001*'
  _FOLDERS.methods_by_name['SetIamPolicy']._options = None
  _FOLDERS.methods_by_name['SetIamPolicy']._serialized_options = b'\332A\017resource,policy\202\323\344\223\002*\"%/v3/{resource=folders/*}:setIamPolicy:\001*'
  _FOLDERS.methods_by_name['TestIamPermissions']._options = None
  _FOLDERS.methods_by_name['TestIamPermissions']._serialized_options = b'\332A\024resource,permissions\202\323\344\223\0020\"+/v3/{resource=folders/*}:testIamPermissions:\001*'
  _FOLDER._serialized_start=362
  _FOLDER._serialized_end=899
  _FOLDER_STATE._serialized_start=765
  _FOLDER_STATE._serialized_end=829
  _GETFOLDERREQUEST._serialized_start=901
  _GETFOLDERREQUEST._serialized_end=992
  _LISTFOLDERSREQUEST._serialized_start=995
  _LISTFOLDERSREQUEST._serialized_end=1164
  _LISTFOLDERSRESPONSE._serialized_start=1167
  _LISTFOLDERSRESPONSE._serialized_end=1295
  _SEARCHFOLDERSREQUEST._serialized_start=1297
  _SEARCHFOLDERSREQUEST._serialized_end=1419
  _SEARCHFOLDERSRESPONSE._serialized_start=1422
  _SEARCHFOLDERSRESPONSE._serialized_end=1552
  _CREATEFOLDERREQUEST._serialized_start=1554
  _CREATEFOLDERREQUEST._serialized_end=1646
  _CREATEFOLDERMETADATA._serialized_start=1648
  _CREATEFOLDERMETADATA._serialized_end=1729
  _UPDATEFOLDERREQUEST._serialized_start=1732
  _UPDATEFOLDERREQUEST._serialized_end=1891
  _UPDATEFOLDERMETADATA._serialized_start=1893
  _UPDATEFOLDERMETADATA._serialized_end=1915
  _MOVEFOLDERREQUEST._serialized_start=1918
  _MOVEFOLDERREQUEST._serialized_end=2069
  _MOVEFOLDERMETADATA._serialized_start=2072
  _MOVEFOLDERMETADATA._serialized_end=2211
  _DELETEFOLDERREQUEST._serialized_start=2213
  _DELETEFOLDERREQUEST._serialized_end=2307
  _DELETEFOLDERMETADATA._serialized_start=2309
  _DELETEFOLDERMETADATA._serialized_end=2331
  _UNDELETEFOLDERREQUEST._serialized_start=2333
  _UNDELETEFOLDERREQUEST._serialized_end=2429
  _UNDELETEFOLDERMETADATA._serialized_start=2431
  _UNDELETEFOLDERMETADATA._serialized_end=2455
  _FOLDERS._serialized_start=2458
  _FOLDERS._serialized_end=4472
# @@protoc_insertion_point(module_scope)
