# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/cx/v3/security_settings.proto
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
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/dialogflow/cx/v3/security_settings.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"e\n\x1aGetSecuritySettingsRequest\x12G\n\x04name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*dialogflow.googleapis.com/SecuritySettingsR\x04name\"\xc6\x01\n\x1dUpdateSecuritySettingsRequest\x12\x62\n\x11security_settings\x18\x01 \x01(\x0b\x32/.google.cloud.dialogflow.cx.v3.SecuritySettingsB\x04\xe2\x41\x01\x02R\x10securitySettings\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"\xa6\x01\n\x1bListSecuritySettingsRequest\x12K\n\x06parent\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\x12*dialogflow.googleapis.com/SecuritySettingsR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\xa4\x01\n\x1cListSecuritySettingsResponse\x12\\\n\x11security_settings\x18\x01 \x03(\x0b\x32/.google.cloud.dialogflow.cx.v3.SecuritySettingsR\x10securitySettings\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xd0\x01\n\x1d\x43reateSecuritySettingsRequest\x12K\n\x06parent\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\x12*dialogflow.googleapis.com/SecuritySettingsR\x06parent\x12\x62\n\x11security_settings\x18\x02 \x01(\x0b\x32/.google.cloud.dialogflow.cx.v3.SecuritySettingsB\x04\xe2\x41\x01\x02R\x10securitySettings\"h\n\x1d\x44\x65leteSecuritySettingsRequest\x12G\n\x04name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*dialogflow.googleapis.com/SecuritySettingsR\x04name\"\xc6\t\n\x10SecuritySettings\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x64isplayName\x12p\n\x12redaction_strategy\x18\x03 \x01(\x0e\x32\x41.google.cloud.dialogflow.cx.v3.SecuritySettings.RedactionStrategyR\x11redactionStrategy\x12g\n\x0fredaction_scope\x18\x04 \x01(\x0e\x32>.google.cloud.dialogflow.cx.v3.SecuritySettings.RedactionScopeR\x0eredactionScope\x12R\n\x10inspect_template\x18\t \x01(\tB\'\xfa\x41$\n\"dlp.googleapis.com/InspectTemplateR\x0finspectTemplate\x12[\n\x13\x64\x65identify_template\x18\x11 \x01(\tB*\xfa\x41\'\n%dlp.googleapis.com/DeidentifyTemplateR\x12\x64\x65identifyTemplate\x12\x34\n\x15retention_window_days\x18\x06 \x01(\x05H\x00R\x13retentionWindowDays\x12g\n\x10purge_data_types\x18\x08 \x03(\x0e\x32=.google.cloud.dialogflow.cx.v3.SecuritySettings.PurgeDataTypeR\x0epurgeDataTypes\x12\x80\x01\n\x18insights_export_settings\x18\r \x01(\x0b\x32\x46.google.cloud.dialogflow.cx.v3.SecuritySettings.InsightsExportSettingsR\x16insightsExportSettings\x1aN\n\x16InsightsExportSettings\x12\x34\n\x16\x65nable_insights_export\x18\x01 \x01(\x08R\x14\x65nableInsightsExport\"P\n\x11RedactionStrategy\x12\"\n\x1eREDACTION_STRATEGY_UNSPECIFIED\x10\x00\x12\x17\n\x13REDACT_WITH_SERVICE\x10\x01\"J\n\x0eRedactionScope\x12\x1f\n\x1bREDACTION_SCOPE_UNSPECIFIED\x10\x00\x12\x17\n\x13REDACT_DISK_STORAGE\x10\x02\"H\n\rPurgeDataType\x12\x1f\n\x1bPURGE_DATA_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x44IALOGFLOW_HISTORY\x10\x01:}\xea\x41z\n*dialogflow.googleapis.com/SecuritySettings\x12Lprojects/{project}/locations/{location}/securitySettings/{security_settings}B\x10\n\x0e\x64\x61ta_retention2\xef\t\n\x17SecuritySettingsService\x12\xf3\x01\n\x16\x43reateSecuritySettings\x12<.google.cloud.dialogflow.cx.v3.CreateSecuritySettingsRequest\x1a/.google.cloud.dialogflow.cx.v3.SecuritySettings\"j\xda\x41\x18parent,security_settings\x82\xd3\xe4\x93\x02I\"4/v3/{parent=projects/*/locations/*}/securitySettings:\x11security_settings\x12\xc6\x01\n\x13GetSecuritySettings\x12\x39.google.cloud.dialogflow.cx.v3.GetSecuritySettingsRequest\x1a/.google.cloud.dialogflow.cx.v3.SecuritySettings\"C\xda\x41\x04name\x82\xd3\xe4\x93\x02\x36\x12\x34/v3/{name=projects/*/locations/*/securitySettings/*}\x12\x8b\x02\n\x16UpdateSecuritySettings\x12<.google.cloud.dialogflow.cx.v3.UpdateSecuritySettingsRequest\x1a/.google.cloud.dialogflow.cx.v3.SecuritySettings\"\x81\x01\xda\x41\x1dsecurity_settings,update_mask\x82\xd3\xe4\x93\x02[2F/v3/{security_settings.name=projects/*/locations/*/securitySettings/*}:\x11security_settings\x12\xd6\x01\n\x14ListSecuritySettings\x12:.google.cloud.dialogflow.cx.v3.ListSecuritySettingsRequest\x1a;.google.cloud.dialogflow.cx.v3.ListSecuritySettingsResponse\"E\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x36\x12\x34/v3/{parent=projects/*/locations/*}/securitySettings\x12\xb3\x01\n\x16\x44\x65leteSecuritySettings\x12<.google.cloud.dialogflow.cx.v3.DeleteSecuritySettingsRequest\x1a\x16.google.protobuf.Empty\"C\xda\x41\x04name\x82\xd3\xe4\x93\x02\x36*4/v3/{name=projects/*/locations/*/securitySettings/*}\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xf0\x04\n!com.google.cloud.dialogflow.cx.v3B\x15SecuritySettingsProtoP\x01Z?google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3;cx\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xea\x41\xc8\x01\n\"dlp.googleapis.com/InspectTemplate\x12Uorganizations/{organization}/locations/{location}/inspectTemplates/{inspect_template}\x12Kprojects/{project}/locations/{location}/inspectTemplates/{inspect_template}\xea\x41\xd7\x01\n%dlp.googleapis.com/DeidentifyTemplate\x12[organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}\x12Qprojects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}b\x06proto3')



_GETSECURITYSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['GetSecuritySettingsRequest']
_UPDATESECURITYSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['UpdateSecuritySettingsRequest']
_LISTSECURITYSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['ListSecuritySettingsRequest']
_LISTSECURITYSETTINGSRESPONSE = DESCRIPTOR.message_types_by_name['ListSecuritySettingsResponse']
_CREATESECURITYSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['CreateSecuritySettingsRequest']
_DELETESECURITYSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['DeleteSecuritySettingsRequest']
_SECURITYSETTINGS = DESCRIPTOR.message_types_by_name['SecuritySettings']
_SECURITYSETTINGS_INSIGHTSEXPORTSETTINGS = _SECURITYSETTINGS.nested_types_by_name['InsightsExportSettings']
_SECURITYSETTINGS_REDACTIONSTRATEGY = _SECURITYSETTINGS.enum_types_by_name['RedactionStrategy']
_SECURITYSETTINGS_REDACTIONSCOPE = _SECURITYSETTINGS.enum_types_by_name['RedactionScope']
_SECURITYSETTINGS_PURGEDATATYPE = _SECURITYSETTINGS.enum_types_by_name['PurgeDataType']
GetSecuritySettingsRequest = _reflection.GeneratedProtocolMessageType('GetSecuritySettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSECURITYSETTINGSREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.security_settings_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.GetSecuritySettingsRequest)
  })
_sym_db.RegisterMessage(GetSecuritySettingsRequest)

UpdateSecuritySettingsRequest = _reflection.GeneratedProtocolMessageType('UpdateSecuritySettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESECURITYSETTINGSREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.security_settings_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.UpdateSecuritySettingsRequest)
  })
