"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.resources.billing_setup_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetBillingSetupRequest(google.protobuf.message.Message):
    """Request message for
    [BillingSetupService.GetBillingSetup][google.ads.googleads.v7.services.BillingSetupService.GetBillingSetup].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the billing setup to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetBillingSetupRequest = GetBillingSetupRequest

class MutateBillingSetupRequest(google.protobuf.message.Message):
    """Request message for billing setup mutate operations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. Id of the customer to apply the billing setup mutate operation to."""

    @property
    def operation(self) -> global___BillingSetupOperation:
        """Required. The operation to perform."""
        pass
    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operation : typing.Optional[global___BillingSetupOperation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["operation",b"operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operation",b"operation"]) -> None: ...
global___MutateBillingSetupRequest = MutateBillingSetupRequest

class BillingSetupOperation(google.protobuf.message.Message):
    """A single operation on a billing setup, which describes the cancellation of an
    existing billing setup.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    @property
    def create(self) -> google.ads.googleads.v7.resources.billing_setup_pb2.BillingSetup:
        """Creates a billing setup. No resource name is expected for the new billing
        setup.
        """
        pass
    remove: typing.Text = ...
    """Resource name of the billing setup to remove. A setup cannot be
    removed unless it is in a pending state or its scheduled start time is in
    the future. The resource name looks like
    `customers/{customer_id}/billingSetups/{billing_id}`.
    """

    def __init__(self,
        *,
        create : typing.Optional[google.ads.googleads.v7.resources.billing_setup_pb2.BillingSetup] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","remove"]]: ...
global___BillingSetupOperation = BillingSetupOperation

class MutateBillingSetupResponse(google.protobuf.message.Message):
    """Response message for a billing setup operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> global___MutateBillingSetupResult:
        """A result that identifies the resource affected by the mutate request."""
        pass
    def __init__(self,
        *,
        result : typing.Optional[global___MutateBillingSetupResult] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result",b"result"]) -> None: ...
global___MutateBillingSetupResponse = MutateBillingSetupResponse

class MutateBillingSetupResult(google.protobuf.message.Message):
    """Result for a single billing setup mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___MutateBillingSetupResult = MutateBillingSetupResult
