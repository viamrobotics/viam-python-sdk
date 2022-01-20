"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.campaign_draft_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetCampaignDraftRequest(google.protobuf.message.Message):
    """Request message for [CampaignDraftService.GetCampaignDraft][google.ads.googleads.v9.services.CampaignDraftService.GetCampaignDraft]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the campaign draft to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetCampaignDraftRequest = GetCampaignDraftRequest

class MutateCampaignDraftsRequest(google.protobuf.message.Message):
    """Request message for [CampaignDraftService.MutateCampaignDrafts][google.ads.googleads.v9.services.CampaignDraftService.MutateCampaignDrafts]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer whose campaign drafts are being modified."""

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CampaignDraftOperation]:
        """Required. The list of operations to perform on individual campaign drafts."""
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
        operations : typing.Optional[typing.Iterable[global___CampaignDraftOperation]] = ...,
        partial_failure : builtins.bool = ...,
        validate_only : builtins.bool = ...,
        response_content_type : google.ads.googleads.v9.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operations",b"operations","partial_failure",b"partial_failure","response_content_type",b"response_content_type","validate_only",b"validate_only"]) -> None: ...
global___MutateCampaignDraftsRequest = MutateCampaignDraftsRequest

class PromoteCampaignDraftRequest(google.protobuf.message.Message):
    """Request message for [CampaignDraftService.PromoteCampaignDraft][google.ads.googleads.v9.services.CampaignDraftService.PromoteCampaignDraft]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CAMPAIGN_DRAFT_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    campaign_draft: typing.Text = ...
    """Required. The resource name of the campaign draft to promote."""

    validate_only: builtins.bool = ...
    """If true, the request is validated but no Long Running Operation is created.
    Only errors are returned.
    """

    def __init__(self,
        *,
        campaign_draft : typing.Text = ...,
        validate_only : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["campaign_draft",b"campaign_draft","validate_only",b"validate_only"]) -> None: ...
global___PromoteCampaignDraftRequest = PromoteCampaignDraftRequest

class CampaignDraftOperation(google.protobuf.message.Message):
    """A single operation (create, update, remove) on a campaign draft."""
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
    def create(self) -> google.ads.googleads.v9.resources.campaign_draft_pb2.CampaignDraft:
        """Create operation: No resource name is expected for the new campaign
        draft.
        """
        pass
    @property
    def update(self) -> google.ads.googleads.v9.resources.campaign_draft_pb2.CampaignDraft:
        """Update operation: The campaign draft is expected to have a valid
        resource name.
        """
        pass
    remove: typing.Text = ...
    """Remove operation: The campaign draft is expected to have a valid
    resource name, in this format:

    `customers/{customer_id}/campaignDrafts/{base_campaign_id}~{draft_id}`
    """

    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        create : typing.Optional[google.ads.googleads.v9.resources.campaign_draft_pb2.CampaignDraft] = ...,
        update : typing.Optional[google.ads.googleads.v9.resources.campaign_draft_pb2.CampaignDraft] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","update","remove"]]: ...
global___CampaignDraftOperation = CampaignDraftOperation

class MutateCampaignDraftsResponse(google.protobuf.message.Message):
    """Response message for campaign draft mutate."""
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
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateCampaignDraftResult]:
        """All results for the mutate."""
        pass
    def __init__(self,
        *,
        partial_failure_error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        results : typing.Optional[typing.Iterable[global___MutateCampaignDraftResult]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error","results",b"results"]) -> None: ...
global___MutateCampaignDraftsResponse = MutateCampaignDraftsResponse

class MutateCampaignDraftResult(google.protobuf.message.Message):
    """The result for the campaign draft mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CAMPAIGN_DRAFT_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    @property
    def campaign_draft(self) -> google.ads.googleads.v9.resources.campaign_draft_pb2.CampaignDraft:
        """The mutated campaign draft with only mutable fields after mutate. The field
        will only be returned when response_content_type is set to
        "MUTABLE_RESOURCE".
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        campaign_draft : typing.Optional[google.ads.googleads.v9.resources.campaign_draft_pb2.CampaignDraft] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["campaign_draft",b"campaign_draft"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["campaign_draft",b"campaign_draft","resource_name",b"resource_name"]) -> None: ...
global___MutateCampaignDraftResult = MutateCampaignDraftResult

class ListCampaignDraftAsyncErrorsRequest(google.protobuf.message.Message):
    """Request message for [CampaignDraftService.ListCampaignDraftAsyncErrors][google.ads.googleads.v9.services.CampaignDraftService.ListCampaignDraftAsyncErrors]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The name of the campaign draft from which to retrieve the async errors."""

    page_token: typing.Text = ...
    """Token of the page to retrieve. If not specified, the first
    page of results will be returned. Use the value obtained from
    `next_page_token` in the previous response in order to request
    the next page of results.
    """

    page_size: builtins.int = ...
    """Number of elements to retrieve in a single page.
    When a page request is too large, the server may decide to
    further limit the number of returned resources.
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        page_token : typing.Text = ...,
        page_size : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","resource_name",b"resource_name"]) -> None: ...
global___ListCampaignDraftAsyncErrorsRequest = ListCampaignDraftAsyncErrorsRequest

class ListCampaignDraftAsyncErrorsResponse(google.protobuf.message.Message):
    """Response message for [CampaignDraftService.ListCampaignDraftAsyncErrors][google.ads.googleads.v9.services.CampaignDraftService.ListCampaignDraftAsyncErrors]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ERRORS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.rpc.status_pb2.Status]:
        """Details of the errors when performing the asynchronous operation."""
        pass
    next_page_token: typing.Text = ...
    """Pagination token used to retrieve the next page of results.
    Pass the content of this string as the `page_token` attribute of
    the next request. `next_page_token` is not returned for the last
    page.
    """

    def __init__(self,
        *,
        errors : typing.Optional[typing.Iterable[google.rpc.status_pb2.Status]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["errors",b"errors","next_page_token",b"next_page_token"]) -> None: ...
global___ListCampaignDraftAsyncErrorsResponse = ListCampaignDraftAsyncErrorsResponse
