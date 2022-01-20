# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/connection/v1beta1/connection.proto
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
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/bigquery/connection/v1beta1/connection.proto\x12(google.cloud.bigquery.connection.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xe4\x01\n\x17\x43reateConnectionRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12)\n\rconnection_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\x0c\x63onnectionId\x12Z\n\nconnection\x18\x03 \x01(\x0b\x32\x34.google.cloud.bigquery.connection.v1beta1.ConnectionB\x04\xe2\x41\x01\x02R\nconnection\"a\n\x14GetConnectionRequest\x12I\n\x04name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,bigqueryconnection.googleapis.com/ConnectionR\x04name\"\xc0\x01\n\x16ListConnectionsRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x43\n\x0bmax_results\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x04\xe2\x41\x01\x02R\nmaxResults\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x99\x01\n\x17ListConnectionsResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12V\n\x0b\x63onnections\x18\x02 \x03(\x0b\x32\x34.google.cloud.bigquery.connection.v1beta1.ConnectionR\x0b\x63onnections\"\x83\x02\n\x17UpdateConnectionRequest\x12I\n\x04name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,bigqueryconnection.googleapis.com/ConnectionR\x04name\x12Z\n\nconnection\x18\x02 \x01(\x0b\x32\x34.google.cloud.bigquery.connection.v1beta1.ConnectionB\x04\xe2\x41\x01\x02R\nconnection\x12\x41\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"\xa3\x01\n!UpdateConnectionCredentialRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\x64\n\ncredential\x18\x02 \x01(\x0b\x32>.google.cloud.bigquery.connection.v1beta1.ConnectionCredentialB\x04\xe2\x41\x01\x02R\ncredential\"d\n\x17\x44\x65leteConnectionRequest\x12I\n\x04name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,bigqueryconnection.googleapis.com/ConnectionR\x04name\"\xd3\x03\n\nConnection\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rfriendly_name\x18\x02 \x01(\tR\x0c\x66riendlyName\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12[\n\tcloud_sql\x18\x04 \x01(\x0b\x32<.google.cloud.bigquery.connection.v1beta1.CloudSqlPropertiesH\x00R\x08\x63loudSql\x12)\n\rcreation_time\x18\x05 \x01(\x03\x42\x04\xe2\x41\x01\x03R\x0c\x63reationTime\x12\x32\n\x12last_modified_time\x18\x06 \x01(\x03\x42\x04\xe2\x41\x01\x03R\x10lastModifiedTime\x12+\n\x0ehas_credential\x18\x07 \x01(\x08\x42\x04\xe2\x41\x01\x03R\rhasCredential:s\xea\x41p\n,bigqueryconnection.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}B\x0c\n\nproperties\"\x81\x01\n\x14\x43onnectionCredential\x12[\n\tcloud_sql\x18\x01 \x01(\x0b\x32<.google.cloud.bigquery.connection.v1beta1.CloudSqlCredentialH\x00R\x08\x63loudSqlB\x0c\n\ncredential\"\xdc\x02\n\x12\x43loudSqlProperties\x12\x1f\n\x0binstance_id\x18\x01 \x01(\tR\ninstanceId\x12\x1a\n\x08\x64\x61tabase\x18\x02 \x01(\tR\x08\x64\x61tabase\x12]\n\x04type\x18\x03 \x01(\x0e\x32I.google.cloud.bigquery.connection.v1beta1.CloudSqlProperties.DatabaseTypeR\x04type\x12\x62\n\ncredential\x18\x04 \x01(\x0b\x32<.google.cloud.bigquery.connection.v1beta1.CloudSqlCredentialB\x04\xe2\x41\x01\x04R\ncredential\"F\n\x0c\x44\x61tabaseType\x12\x1d\n\x19\x44\x41TABASE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSTGRES\x10\x01\x12\t\n\x05MYSQL\x10\x02\"L\n\x12\x43loudSqlCredential\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password2\x98\x10\n\x11\x43onnectionService\x12\xf7\x01\n\x10\x43reateConnection\x12\x41.google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest\x1a\x34.google.cloud.bigquery.connection.v1beta1.Connection\"j\xda\x41\x1fparent,connection,connection_id\x82\xd3\xe4\x93\x02\x42\"4/v1beta1/{parent=projects/*/locations/*}/connections:\nconnection\x12\xca\x01\n\rGetConnection\x12>.google.cloud.bigquery.connection.v1beta1.GetConnectionRequest\x1a\x34.google.cloud.bigquery.connection.v1beta1.Connection\"C\xda\x41\x04name\x82\xd3\xe4\x93\x02\x36\x12\x34/v1beta1/{name=projects/*/locations/*/connections/*}\x12\xe9\x01\n\x0fListConnections\x12@.google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest\x1a\x41.google.cloud.bigquery.connection.v1beta1.ListConnectionsResponse\"Q\xda\x41\x12parent,max_results\x82\xd3\xe4\x93\x02\x36\x12\x34/v1beta1/{parent=projects/*/locations/*}/connections\x12\xf3\x01\n\x10UpdateConnection\x12\x41.google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest\x1a\x34.google.cloud.bigquery.connection.v1beta1.Connection\"f\xda\x41\x1bname,connection,update_mask\x82\xd3\xe4\x93\x02\x42\x32\x34/v1beta1/{name=projects/*/locations/*/connections/*}:\nconnection\x12\xe8\x01\n\x1aUpdateConnectionCredential\x12K.google.cloud.bigquery.connection.v1beta1.UpdateConnectionCredentialRequest\x1a\x16.google.protobuf.Empty\"e\xda\x41\x0fname,credential\x82\xd3\xe4\x93\x02M2?/v1beta1/{name=projects/*/locations/*/connections/*/credential}:\ncredential\x12\xb2\x01\n\x10\x44\x65leteConnection\x12\x41.google.cloud.bigquery.connection.v1beta1.DeleteConnectionRequest\x1a\x16.google.protobuf.Empty\"C\xda\x41\x04name\x82\xd3\xe4\x93\x02\x36*4/v1beta1/{name=projects/*/locations/*/connections/*}\x12\xae\x01\n\x0cGetIamPolicy\x12\".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy\"c\xda\x41\x10resource,options\x82\xd3\xe4\x93\x02J\"E/v1beta1/{resource=projects/*/locations/*/connections/*}:getIamPolicy:\x01*\x12\xad\x01\n\x0cSetIamPolicy\x12\".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy\"b\xda\x41\x0fresource,policy\x82\xd3\xe4\x93\x02J\"E/v1beta1/{resource=projects/*/locations/*/connections/*}:setIamPolicy:\x01*\x12\xd8\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse\"m\xda\x41\x14resource,permissions\x82\xd3\xe4\x93\x02P\"K/v1beta1/{resource=projects/*/locations/*/connections/*}:testIamPermissions:\x01*\x1a~\xca\x41!bigqueryconnection.googleapis.com\xd2\x41Whttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xe9\x01\n,com.google.cloud.bigquery.connection.v1beta1B\x0f\x43onnectionProtoZRgoogle.golang.org/genproto/googleapis/cloud/bigquery/connection/v1beta1;connection\xaa\x02(Google.Cloud.BigQuery.Connection.V1Beta1\xca\x02(Google\\Cloud\\BigQuery\\Connection\\V1beta1b\x06proto3')



_CREATECONNECTIONREQUEST = DESCRIPTOR.message_types_by_name['CreateConnectionRequest']
_GETCONNECTIONREQUEST = DESCRIPTOR.message_types_by_name['GetConnectionRequest']
_LISTCONNECTIONSREQUEST = DESCRIPTOR.message_types_by_name['ListConnectionsRequest']
_LISTCONNECTIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListConnectionsResponse']
_UPDATECONNECTIONREQUEST = DESCRIPTOR.message_types_by_name['UpdateConnectionRequest']
_UPDATECONNECTIONCREDENTIALREQUEST = DESCRIPTOR.message_types_by_name['UpdateConnectionCredentialRequest']
_DELETECONNECTIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteConnectionRequest']
_CONNECTION = DESCRIPTOR.message_types_by_name['Connection']
_CONNECTIONCREDENTIAL = DESCRIPTOR.message_types_by_name['ConnectionCredential']
_CLOUDSQLPROPERTIES = DESCRIPTOR.message_types_by_name['CloudSqlProperties']
_CLOUDSQLCREDENTIAL = DESCRIPTOR.message_types_by_name['CloudSqlCredential']
_CLOUDSQLPROPERTIES_DATABASETYPE = _CLOUDSQLPROPERTIES.enum_types_by_name['DatabaseType']
CreateConnectionRequest = _reflection.GeneratedProtocolMessageType('CreateConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONNECTIONREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest)
  })
_sym_db.RegisterMessage(CreateConnectionRequest)

GetConnectionRequest = _reflection.GeneratedProtocolMessageType('GetConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTIONREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.GetConnectionRequest)
  })
