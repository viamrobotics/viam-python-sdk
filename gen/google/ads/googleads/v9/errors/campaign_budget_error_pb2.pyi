"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CampaignBudgetErrorEnum(google.protobuf.message.Message):
    """Proto file describing campaign budget errors.

    Container for enum describing possible campaign budget errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CampaignBudgetError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CampaignBudgetErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CampaignBudgetError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        CAMPAIGN_BUDGET_CANNOT_BE_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 17
        """The campaign budget cannot be shared."""

        CAMPAIGN_BUDGET_REMOVED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 2
        """The requested campaign budget no longer exists."""

        CAMPAIGN_BUDGET_IN_USE: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 3
        """The campaign budget is associated with at least one campaign, and so the
        campaign budget cannot be removed.
        """

        CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 4
        """Customer is not on the allow-list for this campaign budget period."""

        CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 6
        """This field is not mutable on implicitly shared campaign budgets"""

        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 7
        """Cannot change explicitly shared campaign budgets back to implicitly
        shared ones.
        """

        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 8
        """An implicit campaign budget without a name cannot be changed to
        explicitly shared campaign budget.
        """

        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 9
        """Cannot change an implicitly shared campaign budget to an explicitly
        shared one.
        """

        CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 10
        """Only explicitly shared campaign budgets can be used with multiple
        campaigns.
        """

        DUPLICATE_NAME: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 11
        """A campaign budget with this name already exists."""

        MONEY_AMOUNT_IN_WRONG_CURRENCY: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 12
        """A money amount was not in the expected currency."""

        MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 13
        """A money amount was less than the minimum CPC for currency."""

        MONEY_AMOUNT_TOO_LARGE: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 14
        """A money amount was greater than the maximum allowed."""

        NEGATIVE_MONEY_AMOUNT: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 15
        """A money amount was negative."""

        NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 16
        """A money amount was not a multiple of a minimum unit."""

        TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 18
        """Total budget amount must be unset when BudgetPeriod is DAILY."""

        INVALID_PERIOD: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 19
        """The period of the budget is not allowed."""

    class CampaignBudgetError(_CampaignBudgetError, metaclass=_CampaignBudgetErrorEnumTypeWrapper):
        """Enum describing possible campaign budget errors."""
        pass

    UNSPECIFIED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    CAMPAIGN_BUDGET_CANNOT_BE_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 17
    """The campaign budget cannot be shared."""

    CAMPAIGN_BUDGET_REMOVED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 2
    """The requested campaign budget no longer exists."""

    CAMPAIGN_BUDGET_IN_USE: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 3
    """The campaign budget is associated with at least one campaign, and so the
    campaign budget cannot be removed.
    """

    CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 4
    """Customer is not on the allow-list for this campaign budget period."""

    CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 6
    """This field is not mutable on implicitly shared campaign budgets"""

    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 7
    """Cannot change explicitly shared campaign budgets back to implicitly
    shared ones.
    """

    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 8
    """An implicit campaign budget without a name cannot be changed to
    explicitly shared campaign budget.
    """

    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 9
    """Cannot change an implicitly shared campaign budget to an explicitly
    shared one.
    """

    CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 10
    """Only explicitly shared campaign budgets can be used with multiple
    campaigns.
    """

    DUPLICATE_NAME: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 11
    """A campaign budget with this name already exists."""

    MONEY_AMOUNT_IN_WRONG_CURRENCY: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 12
    """A money amount was not in the expected currency."""

    MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 13
    """A money amount was less than the minimum CPC for currency."""

    MONEY_AMOUNT_TOO_LARGE: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 14
    """A money amount was greater than the maximum allowed."""

    NEGATIVE_MONEY_AMOUNT: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 15
    """A money amount was negative."""

    NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 16
    """A money amount was not a multiple of a minimum unit."""

    TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 18
    """Total budget amount must be unset when BudgetPeriod is DAILY."""

    INVALID_PERIOD: CampaignBudgetErrorEnum.CampaignBudgetError.ValueType = ...  # 19
    """The period of the budget is not allowed."""


    def __init__(self,
        ) -> None: ...
global___CampaignBudgetErrorEnum = CampaignBudgetErrorEnum
