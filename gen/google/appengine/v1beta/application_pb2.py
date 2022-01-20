# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/appengine/v1beta/application.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/appengine/v1beta/application.proto\x12\x17google.appengine.v1beta\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\"\xab\n\n\x0b\x41pplication\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12O\n\x0e\x64ispatch_rules\x18\x03 \x03(\x0b\x32(.google.appengine.v1beta.UrlDispatchRuleR\rdispatchRules\x12\x1f\n\x0b\x61uth_domain\x18\x06 \x01(\tR\nauthDomain\x12\x1f\n\x0blocation_id\x18\x07 \x01(\tR\nlocationId\x12\x1f\n\x0b\x63ode_bucket\x18\x08 \x01(\tR\ncodeBucket\x12U\n\x19\x64\x65\x66\x61ult_cookie_expiration\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationR\x17\x64\x65\x66\x61ultCookieExpiration\x12Y\n\x0eserving_status\x18\n \x01(\x0e\x32\x32.google.appengine.v1beta.Application.ServingStatusR\rservingStatus\x12)\n\x10\x64\x65\x66\x61ult_hostname\x18\x0b \x01(\tR\x0f\x64\x65\x66\x61ultHostname\x12%\n\x0e\x64\x65\x66\x61ult_bucket\x18\x0c \x01(\tR\rdefaultBucket\x12I\n\x03iap\x18\x0e \x01(\x0b\x32\x37.google.appengine.v1beta.Application.IdentityAwareProxyR\x03iap\x12\x1d\n\ngcr_domain\x18\x10 \x01(\tR\tgcrDomain\x12V\n\rdatabase_type\x18\x11 \x01(\x0e\x32\x31.google.appengine.v1beta.Application.DatabaseTypeR\x0c\x64\x61tabaseType\x12_\n\x10\x66\x65\x61ture_settings\x18\x12 \x01(\x0b\x32\x34.google.appengine.v1beta.Application.FeatureSettingsR\x0f\x66\x65\x61tureSettings\x1a\xc9\x01\n\x12IdentityAwareProxy\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12(\n\x10oauth2_client_id\x18\x02 \x01(\tR\x0eoauth2ClientId\x12\x30\n\x14oauth2_client_secret\x18\x03 \x01(\tR\x12oauth2ClientSecret\x12=\n\x1boauth2_client_secret_sha256\x18\x04 \x01(\tR\x18oauth2ClientSecretSha256\x1a~\n\x0f\x46\x65\x61tureSettings\x12.\n\x13split_health_checks\x18\x01 \x01(\x08R\x11splitHealthChecks\x12;\n\x1ause_container_optimized_os\x18\x02 \x01(\x08R\x17useContainerOptimizedOs\"U\n\rServingStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x11\n\rUSER_DISABLED\x10\x02\x12\x13\n\x0fSYSTEM_DISABLED\x10\x03\"z\n\x0c\x44\x61tabaseType\x12\x1d\n\x19\x44\x41TABASE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x43LOUD_DATASTORE\x10\x01\x12\x13\n\x0f\x43LOUD_FIRESTORE\x10\x02\x12!\n\x1d\x43LOUD_DATASTORE_COMPATIBILITY\x10\x03\"W\n\x0fUrlDispatchRule\x12\x16\n\x06\x64omain\x18\x01 \x01(\tR\x06\x64omain\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12\x18\n\x07service\x18\x03 \x01(\tR\x07serviceB\xd6\x01\n\x1b\x63om.google.appengine.v1betaB\x10\x41pplicationProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')



_APPLICATION = DESCRIPTOR.message_types_by_name['Application']
_APPLICATION_IDENTITYAWAREPROXY = _APPLICATION.nested_types_by_name['IdentityAwareProxy']
_APPLICATION_FEATURESETTINGS = _APPLICATION.nested_types_by_name['FeatureSettings']
_URLDISPATCHRULE = DESCRIPTOR.message_types_by_name['UrlDispatchRule']
_APPLICATION_SERVINGSTATUS = _APPLICATION.enum_types_by_name['ServingStatus']
_APPLICATION_DATABASETYPE = _APPLICATION.enum_types_by_name['DatabaseType']
Application = _reflection.GeneratedProtocolMessageType('Application', (_message.Message,), {

  'IdentityAwareProxy' : _reflection.GeneratedProtocolMessageType('IdentityAwareProxy', (_message.Message,), {
    'DESCRIPTOR' : _APPLICATION_IDENTITYAWAREPROXY,
    '__module__' : 'google.appengine.v1beta.application_pb2'
    # @@protoc_insertion_point(class_scope:google.appengine.v1beta.Application.IdentityAwareProxy)
    })
  ,

  'FeatureSettings' : _reflection.GeneratedProtocolMessageType('FeatureSettings', (_message.Message,), {
    'DESCRIPTOR' : _APPLICATION_FEATURESETTINGS,
    '__module__' : 'google.appengine.v1beta.application_pb2'
    # @@protoc_insertion_point(class_scope:google.appengine.v1beta.Application.FeatureSettings)
    })
  ,
  'DESCRIPTOR' : _APPLICATION,
  '__module__' : 'google.appengine.v1beta.application_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.Application)
  })
_sym_db.RegisterMessage(Application)
_sym_db.RegisterMessage(Application.IdentityAwareProxy)
_sym_db.RegisterMessage(Application.FeatureSettings)

UrlDispatchRule = _reflection.GeneratedProtocolMessageType('UrlDispatchRule', (_message.Message,), {
  'DESCRIPTOR' : _URLDISPATCHRULE,
  '__module__' : 'google.appengine.v1beta.application_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.UrlDispatchRule)
  })
_sym_db.RegisterMessage(UrlDispatchRule)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.google.appengine.v1betaB\020ApplicationProtoP\001Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\252\002\035Google.Cloud.AppEngine.V1Beta\312\002\035Google\\Cloud\\AppEngine\\V1beta\352\002 Google::Cloud::AppEngine::V1beta'
  _APPLICATION._serialized_start=133
  _APPLICATION._serialized_end=1456
  _APPLICATION_IDENTITYAWAREPROXY._serialized_start=916
  _APPLICATION_IDENTITYAWAREPROXY._serialized_end=1117
  _APPLICATION_FEATURESETTINGS._serialized_start=1119
  _APPLICATION_FEATURESETTINGS._serialized_end=1245
  _APPLICATION_SERVINGSTATUS._serialized_start=1247
  _APPLICATION_SERVINGSTATUS._serialized_end=1332
  _APPLICATION_DATABASETYPE._serialized_start=1334
  _APPLICATION_DATABASETYPE._serialized_end=1456
  _URLDISPATCHRULE._serialized_start=1458
  _URLDISPATCHRULE._serialized_end=1545
# @@protoc_insertion_point(module_scope)
