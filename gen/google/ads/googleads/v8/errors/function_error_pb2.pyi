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

class FunctionErrorEnum(google.protobuf.message.Message):
    """Proto file describing function errors.

    Container for enum describing possible function errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FunctionError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _FunctionErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FunctionError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: FunctionErrorEnum.FunctionError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: FunctionErrorEnum.FunctionError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        INVALID_FUNCTION_FORMAT: FunctionErrorEnum.FunctionError.ValueType = ...  # 2
        """The format of the function is not recognized as a supported function
        format.
        """

        DATA_TYPE_MISMATCH: FunctionErrorEnum.FunctionError.ValueType = ...  # 3
        """Operand data types do not match."""

        INVALID_CONJUNCTION_OPERANDS: FunctionErrorEnum.FunctionError.ValueType = ...  # 4
        """The operands cannot be used together in a conjunction."""

        INVALID_NUMBER_OF_OPERANDS: FunctionErrorEnum.FunctionError.ValueType = ...  # 5
        """Invalid numer of Operands."""

        INVALID_OPERAND_TYPE: FunctionErrorEnum.FunctionError.ValueType = ...  # 6
        """Operand Type not supported."""

        INVALID_OPERATOR: FunctionErrorEnum.FunctionError.ValueType = ...  # 7
        """Operator not supported."""

        INVALID_REQUEST_CONTEXT_TYPE: FunctionErrorEnum.FunctionError.ValueType = ...  # 8
        """Request context type not supported."""

        INVALID_FUNCTION_FOR_CALL_PLACEHOLDER: FunctionErrorEnum.FunctionError.ValueType = ...  # 9
        """The matching function is not allowed for call placeholders"""

        INVALID_FUNCTION_FOR_PLACEHOLDER: FunctionErrorEnum.FunctionError.ValueType = ...  # 10
        """The matching function is not allowed for the specified placeholder"""

        INVALID_OPERAND: FunctionErrorEnum.FunctionError.ValueType = ...  # 11
        """Invalid operand."""

        MISSING_CONSTANT_OPERAND_VALUE: FunctionErrorEnum.FunctionError.ValueType = ...  # 12
        """Missing value for the constant operand."""

        INVALID_CONSTANT_OPERAND_VALUE: FunctionErrorEnum.FunctionError.ValueType = ...  # 13
        """The value of the constant operand is invalid."""

        INVALID_NESTING: FunctionErrorEnum.FunctionError.ValueType = ...  # 14
        """Invalid function nesting."""

        MULTIPLE_FEED_IDS_NOT_SUPPORTED: FunctionErrorEnum.FunctionError.ValueType = ...  # 15
        """The Feed ID was different from another Feed ID in the same function."""

        INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA: FunctionErrorEnum.FunctionError.ValueType = ...  # 16
        """The matching function is invalid for use with a feed with a fixed schema."""

        INVALID_ATTRIBUTE_NAME: FunctionErrorEnum.FunctionError.ValueType = ...  # 17
        """Invalid attribute name."""

    class FunctionError(_FunctionError, metaclass=_FunctionErrorEnumTypeWrapper):
        """Enum describing possible function errors."""
        pass

    UNSPECIFIED: FunctionErrorEnum.FunctionError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: FunctionErrorEnum.FunctionError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    INVALID_FUNCTION_FORMAT: FunctionErrorEnum.FunctionError.ValueType = ...  # 2
    """The format of the function is not recognized as a supported function
    format.
    """

    DATA_TYPE_MISMATCH: FunctionErrorEnum.FunctionError.ValueType = ...  # 3
    """Operand data types do not match."""

    INVALID_CONJUNCTION_OPERANDS: FunctionErrorEnum.FunctionError.ValueType = ...  # 4
    """The operands cannot be used together in a conjunction."""

    INVALID_NUMBER_OF_OPERANDS: FunctionErrorEnum.FunctionError.ValueType = ...  # 5
    """Invalid numer of Operands."""

    INVALID_OPERAND_TYPE: FunctionErrorEnum.FunctionError.ValueType = ...  # 6
    """Operand Type not supported."""

    INVALID_OPERATOR: FunctionErrorEnum.FunctionError.ValueType = ...  # 7
    """Operator not supported."""

    INVALID_REQUEST_CONTEXT_TYPE: FunctionErrorEnum.FunctionError.ValueType = ...  # 8
    """Request context type not supported."""

    INVALID_FUNCTION_FOR_CALL_PLACEHOLDER: FunctionErrorEnum.FunctionError.ValueType = ...  # 9
    """The matching function is not allowed for call placeholders"""

    INVALID_FUNCTION_FOR_PLACEHOLDER: FunctionErrorEnum.FunctionError.ValueType = ...  # 10
    """The matching function is not allowed for the specified placeholder"""

    INVALID_OPERAND: FunctionErrorEnum.FunctionError.ValueType = ...  # 11
    """Invalid operand."""

    MISSING_CONSTANT_OPERAND_VALUE: FunctionErrorEnum.FunctionError.ValueType = ...  # 12
    """Missing value for the constant operand."""

    INVALID_CONSTANT_OPERAND_VALUE: FunctionErrorEnum.FunctionError.ValueType = ...  # 13
    """The value of the constant operand is invalid."""

    INVALID_NESTING: FunctionErrorEnum.FunctionError.ValueType = ...  # 14
    """Invalid function nesting."""

    MULTIPLE_FEED_IDS_NOT_SUPPORTED: FunctionErrorEnum.FunctionError.ValueType = ...  # 15
    """The Feed ID was different from another Feed ID in the same function."""

    INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA: FunctionErrorEnum.FunctionError.ValueType = ...  # 16
    """The matching function is invalid for use with a feed with a fixed schema."""

    INVALID_ATTRIBUTE_NAME: FunctionErrorEnum.FunctionError.ValueType = ...  # 17
    """Invalid attribute name."""


    def __init__(self,
        ) -> None: ...
global___FunctionErrorEnum = FunctionErrorEnum
