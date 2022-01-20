# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/networksecurity/v1beta1/client_tls_policy.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/networksecurity/v1beta1/client_tls_policy.proto\x12$google.cloud.networksecurity.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/networksecurity/v1beta1/tls.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xee\x05\n\x0f\x43lientTlsPolicy\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12&\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\x0b\x64\x65scription\x12\x41\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12_\n\x06labels\x18\x05 \x03(\x0b\x32\x41.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.LabelsEntryB\x04\xe2\x41\x01\x01R\x06labels\x12\x16\n\x03sni\x18\x06 \x01(\tB\x04\xe2\x41\x01\x01R\x03sni\x12n\n\x12\x63lient_certificate\x18\x07 \x01(\x0b\x32\x39.google.cloud.networksecurity.v1beta1.CertificateProviderB\x04\xe2\x41\x01\x01R\x11\x63lientCertificate\x12j\n\x14server_validation_ca\x18\x08 \x03(\x0b\x32\x32.google.cloud.networksecurity.v1beta1.ValidationCAB\x04\xe2\x41\x01\x01R\x12serverValidationCa\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:\x82\x01\xea\x41\x7f\n.networksecurity.googleapis.com/ClientTlsPolicy\x12Mprojects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}\"\x9e\x01\n\x1cListClientTlsPoliciesRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\xae\x01\n\x1dListClientTlsPoliciesResponse\x12\x65\n\x13\x63lient_tls_policies\x18\x01 \x03(\x0b\x32\x35.google.cloud.networksecurity.v1beta1.ClientTlsPolicyR\x11\x63lientTlsPolicies\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"h\n\x19GetClientTlsPolicyRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.networksecurity.googleapis.com/ClientTlsPolicyR\x04name\"\x8f\x02\n\x1c\x43reateClientTlsPolicyRequest\x12O\n\x06parent\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.networksecurity.googleapis.com/ClientTlsPolicyR\x06parent\x12\x35\n\x14\x63lient_tls_policy_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x11\x63lientTlsPolicyId\x12g\n\x11\x63lient_tls_policy\x18\x03 \x01(\x0b\x32\x35.google.cloud.networksecurity.v1beta1.ClientTlsPolicyB\x04\xe2\x41\x01\x02R\x0f\x63lientTlsPolicy\"\xca\x01\n\x1cUpdateClientTlsPolicyRequest\x12\x41\n\x0bupdate_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01R\nupdateMask\x12g\n\x11\x63lient_tls_policy\x18\x02 \x01(\x0b\x32\x35.google.cloud.networksecurity.v1beta1.ClientTlsPolicyB\x04\xe2\x41\x01\x02R\x0f\x63lientTlsPolicy\"k\n\x1c\x44\x65leteClientTlsPolicyRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.networksecurity.googleapis.com/ClientTlsPolicyR\x04nameB\x8f\x02\n(com.google.cloud.networksecurity.v1beta1B\x14\x43lientTlsPolicyProtoP\x01ZSgoogle.golang.org/genproto/googleapis/cloud/networksecurity/v1beta1;networksecurity\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02\'Google::Cloud::NetworkSecurity::V1beta1b\x06proto3')



_CLIENTTLSPOLICY = DESCRIPTOR.message_types_by_name['ClientTlsPolicy']
_CLIENTTLSPOLICY_LABELSENTRY = _CLIENTTLSPOLICY.nested_types_by_name['LabelsEntry']
_LISTCLIENTTLSPOLICIESREQUEST = DESCRIPTOR.message_types_by_name['ListClientTlsPoliciesRequest']
_LISTCLIENTTLSPOLICIESRESPONSE = DESCRIPTOR.message_types_by_name['ListClientTlsPoliciesResponse']
_GETCLIENTTLSPOLICYREQUEST = DESCRIPTOR.message_types_by_name['GetClientTlsPolicyRequest']
_CREATECLIENTTLSPOLICYREQUEST = DESCRIPTOR.message_types_by_name['CreateClientTlsPolicyRequest']
_UPDATECLIENTTLSPOLICYREQUEST = DESCRIPTOR.message_types_by_name['UpdateClientTlsPolicyRequest']
_DELETECLIENTTLSPOLICYREQUEST = DESCRIPTOR.message_types_by_name['DeleteClientTlsPolicyRequest']
ClientTlsPolicy = _reflection.GeneratedProtocolMessageType('ClientTlsPolicy', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLIENTTLSPOLICY_LABELSENTRY,
    '__module__' : 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ClientTlsPolicy.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CLIENTTLSPOLICY,
  '__module__' : 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ClientTlsPolicy)
  })
