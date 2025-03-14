"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'app/mlinference/v1/ml_inference.proto')
_sym_db = _symbol_database.Default()
from ....app.data.v1 import data_pb2 as app_dot_data_dot_v1_dot_data__pb2
from ....service.mlmodel.v1 import mlmodel_pb2 as service_dot_mlmodel_dot_v1_dot_mlmodel__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%app/mlinference/v1/ml_inference.proto\x12\x17viam.app.mlinference.v1\x1a\x16app/data/v1/data.proto\x1a service/mlmodel/v1/mlmodel.proto"\xfb\x01\n\x13GetInferenceRequest\x12(\n\x10registry_item_id\x18\x01 \x01(\tR\x0eregistryItemId\x122\n\x15registry_item_version\x18\x02 \x01(\tR\x13registryItemVersion\x127\n\tbinary_id\x18\x03 \x01(\x0b2\x1a.viam.app.data.v1.BinaryIDR\x08binaryId\x12$\n\x0ebinary_data_id\x18\x05 \x01(\tR\x0cbinaryDataId\x12\'\n\x0forganization_id\x18\x04 \x01(\tR\x0eorganizationId"\xa4\x01\n\x14GetInferenceResponse\x12K\n\x0eoutput_tensors\x18\x01 \x01(\x0b2$.viam.service.mlmodel.v1.FlatTensorsR\routputTensors\x12?\n\x0bannotations\x18\x02 \x01(\x0b2\x1d.viam.app.data.v1.AnnotationsR\x0bannotations2\x81\x01\n\x12MLInferenceService\x12k\n\x0cGetInference\x12,.viam.app.mlinference.v1.GetInferenceRequest\x1a-.viam.app.mlinference.v1.GetInferenceResponseB$Z"go.viam.com/api/app/mlinference/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.mlinference.v1.ml_inference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z"go.viam.com/api/app/mlinference/v1'
    _globals['_GETINFERENCEREQUEST']._serialized_start = 125
    _globals['_GETINFERENCEREQUEST']._serialized_end = 376
    _globals['_GETINFERENCERESPONSE']._serialized_start = 379
    _globals['_GETINFERENCERESPONSE']._serialized_end = 543
    _globals['_MLINFERENCESERVICE']._serialized_start = 546
    _globals['_MLINFERENCESERVICE']._serialized_end = 675