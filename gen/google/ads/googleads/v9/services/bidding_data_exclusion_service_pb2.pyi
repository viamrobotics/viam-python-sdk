"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.bidding_data_exclusion_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetBiddingDataExclusionRequest(google.protobuf.message.Message):
    """Request message for
    [BiddingDataExclusionService.GetBiddingDataExclusion][google.ads.googleads.v9.services.BiddingDataExclusionService.GetBiddingDataExclusion].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the data exclusion to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetBiddingDataExclusionRequest = GetBiddingDataExclusionRequest

class MutateBiddingDataExclusionsRequest(google.protobuf.message.Message):
    """Request message for
    [BiddingDataExclusionService.MutateBiddingDataExclusions][google.ads.googleads.v9.services.BiddingDataExclusionService.MutateBiddingDataExclusions].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. ID of the customer whose data exclusions are being modified."""

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BiddingDataExclusionOperation]:
        """Required. The list of operations to perform on individual data exclusions."""
        pass
    partial_failure: builtins.bool = ...
    """If true, successful operations will be carried out and invalid
    operations will return errors. If false, all operations will be carried
    out in one transaction if and only if they are all valid.
    Default is false.
    """

    validate_only: builtins.bool = ...
    """If true, the request is validated but not executed. Only errors are
    returned, not results.
    """

    response_content_type: google.ads.googleads.v9.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...
    """The response content type setting. Determines whether the mutable resource
    or just the resource name should be returned post mutation.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operations : typing.Optional[typing.Iterable[global___BiddingDataExclusionOperation]] = ...,
        partial_failure : builtins.bool = ...,
        validate_only : builtins.bool = ...,
        response_content_type : google.ads.googleads.v9.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operations",b"operations","partial_failure",b"partial_failure","response_content_type",b"response_content_type","validate_only",b"validate_only"]) -> None: ...
global___MutateBiddingDataExclusionsRequest = MutateBiddingDataExclusionsRequest

class BiddingDataExclusionOperation(google.protobuf.message.Message):
    """A single operation (create, remove, update) on a data exclusion."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    CREATE_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """FieldMask that determines which resource fields are modified in an update."""
        pass
    @property
    def create(self) -> google.ads.googleads.v9.resources.bidding_data_exclusion_pb2.BiddingDataExclusion:
        """Create operation: No resource name is expected for the new data
        exclusion.
        """
        pass
    @property
    def update(self) -> google.ads.googleads.v9.resources.bidding_data_exclusion_pb2.BiddingDataExclusion:
        """Update operation: The data exclusion is expected to have a valid
        resource name.
        """
        pass
    remove: typing.Text = ...
    """Remove operation: A resource name for the removed data exclusion
    is expected, in this format:

    `customers/{customer_id}/biddingDataExclusions/{data_exclusion_id}`
    """

    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        create : typing.Optional[google.ads.googleads.v9.resources.bidding_data_exclusion_pb2.BiddingDataExclusion] = ...,
        update : typing.Optional[google.ads.googleads.v9.resources.bidding_data_exclusion_pb2.BiddingDataExclusion] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","update","remove"]]: ...
global___BiddingDataExclusionOperation = BiddingDataExclusionOperation

class MutateBiddingDataExclusionsResponse(google.protobuf.message.Message):
    """Response message for data exlusions mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def partial_failure_error(self) -> google.rpc.status_pb2.Status:
        """Errors that pertain to operation failures in the partial failure mode.
        Returned only when partial_failure = true and all errors occur inside the
        operations. If any errors occur outside the operations (e.g. auth errors),
        we return an RPC level error.
        """
        pass
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateBiddingDataExclusionsResult]:
        """All results for the mutate."""
        pass
    def __init__(self,
        *,
        partial_failure_error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        results : typing.Optional[typing.Iterable[global___MutateBiddingDataExclusionsResult]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error","results",b"results"]) -> None: ...
global___MutateBiddingDataExclusionsResponse = MutateBiddingDataExclusionsResponse

class MutateBiddingDataExclusionsResult(google.protobuf.message.Message):
    """The result for the data exclusion mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    BIDDING_DATA_EXCLUSION_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    @property
    def bidding_data_exclusion(self) -> google.ads.googleads.v9.resources.bidding_data_exclusion_pb2.BiddingDataExclusion:
        """The mutated bidding data exclusion with only mutable fields after mutate.
        The field will only be returned when response_content_type is set
        to "MUTABLE_RESOURCE".
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        bidding_data_exclusion : typing.Optional[google.ads.googleads.v9.resources.bidding_data_exclusion_pb2.BiddingDataExclusion] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bidding_data_exclusion",b"bidding_data_exclusion"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bidding_data_exclusion",b"bidding_data_exclusion","resource_name",b"resource_name"]) -> None: ...
global___MutateBiddingDataExclusionsResult = MutateBiddingDataExclusionsResult
