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

class FeedItemSetStringFilterTypeEnum(google.protobuf.message.Message):
    """The type of string matching to be used for a dynamic FeedItemSet filter."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FeedItemSetStringFilterType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _FeedItemSetStringFilterTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FeedItemSetStringFilterType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType.ValueType = ...  # 1
        """The received error code is not known in this version."""

        EXACT: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType.ValueType = ...  # 2
        """The dynamic set filter will use exact string matching."""

    class FeedItemSetStringFilterType(_FeedItemSetStringFilterType, metaclass=_FeedItemSetStringFilterTypeEnumTypeWrapper):
        """describe the possible types for a FeedItemSetStringFilter."""
        pass

    UNSPECIFIED: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType.ValueType = ...  # 1
    """The received error code is not known in this version."""

    EXACT: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType.ValueType = ...  # 2
    """The dynamic set filter will use exact string matching."""


    def __init__(self,
        ) -> None: ...
global___FeedItemSetStringFilterTypeEnum = FeedItemSetStringFilterTypeEnum
