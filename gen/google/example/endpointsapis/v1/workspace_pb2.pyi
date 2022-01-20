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

class Workspace(google.protobuf.message.Message):
    """Presents a workspace"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The Workspace name in the format of "projects/*/locations/*/workspaces/*"."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___Workspace = Workspace

class ListWorkspacesRequest(google.protobuf.message.Message):
    """Request message for listing Workspaces."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The parent used for listing. It should have the format of
    `projects/{number}/locations/{location}`.
    """

    page_size: builtins.int = ...
    """The page size for list pagination."""

    page_token: typing.Text = ...
    """The page token for list pagination."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListWorkspacesRequest = ListWorkspacesRequest

class ListWorkspacesResponse(google.protobuf.message.Message):
    """A list of workspaces."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ITEMS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Workspace]:
        """The list of workspaces."""
        pass
    next_page_token: typing.Text = ...
    """The next page token for list pagination."""

    def __init__(self,
        *,
        items : typing.Optional[typing.Iterable[global___Workspace]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["items",b"items","next_page_token",b"next_page_token"]) -> None: ...
global___ListWorkspacesResponse = ListWorkspacesResponse

class GetWorkspaceRequest(google.protobuf.message.Message):
    """Request message for retrieving a Workspace."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the Workspace to retrieve."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetWorkspaceRequest = GetWorkspaceRequest

class CreateWorkspaceRequest(google.protobuf.message.Message):
    """Request message for creating a Workspace."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    WORKSPACE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The namespace in which the Workspace should be created."""

    @property
    def workspace(self) -> global___Workspace:
        """The Workspace instance to create."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        workspace : typing.Optional[global___Workspace] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["workspace",b"workspace"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","workspace",b"workspace"]) -> None: ...
global___CreateWorkspaceRequest = CreateWorkspaceRequest

class UpdateWorkspaceRequest(google.protobuf.message.Message):
    """Request message for replacing a Workspace."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    WORKSPACE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the Workspace being replaced."""

    @property
    def workspace(self) -> global___Workspace:
        """The Workspace object being replaced."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        workspace : typing.Optional[global___Workspace] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["workspace",b"workspace"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","workspace",b"workspace"]) -> None: ...
global___UpdateWorkspaceRequest = UpdateWorkspaceRequest

class DeleteWorkspaceRequest(google.protobuf.message.Message):
    """Request message for deleting a Workspace."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the Workspace to delete."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteWorkspaceRequest = DeleteWorkspaceRequest
