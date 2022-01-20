# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/identitytoolkit/v2/authentication_service.proto
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
from google.cloud.identitytoolkit.v2 import mfa_info_pb2 as google_dot_cloud_dot_identitytoolkit_dot_v2_dot_mfa__info__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/identitytoolkit/v2/authentication_service.proto\x12\x1fgoogle.cloud.identitytoolkit.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/cloud/identitytoolkit/v2/mfa_info.proto\x1a\x17google/api/client.proto\"\x80\x02\n\x18\x46inalizeMfaSignInRequest\x12:\n\x16mfa_pending_credential\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x14mfaPendingCredential\x12v\n\x17phone_verification_info\x18\x03 \x01(\x0b\x32<.google.cloud.identitytoolkit.v2.FinalizeMfaPhoneRequestInfoH\x00R\x15phoneVerificationInfo\x12\x1b\n\ttenant_id\x18\x04 \x01(\tR\x08tenantIdB\x13\n\x11verification_info\"\xdb\x01\n\x19\x46inalizeMfaSignInResponse\x12\x19\n\x08id_token\x18\x01 \x01(\tR\x07idToken\x12#\n\rrefresh_token\x18\x02 \x01(\tR\x0crefreshToken\x12g\n\x0fphone_auth_info\x18\x03 \x01(\x0b\x32=.google.cloud.identitytoolkit.v2.FinalizeMfaPhoneResponseInfoH\x00R\rphoneAuthInfoB\x15\n\x13\x61uxiliary_auth_info\"\x9c\x02\n\x15StartMfaSignInRequest\x12:\n\x16mfa_pending_credential\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x14mfaPendingCredential\x12\x30\n\x11mfa_enrollment_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x0fmfaEnrollmentId\x12h\n\x12phone_sign_in_info\x18\x04 \x01(\x0b\x32\x39.google.cloud.identitytoolkit.v2.StartMfaPhoneRequestInfoH\x00R\x0fphoneSignInInfo\x12\x1b\n\ttenant_id\x18\x05 \x01(\tR\x08tenantIdB\x0e\n\x0csign_in_info\"\x97\x01\n\x16StartMfaSignInResponse\x12l\n\x13phone_response_info\x18\x01 \x01(\x0b\x32:.google.cloud.identitytoolkit.v2.StartMfaPhoneResponseInfoH\x00R\x11phoneResponseInfoB\x0f\n\rresponse_info2\xd1\x03\n\x15\x41uthenticationService\x12\xb6\x01\n\x11\x46inalizeMfaSignIn\x12\x39.google.cloud.identitytoolkit.v2.FinalizeMfaSignInRequest\x1a:.google.cloud.identitytoolkit.v2.FinalizeMfaSignInResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/v2/accounts/mfaSignIn:finalize:\x01*\x12\xaa\x01\n\x0eStartMfaSignIn\x12\x36.google.cloud.identitytoolkit.v2.StartMfaSignInRequest\x1a\x37.google.cloud.identitytoolkit.v2.StartMfaSignInResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v2/accounts/mfaSignIn:start:\x01*\x1aR\xca\x41\x1eidentitytoolkit.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xe0\x01\n#com.google.cloud.identitytoolkit.v2P\x01ZNgoogle.golang.org/genproto/googleapis/cloud/identitytoolkit/v2;identitytoolkit\xaa\x02\x1fGoogle.Cloud.IdentityToolkit.V2\xca\x02\x1fGoogle\\Cloud\\IdentityToolkit\\V2\xea\x02\"Google::Cloud::IdentityToolkit::V2b\x06proto3')



_FINALIZEMFASIGNINREQUEST = DESCRIPTOR.message_types_by_name['FinalizeMfaSignInRequest']
_FINALIZEMFASIGNINRESPONSE = DESCRIPTOR.message_types_by_name['FinalizeMfaSignInResponse']
_STARTMFASIGNINREQUEST = DESCRIPTOR.message_types_by_name['StartMfaSignInRequest']
_STARTMFASIGNINRESPONSE = DESCRIPTOR.message_types_by_name['StartMfaSignInResponse']
FinalizeMfaSignInRequest = _reflection.GeneratedProtocolMessageType('FinalizeMfaSignInRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEMFASIGNINREQUEST,
  '__module__' : 'google.cloud.identitytoolkit.v2.authentication_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.identitytoolkit.v2.FinalizeMfaSignInRequest)
  })
