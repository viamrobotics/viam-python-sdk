"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _LabelType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LabelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LabelType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LABEL_TYPE_UNSPECIFIED: _LabelType.ValueType
    LABEL_TYPE_TENSOR_VALUE: _LabelType.ValueType
    'the value of the arrays/tensor is the label index'
    LABEL_TYPE_TENSOR_AXIS: _LabelType.ValueType
    'the position of the tensor value in the axis is the label index'

class LabelType(_LabelType, metaclass=_LabelTypeEnumTypeWrapper):
    ...
LABEL_TYPE_UNSPECIFIED: LabelType.ValueType
LABEL_TYPE_TENSOR_VALUE: LabelType.ValueType
'the value of the arrays/tensor is the label index'
LABEL_TYPE_TENSOR_AXIS: LabelType.ValueType
'the position of the tensor value in the axis is the label index'
global___LabelType = LabelType

@typing.final
class InferRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    INPUT_TENSORS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the model service'

    @property
    def input_tensors(self) -> global___FlatTensors:
        """the input data is provided as set of named flat tensors"""

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., input_tensors: global___FlatTensors | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra', 'input_tensors', b'input_tensors']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'input_tensors', b'input_tensors', 'name', b'name']) -> None:
        ...
global___InferRequest = InferRequest

@typing.final
class InferResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OUTPUT_TENSORS_FIELD_NUMBER: builtins.int

    @property
    def output_tensors(self) -> global___FlatTensors:
        """the output data is provided as a set of named flat tensors"""

    def __init__(self, *, output_tensors: global___FlatTensors | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['output_tensors', b'output_tensors']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['output_tensors', b'output_tensors']) -> None:
        ...
global___InferResponse = InferResponse

@typing.final
class MetadataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the model service'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___MetadataRequest = MetadataRequest

@typing.final
class MetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    METADATA_FIELD_NUMBER: builtins.int

    @property
    def metadata(self) -> global___Metadata:
        """this is the metadata associated with the ML model"""

    def __init__(self, *, metadata: global___Metadata | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['metadata', b'metadata']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['metadata', b'metadata']) -> None:
        ...
global___MetadataResponse = MetadataResponse

@typing.final
class Metadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    INPUT_INFO_FIELD_NUMBER: builtins.int
    OUTPUT_INFO_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the model'
    type: builtins.str
    'type of model e.g. object_detector, text_classifier'
    description: builtins.str
    'description of the model'

    @property
    def input_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorInfo]:
        """the necessary input arrays/tensors for an inference, order matters"""

    @property
    def output_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorInfo]:
        """the output arrays/tensors of the model, order matters"""

    def __init__(self, *, name: builtins.str=..., type: builtins.str=..., description: builtins.str=..., input_info: collections.abc.Iterable[global___TensorInfo] | None=..., output_info: collections.abc.Iterable[global___TensorInfo] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['description', b'description', 'input_info', b'input_info', 'name', b'name', 'output_info', b'output_info', 'type', b'type']) -> None:
        ...
global___Metadata = Metadata

@typing.final
class TensorInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DATA_TYPE_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    ASSOCIATED_FILES_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the data in the array/tensor'
    description: builtins.str
    'description of the data in the array/tensor'
    data_type: builtins.str
    'data type of the array/tensor, e.g. float32, float64, uint8'

    @property
    def shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """shape of the array/tensor (-1 for unknown)"""

    @property
    def associated_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]:
        """files associated with the array/tensor, like for category labels"""

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """anything else you want to say"""

    def __init__(self, *, name: builtins.str=..., description: builtins.str=..., data_type: builtins.str=..., shape: collections.abc.Iterable[builtins.int] | None=..., associated_files: collections.abc.Iterable[global___File] | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['associated_files', b'associated_files', 'data_type', b'data_type', 'description', b'description', 'extra', b'extra', 'name', b'name', 'shape', b'shape']) -> None:
        ...
global___TensorInfo = TensorInfo

