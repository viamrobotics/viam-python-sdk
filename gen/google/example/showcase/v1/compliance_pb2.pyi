"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class RepeatRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    @property
    def info(self) -> global___ComplianceData: ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        info : typing.Optional[global___ComplianceData] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info",b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info",b"info","name",b"name"]) -> None: ...
global___RepeatRequest = RepeatRequest

class RepeatResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> global___ComplianceData: ...
    def __init__(self,
        *,
        info : typing.Optional[global___ComplianceData] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info",b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info",b"info"]) -> None: ...
global___RepeatResponse = RepeatResponse

class ComplianceData(google.protobuf.message.Message):
    """ComplianceData is a message used for testing REST transcoding of
    different data types.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    F_STRING_FIELD_NUMBER: builtins.int
    F_INT32_FIELD_NUMBER: builtins.int
    F_SINT32_FIELD_NUMBER: builtins.int
    F_SFIXED32_FIELD_NUMBER: builtins.int
    F_UINT32_FIELD_NUMBER: builtins.int
    F_FIXED32_FIELD_NUMBER: builtins.int
    F_INT64_FIELD_NUMBER: builtins.int
    F_SINT64_FIELD_NUMBER: builtins.int
    F_SFIXED64_FIELD_NUMBER: builtins.int
    F_UINT64_FIELD_NUMBER: builtins.int
    F_FIXED64_FIELD_NUMBER: builtins.int
    F_DOUBLE_FIELD_NUMBER: builtins.int
    F_FLOAT_FIELD_NUMBER: builtins.int
    F_BOOL_FIELD_NUMBER: builtins.int
    F_BYTES_FIELD_NUMBER: builtins.int
    F_CHILD_FIELD_NUMBER: builtins.int
    P_STRING_FIELD_NUMBER: builtins.int
    P_INT32_FIELD_NUMBER: builtins.int
    P_DOUBLE_FIELD_NUMBER: builtins.int
    P_BOOL_FIELD_NUMBER: builtins.int
    P_CHILD_FIELD_NUMBER: builtins.int
    f_string: typing.Text = ...
    f_int32: builtins.int = ...
    f_sint32: builtins.int = ...
    f_sfixed32: builtins.int = ...
    f_uint32: builtins.int = ...
    f_fixed32: builtins.int = ...
    f_int64: builtins.int = ...
    f_sint64: builtins.int = ...
    f_sfixed64: builtins.int = ...
    f_uint64: builtins.int = ...
    f_fixed64: builtins.int = ...
    f_double: builtins.float = ...
    f_float: builtins.float = ...
    f_bool: builtins.bool = ...
    f_bytes: builtins.bytes = ...
    @property
    def f_child(self) -> global___ComplianceDataChild: ...
    p_string: typing.Text = ...
    p_int32: builtins.int = ...
    p_double: builtins.float = ...
    p_bool: builtins.bool = ...
    @property
    def p_child(self) -> global___ComplianceDataChild: ...
    def __init__(self,
        *,
        f_string : typing.Text = ...,
        f_int32 : builtins.int = ...,
        f_sint32 : builtins.int = ...,
        f_sfixed32 : builtins.int = ...,
        f_uint32 : builtins.int = ...,
        f_fixed32 : builtins.int = ...,
        f_int64 : builtins.int = ...,
        f_sint64 : builtins.int = ...,
        f_sfixed64 : builtins.int = ...,
        f_uint64 : builtins.int = ...,
        f_fixed64 : builtins.int = ...,
        f_double : builtins.float = ...,
        f_float : builtins.float = ...,
        f_bool : builtins.bool = ...,
        f_bytes : builtins.bytes = ...,
        f_child : typing.Optional[global___ComplianceDataChild] = ...,
        p_string : typing.Optional[typing.Text] = ...,
        p_int32 : typing.Optional[builtins.int] = ...,
        p_double : typing.Optional[builtins.float] = ...,
        p_bool : typing.Optional[builtins.bool] = ...,
        p_child : typing.Optional[global___ComplianceDataChild] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_p_bool",b"_p_bool","_p_child",b"_p_child","_p_double",b"_p_double","_p_int32",b"_p_int32","_p_string",b"_p_string","f_child",b"f_child","p_bool",b"p_bool","p_child",b"p_child","p_double",b"p_double","p_int32",b"p_int32","p_string",b"p_string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_p_bool",b"_p_bool","_p_child",b"_p_child","_p_double",b"_p_double","_p_int32",b"_p_int32","_p_string",b"_p_string","f_bool",b"f_bool","f_bytes",b"f_bytes","f_child",b"f_child","f_double",b"f_double","f_fixed32",b"f_fixed32","f_fixed64",b"f_fixed64","f_float",b"f_float","f_int32",b"f_int32","f_int64",b"f_int64","f_sfixed32",b"f_sfixed32","f_sfixed64",b"f_sfixed64","f_sint32",b"f_sint32","f_sint64",b"f_sint64","f_string",b"f_string","f_uint32",b"f_uint32","f_uint64",b"f_uint64","p_bool",b"p_bool","p_child",b"p_child","p_double",b"p_double","p_int32",b"p_int32","p_string",b"p_string"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_bool",b"_p_bool"]) -> typing.Optional[typing_extensions.Literal["p_bool"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_child",b"_p_child"]) -> typing.Optional[typing_extensions.Literal["p_child"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_double",b"_p_double"]) -> typing.Optional[typing_extensions.Literal["p_double"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_int32",b"_p_int32"]) -> typing.Optional[typing_extensions.Literal["p_int32"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_string",b"_p_string"]) -> typing.Optional[typing_extensions.Literal["p_string"]]: ...
global___ComplianceData = ComplianceData

class ComplianceDataChild(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    F_STRING_FIELD_NUMBER: builtins.int
    F_FLOAT_FIELD_NUMBER: builtins.int
    F_DOUBLE_FIELD_NUMBER: builtins.int
    F_BOOL_FIELD_NUMBER: builtins.int
    F_CHILD_FIELD_NUMBER: builtins.int
    P_STRING_FIELD_NUMBER: builtins.int
    P_FLOAT_FIELD_NUMBER: builtins.int
    P_DOUBLE_FIELD_NUMBER: builtins.int
    P_BOOL_FIELD_NUMBER: builtins.int
    P_CHILD_FIELD_NUMBER: builtins.int
    f_string: typing.Text = ...
    f_float: builtins.float = ...
    f_double: builtins.float = ...
    f_bool: builtins.bool = ...
    @property
    def f_child(self) -> global___ComplianceDataGrandchild: ...
    p_string: typing.Text = ...
    p_float: builtins.float = ...
    p_double: builtins.float = ...
    p_bool: builtins.bool = ...
    @property
    def p_child(self) -> global___ComplianceDataGrandchild: ...
    def __init__(self,
        *,
        f_string : typing.Text = ...,
        f_float : builtins.float = ...,
        f_double : builtins.float = ...,
        f_bool : builtins.bool = ...,
        f_child : typing.Optional[global___ComplianceDataGrandchild] = ...,
        p_string : typing.Optional[typing.Text] = ...,
        p_float : typing.Optional[builtins.float] = ...,
        p_double : typing.Optional[builtins.float] = ...,
        p_bool : typing.Optional[builtins.bool] = ...,
        p_child : typing.Optional[global___ComplianceDataGrandchild] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_p_bool",b"_p_bool","_p_child",b"_p_child","_p_double",b"_p_double","_p_float",b"_p_float","_p_string",b"_p_string","f_child",b"f_child","p_bool",b"p_bool","p_child",b"p_child","p_double",b"p_double","p_float",b"p_float","p_string",b"p_string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_p_bool",b"_p_bool","_p_child",b"_p_child","_p_double",b"_p_double","_p_float",b"_p_float","_p_string",b"_p_string","f_bool",b"f_bool","f_child",b"f_child","f_double",b"f_double","f_float",b"f_float","f_string",b"f_string","p_bool",b"p_bool","p_child",b"p_child","p_double",b"p_double","p_float",b"p_float","p_string",b"p_string"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_bool",b"_p_bool"]) -> typing.Optional[typing_extensions.Literal["p_bool"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_child",b"_p_child"]) -> typing.Optional[typing_extensions.Literal["p_child"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_double",b"_p_double"]) -> typing.Optional[typing_extensions.Literal["p_double"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_float",b"_p_float"]) -> typing.Optional[typing_extensions.Literal["p_float"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_p_string",b"_p_string"]) -> typing.Optional[typing_extensions.Literal["p_string"]]: ...
global___ComplianceDataChild = ComplianceDataChild

class ComplianceDataGrandchild(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    F_STRING_FIELD_NUMBER: builtins.int
    F_DOUBLE_FIELD_NUMBER: builtins.int
    F_BOOL_FIELD_NUMBER: builtins.int
    f_string: typing.Text = ...
    f_double: builtins.float = ...
    f_bool: builtins.bool = ...
    def __init__(self,
        *,
        f_string : typing.Text = ...,
        f_double : builtins.float = ...,
        f_bool : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["f_bool",b"f_bool","f_double",b"f_double","f_string",b"f_string"]) -> None: ...
global___ComplianceDataGrandchild = ComplianceDataGrandchild
