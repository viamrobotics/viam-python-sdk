# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/networksecurity/v1beta1/server_tls_policy.proto
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
from google.cloud.networksecurity.v1beta1 import tls_pb2 as google_dot_cloud_dot_networksecurity_dot_v1beta1_dot_tls__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/networksecurity/v1beta1/server_tls_policy.proto\x12$google.cloud.networksecurity.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/networksecurity/v1beta1/tls.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xce\x06\n\x0fServerTlsPolicy\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x41\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12Y\n\x06labels\x18\x05 \x03(\x0b\x32\x41.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.LabelsEntryR\x06labels\x12\x1d\n\nallow_open\x18\x06 \x01(\x08R\tallowOpen\x12h\n\x12server_certificate\x18\x07 \x01(\x0b\x32\x39.google.cloud.networksecurity.v1beta1.CertificateProviderR\x11serverCertificate\x12\x61\n\x0bmtls_policy\x18\x08 \x01(\x0b\x32@.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.MTLSPolicyR\nmtlsPolicy\x1ar\n\nMTLSPolicy\x12\x64\n\x14\x63lient_validation_ca\x18\x01 \x03(\x0b\x32\x32.google.cloud.networksecurity.v1beta1.ValidationCAR\x12\x63lientValidationCa\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:\x82\x01\xea\x41\x7f\n.networksecurity.googleapis.com/ServerTlsPolicy\x12Mprojects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}\"\x9e\x01\n\x1cListServerTlsPoliciesRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\xae\x01\n\x1dListServerTlsPoliciesResponse\x12\x65\n\x13server_tls_policies\x18\x01 \x03(\x0b\x32\x35.google.cloud.networksecurity.v1beta1.ServerTlsPolicyR\x11serverTlsPolicies\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"h\n\x19GetServerTlsPolicyRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.networksecurity.googleapis.com/ServerTlsPolicyR\x04name\"\x8f\x02\n\x1c\x43reateServerTlsPolicyRequest\x12O\n\x06parent\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.networksecurity.googleapis.com/ServerTlsPolicyR\x06parent\x12\x35\n\x14server_tls_policy_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x11serverTlsPolicyId\x12g\n\x11server_tls_policy\x18\x03 \x01(\x0b\x32\x35.google.cloud.networksecurity.v1beta1.ServerTlsPolicyB\x04\xe2\x41\x01\x02R\x0fserverTlsPolicy\"\xca\x01\n\x1cUpdateServerTlsPolicyRequest\x12\x41\n\x0bupdate_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01R\nupdateMask\x12g\n\x11server_tls_policy\x18\x02 \x01(\x0b\x32\x35.google.cloud.networksecurity.v1beta1.ServerTlsPolicyB\x04\xe2\x41\x01\x02R\x0fserverTlsPolicy\"k\n\x1c\x44\x65leteServerTlsPolicyRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.networksecurity.googleapis.com/ServerTlsPolicyR\x04nameB\x8f\x02\n(com.google.cloud.networksecurity.v1beta1B\x14ServerTlsPolicyProtoP\x01ZSgoogle.golang.org/genproto/googleapis/cloud/networksecurity/v1beta1;networksecurity\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02\'Google::Cloud::NetworkSecurity::V1beta1b\x06proto3')



_SERVERTLSPOLICY = DESCRIPTOR.message_types_by_name['ServerTlsPolicy']
_SERVERTLSPOLICY_MTLSPOLICY = _SERVERTLSPOLICY.nested_types_by_name['MTLSPolicy']
_SERVERTLSPOLICY_LABELSENTRY = _SERVERTLSPOLICY.nested_types_by_name['LabelsEntry']
_LISTSERVERTLSPOLICIESREQUEST = DESCRIPTOR.message_types_by_name['ListServerTlsPoliciesRequest']
_LISTSERVERTLSPOLICIESRESPONSE = DESCRIPTOR.message_types_by_name['ListServerTlsPoliciesResponse']
_GETSERVERTLSPOLICYREQUEST = DESCRIPTOR.message_types_by_name['GetServerTlsPolicyRequest']
_CREATESERVERTLSPOLICYREQUEST = DESCRIPTOR.message_types_by_name['CreateServerTlsPolicyRequest']
_UPDATESERVERTLSPOLICYREQUEST = DESCRIPTOR.message_types_by_name['UpdateServerTlsPolicyRequest']
_DELETESERVERTLSPOLICYREQUEST = DESCRIPTOR.message_types_by_name['DeleteServerTlsPolicyRequest']
ServerTlsPolicy = _reflection.GeneratedProtocolMessageType('ServerTlsPolicy', (_message.Message,), {

  'MTLSPolicy' : _reflection.GeneratedProtocolMessageType('MTLSPolicy', (_message.Message,), {
    'DESCRIPTOR' : _SERVERTLSPOLICY_MTLSPOLICY,
    '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ServerTlsPolicy.MTLSPolicy)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVERTLSPOLICY_LABELSENTRY,
    '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ServerTlsPolicy.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SERVERTLSPOLICY,
  '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ServerTlsPolicy)
  })
_sym_db.RegisterMessage(ServerTlsPolicy)
_sym_db.RegisterMessage(ServerTlsPolicy.MTLSPolicy)
_sym_db.RegisterMessage(ServerTlsPolicy.LabelsEntry)

ListServerTlsPoliciesRequest = _reflection.GeneratedProtocolMessageType('ListServerTlsPoliciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVERTLSPOLICIESREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ListServerTlsPoliciesRequest)
  })
_sym_db.RegisterMessage(ListServerTlsPoliciesRequest)

ListServerTlsPoliciesResponse = _reflection.GeneratedProtocolMessageType('ListServerTlsPoliciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVERTLSPOLICIESRESPONSE,
  '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ListServerTlsPoliciesResponse)
  })
_sym_db.RegisterMessage(ListServerTlsPoliciesResponse)

GetServerTlsPolicyRequest = _reflection.GeneratedProtocolMessageType('GetServerTlsPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERTLSPOLICYREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.GetServerTlsPolicyRequest)
  })
_sym_db.RegisterMessage(GetServerTlsPolicyRequest)

CreateServerTlsPolicyRequest = _reflection.GeneratedProtocolMessageType('CreateServerTlsPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVERTLSPOLICYREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.CreateServerTlsPolicyRequest)
  })
_sym_db.RegisterMessage(CreateServerTlsPolicyRequest)

UpdateServerTlsPolicyRequest = _reflection.GeneratedProtocolMessageType('UpdateServerTlsPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVERTLSPOLICYREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.UpdateServerTlsPolicyRequest)
  })
_sym_db.RegisterMessage(UpdateServerTlsPolicyRequest)

DeleteServerTlsPolicyRequest = _reflection.GeneratedProtocolMessageType('DeleteServerTlsPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVERTLSPOLICYREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.DeleteServerTlsPolicyRequest)
  })
