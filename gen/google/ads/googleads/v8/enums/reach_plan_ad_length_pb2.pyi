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

class ReachPlanAdLengthEnum(google.protobuf.message.Message):
    """Proto file describing ad lengths of a plannable video ad.

    Message describing length of a plannable video ad.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ReachPlanAdLength:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ReachPlanAdLengthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReachPlanAdLength.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 1
        """The value is unknown in this version."""

        SIX_SECONDS: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 2
        """6 seconds long ad."""

        FIFTEEN_OR_TWENTY_SECONDS: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 3
        """15 or 20 seconds long ad."""

        TWENTY_SECONDS_OR_MORE: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 4
        """More than 20 seconds long ad."""

    class ReachPlanAdLength(_ReachPlanAdLength, metaclass=_ReachPlanAdLengthEnumTypeWrapper):
        """Possible ad length values."""
        pass

    UNSPECIFIED: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 1
    """The value is unknown in this version."""

    SIX_SECONDS: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 2
    """6 seconds long ad."""

    FIFTEEN_OR_TWENTY_SECONDS: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 3
    """15 or 20 seconds long ad."""

    TWENTY_SECONDS_OR_MORE: ReachPlanAdLengthEnum.ReachPlanAdLength.ValueType = ...  # 4
    """More than 20 seconds long ad."""


    def __init__(self,
        ) -> None: ...
global___ReachPlanAdLengthEnum = ReachPlanAdLengthEnum
