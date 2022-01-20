# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner/v1/finding_addon.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/websecurityscanner/v1/finding_addon.proto\x12\"google.cloud.websecurityscanner.v1\"=\n\x04\x46orm\x12\x1d\n\naction_uri\x18\x01 \x01(\tR\tactionUri\x12\x16\n\x06\x66ields\x18\x02 \x03(\tR\x06\x66ields\"v\n\x0fOutdatedLibrary\x12!\n\x0clibrary_name\x18\x01 \x01(\tR\x0blibraryName\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12&\n\x0flearn_more_urls\x18\x03 \x03(\tR\rlearnMoreUrls\"Y\n\x11ViolatingResource\x12!\n\x0c\x63ontent_type\x18\x01 \x01(\tR\x0b\x63ontentType\x12!\n\x0cresource_url\x18\x02 \x01(\tR\x0bresourceUrl\"?\n\x14VulnerableParameters\x12\'\n\x0fparameter_names\x18\x01 \x03(\tR\x0eparameterNames\"\x86\x02\n\x11VulnerableHeaders\x12V\n\x07headers\x18\x01 \x03(\x0b\x32<.google.cloud.websecurityscanner.v1.VulnerableHeaders.HeaderR\x07headers\x12\x65\n\x0fmissing_headers\x18\x02 \x03(\x0b\x32<.google.cloud.websecurityscanner.v1.VulnerableHeaders.HeaderR\x0emissingHeaders\x1a\x32\n\x06Header\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\x99\x04\n\x03Xss\x12!\n\x0cstack_traces\x18\x01 \x03(\tR\x0bstackTraces\x12#\n\rerror_message\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12Y\n\rattack_vector\x18\x03 \x01(\x0e\x32\x34.google.cloud.websecurityscanner.v1.Xss.AttackVectorR\x0c\x61ttackVector\x12\x33\n\x16stored_xss_seeding_url\x18\x04 \x01(\tR\x13storedXssSeedingUrl\"\xb9\x02\n\x0c\x41ttackVector\x12\x1d\n\x19\x41TTACK_VECTOR_UNSPECIFIED\x10\x00\x12\x11\n\rLOCAL_STORAGE\x10\x01\x12\x13\n\x0fSESSION_STORAGE\x10\x02\x12\x0f\n\x0bWINDOW_NAME\x10\x03\x12\x0c\n\x08REFERRER\x10\x04\x12\x0e\n\nFORM_INPUT\x10\x05\x12\n\n\x06\x43OOKIE\x10\x06\x12\x10\n\x0cPOST_MESSAGE\x10\x07\x12\x12\n\x0eGET_PARAMETERS\x10\x08\x12\x10\n\x0cURL_FRAGMENT\x10\t\x12\x10\n\x0cHTML_COMMENT\x10\n\x12\x13\n\x0fPOST_PARAMETERS\x10\x0b\x12\x0c\n\x08PROTOCOL\x10\x0c\x12\x0e\n\nSTORED_XSS\x10\r\x12\x0f\n\x0bSAME_ORIGIN\x10\x0e\x12\x19\n\x15USER_CONTROLLABLE_URL\x10\x0f\x42\x85\x02\n&com.google.cloud.websecurityscanner.v1B\x11\x46indingAddonProtoP\x01ZTgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1;websecurityscanner\xaa\x02\"Google.Cloud.WebSecurityScanner.V1\xca\x02\"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1b\x06proto3')



_FORM = DESCRIPTOR.message_types_by_name['Form']
_OUTDATEDLIBRARY = DESCRIPTOR.message_types_by_name['OutdatedLibrary']
_VIOLATINGRESOURCE = DESCRIPTOR.message_types_by_name['ViolatingResource']
_VULNERABLEPARAMETERS = DESCRIPTOR.message_types_by_name['VulnerableParameters']
_VULNERABLEHEADERS = DESCRIPTOR.message_types_by_name['VulnerableHeaders']
_VULNERABLEHEADERS_HEADER = _VULNERABLEHEADERS.nested_types_by_name['Header']
_XSS = DESCRIPTOR.message_types_by_name['Xss']
_XSS_ATTACKVECTOR = _XSS.enum_types_by_name['AttackVector']
Form = _reflection.GeneratedProtocolMessageType('Form', (_message.Message,), {
  'DESCRIPTOR' : _FORM,
  '__module__' : 'google.cloud.websecurityscanner.v1.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1.Form)
  })
_sym_db.RegisterMessage(Form)

OutdatedLibrary = _reflection.GeneratedProtocolMessageType('OutdatedLibrary', (_message.Message,), {
  'DESCRIPTOR' : _OUTDATEDLIBRARY,
  '__module__' : 'google.cloud.websecurityscanner.v1.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1.OutdatedLibrary)
  })
_sym_db.RegisterMessage(OutdatedLibrary)

ViolatingResource = _reflection.GeneratedProtocolMessageType('ViolatingResource', (_message.Message,), {
  'DESCRIPTOR' : _VIOLATINGRESOURCE,
  '__module__' : 'google.cloud.websecurityscanner.v1.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1.ViolatingResource)
  })
_sym_db.RegisterMessage(ViolatingResource)

VulnerableParameters = _reflection.GeneratedProtocolMessageType('VulnerableParameters', (_message.Message,), {
  'DESCRIPTOR' : _VULNERABLEPARAMETERS,
  '__module__' : 'google.cloud.websecurityscanner.v1.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1.VulnerableParameters)
  })
_sym_db.RegisterMessage(VulnerableParameters)

VulnerableHeaders = _reflection.GeneratedProtocolMessageType('VulnerableHeaders', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _VULNERABLEHEADERS_HEADER,
    '__module__' : 'google.cloud.websecurityscanner.v1.finding_addon_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1.VulnerableHeaders.Header)
    })
  ,
  'DESCRIPTOR' : _VULNERABLEHEADERS,
  '__module__' : 'google.cloud.websecurityscanner.v1.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1.VulnerableHeaders)
  })
_sym_db.RegisterMessage(VulnerableHeaders)
_sym_db.RegisterMessage(VulnerableHeaders.Header)

Xss = _reflection.GeneratedProtocolMessageType('Xss', (_message.Message,), {
  'DESCRIPTOR' : _XSS,
  '__module__' : 'google.cloud.websecurityscanner.v1.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1.Xss)
  })
_sym_db.RegisterMessage(Xss)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.google.cloud.websecurityscanner.v1B\021FindingAddonProtoP\001ZTgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1;websecurityscanner\252\002\"Google.Cloud.WebSecurityScanner.V1\312\002\"Google\\Cloud\\WebSecurityScanner\\V1\352\002%Google::Cloud::WebSecurityScanner::V1'
  _FORM._serialized_start=94
  _FORM._serialized_end=155
  _OUTDATEDLIBRARY._serialized_start=157
  _OUTDATEDLIBRARY._serialized_end=275
  _VIOLATINGRESOURCE._serialized_start=277
  _VIOLATINGRESOURCE._serialized_end=366
  _VULNERABLEPARAMETERS._serialized_start=368
  _VULNERABLEPARAMETERS._serialized_end=431
  _VULNERABLEHEADERS._serialized_start=434
  _VULNERABLEHEADERS._serialized_end=696
  _VULNERABLEHEADERS_HEADER._serialized_start=646
  _VULNERABLEHEADERS_HEADER._serialized_end=696
  _XSS._serialized_start=699
  _XSS._serialized_end=1236
  _XSS_ATTACKVECTOR._serialized_start=923
  _XSS_ATTACKVECTOR._serialized_end=1236
# @@protoc_insertion_point(module_scope)
