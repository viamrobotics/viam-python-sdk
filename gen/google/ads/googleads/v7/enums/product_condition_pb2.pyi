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

class ProductConditionEnum(google.protobuf.message.Message):
    """Proto file describing bidding schemes.

    Condition of a product offer.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ProductCondition:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ProductConditionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProductCondition.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ProductConditionEnum.ProductCondition.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: ProductConditionEnum.ProductCondition.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        NEW: ProductConditionEnum.ProductCondition.ValueType = ...  # 3
        """The product condition is new."""

        REFURBISHED: ProductConditionEnum.ProductCondition.ValueType = ...  # 4
        """The product condition is refurbished."""

        USED: ProductConditionEnum.ProductCondition.ValueType = ...  # 5
        """The product condition is used."""

    class ProductCondition(_ProductCondition, metaclass=_ProductConditionEnumTypeWrapper):
        """Enum describing the condition of a product offer."""
        pass

    UNSPECIFIED: ProductConditionEnum.ProductCondition.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: ProductConditionEnum.ProductCondition.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    NEW: ProductConditionEnum.ProductCondition.ValueType = ...  # 3
    """The product condition is new."""

    REFURBISHED: ProductConditionEnum.ProductCondition.ValueType = ...  # 4
    """The product condition is refurbished."""

    USED: ProductConditionEnum.ProductCondition.ValueType = ...  # 5
    """The product condition is used."""


    def __init__(self,
        ) -> None: ...
global___ProductConditionEnum = ProductConditionEnum
