# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/oslogin/v1alpha/oslogin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.oslogin.common import common_pb2 as google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/oslogin/v1alpha/oslogin.proto\x12\x1cgoogle.cloud.oslogin.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a(google/cloud/oslogin/common/common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"\xe6\x02\n\x0cLoginProfile\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12P\n\x0eposix_accounts\x18\x02 \x03(\x0b\x32).google.cloud.oslogin.common.PosixAccountR\rposixAccounts\x12\x65\n\x0fssh_public_keys\x18\x03 \x03(\x0b\x32=.google.cloud.oslogin.v1alpha.LoginProfile.SshPublicKeysEntryR\rsshPublicKeys\x12\x1c\n\tsuspended\x18\x04 \x01(\x08R\tsuspended\x1ak\n\x12SshPublicKeysEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12?\n\x05value\x18\x02 \x01(\x0b\x32).google.cloud.oslogin.common.SshPublicKeyR\x05value:\x02\x38\x01\"/\n\x19\x44\x65letePosixAccountRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"/\n\x19\x44\x65leteSshPublicKeyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\",\n\x16GetLoginProfileRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\",\n\x16GetSshPublicKeyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\xa3\x01\n\x19ImportSshPublicKeyRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12O\n\x0essh_public_key\x18\x02 \x01(\x0b\x32).google.cloud.oslogin.common.SshPublicKeyR\x0csshPublicKey\x12\x1d\n\nproject_id\x18\x03 \x01(\tR\tprojectId\"m\n\x1aImportSshPublicKeyResponse\x12O\n\rlogin_profile\x18\x01 \x01(\x0b\x32*.google.cloud.oslogin.v1alpha.LoginProfileR\x0cloginProfile\"\xbd\x01\n\x19UpdateSshPublicKeyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12O\n\x0essh_public_key\x18\x02 \x01(\x0b\x32).google.cloud.oslogin.common.SshPublicKeyR\x0csshPublicKey\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask2\x93\x08\n\x0eOsLoginService\x12\x91\x01\n\x12\x44\x65letePosixAccount\x12\x37.google.cloud.oslogin.v1alpha.DeletePosixAccountRequest\x1a\x16.google.protobuf.Empty\"*\x82\xd3\xe4\x93\x02$*\"/v1alpha/{name=users/*/projects/*}\x12\x96\x01\n\x12\x44\x65leteSshPublicKey\x12\x37.google.cloud.oslogin.v1alpha.DeleteSshPublicKeyRequest\x1a\x16.google.protobuf.Empty\"/\x82\xd3\xe4\x93\x02)*\'/v1alpha/{name=users/*/sshPublicKeys/*}\x12\xa1\x01\n\x0fGetLoginProfile\x12\x34.google.cloud.oslogin.v1alpha.GetLoginProfileRequest\x1a*.google.cloud.oslogin.v1alpha.LoginProfile\",\x82\xd3\xe4\x93\x02&\x12$/v1alpha/{name=users/*}/loginProfile\x12\xa3\x01\n\x0fGetSshPublicKey\x12\x34.google.cloud.oslogin.v1alpha.GetSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey\"/\x82\xd3\xe4\x93\x02)\x12\'/v1alpha/{name=users/*/sshPublicKeys/*}\x12\xcd\x01\n\x12ImportSshPublicKey\x12\x37.google.cloud.oslogin.v1alpha.ImportSshPublicKeyRequest\x1a\x38.google.cloud.oslogin.v1alpha.ImportSshPublicKeyResponse\"D\x82\xd3\xe4\x93\x02>\",/v1alpha/{parent=users/*}:importSshPublicKey:\x0essh_public_key\x12\xb9\x01\n\x12UpdateSshPublicKey\x12\x37.google.cloud.oslogin.v1alpha.UpdateSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey\"?\x82\xd3\xe4\x93\x02\x39\x32\'/v1alpha/{name=users/*/sshPublicKeys/*}:\x0essh_public_keyB\xb5\x01\n com.google.cloud.oslogin.v1alphaB\x0cOsLoginProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/oslogin/v1alpha;oslogin\xaa\x02\x1cGoogle.Cloud.OsLogin.V1Alpha\xca\x02\x1cGoogle\\Cloud\\OsLogin\\V1alphab\x06proto3')