_sym_db.RegisterMessage(DeleteServerTlsPolicyRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.google.cloud.networksecurity.v1beta1B\024ServerTlsPolicyProtoP\001ZSgoogle.golang.org/genproto/googleapis/cloud/networksecurity/v1beta1;networksecurity\252\002$Google.Cloud.NetworkSecurity.V1Beta1\312\002$Google\\Cloud\\NetworkSecurity\\V1beta1\352\002\'Google::Cloud::NetworkSecurity::V1beta1'
  _SERVERTLSPOLICY_LABELSENTRY._options = None
  _SERVERTLSPOLICY_LABELSENTRY._serialized_options = b'8\001'
  _SERVERTLSPOLICY.fields_by_name['name']._options = None
  _SERVERTLSPOLICY.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _SERVERTLSPOLICY.fields_by_name['create_time']._options = None
  _SERVERTLSPOLICY.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _SERVERTLSPOLICY.fields_by_name['update_time']._options = None
  _SERVERTLSPOLICY.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _SERVERTLSPOLICY._options = None
  _SERVERTLSPOLICY._serialized_options = b'\352A\177\n.networksecurity.googleapis.com/ServerTlsPolicy\022Mprojects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}'
  _LISTSERVERTLSPOLICIESREQUEST.fields_by_name['parent']._options = None
  _LISTSERVERTLSPOLICIESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _GETSERVERTLSPOLICYREQUEST.fields_by_name['name']._options = None
  _GETSERVERTLSPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A0\n.networksecurity.googleapis.com/ServerTlsPolicy'
  _CREATESERVERTLSPOLICYREQUEST.fields_by_name['parent']._options = None
  _CREATESERVERTLSPOLICYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A0\n.networksecurity.googleapis.com/ServerTlsPolicy'
  _CREATESERVERTLSPOLICYREQUEST.fields_by_name['server_tls_policy_id']._options = None
  _CREATESERVERTLSPOLICYREQUEST.fields_by_name['server_tls_policy_id']._serialized_options = b'\342A\001\002'
  _CREATESERVERTLSPOLICYREQUEST.fields_by_name['server_tls_policy']._options = None
  _CREATESERVERTLSPOLICYREQUEST.fields_by_name['server_tls_policy']._serialized_options = b'\342A\001\002'
  _UPDATESERVERTLSPOLICYREQUEST.fields_by_name['update_mask']._options = None
  _UPDATESERVERTLSPOLICYREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _UPDATESERVERTLSPOLICYREQUEST.fields_by_name['server_tls_policy']._options = None
  _UPDATESERVERTLSPOLICYREQUEST.fields_by_name['server_tls_policy']._serialized_options = b'\342A\001\002'
  _DELETESERVERTLSPOLICYREQUEST.fields_by_name['name']._options = None
  _DELETESERVERTLSPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A0\n.networksecurity.googleapis.com/ServerTlsPolicy'
  _SERVERTLSPOLICY._serialized_start=308
  _SERVERTLSPOLICY._serialized_end=1154
  _SERVERTLSPOLICY_MTLSPOLICY._serialized_start=848
  _SERVERTLSPOLICY_MTLSPOLICY._serialized_end=962
  _SERVERTLSPOLICY_LABELSENTRY._serialized_start=964
  _SERVERTLSPOLICY_LABELSENTRY._serialized_end=1021
  _LISTSERVERTLSPOLICIESREQUEST._serialized_start=1157
  _LISTSERVERTLSPOLICIESREQUEST._serialized_end=1315
  _LISTSERVERTLSPOLICIESRESPONSE._serialized_start=1318
  _LISTSERVERTLSPOLICIESRESPONSE._serialized_end=1492
  _GETSERVERTLSPOLICYREQUEST._serialized_start=1494
  _GETSERVERTLSPOLICYREQUEST._serialized_end=1598
  _CREATESERVERTLSPOLICYREQUEST._serialized_start=1601
  _CREATESERVERTLSPOLICYREQUEST._serialized_end=1872
  _UPDATESERVERTLSPOLICYREQUEST._serialized_start=1875
  _UPDATESERVERTLSPOLICYREQUEST._serialized_end=2077
  _DELETESERVERTLSPOLICYREQUEST._serialized_start=2079
  _DELETESERVERTLSPOLICYREQUEST._serialized_end=2186
# @@protoc_insertion_point(module_scope)
