# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/model_service.proto
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
from google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from google.cloud.aiplatform.v1beta1 import model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__pb2
from google.cloud.aiplatform.v1beta1 import model_evaluation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__evaluation__pb2
from google.cloud.aiplatform.v1beta1 import model_evaluation_slice_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__evaluation__slice__pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1beta1/model_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a+google/cloud/aiplatform/v1beta1/model.proto\x1a\x36google/cloud/aiplatform/v1beta1/model_evaluation.proto\x1a<google/cloud/aiplatform/v1beta1/model_evaluation_slice.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\"\x9c\x01\n\x12UploadModelRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x42\n\x05model\x18\x02 \x01(\x0b\x32&.google.cloud.aiplatform.v1beta1.ModelB\x04\xe2\x41\x01\x02R\x05model\"\x84\x01\n\x1cUploadModelOperationMetadata\x12\x64\n\x10generic_metadata\x18\x01 \x01(\x0b\x32\x39.google.cloud.aiplatform.v1beta1.GenericOperationMetadataR\x0fgenericMetadata\"Q\n\x13UploadModelResponse\x12:\n\x05model\x18\x01 \x01(\tB$\xfa\x41!\n\x1f\x61iplatform.googleapis.com/ModelR\x05model\"O\n\x0fGetModelRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/ModelR\x04name\"\xe4\x01\n\x11ListModelsRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x37\n\tread_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\"|\n\x12ListModelsResponse\x12>\n\x06models\x18\x01 \x03(\x0b\x32&.google.cloud.aiplatform.v1beta1.ModelR\x06models\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\x9b\x01\n\x12UpdateModelRequest\x12\x42\n\x05model\x18\x01 \x01(\x0b\x32&.google.cloud.aiplatform.v1beta1.ModelB\x04\xe2\x41\x01\x02R\x05model\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"R\n\x12\x44\x65leteModelRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/ModelR\x04name\"\xca\x03\n\x12\x45xportModelRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/ModelR\x04name\x12k\n\routput_config\x18\x02 \x01(\x0b\x32@.google.cloud.aiplatform.v1beta1.ExportModelRequest.OutputConfigB\x04\xe2\x41\x01\x02R\x0coutputConfig\x1a\x88\x02\n\x0cOutputConfig\x12(\n\x10\x65xport_format_id\x18\x01 \x01(\tR\x0e\x65xportFormatId\x12\x62\n\x14\x61rtifact_destination\x18\x03 \x01(\x0b\x32/.google.cloud.aiplatform.v1beta1.GcsDestinationR\x13\x61rtifactDestination\x12j\n\x11image_destination\x18\x04 \x01(\x0b\x32=.google.cloud.aiplatform.v1beta1.ContainerRegistryDestinationR\x10imageDestination\"\xe9\x02\n\x1c\x45xportModelOperationMetadata\x12\x64\n\x10generic_metadata\x18\x01 \x01(\x0b\x32\x39.google.cloud.aiplatform.v1beta1.GenericOperationMetadataR\x0fgenericMetadata\x12o\n\x0boutput_info\x18\x02 \x01(\x0b\x32H.google.cloud.aiplatform.v1beta1.ExportModelOperationMetadata.OutputInfoB\x04\xe2\x41\x01\x03R\noutputInfo\x1ar\n\nOutputInfo\x12\x34\n\x13\x61rtifact_output_uri\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x11\x61rtifactOutputUri\x12.\n\x10image_output_uri\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x0eimageOutputUri\"\x15\n\x13\x45xportModelResponse\"c\n\x19GetModelEvaluationRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)aiplatform.googleapis.com/ModelEvaluationR\x04name\"\xec\x01\n\x1bListModelEvaluationsRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/ModelR\x06parent\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x37\n\tread_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\"\xa5\x01\n\x1cListModelEvaluationsResponse\x12]\n\x11model_evaluations\x18\x01 \x03(\x0b\x32\x30.google.cloud.aiplatform.v1beta1.ModelEvaluationR\x10modelEvaluations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"m\n\x1eGetModelEvaluationSliceRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.aiplatform.googleapis.com/ModelEvaluationSliceR\x04name\"\xfb\x01\n ListModelEvaluationSlicesRequest\x12J\n\x06parent\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)aiplatform.googleapis.com/ModelEvaluationR\x06parent\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x37\n\tread_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\"\xba\x01\n!ListModelEvaluationSlicesResponse\x12m\n\x17model_evaluation_slices\x18\x01 \x03(\x0b\x32\x35.google.cloud.aiplatform.v1beta1.ModelEvaluationSliceR\x15modelEvaluationSlices\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken2\xde\x11\n\x0cModelService\x12\xea\x01\n\x0bUploadModel\x12\x33.google.cloud.aiplatform.v1beta1.UploadModelRequest\x1a\x1d.google.longrunning.Operation\"\x86\x01\xca\x41\x33\n\x13UploadModelResponse\x12\x1cUploadModelOperationMetadata\xda\x41\x0cparent,model\x82\xd3\xe4\x93\x02;\"6/v1beta1/{parent=projects/*/locations/*}/models:upload:\x01*\x12\xa4\x01\n\x08GetModel\x12\x30.google.cloud.aiplatform.v1beta1.GetModelRequest\x1a&.google.cloud.aiplatform.v1beta1.Model\">\xda\x41\x04name\x82\xd3\xe4\x93\x02\x31\x12//v1beta1/{name=projects/*/locations/*/models/*}\x12\xb7\x01\n\nListModels\x12\x32.google.cloud.aiplatform.v1beta1.ListModelsRequest\x1a\x33.google.cloud.aiplatform.v1beta1.ListModelsResponse\"@\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x31\x12//v1beta1/{parent=projects/*/locations/*}/models\x12\xc4\x01\n\x0bUpdateModel\x12\x33.google.cloud.aiplatform.v1beta1.UpdateModelRequest\x1a&.google.cloud.aiplatform.v1beta1.Model\"X\xda\x41\x11model,update_mask\x82\xd3\xe4\x93\x02>25/v1beta1/{model.name=projects/*/locations/*/models/*}:\x05model\x12\xd4\x01\n\x0b\x44\x65leteModel\x12\x33.google.cloud.aiplatform.v1beta1.DeleteModelRequest\x1a\x1d.google.longrunning.Operation\"q\xca\x41\x30\n\x15google.protobuf.Empty\x12\x17\x44\x65leteOperationMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02\x31*//v1beta1/{name=projects/*/locations/*/models/*}\x12\xf0\x01\n\x0b\x45xportModel\x12\x33.google.cloud.aiplatform.v1beta1.ExportModelRequest\x1a\x1d.google.longrunning.Operation\"\x8c\x01\xca\x41\x33\n\x13\x45xportModelResponse\x12\x1c\x45xportModelOperationMetadata\xda\x41\x12name,output_config\x82\xd3\xe4\x93\x02;\"6/v1beta1/{name=projects/*/locations/*/models/*}:export:\x01*\x12\xd0\x01\n\x12GetModelEvaluation\x12:.google.cloud.aiplatform.v1beta1.GetModelEvaluationRequest\x1a\x30.google.cloud.aiplatform.v1beta1.ModelEvaluation\"L\xda\x41\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*}\x12\xe3\x01\n\x14ListModelEvaluations\x12<.google.cloud.aiplatform.v1beta1.ListModelEvaluationsRequest\x1a=.google.cloud.aiplatform.v1beta1.ListModelEvaluationsResponse\"N\xda\x41\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{parent=projects/*/locations/*/models/*}/evaluations\x12\xe8\x01\n\x17GetModelEvaluationSlice\x12?.google.cloud.aiplatform.v1beta1.GetModelEvaluationSliceRequest\x1a\x35.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice\"U\xda\x41\x04name\x82\xd3\xe4\x93\x02H\x12\x46/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/slices/*}\x12\xfb\x01\n\x19ListModelEvaluationSlices\x12\x41.google.cloud.aiplatform.v1beta1.ListModelEvaluationSlicesRequest\x1a\x42.google.cloud.aiplatform.v1beta1.ListModelEvaluationSlicesResponse\"W\xda\x41\x06parent\x82\xd3\xe4\x93\x02H\x12\x46/v1beta1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices\x1aM\xca\x41\x19\x61iplatform.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xee\x01\n#com.google.cloud.aiplatform.v1beta1B\x11ModelServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02\"Google::Cloud::AIPlatform::V1beta1b\x06proto3')