_sym_db.RegisterMessage(UpdateSecuritySettingsRequest)

ListSecuritySettingsRequest = _reflection.GeneratedProtocolMessageType('ListSecuritySettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSECURITYSETTINGSREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.security_settings_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ListSecuritySettingsRequest)
  })
_sym_db.RegisterMessage(ListSecuritySettingsRequest)

ListSecuritySettingsResponse = _reflection.GeneratedProtocolMessageType('ListSecuritySettingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSECURITYSETTINGSRESPONSE,
  '__module__' : 'google.cloud.dialogflow.cx.v3.security_settings_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ListSecuritySettingsResponse)
  })
_sym_db.RegisterMessage(ListSecuritySettingsResponse)

CreateSecuritySettingsRequest = _reflection.GeneratedProtocolMessageType('CreateSecuritySettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESECURITYSETTINGSREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.security_settings_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.CreateSecuritySettingsRequest)
  })
_sym_db.RegisterMessage(CreateSecuritySettingsRequest)

DeleteSecuritySettingsRequest = _reflection.GeneratedProtocolMessageType('DeleteSecuritySettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESECURITYSETTINGSREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.security_settings_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.DeleteSecuritySettingsRequest)
  })
_sym_db.RegisterMessage(DeleteSecuritySettingsRequest)

