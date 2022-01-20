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

class ProductBiddingCategoryStatusEnum(google.protobuf.message.Message):
    """Proto file describing bidding schemes.

    Status of the product bidding category.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ProductBiddingCategoryStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ProductBiddingCategoryStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProductBiddingCategoryStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        ACTIVE: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus.ValueType = ...  # 2
        """The category is active and can be used for bidding."""

        OBSOLETE: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus.ValueType = ...  # 3
        """The category is obsolete. Used only for reporting purposes."""

    class ProductBiddingCategoryStatus(_ProductBiddingCategoryStatus, metaclass=_ProductBiddingCategoryStatusEnumTypeWrapper):
        """Enum describing the status of the product bidding category."""
        pass

    UNSPECIFIED: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    ACTIVE: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus.ValueType = ...  # 2
    """The category is active and can be used for bidding."""

    OBSOLETE: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus.ValueType = ...  # 3
    """The category is obsolete. Used only for reporting purposes."""


    def __init__(self,
        ) -> None: ...
global___ProductBiddingCategoryStatusEnum = ProductBiddingCategoryStatusEnum
