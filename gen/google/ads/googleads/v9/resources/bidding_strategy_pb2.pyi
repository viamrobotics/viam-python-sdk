"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.common.bidding_pb2
import google.ads.googleads.v9.enums.bidding_strategy_status_pb2
import google.ads.googleads.v9.enums.bidding_strategy_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BiddingStrategy(google.protobuf.message.Message):
    """Proto file describing the BiddingStrategy resource

    A bidding strategy.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CURRENCY_CODE_FIELD_NUMBER: builtins.int
    EFFECTIVE_CURRENCY_CODE_FIELD_NUMBER: builtins.int
    CAMPAIGN_COUNT_FIELD_NUMBER: builtins.int
    NON_REMOVED_CAMPAIGN_COUNT_FIELD_NUMBER: builtins.int
    ENHANCED_CPC_FIELD_NUMBER: builtins.int
    MAXIMIZE_CONVERSION_VALUE_FIELD_NUMBER: builtins.int
    MAXIMIZE_CONVERSIONS_FIELD_NUMBER: builtins.int
    TARGET_CPA_FIELD_NUMBER: builtins.int
    TARGET_IMPRESSION_SHARE_FIELD_NUMBER: builtins.int
    TARGET_ROAS_FIELD_NUMBER: builtins.int
    TARGET_SPEND_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the bidding strategy.
    Bidding strategy resource names have the form:

    `customers/{customer_id}/biddingStrategies/{bidding_strategy_id}`
    """

    id: builtins.int = ...
    """Output only. The ID of the bidding strategy."""

    name: typing.Text = ...
    """The name of the bidding strategy.
    All bidding strategies within an account must be named distinctly.

    The length of this string should be between 1 and 255, inclusive,
    in UTF-8 bytes, (trimmed).
    """

    status: google.ads.googleads.v9.enums.bidding_strategy_status_pb2.BiddingStrategyStatusEnum.BiddingStrategyStatus.ValueType = ...
    """Output only. The status of the bidding strategy.

    This field is read-only.
    """

    type: google.ads.googleads.v9.enums.bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType.ValueType = ...
    """Output only. The type of the bidding strategy.
    Create a bidding strategy by setting the bidding scheme.

    This field is read-only.
    """

    currency_code: typing.Text = ...
    """Immutable. The currency used by the bidding strategy (ISO 4217 three-letter code).

    For bidding strategies in manager customers, this currency can be set on
    creation and defaults to the manager customer's currency. For serving
    customers, this field cannot be set; all strategies in a serving customer
    implicitly use the serving customer's currency. In all cases the
    effective_currency_code field returns the currency used by the strategy.
    """

    effective_currency_code: typing.Text = ...
    """Output only. The currency used by the bidding strategy (ISO 4217 three-letter code).

    For bidding strategies in manager customers, this is the currency set by
    the advertiser when creating the strategy. For serving customers, this is
    the customer's currency_code.

    Bidding strategy metrics are reported in this currency.

    This field is read-only.
    """

    campaign_count: builtins.int = ...
    """Output only. The number of campaigns attached to this bidding strategy.

    This field is read-only.
    """

    non_removed_campaign_count: builtins.int = ...
    """Output only. The number of non-removed campaigns attached to this bidding strategy.

    This field is read-only.
    """

    @property
    def enhanced_cpc(self) -> google.ads.googleads.v9.common.bidding_pb2.EnhancedCpc:
        """A bidding strategy that raises bids for clicks that seem more likely to
        lead to a conversion and lowers them for clicks where they seem less
        likely.
        """
        pass
    @property
    def maximize_conversion_value(self) -> google.ads.googleads.v9.common.bidding_pb2.MaximizeConversionValue:
        """An automated bidding strategy to help get the most conversion value for
        your campaigns while spending your budget.
        """
        pass
    @property
    def maximize_conversions(self) -> google.ads.googleads.v9.common.bidding_pb2.MaximizeConversions:
        """An automated bidding strategy to help get the most conversions for your
        campaigns while spending your budget.
        """
        pass
    @property
    def target_cpa(self) -> google.ads.googleads.v9.common.bidding_pb2.TargetCpa:
        """A bidding strategy that sets bids to help get as many conversions as
        possible at the target cost-per-acquisition (CPA) you set.
        """
        pass
    @property
    def target_impression_share(self) -> google.ads.googleads.v9.common.bidding_pb2.TargetImpressionShare:
        """A bidding strategy that automatically optimizes towards a desired
        percentage of impressions.
        """
        pass
    @property
    def target_roas(self) -> google.ads.googleads.v9.common.bidding_pb2.TargetRoas:
        """A bidding strategy that helps you maximize revenue while averaging a
        specific target Return On Ad Spend (ROAS).
        """
        pass
    @property
    def target_spend(self) -> google.ads.googleads.v9.common.bidding_pb2.TargetSpend:
        """A bid strategy that sets your bids to help get as many clicks as
        possible within your budget.
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : typing.Optional[builtins.int] = ...,
        name : typing.Optional[typing.Text] = ...,
        status : google.ads.googleads.v9.enums.bidding_strategy_status_pb2.BiddingStrategyStatusEnum.BiddingStrategyStatus.ValueType = ...,
        type : google.ads.googleads.v9.enums.bidding_strategy_type_pb2.BiddingStrategyTypeEnum.BiddingStrategyType.ValueType = ...,
        currency_code : typing.Text = ...,
        effective_currency_code : typing.Optional[typing.Text] = ...,
        campaign_count : typing.Optional[builtins.int] = ...,
        non_removed_campaign_count : typing.Optional[builtins.int] = ...,
        enhanced_cpc : typing.Optional[google.ads.googleads.v9.common.bidding_pb2.EnhancedCpc] = ...,
        maximize_conversion_value : typing.Optional[google.ads.googleads.v9.common.bidding_pb2.MaximizeConversionValue] = ...,
        maximize_conversions : typing.Optional[google.ads.googleads.v9.common.bidding_pb2.MaximizeConversions] = ...,
        target_cpa : typing.Optional[google.ads.googleads.v9.common.bidding_pb2.TargetCpa] = ...,
        target_impression_share : typing.Optional[google.ads.googleads.v9.common.bidding_pb2.TargetImpressionShare] = ...,
        target_roas : typing.Optional[google.ads.googleads.v9.common.bidding_pb2.TargetRoas] = ...,
        target_spend : typing.Optional[google.ads.googleads.v9.common.bidding_pb2.TargetSpend] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_campaign_count",b"_campaign_count","_effective_currency_code",b"_effective_currency_code","_id",b"_id","_name",b"_name","_non_removed_campaign_count",b"_non_removed_campaign_count","campaign_count",b"campaign_count","effective_currency_code",b"effective_currency_code","enhanced_cpc",b"enhanced_cpc","id",b"id","maximize_conversion_value",b"maximize_conversion_value","maximize_conversions",b"maximize_conversions","name",b"name","non_removed_campaign_count",b"non_removed_campaign_count","scheme",b"scheme","target_cpa",b"target_cpa","target_impression_share",b"target_impression_share","target_roas",b"target_roas","target_spend",b"target_spend"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_campaign_count",b"_campaign_count","_effective_currency_code",b"_effective_currency_code","_id",b"_id","_name",b"_name","_non_removed_campaign_count",b"_non_removed_campaign_count","campaign_count",b"campaign_count","currency_code",b"currency_code","effective_currency_code",b"effective_currency_code","enhanced_cpc",b"enhanced_cpc","id",b"id","maximize_conversion_value",b"maximize_conversion_value","maximize_conversions",b"maximize_conversions","name",b"name","non_removed_campaign_count",b"non_removed_campaign_count","resource_name",b"resource_name","scheme",b"scheme","status",b"status","target_cpa",b"target_cpa","target_impression_share",b"target_impression_share","target_roas",b"target_roas","target_spend",b"target_spend","type",b"type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_campaign_count",b"_campaign_count"]) -> typing.Optional[typing_extensions.Literal["campaign_count"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_effective_currency_code",b"_effective_currency_code"]) -> typing.Optional[typing_extensions.Literal["effective_currency_code"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_non_removed_campaign_count",b"_non_removed_campaign_count"]) -> typing.Optional[typing_extensions.Literal["non_removed_campaign_count"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["scheme",b"scheme"]) -> typing.Optional[typing_extensions.Literal["enhanced_cpc","maximize_conversion_value","maximize_conversions","target_cpa","target_impression_share","target_roas","target_spend"]]: ...
global___BiddingStrategy = BiddingStrategy
