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

class TimeTypeEnum(google.protobuf.message.Message):
    """Proto file describing TimeType types.

    Message describing time types.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _TimeType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TimeTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TimeType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: TimeTypeEnum.TimeType.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: TimeTypeEnum.TimeType.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        NOW: TimeTypeEnum.TimeType.ValueType = ...  # 2
        """As soon as possible."""

        FOREVER: TimeTypeEnum.TimeType.ValueType = ...  # 3
        """An infinite point in the future."""

    class TimeType(_TimeType, metaclass=_TimeTypeEnumTypeWrapper):
        """The possible time types used by certain resources as an alternative to
        absolute timestamps.
        """
        pass

    UNSPECIFIED: TimeTypeEnum.TimeType.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: TimeTypeEnum.TimeType.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    NOW: TimeTypeEnum.TimeType.ValueType = ...  # 2
    """As soon as possible."""

    FOREVER: TimeTypeEnum.TimeType.ValueType = ...  # 3
    """An infinite point in the future."""


    def __init__(self,
        ) -> None: ...
global___TimeTypeEnum = TimeTypeEnum
