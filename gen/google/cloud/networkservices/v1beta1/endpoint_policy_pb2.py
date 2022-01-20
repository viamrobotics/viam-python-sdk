# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/networkservices/v1beta1/endpoint_policy.proto
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
from google.cloud.networkservices.v1beta1 import common_pb2 as google_dot_cloud_dot_networkservices_dot_v1beta1_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/networkservices/v1beta1/endpoint_policy.proto\x12$google.cloud.networkservices.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x31google/cloud/networkservices/v1beta1/common.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xcd\t\n\x0e\x45ndpointPolicy\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\x41\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12^\n\x06labels\x18\x04 \x03(\x0b\x32@.google.cloud.networkservices.v1beta1.EndpointPolicy.LabelsEntryB\x04\xe2\x41\x01\x01R\x06labels\x12\x61\n\x04type\x18\x05 \x01(\x0e\x32G.google.cloud.networkservices.v1beta1.EndpointPolicy.EndpointPolicyTypeB\x04\xe2\x41\x01\x02R\x04type\x12n\n\x14\x61uthorization_policy\x18\x07 \x01(\tB;\xe2\x41\x01\x01\xfa\x41\x34\n2networksecurity.googleapis.com/AuthorizationPolicyR\x13\x61uthorizationPolicy\x12\x66\n\x10\x65ndpoint_matcher\x18\t \x01(\x0b\x32\x35.google.cloud.networkservices.v1beta1.EndpointMatcherB\x04\xe2\x41\x01\x02R\x0f\x65ndpointMatcher\x12s\n\x15traffic_port_selector\x18\n \x01(\x0b\x32\x39.google.cloud.networkservices.v1beta1.TrafficPortSelectorB\x04\xe2\x41\x01\x01R\x13trafficPortSelector\x12&\n\x0b\x64\x65scription\x18\x0b \x01(\tB\x04\xe2\x41\x01\x01R\x0b\x64\x65scription\x12\x63\n\x11server_tls_policy\x18\x0c \x01(\tB7\xe2\x41\x01\x01\xfa\x41\x30\n.networksecurity.googleapis.com/ServerTlsPolicyR\x0fserverTlsPolicy\x12\x63\n\x11\x63lient_tls_policy\x18\r \x01(\tB7\xe2\x41\x01\x01\xfa\x41\x30\n.networksecurity.googleapis.com/ClientTlsPolicyR\x0f\x63lientTlsPolicy\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"^\n\x12\x45ndpointPolicyType\x12$\n ENDPOINT_POLICY_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rSIDECAR_PROXY\x10\x01\x12\x0f\n\x0bGRPC_SERVER\x10\x02:~\xea\x41{\n-networkservices.googleapis.com/EndpointPolicy\x12Jprojects/{project}/locations/{location}/endpointPolicies/{endpoint_policy}\"\xa9\x01\n\x1bListEndpointPoliciesRequest\x12N\n\x06parent\x18\x01 \x01(\tB6\xe2\x41\x01\x02\xfa\x41/\x12-networkservices.googleapis.com/EndpointPolicyR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\xa9\x01\n\x1cListEndpointPoliciesResponse\x12\x61\n\x11\x65ndpoint_policies\x18\x01 \x03(\x0b\x32\x34.google.cloud.networkservices.v1beta1.EndpointPolicyR\x10\x65ndpointPolicies\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"f\n\x18GetEndpointPolicyRequest\x12J\n\x04name\x18\x01 \x01(\tB6\xe2\x41\x01\x02\xfa\x41/\n-networkservices.googleapis.com/EndpointPolicyR\x04name\"\x86\x02\n\x1b\x43reateEndpointPolicyRequest\x12N\n\x06parent\x18\x01 \x01(\tB6\xe2\x41\x01\x02\xfa\x41/\x12-networkservices.googleapis.com/EndpointPolicyR\x06parent\x12\x32\n\x12\x65ndpoint_policy_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x10\x65ndpointPolicyId\x12\x63\n\x0f\x65ndpoint_policy\x18\x03 \x01(\x0b\x32\x34.google.cloud.networkservices.v1beta1.EndpointPolicyB\x04\xe2\x41\x01\x02R\x0e\x65ndpointPolicy\"\xc5\x01\n\x1bUpdateEndpointPolicyRequest\x12\x41\n\x0bupdate_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01R\nupdateMask\x12\x63\n\x0f\x65ndpoint_policy\x18\x02 \x01(\x0b\x32\x34.google.cloud.networkservices.v1beta1.EndpointPolicyB\x04\xe2\x41\x01\x02R\x0e\x65ndpointPolicy\"i\n\x1b\x44\x65leteEndpointPolicyRequest\x12J\n\x04name\x18\x01 \x01(\tB6\xe2\x41\x01\x02\xfa\x41/\n-networkservices.googleapis.com/EndpointPolicyR\x04nameB\xa0\x05\n(com.google.cloud.networkservices.v1beta1B\x13\x45ndpointPolicyProtoP\x01ZSgoogle.golang.org/genproto/googleapis/cloud/networkservices/v1beta1;networkservices\xaa\x02$Google.Cloud.NetworkServices.V1Beta1\xca\x02$Google\\Cloud\\NetworkServices\\V1beta1\xea\x02\'Google::Cloud::NetworkServices::V1beta1\xea\x41\x8a\x01\n2networksecurity.googleapis.com/AuthorizationPolicy\x12Tprojects/{project}/locations/{location}/authorizationPolicies/{authorization_policy}\xea\x41\x7f\n.networksecurity.googleapis.com/ServerTlsPolicy\x12Mprojects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}\xea\x41\x7f\n.networksecurity.googleapis.com/ClientTlsPolicy\x12Mprojects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}b\x06proto3')



_ENDPOINTPOLICY = DESCRIPTOR.message_types_by_name['EndpointPolicy']
_ENDPOINTPOLICY_LABELSENTRY = _ENDPOINTPOLICY.nested_types_by_name['LabelsEntry']
_LISTENDPOINTPOLICIESREQUEST = DESCRIPTOR.message_types_by_name['ListEndpointPoliciesRequest']
_LISTENDPOINTPOLICIESRESPONSE = DESCRIPTOR.message_types_by_name['ListEndpointPoliciesResponse']
_GETENDPOINTPOLICYREQUEST = DESCRIPTOR.message_types_by_name['GetEndpointPolicyRequest']
_CREATEENDPOINTPOLICYREQUEST = DESCRIPTOR.message_types_by_name['CreateEndpointPolicyRequest']
_UPDATEENDPOINTPOLICYREQUEST = DESCRIPTOR.message_types_by_name['UpdateEndpointPolicyRequest']
_DELETEENDPOINTPOLICYREQUEST = DESCRIPTOR.message_types_by_name['DeleteEndpointPolicyRequest']
_ENDPOINTPOLICY_ENDPOINTPOLICYTYPE = _ENDPOINTPOLICY.enum_types_by_name['EndpointPolicyType']
EndpointPolicy = _reflection.GeneratedProtocolMessageType('EndpointPolicy', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENDPOINTPOLICY_LABELSENTRY,
    '__module__' : 'google.cloud.networkservices.v1beta1.endpoint_policy_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.networkservices.v1beta1.EndpointPolicy.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _ENDPOINTPOLICY,
  '__module__' : 'google.cloud.networkservices.v1beta1.endpoint_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkservices.v1beta1.EndpointPolicy)
  })
_sym_db.RegisterMessage(EndpointPolicy)
_sym_db.RegisterMessage(EndpointPolicy.LabelsEntry)

ListEndpointPoliciesRequest = _reflection.GeneratedProtocolMessageType('ListEndpointPoliciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTENDPOINTPOLICIESREQUEST,
  '__module__' : 'google.cloud.networkservices.v1beta1.endpoint_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkservices.v1beta1.ListEndpointPoliciesRequest)
  })
_sym_db.RegisterMessage(ListEndpointPoliciesRequest)

ListEndpointPoliciesResponse = _reflection.GeneratedProtocolMessageType('ListEndpointPoliciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTENDPOINTPOLICIESRESPONSE,
  '__module__' : 'google.cloud.networkservices.v1beta1.endpoint_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkservices.v1beta1.ListEndpointPoliciesResponse)
  })
_sym_db.RegisterMessage(ListEndpointPoliciesResponse)

GetEndpointPolicyRequest = _reflection.GeneratedProtocolMessageType('GetEndpointPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETENDPOINTPOLICYREQUEST,
  '__module__' : 'google.cloud.networkservices.v1beta1.endpoint_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkservices.v1beta1.GetEndpointPolicyRequest)
  })
_sym_db.RegisterMessage(GetEndpointPolicyRequest)

CreateEndpointPolicyRequest = _reflection.GeneratedProtocolMessageType('CreateEndpointPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENDPOINTPOLICYREQUEST,
  '__module__' : 'google.cloud.networkservices.v1beta1.endpoint_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkservices.v1beta1.CreateEndpointPolicyRequest)
  })
_sym_db.RegisterMessage(CreateEndpointPolicyRequest)

UpdateEndpointPolicyRequest = _reflection.GeneratedProtocolMessageType('UpdateEndpointPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENDPOINTPOLICYREQUEST,
  '__module__' : 'google.cloud.networkservices.v1beta1.endpoint_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkservices.v1beta1.UpdateEndpointPolicyRequest)
  })
_sym_db.RegisterMessage(UpdateEndpointPolicyRequest)

DeleteEndpointPolicyRequest = _reflection.GeneratedProtocolMessageType('DeleteEndpointPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENDPOINTPOLICYREQUEST,
  '__module__' : 'google.cloud.networkservices.v1beta1.endpoint_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkservices.v1beta1.DeleteEndpointPolicyRequest)
  })
_sym_db.RegisterMessage(DeleteEndpointPolicyRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.google.cloud.networkservices.v1beta1B\023EndpointPolicyProtoP\001ZSgoogle.golang.org/genproto/googleapis/cloud/networkservices/v1beta1;networkservices\252\002$Google.Cloud.NetworkServices.V1Beta1\312\002$Google\\Cloud\\NetworkServices\\V1beta1\352\002\'Google::Cloud::NetworkServices::V1beta1\352A\212\001\n2networksecurity.googleapis.com/AuthorizationPolicy\022Tprojects/{project}/locations/{location}/authorizationPolicies/{authorization_policy}\352A\177\n.networksecurity.googleapis.com/ServerTlsPolicy\022Mprojects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}\352A\177\n.networksecurity.googleapis.com/ClientTlsPolicy\022Mprojects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}'
  _ENDPOINTPOLICY_LABELSENTRY._options = None
  _ENDPOINTPOLICY_LABELSENTRY._serialized_options = b'8\001'
  _ENDPOINTPOLICY.fields_by_name['name']._options = None
  _ENDPOINTPOLICY.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _ENDPOINTPOLICY.fields_by_name['create_time']._options = None
  _ENDPOINTPOLICY.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _ENDPOINTPOLICY.fields_by_name['update_time']._options = None
  _ENDPOINTPOLICY.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _ENDPOINTPOLICY.fields_by_name['labels']._options = None
  _ENDPOINTPOLICY.fields_by_name['labels']._serialized_options = b'\342A\001\001'
  _ENDPOINTPOLICY.fields_by_name['type']._options = None
  _ENDPOINTPOLICY.fields_by_name['type']._serialized_options = b'\342A\001\002'
  _ENDPOINTPOLICY.fields_by_name['authorization_policy']._options = None
  _ENDPOINTPOLICY.fields_by_name['authorization_policy']._serialized_options = b'\342A\001\001\372A4\n2networksecurity.googleapis.com/AuthorizationPolicy'
  _ENDPOINTPOLICY.fields_by_name['endpoint_matcher']._options = None
  _ENDPOINTPOLICY.fields_by_name['endpoint_matcher']._serialized_options = b'\342A\001\002'
  _ENDPOINTPOLICY.fields_by_name['traffic_port_selector']._options = None
  _ENDPOINTPOLICY.fields_by_name['traffic_port_selector']._serialized_options = b'\342A\001\001'
  _ENDPOINTPOLICY.fields_by_name['description']._options = None
  _ENDPOINTPOLICY.fields_by_name['description']._serialized_options = b'\342A\001\001'
  _ENDPOINTPOLICY.fields_by_name['server_tls_policy']._options = None
  _ENDPOINTPOLICY.fields_by_name['server_tls_policy']._serialized_options = b'\342A\001\001\372A0\n.networksecurity.googleapis.com/ServerTlsPolicy'
  _ENDPOINTPOLICY.fields_by_name['client_tls_policy']._options = None
  _ENDPOINTPOLICY.fields_by_name['client_tls_policy']._serialized_options = b'\342A\001\001\372A0\n.networksecurity.googleapis.com/ClientTlsPolicy'
  _ENDPOINTPOLICY._options = None
  _ENDPOINTPOLICY._serialized_options = b'\352A{\n-networkservices.googleapis.com/EndpointPolicy\022Jprojects/{project}/locations/{location}/endpointPolicies/{endpoint_policy}'
  _LISTENDPOINTPOLICIESREQUEST.fields_by_name['parent']._options = None
  _LISTENDPOINTPOLICIESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A/\022-networkservices.googleapis.com/EndpointPolicy'
  _GETENDPOINTPOLICYREQUEST.fields_by_name['name']._options = None
  _GETENDPOINTPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A/\n-networkservices.googleapis.com/EndpointPolicy'
  _CREATEENDPOINTPOLICYREQUEST.fields_by_name['parent']._options = None
  _CREATEENDPOINTPOLICYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A/\022-networkservices.googleapis.com/EndpointPolicy'
  _CREATEENDPOINTPOLICYREQUEST.fields_by_name['endpoint_policy_id']._options = None
  _CREATEENDPOINTPOLICYREQUEST.fields_by_name['endpoint_policy_id']._serialized_options = b'\342A\001\002'
  _CREATEENDPOINTPOLICYREQUEST.fields_by_name['endpoint_policy']._options = None
  _CREATEENDPOINTPOLICYREQUEST.fields_by_name['endpoint_policy']._serialized_options = b'\342A\001\002'
  _UPDATEENDPOINTPOLICYREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEENDPOINTPOLICYREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _UPDATEENDPOINTPOLICYREQUEST.fields_by_name['endpoint_policy']._options = None
  _UPDATEENDPOINTPOLICYREQUEST.fields_by_name['endpoint_policy']._serialized_options = b'\342A\001\002'
  _DELETEENDPOINTPOLICYREQUEST.fields_by_name['name']._options = None
  _DELETEENDPOINTPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A/\n-networkservices.googleapis.com/EndpointPolicy'
  _ENDPOINTPOLICY._serialized_start=309
  _ENDPOINTPOLICY._serialized_end=1538
  _ENDPOINTPOLICY_LABELSENTRY._serialized_start=1257
  _ENDPOINTPOLICY_LABELSENTRY._serialized_end=1314
  _ENDPOINTPOLICY_ENDPOINTPOLICYTYPE._serialized_start=1316
  _ENDPOINTPOLICY_ENDPOINTPOLICYTYPE._serialized_end=1410
  _LISTENDPOINTPOLICIESREQUEST._serialized_start=1541
  _LISTENDPOINTPOLICIESREQUEST._serialized_end=1710
  _LISTENDPOINTPOLICIESRESPONSE._serialized_start=1713
  _LISTENDPOINTPOLICIESRESPONSE._serialized_end=1882
  _GETENDPOINTPOLICYREQUEST._serialized_start=1884
  _GETENDPOINTPOLICYREQUEST._serialized_end=1986
  _CREATEENDPOINTPOLICYREQUEST._serialized_start=1989
  _CREATEENDPOINTPOLICYREQUEST._serialized_end=2251
  _UPDATEENDPOINTPOLICYREQUEST._serialized_start=2254
  _UPDATEENDPOINTPOLICYREQUEST._serialized_end=2451
  _DELETEENDPOINTPOLICYREQUEST._serialized_start=2453
  _DELETEENDPOINTPOLICYREQUEST._serialized_end=2558
# @@protoc_insertion_point(module_scope)