_UPLOADMODELREQUEST = DESCRIPTOR.message_types_by_name['UploadModelRequest']
_UPLOADMODELOPERATIONMETADATA = DESCRIPTOR.message_types_by_name['UploadModelOperationMetadata']
_UPLOADMODELRESPONSE = DESCRIPTOR.message_types_by_name['UploadModelResponse']
_GETMODELREQUEST = DESCRIPTOR.message_types_by_name['GetModelRequest']
_LISTMODELSREQUEST = DESCRIPTOR.message_types_by_name['ListModelsRequest']
_LISTMODELSRESPONSE = DESCRIPTOR.message_types_by_name['ListModelsResponse']
_UPDATEMODELREQUEST = DESCRIPTOR.message_types_by_name['UpdateModelRequest']
_DELETEMODELREQUEST = DESCRIPTOR.message_types_by_name['DeleteModelRequest']
_EXPORTMODELREQUEST = DESCRIPTOR.message_types_by_name['ExportModelRequest']
_EXPORTMODELREQUEST_OUTPUTCONFIG = _EXPORTMODELREQUEST.nested_types_by_name['OutputConfig']
_EXPORTMODELOPERATIONMETADATA = DESCRIPTOR.message_types_by_name['ExportModelOperationMetadata']
_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO = _EXPORTMODELOPERATIONMETADATA.nested_types_by_name['OutputInfo']
_EXPORTMODELRESPONSE = DESCRIPTOR.message_types_by_name['ExportModelResponse']
_GETMODELEVALUATIONREQUEST = DESCRIPTOR.message_types_by_name['GetModelEvaluationRequest']
_LISTMODELEVALUATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListModelEvaluationsRequest']
_LISTMODELEVALUATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListModelEvaluationsResponse']
_GETMODELEVALUATIONSLICEREQUEST = DESCRIPTOR.message_types_by_name['GetModelEvaluationSliceRequest']
_LISTMODELEVALUATIONSLICESREQUEST = DESCRIPTOR.message_types_by_name['ListModelEvaluationSlicesRequest']
_LISTMODELEVALUATIONSLICESRESPONSE = DESCRIPTOR.message_types_by_name['ListModelEvaluationSlicesResponse']
UploadModelRequest = _reflection.GeneratedProtocolMessageType('UploadModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMODELREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.UploadModelRequest)
  })
