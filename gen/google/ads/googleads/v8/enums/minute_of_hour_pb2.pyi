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

class MinuteOfHourEnum(google.protobuf.message.Message):
    """Proto file describing days of week.

    Container for enumeration of quarter-hours.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _MinuteOfHour:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _MinuteOfHourEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MinuteOfHour.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 1
        """The value is unknown in this version."""

        ZERO: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 2
        """Zero minutes past the hour."""

        FIFTEEN: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 3
        """Fifteen minutes past the hour."""

        THIRTY: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 4
        """Thirty minutes past the hour."""

        FORTY_FIVE: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 5
        """Forty-five minutes past the hour."""

    class MinuteOfHour(_MinuteOfHour, metaclass=_MinuteOfHourEnumTypeWrapper):
        """Enumerates of quarter-hours. E.g. "FIFTEEN" """
        pass

    UNSPECIFIED: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 1
    """The value is unknown in this version."""

    ZERO: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 2
    """Zero minutes past the hour."""

    FIFTEEN: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 3
    """Fifteen minutes past the hour."""

    THIRTY: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 4
    """Thirty minutes past the hour."""

    FORTY_FIVE: MinuteOfHourEnum.MinuteOfHour.ValueType = ...  # 5
    """Forty-five minutes past the hour."""


    def __init__(self,
        ) -> None: ...
global___MinuteOfHourEnum = MinuteOfHourEnum
