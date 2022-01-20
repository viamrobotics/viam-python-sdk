"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.resources.keyword_plan_ad_group_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetKeywordPlanAdGroupRequest(google.protobuf.message.Message):
    """Request message for [KeywordPlanAdGroupService.GetKeywordPlanAdGroup][google.ads.googleads.v7.services.KeywordPlanAdGroupService.GetKeywordPlanAdGroup]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the Keyword Plan ad group to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetKeywordPlanAdGroupRequest = GetKeywordPlanAdGroupRequest

class MutateKeywordPlanAdGroupsRequest(google.protobuf.message.Message):
    """Request message for [KeywordPlanAdGroupService.MutateKeywordPlanAdGroups][google.ads.googleads.v7.services.KeywordPlanAdGroupService.MutateKeywordPlanAdGroups]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer whose Keyword Plan ad groups are being modified."""

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeywordPlanAdGroupOperation]:
        """Required. The list of operations to perform on individual Keyword Plan ad groups."""
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

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operations : typing.Optional[typing.Iterable[global___KeywordPlanAdGroupOperation]] = ...,
        partial_failure : builtins.bool = ...,
        validate_only : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operations",b"operations","partial_failure",b"partial_failure","validate_only",b"validate_only"]) -> None: ...
global___MutateKeywordPlanAdGroupsRequest = MutateKeywordPlanAdGroupsRequest

class KeywordPlanAdGroupOperation(google.protobuf.message.Message):
    """A single operation (create, update, remove) on a Keyword Plan ad group."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    CREATE_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The FieldMask that determines which resource fields are modified in an
        update.
        """
        pass
    @property
    def create(self) -> google.ads.googleads.v7.resources.keyword_plan_ad_group_pb2.KeywordPlanAdGroup:
        """Create operation: No resource name is expected for the new Keyword Plan
        ad group.
        """
        pass
    @property
    def update(self) -> google.ads.googleads.v7.resources.keyword_plan_ad_group_pb2.KeywordPlanAdGroup:
        """Update operation: The Keyword Plan ad group is expected to have a valid
        resource name.
        """
        pass
    remove: typing.Text = ...
    """Remove operation: A resource name for the removed Keyword Plan ad group
    is expected, in this format:

    `customers/{customer_id}/keywordPlanAdGroups/{kp_ad_group_id}`
    """

    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        create : typing.Optional[google.ads.googleads.v7.resources.keyword_plan_ad_group_pb2.KeywordPlanAdGroup] = ...,
        update : typing.Optional[google.ads.googleads.v7.resources.keyword_plan_ad_group_pb2.KeywordPlanAdGroup] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","update","remove"]]: ...
global___KeywordPlanAdGroupOperation = KeywordPlanAdGroupOperation

class MutateKeywordPlanAdGroupsResponse(google.protobuf.message.Message):
    """Response message for a Keyword Plan ad group mutate."""
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
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateKeywordPlanAdGroupResult]:
        """All results for the mutate. The order of the results is determined by the
        order of the keywords in the original request.
        """
        pass
    def __init__(self,
        *,
        partial_failure_error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        results : typing.Optional[typing.Iterable[global___MutateKeywordPlanAdGroupResult]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error","results",b"results"]) -> None: ...
global___MutateKeywordPlanAdGroupsResponse = MutateKeywordPlanAdGroupsResponse

class MutateKeywordPlanAdGroupResult(google.protobuf.message.Message):
    """The result for the Keyword Plan ad group mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___MutateKeywordPlanAdGroupResult = MutateKeywordPlanAdGroupResult
