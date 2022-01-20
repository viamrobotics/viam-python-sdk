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

class ReachPlanErrorEnum(google.protobuf.message.Message):
    """Proto file describing errors generated from ReachPlanService.

    Container for enum describing possible errors returned from
    the ReachPlanService.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ReachPlanError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ReachPlanErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReachPlanError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ReachPlanErrorEnum.ReachPlanError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: ReachPlanErrorEnum.ReachPlanError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        NOT_FORECASTABLE_MISSING_RATE: ReachPlanErrorEnum.ReachPlanError.ValueType = ...  # 2
        """Not forecastable due to missing rate card data."""

    class ReachPlanError(_ReachPlanError, metaclass=_ReachPlanErrorEnumTypeWrapper):
        """Enum describing possible errors from ReachPlanService."""
        pass

    UNSPECIFIED: ReachPlanErrorEnum.ReachPlanError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: ReachPlanErrorEnum.ReachPlanError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    NOT_FORECASTABLE_MISSING_RATE: ReachPlanErrorEnum.ReachPlanError.ValueType = ...  # 2
    """Not forecastable due to missing rate card data."""


    def __init__(self,
        ) -> None: ...
global___ReachPlanErrorEnum = ReachPlanErrorEnum
