"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
from .... import common
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetSensorsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetSensorsRequest = GetSensorsRequest

class GetSensorsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SENSOR_NAMES_FIELD_NUMBER: builtins.int

    @property
    def sensor_names(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.ResourceName]:
        ...

    def __init__(self, *, sensor_names: collections.abc.Iterable[common.v1.common_pb2.ResourceName] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['sensor_names', b'sensor_names']) -> None:
        ...
global___GetSensorsResponse = GetSensorsResponse

class GetReadingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    SENSOR_NAMES_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def sensor_names(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.ResourceName]:
        ...

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., sensor_names: collections.abc.Iterable[common.v1.common_pb2.ResourceName] | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'sensor_names', b'sensor_names']) -> None:
        ...
global___GetReadingsRequest = GetReadingsRequest

class Readings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ReadingsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> google.protobuf.struct_pb2.Value:
            ...

        def __init__(self, *, key: builtins.str=..., value: google.protobuf.struct_pb2.Value | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    NAME_FIELD_NUMBER: builtins.int
    READINGS_FIELD_NUMBER: builtins.int

    @property
    def name(self) -> common.v1.common_pb2.ResourceName:
        ...

    @property
    def readings(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, google.protobuf.struct_pb2.Value]:
        ...

    def __init__(self, *, name: common.v1.common_pb2.ResourceName | None=..., readings: collections.abc.Mapping[builtins.str, google.protobuf.struct_pb2.Value] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['name', b'name']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'readings', b'readings']) -> None:
        ...
global___Readings = Readings

class GetReadingsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    READINGS_FIELD_NUMBER: builtins.int

    @property
    def readings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Readings]:
        ...

    def __init__(self, *, readings: collections.abc.Iterable[global___Readings] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['readings', b'readings']) -> None:
        ...
global___GetReadingsResponse = GetReadingsResponse