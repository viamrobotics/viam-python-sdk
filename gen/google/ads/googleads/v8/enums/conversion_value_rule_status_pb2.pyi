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

class ConversionValueRuleStatusEnum(google.protobuf.message.Message):
    """Proto file describing conversion value rule status.

    Container for enum describing possible statuses of a conversion value rule.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ConversionValueRuleStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ConversionValueRuleStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ConversionValueRuleStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        ENABLED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 2
        """Conversion Value Rule is enabled and can be applied."""

        REMOVED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 3
        """Conversion Value Rule is permanently deleted and can't be applied."""

        PAUSED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 4
        """Conversion Value Rule is paused, but can be re-enabled."""

    class ConversionValueRuleStatus(_ConversionValueRuleStatus, metaclass=_ConversionValueRuleStatusEnumTypeWrapper):
        """Possible statuses of a conversion value rule."""
        pass

    UNSPECIFIED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    ENABLED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 2
    """Conversion Value Rule is enabled and can be applied."""

    REMOVED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 3
    """Conversion Value Rule is permanently deleted and can't be applied."""

    PAUSED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...  # 4
    """Conversion Value Rule is paused, but can be re-enabled."""


    def __init__(self,
        ) -> None: ...
global___ConversionValueRuleStatusEnum = ConversionValueRuleStatusEnum
