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

class FieldErrorEnum(google.protobuf.message.Message):
    """Proto file describing field errors.

    Container for enum describing possible field errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FieldError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _FieldErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FieldError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: FieldErrorEnum.FieldError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: FieldErrorEnum.FieldError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        REQUIRED: FieldErrorEnum.FieldError.ValueType = ...  # 2
        """The required field was not present."""

        IMMUTABLE_FIELD: FieldErrorEnum.FieldError.ValueType = ...  # 3
        """The field attempted to be mutated is immutable."""

        INVALID_VALUE: FieldErrorEnum.FieldError.ValueType = ...  # 4
        """The field's value is invalid."""

        VALUE_MUST_BE_UNSET: FieldErrorEnum.FieldError.ValueType = ...  # 5
        """The field cannot be set."""

        REQUIRED_NONEMPTY_LIST: FieldErrorEnum.FieldError.ValueType = ...  # 6
        """The required repeated field was empty."""

        FIELD_CANNOT_BE_CLEARED: FieldErrorEnum.FieldError.ValueType = ...  # 7
        """The field cannot be cleared."""

        BLOCKED_VALUE: FieldErrorEnum.FieldError.ValueType = ...  # 9
        """The field's value is on a deny-list for this field."""

    class FieldError(_FieldError, metaclass=_FieldErrorEnumTypeWrapper):
        """Enum describing possible field errors."""
        pass

    UNSPECIFIED: FieldErrorEnum.FieldError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: FieldErrorEnum.FieldError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    REQUIRED: FieldErrorEnum.FieldError.ValueType = ...  # 2
    """The required field was not present."""

    IMMUTABLE_FIELD: FieldErrorEnum.FieldError.ValueType = ...  # 3
    """The field attempted to be mutated is immutable."""

    INVALID_VALUE: FieldErrorEnum.FieldError.ValueType = ...  # 4
    """The field's value is invalid."""

    VALUE_MUST_BE_UNSET: FieldErrorEnum.FieldError.ValueType = ...  # 5
    """The field cannot be set."""

    REQUIRED_NONEMPTY_LIST: FieldErrorEnum.FieldError.ValueType = ...  # 6
    """The required repeated field was empty."""

    FIELD_CANNOT_BE_CLEARED: FieldErrorEnum.FieldError.ValueType = ...  # 7
    """The field cannot be cleared."""

    BLOCKED_VALUE: FieldErrorEnum.FieldError.ValueType = ...  # 9
    """The field's value is on a deny-list for this field."""


    def __init__(self,
        ) -> None: ...
global___FieldErrorEnum = FieldErrorEnum
