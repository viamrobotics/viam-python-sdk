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

class CustomParameter(google.protobuf.message.Message):
    """Proto file describing CustomParameter and operation

    A mapping that can be used by custom parameter tags in a
    `tracking_url_template`, `final_urls`, or `mobile_final_urls`.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: typing.Text = ...
    """The key matching the parameter tag name."""

    value: typing.Text = ...
    """The value to be substituted."""

    def __init__(self,
        *,
        key : typing.Optional[typing.Text] = ...,
        value : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_key",b"_key","_value",b"_value","key",b"key","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_key",b"_key","_value",b"_value","key",b"key","value",b"value"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_key",b"_key"]) -> typing.Optional[typing_extensions.Literal["key"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_value",b"_value"]) -> typing.Optional[typing_extensions.Literal["value"]]: ...
global___CustomParameter = CustomParameter
