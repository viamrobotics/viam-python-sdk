# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/retail/v2/prediction_service.proto
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
from google.cloud.retail.v2 import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_user__event__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/retail/v2/prediction_service.proto\x12\x16google.cloud.retail.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\'google/cloud/retail/v2/user_event.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x9b\x04\n\x0ePredictRequest\x12\"\n\tplacement\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tplacement\x12\x46\n\nuser_event\x18\x02 \x01(\x0b\x32!.google.cloud.retail.v2.UserEventB\x04\xe2\x41\x01\x02R\tuserEvent\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x16\n\x06\x66ilter\x18\x05 \x01(\tR\x06\x66ilter\x12#\n\rvalidate_only\x18\x06 \x01(\x08R\x0cvalidateOnly\x12J\n\x06params\x18\x07 \x03(\x0b\x32\x32.google.cloud.retail.v2.PredictRequest.ParamsEntryR\x06params\x12J\n\x06labels\x18\x08 \x03(\x0b\x32\x32.google.cloud.retail.v2.PredictRequest.LabelsEntryR\x06labels\x1aQ\n\x0bParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xb6\x03\n\x0fPredictResponse\x12R\n\x07results\x18\x01 \x03(\x0b\x32\x38.google.cloud.retail.v2.PredictResponse.PredictionResultR\x07results\x12+\n\x11\x61ttribution_token\x18\x02 \x01(\tR\x10\x61ttributionToken\x12\x1f\n\x0bmissing_ids\x18\x03 \x03(\tR\nmissingIds\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\x1a\xdb\x01\n\x10PredictionResult\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x62\n\x08metadata\x18\x02 \x03(\x0b\x32\x46.google.cloud.retail.v2.PredictResponse.PredictionResult.MetadataEntryR\x08metadata\x1aS\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x32\x8e\x02\n\x11PredictionService\x12\xad\x01\n\x07Predict\x12&.google.cloud.retail.v2.PredictRequest\x1a\'.google.cloud.retail.v2.PredictResponse\"Q\x82\xd3\xe4\x93\x02K\"F/v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:predict:\x01*\x1aI\xca\x41\x15retail.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xcb\x01\n\x1a\x63om.google.cloud.retail.v2B\x16PredictionServiceProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/retail/v2;retail\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')



_PREDICTREQUEST = DESCRIPTOR.message_types_by_name['PredictRequest']
_PREDICTREQUEST_PARAMSENTRY = _PREDICTREQUEST.nested_types_by_name['ParamsEntry']
_PREDICTREQUEST_LABELSENTRY = _PREDICTREQUEST.nested_types_by_name['LabelsEntry']
_PREDICTRESPONSE = DESCRIPTOR.message_types_by_name['PredictResponse']
_PREDICTRESPONSE_PREDICTIONRESULT = _PREDICTRESPONSE.nested_types_by_name['PredictionResult']
_PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY = _PREDICTRESPONSE_PREDICTIONRESULT.nested_types_by_name['MetadataEntry']
PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTREQUEST_PARAMSENTRY,
    '__module__' : 'google.cloud.retail.v2.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.PredictRequest.ParamsEntry)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTREQUEST_LABELSENTRY,
    '__module__' : 'google.cloud.retail.v2.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.PredictRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTREQUEST,
  '__module__' : 'google.cloud.retail.v2.prediction_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.PredictRequest)
  })
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.ParamsEntry)
_sym_db.RegisterMessage(PredictRequest.LabelsEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), {

  'PredictionResult' : _reflection.GeneratedProtocolMessageType('PredictionResult', (_message.Message,), {

    'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
      'DESCRIPTOR' : _PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY,
      '__module__' : 'google.cloud.retail.v2.prediction_service_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.PredictResponse.PredictionResult.MetadataEntry)
      })
    ,
    'DESCRIPTOR' : _PREDICTRESPONSE_PREDICTIONRESULT,
    '__module__' : 'google.cloud.retail.v2.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.PredictResponse.PredictionResult)
    })
  ,
  'DESCRIPTOR' : _PREDICTRESPONSE,
  '__module__' : 'google.cloud.retail.v2.prediction_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.PredictResponse)
  })
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.PredictionResult)
_sym_db.RegisterMessage(PredictResponse.PredictionResult.MetadataEntry)

_PREDICTIONSERVICE = DESCRIPTOR.services_by_name['PredictionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.google.cloud.retail.v2B\026PredictionServiceProtoP\001Z<google.golang.org/genproto/googleapis/cloud/retail/v2;retail\242\002\006RETAIL\252\002\026Google.Cloud.Retail.V2\312\002\026Google\\Cloud\\Retail\\V2\352\002\031Google::Cloud::Retail::V2'
  _PREDICTREQUEST_PARAMSENTRY._options = None
  _PREDICTREQUEST_PARAMSENTRY._serialized_options = b'8\001'
  _PREDICTREQUEST_LABELSENTRY._options = None
  _PREDICTREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _PREDICTREQUEST.fields_by_name['placement']._options = None
  _PREDICTREQUEST.fields_by_name['placement']._serialized_options = b'\342A\001\002'
  _PREDICTREQUEST.fields_by_name['user_event']._options = None
  _PREDICTREQUEST.fields_by_name['user_event']._serialized_options = b'\342A\001\002'
  _PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY._options = None
  _PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY._serialized_options = b'8\001'
  _PREDICTIONSERVICE._options = None
  _PREDICTIONSERVICE._serialized_options = b'\312A\025retail.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _PREDICTIONSERVICE.methods_by_name['Predict']._options = None
  _PREDICTIONSERVICE.methods_by_name['Predict']._serialized_options = b'\202\323\344\223\002K\"F/v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:predict:\001*'
  _PREDICTREQUEST._serialized_start=235
  _PREDICTREQUEST._serialized_end=774
  _PREDICTREQUEST_PARAMSENTRY._serialized_start=634
  _PREDICTREQUEST_PARAMSENTRY._serialized_end=715
  _PREDICTREQUEST_LABELSENTRY._serialized_start=717
  _PREDICTREQUEST_LABELSENTRY._serialized_end=774
  _PREDICTRESPONSE._serialized_start=777
  _PREDICTRESPONSE._serialized_end=1215
  _PREDICTRESPONSE_PREDICTIONRESULT._serialized_start=996
  _PREDICTRESPONSE_PREDICTIONRESULT._serialized_end=1215
  _PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY._serialized_start=1132
  _PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY._serialized_end=1215
  _PREDICTIONSERVICE._serialized_start=1218
  _PREDICTIONSERVICE._serialized_end=1488
# @@protoc_insertion_point(module_scope)
