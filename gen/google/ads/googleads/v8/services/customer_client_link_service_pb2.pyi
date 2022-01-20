"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.resources.customer_client_link_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetCustomerClientLinkRequest(google.protobuf.message.Message):
    """Request message for [CustomerClientLinkService.GetCustomerClientLink][google.ads.googleads.v8.services.CustomerClientLinkService.GetCustomerClientLink]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the customer client link to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetCustomerClientLinkRequest = GetCustomerClientLinkRequest

class MutateCustomerClientLinkRequest(google.protobuf.message.Message):
    """Request message for [CustomerClientLinkService.MutateCustomerClientLink][google.ads.googleads.v8.services.CustomerClientLinkService.MutateCustomerClientLink]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer whose customer link are being modified."""

    @property
    def operation(self) -> global___CustomerClientLinkOperation:
        """Required. The operation to perform on the individual CustomerClientLink."""
        pass
    validate_only: builtins.bool = ...
    """If true, the request is validated but not executed. Only errors are
    returned, not results.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operation : typing.Optional[global___CustomerClientLinkOperation] = ...,
        validate_only : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["operation",b"operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operation",b"operation","validate_only",b"validate_only"]) -> None: ...
global___MutateCustomerClientLinkRequest = MutateCustomerClientLinkRequest

class CustomerClientLinkOperation(google.protobuf.message.Message):
    """A single operation (create, update) on a CustomerClientLink."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    CREATE_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """FieldMask that determines which resource fields are modified in an update."""
        pass
    @property
    def create(self) -> google.ads.googleads.v8.resources.customer_client_link_pb2.CustomerClientLink:
        """Create operation: No resource name is expected for the new link."""
        pass
    @property
    def update(self) -> google.ads.googleads.v8.resources.customer_client_link_pb2.CustomerClientLink:
        """Update operation: The link is expected to have a valid resource name."""
        pass
    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        create : typing.Optional[google.ads.googleads.v8.resources.customer_client_link_pb2.CustomerClientLink] = ...,
        update : typing.Optional[google.ads.googleads.v8.resources.customer_client_link_pb2.CustomerClientLink] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","update",b"update","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","update",b"update","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","update"]]: ...
global___CustomerClientLinkOperation = CustomerClientLinkOperation

class MutateCustomerClientLinkResponse(google.protobuf.message.Message):
    """Response message for a CustomerClientLink mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> global___MutateCustomerClientLinkResult:
        """A result that identifies the resource affected by the mutate request."""
        pass
    def __init__(self,
        *,
        result : typing.Optional[global___MutateCustomerClientLinkResult] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result",b"result"]) -> None: ...
global___MutateCustomerClientLinkResponse = MutateCustomerClientLinkResponse

class MutateCustomerClientLinkResult(google.protobuf.message.Message):
    """The result for a single customer client link mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___MutateCustomerClientLinkResult = MutateCustomerClientLinkResult
