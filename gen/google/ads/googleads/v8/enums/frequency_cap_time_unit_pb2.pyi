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

class FrequencyCapTimeUnitEnum(google.protobuf.message.Message):
    """Proto file describing frequency caps.

    Container for enum describing the unit of time the cap is defined at.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FrequencyCapTimeUnit:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _FrequencyCapTimeUnitEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FrequencyCapTimeUnit.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        DAY: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 2
        """The cap would define limit per one day."""

        WEEK: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 3
        """The cap would define limit per one week."""

        MONTH: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 4
        """The cap would define limit per one month."""

    class FrequencyCapTimeUnit(_FrequencyCapTimeUnit, metaclass=_FrequencyCapTimeUnitEnumTypeWrapper):
        """Unit of time the cap is defined at (e.g. day, week)."""
        pass

    UNSPECIFIED: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    DAY: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 2
    """The cap would define limit per one day."""

    WEEK: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 3
    """The cap would define limit per one week."""

    MONTH: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...  # 4
    """The cap would define limit per one month."""


    def __init__(self,
        ) -> None: ...
global___FrequencyCapTimeUnitEnum = FrequencyCapTimeUnitEnum
