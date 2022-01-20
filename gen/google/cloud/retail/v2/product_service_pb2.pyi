"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.retail.v2.product_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateProductRequest(google.protobuf.message.Message):
    """Request message for [CreateProduct][] method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PRODUCT_FIELD_NUMBER: builtins.int
    PRODUCT_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent catalog resource name, such as
    `projects/*/locations/global/catalogs/default_catalog/branches/default_branch`.
    """

    @property
    def product(self) -> google.cloud.retail.v2.product_pb2.Product:
        """Required. The [Product][google.cloud.retail.v2.Product] to create."""
        pass
    product_id: typing.Text = ...
    """Required. The ID to use for the [Product][google.cloud.retail.v2.Product],
    which will become the final component of the
    [Product.name][google.cloud.retail.v2.Product.name].

    If the caller does not have permission to create the
    [Product][google.cloud.retail.v2.Product], regardless of whether or not it
    exists, a PERMISSION_DENIED error is returned.

    This field must be unique among all
    [Product][google.cloud.retail.v2.Product]s with the same
    [parent][google.cloud.retail.v2.CreateProductRequest.parent]. Otherwise, an
    ALREADY_EXISTS error is returned.

    This field must be a UTF-8 encoded string with a length limit of 128
    characters. Otherwise, an INVALID_ARGUMENT error is returned.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        product : typing.Optional[google.cloud.retail.v2.product_pb2.Product] = ...,
        product_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["product",b"product"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","product",b"product","product_id",b"product_id"]) -> None: ...
global___CreateProductRequest = CreateProductRequest

class GetProductRequest(google.protobuf.message.Message):
    """Request message for [GetProduct][] method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Full resource name of [Product][google.cloud.retail.v2.Product],
    such as
    `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.

    If the caller does not have permission to access the
    [Product][google.cloud.retail.v2.Product], regardless of whether or not it
    exists, a PERMISSION_DENIED error is returned.

    If the requested [Product][google.cloud.retail.v2.Product] does not exist,
    a NOT_FOUND error is returned.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetProductRequest = GetProductRequest

class UpdateProductRequest(google.protobuf.message.Message):
    """Request message for [UpdateProduct][] method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PRODUCT_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_FIELD_NUMBER: builtins.int
    @property
    def product(self) -> google.cloud.retail.v2.product_pb2.Product:
        """Required. The product to update/create.

        If the caller does not have permission to update the
        [Product][google.cloud.retail.v2.Product], regardless of whether or not it
        exists, a PERMISSION_DENIED error is returned.

        If the [Product][google.cloud.retail.v2.Product] to update does not exist
        and
        [allow_missing][google.cloud.retail.v2.UpdateProductRequest.allow_missing]
        is not set, a NOT_FOUND error is returned.
        """
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Indicates which fields in the provided
        [Product][google.cloud.retail.v2.Product] to update. The immutable and
        output only fields are NOT supported. If not set, all supported fields (the
        fields that are neither immutable nor output only) are updated.

        If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
        is returned.
        """
        pass
    allow_missing: builtins.bool = ...
    """If set to true, and the [Product][google.cloud.retail.v2.Product] is not
    found, a new [Product][google.cloud.retail.v2.Product] will be created. In
    this situation, `update_mask` is ignored.
    """

    def __init__(self,
        *,
        product : typing.Optional[google.cloud.retail.v2.product_pb2.Product] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        allow_missing : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["product",b"product","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_missing",b"allow_missing","product",b"product","update_mask",b"update_mask"]) -> None: ...
global___UpdateProductRequest = UpdateProductRequest

class DeleteProductRequest(google.protobuf.message.Message):
    """Request message for [DeleteProduct][] method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Full resource name of [Product][google.cloud.retail.v2.Product],
    such as
    `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.

    If the caller does not have permission to delete the
    [Product][google.cloud.retail.v2.Product], regardless of whether or not it
    exists, a PERMISSION_DENIED error is returned.

    If the [Product][google.cloud.retail.v2.Product] to delete does not exist,
    a NOT_FOUND error is returned.

    The [Product][google.cloud.retail.v2.Product] to delete can neither be a
    [Product.Type.COLLECTION][google.cloud.retail.v2.Product.Type.COLLECTION]
    [Product][google.cloud.retail.v2.Product] member nor a
    [Product.Type.PRIMARY][google.cloud.retail.v2.Product.Type.PRIMARY]
    [Product][google.cloud.retail.v2.Product] with more than one
    [variants][google.cloud.retail.v2.Product.Type.VARIANT]. Otherwise, an
    INVALID_ARGUMENT error is returned.

    All inventory information for the named
    [Product][google.cloud.retail.v2.Product] will be deleted.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteProductRequest = DeleteProductRequest