_sym_db.RegisterMessage(UploadModelRequest)

UploadModelOperationMetadata = _reflection.GeneratedProtocolMessageType('UploadModelOperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMODELOPERATIONMETADATA,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.UploadModelOperationMetadata)
  })
_sym_db.RegisterMessage(UploadModelOperationMetadata)

UploadModelResponse = _reflection.GeneratedProtocolMessageType('UploadModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMODELRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.UploadModelResponse)
  })
_sym_db.RegisterMessage(UploadModelResponse)

GetModelRequest = _reflection.GeneratedProtocolMessageType('GetModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.GetModelRequest)
  })
_sym_db.RegisterMessage(GetModelRequest)

ListModelsRequest = _reflection.GeneratedProtocolMessageType('ListModelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELSREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ListModelsRequest)
  })
_sym_db.RegisterMessage(ListModelsRequest)

ListModelsResponse = _reflection.GeneratedProtocolMessageType('ListModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELSRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ListModelsResponse)
  })
_sym_db.RegisterMessage(ListModelsResponse)

UpdateModelRequest = _reflection.GeneratedProtocolMessageType('UpdateModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.UpdateModelRequest)
  })
_sym_db.RegisterMessage(UpdateModelRequest)

DeleteModelRequest = _reflection.GeneratedProtocolMessageType('DeleteModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODELREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.DeleteModelRequest)
  })
_sym_db.RegisterMessage(DeleteModelRequest)

