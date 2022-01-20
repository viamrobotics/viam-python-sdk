# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/explanation_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1/explanation_metadata.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\"\x8c\x16\n\x13\x45xplanationMetadata\x12Y\n\x06inputs\x18\x01 \x03(\x0b\x32;.google.cloud.aiplatform.v1.ExplanationMetadata.InputsEntryB\x04\xe2\x41\x01\x02R\x06inputs\x12\\\n\x07outputs\x18\x02 \x03(\x0b\x32<.google.cloud.aiplatform.v1.ExplanationMetadata.OutputsEntryB\x04\xe2\x41\x01\x02R\x07outputs\x12\x45\n\x1f\x66\x65\x61ture_attributions_schema_uri\x18\x03 \x01(\tR\x1c\x66\x65\x61tureAttributionsSchemaUri\x1a\x93\x10\n\rInputMetadata\x12?\n\x0finput_baselines\x18\x01 \x03(\x0b\x32\x16.google.protobuf.ValueR\x0einputBaselines\x12*\n\x11input_tensor_name\x18\x02 \x01(\tR\x0finputTensorName\x12\x62\n\x08\x65ncoding\x18\x03 \x01(\x0e\x32\x46.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.EncodingR\x08\x65ncoding\x12\x1a\n\x08modality\x18\x04 \x01(\tR\x08modality\x12\x82\x01\n\x14\x66\x65\x61ture_value_domain\x18\x05 \x01(\x0b\x32P.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.FeatureValueDomainR\x12\x66\x65\x61tureValueDomain\x12.\n\x13indices_tensor_name\x18\x06 \x01(\tR\x11indicesTensorName\x12\x35\n\x17\x64\x65nse_shape_tensor_name\x18\x07 \x01(\tR\x14\x64\x65nseShapeTensorName\x12\x32\n\x15index_feature_mapping\x18\x08 \x03(\tR\x13indexFeatureMapping\x12.\n\x13\x65ncoded_tensor_name\x18\t \x01(\tR\x11\x65ncodedTensorName\x12\x43\n\x11\x65ncoded_baselines\x18\n \x03(\x0b\x32\x16.google.protobuf.ValueR\x10\x65ncodedBaselines\x12q\n\rvisualization\x18\x0b \x01(\x0b\x32K.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.VisualizationR\rvisualization\x12\x1d\n\ngroup_name\x18\x0c \x01(\tR\tgroupName\x1a\x9c\x01\n\x12\x46\x65\x61tureValueDomain\x12\x1b\n\tmin_value\x18\x01 \x01(\x02R\x08minValue\x12\x1b\n\tmax_value\x18\x02 \x01(\x02R\x08maxValue\x12#\n\roriginal_mean\x18\x03 \x01(\x02R\x0coriginalMean\x12\'\n\x0foriginal_stddev\x18\x04 \x01(\x02R\x0eoriginalStddev\x1a\xab\x07\n\rVisualization\x12\x64\n\x04type\x18\x01 \x01(\x0e\x32P.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization.TypeR\x04type\x12p\n\x08polarity\x18\x02 \x01(\x0e\x32T.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization.PolarityR\x08polarity\x12q\n\tcolor_map\x18\x03 \x01(\x0e\x32T.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization.ColorMapR\x08\x63olorMap\x12\x36\n\x17\x63lip_percent_upperbound\x18\x04 \x01(\x02R\x15\x63lipPercentUpperbound\x12\x36\n\x17\x63lip_percent_lowerbound\x18\x05 \x01(\x02R\x15\x63lipPercentLowerbound\x12z\n\x0coverlay_type\x18\x06 \x01(\x0e\x32W.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization.OverlayTypeR\x0boverlayType\"6\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06PIXELS\x10\x01\x12\x0c\n\x08OUTLINES\x10\x02\"J\n\x08Polarity\x12\x18\n\x14POLARITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSITIVE\x10\x01\x12\x0c\n\x08NEGATIVE\x10\x02\x12\x08\n\x04\x42OTH\x10\x03\"{\n\x08\x43olorMap\x12\x19\n\x15\x43OLOR_MAP_UNSPECIFIED\x10\x00\x12\x0e\n\nPINK_GREEN\x10\x01\x12\x0b\n\x07VIRIDIS\x10\x02\x12\x07\n\x03RED\x10\x03\x12\t\n\x05GREEN\x10\x04\x12\r\n\tRED_GREEN\x10\x06\x12\x14\n\x10PINK_WHITE_GREEN\x10\x05\"b\n\x0bOverlayType\x12\x1c\n\x18OVERLAY_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x0c\n\x08ORIGINAL\x10\x02\x12\r\n\tGRAYSCALE\x10\x03\x12\x0e\n\nMASK_BLACK\x10\x04\"\xa0\x01\n\x08\x45ncoding\x12\x18\n\x14\x45NCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08IDENTITY\x10\x01\x12\x13\n\x0f\x42\x41G_OF_FEATURES\x10\x02\x12\x1a\n\x16\x42\x41G_OF_FEATURES_SPARSE\x10\x03\x12\r\n\tINDICATOR\x10\x04\x12\x16\n\x12\x43OMBINED_EMBEDDING\x10\x05\x12\x14\n\x10\x43ONCAT_EMBEDDING\x10\x06\x1a\xe8\x01\n\x0eOutputMetadata\x12U\n\x1aindex_display_name_mapping\x18\x01 \x01(\x0b\x32\x16.google.protobuf.ValueH\x00R\x17indexDisplayNameMapping\x12\x39\n\x18\x64isplay_name_mapping_key\x18\x02 \x01(\tH\x00R\x15\x64isplayNameMappingKey\x12,\n\x12output_tensor_name\x18\x03 \x01(\tR\x10outputTensorNameB\x16\n\x14\x64isplay_name_mapping\x1ax\n\x0bInputsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12S\n\x05value\x18\x02 \x01(\x0b\x32=.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadataR\x05value:\x02\x38\x01\x1az\n\x0cOutputsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12T\n\x05value\x18\x02 \x01(\x0b\x32>.google.cloud.aiplatform.v1.ExplanationMetadata.OutputMetadataR\x05value:\x02\x38\x01\x42\xdc\x01\n\x1e\x63om.google.cloud.aiplatform.v1B\x18\x45xplanationMetadataProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')



