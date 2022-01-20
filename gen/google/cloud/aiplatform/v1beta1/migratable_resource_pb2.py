# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/migratable_resource.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1beta1/migratable_resource.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x90\x0c\n\x12MigratableResource\x12\x87\x01\n\x17ml_engine_model_version\x18\x01 \x01(\x0b\x32H.google.cloud.aiplatform.v1beta1.MigratableResource.MlEngineModelVersionB\x04\xe2\x41\x01\x03H\x00R\x14mlEngineModelVersion\x12j\n\x0c\x61utoml_model\x18\x02 \x01(\x0b\x32?.google.cloud.aiplatform.v1beta1.MigratableResource.AutomlModelB\x04\xe2\x41\x01\x03H\x00R\x0b\x61utomlModel\x12p\n\x0e\x61utoml_dataset\x18\x03 \x01(\x0b\x32\x41.google.cloud.aiplatform.v1beta1.MigratableResource.AutomlDatasetB\x04\xe2\x41\x01\x03H\x00R\rautomlDataset\x12\x83\x01\n\x15\x64\x61ta_labeling_dataset\x18\x04 \x01(\x0b\x32G.google.cloud.aiplatform.v1beta1.MigratableResource.DataLabelingDatasetB\x04\xe2\x41\x01\x03H\x00R\x13\x64\x61taLabelingDataset\x12L\n\x11last_migrate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x0flastMigrateTime\x12J\n\x10last_update_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x0elastUpdateTime\x1al\n\x14MlEngineModelVersion\x12\x1a\n\x08\x65ndpoint\x18\x01 \x01(\tR\x08\x65ndpoint\x12\x38\n\x07version\x18\x02 \x01(\tB\x1e\xfa\x41\x1b\n\x19ml.googleapis.com/VersionR\x07version\x1as\n\x0b\x41utomlModel\x12\x36\n\x05model\x18\x01 \x01(\tB \xfa\x41\x1d\n\x1b\x61utoml.googleapis.com/ModelR\x05model\x12,\n\x12model_display_name\x18\x03 \x01(\tR\x10modelDisplayName\x1a\x7f\n\rAutomlDataset\x12<\n\x07\x64\x61taset\x18\x01 \x01(\tB\"\xfa\x41\x1f\n\x1d\x61utoml.googleapis.com/DatasetR\x07\x64\x61taset\x12\x30\n\x14\x64\x61taset_display_name\x18\x04 \x01(\tR\x12\x64\x61tasetDisplayName\x1a\x81\x04\n\x13\x44\x61taLabelingDataset\x12\x42\n\x07\x64\x61taset\x18\x01 \x01(\tB(\xfa\x41%\n#datalabeling.googleapis.com/DatasetR\x07\x64\x61taset\x12\x30\n\x14\x64\x61taset_display_name\x18\x04 \x01(\tR\x12\x64\x61tasetDisplayName\x12\xad\x01\n data_labeling_annotated_datasets\x18\x03 \x03(\x0b\x32\x64.google.cloud.aiplatform.v1beta1.MigratableResource.DataLabelingDataset.DataLabelingAnnotatedDatasetR\x1d\x64\x61taLabelingAnnotatedDatasets\x1a\xc3\x01\n\x1c\x44\x61taLabelingAnnotatedDataset\x12^\n\x11\x61nnotated_dataset\x18\x01 \x01(\tB1\xfa\x41.\n,datalabeling.googleapis.com/AnnotatedDatasetR\x10\x61nnotatedDataset\x12\x43\n\x1e\x61nnotated_dataset_display_name\x18\x03 \x01(\tR\x1b\x61nnotatedDatasetDisplayNameB\n\n\x08resourceB\xcb\x05\n#com.google.cloud.aiplatform.v1beta1B\x17MigratableResourceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02\"Google::Cloud::AIPlatform::V1beta1\xea\x41Q\n\x19ml.googleapis.com/Version\x12\x34projects/{project}/models/{model}/versions/{version}\xea\x41U\n\x1b\x61utoml.googleapis.com/Model\x12\x36projects/{project}/locations/{location}/models/{model}\xea\x41[\n\x1d\x61utoml.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}\xea\x41L\n#datalabeling.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}\xea\x41{\n,datalabeling.googleapis.com/AnnotatedDataset\x12Kprojects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}b\x06proto3')



