# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/binaryauthorization/v1beta1/service.proto
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
from google.cloud.binaryauthorization.v1beta1 import resources_pb2 as google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/binaryauthorization/v1beta1/service.proto\x12(google.cloud.binaryauthorization.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x38google/cloud/binaryauthorization/v1beta1/resources.proto\x1a\x1bgoogle/protobuf/empty.proto\"Z\n\x10GetPolicyRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)binaryauthorization.googleapis.com/PolicyR\x04name\"e\n\x13UpdatePolicyRequest\x12N\n\x06policy\x18\x01 \x01(\x0b\x32\x30.google.cloud.binaryauthorization.v1beta1.PolicyB\x04\xe2\x41\x01\x02R\x06policy\"\xe2\x01\n\x15\x43reateAttestorRequest\x12L\n\x06parent\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+cloudresourcemanager.googleapis.com/ProjectR\x06parent\x12%\n\x0b\x61ttestor_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\nattestorId\x12T\n\x08\x61ttestor\x18\x03 \x01(\x0b\x32\x32.google.cloud.binaryauthorization.v1beta1.AttestorB\x04\xe2\x41\x01\x02R\x08\x61ttestor\"^\n\x12GetAttestorRequest\x12H\n\x04name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+binaryauthorization.googleapis.com/AttestorR\x04name\"m\n\x15UpdateAttestorRequest\x12T\n\x08\x61ttestor\x18\x01 \x01(\x0b\x32\x32.google.cloud.binaryauthorization.v1beta1.AttestorB\x04\xe2\x41\x01\x02R\x08\x61ttestor\"\xa0\x01\n\x14ListAttestorsRequest\x12L\n\x06parent\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+cloudresourcemanager.googleapis.com/ProjectR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x91\x01\n\x15ListAttestorsResponse\x12P\n\tattestors\x18\x01 \x03(\x0b\x32\x32.google.cloud.binaryauthorization.v1beta1.AttestorR\tattestors\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"a\n\x15\x44\x65leteAttestorRequest\x12H\n\x04name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+binaryauthorization.googleapis.com/AttestorR\x04name\"`\n\x16GetSystemPolicyRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)binaryauthorization.googleapis.com/PolicyR\x04name2\xcb\x0b\n BinauthzManagementServiceV1Beta1\x12\xab\x01\n\tGetPolicy\x12:.google.cloud.binaryauthorization.v1beta1.GetPolicyRequest\x1a\x30.google.cloud.binaryauthorization.v1beta1.Policy\"0\xda\x41\x04name\x82\xd3\xe4\x93\x02#\x12!/v1beta1/{name=projects/*/policy}\x12\xc2\x01\n\x0cUpdatePolicy\x12=.google.cloud.binaryauthorization.v1beta1.UpdatePolicyRequest\x1a\x30.google.cloud.binaryauthorization.v1beta1.Policy\"A\xda\x41\x06policy\x82\xd3\xe4\x93\x02\x32\x1a(/v1beta1/{policy.name=projects/*/policy}:\x06policy\x12\xdd\x01\n\x0e\x43reateAttestor\x12?.google.cloud.binaryauthorization.v1beta1.CreateAttestorRequest\x1a\x32.google.cloud.binaryauthorization.v1beta1.Attestor\"V\xda\x41\x1bparent,attestor_id,attestor\x82\xd3\xe4\x93\x02\x32\"&/v1beta1/{parent=projects/*}/attestors:\x08\x61ttestor\x12\xb6\x01\n\x0bGetAttestor\x12<.google.cloud.binaryauthorization.v1beta1.GetAttestorRequest\x1a\x32.google.cloud.binaryauthorization.v1beta1.Attestor\"5\xda\x41\x04name\x82\xd3\xe4\x93\x02(\x12&/v1beta1/{name=projects/*/attestors/*}\x12\xd3\x01\n\x0eUpdateAttestor\x12?.google.cloud.binaryauthorization.v1beta1.UpdateAttestorRequest\x1a\x32.google.cloud.binaryauthorization.v1beta1.Attestor\"L\xda\x41\x08\x61ttestor\x82\xd3\xe4\x93\x02;\x1a//v1beta1/{attestor.name=projects/*/attestors/*}:\x08\x61ttestor\x12\xc9\x01\n\rListAttestors\x12>.google.cloud.binaryauthorization.v1beta1.ListAttestorsRequest\x1a?.google.cloud.binaryauthorization.v1beta1.ListAttestorsResponse\"7\xda\x41\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1beta1/{parent=projects/*}/attestors\x12\xa0\x01\n\x0e\x44\x65leteAttestor\x12?.google.cloud.binaryauthorization.v1beta1.DeleteAttestorRequest\x1a\x16.google.protobuf.Empty\"5\xda\x41\x04name\x82\xd3\xe4\x93\x02(*&/v1beta1/{name=projects/*/attestors/*}\x1aV\xca\x41\"binaryauthorization.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platform2\xa8\x02\n\x13SystemPolicyV1Beta1\x12\xb8\x01\n\x0fGetSystemPolicy\x12@.google.cloud.binaryauthorization.v1beta1.GetSystemPolicyRequest\x1a\x30.google.cloud.binaryauthorization.v1beta1.Policy\"1\xda\x41\x04name\x82\xd3\xe4\x93\x02$\x12\"/v1beta1/{name=locations/*/policy}\x1aV\xca\x41\"binaryauthorization.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xb5\x02\n,com.google.cloud.binaryauthorization.v1beta1B\x1f\x42inaryAuthorizationServiceProtoP\x01Z[google.golang.org/genproto/googleapis/cloud/binaryauthorization/v1beta1;binaryauthorization\xf8\x01\x01\xaa\x02(Google.Cloud.BinaryAuthorization.V1Beta1\xca\x02(Google\\Cloud\\BinaryAuthorization\\V1beta1\xea\x02+Google::Cloud::BinaryAuthorization::V1beta1b\x06proto3')



_GETPOLICYREQUEST = DESCRIPTOR.message_types_by_name['GetPolicyRequest']
_UPDATEPOLICYREQUEST = DESCRIPTOR.message_types_by_name['UpdatePolicyRequest']
_CREATEATTESTORREQUEST = DESCRIPTOR.message_types_by_name['CreateAttestorRequest']
_GETATTESTORREQUEST = DESCRIPTOR.message_types_by_name['GetAttestorRequest']
_UPDATEATTESTORREQUEST = DESCRIPTOR.message_types_by_name['UpdateAttestorRequest']
_LISTATTESTORSREQUEST = DESCRIPTOR.message_types_by_name['ListAttestorsRequest']
_LISTATTESTORSRESPONSE = DESCRIPTOR.message_types_by_name['ListAttestorsResponse']
_DELETEATTESTORREQUEST = DESCRIPTOR.message_types_by_name['DeleteAttestorRequest']
_GETSYSTEMPOLICYREQUEST = DESCRIPTOR.message_types_by_name['GetSystemPolicyRequest']
GetPolicyRequest = _reflection.GeneratedProtocolMessageType('GetPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPOLICYREQUEST,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.GetPolicyRequest)
  })
