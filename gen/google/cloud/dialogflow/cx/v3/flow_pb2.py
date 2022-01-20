# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/cx/v3/flow.proto
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
from google.cloud.dialogflow.cx.v3 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_advanced__settings__pb2
from google.cloud.dialogflow.cx.v3 import page_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_page__pb2
from google.cloud.dialogflow.cx.v3 import validation_message_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_validation__message__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/dialogflow/cx/v3/flow.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x35google/cloud/dialogflow/cx/v3/advanced_settings.proto\x1a(google/cloud/dialogflow/cx/v3/page.proto\x1a\x36google/cloud/dialogflow/cx/v3/validation_message.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe3\x03\n\x0bNluSettings\x12S\n\nmodel_type\x18\x01 \x01(\x0e\x32\x34.google.cloud.dialogflow.cx.v3.NluSettings.ModelTypeR\tmodelType\x12\x39\n\x18\x63lassification_threshold\x18\x03 \x01(\x02R\x17\x63lassificationThreshold\x12l\n\x13model_training_mode\x18\x04 \x01(\x0e\x32<.google.cloud.dialogflow.cx.v3.NluSettings.ModelTrainingModeR\x11modelTrainingMode\"Y\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13MODEL_TYPE_STANDARD\x10\x01\x12\x17\n\x13MODEL_TYPE_ADVANCED\x10\x03\"{\n\x11ModelTrainingMode\x12#\n\x1fMODEL_TRAINING_MODE_UNSPECIFIED\x10\x00\x12!\n\x1dMODEL_TRAINING_MODE_AUTOMATIC\x10\x01\x12\x1e\n\x1aMODEL_TRAINING_MODE_MANUAL\x10\x02\"\xbc\x04\n\x04\x46low\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x64isplayName\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12[\n\x11transition_routes\x18\x04 \x03(\x0b\x32..google.cloud.dialogflow.cx.v3.TransitionRouteR\x10transitionRoutes\x12R\n\x0e\x65vent_handlers\x18\n \x03(\x0b\x32+.google.cloud.dialogflow.cx.v3.EventHandlerR\reventHandlers\x12k\n\x17transition_route_groups\x18\x0f \x03(\tB3\xfa\x41\x30\n.dialogflow.googleapis.com/TransitionRouteGroupR\x15transitionRouteGroups\x12M\n\x0cnlu_settings\x18\x0b \x01(\x0b\x32*.google.cloud.dialogflow.cx.v3.NluSettingsR\x0bnluSettings:h\xea\x41\x65\n\x1e\x64ialogflow.googleapis.com/Flow\x12\x43projects/{project}/locations/{location}/agents/{agent}/flows/{flow}\"\xb8\x01\n\x11\x43reateFlowRequest\x12?\n\x06parent\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \x12\x1e\x64ialogflow.googleapis.com/FlowR\x06parent\x12=\n\x04\x66low\x18\x02 \x01(\x0b\x32#.google.cloud.dialogflow.cx.v3.FlowB\x04\xe2\x41\x01\x02R\x04\x66low\x12#\n\rlanguage_code\x18\x03 \x01(\tR\x0clanguageCode\"f\n\x11\x44\x65leteFlowRequest\x12;\n\x04name\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \n\x1e\x64ialogflow.googleapis.com/FlowR\x04name\x12\x14\n\x05\x66orce\x18\x02 \x01(\x08R\x05\x66orce\"\xb4\x01\n\x10ListFlowsRequest\x12?\n\x06parent\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \x12\x1e\x64ialogflow.googleapis.com/FlowR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12#\n\rlanguage_code\x18\x04 \x01(\tR\x0clanguageCode\"v\n\x11ListFlowsResponse\x12\x39\n\x05\x66lows\x18\x01 \x03(\x0b\x32#.google.cloud.dialogflow.cx.v3.FlowR\x05\x66lows\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"r\n\x0eGetFlowRequest\x12;\n\x04name\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \n\x1e\x64ialogflow.googleapis.com/FlowR\x04name\x12#\n\rlanguage_code\x18\x02 \x01(\tR\x0clanguageCode\"\xb4\x01\n\x11UpdateFlowRequest\x12=\n\x04\x66low\x18\x01 \x01(\x0b\x32#.google.cloud.dialogflow.cx.v3.FlowB\x04\xe2\x41\x01\x02R\x04\x66low\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12#\n\rlanguage_code\x18\x03 \x01(\tR\x0clanguageCode\"O\n\x10TrainFlowRequest\x12;\n\x04name\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \n\x1e\x64ialogflow.googleapis.com/FlowR\x04name\"w\n\x13ValidateFlowRequest\x12;\n\x04name\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \n\x1e\x64ialogflow.googleapis.com/FlowR\x04name\x12#\n\rlanguage_code\x18\x02 \x01(\tR\x0clanguageCode\"\x92\x01\n\x1eGetFlowValidationResultRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.dialogflow.googleapis.com/FlowValidationResultR\x04name\x12#\n\rlanguage_code\x18\x02 \x01(\tR\x0clanguageCode\"\xd7\x02\n\x14\x46lowValidationResult\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x61\n\x13validation_messages\x18\x02 \x03(\x0b\x32\x30.google.cloud.dialogflow.cx.v3.ValidationMessageR\x12validationMessages\x12;\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime:\x8a\x01\xea\x41\x86\x01\n.dialogflow.googleapis.com/FlowValidationResult\x12Tprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/validationResult\"\xc9\x02\n\x11ImportFlowRequest\x12?\n\x06parent\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \x12\x1e\x64ialogflow.googleapis.com/FlowR\x06parent\x12\x1b\n\x08\x66low_uri\x18\x02 \x01(\tH\x00R\x07\x66lowUri\x12#\n\x0c\x66low_content\x18\x03 \x01(\x0cH\x00R\x0b\x66lowContent\x12\x62\n\rimport_option\x18\x04 \x01(\x0e\x32=.google.cloud.dialogflow.cx.v3.ImportFlowRequest.ImportOptionR\x0cimportOption\"E\n\x0cImportOption\x12\x1d\n\x19IMPORT_OPTION_UNSPECIFIED\x10\x00\x12\x08\n\x04KEEP\x10\x01\x12\x0c\n\x08\x46\x41LLBACK\x10\x02\x42\x06\n\x04\x66low\"M\n\x12ImportFlowResponse\x12\x37\n\x04\x66low\x18\x01 \x01(\tB#\xfa\x41 \n\x1e\x64ialogflow.googleapis.com/FlowR\x04\x66low\"\xb1\x01\n\x11\x45xportFlowRequest\x12;\n\x04name\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \n\x1e\x64ialogflow.googleapis.com/FlowR\x04name\x12\x1f\n\x08\x66low_uri\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\x07\x66lowUri\x12>\n\x18include_referenced_flows\x18\x04 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x16includeReferencedFlows\"^\n\x12\x45xportFlowResponse\x12\x1b\n\x08\x66low_uri\x18\x01 \x01(\tH\x00R\x07\x66lowUri\x12#\n\x0c\x66low_content\x18\x02 \x01(\x0cH\x00R\x0b\x66lowContentB\x06\n\x04\x66low2\x98\x10\n\x05\x46lows\x12\xb3\x01\n\nCreateFlow\x12\x30.google.cloud.dialogflow.cx.v3.CreateFlowRequest\x1a#.google.cloud.dialogflow.cx.v3.Flow\"N\xda\x41\x0bparent,flow\x82\xd3\xe4\x93\x02:\"2/v3/{parent=projects/*/locations/*/agents/*}/flows:\x04\x66low\x12\x99\x01\n\nDeleteFlow\x12\x30.google.cloud.dialogflow.cx.v3.DeleteFlowRequest\x1a\x16.google.protobuf.Empty\"A\xda\x41\x04name\x82\xd3\xe4\x93\x02\x34*2/v3/{name=projects/*/locations/*/agents/*/flows/*}\x12\xb3\x01\n\tListFlows\x12/.google.cloud.dialogflow.cx.v3.ListFlowsRequest\x1a\x30.google.cloud.dialogflow.cx.v3.ListFlowsResponse\"C\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x34\x12\x32/v3/{parent=projects/*/locations/*/agents/*}/flows\x12\xa0\x01\n\x07GetFlow\x12-.google.cloud.dialogflow.cx.v3.GetFlowRequest\x1a#.google.cloud.dialogflow.cx.v3.Flow\"A\xda\x41\x04name\x82\xd3\xe4\x93\x02\x34\x12\x32/v3/{name=projects/*/locations/*/agents/*/flows/*}\x12\xbd\x01\n\nUpdateFlow\x12\x30.google.cloud.dialogflow.cx.v3.UpdateFlowRequest\x1a#.google.cloud.dialogflow.cx.v3.Flow\"X\xda\x41\x10\x66low,update_mask\x82\xd3\xe4\x93\x02?27/v3/{flow.name=projects/*/locations/*/agents/*/flows/*}:\x04\x66low\x12\xd9\x01\n\tTrainFlow\x12/.google.cloud.dialogflow.cx.v3.TrainFlowRequest\x1a\x1d.google.longrunning.Operation\"|\xca\x41/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xda\x41\x04name\x82\xd3\xe4\x93\x02=\"8/v3/{name=projects/*/locations/*/agents/*/flows/*}:train:\x01*\x12\xbf\x01\n\x0cValidateFlow\x12\x32.google.cloud.dialogflow.cx.v3.ValidateFlowRequest\x1a\x33.google.cloud.dialogflow.cx.v3.FlowValidationResult\"F\x82\xd3\xe4\x93\x02@\";/v3/{name=projects/*/locations/*/agents/*/flows/*}:validate:\x01*\x12\xe1\x01\n\x17GetFlowValidationResult\x12=.google.cloud.dialogflow.cx.v3.GetFlowValidationResultRequest\x1a\x33.google.cloud.dialogflow.cx.v3.FlowValidationResult\"R\xda\x41\x04name\x82\xd3\xe4\x93\x02\x45\x12\x43/v3/{name=projects/*/locations/*/agents/*/flows/*/validationResult}\x12\xd2\x01\n\nImportFlow\x12\x30.google.cloud.dialogflow.cx.v3.ImportFlowRequest\x1a\x1d.google.longrunning.Operation\"s\xca\x41,\n\x12ImportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02>\"9/v3/{parent=projects/*/locations/*/agents/*}/flows:import:\x01*\x12\xd2\x01\n\nExportFlow\x12\x30.google.cloud.dialogflow.cx.v3.ExportFlowRequest\x1a\x1d.google.longrunning.Operation\"s\xca\x41,\n\x12\x45xportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02>\"9/v3/{name=projects/*/locations/*/agents/*/flows/*}:export:\x01*\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xbd\x01\n!com.google.cloud.dialogflow.cx.v3B\tFlowProtoP\x01Z?google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3;cx\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')



_NLUSETTINGS = DESCRIPTOR.message_types_by_name['NluSettings']
_FLOW = DESCRIPTOR.message_types_by_name['Flow']
_CREATEFLOWREQUEST = DESCRIPTOR.message_types_by_name['CreateFlowRequest']
_DELETEFLOWREQUEST = DESCRIPTOR.message_types_by_name['DeleteFlowRequest']
_LISTFLOWSREQUEST = DESCRIPTOR.message_types_by_name['ListFlowsRequest']
_LISTFLOWSRESPONSE = DESCRIPTOR.message_types_by_name['ListFlowsResponse']
_GETFLOWREQUEST = DESCRIPTOR.message_types_by_name['GetFlowRequest']
_UPDATEFLOWREQUEST = DESCRIPTOR.message_types_by_name['UpdateFlowRequest']
_TRAINFLOWREQUEST = DESCRIPTOR.message_types_by_name['TrainFlowRequest']
_VALIDATEFLOWREQUEST = DESCRIPTOR.message_types_by_name['ValidateFlowRequest']
_GETFLOWVALIDATIONRESULTREQUEST = DESCRIPTOR.message_types_by_name['GetFlowValidationResultRequest']
_FLOWVALIDATIONRESULT = DESCRIPTOR.message_types_by_name['FlowValidationResult']
_IMPORTFLOWREQUEST = DESCRIPTOR.message_types_by_name['ImportFlowRequest']
_IMPORTFLOWRESPONSE = DESCRIPTOR.message_types_by_name['ImportFlowResponse']
_EXPORTFLOWREQUEST = DESCRIPTOR.message_types_by_name['ExportFlowRequest']
_EXPORTFLOWRESPONSE = DESCRIPTOR.message_types_by_name['ExportFlowResponse']
_NLUSETTINGS_MODELTYPE = _NLUSETTINGS.enum_types_by_name['ModelType']
_NLUSETTINGS_MODELTRAININGMODE = _NLUSETTINGS.enum_types_by_name['ModelTrainingMode']
_IMPORTFLOWREQUEST_IMPORTOPTION = _IMPORTFLOWREQUEST.enum_types_by_name['ImportOption']
NluSettings = _reflection.GeneratedProtocolMessageType('NluSettings', (_message.Message,), {
  'DESCRIPTOR' : _NLUSETTINGS,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.NluSettings)
  })
_sym_db.RegisterMessage(NluSettings)

Flow = _reflection.GeneratedProtocolMessageType('Flow', (_message.Message,), {
  'DESCRIPTOR' : _FLOW,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.Flow)
  })
_sym_db.RegisterMessage(Flow)

CreateFlowRequest = _reflection.GeneratedProtocolMessageType('CreateFlowRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFLOWREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.CreateFlowRequest)
  })
_sym_db.RegisterMessage(CreateFlowRequest)

DeleteFlowRequest = _reflection.GeneratedProtocolMessageType('DeleteFlowRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFLOWREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.DeleteFlowRequest)
  })