_MIGRATABLERESOURCE = DESCRIPTOR.message_types_by_name['MigratableResource']
_MIGRATABLERESOURCE_MLENGINEMODELVERSION = _MIGRATABLERESOURCE.nested_types_by_name['MlEngineModelVersion']
_MIGRATABLERESOURCE_AUTOMLMODEL = _MIGRATABLERESOURCE.nested_types_by_name['AutomlModel']
_MIGRATABLERESOURCE_AUTOMLDATASET = _MIGRATABLERESOURCE.nested_types_by_name['AutomlDataset']
_MIGRATABLERESOURCE_DATALABELINGDATASET = _MIGRATABLERESOURCE.nested_types_by_name['DataLabelingDataset']
_MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET = _MIGRATABLERESOURCE_DATALABELINGDATASET.nested_types_by_name['DataLabelingAnnotatedDataset']
MigratableResource = _reflection.GeneratedProtocolMessageType('MigratableResource', (_message.Message,), {

  'MlEngineModelVersion' : _reflection.GeneratedProtocolMessageType('MlEngineModelVersion', (_message.Message,), {
    'DESCRIPTOR' : _MIGRATABLERESOURCE_MLENGINEMODELVERSION,
    '__module__' : 'google.cloud.aiplatform.v1beta1.migratable_resource_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.MigratableResource.MlEngineModelVersion)
    })
  ,

  'AutomlModel' : _reflection.GeneratedProtocolMessageType('AutomlModel', (_message.Message,), {
    'DESCRIPTOR' : _MIGRATABLERESOURCE_AUTOMLMODEL,
    '__module__' : 'google.cloud.aiplatform.v1beta1.migratable_resource_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.MigratableResource.AutomlModel)
    })
  ,

  'AutomlDataset' : _reflection.GeneratedProtocolMessageType('AutomlDataset', (_message.Message,), {
    'DESCRIPTOR' : _MIGRATABLERESOURCE_AUTOMLDATASET,
    '__module__' : 'google.cloud.aiplatform.v1beta1.migratable_resource_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.MigratableResource.AutomlDataset)
    })
  ,

  'DataLabelingDataset' : _reflection.GeneratedProtocolMessageType('DataLabelingDataset', (_message.Message,), {

    'DataLabelingAnnotatedDataset' : _reflection.GeneratedProtocolMessageType('DataLabelingAnnotatedDataset', (_message.Message,), {
      'DESCRIPTOR' : _MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET,
      '__module__' : 'google.cloud.aiplatform.v1beta1.migratable_resource_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.MigratableResource.DataLabelingDataset.DataLabelingAnnotatedDataset)
      })
    ,
    'DESCRIPTOR' : _MIGRATABLERESOURCE_DATALABELINGDATASET,
    '__module__' : 'google.cloud.aiplatform.v1beta1.migratable_resource_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.MigratableResource.DataLabelingDataset)
    })
  ,
  'DESCRIPTOR' : _MIGRATABLERESOURCE,
  '__module__' : 'google.cloud.aiplatform.v1beta1.migratable_resource_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.MigratableResource)
  })
