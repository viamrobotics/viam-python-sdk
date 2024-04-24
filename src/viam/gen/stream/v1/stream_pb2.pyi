"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListStreamsRequest(google.protobuf.message.Message):
    """ListStreamsRequest requests all streams registered."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___ListStreamsRequest = ListStreamsRequest

@typing.final
class ListStreamsResponse(google.protobuf.message.Message):
    """A ListStreamsResponse details streams registered."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMES_FIELD_NUMBER: builtins.int

    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, names: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['names', b'names']) -> None:
        ...
global___ListStreamsResponse = ListStreamsResponse

@typing.final
class AddStreamRequest(google.protobuf.message.Message):
    """A AddStreamRequest requests the given stream be added to the connection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name']) -> None:
        ...
global___AddStreamRequest = AddStreamRequest

@typing.final
class AddStreamResponse(google.protobuf.message.Message):
    """AddStreamResponse is returned after a successful AddStreamRequest."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___AddStreamResponse = AddStreamResponse

@typing.final
class RemoveStreamRequest(google.protobuf.message.Message):
    """A RemoveStreamRequest requests the given stream be removed from the connection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name']) -> None:
        ...
global___RemoveStreamRequest = RemoveStreamRequest

@typing.final
class RemoveStreamResponse(google.protobuf.message.Message):
    """RemoveStreamResponse is returned after a successful RemoveStreamRequest."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___RemoveStreamResponse = RemoveStreamResponse