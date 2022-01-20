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

class ReachPlanAgeRangeEnum(google.protobuf.message.Message):
    """Proto file describing a plannable age range.

    Message describing plannable age ranges.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ReachPlanAgeRange:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ReachPlanAgeRangeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReachPlanAgeRange.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 1
        """The value is unknown in this version."""

        AGE_RANGE_18_24: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503001
        """Between 18 and 24 years old."""

        AGE_RANGE_18_34: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 2
        """Between 18 and 34 years old."""

        AGE_RANGE_18_44: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 3
        """Between 18 and 44 years old."""

        AGE_RANGE_18_49: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 4
        """Between 18 and 49 years old."""

        AGE_RANGE_18_54: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 5
        """Between 18 and 54 years old."""

        AGE_RANGE_18_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 6
        """Between 18 and 64 years old."""

        AGE_RANGE_18_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 7
        """Between 18 and 65+ years old."""

        AGE_RANGE_21_34: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 8
        """Between 21 and 34 years old."""

        AGE_RANGE_25_34: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503002
        """Between 25 and 34 years old."""

        AGE_RANGE_25_44: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 9
        """Between 25 and 44 years old."""

        AGE_RANGE_25_49: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 10
        """Between 25 and 49 years old."""

        AGE_RANGE_25_54: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 11
        """Between 25 and 54 years old."""

        AGE_RANGE_25_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 12
        """Between 25 and 64 years old."""

        AGE_RANGE_25_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 13
        """Between 25 and 65+ years old."""

        AGE_RANGE_35_44: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503003
        """Between 35 and 44 years old."""

        AGE_RANGE_35_49: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 14
        """Between 35 and 49 years old."""

        AGE_RANGE_35_54: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 15
        """Between 35 and 54 years old."""

        AGE_RANGE_35_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 16
        """Between 35 and 64 years old."""

        AGE_RANGE_35_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 17
        """Between 35 and 65+ years old."""

        AGE_RANGE_45_54: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503004
        """Between 45 and 54 years old."""

        AGE_RANGE_45_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 18
        """Between 45 and 64 years old."""

        AGE_RANGE_45_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 19
        """Between 45 and 65+ years old."""

        AGE_RANGE_50_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 20
        """Between 50 and 65+ years old."""

        AGE_RANGE_55_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503005
        """Between 55 and 64 years old."""

        AGE_RANGE_55_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 21
        """Between 55 and 65+ years old."""

        AGE_RANGE_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503006
        """65 years old and beyond."""

    class ReachPlanAgeRange(_ReachPlanAgeRange, metaclass=_ReachPlanAgeRangeEnumTypeWrapper):
        """Possible plannable age range values."""
        pass

    UNSPECIFIED: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 1
    """The value is unknown in this version."""

    AGE_RANGE_18_24: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503001
    """Between 18 and 24 years old."""

    AGE_RANGE_18_34: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 2
    """Between 18 and 34 years old."""

    AGE_RANGE_18_44: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 3
    """Between 18 and 44 years old."""

    AGE_RANGE_18_49: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 4
    """Between 18 and 49 years old."""

    AGE_RANGE_18_54: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 5
    """Between 18 and 54 years old."""

    AGE_RANGE_18_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 6
    """Between 18 and 64 years old."""

    AGE_RANGE_18_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 7
    """Between 18 and 65+ years old."""

    AGE_RANGE_21_34: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 8
    """Between 21 and 34 years old."""

    AGE_RANGE_25_34: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503002
    """Between 25 and 34 years old."""

    AGE_RANGE_25_44: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 9
    """Between 25 and 44 years old."""

    AGE_RANGE_25_49: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 10
    """Between 25 and 49 years old."""

    AGE_RANGE_25_54: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 11
    """Between 25 and 54 years old."""

    AGE_RANGE_25_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 12
    """Between 25 and 64 years old."""

    AGE_RANGE_25_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 13
    """Between 25 and 65+ years old."""

    AGE_RANGE_35_44: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503003
    """Between 35 and 44 years old."""

    AGE_RANGE_35_49: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 14
    """Between 35 and 49 years old."""

    AGE_RANGE_35_54: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 15
    """Between 35 and 54 years old."""

    AGE_RANGE_35_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 16
    """Between 35 and 64 years old."""

    AGE_RANGE_35_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 17
    """Between 35 and 65+ years old."""

    AGE_RANGE_45_54: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503004
    """Between 45 and 54 years old."""

    AGE_RANGE_45_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 18
    """Between 45 and 64 years old."""

    AGE_RANGE_45_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 19
    """Between 45 and 65+ years old."""

    AGE_RANGE_50_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 20
    """Between 50 and 65+ years old."""

    AGE_RANGE_55_64: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503005
    """Between 55 and 64 years old."""

    AGE_RANGE_55_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 21
    """Between 55 and 65+ years old."""

    AGE_RANGE_65_UP: ReachPlanAgeRangeEnum.ReachPlanAgeRange.ValueType = ...  # 503006
    """65 years old and beyond."""


    def __init__(self,
        ) -> None: ...
global___ReachPlanAgeRangeEnum = ReachPlanAgeRangeEnum
