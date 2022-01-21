"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.devtools.artifactregistry.v1beta2.tag_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _VersionView:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _VersionViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VersionView.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    VERSION_VIEW_UNSPECIFIED: VersionView.ValueType = ...  # 0
    """The default / unset value.
    The API will default to the BASIC view.
    """

    BASIC: VersionView.ValueType = ...  # 1
    """Includes basic information about the version, but not any related tags."""

    FULL: VersionView.ValueType = ...  # 2
    """Include everything."""

class VersionView(_VersionView, metaclass=_VersionViewEnumTypeWrapper):
    """The view, which determines what version information is returned in a
    response.
    """
    pass

VERSION_VIEW_UNSPECIFIED: VersionView.ValueType = ...  # 0
"""The default / unset value.
The API will default to the BASIC view.
"""

BASIC: VersionView.ValueType = ...  # 1
"""Includes basic information about the version, but not any related tags."""

FULL: VersionView.ValueType = ...  # 2
"""Include everything."""

global___VersionView = VersionView


class Version(google.protobuf.message.Message):
    """The body of a version resource. A version resource represents a
    collection of components, such as files and other data. This may correspond
    to a version in many package management schemes.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    RELATED_TAGS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the version, for example:
    "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/art1".
    If the package or version ID parts contain slashes, the slashes are
    escaped.
    """

    description: typing.Text = ...
    """Optional. Description of the version, as specified in its metadata."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the version was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the version was last updated."""
        pass
    @property
    def related_tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.devtools.artifactregistry.v1beta2.tag_pb2.Tag]:
        """Output only. A list of related tags. Will contain up to 100 tags that
        reference this version.
        """
        pass
    @property
    def metadata(self) -> google.protobuf.struct_pb2.Struct:
        """Output only. Repository-specific Metadata stored against this version.
        The fields returned are defined by the underlying repository-specific
        resource. Currently, the only resource in use is
        [DockerImage][google.devtools.artifactregistry.v1.DockerImage]
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        description : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        related_tags : typing.Optional[typing.Iterable[google.devtools.artifactregistry.v1beta2.tag_pb2.Tag]] = ...,
        metadata : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","metadata",b"metadata","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","description",b"description","metadata",b"metadata","name",b"name","related_tags",b"related_tags","update_time",b"update_time"]) -> None: ...
global___Version = Version

class ListVersionsRequest(google.protobuf.message.Message):
    """The request to list versions."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The name of the parent resource whose versions will be listed."""

    page_size: builtins.int = ...
    """The maximum number of versions to return. Maximum page size is 1,000."""

    page_token: typing.Text = ...
    """The next_page_token value returned from a previous list request, if any."""

    view: global___VersionView.ValueType = ...
    """The view that should be returned in the response."""

    order_by: typing.Text = ...
    """Optional. The field to order the results by."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        view : global___VersionView.ValueType = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["order_by",b"order_by","page_size",b"page_size","page_token",b"page_token","parent",b"parent","view",b"view"]) -> None: ...
global___ListVersionsRequest = ListVersionsRequest

class ListVersionsResponse(google.protobuf.message.Message):
    """The response from listing versions."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Version]:
        """The versions returned."""
        pass
    next_page_token: typing.Text = ...
    """The token to retrieve the next page of versions, or empty if there are no
    more versions to return.
    """

    def __init__(self,
        *,
        versions : typing.Optional[typing.Iterable[global___Version]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","versions",b"versions"]) -> None: ...
global___ListVersionsResponse = ListVersionsResponse

class GetVersionRequest(google.protobuf.message.Message):
    """The request to retrieve a version."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the version to retrieve."""

    view: global___VersionView.ValueType = ...
    """The view that should be returned in the response."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        view : global___VersionView.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","view",b"view"]) -> None: ...
global___GetVersionRequest = GetVersionRequest

class DeleteVersionRequest(google.protobuf.message.Message):
    """The request to delete a version."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FORCE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the version to delete."""

    force: builtins.bool = ...
    """By default, a version that is tagged may not be deleted. If force=true, the
    version and any tags pointing to the version are deleted.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        force : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["force",b"force","name",b"name"]) -> None: ...
global___DeleteVersionRequest = DeleteVersionRequest
