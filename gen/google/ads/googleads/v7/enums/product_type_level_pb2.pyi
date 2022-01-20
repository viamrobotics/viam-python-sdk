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

class ProductTypeLevelEnum(google.protobuf.message.Message):
    """Proto file describing bidding schemes.

    Level of the type of a product offer.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ProductTypeLevel:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ProductTypeLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProductTypeLevel.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        LEVEL1: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 7
        """Level 1."""

        LEVEL2: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 8
        """Level 2."""

        LEVEL3: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 9
        """Level 3."""

        LEVEL4: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 10
        """Level 4."""

        LEVEL5: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 11
        """Level 5."""

    class ProductTypeLevel(_ProductTypeLevel, metaclass=_ProductTypeLevelEnumTypeWrapper):
        """Enum describing the level of the type of a product offer."""
        pass

    UNSPECIFIED: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    LEVEL1: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 7
    """Level 1."""

    LEVEL2: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 8
    """Level 2."""

    LEVEL3: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 9
    """Level 3."""

    LEVEL4: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 10
    """Level 4."""

    LEVEL5: ProductTypeLevelEnum.ProductTypeLevel.ValueType = ...  # 11
    """Level 5."""


    def __init__(self,
        ) -> None: ...
global___ProductTypeLevelEnum = ProductTypeLevelEnum
