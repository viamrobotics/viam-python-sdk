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

class EchoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MESSAGE_FIELD_NUMBER: builtins.int
    message: typing.Text = ...
    def __init__(self,
        *,
        message : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message",b"message"]) -> None: ...
global___EchoRequest = EchoRequest

class EchoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MESSAGE_FIELD_NUMBER: builtins.int
    message: typing.Text = ...
    def __init__(self,
        *,
        message : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message",b"message"]) -> None: ...
global___EchoResponse = EchoResponse

class EchoMultipleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MESSAGE_FIELD_NUMBER: builtins.int
    message: typing.Text = ...
    def __init__(self,
        *,
        message : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message",b"message"]) -> None: ...
global___EchoMultipleRequest = EchoMultipleRequest

class EchoMultipleResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MESSAGE_FIELD_NUMBER: builtins.int
    message: typing.Text = ...
    def __init__(self,
        *,
        message : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message",b"message"]) -> None: ...
global___EchoMultipleResponse = EchoMultipleResponse

class EchoBiDiRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MESSAGE_FIELD_NUMBER: builtins.int
    message: typing.Text = ...
    def __init__(self,
        *,
        message : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message",b"message"]) -> None: ...
global___EchoBiDiRequest = EchoBiDiRequest

class EchoBiDiResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MESSAGE_FIELD_NUMBER: builtins.int
    message: typing.Text = ...
    def __init__(self,
        *,
        message : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message",b"message"]) -> None: ...
global___EchoBiDiResponse = EchoBiDiResponse
