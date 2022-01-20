# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/sql/v1beta4/cloud_sql_connect.proto
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
from google.cloud.sql.v1beta4 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1beta4_dot_cloud__sql__resources__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/sql/v1beta4/cloud_sql_connect.proto\x12\x18google.cloud.sql.v1beta4\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x32google/cloud/sql/v1beta4/cloud_sql_resources.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/api/client.proto\"\x90\x01\n\x19GetConnectSettingsRequest\x12\x1a\n\x08instance\x18\x01 \x01(\tR\x08instance\x12\x18\n\x07project\x18\x02 \x01(\tR\x07project\x12=\n\tread_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x01R\x08readTime\"\xf4\x02\n\x0f\x43onnectSettings\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\x12G\n\x0eserver_ca_cert\x18\x02 \x01(\x0b\x32!.google.cloud.sql.v1beta4.SslCertR\x0cserverCaCert\x12\x46\n\x0cip_addresses\x18\x03 \x03(\x0b\x32#.google.cloud.sql.v1beta4.IpMappingR\x0bipAddresses\x12\x16\n\x06region\x18\x04 \x01(\tR\x06region\x12W\n\x10\x64\x61tabase_version\x18\x1f \x01(\x0e\x32,.google.cloud.sql.v1beta4.SqlDatabaseVersionR\x0f\x64\x61tabaseVersion\x12K\n\x0c\x62\x61\x63kend_type\x18  \x01(\x0e\x32(.google.cloud.sql.v1beta4.SqlBackendTypeR\x0b\x62\x61\x63kendType\"\xa3\x02\n\x1cGenerateEphemeralCertRequest\x12\x1a\n\x08instance\x18\x01 \x01(\tR\x08instance\x12\x18\n\x07project\x18\x02 \x01(\tR\x07project\x12\x1d\n\npublic_key\x18\x03 \x01(\tR\tpublicKey\x12\'\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\x0b\x61\x63\x63\x65ssToken\x12=\n\tread_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x01R\x08readTime\x12\x46\n\x0evalid_duration\x18\x0c \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe2\x41\x01\x01R\rvalidDuration\"i\n\x1dGenerateEphemeralCertResponse\x12H\n\x0e\x65phemeral_cert\x18\x01 \x01(\x0b\x32!.google.cloud.sql.v1beta4.SslCertR\rephemeralCert2\xb8\x04\n\x11SqlConnectService\x12\xc2\x01\n\x12GetConnectSettings\x12\x33.google.cloud.sql.v1beta4.GetConnectSettingsRequest\x1a).google.cloud.sql.v1beta4.ConnectSettings\"L\x82\xd3\xe4\x93\x02\x46\x12\x44/sql/v1beta4/projects/{project}/instances/{instance}/connectSettings\x12\xdf\x01\n\x15GenerateEphemeralCert\x12\x36.google.cloud.sql.v1beta4.GenerateEphemeralCertRequest\x1a\x37.google.cloud.sql.v1beta4.GenerateEphemeralCertResponse\"U\x82\xd3\xe4\x93\x02O\"J/sql/v1beta4/projects/{project}/instances/{instance}:generateEphemeralCert:\x01*\x1a|\xca\x41\x17sqladmin.googleapis.com\xd2\x41_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminBs\n\x1c\x63om.google.cloud.sql.v1beta4B\x14\x43loudSqlConnectProtoP\x01Z;google.golang.org/genproto/googleapis/cloud/sql/v1beta4;sqlb\x06proto3')



_GETCONNECTSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['GetConnectSettingsRequest']
_CONNECTSETTINGS = DESCRIPTOR.message_types_by_name['ConnectSettings']
_GENERATEEPHEMERALCERTREQUEST = DESCRIPTOR.message_types_by_name['GenerateEphemeralCertRequest']
_GENERATEEPHEMERALCERTRESPONSE = DESCRIPTOR.message_types_by_name['GenerateEphemeralCertResponse']
GetConnectSettingsRequest = _reflection.GeneratedProtocolMessageType('GetConnectSettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTSETTINGSREQUEST,
  '__module__' : 'google.cloud.sql.v1beta4.cloud_sql_connect_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.sql.v1beta4.GetConnectSettingsRequest)
  })
