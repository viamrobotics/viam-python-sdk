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

class CustomInterestStatusEnum(google.protobuf.message.Message):
    """Proto file describing custom interest status.

    The status of custom interest.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CustomInterestStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CustomInterestStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CustomInterestStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: CustomInterestStatusEnum.CustomInterestStatus.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: CustomInterestStatusEnum.CustomInterestStatus.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        ENABLED: CustomInterestStatusEnum.CustomInterestStatus.ValueType = ...  # 2
        """Enabled status - custom interest is enabled and can be targeted to."""

        REMOVED: CustomInterestStatusEnum.CustomInterestStatus.ValueType = ...  # 3
        """Removed status - custom interest is removed and cannot be used for
        targeting.
        """

    class CustomInterestStatus(_CustomInterestStatus, metaclass=_CustomInterestStatusEnumTypeWrapper):
        """Enum containing possible custom interest types."""
        pass

    UNSPECIFIED: CustomInterestStatusEnum.CustomInterestStatus.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: CustomInterestStatusEnum.CustomInterestStatus.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    ENABLED: CustomInterestStatusEnum.CustomInterestStatus.ValueType = ...  # 2
    """Enabled status - custom interest is enabled and can be targeted to."""

    REMOVED: CustomInterestStatusEnum.CustomInterestStatus.ValueType = ...  # 3
    """Removed status - custom interest is removed and cannot be used for
    targeting.
    """


    def __init__(self,
        ) -> None: ...
global___CustomInterestStatusEnum = CustomInterestStatusEnum