_sym_db.RegisterMessage(ClientTlsPolicy)
_sym_db.RegisterMessage(ClientTlsPolicy.LabelsEntry)

ListClientTlsPoliciesRequest = _reflection.GeneratedProtocolMessageType('ListClientTlsPoliciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCLIENTTLSPOLICIESREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ListClientTlsPoliciesRequest)
  })
_sym_db.RegisterMessage(ListClientTlsPoliciesRequest)

ListClientTlsPoliciesResponse = _reflection.GeneratedProtocolMessageType('ListClientTlsPoliciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCLIENTTLSPOLICIESRESPONSE,
  '__module__' : 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.ListClientTlsPoliciesResponse)
  })
_sym_db.RegisterMessage(ListClientTlsPoliciesResponse)

GetClientTlsPolicyRequest = _reflection.GeneratedProtocolMessageType('GetClientTlsPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTTLSPOLICYREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.GetClientTlsPolicyRequest)
  })
_sym_db.RegisterMessage(GetClientTlsPolicyRequest)

CreateClientTlsPolicyRequest = _reflection.GeneratedProtocolMessageType('CreateClientTlsPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECLIENTTLSPOLICYREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.CreateClientTlsPolicyRequest)
  })
_sym_db.RegisterMessage(CreateClientTlsPolicyRequest)

UpdateClientTlsPolicyRequest = _reflection.GeneratedProtocolMessageType('UpdateClientTlsPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECLIENTTLSPOLICYREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.UpdateClientTlsPolicyRequest)
  })
_sym_db.RegisterMessage(UpdateClientTlsPolicyRequest)

DeleteClientTlsPolicyRequest = _reflection.GeneratedProtocolMessageType('DeleteClientTlsPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECLIENTTLSPOLICYREQUEST,
  '__module__' : 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networksecurity.v1beta1.DeleteClientTlsPolicyRequest)
  })
