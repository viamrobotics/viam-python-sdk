"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Device(google.protobuf.message.Message):
    """Device resource represents an instance of enterprise managed device in the
    property.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    TRAITS_FIELD_NUMBER: builtins.int
    PARENT_RELATIONS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the device. For example:
    "enterprises/XYZ/devices/123".
    """

    type: typing.Text = ...
    """Output only. Type of the device for general display purposes.
    For example: "THERMOSTAT". The device type should not be used to deduce or
    infer functionality of the actual device it is assigned to. Instead, use
    the returned traits for the device.
    """

    @property
    def traits(self) -> google.protobuf.struct_pb2.Struct:
        """Output only. Device traits."""
        pass
    @property
    def parent_relations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ParentRelation]:
        """Assignee details of the device."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        type : typing.Text = ...,
        traits : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        parent_relations : typing.Optional[typing.Iterable[global___ParentRelation]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["traits",b"traits"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","parent_relations",b"parent_relations","traits",b"traits","type",b"type"]) -> None: ...
global___Device = Device

class ParentRelation(google.protobuf.message.Message):
    """Represents device relationships, for instance, structure/room to which the
    device is assigned to. For now this is only filled in the enterprise flow.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Output only. The name of the relation -- e.g., structure/room where the
    device is assigned to. For example: "enterprises/XYZ/structures/ABC" or
    "enterprises/XYZ/structures/ABC/rooms/123"
    """

    display_name: typing.Text = ...
    """Output only. The custom name of the relation -- e.g., structure/room where
    the device is assigned to.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        display_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name","parent",b"parent"]) -> None: ...
global___ParentRelation = ParentRelation
