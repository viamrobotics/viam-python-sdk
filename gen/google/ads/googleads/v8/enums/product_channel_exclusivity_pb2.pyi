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

class ProductChannelExclusivityEnum(google.protobuf.message.Message):
    """Proto file describing bidding schemes.

    Availability of a product offer.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ProductChannelExclusivity:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ProductChannelExclusivityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProductChannelExclusivity.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ProductChannelExclusivityEnum.ProductChannelExclusivity.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: ProductChannelExclusivityEnum.ProductChannelExclusivity.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        SINGLE_CHANNEL: ProductChannelExclusivityEnum.ProductChannelExclusivity.ValueType = ...  # 2
        """The item is sold through one channel only, either local stores or online
        as indicated by its ProductChannel.
        """

        MULTI_CHANNEL: ProductChannelExclusivityEnum.ProductChannelExclusivity.ValueType = ...  # 3
        """The item is matched to its online or local stores counterpart, indicating
        it is available for purchase in both ShoppingProductChannels.
        """

    class ProductChannelExclusivity(_ProductChannelExclusivity, metaclass=_ProductChannelExclusivityEnumTypeWrapper):
        """Enum describing the availability of a product offer."""
        pass

    UNSPECIFIED: ProductChannelExclusivityEnum.ProductChannelExclusivity.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: ProductChannelExclusivityEnum.ProductChannelExclusivity.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    SINGLE_CHANNEL: ProductChannelExclusivityEnum.ProductChannelExclusivity.ValueType = ...  # 2
    """The item is sold through one channel only, either local stores or online
    as indicated by its ProductChannel.
    """

    MULTI_CHANNEL: ProductChannelExclusivityEnum.ProductChannelExclusivity.ValueType = ...  # 3
    """The item is matched to its online or local stores counterpart, indicating
    it is available for purchase in both ShoppingProductChannels.
    """


    def __init__(self,
        ) -> None: ...
global___ProductChannelExclusivityEnum = ProductChannelExclusivityEnum