_EXPLANATIONMETADATA = DESCRIPTOR.message_types_by_name['ExplanationMetadata']
_EXPLANATIONMETADATA_INPUTMETADATA = _EXPLANATIONMETADATA.nested_types_by_name['InputMetadata']
_EXPLANATIONMETADATA_INPUTMETADATA_FEATUREVALUEDOMAIN = _EXPLANATIONMETADATA_INPUTMETADATA.nested_types_by_name['FeatureValueDomain']
_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION = _EXPLANATIONMETADATA_INPUTMETADATA.nested_types_by_name['Visualization']
_EXPLANATIONMETADATA_OUTPUTMETADATA = _EXPLANATIONMETADATA.nested_types_by_name['OutputMetadata']
_EXPLANATIONMETADATA_INPUTSENTRY = _EXPLANATIONMETADATA.nested_types_by_name['InputsEntry']
_EXPLANATIONMETADATA_OUTPUTSENTRY = _EXPLANATIONMETADATA.nested_types_by_name['OutputsEntry']
_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_TYPE = _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION.enum_types_by_name['Type']
_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_POLARITY = _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION.enum_types_by_name['Polarity']
_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_COLORMAP = _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION.enum_types_by_name['ColorMap']
_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_OVERLAYTYPE = _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION.enum_types_by_name['OverlayType']
_EXPLANATIONMETADATA_INPUTMETADATA_ENCODING = _EXPLANATIONMETADATA_INPUTMETADATA.enum_types_by_name['Encoding']
ExplanationMetadata = _reflection.GeneratedProtocolMessageType('ExplanationMetadata', (_message.Message,), {

  'InputMetadata' : _reflection.GeneratedProtocolMessageType('InputMetadata', (_message.Message,), {

    'FeatureValueDomain' : _reflection.GeneratedProtocolMessageType('FeatureValueDomain', (_message.Message,), {
      'DESCRIPTOR' : _EXPLANATIONMETADATA_INPUTMETADATA_FEATUREVALUEDOMAIN,
      '__module__' : 'google.cloud.aiplatform.v1.explanation_metadata_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.FeatureValueDomain)
      })
    ,

    'Visualization' : _reflection.GeneratedProtocolMessageType('Visualization', (_message.Message,), {
      'DESCRIPTOR' : _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION,
      '__module__' : 'google.cloud.aiplatform.v1.explanation_metadata_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization)
      })
    ,
    'DESCRIPTOR' : _EXPLANATIONMETADATA_INPUTMETADATA,
    '__module__' : 'google.cloud.aiplatform.v1.explanation_metadata_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata)
    })
  ,

  'OutputMetadata' : _reflection.GeneratedProtocolMessageType('OutputMetadata', (_message.Message,), {
    'DESCRIPTOR' : _EXPLANATIONMETADATA_OUTPUTMETADATA,
    '__module__' : 'google.cloud.aiplatform.v1.explanation_metadata_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ExplanationMetadata.OutputMetadata)
    })
  ,

  'InputsEntry' : _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXPLANATIONMETADATA_INPUTSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.explanation_metadata_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ExplanationMetadata.InputsEntry)
    })
  ,

  'OutputsEntry' : _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXPLANATIONMETADATA_OUTPUTSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.explanation_metadata_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ExplanationMetadata.OutputsEntry)
    })
  ,
  'DESCRIPTOR' : _EXPLANATIONMETADATA,
  '__module__' : 'google.cloud.aiplatform.v1.explanation_metadata_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ExplanationMetadata)
  })