class ListProductsRequest(google.protobuf.message.Message):
    """Request message for
    [ProductService.ListProducts][google.cloud.retail.v2.ProductService.ListProducts]
    method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    READ_MASK_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent branch resource name, such as
    `projects/*/locations/global/catalogs/default_catalog/branches/0`. Use
    `default_branch` as the branch ID, to list products under the default
    branch.

    If the caller does not have permission to list
    [Product][google.cloud.retail.v2.Product]s under this branch, regardless of
    whether or not this branch exists, a PERMISSION_DENIED error is returned.
    """

    page_size: builtins.int = ...
    """Maximum number of [Product][google.cloud.retail.v2.Product]s to return. If
    unspecified, defaults to 100. The maximum allowed value is 1000. Values
    above 1000 will be coerced to 1000.

    If this field is negative, an INVALID_ARGUMENT error is returned.
    """

    page_token: typing.Text = ...
    """A page token
    [ListProductsResponse.next_page_token][google.cloud.retail.v2.ListProductsResponse.next_page_token],
    received from a previous
    [ProductService.ListProducts][google.cloud.retail.v2.ProductService.ListProducts]
    call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to
    [ProductService.ListProducts][google.cloud.retail.v2.ProductService.ListProducts]
    must match the call that provided the page token. Otherwise, an
    INVALID_ARGUMENT error is returned.
    """

    filter: typing.Text = ...
    """A filter to apply on the list results. Supported features:

    * List all the products under the parent branch if
    [filter][google.cloud.retail.v2.ListProductsRequest.filter] is unset.
    * List [Product.Type.VARIANT][google.cloud.retail.v2.Product.Type.VARIANT]
    [Product][google.cloud.retail.v2.Product]s sharing the same
      [Product.Type.PRIMARY][google.cloud.retail.v2.Product.Type.PRIMARY]
      [Product][google.cloud.retail.v2.Product]. For example:
        `primary_product_id = "some_product_id"`
    * List [Product][google.cloud.retail.v2.Product]s bundled in a
    [Product.Type.COLLECTION][google.cloud.retail.v2.Product.Type.COLLECTION]
    [Product][google.cloud.retail.v2.Product].
      For example:
        `collection_product_id = "some_product_id"`
    * List [Product][google.cloud.retail.v2.Product]s with a partibular type.
    For example:
        `type = "PRIMARY"`
        `type = "VARIANT"`
        `type = "COLLECTION"`

    If the field is unrecognizable, an INVALID_ARGUMENT error is returned.

    If the specified
    [Product.Type.PRIMARY][google.cloud.retail.v2.Product.Type.PRIMARY]
    [Product][google.cloud.retail.v2.Product] or
    [Product.Type.COLLECTION][google.cloud.retail.v2.Product.Type.COLLECTION]
    [Product][google.cloud.retail.v2.Product] does not exist, a NOT_FOUND error
    is returned.
    """

    @property
    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The fields of [Product][google.cloud.retail.v2.Product] to return in the
        responses. If not set or empty, the following fields are returned:

        * [Product.name][google.cloud.retail.v2.Product.name]
        * [Product.id][google.cloud.retail.v2.Product.id]
        * [Product.title][google.cloud.retail.v2.Product.title]
        * [Product.uri][google.cloud.retail.v2.Product.uri]
        * [Product.images][google.cloud.retail.v2.Product.images]
        * [Product.price_info][google.cloud.retail.v2.Product.price_info]
        * [Product.brands][google.cloud.retail.v2.Product.brands]

        If "*" is provided, all fields are returned.
        [Product.name][google.cloud.retail.v2.Product.name] is always returned no
        matter what mask is set.

        If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
        is returned.
        """
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        filter : typing.Text = ...,
        read_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","parent",b"parent","read_mask",b"read_mask"]) -> None: ...
global___ListProductsRequest = ListProductsRequest

class ListProductsResponse(google.protobuf.message.Message):
    """Response message for
    [ProductService.ListProducts][google.cloud.retail.v2.ProductService.ListProducts]
    method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PRODUCTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def products(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.retail.v2.product_pb2.Product]:
        """The [Product][google.cloud.retail.v2.Product]s."""
        pass
    next_page_token: typing.Text = ...
    """A token that can be sent as
    [ListProductsRequest.page_token][google.cloud.retail.v2.ListProductsRequest.page_token]
    to retrieve the next page. If this field is omitted, there are no
    subsequent pages.
    """

    def __init__(self,
        *,
        products : typing.Optional[typing.Iterable[google.cloud.retail.v2.product_pb2.Product]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","products",b"products"]) -> None: ...
global___ListProductsResponse = ListProductsResponse

class SetInventoryRequest(google.protobuf.message.Message):
    """Request message for [SetInventory][] method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INVENTORY_FIELD_NUMBER: builtins.int
    SET_MASK_FIELD_NUMBER: builtins.int
    SET_TIME_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_FIELD_NUMBER: builtins.int
    @property
    def inventory(self) -> google.cloud.retail.v2.product_pb2.Product:
        """Required. The inventory information to update. The allowable fields to
        update are:
        * [Product.price_info][google.cloud.retail.v2.Product.price_info]
        * [Product.availability][google.cloud.retail.v2.Product.availability]
        * [Product.available_quantity][google.cloud.retail.v2.Product.available_quantity]
        * [Product.fulfillment_info][google.cloud.retail.v2.Product.fulfillment_info]
        The updated inventory fields must be specified in
        [SetInventoryRequest.set_mask][google.cloud.retail.v2.SetInventoryRequest.set_mask].

        If [SetInventoryRequest.inventory.name][] is empty or invalid, an
        INVALID_ARGUMENT error is returned.

        If the caller does not have permission to update the
        [Product][google.cloud.retail.v2.Product] named in
        [Product.name][google.cloud.retail.v2.Product.name], regardless of whether
        or not it exists, a PERMISSION_DENIED error is returned.

        If the [Product][google.cloud.retail.v2.Product] to update does not have
        existing inventory information, the provided inventory information will be
        inserted.

        If the [Product][google.cloud.retail.v2.Product] to update has existing
        inventory information, the provided inventory information will be merged
        while respecting the last update time for each inventory field, using the
        provided or default value for
        [SetInventoryRequest.set_time][google.cloud.retail.v2.SetInventoryRequest.set_time].

        The last update time is recorded for the following inventory fields:
        * [Product.price_info][google.cloud.retail.v2.Product.price_info]
        * [Product.availability][google.cloud.retail.v2.Product.availability]
        * [Product.available_quantity][google.cloud.retail.v2.Product.available_quantity]
        * [Product.fulfillment_info][google.cloud.retail.v2.Product.fulfillment_info]

        If a full overwrite of inventory information while ignoring timestamps is
        needed, [UpdateProduct][] should be invoked instead.
        """
        pass
    @property
    def set_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Indicates which inventory fields in the provided
        [Product][google.cloud.retail.v2.Product] to update. If not set or set with
        empty paths, all inventory fields will be updated.

        If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
        is returned and the entire update will be ignored.
        """
        pass
    @property
    def set_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the request is issued, used to prevent
        out-of-order updates on inventory fields with the last update time
        recorded. If not provided, the internal system time will be used.
        """
        pass
    allow_missing: builtins.bool = ...
    """If set to true, and the [Product][google.cloud.retail.v2.Product] with name
    [Product.name][google.cloud.retail.v2.Product.name] is not found, the
    inventory update will still be processed and retained for at most 1 day
    until the [Product][google.cloud.retail.v2.Product] is created. If set to
    false, a NOT_FOUND error is returned if the
    [Product][google.cloud.retail.v2.Product] is not found.
    """

    def __init__(self,
        *,
        inventory : typing.Optional[google.cloud.retail.v2.product_pb2.Product] = ...,
        set_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        set_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        allow_missing : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["inventory",b"inventory","set_mask",b"set_mask","set_time",b"set_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_missing",b"allow_missing","inventory",b"inventory","set_mask",b"set_mask","set_time",b"set_time"]) -> None: ...
global___SetInventoryRequest = SetInventoryRequest

class SetInventoryMetadata(google.protobuf.message.Message):
    """Metadata related to the progress of the SetInventory operation.
    Currently empty because there is no meaningful metadata populated from the
    [SetInventory][] method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___SetInventoryMetadata = SetInventoryMetadata

class SetInventoryResponse(google.protobuf.message.Message):
    """Response of the SetInventoryRequest.  Currently empty because
    there is no meaningful response populated from the [SetInventory][]
    method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___SetInventoryResponse = SetInventoryResponse

class AddFulfillmentPlacesRequest(google.protobuf.message.Message):
    """Request message for [AddFulfillmentPlaces][] method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PRODUCT_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PLACE_IDS_FIELD_NUMBER: builtins.int
    ADD_TIME_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_FIELD_NUMBER: builtins.int
    product: typing.Text = ...
    """Required. Full resource name of [Product][google.cloud.retail.v2.Product],
    such as
    `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.

    If the caller does not have permission to access the
    [Product][google.cloud.retail.v2.Product], regardless of whether or not it
    exists, a PERMISSION_DENIED error is returned.
    """

    type: typing.Text = ...
    """Required. The fulfillment type, including commonly used types (such as
    pickup in store and same day delivery), and custom types.

    Supported values:

    * "pickup-in-store"
    * "ship-to-store"
    * "same-day-delivery"
    * "next-day-delivery"
    * "custom-type-1"
    * "custom-type-2"
    * "custom-type-3"
    * "custom-type-4"
    * "custom-type-5"

    If this field is set to an invalid value other than these, an
    INVALID_ARGUMENT error is returned.

    This field directly corresponds to [Product.fulfillment_info.type][].
    """

    @property
    def place_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. The IDs for this
        [type][google.cloud.retail.v2.AddFulfillmentPlacesRequest.type], such as
        the store IDs for "pickup-in-store" or the region IDs for
        "same-day-delivery" to be added for this
        [type][google.cloud.retail.v2.AddFulfillmentPlacesRequest.type]. Duplicate
        IDs will be automatically ignored.

        At least 1 value is required, and a maximum of 2000 values are allowed.
        Each value must be a string with a length limit of 10 characters, matching
        the pattern `[a-zA-Z0-9_-]+`, such as "store1" or "REGION-2". Otherwise, an
        INVALID_ARGUMENT error is returned.

        If the total number of place IDs exceeds 2000 for this
        [type][google.cloud.retail.v2.AddFulfillmentPlacesRequest.type] after
        adding, then the update will be rejected.
        """
        pass
    @property
    def add_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the fulfillment updates are issued, used to prevent
        out-of-order updates on fulfillment information. If not provided, the
        internal system time will be used.
        """
        pass
    allow_missing: builtins.bool = ...
    """If set to true, and the [Product][google.cloud.retail.v2.Product] is not
    found, the fulfillment information will still be processed and retained for
    at most 1 day and processed once the
    [Product][google.cloud.retail.v2.Product] is created. If set to false, a
    NOT_FOUND error is returned if the
    [Product][google.cloud.retail.v2.Product] is not found.
    """

    def __init__(self,
        *,
        product : typing.Text = ...,
        type : typing.Text = ...,
        place_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        add_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        allow_missing : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["add_time",b"add_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["add_time",b"add_time","allow_missing",b"allow_missing","place_ids",b"place_ids","product",b"product","type",b"type"]) -> None: ...
global___AddFulfillmentPlacesRequest = AddFulfillmentPlacesRequest

class AddFulfillmentPlacesMetadata(google.protobuf.message.Message):
    """Metadata related to the progress of the AddFulfillmentPlaces operation.
    Currently empty because there is no meaningful metadata populated from the
    [AddFulfillmentPlaces][] method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___AddFulfillmentPlacesMetadata = AddFulfillmentPlacesMetadata

class AddFulfillmentPlacesResponse(google.protobuf.message.Message):
    """Response of the AddFulfillmentPlacesRequest.  Currently empty because
    there is no meaningful response populated from the [AddFulfillmentPlaces][]
    method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___AddFulfillmentPlacesResponse = AddFulfillmentPlacesResponse

class RemoveFulfillmentPlacesRequest(google.protobuf.message.Message):
    """Request message for [RemoveFulfillmentPlaces][] method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PRODUCT_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PLACE_IDS_FIELD_NUMBER: builtins.int
    REMOVE_TIME_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_FIELD_NUMBER: builtins.int
    product: typing.Text = ...
    """Required. Full resource name of [Product][google.cloud.retail.v2.Product],
    such as
    `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.

    If the caller does not have permission to access the
    [Product][google.cloud.retail.v2.Product], regardless of whether or not it
    exists, a PERMISSION_DENIED error is returned.
    """

    type: typing.Text = ...
    """Required. The fulfillment type, including commonly used types (such as
    pickup in store and same day delivery), and custom types.

    Supported values:

    * "pickup-in-store"
    * "ship-to-store"
    * "same-day-delivery"
    * "next-day-delivery"
    * "custom-type-1"
    * "custom-type-2"
    * "custom-type-3"
    * "custom-type-4"
    * "custom-type-5"

    If this field is set to an invalid value other than these, an
    INVALID_ARGUMENT error is returned.

    This field directly corresponds to [Product.fulfillment_info.type][].
    """

    @property
    def place_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. The IDs for this
        [type][google.cloud.retail.v2.RemoveFulfillmentPlacesRequest.type], such as
        the store IDs for "pickup-in-store" or the region IDs for
        "same-day-delivery", to be removed for this
        [type][google.cloud.retail.v2.RemoveFulfillmentPlacesRequest.type].

        At least 1 value is required, and a maximum of 2000 values are allowed.
        Each value must be a string with a length limit of 10 characters, matching
        the pattern `[a-zA-Z0-9_-]+`, such as "store1" or "REGION-2". Otherwise, an
        INVALID_ARGUMENT error is returned.
        """
        pass
    @property
    def remove_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the fulfillment updates are issued, used to prevent
        out-of-order updates on fulfillment information. If not provided, the
        internal system time will be used.
        """
        pass
    allow_missing: builtins.bool = ...
    """If set to true, and the [Product][google.cloud.retail.v2.Product] is not
    found, the fulfillment information will still be processed and retained for
    at most 1 day and processed once the
    [Product][google.cloud.retail.v2.Product] is created. If set to false, a
    NOT_FOUND error is returned if the
    [Product][google.cloud.retail.v2.Product] is not found.
    """

    def __init__(self,
        *,
        product : typing.Text = ...,
        type : typing.Text = ...,
        place_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        remove_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        allow_missing : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["remove_time",b"remove_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_missing",b"allow_missing","place_ids",b"place_ids","product",b"product","remove_time",b"remove_time","type",b"type"]) -> None: ...
global___RemoveFulfillmentPlacesRequest = RemoveFulfillmentPlacesRequest

class RemoveFulfillmentPlacesMetadata(google.protobuf.message.Message):
    """Metadata related to the progress of the RemoveFulfillmentPlaces operation.
    Currently empty because there is no meaningful metadata populated from the
    [RemoveFulfillmentPlaces][] method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___RemoveFulfillmentPlacesMetadata = RemoveFulfillmentPlacesMetadata

class RemoveFulfillmentPlacesResponse(google.protobuf.message.Message):
    """Response of the RemoveFulfillmentPlacesRequest. Currently empty because there
    is no meaningful response populated from the [RemoveFulfillmentPlaces][]
    method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___RemoveFulfillmentPlacesResponse = RemoveFulfillmentPlacesResponse
