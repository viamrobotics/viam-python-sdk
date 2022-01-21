# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/artifactregistry/v1beta2/repository.proto
"""Generated protocol buffer code."""
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
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/devtools/artifactregistry/v1beta2/repository.proto\x12(google.devtools.artifactregistry.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc1\x08\n\nRepository\x12o\n\x0cmaven_config\x18\t \x01(\x0b\x32J.google.devtools.artifactregistry.v1beta2.Repository.MavenRepositoryConfigH\x00R\x0bmavenConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12S\n\x06\x66ormat\x18\x02 \x01(\x0e\x32;.google.devtools.artifactregistry.v1beta2.Repository.FormatR\x06\x66ormat\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12X\n\x06labels\x18\x04 \x03(\x0b\x32@.google.devtools.artifactregistry.v1beta2.Repository.LabelsEntryR\x06labels\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12 \n\x0ckms_key_name\x18\x08 \x01(\tR\nkmsKeyName\x1a\xa0\x02\n\x15MavenRepositoryConfig\x12:\n\x19\x61llow_snapshot_overwrites\x18\x01 \x01(\x08R\x17\x61llowSnapshotOverwrites\x12\x7f\n\x0eversion_policy\x18\x02 \x01(\x0e\x32X.google.devtools.artifactregistry.v1beta2.Repository.MavenRepositoryConfig.VersionPolicyR\rversionPolicy\"J\n\rVersionPolicy\x12\x1e\n\x1aVERSION_POLICY_UNSPECIFIED\x10\x00\x12\x0b\n\x07RELEASE\x10\x01\x12\x0c\n\x08SNAPSHOT\x10\x02\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"^\n\x06\x46ormat\x12\x16\n\x12\x46ORMAT_UNSPECIFIED\x10\x00\x12\n\n\x06\x44OCKER\x10\x01\x12\t\n\x05MAVEN\x10\x02\x12\x07\n\x03NPM\x10\x03\x12\x07\n\x03\x41PT\x10\x05\x12\x07\n\x03YUM\x10\x06\x12\n\n\x06PYTHON\x10\x08:r\xea\x41o\n*artifactregistry.googleapis.com/Repository\x12\x41projects/{project}/locations/{location}/repositories/{repository}B\x0f\n\rformat_config\"\xa2\x01\n\x17ListRepositoriesRequest\x12K\n\x06parent\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\x12*artifactregistry.googleapis.com/RepositoryR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x9c\x01\n\x18ListRepositoriesResponse\x12X\n\x0crepositories\x18\x01 \x03(\x0b\x32\x34.google.devtools.artifactregistry.v1beta2.RepositoryR\x0crepositories\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"_\n\x14GetRepositoryRequest\x12G\n\x04name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*artifactregistry.googleapis.com/RepositoryR\x04name\"\xe1\x01\n\x17\x43reateRepositoryRequest\x12K\n\x06parent\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\x12*artifactregistry.googleapis.com/RepositoryR\x06parent\x12#\n\rrepository_id\x18\x02 \x01(\tR\x0crepositoryId\x12T\n\nrepository\x18\x03 \x01(\x0b\x32\x34.google.devtools.artifactregistry.v1beta2.RepositoryR\nrepository\"\xac\x01\n\x17UpdateRepositoryRequest\x12T\n\nrepository\x18\x01 \x01(\x0b\x32\x34.google.devtools.artifactregistry.v1beta2.RepositoryR\nrepository\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"b\n\x17\x44\x65leteRepositoryRequest\x12G\n\x04name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*artifactregistry.googleapis.com/RepositoryR\x04nameB\x96\x02\n,com.google.devtools.artifactregistry.v1beta2B\x0fRepositoryProtoP\x01ZXgoogle.golang.org/genproto/googleapis/devtools/artifactregistry/v1beta2;artifactregistry\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3')



_REPOSITORY = DESCRIPTOR.message_types_by_name['Repository']
_REPOSITORY_MAVENREPOSITORYCONFIG = _REPOSITORY.nested_types_by_name['MavenRepositoryConfig']
_REPOSITORY_LABELSENTRY = _REPOSITORY.nested_types_by_name['LabelsEntry']
_LISTREPOSITORIESREQUEST = DESCRIPTOR.message_types_by_name['ListRepositoriesRequest']
_LISTREPOSITORIESRESPONSE = DESCRIPTOR.message_types_by_name['ListRepositoriesResponse']
_GETREPOSITORYREQUEST = DESCRIPTOR.message_types_by_name['GetRepositoryRequest']
_CREATEREPOSITORYREQUEST = DESCRIPTOR.message_types_by_name['CreateRepositoryRequest']
_UPDATEREPOSITORYREQUEST = DESCRIPTOR.message_types_by_name['UpdateRepositoryRequest']
_DELETEREPOSITORYREQUEST = DESCRIPTOR.message_types_by_name['DeleteRepositoryRequest']
_REPOSITORY_MAVENREPOSITORYCONFIG_VERSIONPOLICY = _REPOSITORY_MAVENREPOSITORYCONFIG.enum_types_by_name['VersionPolicy']
_REPOSITORY_FORMAT = _REPOSITORY.enum_types_by_name['Format']
Repository = _reflection.GeneratedProtocolMessageType('Repository', (_message.Message,), {

  'MavenRepositoryConfig' : _reflection.GeneratedProtocolMessageType('MavenRepositoryConfig', (_message.Message,), {
    'DESCRIPTOR' : _REPOSITORY_MAVENREPOSITORYCONFIG,
    '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.Repository.MavenRepositoryConfig)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REPOSITORY_LABELSENTRY,
    '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.Repository.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _REPOSITORY,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.Repository)
  })
_sym_db.RegisterMessage(Repository)
_sym_db.RegisterMessage(Repository.MavenRepositoryConfig)
_sym_db.RegisterMessage(Repository.LabelsEntry)

ListRepositoriesRequest = _reflection.GeneratedProtocolMessageType('ListRepositoriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREPOSITORIESREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.ListRepositoriesRequest)
  })
_sym_db.RegisterMessage(ListRepositoriesRequest)

ListRepositoriesResponse = _reflection.GeneratedProtocolMessageType('ListRepositoriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTREPOSITORIESRESPONSE,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.ListRepositoriesResponse)
  })
_sym_db.RegisterMessage(ListRepositoriesResponse)

GetRepositoryRequest = _reflection.GeneratedProtocolMessageType('GetRepositoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREPOSITORYREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.GetRepositoryRequest)
  })
_sym_db.RegisterMessage(GetRepositoryRequest)

CreateRepositoryRequest = _reflection.GeneratedProtocolMessageType('CreateRepositoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREPOSITORYREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.CreateRepositoryRequest)
  })
_sym_db.RegisterMessage(CreateRepositoryRequest)

UpdateRepositoryRequest = _reflection.GeneratedProtocolMessageType('UpdateRepositoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREPOSITORYREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.UpdateRepositoryRequest)
  })
_sym_db.RegisterMessage(UpdateRepositoryRequest)

DeleteRepositoryRequest = _reflection.GeneratedProtocolMessageType('DeleteRepositoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREPOSITORYREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.repository_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.DeleteRepositoryRequest)
  })
_sym_db.RegisterMessage(DeleteRepositoryRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n,com.google.devtools.artifactregistry.v1beta2B\017RepositoryProtoP\001ZXgoogle.golang.org/genproto/googleapis/devtools/artifactregistry/v1beta2;artifactregistry\252\002%Google.Cloud.ArtifactRegistry.V1Beta2\312\002%Google\\Cloud\\ArtifactRegistry\\V1beta2\352\002(Google::Cloud::ArtifactRegistry::V1beta2'
  _REPOSITORY_LABELSENTRY._options = None
  _REPOSITORY_LABELSENTRY._serialized_options = b'8\001'
  _REPOSITORY._options = None
  _REPOSITORY._serialized_options = b'\352Ao\n*artifactregistry.googleapis.com/Repository\022Aprojects/{project}/locations/{location}/repositories/{repository}'
  _LISTREPOSITORIESREQUEST.fields_by_name['parent']._options = None
  _LISTREPOSITORIESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A,\022*artifactregistry.googleapis.com/Repository'
  _GETREPOSITORYREQUEST.fields_by_name['name']._options = None
  _GETREPOSITORYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A,\n*artifactregistry.googleapis.com/Repository'
  _CREATEREPOSITORYREQUEST.fields_by_name['parent']._options = None
  _CREATEREPOSITORYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A,\022*artifactregistry.googleapis.com/Repository'
  _DELETEREPOSITORYREQUEST.fields_by_name['name']._options = None
  _DELETEREPOSITORYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A,\n*artifactregistry.googleapis.com/Repository'
  _REPOSITORY._serialized_start=261
  _REPOSITORY._serialized_end=1350
  _REPOSITORY_MAVENREPOSITORYCONFIG._serialized_start=774
  _REPOSITORY_MAVENREPOSITORYCONFIG._serialized_end=1062
  _REPOSITORY_MAVENREPOSITORYCONFIG_VERSIONPOLICY._serialized_start=988
  _REPOSITORY_MAVENREPOSITORYCONFIG_VERSIONPOLICY._serialized_end=1062
  _REPOSITORY_LABELSENTRY._serialized_start=1064
  _REPOSITORY_LABELSENTRY._serialized_end=1121
  _REPOSITORY_FORMAT._serialized_start=1123
  _REPOSITORY_FORMAT._serialized_end=1217
  _LISTREPOSITORIESREQUEST._serialized_start=1353
  _LISTREPOSITORIESREQUEST._serialized_end=1515
  _LISTREPOSITORIESRESPONSE._serialized_start=1518
  _LISTREPOSITORIESRESPONSE._serialized_end=1674
  _GETREPOSITORYREQUEST._serialized_start=1676
  _GETREPOSITORYREQUEST._serialized_end=1771
  _CREATEREPOSITORYREQUEST._serialized_start=1774
  _CREATEREPOSITORYREQUEST._serialized_end=1999
  _UPDATEREPOSITORYREQUEST._serialized_start=2002
  _UPDATEREPOSITORYREQUEST._serialized_end=2174
  _DELETEREPOSITORYREQUEST._serialized_start=2176
  _DELETEREPOSITORYREQUEST._serialized_end=2274
# @@protoc_insertion_point(module_scope)
