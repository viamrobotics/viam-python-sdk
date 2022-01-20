"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Structure(google.protobuf.message.Message):
    """Structure resource represents an instance of enterprise managed home or hotel
    room.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TRAITS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The resource name of the structure. For example:
    "enterprises/XYZ/structures/ABC".
    """

    @property
    def traits(self) -> google.protobuf.struct_pb2.Struct:
        """Structure traits."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        traits : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["traits",b"traits"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","traits",b"traits"]) -> None: ...
global___Structure = Structure

class Room(google.protobuf.message.Message):
    """Room resource represents an instance of sub-space within a structure such as
    rooms in a hotel suite or rental apartment.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TRAITS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The resource name of the room. For example:
    "enterprises/XYZ/structures/ABC/rooms/123".
    """

    @property
    def traits(self) -> google.protobuf.struct_pb2.Struct:
        """Room traits."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        traits : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["traits",b"traits"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","traits",b"traits"]) -> None: ...
global___Room = Room