ExportModelRequest = _reflection.GeneratedProtocolMessageType('ExportModelRequest', (_message.Message,), {

  'OutputConfig' : _reflection.GeneratedProtocolMessageType('OutputConfig', (_message.Message,), {
    'DESCRIPTOR' : _EXPORTMODELREQUEST_OUTPUTCONFIG,
    '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ExportModelRequest.OutputConfig)
    })
  ,
  'DESCRIPTOR' : _EXPORTMODELREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ExportModelRequest)
  })
_sym_db.RegisterMessage(ExportModelRequest)
_sym_db.RegisterMessage(ExportModelRequest.OutputConfig)

ExportModelOperationMetadata = _reflection.GeneratedProtocolMessageType('ExportModelOperationMetadata', (_message.Message,), {

  'OutputInfo' : _reflection.GeneratedProtocolMessageType('OutputInfo', (_message.Message,), {
    'DESCRIPTOR' : _EXPORTMODELOPERATIONMETADATA_OUTPUTINFO,
    '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ExportModelOperationMetadata.OutputInfo)
    })
  ,
  'DESCRIPTOR' : _EXPORTMODELOPERATIONMETADATA,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ExportModelOperationMetadata)
  })
_sym_db.RegisterMessage(ExportModelOperationMetadata)
_sym_db.RegisterMessage(ExportModelOperationMetadata.OutputInfo)

ExportModelResponse = _reflection.GeneratedProtocolMessageType('ExportModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTMODELRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ExportModelResponse)
  })
_sym_db.RegisterMessage(ExportModelResponse)

GetModelEvaluationRequest = _reflection.GeneratedProtocolMessageType('GetModelEvaluationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELEVALUATIONREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.GetModelEvaluationRequest)
  })
_sym_db.RegisterMessage(GetModelEvaluationRequest)

ListModelEvaluationsRequest = _reflection.GeneratedProtocolMessageType('ListModelEvaluationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELEVALUATIONSREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ListModelEvaluationsRequest)
  })
_sym_db.RegisterMessage(ListModelEvaluationsRequest)

ListModelEvaluationsResponse = _reflection.GeneratedProtocolMessageType('ListModelEvaluationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELEVALUATIONSRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ListModelEvaluationsResponse)
  })
_sym_db.RegisterMessage(ListModelEvaluationsResponse)

GetModelEvaluationSliceRequest = _reflection.GeneratedProtocolMessageType('GetModelEvaluationSliceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELEVALUATIONSLICEREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.GetModelEvaluationSliceRequest)
  })
_sym_db.RegisterMessage(GetModelEvaluationSliceRequest)

ListModelEvaluationSlicesRequest = _reflection.GeneratedProtocolMessageType('ListModelEvaluationSlicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELEVALUATIONSLICESREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ListModelEvaluationSlicesRequest)
  })
_sym_db.RegisterMessage(ListModelEvaluationSlicesRequest)

ListModelEvaluationSlicesResponse = _reflection.GeneratedProtocolMessageType('ListModelEvaluationSlicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELEVALUATIONSLICESRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1beta1.model_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ListModelEvaluationSlicesResponse)
  })
_sym_db.RegisterMessage(ListModelEvaluationSlicesResponse)