_sym_db.RegisterMessage(DeleteClientTlsPolicyRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.google.cloud.networksecurity.v1beta1B\024ClientTlsPolicyProtoP\001ZSgoogle.golang.org/genproto/googleapis/cloud/networksecurity/v1beta1;networksecurity\252\002$Google.Cloud.NetworkSecurity.V1Beta1\312\002$Google\\Cloud\\NetworkSecurity\\V1beta1\352\002\'Google::Cloud::NetworkSecurity::V1beta1'
  _CLIENTTLSPOLICY_LABELSENTRY._options = None
  _CLIENTTLSPOLICY_LABELSENTRY._serialized_options = b'8\001'
  _CLIENTTLSPOLICY.fields_by_name['name']._options = None
  _CLIENTTLSPOLICY.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _CLIENTTLSPOLICY.fields_by_name['description']._options = None
  _CLIENTTLSPOLICY.fields_by_name['description']._serialized_options = b'\342A\001\001'
  _CLIENTTLSPOLICY.fields_by_name['create_time']._options = None
  _CLIENTTLSPOLICY.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _CLIENTTLSPOLICY.fields_by_name['update_time']._options = None
  _CLIENTTLSPOLICY.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _CLIENTTLSPOLICY.fields_by_name['labels']._options = None
  _CLIENTTLSPOLICY.fields_by_name['labels']._serialized_options = b'\342A\001\001'
  _CLIENTTLSPOLICY.fields_by_name['sni']._options = None
  _CLIENTTLSPOLICY.fields_by_name['sni']._serialized_options = b'\342A\001\001'
  _CLIENTTLSPOLICY.fields_by_name['client_certificate']._options = None
  _CLIENTTLSPOLICY.fields_by_name['client_certificate']._serialized_options = b'\342A\001\001'
  _CLIENTTLSPOLICY.fields_by_name['server_validation_ca']._options = None
  _CLIENTTLSPOLICY.fields_by_name['server_validation_ca']._serialized_options = b'\342A\001\001'
  _CLIENTTLSPOLICY._options = None
  _CLIENTTLSPOLICY._serialized_options = b'\352A\177\n.networksecurity.googleapis.com/ClientTlsPolicy\022Mprojects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}'
  _LISTCLIENTTLSPOLICIESREQUEST.fields_by_name['parent']._options = None
  _LISTCLIENTTLSPOLICIESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _GETCLIENTTLSPOLICYREQUEST.fields_by_name['name']._options = None
  _GETCLIENTTLSPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A0\n.networksecurity.googleapis.com/ClientTlsPolicy'
  _CREATECLIENTTLSPOLICYREQUEST.fields_by_name['parent']._options = None
  _CREATECLIENTTLSPOLICYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A0\n.networksecurity.googleapis.com/ClientTlsPolicy'
  _CREATECLIENTTLSPOLICYREQUEST.fields_by_name['client_tls_policy_id']._options = None
  _CREATECLIENTTLSPOLICYREQUEST.fields_by_name['client_tls_policy_id']._serialized_options = b'\342A\001\002'
  _CREATECLIENTTLSPOLICYREQUEST.fields_by_name['client_tls_policy']._options = None
  _CREATECLIENTTLSPOLICYREQUEST.fields_by_name['client_tls_policy']._serialized_options = b'\342A\001\002'
  _UPDATECLIENTTLSPOLICYREQUEST.fields_by_name['update_mask']._options = None
  _UPDATECLIENTTLSPOLICYREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _UPDATECLIENTTLSPOLICYREQUEST.fields_by_name['client_tls_policy']._options = None
  _UPDATECLIENTTLSPOLICYREQUEST.fields_by_name['client_tls_policy']._serialized_options = b'\342A\001\002'
  _DELETECLIENTTLSPOLICYREQUEST.fields_by_name['name']._options = None
  _DELETECLIENTTLSPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A0\n.networksecurity.googleapis.com/ClientTlsPolicy'
  _CLIENTTLSPOLICY._serialized_start=308
  _CLIENTTLSPOLICY._serialized_end=1058
  _CLIENTTLSPOLICY_LABELSENTRY._serialized_start=868
  _CLIENTTLSPOLICY_LABELSENTRY._serialized_end=925
  _LISTCLIENTTLSPOLICIESREQUEST._serialized_start=1061
  _LISTCLIENTTLSPOLICIESREQUEST._serialized_end=1219
  _LISTCLIENTTLSPOLICIESRESPONSE._serialized_start=1222
  _LISTCLIENTTLSPOLICIESRESPONSE._serialized_end=1396
  _GETCLIENTTLSPOLICYREQUEST._serialized_start=1398
  _GETCLIENTTLSPOLICYREQUEST._serialized_end=1502
  _CREATECLIENTTLSPOLICYREQUEST._serialized_start=1505
  _CREATECLIENTTLSPOLICYREQUEST._serialized_end=1776
  _UPDATECLIENTTLSPOLICYREQUEST._serialized_start=1779
  _UPDATECLIENTTLSPOLICYREQUEST._serialized_end=1981
  _DELETECLIENTTLSPOLICYREQUEST._serialized_start=1983
  _DELETECLIENTTLSPOLICYREQUEST._serialized_end=2090
# @@protoc_insertion_point(module_scope)
