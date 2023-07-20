"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n service/mlmodel/v1/mlmodel.proto\x12\x17viam.service.mlmodel.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"Z\n\x0cInferRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x126\n\ninput_data\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\tinputData"I\n\rInferResponse\x128\n\x0boutput_data\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\noutputData"%\n\x0fMetadataRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"Q\n\x10MetadataResponse\x12=\n\x08metadata\x18\x01 \x01(\x0b2!.viam.service.mlmodel.v1.MetadataR\x08metadata"\xde\x01\n\x08Metadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x12B\n\ninput_info\x18\x04 \x03(\x0b2#.viam.service.mlmodel.v1.TensorInfoR\tinputInfo\x12D\n\x0boutput_info\x18\x05 \x03(\x0b2#.viam.service.mlmodel.v1.TensorInfoR\noutputInfo"\xee\x01\n\nTensorInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x1b\n\tdata_type\x18\x03 \x01(\tR\x08dataType\x12\x14\n\x05shape\x18\x04 \x03(\x05R\x05shape\x12H\n\x10associated_files\x18\x05 \x03(\x0b2\x1d.viam.service.mlmodel.v1.FileR\x0fassociatedFiles\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x7f\n\x04File\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12A\n\nlabel_type\x18\x03 \x01(\x0e2".viam.service.mlmodel.v1.LabelTypeR\tlabelType*`\n\tLabelType\x12\x1a\n\x16LABEL_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17LABEL_TYPE_TENSOR_VALUE\x10\x01\x12\x1a\n\x16LABEL_TYPE_TENSOR_AXIS\x10\x022\xb4\x02\n\x0eMLModelService\x12\x89\x01\n\x05Infer\x12%.viam.service.mlmodel.v1.InferRequest\x1a&.viam.service.mlmodel.v1.InferResponse"1\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/mlmodel/{name}/infer\x12\x95\x01\n\x08Metadata\x12(.viam.service.mlmodel.v1.MetadataRequest\x1a).viam.service.mlmodel.v1.MetadataResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/mlmodel/{name}/metadataBA\n\x1bcom.viam.service.mlmodel.v1Z"go.viam.com/api/service/mlmodel/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.mlmodel.v1.mlmodel_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.viam.service.mlmodel.v1Z"go.viam.com/api/service/mlmodel/v1'
    _MLMODELSERVICE.methods_by_name['Infer']._options = None
    _MLMODELSERVICE.methods_by_name['Infer']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/mlmodel/{name}/infer'
    _MLMODELSERVICE.methods_by_name['Metadata']._options = None
    _MLMODELSERVICE.methods_by_name['Metadata']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/mlmodel/{name}/metadata'
    _LABELTYPE._serialized_start = 1005
    _LABELTYPE._serialized_end = 1101
    _INFERREQUEST._serialized_start = 121
    _INFERREQUEST._serialized_end = 211
    _INFERRESPONSE._serialized_start = 213
    _INFERRESPONSE._serialized_end = 286
    _METADATAREQUEST._serialized_start = 288
    _METADATAREQUEST._serialized_end = 325
    _METADATARESPONSE._serialized_start = 327
    _METADATARESPONSE._serialized_end = 408
    _METADATA._serialized_start = 411
    _METADATA._serialized_end = 633
    _TENSORINFO._serialized_start = 636
    _TENSORINFO._serialized_end = 874
    _FILE._serialized_start = 876
    _FILE._serialized_end = 1003
    _MLMODELSERVICE._serialized_start = 1104
    _MLMODELSERVICE._serialized_end = 1412