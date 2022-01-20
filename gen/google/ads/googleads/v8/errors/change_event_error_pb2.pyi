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

class ChangeEventErrorEnum(google.protobuf.message.Message):
    """Proto file describing change event errors.

    Container for enum describing possible change event errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ChangeEventError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ChangeEventErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ChangeEventError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        START_DATE_TOO_OLD: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 2
        """The requested start date is too old. It cannot be older than 30 days."""

        CHANGE_DATE_RANGE_INFINITE: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 3
        """The change_event search request must specify a finite range filter
        on change_date_time.
        """

        CHANGE_DATE_RANGE_NEGATIVE: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 4
        """The change event search request has specified invalid date time filters
        that can never logically produce any valid results (for example, start
        time after end time).
        """

        LIMIT_NOT_SPECIFIED: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 5
        """The change_event search request must specify a LIMIT."""

        INVALID_LIMIT_CLAUSE: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 6
        """The LIMIT specified by change_event request should be less than or equal
        to 10K.
        """

    class ChangeEventError(_ChangeEventError, metaclass=_ChangeEventErrorEnumTypeWrapper):
        """Enum describing possible change event errors."""
        pass

    UNSPECIFIED: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    START_DATE_TOO_OLD: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 2
    """The requested start date is too old. It cannot be older than 30 days."""

    CHANGE_DATE_RANGE_INFINITE: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 3
    """The change_event search request must specify a finite range filter
    on change_date_time.
    """

    CHANGE_DATE_RANGE_NEGATIVE: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 4
    """The change event search request has specified invalid date time filters
    that can never logically produce any valid results (for example, start
    time after end time).
    """

    LIMIT_NOT_SPECIFIED: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 5
    """The change_event search request must specify a LIMIT."""

    INVALID_LIMIT_CLAUSE: ChangeEventErrorEnum.ChangeEventError.ValueType = ...  # 6
    """The LIMIT specified by change_event request should be less than or equal
    to 10K.
    """


    def __init__(self,
        ) -> None: ...
global___ChangeEventErrorEnum = ChangeEventErrorEnum