_sym_db.RegisterMessage(GetPolicyRequest)

UpdatePolicyRequest = _reflection.GeneratedProtocolMessageType('UpdatePolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPOLICYREQUEST,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.UpdatePolicyRequest)
  })
_sym_db.RegisterMessage(UpdatePolicyRequest)

CreateAttestorRequest = _reflection.GeneratedProtocolMessageType('CreateAttestorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEATTESTORREQUEST,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.CreateAttestorRequest)
  })
_sym_db.RegisterMessage(CreateAttestorRequest)

GetAttestorRequest = _reflection.GeneratedProtocolMessageType('GetAttestorRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETATTESTORREQUEST,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.GetAttestorRequest)
  })
_sym_db.RegisterMessage(GetAttestorRequest)

UpdateAttestorRequest = _reflection.GeneratedProtocolMessageType('UpdateAttestorRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEATTESTORREQUEST,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.UpdateAttestorRequest)
  })
_sym_db.RegisterMessage(UpdateAttestorRequest)

ListAttestorsRequest = _reflection.GeneratedProtocolMessageType('ListAttestorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTATTESTORSREQUEST,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.ListAttestorsRequest)
  })
_sym_db.RegisterMessage(ListAttestorsRequest)

ListAttestorsResponse = _reflection.GeneratedProtocolMessageType('ListAttestorsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTATTESTORSRESPONSE,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.ListAttestorsResponse)
  })