_sym_db.RegisterMessage(FinalizeMfaSignInRequest)

FinalizeMfaSignInResponse = _reflection.GeneratedProtocolMessageType('FinalizeMfaSignInResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEMFASIGNINRESPONSE,
  '__module__' : 'google.cloud.identitytoolkit.v2.authentication_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.identitytoolkit.v2.FinalizeMfaSignInResponse)
  })
_sym_db.RegisterMessage(FinalizeMfaSignInResponse)

StartMfaSignInRequest = _reflection.GeneratedProtocolMessageType('StartMfaSignInRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTMFASIGNINREQUEST,
  '__module__' : 'google.cloud.identitytoolkit.v2.authentication_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.identitytoolkit.v2.StartMfaSignInRequest)
  })
_sym_db.RegisterMessage(StartMfaSignInRequest)

StartMfaSignInResponse = _reflection.GeneratedProtocolMessageType('StartMfaSignInResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTMFASIGNINRESPONSE,
  '__module__' : 'google.cloud.identitytoolkit.v2.authentication_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.identitytoolkit.v2.StartMfaSignInResponse)
  })
_sym_db.RegisterMessage(StartMfaSignInResponse)

_AUTHENTICATIONSERVICE = DESCRIPTOR.services_by_name['AuthenticationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.identitytoolkit.v2P\001ZNgoogle.golang.org/genproto/googleapis/cloud/identitytoolkit/v2;identitytoolkit\252\002\037Google.Cloud.IdentityToolkit.V2\312\002\037Google\\Cloud\\IdentityToolkit\\V2\352\002\"Google::Cloud::IdentityToolkit::V2'
  _FINALIZEMFASIGNINREQUEST.fields_by_name['mfa_pending_credential']._options = None
  _FINALIZEMFASIGNINREQUEST.fields_by_name['mfa_pending_credential']._serialized_options = b'\342A\001\002'
  _STARTMFASIGNINREQUEST.fields_by_name['mfa_pending_credential']._options = None
  _STARTMFASIGNINREQUEST.fields_by_name['mfa_pending_credential']._serialized_options = b'\342A\001\002'
  _STARTMFASIGNINREQUEST.fields_by_name['mfa_enrollment_id']._options = None
  _STARTMFASIGNINREQUEST.fields_by_name['mfa_enrollment_id']._serialized_options = b'\342A\001\002'
  _AUTHENTICATIONSERVICE._options = None
  _AUTHENTICATIONSERVICE._serialized_options = b'\312A\036identitytoolkit.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _AUTHENTICATIONSERVICE.methods_by_name['FinalizeMfaSignIn']._options = None
  _AUTHENTICATIONSERVICE.methods_by_name['FinalizeMfaSignIn']._serialized_options = b'\202\323\344\223\002$\"\037/v2/accounts/mfaSignIn:finalize:\001*'
  _AUTHENTICATIONSERVICE.methods_by_name['StartMfaSignIn']._options = None
  _AUTHENTICATIONSERVICE.methods_by_name['StartMfaSignIn']._serialized_options = b'\202\323\344\223\002!\"\034/v2/accounts/mfaSignIn:start:\001*'
  _FINALIZEMFASIGNINREQUEST._serialized_start=234
  _FINALIZEMFASIGNINREQUEST._serialized_end=490
  _FINALIZEMFASIGNINRESPONSE._serialized_start=493
  _FINALIZEMFASIGNINRESPONSE._serialized_end=712
  _STARTMFASIGNINREQUEST._serialized_start=715
  _STARTMFASIGNINREQUEST._serialized_end=999
  _STARTMFASIGNINRESPONSE._serialized_start=1002
  _STARTMFASIGNINRESPONSE._serialized_end=1153
  _AUTHENTICATIONSERVICE._serialized_start=1156
  _AUTHENTICATIONSERVICE._serialized_end=1621
# @@protoc_insertion_point(module_scope)
