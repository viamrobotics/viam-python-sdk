"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.retail.v2beta.catalog_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ListCatalogsRequest(google.protobuf.message.Message):
    """Request for
    [CatalogService.ListCatalogs][google.cloud.retail.v2beta.CatalogService.ListCatalogs]
    method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The account resource name with an associated location.

    If the caller does not have permission to list
    [Catalog][google.cloud.retail.v2beta.Catalog]s under this location,
    regardless of whether or not this location exists, a PERMISSION_DENIED
    error is returned.
    """

    page_size: builtins.int = ...
    """Maximum number of [Catalog][google.cloud.retail.v2beta.Catalog]s to return.
    If unspecified, defaults to 50. The maximum allowed value is 1000. Values
    above 1000 will be coerced to 1000.

    If this field is negative, an INVALID_ARGUMENT is returned.
    """

    page_token: typing.Text = ...
    """A page token
    [ListCatalogsResponse.next_page_token][google.cloud.retail.v2beta.ListCatalogsResponse.next_page_token],
    received from a previous
    [CatalogService.ListCatalogs][google.cloud.retail.v2beta.CatalogService.ListCatalogs]
    call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to
    [CatalogService.ListCatalogs][google.cloud.retail.v2beta.CatalogService.ListCatalogs]
    must match the call that provided the page token. Otherwise, an
    INVALID_ARGUMENT error is returned.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListCatalogsRequest = ListCatalogsRequest

class ListCatalogsResponse(google.protobuf.message.Message):
    """Response for
    [CatalogService.ListCatalogs][google.cloud.retail.v2beta.CatalogService.ListCatalogs]
    method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CATALOGS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def catalogs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.retail.v2beta.catalog_pb2.Catalog]:
        """All the customer's [Catalog][google.cloud.retail.v2beta.Catalog]s."""
        pass
    next_page_token: typing.Text = ...
    """A token that can be sent as
    [ListCatalogsRequest.page_token][google.cloud.retail.v2beta.ListCatalogsRequest.page_token]
    to retrieve the next page. If this field is omitted, there are no
    subsequent pages.
    """

    def __init__(self,
        *,
        catalogs : typing.Optional[typing.Iterable[google.cloud.retail.v2beta.catalog_pb2.Catalog]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalogs",b"catalogs","next_page_token",b"next_page_token"]) -> None: ...
global___ListCatalogsResponse = ListCatalogsResponse

class UpdateCatalogRequest(google.protobuf.message.Message):
    """Request for
    [CatalogService.UpdateCatalog][google.cloud.retail.v2beta.CatalogService.UpdateCatalog]
    method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CATALOG_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def catalog(self) -> google.cloud.retail.v2beta.catalog_pb2.Catalog:
        """Required. The [Catalog][google.cloud.retail.v2beta.Catalog] to update.

        If the caller does not have permission to update the
        [Catalog][google.cloud.retail.v2beta.Catalog], regardless of whether or not
        it exists, a PERMISSION_DENIED error is returned.

        If the [Catalog][google.cloud.retail.v2beta.Catalog] to update does not
        exist, a NOT_FOUND error is returned.
        """
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Indicates which fields in the provided
        [Catalog][google.cloud.retail.v2beta.Catalog] to update.

        If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
        is returned.
        """
        pass
    def __init__(self,
        *,
        catalog : typing.Optional[google.cloud.retail.v2beta.catalog_pb2.Catalog] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["catalog",b"catalog","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog",b"catalog","update_mask",b"update_mask"]) -> None: ...
global___UpdateCatalogRequest = UpdateCatalogRequest

class SetDefaultBranchRequest(google.protobuf.message.Message):
    """Request message to set a specified branch as new default_branch."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CATALOG_FIELD_NUMBER: builtins.int
    BRANCH_ID_FIELD_NUMBER: builtins.int
    NOTE_FIELD_NUMBER: builtins.int
    catalog: typing.Text = ...
    """Full resource name of the catalog, such as
    `projects/*/locations/global/catalogs/default_catalog`.
    """

    branch_id: typing.Text = ...
    """The final component of the resource name of a branch.

    This field must be one of "0", "1" or "2". Otherwise, an INVALID_ARGUMENT
    error is returned.
    """

    note: typing.Text = ...
    """Some note on this request, this can be retrieved by
    [CatalogService.GetDefaultBranch][google.cloud.retail.v2beta.CatalogService.GetDefaultBranch]
    before next valid default branch set occurs.

    This field must be a UTF-8 encoded string with a length limit of 1,000
    characters. Otherwise, an INVALID_ARGUMENT error is returned.
    """

    def __init__(self,
        *,
        catalog : typing.Text = ...,
        branch_id : typing.Text = ...,
        note : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["branch_id",b"branch_id","catalog",b"catalog","note",b"note"]) -> None: ...
global___SetDefaultBranchRequest = SetDefaultBranchRequest

class GetDefaultBranchRequest(google.protobuf.message.Message):
    """Request message to show which branch is currently the default branch."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CATALOG_FIELD_NUMBER: builtins.int
    catalog: typing.Text = ...
    """The parent catalog resource name, such as
    `projects/*/locations/global/catalogs/default_catalog`.
    """

    def __init__(self,
        *,
        catalog : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog",b"catalog"]) -> None: ...
global___GetDefaultBranchRequest = GetDefaultBranchRequest

class GetDefaultBranchResponse(google.protobuf.message.Message):
    """Response message of
    [CatalogService.GetDefaultBranch][google.cloud.retail.v2beta.CatalogService.GetDefaultBranch].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BRANCH_FIELD_NUMBER: builtins.int
    SET_TIME_FIELD_NUMBER: builtins.int
    NOTE_FIELD_NUMBER: builtins.int
    branch: typing.Text = ...
    """Full resource name of the branch id currently set as default branch."""

    @property
    def set_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when this branch is set to default."""
        pass
    note: typing.Text = ...
    """This corresponds to
    [SetDefaultBranchRequest.note][google.cloud.retail.v2beta.SetDefaultBranchRequest.note]
    field, when this branch was set as default.
    """

    def __init__(self,
        *,
        branch : typing.Text = ...,
        set_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        note : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["set_time",b"set_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["branch",b"branch","note",b"note","set_time",b"set_time"]) -> None: ...
global___GetDefaultBranchResponse = GetDefaultBranchResponse
