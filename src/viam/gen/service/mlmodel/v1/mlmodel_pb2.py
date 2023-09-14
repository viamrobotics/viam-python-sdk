"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n service/mlmodel/v1/mlmodel.proto\x12\x17viam.service.mlmodel.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xae\x01\n\x0cInferRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12I\n\rinput_tensors\x18\x03 \x01(\x0b2$.viam.service.mlmodel.v1.FlatTensorsR\x0cinputTensors\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraJ\x04\x08\x02\x10\x03R\ninput_data"{\n\rInferResponse\x12K\n\x0eoutput_tensors\x18\x03 \x01(\x0b2$.viam.service.mlmodel.v1.FlatTensorsR\routputTensorsJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03R\x04nameR\x0boutput_data"T\n\x0fMetadataRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"Q\n\x10MetadataResponse\x12=\n\x08metadata\x18\x01 \x01(\x0b2!.viam.service.mlmodel.v1.MetadataR\x08metadata"\xde\x01\n\x08Metadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x12B\n\ninput_info\x18\x04 \x03(\x0b2#.viam.service.mlmodel.v1.TensorInfoR\tinputInfo\x12D\n\x0boutput_info\x18\x05 \x03(\x0b2#.viam.service.mlmodel.v1.TensorInfoR\noutputInfo"\xee\x01\n\nTensorInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x1b\n\tdata_type\x18\x03 \x01(\tR\x08dataType\x12\x14\n\x05shape\x18\x04 \x03(\x05R\x05shape\x12H\n\x10associated_files\x18\x05 \x03(\x0b2\x1d.viam.service.mlmodel.v1.FileR\x0fassociatedFiles\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x7f\n\x04File\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12A\n\nlabel_type\x18\x03 \x01(\x0e2".viam.service.mlmodel.v1.LabelTypeR\tlabelType"(\n\x12FlatTensorDataInt8\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data")\n\x13FlatTensorDataUInt8\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data"-\n\x13FlatTensorDataInt16\x12\x16\n\x04data\x18\x01 \x03(\x07B\x02\x10\x01R\x04data".\n\x14FlatTensorDataUInt16\x12\x16\n\x04data\x18\x01 \x03(\x07B\x02\x10\x01R\x04data"-\n\x13FlatTensorDataInt32\x12\x16\n\x04data\x18\x01 \x03(\x0fB\x02\x10\x01R\x04data".\n\x14FlatTensorDataUInt32\x12\x16\n\x04data\x18\x01 \x03(\x07B\x02\x10\x01R\x04data"-\n\x13FlatTensorDataInt64\x12\x16\n\x04data\x18\x01 \x03(\x10B\x02\x10\x01R\x04data".\n\x14FlatTensorDataUInt64\x12\x16\n\x04data\x18\x01 \x03(\x06B\x02\x10\x01R\x04data"-\n\x13FlatTensorDataFloat\x12\x16\n\x04data\x18\x01 \x03(\x02B\x02\x10\x01R\x04data".\n\x14FlatTensorDataDouble\x12\x16\n\x04data\x18\x01 \x03(\x01B\x02\x10\x01R\x04data"\xf3\x06\n\nFlatTensor\x12\x14\n\x05shape\x18\x01 \x03(\x06R\x05shape\x12N\n\x0bint8_tensor\x18\x02 \x01(\x0b2+.viam.service.mlmodel.v1.FlatTensorDataInt8H\x00R\nint8Tensor\x12Q\n\x0cuint8_tensor\x18\x03 \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataUInt8H\x00R\x0buint8Tensor\x12Q\n\x0cint16_tensor\x18\x04 \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataInt16H\x00R\x0bint16Tensor\x12T\n\ruint16_tensor\x18\x05 \x01(\x0b2-.viam.service.mlmodel.v1.FlatTensorDataUInt16H\x00R\x0cuint16Tensor\x12Q\n\x0cint32_tensor\x18\x06 \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataInt32H\x00R\x0bint32Tensor\x12T\n\ruint32_tensor\x18\x07 \x01(\x0b2-.viam.service.mlmodel.v1.FlatTensorDataUInt32H\x00R\x0cuint32Tensor\x12Q\n\x0cint64_tensor\x18\x08 \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataInt64H\x00R\x0bint64Tensor\x12T\n\ruint64_tensor\x18\t \x01(\x0b2-.viam.service.mlmodel.v1.FlatTensorDataUInt64H\x00R\x0cuint64Tensor\x12Q\n\x0cfloat_tensor\x18\n \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataFloatH\x00R\x0bfloatTensor\x12T\n\rdouble_tensor\x18\x0b \x01(\x0b2-.viam.service.mlmodel.v1.FlatTensorDataDoubleH\x00R\x0cdoubleTensorB\x08\n\x06tensor"\xbb\x01\n\x0bFlatTensors\x12K\n\x07tensors\x18\x01 \x03(\x0b21.viam.service.mlmodel.v1.FlatTensors.TensorsEntryR\x07tensors\x1a_\n\x0cTensorsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x129\n\x05value\x18\x02 \x01(\x0b2#.viam.service.mlmodel.v1.FlatTensorR\x05value:\x028\x01*`\n\tLabelType\x12\x1a\n\x16LABEL_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17LABEL_TYPE_TENSOR_VALUE\x10\x01\x12\x1a\n\x16LABEL_TYPE_TENSOR_AXIS\x10\x022\xb4\x02\n\x0eMLModelService\x12\x89\x01\n\x05Infer\x12%.viam.service.mlmodel.v1.InferRequest\x1a&.viam.service.mlmodel.v1.InferResponse"1\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/mlmodel/{name}/infer\x12\x95\x01\n\x08Metadata\x12(.viam.service.mlmodel.v1.MetadataRequest\x1a).viam.service.mlmodel.v1.MetadataResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/mlmodel/{name}/metadataBA\n\x1bcom.viam.service.mlmodel.v1Z"go.viam.com/api/service/mlmodel/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.mlmodel.v1.mlmodel_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.viam.service.mlmodel.v1Z"go.viam.com/api/service/mlmodel/v1'
    _FLATTENSORDATAINT16.fields_by_name['data']._options = None
    _FLATTENSORDATAINT16.fields_by_name['data']._serialized_options = b'\x10\x01'
    _FLATTENSORDATAUINT16.fields_by_name['data']._options = None
    _FLATTENSORDATAUINT16.fields_by_name['data']._serialized_options = b'\x10\x01'
    _FLATTENSORDATAINT32.fields_by_name['data']._options = None
    _FLATTENSORDATAINT32.fields_by_name['data']._serialized_options = b'\x10\x01'
    _FLATTENSORDATAUINT32.fields_by_name['data']._options = None
    _FLATTENSORDATAUINT32.fields_by_name['data']._serialized_options = b'\x10\x01'
    _FLATTENSORDATAINT64.fields_by_name['data']._options = None
    _FLATTENSORDATAINT64.fields_by_name['data']._serialized_options = b'\x10\x01'
    _FLATTENSORDATAUINT64.fields_by_name['data']._options = None
    _FLATTENSORDATAUINT64.fields_by_name['data']._serialized_options = b'\x10\x01'
    _FLATTENSORDATAFLOAT.fields_by_name['data']._options = None
    _FLATTENSORDATAFLOAT.fields_by_name['data']._serialized_options = b'\x10\x01'
    _FLATTENSORDATADOUBLE.fields_by_name['data']._options = None
    _FLATTENSORDATADOUBLE.fields_by_name['data']._serialized_options = b'\x10\x01'
    _FLATTENSORS_TENSORSENTRY._options = None
    _FLATTENSORS_TENSORSENTRY._serialized_options = b'8\x01'
    _MLMODELSERVICE.methods_by_name['Infer']._options = None
    _MLMODELSERVICE.methods_by_name['Infer']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/mlmodel/{name}/infer'
    _MLMODELSERVICE.methods_by_name['Metadata']._options = None
    _MLMODELSERVICE.methods_by_name['Metadata']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/mlmodel/{name}/metadata'
    _LABELTYPE._serialized_start = 2728
    _LABELTYPE._serialized_end = 2824
    _INFERREQUEST._serialized_start = 122
    _INFERREQUEST._serialized_end = 296
    _INFERRESPONSE._serialized_start = 298
    _INFERRESPONSE._serialized_end = 421
    _METADATAREQUEST._serialized_start = 423
    _METADATAREQUEST._serialized_end = 507
    _METADATARESPONSE._serialized_start = 509
    _METADATARESPONSE._serialized_end = 590
    _METADATA._serialized_start = 593
    _METADATA._serialized_end = 815
    _TENSORINFO._serialized_start = 818
    _TENSORINFO._serialized_end = 1056
    _FILE._serialized_start = 1058
    _FILE._serialized_end = 1185
    _FLATTENSORDATAINT8._serialized_start = 1187
    _FLATTENSORDATAINT8._serialized_end = 1227
    _FLATTENSORDATAUINT8._serialized_start = 1229
    _FLATTENSORDATAUINT8._serialized_end = 1270
    _FLATTENSORDATAINT16._serialized_start = 1272
    _FLATTENSORDATAINT16._serialized_end = 1317
    _FLATTENSORDATAUINT16._serialized_start = 1319
    _FLATTENSORDATAUINT16._serialized_end = 1365
    _FLATTENSORDATAINT32._serialized_start = 1367
    _FLATTENSORDATAINT32._serialized_end = 1412
    _FLATTENSORDATAUINT32._serialized_start = 1414
    _FLATTENSORDATAUINT32._serialized_end = 1460
    _FLATTENSORDATAINT64._serialized_start = 1462
    _FLATTENSORDATAINT64._serialized_end = 1507
    _FLATTENSORDATAUINT64._serialized_start = 1509
    _FLATTENSORDATAUINT64._serialized_end = 1555
    _FLATTENSORDATAFLOAT._serialized_start = 1557
    _FLATTENSORDATAFLOAT._serialized_end = 1602
    _FLATTENSORDATADOUBLE._serialized_start = 1604
    _FLATTENSORDATADOUBLE._serialized_end = 1650
    _FLATTENSOR._serialized_start = 1653
    _FLATTENSOR._serialized_end = 2536
    _FLATTENSORS._serialized_start = 2539
    _FLATTENSORS._serialized_end = 2726
    _FLATTENSORS_TENSORSENTRY._serialized_start = 2631
    _FLATTENSORS_TENSORSENTRY._serialized_end = 2726
    _MLMODELSERVICE._serialized_start = 2827
    _MLMODELSERVICE._serialized_end = 3135