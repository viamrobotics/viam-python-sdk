"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class KeywordPlanAdGroup(google.protobuf.message.Message):
    """Proto file describing the keyword plan ad group resource.

    A Keyword Planner ad group.
    Max number of keyword plan ad groups per plan: 200.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    KEYWORD_PLAN_CAMPAIGN_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the Keyword Planner ad group.
    KeywordPlanAdGroup resource names have the form:

    `customers/{customer_id}/keywordPlanAdGroups/{kp_ad_group_id}`
    """

    keyword_plan_campaign: typing.Text = ...
    """The keyword plan campaign to which this ad group belongs."""

    id: builtins.int = ...
    """Output only. The ID of the keyword plan ad group."""

    name: typing.Text = ...
    """The name of the keyword plan ad group.

    This field is required and should not be empty when creating keyword plan
    ad group.
    """

    cpc_bid_micros: builtins.int = ...
    """A default ad group max cpc bid in micros in account currency for all
    biddable keywords under the keyword plan ad group.
    If not set, will inherit from parent campaign.
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        keyword_plan_campaign : typing.Optional[typing.Text] = ...,
        id : typing.Optional[builtins.int] = ...,
        name : typing.Optional[typing.Text] = ...,
        cpc_bid_micros : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_cpc_bid_micros",b"_cpc_bid_micros","_id",b"_id","_keyword_plan_campaign",b"_keyword_plan_campaign","_name",b"_name","cpc_bid_micros",b"cpc_bid_micros","id",b"id","keyword_plan_campaign",b"keyword_plan_campaign","name",b"name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_cpc_bid_micros",b"_cpc_bid_micros","_id",b"_id","_keyword_plan_campaign",b"_keyword_plan_campaign","_name",b"_name","cpc_bid_micros",b"cpc_bid_micros","id",b"id","keyword_plan_campaign",b"keyword_plan_campaign","name",b"name","resource_name",b"resource_name"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_cpc_bid_micros",b"_cpc_bid_micros"]) -> typing.Optional[typing_extensions.Literal["cpc_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_keyword_plan_campaign",b"_keyword_plan_campaign"]) -> typing.Optional[typing_extensions.Literal["keyword_plan_campaign"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
global___KeywordPlanAdGroup = KeywordPlanAdGroup
