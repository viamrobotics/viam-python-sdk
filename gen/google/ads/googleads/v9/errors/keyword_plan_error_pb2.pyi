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

class KeywordPlanErrorEnum(google.protobuf.message.Message):
    """Proto file describing errors from applying keyword plan resources (keyword
    plan, keyword plan campaign, keyword plan ad group or keyword plan keyword)
    or KeywordPlanService RPC.

    Container for enum describing possible errors from applying a keyword plan
    resource (keyword plan, keyword plan campaign, keyword plan ad group or
    keyword plan keyword) or KeywordPlanService RPC.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _KeywordPlanError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _KeywordPlanErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KeywordPlanError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        BID_MULTIPLIER_OUT_OF_RANGE: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 2
        """The plan's bid multiplier value is outside the valid range."""

        BID_TOO_HIGH: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 3
        """The plan's bid value is too high."""

        BID_TOO_LOW: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 4
        """The plan's bid value is too low."""

        BID_TOO_MANY_FRACTIONAL_DIGITS: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 5
        """The plan's cpc bid is not a multiple of the minimum billable unit."""

        DAILY_BUDGET_TOO_LOW: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 6
        """The plan's daily budget value is too low."""

        DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 7
        """The plan's daily budget is not a multiple of the minimum billable unit."""

        INVALID_VALUE: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 8
        """The input has an invalid value."""

        KEYWORD_PLAN_HAS_NO_KEYWORDS: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 9
        """The plan has no keyword."""

        KEYWORD_PLAN_NOT_ENABLED: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 10
        """The plan is not enabled and API cannot provide mutation, forecast or
        stats.
        """

        KEYWORD_PLAN_NOT_FOUND: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 11
        """The requested plan cannot be found for providing forecast or stats."""

        MISSING_BID: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 13
        """The plan is missing a cpc bid."""

        MISSING_FORECAST_PERIOD: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 14
        """The plan is missing required forecast_period field."""

        INVALID_FORECAST_DATE_RANGE: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 15
        """The plan's forecast_period has invalid forecast date range."""

        INVALID_NAME: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 16
        """The plan's name is invalid."""

    class KeywordPlanError(_KeywordPlanError, metaclass=_KeywordPlanErrorEnumTypeWrapper):
        """Enum describing possible errors from applying a keyword plan."""
        pass

    UNSPECIFIED: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    BID_MULTIPLIER_OUT_OF_RANGE: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 2
    """The plan's bid multiplier value is outside the valid range."""

    BID_TOO_HIGH: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 3
    """The plan's bid value is too high."""

    BID_TOO_LOW: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 4
    """The plan's bid value is too low."""

    BID_TOO_MANY_FRACTIONAL_DIGITS: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 5
    """The plan's cpc bid is not a multiple of the minimum billable unit."""

    DAILY_BUDGET_TOO_LOW: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 6
    """The plan's daily budget value is too low."""

    DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 7
    """The plan's daily budget is not a multiple of the minimum billable unit."""

    INVALID_VALUE: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 8
    """The input has an invalid value."""

    KEYWORD_PLAN_HAS_NO_KEYWORDS: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 9
    """The plan has no keyword."""

    KEYWORD_PLAN_NOT_ENABLED: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 10
    """The plan is not enabled and API cannot provide mutation, forecast or
    stats.
    """

    KEYWORD_PLAN_NOT_FOUND: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 11
    """The requested plan cannot be found for providing forecast or stats."""

    MISSING_BID: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 13
    """The plan is missing a cpc bid."""

    MISSING_FORECAST_PERIOD: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 14
    """The plan is missing required forecast_period field."""

    INVALID_FORECAST_DATE_RANGE: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 15
    """The plan's forecast_period has invalid forecast date range."""

    INVALID_NAME: KeywordPlanErrorEnum.KeywordPlanError.ValueType = ...  # 16
    """The plan's name is invalid."""


    def __init__(self,
        ) -> None: ...
global___KeywordPlanErrorEnum = KeywordPlanErrorEnum