_sym_db.RegisterMessage(GetConnectionRequest)

ListConnectionsRequest = _reflection.GeneratedProtocolMessageType('ListConnectionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONNECTIONSREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest)
  })
_sym_db.RegisterMessage(ListConnectionsRequest)

ListConnectionsResponse = _reflection.GeneratedProtocolMessageType('ListConnectionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONNECTIONSRESPONSE,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.ListConnectionsResponse)
  })
_sym_db.RegisterMessage(ListConnectionsResponse)

UpdateConnectionRequest = _reflection.GeneratedProtocolMessageType('UpdateConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONNECTIONREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest)
  })
_sym_db.RegisterMessage(UpdateConnectionRequest)

UpdateConnectionCredentialRequest = _reflection.GeneratedProtocolMessageType('UpdateConnectionCredentialRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONNECTIONCREDENTIALREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.UpdateConnectionCredentialRequest)
  })
_sym_db.RegisterMessage(UpdateConnectionCredentialRequest)

DeleteConnectionRequest = _reflection.GeneratedProtocolMessageType('DeleteConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECONNECTIONREQUEST,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.DeleteConnectionRequest)
  })
_sym_db.RegisterMessage(DeleteConnectionRequest)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTION,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.Connection)
  })
_sym_db.RegisterMessage(Connection)

