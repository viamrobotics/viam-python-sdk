"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.enums.campaign_shared_set_status_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CampaignSharedSet(google.protobuf.message.Message):
    """Proto file describing the CampaignSharedSet resource.

    CampaignSharedSets are used for managing the shared sets associated with a
    campaign.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CAMPAIGN_FIELD_NUMBER: builtins.int
    SHARED_SET_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the campaign shared set.
    Campaign shared set resource names have the form:

    `customers/{customer_id}/campaignSharedSets/{campaign_id}~{shared_set_id}`
    """

    campaign: typing.Text = ...
    """Immutable. The campaign to which the campaign shared set belongs."""

    shared_set: typing.Text = ...
    """Immutable. The shared set associated with the campaign. This may be a negative keyword
    shared set of another customer. This customer should be a manager of the
    other customer, otherwise the campaign shared set will exist but have no
    serving effect. Only negative keyword shared sets can be associated with
    Shopping campaigns. Only negative placement shared sets can be associated
    with Display mobile app campaigns.
    """

    status: google.ads.googleads.v7.enums.campaign_shared_set_status_pb2.CampaignSharedSetStatusEnum.CampaignSharedSetStatus.ValueType = ...
    """Output only. The status of this campaign shared set. Read only."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        campaign : typing.Optional[typing.Text] = ...,
        shared_set : typing.Optional[typing.Text] = ...,
        status : google.ads.googleads.v7.enums.campaign_shared_set_status_pb2.CampaignSharedSetStatusEnum.CampaignSharedSetStatus.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_campaign",b"_campaign","_shared_set",b"_shared_set","campaign",b"campaign","shared_set",b"shared_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_campaign",b"_campaign","_shared_set",b"_shared_set","campaign",b"campaign","resource_name",b"resource_name","shared_set",b"shared_set","status",b"status"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_campaign",b"_campaign"]) -> typing.Optional[typing_extensions.Literal["campaign"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_shared_set",b"_shared_set"]) -> typing.Optional[typing_extensions.Literal["shared_set"]]: ...
global___CampaignSharedSet = CampaignSharedSet
