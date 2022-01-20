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

class ConversionAttributionEventTypeEnum(google.protobuf.message.Message):
    """Container for enum indicating the event type the conversion is attributed to."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ConversionAttributionEventType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ConversionAttributionEventTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ConversionAttributionEventType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ConversionAttributionEventTypeEnum.ConversionAttributionEventType.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: ConversionAttributionEventTypeEnum.ConversionAttributionEventType.ValueType = ...  # 1
        """Represents value unknown in this version."""

        IMPRESSION: ConversionAttributionEventTypeEnum.ConversionAttributionEventType.ValueType = ...  # 2
        """The conversion is attributed to an impression."""

        INTERACTION: ConversionAttributionEventTypeEnum.ConversionAttributionEventType.ValueType = ...  # 3
        """The conversion is attributed to an interaction."""

    class ConversionAttributionEventType(_ConversionAttributionEventType, metaclass=_ConversionAttributionEventTypeEnumTypeWrapper):
        """The event type of conversions that are attributed to."""
        pass

    UNSPECIFIED: ConversionAttributionEventTypeEnum.ConversionAttributionEventType.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: ConversionAttributionEventTypeEnum.ConversionAttributionEventType.ValueType = ...  # 1
    """Represents value unknown in this version."""

    IMPRESSION: ConversionAttributionEventTypeEnum.ConversionAttributionEventType.ValueType = ...  # 2
    """The conversion is attributed to an impression."""

    INTERACTION: ConversionAttributionEventTypeEnum.ConversionAttributionEventType.ValueType = ...  # 3
    """The conversion is attributed to an interaction."""


    def __init__(self,
        ) -> None: ...
global___ConversionAttributionEventTypeEnum = ConversionAttributionEventTypeEnum
