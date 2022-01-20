"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TopicConstant(google.protobuf.message.Message):
    """Proto file describing the Topic Constant resource.

    Use topics to target or exclude placements in the Google Display Network
    based on the category into which the placement falls (for example,
    "Pets & Animals/Pets/Dogs").
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    TOPIC_CONSTANT_PARENT_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Output only. The resource name of the topic constant.
    topic constant resource names have the form:

    `topicConstants/{topic_id}`
    """

    id: builtins.int = ...
    """Output only. The ID of the topic."""

    topic_constant_parent: typing.Text = ...
    """Output only. Resource name of parent of the topic constant."""

    @property
    def path(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Output only. The category to target or exclude. Each subsequent element in the array
        describes a more specific sub-category. For example,
        {"Pets & Animals", "Pets", "Dogs"} represents the
        "Pets & Animals/Pets/Dogs" category. List of available topic categories at
        https://developers.google.com/adwords/api/docs/appendix/verticals
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : typing.Optional[builtins.int] = ...,
        topic_constant_parent : typing.Optional[typing.Text] = ...,
        path : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_id",b"_id","_topic_constant_parent",b"_topic_constant_parent","id",b"id","topic_constant_parent",b"topic_constant_parent"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_id",b"_id","_topic_constant_parent",b"_topic_constant_parent","id",b"id","path",b"path","resource_name",b"resource_name","topic_constant_parent",b"topic_constant_parent"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_topic_constant_parent",b"_topic_constant_parent"]) -> typing.Optional[typing_extensions.Literal["topic_constant_parent"]]: ...
global___TopicConstant = TopicConstant
