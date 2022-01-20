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

class KeywordPlanAdGroupKeywordErrorEnum(google.protobuf.message.Message):
    """Proto file describing errors from applying a keyword plan ad group keyword or
    keyword plan campaign keyword.

    Container for enum describing possible errors from applying an ad group
    keyword or a campaign keyword from a keyword plan.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _KeywordPlanAdGroupKeywordError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _KeywordPlanAdGroupKeywordErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KeywordPlanAdGroupKeywordError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        INVALID_KEYWORD_MATCH_TYPE: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 2
        """A keyword or negative keyword has invalid match type."""

        DUPLICATE_KEYWORD: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 3
        """A keyword or negative keyword with same text and match type already
        exists.
        """

        KEYWORD_TEXT_TOO_LONG: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 4
        """Keyword or negative keyword text exceeds the allowed limit."""

        KEYWORD_HAS_INVALID_CHARS: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 5
        """Keyword or negative keyword text has invalid characters or symbols."""

        KEYWORD_HAS_TOO_MANY_WORDS: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 6
        """Keyword or negative keyword text has too many words."""

        INVALID_KEYWORD_TEXT: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 7
        """Keyword or negative keyword has invalid text."""

        NEGATIVE_KEYWORD_HAS_CPC_BID: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 8
        """Cpc Bid set for negative keyword."""

        NEW_BMM_KEYWORDS_NOT_ALLOWED: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 9
        """New broad match modifier (BMM) KpAdGroupKeywords are not allowed."""

    class KeywordPlanAdGroupKeywordError(_KeywordPlanAdGroupKeywordError, metaclass=_KeywordPlanAdGroupKeywordErrorEnumTypeWrapper):
        """Enum describing possible errors from applying a keyword plan ad group
        keyword or keyword plan campaign keyword.
        """
        pass

    UNSPECIFIED: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    INVALID_KEYWORD_MATCH_TYPE: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 2
    """A keyword or negative keyword has invalid match type."""

    DUPLICATE_KEYWORD: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 3
    """A keyword or negative keyword with same text and match type already
    exists.
    """

    KEYWORD_TEXT_TOO_LONG: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 4
    """Keyword or negative keyword text exceeds the allowed limit."""

    KEYWORD_HAS_INVALID_CHARS: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 5
    """Keyword or negative keyword text has invalid characters or symbols."""

    KEYWORD_HAS_TOO_MANY_WORDS: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 6
    """Keyword or negative keyword text has too many words."""

    INVALID_KEYWORD_TEXT: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 7
    """Keyword or negative keyword has invalid text."""

    NEGATIVE_KEYWORD_HAS_CPC_BID: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 8
    """Cpc Bid set for negative keyword."""

    NEW_BMM_KEYWORDS_NOT_ALLOWED: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError.ValueType = ...  # 9
    """New broad match modifier (BMM) KpAdGroupKeywords are not allowed."""


    def __init__(self,
        ) -> None: ...
global___KeywordPlanAdGroupKeywordErrorEnum = KeywordPlanAdGroupKeywordErrorEnum
