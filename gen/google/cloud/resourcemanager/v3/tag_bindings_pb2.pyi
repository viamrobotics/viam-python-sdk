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

class TagBinding(google.protobuf.message.Message):
    """A TagBinding represents a connection between a TagValue and a cloud
    resource (currently project, folder, or organization). Once a TagBinding is
    created, the TagValue is applied to all the descendants of the cloud
    resource.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    TAG_VALUE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The name of the TagBinding. This is a String of the form:
    `tagBindings/{full-resource-name}/{tag-value-name}` (e.g.
    `tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F123/tagValues/456`).
    """

    parent: typing.Text = ...
    """The full resource name of the resource the TagValue is bound to.
    E.g. `//cloudresourcemanager.googleapis.com/projects/123`
    """

    tag_value: typing.Text = ...
    """The TagValue of the TagBinding.
    Must be of the form `tagValues/456`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        parent : typing.Text = ...,
        tag_value : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","parent",b"parent","tag_value",b"tag_value"]) -> None: ...
global___TagBinding = TagBinding

class CreateTagBindingMetadata(google.protobuf.message.Message):
    """Runtime operation information for creating a TagValue."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___CreateTagBindingMetadata = CreateTagBindingMetadata

class CreateTagBindingRequest(google.protobuf.message.Message):
    """The request message to create a TagBinding."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TAG_BINDING_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    @property
    def tag_binding(self) -> global___TagBinding:
        """Required. The TagBinding to be created."""
        pass
    validate_only: builtins.bool = ...
    """Optional. Set to true to perform the validations necessary for creating the resource,
    but not actually perform the action.
    """

    def __init__(self,
        *,
        tag_binding : typing.Optional[global___TagBinding] = ...,
        validate_only : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tag_binding",b"tag_binding"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tag_binding",b"tag_binding","validate_only",b"validate_only"]) -> None: ...
global___CreateTagBindingRequest = CreateTagBindingRequest

class DeleteTagBindingMetadata(google.protobuf.message.Message):
    """Runtime operation information for deleting a TagBinding."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___DeleteTagBindingMetadata = DeleteTagBindingMetadata

class DeleteTagBindingRequest(google.protobuf.message.Message):
    """The request message to delete a TagBinding."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the TagBinding. This is a String of the form:
    `tagBindings/{id}` (e.g.
    `tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F123/tagValues/456`).
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteTagBindingRequest = DeleteTagBindingRequest

class ListTagBindingsRequest(google.protobuf.message.Message):
    """The request message to list all TagBindings for a parent."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The full resource name of a resource for which you want to list existing
    TagBindings.
    E.g. "//cloudresourcemanager.googleapis.com/projects/123"
    """

    page_size: builtins.int = ...
    """Optional. The maximum number of TagBindings to return in the response. The server
    allows a maximum of 300 TagBindings to return. If unspecified, the server
    will use 100 as the default.
    """

    page_token: typing.Text = ...
    """Optional. A pagination token returned from a previous call to `ListTagBindings`
    that indicates where this listing should continue from.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListTagBindingsRequest = ListTagBindingsRequest

class ListTagBindingsResponse(google.protobuf.message.Message):
    """The ListTagBindings response."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TAG_BINDINGS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def tag_bindings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TagBinding]:
        """A possibly paginated list of TagBindings for the specified TagValue or
        resource.
        """
        pass
    next_page_token: typing.Text = ...
    """Pagination token.

    If the result set is too large to fit in a single response, this token
    is returned. It encodes the position of the current result cursor.
    Feeding this value into a new list request with the `page_token` parameter
    gives the next page of the results.

    When `next_page_token` is not filled in, there is no next page and
    the list returned is the last page in the result set.

    Pagination tokens have a limited lifetime.
    """

    def __init__(self,
        *,
        tag_bindings : typing.Optional[typing.Iterable[global___TagBinding]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","tag_bindings",b"tag_bindings"]) -> None: ...
global___ListTagBindingsResponse = ListTagBindingsResponse