_sym_db.RegisterMessage(ExplanationMetadata)
_sym_db.RegisterMessage(ExplanationMetadata.InputMetadata)
_sym_db.RegisterMessage(ExplanationMetadata.InputMetadata.FeatureValueDomain)
_sym_db.RegisterMessage(ExplanationMetadata.InputMetadata.Visualization)
_sym_db.RegisterMessage(ExplanationMetadata.OutputMetadata)
_sym_db.RegisterMessage(ExplanationMetadata.InputsEntry)
_sym_db.RegisterMessage(ExplanationMetadata.OutputsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.aiplatform.v1B\030ExplanationMetadataProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\252\002\032Google.Cloud.AIPlatform.V1\312\002\032Google\\Cloud\\AIPlatform\\V1\352\002\035Google::Cloud::AIPlatform::V1'
  _EXPLANATIONMETADATA_INPUTSENTRY._options = None
  _EXPLANATIONMETADATA_INPUTSENTRY._serialized_options = b'8\001'
  _EXPLANATIONMETADATA_OUTPUTSENTRY._options = None
  _EXPLANATIONMETADATA_OUTPUTSENTRY._serialized_options = b'8\001'
  _EXPLANATIONMETADATA.fields_by_name['inputs']._options = None
  _EXPLANATIONMETADATA.fields_by_name['inputs']._serialized_options = b'\342A\001\002'
  _EXPLANATIONMETADATA.fields_by_name['outputs']._options = None
  _EXPLANATIONMETADATA.fields_by_name['outputs']._serialized_options = b'\342A\001\002'
  _EXPLANATIONMETADATA._serialized_start=179
  _EXPLANATIONMETADATA._serialized_end=3007
  _EXPLANATIONMETADATA_INPUTMETADATA._serialized_start=459
  _EXPLANATIONMETADATA_INPUTMETADATA._serialized_end=2526
  _EXPLANATIONMETADATA_INPUTMETADATA_FEATUREVALUEDOMAIN._serialized_start=1265
  _EXPLANATIONMETADATA_INPUTMETADATA_FEATUREVALUEDOMAIN._serialized_end=1421
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION._serialized_start=1424
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION._serialized_end=2363
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_TYPE._serialized_start=2008
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_TYPE._serialized_end=2062
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_POLARITY._serialized_start=2064
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_POLARITY._serialized_end=2138
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_COLORMAP._serialized_start=2140
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_COLORMAP._serialized_end=2263
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_OVERLAYTYPE._serialized_start=2265
  _EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_OVERLAYTYPE._serialized_end=2363
  _EXPLANATIONMETADATA_INPUTMETADATA_ENCODING._serialized_start=2366
  _EXPLANATIONMETADATA_INPUTMETADATA_ENCODING._serialized_end=2526
  _EXPLANATIONMETADATA_OUTPUTMETADATA._serialized_start=2529
  _EXPLANATIONMETADATA_OUTPUTMETADATA._serialized_end=2761
  _EXPLANATIONMETADATA_INPUTSENTRY._serialized_start=2763
  _EXPLANATIONMETADATA_INPUTSENTRY._serialized_end=2883
  _EXPLANATIONMETADATA_OUTPUTSENTRY._serialized_start=2885
  _EXPLANATIONMETADATA_OUTPUTSENTRY._serialized_end=3007
# @@protoc_insertion_point(module_scope)