SecuritySettings = _reflection.GeneratedProtocolMessageType('SecuritySettings', (_message.Message,), {

  'InsightsExportSettings' : _reflection.GeneratedProtocolMessageType('InsightsExportSettings', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYSETTINGS_INSIGHTSEXPORTSETTINGS,
    '__module__' : 'google.cloud.dialogflow.cx.v3.security_settings_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.SecuritySettings.InsightsExportSettings)
    })
  ,
  'DESCRIPTOR' : _SECURITYSETTINGS,
  '__module__' : 'google.cloud.dialogflow.cx.v3.security_settings_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.SecuritySettings)
  })
_sym_db.RegisterMessage(SecuritySettings)
_sym_db.RegisterMessage(SecuritySettings.InsightsExportSettings)

_SECURITYSETTINGSSERVICE = DESCRIPTOR.services_by_name['SecuritySettingsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\025SecuritySettingsProtoP\001Z?google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3;cx\370\001\001\242\002\002DF\252\002\035Google.Cloud.Dialogflow.Cx.V3\352\002!Google::Cloud::Dialogflow::CX::V3\352A\310\001\n\"dlp.googleapis.com/InspectTemplate\022Uorganizations/{organization}/locations/{location}/inspectTemplates/{inspect_template}\022Kprojects/{project}/locations/{location}/inspectTemplates/{inspect_template}\352A\327\001\n%dlp.googleapis.com/DeidentifyTemplate\022[organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}\022Qprojects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}'
  _GETSECURITYSETTINGSREQUEST.fields_by_name['name']._options = None
  _GETSECURITYSETTINGSREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A,\n*dialogflow.googleapis.com/SecuritySettings'
  _UPDATESECURITYSETTINGSREQUEST.fields_by_name['security_settings']._options = None
  _UPDATESECURITYSETTINGSREQUEST.fields_by_name['security_settings']._serialized_options = b'\342A\001\002'
  _UPDATESECURITYSETTINGSREQUEST.fields_by_name['update_mask']._options = None
  _UPDATESECURITYSETTINGSREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _LISTSECURITYSETTINGSREQUEST.fields_by_name['parent']._options = None
  _LISTSECURITYSETTINGSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A,\022*dialogflow.googleapis.com/SecuritySettings'
  _CREATESECURITYSETTINGSREQUEST.fields_by_name['parent']._options = None
  _CREATESECURITYSETTINGSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A,\022*dialogflow.googleapis.com/SecuritySettings'
  _CREATESECURITYSETTINGSREQUEST.fields_by_name['security_settings']._options = None
  _CREATESECURITYSETTINGSREQUEST.fields_by_name['security_settings']._serialized_options = b'\342A\001\002'
  _DELETESECURITYSETTINGSREQUEST.fields_by_name['name']._options = None
  _DELETESECURITYSETTINGSREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A,\n*dialogflow.googleapis.com/SecuritySettings'
  _SECURITYSETTINGS.fields_by_name['display_name']._options = None
  _SECURITYSETTINGS.fields_by_name['display_name']._serialized_options = b'\342A\001\002'
  _SECURITYSETTINGS.fields_by_name['inspect_template']._options = None
  _SECURITYSETTINGS.fields_by_name['inspect_template']._serialized_options = b'\372A$\n\"dlp.googleapis.com/InspectTemplate'
  _SECURITYSETTINGS.fields_by_name['deidentify_template']._options = None
  _SECURITYSETTINGS.fields_by_name['deidentify_template']._serialized_options = b'\372A\'\n%dlp.googleapis.com/DeidentifyTemplate'
  _SECURITYSETTINGS._options = None
  _SECURITYSETTINGS._serialized_options = b'\352Az\n*dialogflow.googleapis.com/SecuritySettings\022Lprojects/{project}/locations/{location}/securitySettings/{security_settings}'
  _SECURITYSETTINGSSERVICE._options = None
  _SECURITYSETTINGSSERVICE._serialized_options = b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
  _SECURITYSETTINGSSERVICE.methods_by_name['CreateSecuritySettings']._options = None
  _SECURITYSETTINGSSERVICE.methods_by_name['CreateSecuritySettings']._serialized_options = b'\332A\030parent,security_settings\202\323\344\223\002I\"4/v3/{parent=projects/*/locations/*}/securitySettings:\021security_settings'
  _SECURITYSETTINGSSERVICE.methods_by_name['GetSecuritySettings']._options = None
  _SECURITYSETTINGSSERVICE.methods_by_name['GetSecuritySettings']._serialized_options = b'\332A\004name\202\323\344\223\0026\0224/v3/{name=projects/*/locations/*/securitySettings/*}'
  _SECURITYSETTINGSSERVICE.methods_by_name['UpdateSecuritySettings']._options = None
  _SECURITYSETTINGSSERVICE.methods_by_name['UpdateSecuritySettings']._serialized_options = b'\332A\035security_settings,update_mask\202\323\344\223\002[2F/v3/{security_settings.name=projects/*/locations/*/securitySettings/*}:\021security_settings'
  _SECURITYSETTINGSSERVICE.methods_by_name['ListSecuritySettings']._options = None
  _SECURITYSETTINGSSERVICE.methods_by_name['ListSecuritySettings']._serialized_options = b'\332A\006parent\202\323\344\223\0026\0224/v3/{parent=projects/*/locations/*}/securitySettings'
  _SECURITYSETTINGSSERVICE.methods_by_name['DeleteSecuritySettings']._options = None
  _SECURITYSETTINGSSERVICE.methods_by_name['DeleteSecuritySettings']._serialized_options = b'\332A\004name\202\323\344\223\0026*4/v3/{name=projects/*/locations/*/securitySettings/*}'
  _GETSECURITYSETTINGSREQUEST._serialized_start=303
  _GETSECURITYSETTINGSREQUEST._serialized_end=404
  _UPDATESECURITYSETTINGSREQUEST._serialized_start=407
  _UPDATESECURITYSETTINGSREQUEST._serialized_end=605
  _LISTSECURITYSETTINGSREQUEST._serialized_start=608
  _LISTSECURITYSETTINGSREQUEST._serialized_end=774
  _LISTSECURITYSETTINGSRESPONSE._serialized_start=777
  _LISTSECURITYSETTINGSRESPONSE._serialized_end=941
  _CREATESECURITYSETTINGSREQUEST._serialized_start=944
  _CREATESECURITYSETTINGSREQUEST._serialized_end=1152
  _DELETESECURITYSETTINGSREQUEST._serialized_start=1154
  _DELETESECURITYSETTINGSREQUEST._serialized_end=1258
  _SECURITYSETTINGS._serialized_start=1261
  _SECURITYSETTINGS._serialized_end=2483
  _SECURITYSETTINGS_INSIGHTSEXPORTSETTINGS._serialized_start=2028
  _SECURITYSETTINGS_INSIGHTSEXPORTSETTINGS._serialized_end=2106
  _SECURITYSETTINGS_REDACTIONSTRATEGY._serialized_start=2108
  _SECURITYSETTINGS_REDACTIONSTRATEGY._serialized_end=2188
  _SECURITYSETTINGS_REDACTIONSCOPE._serialized_start=2190
  _SECURITYSETTINGS_REDACTIONSCOPE._serialized_end=2264
  _SECURITYSETTINGS_PURGEDATATYPE._serialized_start=2266
  _SECURITYSETTINGS_PURGEDATATYPE._serialized_end=2338
  _SECURITYSETTINGSSERVICE._serialized_start=2486
  _SECURITYSETTINGSSERVICE._serialized_end=3749
# @@protoc_insertion_point(module_scope)