ConnectionCredential = _reflection.GeneratedProtocolMessageType('ConnectionCredential', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONCREDENTIAL,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.ConnectionCredential)
  })
_sym_db.RegisterMessage(ConnectionCredential)

CloudSqlProperties = _reflection.GeneratedProtocolMessageType('CloudSqlProperties', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSQLPROPERTIES,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.CloudSqlProperties)
  })
_sym_db.RegisterMessage(CloudSqlProperties)

CloudSqlCredential = _reflection.GeneratedProtocolMessageType('CloudSqlCredential', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSQLCREDENTIAL,
  '__module__' : 'google.cloud.bigquery.connection.v1beta1.connection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.connection.v1beta1.CloudSqlCredential)
  })
_sym_db.RegisterMessage(CloudSqlCredential)

_CONNECTIONSERVICE = DESCRIPTOR.services_by_name['ConnectionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n,com.google.cloud.bigquery.connection.v1beta1B\017ConnectionProtoZRgoogle.golang.org/genproto/googleapis/cloud/bigquery/connection/v1beta1;connection\252\002(Google.Cloud.BigQuery.Connection.V1Beta1\312\002(Google\\Cloud\\BigQuery\\Connection\\V1beta1'
  _CREATECONNECTIONREQUEST.fields_by_name['parent']._options = None
  _CREATECONNECTIONREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _CREATECONNECTIONREQUEST.fields_by_name['connection_id']._options = None
  _CREATECONNECTIONREQUEST.fields_by_name['connection_id']._serialized_options = b'\342A\001\001'
  _CREATECONNECTIONREQUEST.fields_by_name['connection']._options = None
  _CREATECONNECTIONREQUEST.fields_by_name['connection']._serialized_options = b'\342A\001\002'
  _GETCONNECTIONREQUEST.fields_by_name['name']._options = None
  _GETCONNECTIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A.\n,bigqueryconnection.googleapis.com/Connection'
  _LISTCONNECTIONSREQUEST.fields_by_name['parent']._options = None
  _LISTCONNECTIONSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _LISTCONNECTIONSREQUEST.fields_by_name['max_results']._options = None
  _LISTCONNECTIONSREQUEST.fields_by_name['max_results']._serialized_options = b'\342A\001\002'
  _UPDATECONNECTIONREQUEST.fields_by_name['name']._options = None
  _UPDATECONNECTIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A.\n,bigqueryconnection.googleapis.com/Connection'
  _UPDATECONNECTIONREQUEST.fields_by_name['connection']._options = None
  _UPDATECONNECTIONREQUEST.fields_by_name['connection']._serialized_options = b'\342A\001\002'
  _UPDATECONNECTIONREQUEST.fields_by_name['update_mask']._options = None
  _UPDATECONNECTIONREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _UPDATECONNECTIONCREDENTIALREQUEST.fields_by_name['name']._options = None
  _UPDATECONNECTIONCREDENTIALREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _UPDATECONNECTIONCREDENTIALREQUEST.fields_by_name['credential']._options = None
  _UPDATECONNECTIONCREDENTIALREQUEST.fields_by_name['credential']._serialized_options = b'\342A\001\002'
  _DELETECONNECTIONREQUEST.fields_by_name['name']._options = None
  _DELETECONNECTIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A.\n,bigqueryconnection.googleapis.com/Connection'
  _CONNECTION.fields_by_name['creation_time']._options = None
  _CONNECTION.fields_by_name['creation_time']._serialized_options = b'\342A\001\003'
  _CONNECTION.fields_by_name['last_modified_time']._options = None
  _CONNECTION.fields_by_name['last_modified_time']._serialized_options = b'\342A\001\003'
  _CONNECTION.fields_by_name['has_credential']._options = None
  _CONNECTION.fields_by_name['has_credential']._serialized_options = b'\342A\001\003'
  _CONNECTION._options = None
  _CONNECTION._serialized_options = b'\352Ap\n,bigqueryconnection.googleapis.com/Connection\022@projects/{project}/locations/{location}/connections/{connection}'
  _CLOUDSQLPROPERTIES.fields_by_name['credential']._options = None
  _CLOUDSQLPROPERTIES.fields_by_name['credential']._serialized_options = b'\342A\001\004'
  _CONNECTIONSERVICE._options = None
  _CONNECTIONSERVICE._serialized_options = b'\312A!bigqueryconnection.googleapis.com\322AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
  _CONNECTIONSERVICE.methods_by_name['CreateConnection']._options = None
  _CONNECTIONSERVICE.methods_by_name['CreateConnection']._serialized_options = b'\332A\037parent,connection,connection_id\202\323\344\223\002B\"4/v1beta1/{parent=projects/*/locations/*}/connections:\nconnection'
  _CONNECTIONSERVICE.methods_by_name['GetConnection']._options = None
  _CONNECTIONSERVICE.methods_by_name['GetConnection']._serialized_options = b'\332A\004name\202\323\344\223\0026\0224/v1beta1/{name=projects/*/locations/*/connections/*}'
  _CONNECTIONSERVICE.methods_by_name['ListConnections']._options = None
  _CONNECTIONSERVICE.methods_by_name['ListConnections']._serialized_options = b'\332A\022parent,max_results\202\323\344\223\0026\0224/v1beta1/{parent=projects/*/locations/*}/connections'
  _CONNECTIONSERVICE.methods_by_name['UpdateConnection']._options = None
  _CONNECTIONSERVICE.methods_by_name['UpdateConnection']._serialized_options = b'\332A\033name,connection,update_mask\202\323\344\223\002B24/v1beta1/{name=projects/*/locations/*/connections/*}:\nconnection'
  _CONNECTIONSERVICE.methods_by_name['UpdateConnectionCredential']._options = None
  _CONNECTIONSERVICE.methods_by_name['UpdateConnectionCredential']._serialized_options = b'\332A\017name,credential\202\323\344\223\002M2?/v1beta1/{name=projects/*/locations/*/connections/*/credential}:\ncredential'
  _CONNECTIONSERVICE.methods_by_name['DeleteConnection']._options = None
  _CONNECTIONSERVICE.methods_by_name['DeleteConnection']._serialized_options = b'\332A\004name\202\323\344\223\0026*4/v1beta1/{name=projects/*/locations/*/connections/*}'
  _CONNECTIONSERVICE.methods_by_name['GetIamPolicy']._options = None
  _CONNECTIONSERVICE.methods_by_name['GetIamPolicy']._serialized_options = b'\332A\020resource,options\202\323\344\223\002J\"E/v1beta1/{resource=projects/*/locations/*/connections/*}:getIamPolicy:\001*'
  _CONNECTIONSERVICE.methods_by_name['SetIamPolicy']._options = None
  _CONNECTIONSERVICE.methods_by_name['SetIamPolicy']._serialized_options = b'\332A\017resource,policy\202\323\344\223\002J\"E/v1beta1/{resource=projects/*/locations/*/connections/*}:setIamPolicy:\001*'
  _CONNECTIONSERVICE.methods_by_name['TestIamPermissions']._options = None
  _CONNECTIONSERVICE.methods_by_name['TestIamPermissions']._serialized_options = b'\332A\024resource,permissions\202\323\344\223\002P\"K/v1beta1/{resource=projects/*/locations/*/connections/*}:testIamPermissions:\001*'
  _CREATECONNECTIONREQUEST._serialized_start=374
  _CREATECONNECTIONREQUEST._serialized_end=602
  _GETCONNECTIONREQUEST._serialized_start=604
  _GETCONNECTIONREQUEST._serialized_end=701
  _LISTCONNECTIONSREQUEST._serialized_start=704
  _LISTCONNECTIONSREQUEST._serialized_end=896
  _LISTCONNECTIONSRESPONSE._serialized_start=899
  _LISTCONNECTIONSRESPONSE._serialized_end=1052
  _UPDATECONNECTIONREQUEST._serialized_start=1055
  _UPDATECONNECTIONREQUEST._serialized_end=1314
  _UPDATECONNECTIONCREDENTIALREQUEST._serialized_start=1317
  _UPDATECONNECTIONCREDENTIALREQUEST._serialized_end=1480
  _DELETECONNECTIONREQUEST._serialized_start=1482
  _DELETECONNECTIONREQUEST._serialized_end=1582
  _CONNECTION._serialized_start=1585
  _CONNECTION._serialized_end=2052
  _CONNECTIONCREDENTIAL._serialized_start=2055
  _CONNECTIONCREDENTIAL._serialized_end=2184
  _CLOUDSQLPROPERTIES._serialized_start=2187
  _CLOUDSQLPROPERTIES._serialized_end=2535
  _CLOUDSQLPROPERTIES_DATABASETYPE._serialized_start=2465
  _CLOUDSQLPROPERTIES_DATABASETYPE._serialized_end=2535
  _CLOUDSQLCREDENTIAL._serialized_start=2537
  _CLOUDSQLCREDENTIAL._serialized_end=2613
  _CONNECTIONSERVICE._serialized_start=2616
  _CONNECTIONSERVICE._serialized_end=4688
# @@protoc_insertion_point(module_scope)