_sym_db.RegisterMessage(MigratableResource)
_sym_db.RegisterMessage(MigratableResource.MlEngineModelVersion)
_sym_db.RegisterMessage(MigratableResource.AutomlModel)
_sym_db.RegisterMessage(MigratableResource.AutomlDataset)
_sym_db.RegisterMessage(MigratableResource.DataLabelingDataset)
_sym_db.RegisterMessage(MigratableResource.DataLabelingDataset.DataLabelingAnnotatedDataset)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\027MigratableResourceProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\252\002\037Google.Cloud.AIPlatform.V1Beta1\312\002\037Google\\Cloud\\AIPlatform\\V1beta1\352\002\"Google::Cloud::AIPlatform::V1beta1\352AQ\n\031ml.googleapis.com/Version\0224projects/{project}/models/{model}/versions/{version}\352AU\n\033automl.googleapis.com/Model\0226projects/{project}/locations/{location}/models/{model}\352A[\n\035automl.googleapis.com/Dataset\022:projects/{project}/locations/{location}/datasets/{dataset}\352AL\n#datalabeling.googleapis.com/Dataset\022%projects/{project}/datasets/{dataset}\352A{\n,datalabeling.googleapis.com/AnnotatedDataset\022Kprojects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}'
  _MIGRATABLERESOURCE_MLENGINEMODELVERSION.fields_by_name['version']._options = None
  _MIGRATABLERESOURCE_MLENGINEMODELVERSION.fields_by_name['version']._serialized_options = b'\372A\033\n\031ml.googleapis.com/Version'
  _MIGRATABLERESOURCE_AUTOMLMODEL.fields_by_name['model']._options = None
  _MIGRATABLERESOURCE_AUTOMLMODEL.fields_by_name['model']._serialized_options = b'\372A\035\n\033automl.googleapis.com/Model'
  _MIGRATABLERESOURCE_AUTOMLDATASET.fields_by_name['dataset']._options = None
  _MIGRATABLERESOURCE_AUTOMLDATASET.fields_by_name['dataset']._serialized_options = b'\372A\037\n\035automl.googleapis.com/Dataset'
  _MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET.fields_by_name['annotated_dataset']._options = None
  _MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET.fields_by_name['annotated_dataset']._serialized_options = b'\372A.\n,datalabeling.googleapis.com/AnnotatedDataset'
  _MIGRATABLERESOURCE_DATALABELINGDATASET.fields_by_name['dataset']._options = None
  _MIGRATABLERESOURCE_DATALABELINGDATASET.fields_by_name['dataset']._serialized_options = b'\372A%\n#datalabeling.googleapis.com/Dataset'
  _MIGRATABLERESOURCE.fields_by_name['ml_engine_model_version']._options = None
  _MIGRATABLERESOURCE.fields_by_name['ml_engine_model_version']._serialized_options = b'\342A\001\003'
  _MIGRATABLERESOURCE.fields_by_name['automl_model']._options = None
  _MIGRATABLERESOURCE.fields_by_name['automl_model']._serialized_options = b'\342A\001\003'
  _MIGRATABLERESOURCE.fields_by_name['automl_dataset']._options = None
  _MIGRATABLERESOURCE.fields_by_name['automl_dataset']._serialized_options = b'\342A\001\003'
  _MIGRATABLERESOURCE.fields_by_name['data_labeling_dataset']._options = None
  _MIGRATABLERESOURCE.fields_by_name['data_labeling_dataset']._serialized_options = b'\342A\001\003'
  _MIGRATABLERESOURCE.fields_by_name['last_migrate_time']._options = None
  _MIGRATABLERESOURCE.fields_by_name['last_migrate_time']._serialized_options = b'\342A\001\003'
  _MIGRATABLERESOURCE.fields_by_name['last_update_time']._options = None
  _MIGRATABLERESOURCE.fields_by_name['last_update_time']._serialized_options = b'\342A\001\003'
  _MIGRATABLERESOURCE._serialized_start=218
  _MIGRATABLERESOURCE._serialized_end=1770
  _MIGRATABLERESOURCE_MLENGINEMODELVERSION._serialized_start=888
  _MIGRATABLERESOURCE_MLENGINEMODELVERSION._serialized_end=996
  _MIGRATABLERESOURCE_AUTOMLMODEL._serialized_start=998
  _MIGRATABLERESOURCE_AUTOMLMODEL._serialized_end=1113
  _MIGRATABLERESOURCE_AUTOMLDATASET._serialized_start=1115
  _MIGRATABLERESOURCE_AUTOMLDATASET._serialized_end=1242
  _MIGRATABLERESOURCE_DATALABELINGDATASET._serialized_start=1245
  _MIGRATABLERESOURCE_DATALABELINGDATASET._serialized_end=1758
  _MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET._serialized_start=1563
  _MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET._serialized_end=1758
# @@protoc_insertion_point(module_scope)