_sym_db.RegisterMessage(ListAttestorsResponse)

DeleteAttestorRequest = _reflection.GeneratedProtocolMessageType('DeleteAttestorRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEATTESTORREQUEST,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.DeleteAttestorRequest)
  })
_sym_db.RegisterMessage(DeleteAttestorRequest)

GetSystemPolicyRequest = _reflection.GeneratedProtocolMessageType('GetSystemPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSYSTEMPOLICYREQUEST,
  '__module__' : 'google.cloud.binaryauthorization.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.binaryauthorization.v1beta1.GetSystemPolicyRequest)
  })
_sym_db.RegisterMessage(GetSystemPolicyRequest)

_BINAUTHZMANAGEMENTSERVICEV1BETA1 = DESCRIPTOR.services_by_name['BinauthzManagementServiceV1Beta1']
_SYSTEMPOLICYV1BETA1 = DESCRIPTOR.services_by_name['SystemPolicyV1Beta1']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n,com.google.cloud.binaryauthorization.v1beta1B\037BinaryAuthorizationServiceProtoP\001Z[google.golang.org/genproto/googleapis/cloud/binaryauthorization/v1beta1;binaryauthorization\370\001\001\252\002(Google.Cloud.BinaryAuthorization.V1Beta1\312\002(Google\\Cloud\\BinaryAuthorization\\V1beta1\352\002+Google::Cloud::BinaryAuthorization::V1beta1'
  _GETPOLICYREQUEST.fields_by_name['name']._options = None
  _GETPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A+\n)binaryauthorization.googleapis.com/Policy'
  _UPDATEPOLICYREQUEST.fields_by_name['policy']._options = None
  _UPDATEPOLICYREQUEST.fields_by_name['policy']._serialized_options = b'\342A\001\002'
  _CREATEATTESTORREQUEST.fields_by_name['parent']._options = None
  _CREATEATTESTORREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A-\n+cloudresourcemanager.googleapis.com/Project'
  _CREATEATTESTORREQUEST.fields_by_name['attestor_id']._options = None
  _CREATEATTESTORREQUEST.fields_by_name['attestor_id']._serialized_options = b'\342A\001\002'
  _CREATEATTESTORREQUEST.fields_by_name['attestor']._options = None
  _CREATEATTESTORREQUEST.fields_by_name['attestor']._serialized_options = b'\342A\001\002'
  _GETATTESTORREQUEST.fields_by_name['name']._options = None
  _GETATTESTORREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A-\n+binaryauthorization.googleapis.com/Attestor'
  _UPDATEATTESTORREQUEST.fields_by_name['attestor']._options = None
  _UPDATEATTESTORREQUEST.fields_by_name['attestor']._serialized_options = b'\342A\001\002'
  _LISTATTESTORSREQUEST.fields_by_name['parent']._options = None
  _LISTATTESTORSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A-\n+cloudresourcemanager.googleapis.com/Project'
  _DELETEATTESTORREQUEST.fields_by_name['name']._options = None
  _DELETEATTESTORREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A-\n+binaryauthorization.googleapis.com/Attestor'
  _GETSYSTEMPOLICYREQUEST.fields_by_name['name']._options = None
  _GETSYSTEMPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A+\n)binaryauthorization.googleapis.com/Policy'
  _BINAUTHZMANAGEMENTSERVICEV1BETA1._options = None
  _BINAUTHZMANAGEMENTSERVICEV1BETA1._serialized_options = b'\312A\"binaryauthorization.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['GetPolicy']._options = None
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['GetPolicy']._serialized_options = b'\332A\004name\202\323\344\223\002#\022!/v1beta1/{name=projects/*/policy}'
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['UpdatePolicy']._options = None
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['UpdatePolicy']._serialized_options = b'\332A\006policy\202\323\344\223\0022\032(/v1beta1/{policy.name=projects/*/policy}:\006policy'
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['CreateAttestor']._options = None
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['CreateAttestor']._serialized_options = b'\332A\033parent,attestor_id,attestor\202\323\344\223\0022\"&/v1beta1/{parent=projects/*}/attestors:\010attestor'
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['GetAttestor']._options = None
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['GetAttestor']._serialized_options = b'\332A\004name\202\323\344\223\002(\022&/v1beta1/{name=projects/*/attestors/*}'
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['UpdateAttestor']._options = None
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['UpdateAttestor']._serialized_options = b'\332A\010attestor\202\323\344\223\002;\032//v1beta1/{attestor.name=projects/*/attestors/*}:\010attestor'
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['ListAttestors']._options = None
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['ListAttestors']._serialized_options = b'\332A\006parent\202\323\344\223\002(\022&/v1beta1/{parent=projects/*}/attestors'
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['DeleteAttestor']._options = None
  _BINAUTHZMANAGEMENTSERVICEV1BETA1.methods_by_name['DeleteAttestor']._serialized_options = b'\332A\004name\202\323\344\223\002(*&/v1beta1/{name=projects/*/attestors/*}'
  _SYSTEMPOLICYV1BETA1._options = None
  _SYSTEMPOLICYV1BETA1._serialized_options = b'\312A\"binaryauthorization.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _SYSTEMPOLICYV1BETA1.methods_by_name['GetSystemPolicy']._options = None
  _SYSTEMPOLICYV1BETA1.methods_by_name['GetSystemPolicy']._serialized_options = b'\332A\004name\202\323\344\223\002$\022\"/v1beta1/{name=locations/*/policy}'
  _GETPOLICYREQUEST._serialized_start=302
  _GETPOLICYREQUEST._serialized_end=392
  _UPDATEPOLICYREQUEST._serialized_start=394
  _UPDATEPOLICYREQUEST._serialized_end=495
  _CREATEATTESTORREQUEST._serialized_start=498
  _CREATEATTESTORREQUEST._serialized_end=724
  _GETATTESTORREQUEST._serialized_start=726
  _GETATTESTORREQUEST._serialized_end=820
  _UPDATEATTESTORREQUEST._serialized_start=822
  _UPDATEATTESTORREQUEST._serialized_end=931
  _LISTATTESTORSREQUEST._serialized_start=934
  _LISTATTESTORSREQUEST._serialized_end=1094
  _LISTATTESTORSRESPONSE._serialized_start=1097
  _LISTATTESTORSRESPONSE._serialized_end=1242
  _DELETEATTESTORREQUEST._serialized_start=1244
  _DELETEATTESTORREQUEST._serialized_end=1341
  _GETSYSTEMPOLICYREQUEST._serialized_start=1343
  _GETSYSTEMPOLICYREQUEST._serialized_end=1439
  _BINAUTHZMANAGEMENTSERVICEV1BETA1._serialized_start=1442
  _BINAUTHZMANAGEMENTSERVICEV1BETA1._serialized_end=2925
  _SYSTEMPOLICYV1BETA1._serialized_start=2928
  _SYSTEMPOLICYV1BETA1._serialized_end=3224
# @@protoc_insertion_point(module_scope)
