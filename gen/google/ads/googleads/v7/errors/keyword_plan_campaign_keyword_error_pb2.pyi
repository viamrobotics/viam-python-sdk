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

class KeywordPlanCampaignKeywordErrorEnum(google.protobuf.message.Message):
    """Proto file describing errors from applying a keyword plan campaign keyword.

    Container for enum describing possible errors from applying a keyword plan
    campaign keyword.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _KeywordPlanCampaignKeywordError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _KeywordPlanCampaignKeywordErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KeywordPlanCampaignKeywordError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        CAMPAIGN_KEYWORD_IS_POSITIVE: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError.ValueType = ...  # 8
        """Keyword plan campaign keyword is positive."""

    class KeywordPlanCampaignKeywordError(_KeywordPlanCampaignKeywordError, metaclass=_KeywordPlanCampaignKeywordErrorEnumTypeWrapper):
        """Enum describing possible errors from applying a keyword plan campaign
        keyword.
        """
        pass

    UNSPECIFIED: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    CAMPAIGN_KEYWORD_IS_POSITIVE: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError.ValueType = ...  # 8
    """Keyword plan campaign keyword is positive."""


    def __init__(self,
        ) -> None: ...
global___KeywordPlanCampaignKeywordErrorEnum = KeywordPlanCampaignKeywordErrorEnum