_sym_db.RegisterMessage(DeleteFlowRequest)

ListFlowsRequest = _reflection.GeneratedProtocolMessageType('ListFlowsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFLOWSREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ListFlowsRequest)
  })
_sym_db.RegisterMessage(ListFlowsRequest)

ListFlowsResponse = _reflection.GeneratedProtocolMessageType('ListFlowsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFLOWSRESPONSE,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ListFlowsResponse)
  })
_sym_db.RegisterMessage(ListFlowsResponse)

GetFlowRequest = _reflection.GeneratedProtocolMessageType('GetFlowRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFLOWREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.GetFlowRequest)
  })
_sym_db.RegisterMessage(GetFlowRequest)

UpdateFlowRequest = _reflection.GeneratedProtocolMessageType('UpdateFlowRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFLOWREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.UpdateFlowRequest)
  })
_sym_db.RegisterMessage(UpdateFlowRequest)

TrainFlowRequest = _reflection.GeneratedProtocolMessageType('TrainFlowRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAINFLOWREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.TrainFlowRequest)
  })
_sym_db.RegisterMessage(TrainFlowRequest)

ValidateFlowRequest = _reflection.GeneratedProtocolMessageType('ValidateFlowRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATEFLOWREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ValidateFlowRequest)
  })
