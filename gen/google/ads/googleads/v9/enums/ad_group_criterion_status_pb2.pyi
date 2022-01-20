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

class AdGroupCriterionStatusEnum(google.protobuf.message.Message):
    """Proto file describing AdGroupCriterion statuses.

    Message describing AdGroupCriterion statuses.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AdGroupCriterionStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AdGroupCriterionStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AdGroupCriterionStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 0
        """No value has been specified."""

        UNKNOWN: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 1
        """The received value is not known in this version.

        This is a response-only value.
        """

        ENABLED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 2
        """The ad group criterion is enabled."""

        PAUSED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 3
        """The ad group criterion is paused."""

        REMOVED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 4
        """The ad group criterion is removed."""

    class AdGroupCriterionStatus(_AdGroupCriterionStatus, metaclass=_AdGroupCriterionStatusEnumTypeWrapper):
        """The possible statuses of an AdGroupCriterion."""
        pass

    UNSPECIFIED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 0
    """No value has been specified."""

    UNKNOWN: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 1
    """The received value is not known in this version.

    This is a response-only value.
    """

    ENABLED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 2
    """The ad group criterion is enabled."""

    PAUSED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 3
    """The ad group criterion is paused."""

    REMOVED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...  # 4
    """The ad group criterion is removed."""


    def __init__(self,
        ) -> None: ...
global___AdGroupCriterionStatusEnum = AdGroupCriterionStatusEnum
