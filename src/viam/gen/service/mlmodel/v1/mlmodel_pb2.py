"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 5, '', 'service/mlmodel/v1/mlmodel.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n service/mlmodel/v1/mlmodel.proto\x12\x17viam.service.mlmodel.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xae\x01\n\x0cInferRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12I\n\rinput_tensors\x18\x03 \x01(\x0b2$.viam.service.mlmodel.v1.FlatTensorsR\x0cinputTensors\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraJ\x04\x08\x02\x10\x03R\ninput_data"{\n\rInferResponse\x12K\n\x0eoutput_tensors\x18\x03 \x01(\x0b2$.viam.service.mlmodel.v1.FlatTensorsR\routputTensorsJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03R\x04nameR\x0boutput_data"T\n\x0fMetadataRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"Q\n\x10MetadataResponse\x12=\n\x08metadata\x18\x01 \x01(\x0b2!.viam.service.mlmodel.v1.MetadataR\x08metadata"\xde\x01\n\x08Metadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x12B\n\ninput_info\x18\x04 \x03(\x0b2#.viam.service.mlmodel.v1.TensorInfoR\tinputInfo\x12D\n\x0boutput_info\x18\x05 \x03(\x0b2#.viam.service.mlmodel.v1.TensorInfoR\noutputInfo"\xee\x01\n\nTensorInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x1b\n\tdata_type\x18\x03 \x01(\tR\x08dataType\x12\x14\n\x05shape\x18\x04 \x03(\x05R\x05shape\x12H\n\x10associated_files\x18\x05 \x03(\x0b2\x1d.viam.service.mlmodel.v1.FileR\x0fassociatedFiles\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x7f\n\x04File\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12A\n\nlabel_type\x18\x03 \x01(\x0e2".viam.service.mlmodel.v1.LabelTypeR\tlabelType"(\n\x12FlatTensorDataInt8\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data")\n\x13FlatTensorDataUInt8\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data"-\n\x13FlatTensorDataInt16\x12\x16\n\x04data\x18\x01 \x03(\x07B\x02\x10\x01R\x04data".\n\x14FlatTensorDataUInt16\x12\x16\n\x04data\x18\x01 \x03(\x07B\x02\x10\x01R\x04data"-\n\x13FlatTensorDataInt32\x12\x16\n\x04data\x18\x01 \x03(\x0fB\x02\x10\x01R\x04data".\n\x14FlatTensorDataUInt32\x12\x16\n\x04data\x18\x01 \x03(\x07B\x02\x10\x01R\x04data"-\n\x13FlatTensorDataInt64\x12\x16\n\x04data\x18\x01 \x03(\x10B\x02\x10\x01R\x04data".\n\x14FlatTensorDataUInt64\x12\x16\n\x04data\x18\x01 \x03(\x06B\x02\x10\x01R\x04data"-\n\x13FlatTensorDataFloat\x12\x16\n\x04data\x18\x01 \x03(\x02B\x02\x10\x01R\x04data".\n\x14FlatTensorDataDouble\x12\x16\n\x04data\x18\x01 \x03(\x01B\x02\x10\x01R\x04data"\xf3\x06\n\nFlatTensor\x12\x14\n\x05shape\x18\x01 \x03(\x06R\x05shape\x12N\n\x0bint8_tensor\x18\x02 \x01(\x0b2+.viam.service.mlmodel.v1.FlatTensorDataInt8H\x00R\nint8Tensor\x12Q\n\x0cuint8_tensor\x18\x03 \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataUInt8H\x00R\x0buint8Tensor\x12Q\n\x0cint16_tensor\x18\x04 \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataInt16H\x00R\x0bint16Tensor\x12T\n\ruint16_tensor\x18\x05 \x01(\x0b2-.viam.service.mlmodel.v1.FlatTensorDataUInt16H\x00R\x0cuint16Tensor\x12Q\n\x0cint32_tensor\x18\x06 \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataInt32H\x00R\x0bint32Tensor\x12T\n\ruint32_tensor\x18\x07 \x01(\x0b2-.viam.service.mlmodel.v1.FlatTensorDataUInt32H\x00R\x0cuint32Tensor\x12Q\n\x0cint64_tensor\x18\x08 \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataInt64H\x00R\x0bint64Tensor\x12T\n\ruint64_tensor\x18\t \x01(\x0b2-.viam.service.mlmodel.v1.FlatTensorDataUInt64H\x00R\x0cuint64Tensor\x12Q\n\x0cfloat_tensor\x18\n \x01(\x0b2,.viam.service.mlmodel.v1.FlatTensorDataFloatH\x00R\x0bfloatTensor\x12T\n\rdouble_tensor\x18\x0b \x01(\x0b2-.viam.service.mlmodel.v1.FlatTensorDataDoubleH\x00R\x0cdoubleTensorB\x08\n\x06tensor"\xbb\x01\n\x0bFlatTensors\x12K\n\x07tensors\x18\x01 \x03(\x0b21.viam.service.mlmodel.v1.FlatTensors.TensorsEntryR\x07tensors\x1a_\n\x0cTensorsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x129\n\x05value\x18\x02 \x01(\x0b2#.viam.service.mlmodel.v1.FlatTensorR\x05value:\x028\x01*`\n\tLabelType\x12\x1a\n\x16LABEL_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17LABEL_TYPE_TENSOR_VALUE\x10\x01\x12\x1a\n\x16LABEL_TYPE_TENSOR_AXIS\x10\x022\xbf\x03\n\x0eMLModelService\x12\x89\x01\n\x05Infer\x12%.viam.service.mlmodel.v1.InferRequest\x1a&.viam.service.mlmodel.v1.InferResponse"1\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/mlmodel/{name}/infer\x12\x95\x01\n\x08Metadata\x12(.viam.service.mlmodel.v1.MetadataRequest\x1a).viam.service.mlmodel.v1.MetadataResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/mlmodel/{name}/metadata\x12\x88\x01\n\tGetStatus\x12 .viam.common.v1.GetStatusRequest\x1a!.viam.common.v1.GetStatusResponse"6\x82\xd3\xe4\x93\x020\x12./viam/api/v1/service/mlmodel/{name}/get_statusBA\n\x1bcom.viam.service.mlmodel.v1Z"go.viam.com/api/service/mlmodel/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.mlmodel.v1.mlmodel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.viam.service.mlmodel.v1Z"go.viam.com/api/service/mlmodel/v1'
    _globals['_FLATTENSORDATAINT16'].fields_by_name['data']._loaded_options = None
    _globals['_FLATTENSORDATAINT16'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_FLATTENSORDATAUINT16'].fields_by_name['data']._loaded_options = None
    _globals['_FLATTENSORDATAUINT16'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_FLATTENSORDATAINT32'].fields_by_name['data']._loaded_options = None
    _globals['_FLATTENSORDATAINT32'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_FLATTENSORDATAUINT32'].fields_by_name['data']._loaded_options = None
    _globals['_FLATTENSORDATAUINT32'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_FLATTENSORDATAINT64'].fields_by_name['data']._loaded_options = None
    _globals['_FLATTENSORDATAINT64'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_FLATTENSORDATAUINT64'].fields_by_name['data']._loaded_options = None
    _globals['_FLATTENSORDATAUINT64'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_FLATTENSORDATAFLOAT'].fields_by_name['data']._loaded_options = None
    _globals['_FLATTENSORDATAFLOAT'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_FLATTENSORDATADOUBLE'].fields_by_name['data']._loaded_options = None
    _globals['_FLATTENSORDATADOUBLE'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_FLATTENSORS_TENSORSENTRY']._loaded_options = None
    _globals['_FLATTENSORS_TENSORSENTRY']._serialized_options = b'8\x01'
    _globals['_MLMODELSERVICE'].methods_by_name['Infer']._loaded_options = None
    _globals['_MLMODELSERVICE'].methods_by_name['Infer']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/mlmodel/{name}/infer'
    _globals['_MLMODELSERVICE'].methods_by_name['Metadata']._loaded_options = None
    _globals['_MLMODELSERVICE'].methods_by_name['Metadata']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/mlmodel/{name}/metadata'
    _globals['_MLMODELSERVICE'].methods_by_name['GetStatus']._loaded_options = None
    _globals['_MLMODELSERVICE'].methods_by_name['GetStatus']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./viam/api/v1/service/mlmodel/{name}/get_status'
    _globals['_LABELTYPE']._serialized_start = 2752
    _globals['_LABELTYPE']._serialized_end = 2848
    _globals['_INFERREQUEST']._serialized_start = 146
    _globals['_INFERREQUEST']._serialized_end = 320
    _globals['_INFERRESPONSE']._serialized_start = 322
    _globals['_INFERRESPONSE']._serialized_end = 445
    _globals['_METADATAREQUEST']._serialized_start = 447
    _globals['_METADATAREQUEST']._serialized_end = 531
    _globals['_METADATARESPONSE']._serialized_start = 533
    _globals['_METADATARESPONSE']._serialized_end = 614
    _globals['_METADATA']._serialized_start = 617
    _globals['_METADATA']._serialized_end = 839
    _globals['_TENSORINFO']._serialized_start = 842
    _globals['_TENSORINFO']._serialized_end = 1080
    _globals['_FILE']._serialized_start = 1082
    _globals['_FILE']._serialized_end = 1209
    _globals['_FLATTENSORDATAINT8']._serialized_start = 1211
    _globals['_FLATTENSORDATAINT8']._serialized_end = 1251
    _globals['_FLATTENSORDATAUINT8']._serialized_start = 1253
    _globals['_FLATTENSORDATAUINT8']._serialized_end = 1294
    _globals['_FLATTENSORDATAINT16']._serialized_start = 1296
    _globals['_FLATTENSORDATAINT16']._serialized_end = 1341
    _globals['_FLATTENSORDATAUINT16']._serialized_start = 1343
    _globals['_FLATTENSORDATAUINT16']._serialized_end = 1389
    _globals['_FLATTENSORDATAINT32']._serialized_start = 1391
    _globals['_FLATTENSORDATAINT32']._serialized_end = 1436
    _globals['_FLATTENSORDATAUINT32']._serialized_start = 1438
    _globals['_FLATTENSORDATAUINT32']._serialized_end = 1484
    _globals['_FLATTENSORDATAINT64']._serialized_start = 1486
    _globals['_FLATTENSORDATAINT64']._serialized_end = 1531
    _globals['_FLATTENSORDATAUINT64']._serialized_start = 1533
    _globals['_FLATTENSORDATAUINT64']._serialized_end = 1579
    _globals['_FLATTENSORDATAFLOAT']._serialized_start = 1581
    _globals['_FLATTENSORDATAFLOAT']._serialized_end = 1626
    _globals['_FLATTENSORDATADOUBLE']._serialized_start = 1628
    _globals['_FLATTENSORDATADOUBLE']._serialized_end = 1674
    _globals['_FLATTENSOR']._serialized_start = 1677
    _globals['_FLATTENSOR']._serialized_end = 2560
    _globals['_FLATTENSORS']._serialized_start = 2563
    _globals['_FLATTENSORS']._serialized_end = 2750
    _globals['_FLATTENSORS_TENSORSENTRY']._serialized_start = 2655
    _globals['_FLATTENSORS_TENSORSENTRY']._serialized_end = 2750
    _globals['_MLMODELSERVICE']._serialized_start = 2851
    _globals['_MLMODELSERVICE']._serialized_end = 3298