_sym_db.RegisterMessage(ValidateFlowRequest)

GetFlowValidationResultRequest = _reflection.GeneratedProtocolMessageType('GetFlowValidationResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFLOWVALIDATIONRESULTREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.GetFlowValidationResultRequest)
  })
_sym_db.RegisterMessage(GetFlowValidationResultRequest)

FlowValidationResult = _reflection.GeneratedProtocolMessageType('FlowValidationResult', (_message.Message,), {
  'DESCRIPTOR' : _FLOWVALIDATIONRESULT,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.FlowValidationResult)
  })
_sym_db.RegisterMessage(FlowValidationResult)

ImportFlowRequest = _reflection.GeneratedProtocolMessageType('ImportFlowRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTFLOWREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ImportFlowRequest)
  })
_sym_db.RegisterMessage(ImportFlowRequest)

ImportFlowResponse = _reflection.GeneratedProtocolMessageType('ImportFlowResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTFLOWRESPONSE,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ImportFlowResponse)
  })
_sym_db.RegisterMessage(ImportFlowResponse)

ExportFlowRequest = _reflection.GeneratedProtocolMessageType('ExportFlowRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTFLOWREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ExportFlowRequest)
  })
_sym_db.RegisterMessage(ExportFlowRequest)

ExportFlowResponse = _reflection.GeneratedProtocolMessageType('ExportFlowResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTFLOWRESPONSE,
  '__module__' : 'google.cloud.dialogflow.cx.v3.flow_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ExportFlowResponse)
  })