_sym_db.RegisterMessage(GetConnectSettingsRequest)

ConnectSettings = _reflection.GeneratedProtocolMessageType('ConnectSettings', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTSETTINGS,
  '__module__' : 'google.cloud.sql.v1beta4.cloud_sql_connect_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.sql.v1beta4.ConnectSettings)
  })
_sym_db.RegisterMessage(ConnectSettings)

GenerateEphemeralCertRequest = _reflection.GeneratedProtocolMessageType('GenerateEphemeralCertRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEEPHEMERALCERTREQUEST,
  '__module__' : 'google.cloud.sql.v1beta4.cloud_sql_connect_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.sql.v1beta4.GenerateEphemeralCertRequest)
  })
_sym_db.RegisterMessage(GenerateEphemeralCertRequest)

GenerateEphemeralCertResponse = _reflection.GeneratedProtocolMessageType('GenerateEphemeralCertResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEEPHEMERALCERTRESPONSE,
  '__module__' : 'google.cloud.sql.v1beta4.cloud_sql_connect_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.sql.v1beta4.GenerateEphemeralCertResponse)
  })
_sym_db.RegisterMessage(GenerateEphemeralCertResponse)

_SQLCONNECTSERVICE = DESCRIPTOR.services_by_name['SqlConnectService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.google.cloud.sql.v1beta4B\024CloudSqlConnectProtoP\001Z;google.golang.org/genproto/googleapis/cloud/sql/v1beta4;sql'
  _GETCONNECTSETTINGSREQUEST.fields_by_name['read_time']._options = None
  _GETCONNECTSETTINGSREQUEST.fields_by_name['read_time']._serialized_options = b'\342A\001\001'
  _GENERATEEPHEMERALCERTREQUEST.fields_by_name['access_token']._options = None
  _GENERATEEPHEMERALCERTREQUEST.fields_by_name['access_token']._serialized_options = b'\342A\001\001'
  _GENERATEEPHEMERALCERTREQUEST.fields_by_name['read_time']._options = None
  _GENERATEEPHEMERALCERTREQUEST.fields_by_name['read_time']._serialized_options = b'\342A\001\001'
  _GENERATEEPHEMERALCERTREQUEST.fields_by_name['valid_duration']._options = None
  _GENERATEEPHEMERALCERTREQUEST.fields_by_name['valid_duration']._serialized_options = b'\342A\001\001'
  _SQLCONNECTSERVICE._options = None
  _SQLCONNECTSERVICE._serialized_options = b'\312A\027sqladmin.googleapis.com\322A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
  _SQLCONNECTSERVICE.methods_by_name['GetConnectSettings']._options = None
  _SQLCONNECTSERVICE.methods_by_name['GetConnectSettings']._serialized_options = b'\202\323\344\223\002F\022D/sql/v1beta4/projects/{project}/instances/{instance}/connectSettings'
  _SQLCONNECTSERVICE.methods_by_name['GenerateEphemeralCert']._options = None
  _SQLCONNECTSERVICE.methods_by_name['GenerateEphemeralCert']._serialized_options = b'\202\323\344\223\002O\"J/sql/v1beta4/projects/{project}/instances/{instance}:generateEphemeralCert:\001*'
  _GETCONNECTSETTINGSREQUEST._serialized_start=284
  _GETCONNECTSETTINGSREQUEST._serialized_end=428
  _CONNECTSETTINGS._serialized_start=431
  _CONNECTSETTINGS._serialized_end=803
  _GENERATEEPHEMERALCERTREQUEST._serialized_start=806
  _GENERATEEPHEMERALCERTREQUEST._serialized_end=1097
  _GENERATEEPHEMERALCERTRESPONSE._serialized_start=1099
  _GENERATEEPHEMERALCERTRESPONSE._serialized_end=1204
  _SQLCONNECTSERVICE._serialized_start=1207
  _SQLCONNECTSERVICE._serialized_end=1775
# @@protoc_insertion_point(module_scope)
