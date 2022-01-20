"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.campaign_draft_status_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CampaignDraft(google.protobuf.message.Message):
    """Proto file describing the Campaign Draft resource.

    A campaign draft.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    DRAFT_ID_FIELD_NUMBER: builtins.int
    BASE_CAMPAIGN_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DRAFT_CAMPAIGN_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    HAS_EXPERIMENT_RUNNING_FIELD_NUMBER: builtins.int
    LONG_RUNNING_OPERATION_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the campaign draft.
    Campaign draft resource names have the form:

    `customers/{customer_id}/campaignDrafts/{base_campaign_id}~{draft_id}`
    """

    draft_id: builtins.int = ...
    """Output only. The ID of the draft.

    This field is read-only.
    """

    base_campaign: typing.Text = ...
    """Immutable. The base campaign to which the draft belongs."""

    name: typing.Text = ...
    """The name of the campaign draft.

    This field is required and should not be empty when creating new
    campaign drafts.

    It must not contain any null (code point 0x0), NL line feed
    (code point 0xA) or carriage return (code point 0xD) characters.
    """

    draft_campaign: typing.Text = ...
    """Output only. Resource name of the Campaign that results from overlaying the draft
    changes onto the base campaign.

    This field is read-only.
    """

    status: google.ads.googleads.v9.enums.campaign_draft_status_pb2.CampaignDraftStatusEnum.CampaignDraftStatus.ValueType = ...
    """Output only. The status of the campaign draft. This field is read-only.

    When a new campaign draft is added, the status defaults to PROPOSED.
    """

    has_experiment_running: builtins.bool = ...
    """Output only. Whether there is an experiment based on this draft currently serving."""

    long_running_operation: typing.Text = ...
    """Output only. The resource name of the long-running operation that can be used to poll
    for completion of draft promotion. This is only set if the draft promotion
    is in progress or finished.
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        draft_id : typing.Optional[builtins.int] = ...,
        base_campaign : typing.Optional[typing.Text] = ...,
        name : typing.Optional[typing.Text] = ...,
        draft_campaign : typing.Optional[typing.Text] = ...,
        status : google.ads.googleads.v9.enums.campaign_draft_status_pb2.CampaignDraftStatusEnum.CampaignDraftStatus.ValueType = ...,
        has_experiment_running : typing.Optional[builtins.bool] = ...,
        long_running_operation : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_base_campaign",b"_base_campaign","_draft_campaign",b"_draft_campaign","_draft_id",b"_draft_id","_has_experiment_running",b"_has_experiment_running","_long_running_operation",b"_long_running_operation","_name",b"_name","base_campaign",b"base_campaign","draft_campaign",b"draft_campaign","draft_id",b"draft_id","has_experiment_running",b"has_experiment_running","long_running_operation",b"long_running_operation","name",b"name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_base_campaign",b"_base_campaign","_draft_campaign",b"_draft_campaign","_draft_id",b"_draft_id","_has_experiment_running",b"_has_experiment_running","_long_running_operation",b"_long_running_operation","_name",b"_name","base_campaign",b"base_campaign","draft_campaign",b"draft_campaign","draft_id",b"draft_id","has_experiment_running",b"has_experiment_running","long_running_operation",b"long_running_operation","name",b"name","resource_name",b"resource_name","status",b"status"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_base_campaign",b"_base_campaign"]) -> typing.Optional[typing_extensions.Literal["base_campaign"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_draft_campaign",b"_draft_campaign"]) -> typing.Optional[typing_extensions.Literal["draft_campaign"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_draft_id",b"_draft_id"]) -> typing.Optional[typing_extensions.Literal["draft_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_has_experiment_running",b"_has_experiment_running"]) -> typing.Optional[typing_extensions.Literal["has_experiment_running"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_long_running_operation",b"_long_running_operation"]) -> typing.Optional[typing_extensions.Literal["long_running_operation"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
global___CampaignDraft = CampaignDraft