_sym_db.RegisterMessage(ExportFlowResponse)

_FLOWS = DESCRIPTOR.services_by_name['Flows']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\tFlowProtoP\001Z?google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3;cx\370\001\001\242\002\002DF\252\002\035Google.Cloud.Dialogflow.Cx.V3\352\002!Google::Cloud::Dialogflow::CX::V3'
  _FLOW.fields_by_name['display_name']._options = None
  _FLOW.fields_by_name['display_name']._serialized_options = b'\342A\001\002'
  _FLOW.fields_by_name['transition_route_groups']._options = None
  _FLOW.fields_by_name['transition_route_groups']._serialized_options = b'\372A0\n.dialogflow.googleapis.com/TransitionRouteGroup'
  _FLOW._options = None
  _FLOW._serialized_options = b'\352Ae\n\036dialogflow.googleapis.com/Flow\022Cprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}'
  _CREATEFLOWREQUEST.fields_by_name['parent']._options = None
  _CREATEFLOWREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A \022\036dialogflow.googleapis.com/Flow'
  _CREATEFLOWREQUEST.fields_by_name['flow']._options = None
  _CREATEFLOWREQUEST.fields_by_name['flow']._serialized_options = b'\342A\001\002'
  _DELETEFLOWREQUEST.fields_by_name['name']._options = None
  _DELETEFLOWREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A \n\036dialogflow.googleapis.com/Flow'
  _LISTFLOWSREQUEST.fields_by_name['parent']._options = None
  _LISTFLOWSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A \022\036dialogflow.googleapis.com/Flow'
  _GETFLOWREQUEST.fields_by_name['name']._options = None
  _GETFLOWREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A \n\036dialogflow.googleapis.com/Flow'
  _UPDATEFLOWREQUEST.fields_by_name['flow']._options = None
  _UPDATEFLOWREQUEST.fields_by_name['flow']._serialized_options = b'\342A\001\002'
  _TRAINFLOWREQUEST.fields_by_name['name']._options = None
  _TRAINFLOWREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A \n\036dialogflow.googleapis.com/Flow'
  _VALIDATEFLOWREQUEST.fields_by_name['name']._options = None
  _VALIDATEFLOWREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A \n\036dialogflow.googleapis.com/Flow'
  _GETFLOWVALIDATIONRESULTREQUEST.fields_by_name['name']._options = None
  _GETFLOWVALIDATIONRESULTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A0\n.dialogflow.googleapis.com/FlowValidationResult'
  _FLOWVALIDATIONRESULT._options = None
  _FLOWVALIDATIONRESULT._serialized_options = b'\352A\206\001\n.dialogflow.googleapis.com/FlowValidationResult\022Tprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/validationResult'
  _IMPORTFLOWREQUEST.fields_by_name['parent']._options = None
  _IMPORTFLOWREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A \022\036dialogflow.googleapis.com/Flow'
  _IMPORTFLOWRESPONSE.fields_by_name['flow']._options = None
  _IMPORTFLOWRESPONSE.fields_by_name['flow']._serialized_options = b'\372A \n\036dialogflow.googleapis.com/Flow'
  _EXPORTFLOWREQUEST.fields_by_name['name']._options = None
  _EXPORTFLOWREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A \n\036dialogflow.googleapis.com/Flow'
  _EXPORTFLOWREQUEST.fields_by_name['flow_uri']._options = None
  _EXPORTFLOWREQUEST.fields_by_name['flow_uri']._serialized_options = b'\342A\001\001'
  _EXPORTFLOWREQUEST.fields_by_name['include_referenced_flows']._options = None
  _EXPORTFLOWREQUEST.fields_by_name['include_referenced_flows']._serialized_options = b'\342A\001\001'
  _FLOWS._options = None
  _FLOWS._serialized_options = b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
  _FLOWS.methods_by_name['CreateFlow']._options = None
  _FLOWS.methods_by_name['CreateFlow']._serialized_options = b'\332A\013parent,flow\202\323\344\223\002:\"2/v3/{parent=projects/*/locations/*/agents/*}/flows:\004flow'
  _FLOWS.methods_by_name['DeleteFlow']._options = None
  _FLOWS.methods_by_name['DeleteFlow']._serialized_options = b'\332A\004name\202\323\344\223\0024*2/v3/{name=projects/*/locations/*/agents/*/flows/*}'
  _FLOWS.methods_by_name['ListFlows']._options = None
  _FLOWS.methods_by_name['ListFlows']._serialized_options = b'\332A\006parent\202\323\344\223\0024\0222/v3/{parent=projects/*/locations/*/agents/*}/flows'
  _FLOWS.methods_by_name['GetFlow']._options = None
  _FLOWS.methods_by_name['GetFlow']._serialized_options = b'\332A\004name\202\323\344\223\0024\0222/v3/{name=projects/*/locations/*/agents/*/flows/*}'
  _FLOWS.methods_by_name['UpdateFlow']._options = None
  _FLOWS.methods_by_name['UpdateFlow']._serialized_options = b'\332A\020flow,update_mask\202\323\344\223\002?27/v3/{flow.name=projects/*/locations/*/agents/*/flows/*}:\004flow'
  _FLOWS.methods_by_name['TrainFlow']._options = None
  _FLOWS.methods_by_name['TrainFlow']._serialized_options = b'\312A/\n\025google.protobuf.Empty\022\026google.protobuf.Struct\332A\004name\202\323\344\223\002=\"8/v3/{name=projects/*/locations/*/agents/*/flows/*}:train:\001*'
  _FLOWS.methods_by_name['ValidateFlow']._options = None
  _FLOWS.methods_by_name['ValidateFlow']._serialized_options = b'\202\323\344\223\002@\";/v3/{name=projects/*/locations/*/agents/*/flows/*}:validate:\001*'
  _FLOWS.methods_by_name['GetFlowValidationResult']._options = None
  _FLOWS.methods_by_name['GetFlowValidationResult']._serialized_options = b'\332A\004name\202\323\344\223\002E\022C/v3/{name=projects/*/locations/*/agents/*/flows/*/validationResult}'
  _FLOWS.methods_by_name['ImportFlow']._options = None
  _FLOWS.methods_by_name['ImportFlow']._serialized_options = b'\312A,\n\022ImportFlowResponse\022\026google.protobuf.Struct\202\323\344\223\002>\"9/v3/{parent=projects/*/locations/*/agents/*}/flows:import:\001*'
  _FLOWS.methods_by_name['ExportFlow']._options = None
  _FLOWS.methods_by_name['ExportFlow']._serialized_options = b'\312A,\n\022ExportFlowResponse\022\026google.protobuf.Struct\202\323\344\223\002>\"9/v3/{name=projects/*/locations/*/agents/*/flows/*}:export:\001*'
  _NLUSETTINGS._serialized_start=477
  _NLUSETTINGS._serialized_end=960
  _NLUSETTINGS_MODELTYPE._serialized_start=746
  _NLUSETTINGS_MODELTYPE._serialized_end=835
  _NLUSETTINGS_MODELTRAININGMODE._serialized_start=837
  _NLUSETTINGS_MODELTRAININGMODE._serialized_end=960
  _FLOW._serialized_start=963
  _FLOW._serialized_end=1535
  _CREATEFLOWREQUEST._serialized_start=1538
  _CREATEFLOWREQUEST._serialized_end=1722
  _DELETEFLOWREQUEST._serialized_start=1724
  _DELETEFLOWREQUEST._serialized_end=1826
  _LISTFLOWSREQUEST._serialized_start=1829
  _LISTFLOWSREQUEST._serialized_end=2009
  _LISTFLOWSRESPONSE._serialized_start=2011
  _LISTFLOWSRESPONSE._serialized_end=2129
  _GETFLOWREQUEST._serialized_start=2131
  _GETFLOWREQUEST._serialized_end=2245
  _UPDATEFLOWREQUEST._serialized_start=2248
  _UPDATEFLOWREQUEST._serialized_end=2428
  _TRAINFLOWREQUEST._serialized_start=2430
  _TRAINFLOWREQUEST._serialized_end=2509
  _VALIDATEFLOWREQUEST._serialized_start=2511
  _VALIDATEFLOWREQUEST._serialized_end=2630
  _GETFLOWVALIDATIONRESULTREQUEST._serialized_start=2633
  _GETFLOWVALIDATIONRESULTREQUEST._serialized_end=2779
  _FLOWVALIDATIONRESULT._serialized_start=2782
  _FLOWVALIDATIONRESULT._serialized_end=3125
  _IMPORTFLOWREQUEST._serialized_start=3128
  _IMPORTFLOWREQUEST._serialized_end=3457
  _IMPORTFLOWREQUEST_IMPORTOPTION._serialized_start=3380
  _IMPORTFLOWREQUEST_IMPORTOPTION._serialized_end=3449
  _IMPORTFLOWRESPONSE._serialized_start=3459
  _IMPORTFLOWRESPONSE._serialized_end=3536
  _EXPORTFLOWREQUEST._serialized_start=3539
  _EXPORTFLOWREQUEST._serialized_end=3716
  _EXPORTFLOWRESPONSE._serialized_start=3718
  _EXPORTFLOWRESPONSE._serialized_end=3812
  _FLOWS._serialized_start=3815
  _FLOWS._serialized_end=5887
# @@protoc_insertion_point(module_scope)