_LOGINPROFILE = DESCRIPTOR.message_types_by_name['LoginProfile']
_LOGINPROFILE_SSHPUBLICKEYSENTRY = _LOGINPROFILE.nested_types_by_name['SshPublicKeysEntry']
_DELETEPOSIXACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['DeletePosixAccountRequest']
_DELETESSHPUBLICKEYREQUEST = DESCRIPTOR.message_types_by_name['DeleteSshPublicKeyRequest']
_GETLOGINPROFILEREQUEST = DESCRIPTOR.message_types_by_name['GetLoginProfileRequest']
_GETSSHPUBLICKEYREQUEST = DESCRIPTOR.message_types_by_name['GetSshPublicKeyRequest']
_IMPORTSSHPUBLICKEYREQUEST = DESCRIPTOR.message_types_by_name['ImportSshPublicKeyRequest']
_IMPORTSSHPUBLICKEYRESPONSE = DESCRIPTOR.message_types_by_name['ImportSshPublicKeyResponse']
_UPDATESSHPUBLICKEYREQUEST = DESCRIPTOR.message_types_by_name['UpdateSshPublicKeyRequest']
LoginProfile = _reflection.GeneratedProtocolMessageType('LoginProfile', (_message.Message,), {

  'SshPublicKeysEntry' : _reflection.GeneratedProtocolMessageType('SshPublicKeysEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOGINPROFILE_SSHPUBLICKEYSENTRY,
    '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.LoginProfile.SshPublicKeysEntry)
    })
  ,
  'DESCRIPTOR' : _LOGINPROFILE,
  '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.LoginProfile)
  })
_sym_db.RegisterMessage(LoginProfile)
_sym_db.RegisterMessage(LoginProfile.SshPublicKeysEntry)

DeletePosixAccountRequest = _reflection.GeneratedProtocolMessageType('DeletePosixAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPOSIXACCOUNTREQUEST,
  '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.DeletePosixAccountRequest)
  })
_sym_db.RegisterMessage(DeletePosixAccountRequest)

DeleteSshPublicKeyRequest = _reflection.GeneratedProtocolMessageType('DeleteSshPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESSHPUBLICKEYREQUEST,
  '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.DeleteSshPublicKeyRequest)
  })
_sym_db.RegisterMessage(DeleteSshPublicKeyRequest)

GetLoginProfileRequest = _reflection.GeneratedProtocolMessageType('GetLoginProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGINPROFILEREQUEST,
  '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.GetLoginProfileRequest)
  })
_sym_db.RegisterMessage(GetLoginProfileRequest)

GetSshPublicKeyRequest = _reflection.GeneratedProtocolMessageType('GetSshPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSSHPUBLICKEYREQUEST,
  '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.GetSshPublicKeyRequest)
  })
_sym_db.RegisterMessage(GetSshPublicKeyRequest)

ImportSshPublicKeyRequest = _reflection.GeneratedProtocolMessageType('ImportSshPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTSSHPUBLICKEYREQUEST,
  '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.ImportSshPublicKeyRequest)
  })
_sym_db.RegisterMessage(ImportSshPublicKeyRequest)

ImportSshPublicKeyResponse = _reflection.GeneratedProtocolMessageType('ImportSshPublicKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTSSHPUBLICKEYRESPONSE,
  '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.ImportSshPublicKeyResponse)
  })
_sym_db.RegisterMessage(ImportSshPublicKeyResponse)

UpdateSshPublicKeyRequest = _reflection.GeneratedProtocolMessageType('UpdateSshPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESSHPUBLICKEYREQUEST,
  '__module__' : 'google.cloud.oslogin.v1alpha.oslogin_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.oslogin.v1alpha.UpdateSshPublicKeyRequest)
  })