_MODELSERVICE = DESCRIPTOR.services_by_name['ModelService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\021ModelServiceProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\252\002\037Google.Cloud.AIPlatform.V1Beta1\312\002\037Google\\Cloud\\AIPlatform\\V1beta1\352\002\"Google::Cloud::AIPlatform::V1beta1'
  _UPLOADMODELREQUEST.fields_by_name['parent']._options = None
  _UPLOADMODELREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _UPLOADMODELREQUEST.fields_by_name['model']._options = None
  _UPLOADMODELREQUEST.fields_by_name['model']._serialized_options = b'\342A\001\002'
  _UPLOADMODELRESPONSE.fields_by_name['model']._options = None
  _UPLOADMODELRESPONSE.fields_by_name['model']._serialized_options = b'\372A!\n\037aiplatform.googleapis.com/Model'
  _GETMODELREQUEST.fields_by_name['name']._options = None
  _GETMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Model'
  _LISTMODELSREQUEST.fields_by_name['parent']._options = None
  _LISTMODELSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _UPDATEMODELREQUEST.fields_by_name['model']._options = None
  _UPDATEMODELREQUEST.fields_by_name['model']._serialized_options = b'\342A\001\002'
  _UPDATEMODELREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEMODELREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _DELETEMODELREQUEST.fields_by_name['name']._options = None
  _DELETEMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Model'
  _EXPORTMODELREQUEST.fields_by_name['name']._options = None
  _EXPORTMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Model'
  _EXPORTMODELREQUEST.fields_by_name['output_config']._options = None
  _EXPORTMODELREQUEST.fields_by_name['output_config']._serialized_options = b'\342A\001\002'
  _EXPORTMODELOPERATIONMETADATA_OUTPUTINFO.fields_by_name['artifact_output_uri']._options = None
  _EXPORTMODELOPERATIONMETADATA_OUTPUTINFO.fields_by_name['artifact_output_uri']._serialized_options = b'\342A\001\003'
  _EXPORTMODELOPERATIONMETADATA_OUTPUTINFO.fields_by_name['image_output_uri']._options = None
  _EXPORTMODELOPERATIONMETADATA_OUTPUTINFO.fields_by_name['image_output_uri']._serialized_options = b'\342A\001\003'
  _EXPORTMODELOPERATIONMETADATA.fields_by_name['output_info']._options = None
  _EXPORTMODELOPERATIONMETADATA.fields_by_name['output_info']._serialized_options = b'\342A\001\003'
  _GETMODELEVALUATIONREQUEST.fields_by_name['name']._options = None
  _GETMODELEVALUATIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A+\n)aiplatform.googleapis.com/ModelEvaluation'
  _LISTMODELEVALUATIONSREQUEST.fields_by_name['parent']._options = None
  _LISTMODELEVALUATIONSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Model'
  _GETMODELEVALUATIONSLICEREQUEST.fields_by_name['name']._options = None
  _GETMODELEVALUATIONSLICEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A0\n.aiplatform.googleapis.com/ModelEvaluationSlice'
  _LISTMODELEVALUATIONSLICESREQUEST.fields_by_name['parent']._options = None
  _LISTMODELEVALUATIONSLICESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A+\n)aiplatform.googleapis.com/ModelEvaluation'
  _MODELSERVICE._options = None
  _MODELSERVICE._serialized_options = b'\312A\031aiplatform.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _MODELSERVICE.methods_by_name['UploadModel']._options = None
  _MODELSERVICE.methods_by_name['UploadModel']._serialized_options = b'\312A3\n\023UploadModelResponse\022\034UploadModelOperationMetadata\332A\014parent,model\202\323\344\223\002;\"6/v1beta1/{parent=projects/*/locations/*}/models:upload:\001*'
  _MODELSERVICE.methods_by_name['GetModel']._options = None
  _MODELSERVICE.methods_by_name['GetModel']._serialized_options = b'\332A\004name\202\323\344\223\0021\022//v1beta1/{name=projects/*/locations/*/models/*}'
  _MODELSERVICE.methods_by_name['ListModels']._options = None
  _MODELSERVICE.methods_by_name['ListModels']._serialized_options = b'\332A\006parent\202\323\344\223\0021\022//v1beta1/{parent=projects/*/locations/*}/models'
  _MODELSERVICE.methods_by_name['UpdateModel']._options = None
  _MODELSERVICE.methods_by_name['UpdateModel']._serialized_options = b'\332A\021model,update_mask\202\323\344\223\002>25/v1beta1/{model.name=projects/*/locations/*/models/*}:\005model'
  _MODELSERVICE.methods_by_name['DeleteModel']._options = None
  _MODELSERVICE.methods_by_name['DeleteModel']._serialized_options = b'\312A0\n\025google.protobuf.Empty\022\027DeleteOperationMetadata\332A\004name\202\323\344\223\0021*//v1beta1/{name=projects/*/locations/*/models/*}'
  _MODELSERVICE.methods_by_name['ExportModel']._options = None
  _MODELSERVICE.methods_by_name['ExportModel']._serialized_options = b'\312A3\n\023ExportModelResponse\022\034ExportModelOperationMetadata\332A\022name,output_config\202\323\344\223\002;\"6/v1beta1/{name=projects/*/locations/*/models/*}:export:\001*'
  _MODELSERVICE.methods_by_name['GetModelEvaluation']._options = None
  _MODELSERVICE.methods_by_name['GetModelEvaluation']._serialized_options = b'\332A\004name\202\323\344\223\002?\022=/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*}'
  _MODELSERVICE.methods_by_name['ListModelEvaluations']._options = None
  _MODELSERVICE.methods_by_name['ListModelEvaluations']._serialized_options = b'\332A\006parent\202\323\344\223\002?\022=/v1beta1/{parent=projects/*/locations/*/models/*}/evaluations'
  _MODELSERVICE.methods_by_name['GetModelEvaluationSlice']._options = None
  _MODELSERVICE.methods_by_name['GetModelEvaluationSlice']._serialized_options = b'\332A\004name\202\323\344\223\002H\022F/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/slices/*}'
  _MODELSERVICE.methods_by_name['ListModelEvaluationSlices']._options = None
  _MODELSERVICE.methods_by_name['ListModelEvaluationSlices']._serialized_options = b'\332A\006parent\202\323\344\223\002H\022F/v1beta1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices'
  _UPLOADMODELREQUEST._serialized_start=529
  _UPLOADMODELREQUEST._serialized_end=685
  _UPLOADMODELOPERATIONMETADATA._serialized_start=688
  _UPLOADMODELOPERATIONMETADATA._serialized_end=820
  _UPLOADMODELRESPONSE._serialized_start=822
  _UPLOADMODELRESPONSE._serialized_end=903
  _GETMODELREQUEST._serialized_start=905
  _GETMODELREQUEST._serialized_end=984
  _LISTMODELSREQUEST._serialized_start=987
  _LISTMODELSREQUEST._serialized_end=1215
  _LISTMODELSRESPONSE._serialized_start=1217
  _LISTMODELSRESPONSE._serialized_end=1341
  _UPDATEMODELREQUEST._serialized_start=1344
  _UPDATEMODELREQUEST._serialized_end=1499
  _DELETEMODELREQUEST._serialized_start=1501
  _DELETEMODELREQUEST._serialized_end=1583
  _EXPORTMODELREQUEST._serialized_start=1586
  _EXPORTMODELREQUEST._serialized_end=2044
  _EXPORTMODELREQUEST_OUTPUTCONFIG._serialized_start=1780
  _EXPORTMODELREQUEST_OUTPUTCONFIG._serialized_end=2044
  _EXPORTMODELOPERATIONMETADATA._serialized_start=2047
  _EXPORTMODELOPERATIONMETADATA._serialized_end=2408
  _EXPORTMODELOPERATIONMETADATA_OUTPUTINFO._serialized_start=2294
  _EXPORTMODELOPERATIONMETADATA_OUTPUTINFO._serialized_end=2408
  _EXPORTMODELRESPONSE._serialized_start=2410
  _EXPORTMODELRESPONSE._serialized_end=2431
  _GETMODELEVALUATIONREQUEST._serialized_start=2433
  _GETMODELEVALUATIONREQUEST._serialized_end=2532
  _LISTMODELEVALUATIONSREQUEST._serialized_start=2535
  _LISTMODELEVALUATIONSREQUEST._serialized_end=2771
  _LISTMODELEVALUATIONSRESPONSE._serialized_start=2774
  _LISTMODELEVALUATIONSRESPONSE._serialized_end=2939
  _GETMODELEVALUATIONSLICEREQUEST._serialized_start=2941
  _GETMODELEVALUATIONSLICEREQUEST._serialized_end=3050
  _LISTMODELEVALUATIONSLICESREQUEST._serialized_start=3053
  _LISTMODELEVALUATIONSLICESREQUEST._serialized_end=3304
  _LISTMODELEVALUATIONSLICESRESPONSE._serialized_start=3307
  _LISTMODELEVALUATIONSLICESRESPONSE._serialized_end=3493
  _MODELSERVICE._serialized_start=3496
  _MODELSERVICE._serialized_end=5766
# @@protoc_insertion_point(module_scope)
