# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/version.proto
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
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/dialogflow/v2beta1/version.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x83\x04\n\x07Version\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12&\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\x0b\x64\x65scription\x12+\n\x0eversion_number\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x03R\rversionNumber\x12\x41\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12T\n\x06status\x18\x06 \x01(\x0e\x32\x36.google.cloud.dialogflow.v2beta1.Version.VersionStatusB\x04\xe2\x41\x01\x03R\x06status\"W\n\rVersionStatus\x12\x1e\n\x1aVERSION_STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03:\x96\x01\xea\x41\x92\x01\n!dialogflow.googleapis.com/Version\x12+projects/{project}/agent/versions/{version}\x12@projects/{project}/locations/{location}/agent/versions/{version}\"\xa1\x01\n\x13ListVersionsRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\x12!dialogflow.googleapis.com/VersionR\x06parent\x12!\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\"\x84\x01\n\x14ListVersionsResponse\x12\x44\n\x08versions\x18\x01 \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.VersionR\x08versions\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"S\n\x11GetVersionRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!dialogflow.googleapis.com/VersionR\x04name\"\xa4\x01\n\x14\x43reateVersionRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\x12!dialogflow.googleapis.com/VersionR\x06parent\x12H\n\x07version\x18\x02 \x01(\x0b\x32(.google.cloud.dialogflow.v2beta1.VersionB\x04\xe2\x41\x01\x02R\x07version\"\xa3\x01\n\x14UpdateVersionRequest\x12H\n\x07version\x18\x01 \x01(\x0b\x32(.google.cloud.dialogflow.v2beta1.VersionB\x04\xe2\x41\x01\x02R\x07version\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"V\n\x14\x44\x65leteVersionRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!dialogflow.googleapis.com/VersionR\x04name2\xdb\n\n\x08Versions\x12\xf4\x01\n\x0cListVersions\x12\x34.google.cloud.dialogflow.v2beta1.ListVersionsRequest\x1a\x35.google.cloud.dialogflow.v2beta1.ListVersionsResponse\"w\xda\x41\x06parent\x82\xd3\xe4\x93\x02h\x12+/v2beta1/{parent=projects/*/agent}/versionsZ9\x12\x37/v2beta1/{parent=projects/*/locations/*/agent}/versions\x12\xe1\x01\n\nGetVersion\x12\x32.google.cloud.dialogflow.v2beta1.GetVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version\"u\xda\x41\x04name\x82\xd3\xe4\x93\x02h\x12+/v2beta1/{name=projects/*/agent/versions/*}Z9\x12\x37/v2beta1/{name=projects/*/locations/*/agent/versions/*}\x12\x84\x02\n\rCreateVersion\x12\x35.google.cloud.dialogflow.v2beta1.CreateVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version\"\x91\x01\xda\x41\x0eparent,version\x82\xd3\xe4\x93\x02z\"+/v2beta1/{parent=projects/*/agent}/versions:\x07versionZB\"7/v2beta1/{parent=projects/*/locations/*/agent}/versions:\x07version\x12\x9a\x02\n\rUpdateVersion\x12\x35.google.cloud.dialogflow.v2beta1.UpdateVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version\"\xa7\x01\xda\x41\x13version,update_mask\x82\xd3\xe4\x93\x02\x8a\x01\x32\x33/v2beta1/{version.name=projects/*/agent/versions/*}:\x07versionZJ2?/v2beta1/{version.name=projects/*/locations/*/agent/versions/*}:\x07version\x12\xd5\x01\n\rDeleteVersion\x12\x35.google.cloud.dialogflow.v2beta1.DeleteVersionRequest\x1a\x16.google.protobuf.Empty\"u\xda\x41\x04name\x82\xd3\xe4\x93\x02h*+/v2beta1/{name=projects/*/agent/versions/*}Z9*7/v2beta1/{name=projects/*/locations/*/agent/versions/*}\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xaa\x01\n#com.google.cloud.dialogflow.v2beta1B\x0cVersionProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3')



_VERSION = DESCRIPTOR.message_types_by_name['Version']
_LISTVERSIONSREQUEST = DESCRIPTOR.message_types_by_name['ListVersionsRequest']
_LISTVERSIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListVersionsResponse']
_GETVERSIONREQUEST = DESCRIPTOR.message_types_by_name['GetVersionRequest']
_CREATEVERSIONREQUEST = DESCRIPTOR.message_types_by_name['CreateVersionRequest']
_UPDATEVERSIONREQUEST = DESCRIPTOR.message_types_by_name['UpdateVersionRequest']
_DELETEVERSIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteVersionRequest']
_VERSION_VERSIONSTATUS = _VERSION.enum_types_by_name['VersionStatus']
Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'google.cloud.dialogflow.v2beta1.version_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.Version)
  })
_sym_db.RegisterMessage(Version)

ListVersionsRequest = _reflection.GeneratedProtocolMessageType('ListVersionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVERSIONSREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.version_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListVersionsRequest)
  })
_sym_db.RegisterMessage(ListVersionsRequest)

ListVersionsResponse = _reflection.GeneratedProtocolMessageType('ListVersionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVERSIONSRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.version_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListVersionsResponse)
  })
_sym_db.RegisterMessage(ListVersionsResponse)

GetVersionRequest = _reflection.GeneratedProtocolMessageType('GetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.version_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.GetVersionRequest)
  })
_sym_db.RegisterMessage(GetVersionRequest)

CreateVersionRequest = _reflection.GeneratedProtocolMessageType('CreateVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVERSIONREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.version_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.CreateVersionRequest)
  })
