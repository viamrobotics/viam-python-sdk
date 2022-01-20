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

class LocationSourceTypeEnum(google.protobuf.message.Message):
    """Proto file describing location source types.

    Used to distinguish the location source type.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _LocationSourceType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _LocationSourceTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LocationSourceType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: LocationSourceTypeEnum.LocationSourceType.ValueType = ...  # 0
        """No value has been specified."""

        UNKNOWN: LocationSourceTypeEnum.LocationSourceType.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        GOOGLE_MY_BUSINESS: LocationSourceTypeEnum.LocationSourceType.ValueType = ...  # 2
        """Locations associated with the customer's linked Business Profile."""

        AFFILIATE: LocationSourceTypeEnum.LocationSourceType.ValueType = ...  # 3
        """Affiliate (chain) store locations. For example, Best Buy store locations."""

    class LocationSourceType(_LocationSourceType, metaclass=_LocationSourceTypeEnumTypeWrapper):
        """The possible types of a location source."""
        pass

    UNSPECIFIED: LocationSourceTypeEnum.LocationSourceType.ValueType = ...  # 0
    """No value has been specified."""

    UNKNOWN: LocationSourceTypeEnum.LocationSourceType.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    GOOGLE_MY_BUSINESS: LocationSourceTypeEnum.LocationSourceType.ValueType = ...  # 2
    """Locations associated with the customer's linked Business Profile."""

    AFFILIATE: LocationSourceTypeEnum.LocationSourceType.ValueType = ...  # 3
    """Affiliate (chain) store locations. For example, Best Buy store locations."""


    def __init__(self,
        ) -> None: ...
global___LocationSourceTypeEnum = LocationSourceTypeEnum