_sym_db.RegisterMessage(UpdateSshPublicKeyRequest)

_OSLOGINSERVICE = DESCRIPTOR.services_by_name['OsLoginService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.google.cloud.oslogin.v1alphaB\014OsLoginProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/oslogin/v1alpha;oslogin\252\002\034Google.Cloud.OsLogin.V1Alpha\312\002\034Google\\Cloud\\OsLogin\\V1alpha'
  _LOGINPROFILE_SSHPUBLICKEYSENTRY._options = None
  _LOGINPROFILE_SSHPUBLICKEYSENTRY._serialized_options = b'8\001'
  _OSLOGINSERVICE.methods_by_name['DeletePosixAccount']._options = None
  _OSLOGINSERVICE.methods_by_name['DeletePosixAccount']._serialized_options = b'\202\323\344\223\002$*\"/v1alpha/{name=users/*/projects/*}'
  _OSLOGINSERVICE.methods_by_name['DeleteSshPublicKey']._options = None
  _OSLOGINSERVICE.methods_by_name['DeleteSshPublicKey']._serialized_options = b'\202\323\344\223\002)*\'/v1alpha/{name=users/*/sshPublicKeys/*}'
  _OSLOGINSERVICE.methods_by_name['GetLoginProfile']._options = None
  _OSLOGINSERVICE.methods_by_name['GetLoginProfile']._serialized_options = b'\202\323\344\223\002&\022$/v1alpha/{name=users/*}/loginProfile'
  _OSLOGINSERVICE.methods_by_name['GetSshPublicKey']._options = None
  _OSLOGINSERVICE.methods_by_name['GetSshPublicKey']._serialized_options = b'\202\323\344\223\002)\022\'/v1alpha/{name=users/*/sshPublicKeys/*}'
  _OSLOGINSERVICE.methods_by_name['ImportSshPublicKey']._options = None
  _OSLOGINSERVICE.methods_by_name['ImportSshPublicKey']._serialized_options = b'\202\323\344\223\002>\",/v1alpha/{parent=users/*}:importSshPublicKey:\016ssh_public_key'
  _OSLOGINSERVICE.methods_by_name['UpdateSshPublicKey']._options = None
  _OSLOGINSERVICE.methods_by_name['UpdateSshPublicKey']._serialized_options = b'\202\323\344\223\00292\'/v1alpha/{name=users/*/sshPublicKeys/*}:\016ssh_public_key'
  _LOGINPROFILE._serialized_start=212
  _LOGINPROFILE._serialized_end=570
  _LOGINPROFILE_SSHPUBLICKEYSENTRY._serialized_start=463
  _LOGINPROFILE_SSHPUBLICKEYSENTRY._serialized_end=570
  _DELETEPOSIXACCOUNTREQUEST._serialized_start=572
  _DELETEPOSIXACCOUNTREQUEST._serialized_end=619
  _DELETESSHPUBLICKEYREQUEST._serialized_start=621
  _DELETESSHPUBLICKEYREQUEST._serialized_end=668
  _GETLOGINPROFILEREQUEST._serialized_start=670
  _GETLOGINPROFILEREQUEST._serialized_end=714
  _GETSSHPUBLICKEYREQUEST._serialized_start=716
  _GETSSHPUBLICKEYREQUEST._serialized_end=760
  _IMPORTSSHPUBLICKEYREQUEST._serialized_start=763
  _IMPORTSSHPUBLICKEYREQUEST._serialized_end=926
  _IMPORTSSHPUBLICKEYRESPONSE._serialized_start=928
  _IMPORTSSHPUBLICKEYRESPONSE._serialized_end=1037
  _UPDATESSHPUBLICKEYREQUEST._serialized_start=1040
  _UPDATESSHPUBLICKEYREQUEST._serialized_end=1229
  _OSLOGINSERVICE._serialized_start=1232
  _OSLOGINSERVICE._serialized_end=2275
# @@protoc_insertion_point(module_scope)