@typing.final
class File(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABEL_TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the file, with file extension'
    description: builtins.str
    'description of what the file contains'
    label_type: global___LabelType.ValueType
    'How to associate the arrays/tensors to the labels in the file'

    def __init__(self, *, name: builtins.str=..., description: builtins.str=..., label_type: global___LabelType.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['description', b'description', 'label_type', b'label_type', 'name', b'name']) -> None:
        ...
global___File = File

@typing.final
class FlatTensorDataInt8(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes

    def __init__(self, *, data: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataInt8 = FlatTensorDataInt8

@typing.final
class FlatTensorDataUInt8(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes

    def __init__(self, *, data: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataUInt8 = FlatTensorDataUInt8

@typing.final
class FlatTensorDataInt16(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int

    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """packs two 16-bit numbers per entry - explicitly little-endian
        so big-endian producers/consumers must compensate
        """

    def __init__(self, *, data: collections.abc.Iterable[builtins.int] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataInt16 = FlatTensorDataInt16

@typing.final
class FlatTensorDataUInt16(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int

    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """packs two 16-bit numbers per entry - explicitly little-endian
        so big-endian producers/consumers must compensate
        """

    def __init__(self, *, data: collections.abc.Iterable[builtins.int] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataUInt16 = FlatTensorDataUInt16

@typing.final
class FlatTensorDataInt32(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int

    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        ...

    def __init__(self, *, data: collections.abc.Iterable[builtins.int] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataInt32 = FlatTensorDataInt32

@typing.final
class FlatTensorDataUInt32(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int

    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        ...

    def __init__(self, *, data: collections.abc.Iterable[builtins.int] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataUInt32 = FlatTensorDataUInt32

@typing.final
class FlatTensorDataInt64(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int

    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        ...

    def __init__(self, *, data: collections.abc.Iterable[builtins.int] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataInt64 = FlatTensorDataInt64

@typing.final
class FlatTensorDataUInt64(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int

    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        ...

    def __init__(self, *, data: collections.abc.Iterable[builtins.int] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataUInt64 = FlatTensorDataUInt64

@typing.final
class FlatTensorDataFloat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int

    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        ...

    def __init__(self, *, data: collections.abc.Iterable[builtins.float] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataFloat = FlatTensorDataFloat

@typing.final
class FlatTensorDataDouble(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int

    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        ...

    def __init__(self, *, data: collections.abc.Iterable[builtins.float] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data', b'data']) -> None:
        ...
global___FlatTensorDataDouble = FlatTensorDataDouble

@typing.final
class FlatTensor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SHAPE_FIELD_NUMBER: builtins.int
    INT8_TENSOR_FIELD_NUMBER: builtins.int
    UINT8_TENSOR_FIELD_NUMBER: builtins.int
    INT16_TENSOR_FIELD_NUMBER: builtins.int
    UINT16_TENSOR_FIELD_NUMBER: builtins.int
    INT32_TENSOR_FIELD_NUMBER: builtins.int
    UINT32_TENSOR_FIELD_NUMBER: builtins.int
    INT64_TENSOR_FIELD_NUMBER: builtins.int
    UINT64_TENSOR_FIELD_NUMBER: builtins.int
    FLOAT_TENSOR_FIELD_NUMBER: builtins.int
    DOUBLE_TENSOR_FIELD_NUMBER: builtins.int

    @property
    def shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """the shape of the provided tensor as a list of integer extents"""

    @property
    def int8_tensor(self) -> global___FlatTensorDataInt8:
        ...

    @property
    def uint8_tensor(self) -> global___FlatTensorDataUInt8:
        ...

    @property
    def int16_tensor(self) -> global___FlatTensorDataInt16:
        ...

    @property
    def uint16_tensor(self) -> global___FlatTensorDataUInt16:
        ...

    @property
    def int32_tensor(self) -> global___FlatTensorDataInt32:
        ...

    @property
    def uint32_tensor(self) -> global___FlatTensorDataUInt32:
        ...

    @property
    def int64_tensor(self) -> global___FlatTensorDataInt64:
        ...

    @property
    def uint64_tensor(self) -> global___FlatTensorDataUInt64:
        ...

    @property
    def float_tensor(self) -> global___FlatTensorDataFloat:
        ...

    @property
    def double_tensor(self) -> global___FlatTensorDataDouble:
        ...

    def __init__(self, *, shape: collections.abc.Iterable[builtins.int] | None=..., int8_tensor: global___FlatTensorDataInt8 | None=..., uint8_tensor: global___FlatTensorDataUInt8 | None=..., int16_tensor: global___FlatTensorDataInt16 | None=..., uint16_tensor: global___FlatTensorDataUInt16 | None=..., int32_tensor: global___FlatTensorDataInt32 | None=..., uint32_tensor: global___FlatTensorDataUInt32 | None=..., int64_tensor: global___FlatTensorDataInt64 | None=..., uint64_tensor: global___FlatTensorDataUInt64 | None=..., float_tensor: global___FlatTensorDataFloat | None=..., double_tensor: global___FlatTensorDataDouble | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['double_tensor', b'double_tensor', 'float_tensor', b'float_tensor', 'int16_tensor', b'int16_tensor', 'int32_tensor', b'int32_tensor', 'int64_tensor', b'int64_tensor', 'int8_tensor', b'int8_tensor', 'tensor', b'tensor', 'uint16_tensor', b'uint16_tensor', 'uint32_tensor', b'uint32_tensor', 'uint64_tensor', b'uint64_tensor', 'uint8_tensor', b'uint8_tensor']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['double_tensor', b'double_tensor', 'float_tensor', b'float_tensor', 'int16_tensor', b'int16_tensor', 'int32_tensor', b'int32_tensor', 'int64_tensor', b'int64_tensor', 'int8_tensor', b'int8_tensor', 'shape', b'shape', 'tensor', b'tensor', 'uint16_tensor', b'uint16_tensor', 'uint32_tensor', b'uint32_tensor', 'uint64_tensor', b'uint64_tensor', 'uint8_tensor', b'uint8_tensor']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['tensor', b'tensor']) -> typing.Literal['int8_tensor', 'uint8_tensor', 'int16_tensor', 'uint16_tensor', 'int32_tensor', 'uint32_tensor', 'int64_tensor', 'uint64_tensor', 'float_tensor', 'double_tensor'] | None:
        ...
global___FlatTensor = FlatTensor

@typing.final
class FlatTensors(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TensorsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___FlatTensor:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___FlatTensor | None=...) -> None:
            ...

        def HasField(self, field_name: typing.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    TENSORS_FIELD_NUMBER: builtins.int

    @property
    def tensors(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___FlatTensor]:
        """A name-indexed collection of flat tensor objects"""

    def __init__(self, *, tensors: collections.abc.Mapping[builtins.str, global___FlatTensor] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['tensors', b'tensors']) -> None:
        ...
global___FlatTensors = FlatTensors