_sym_db.RegisterMessage(CreateVersionRequest)

UpdateVersionRequest = _reflection.GeneratedProtocolMessageType('UpdateVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVERSIONREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.version_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.UpdateVersionRequest)
  })
_sym_db.RegisterMessage(UpdateVersionRequest)

DeleteVersionRequest = _reflection.GeneratedProtocolMessageType('DeleteVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVERSIONREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.version_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.DeleteVersionRequest)
  })
_sym_db.RegisterMessage(DeleteVersionRequest)

_VERSIONS = DESCRIPTOR.services_by_name['Versions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\014VersionProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1'
  _VERSION.fields_by_name['name']._options = None
  _VERSION.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _VERSION.fields_by_name['description']._options = None
  _VERSION.fields_by_name['description']._serialized_options = b'\342A\001\001'
  _VERSION.fields_by_name['version_number']._options = None
  _VERSION.fields_by_name['version_number']._serialized_options = b'\342A\001\003'
  _VERSION.fields_by_name['create_time']._options = None
  _VERSION.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _VERSION.fields_by_name['status']._options = None
  _VERSION.fields_by_name['status']._serialized_options = b'\342A\001\003'
  _VERSION._options = None
  _VERSION._serialized_options = b'\352A\222\001\n!dialogflow.googleapis.com/Version\022+projects/{project}/agent/versions/{version}\022@projects/{project}/locations/{location}/agent/versions/{version}'
  _LISTVERSIONSREQUEST.fields_by_name['parent']._options = None
  _LISTVERSIONSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\022!dialogflow.googleapis.com/Version'
  _LISTVERSIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTVERSIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTVERSIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTVERSIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _GETVERSIONREQUEST.fields_by_name['name']._options = None
  _GETVERSIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A#\n!dialogflow.googleapis.com/Version'
  _CREATEVERSIONREQUEST.fields_by_name['parent']._options = None
  _CREATEVERSIONREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\022!dialogflow.googleapis.com/Version'
  _CREATEVERSIONREQUEST.fields_by_name['version']._options = None
  _CREATEVERSIONREQUEST.fields_by_name['version']._serialized_options = b'\342A\001\002'
  _UPDATEVERSIONREQUEST.fields_by_name['version']._options = None
  _UPDATEVERSIONREQUEST.fields_by_name['version']._serialized_options = b'\342A\001\002'
  _UPDATEVERSIONREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEVERSIONREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _DELETEVERSIONREQUEST.fields_by_name['name']._options = None
  _DELETEVERSIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A#\n!dialogflow.googleapis.com/Version'
  _VERSIONS._options = None
  _VERSIONS._serialized_options = b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
  _VERSIONS.methods_by_name['ListVersions']._options = None
  _VERSIONS.methods_by_name['ListVersions']._serialized_options = b'\332A\006parent\202\323\344\223\002h\022+/v2beta1/{parent=projects/*/agent}/versionsZ9\0227/v2beta1/{parent=projects/*/locations/*/agent}/versions'
  _VERSIONS.methods_by_name['GetVersion']._options = None
  _VERSIONS.methods_by_name['GetVersion']._serialized_options = b'\332A\004name\202\323\344\223\002h\022+/v2beta1/{name=projects/*/agent/versions/*}Z9\0227/v2beta1/{name=projects/*/locations/*/agent/versions/*}'
  _VERSIONS.methods_by_name['CreateVersion']._options = None
  _VERSIONS.methods_by_name['CreateVersion']._serialized_options = b'\332A\016parent,version\202\323\344\223\002z\"+/v2beta1/{parent=projects/*/agent}/versions:\007versionZB\"7/v2beta1/{parent=projects/*/locations/*/agent}/versions:\007version'
  _VERSIONS.methods_by_name['UpdateVersion']._options = None
  _VERSIONS.methods_by_name['UpdateVersion']._serialized_options = b'\332A\023version,update_mask\202\323\344\223\002\212\00123/v2beta1/{version.name=projects/*/agent/versions/*}:\007versionZJ2?/v2beta1/{version.name=projects/*/locations/*/agent/versions/*}:\007version'
  _VERSIONS.methods_by_name['DeleteVersion']._options = None
  _VERSIONS.methods_by_name['DeleteVersion']._serialized_options = b'\332A\004name\202\323\344\223\002h*+/v2beta1/{name=projects/*/agent/versions/*}Z9*7/v2beta1/{name=projects/*/locations/*/agent/versions/*}'
  _VERSION._serialized_start=294
  _VERSION._serialized_end=809
  _VERSION_VERSIONSTATUS._serialized_start=569
  _VERSION_VERSIONSTATUS._serialized_end=656
  _LISTVERSIONSREQUEST._serialized_start=812
  _LISTVERSIONSREQUEST._serialized_end=973
  _LISTVERSIONSRESPONSE._serialized_start=976
  _LISTVERSIONSRESPONSE._serialized_end=1108
  _GETVERSIONREQUEST._serialized_start=1110
  _GETVERSIONREQUEST._serialized_end=1193
  _CREATEVERSIONREQUEST._serialized_start=1196
  _CREATEVERSIONREQUEST._serialized_end=1360
  _UPDATEVERSIONREQUEST._serialized_start=1363
  _UPDATEVERSIONREQUEST._serialized_end=1526
  _DELETEVERSIONREQUEST._serialized_start=1528
  _DELETEVERSIONREQUEST._serialized_end=1614
  _VERSIONS._serialized_start=1617
  _VERSIONS._serialized_end=2988
# @@protoc_insertion_point(module_scope)
