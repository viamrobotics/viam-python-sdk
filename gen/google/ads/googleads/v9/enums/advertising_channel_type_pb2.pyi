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

class AdvertisingChannelTypeEnum(google.protobuf.message.Message):
    """Proto file describing advertising channel types

    The channel type a campaign may target to serve on.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AdvertisingChannelType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AdvertisingChannelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AdvertisingChannelType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        SEARCH: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 2
        """Search Network. Includes display bundled, and Search+ campaigns."""

        DISPLAY: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 3
        """Google Display Network only."""

        SHOPPING: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 4
        """Shopping campaigns serve on the shopping property
        and on google.com search results.
        """

        HOTEL: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 5
        """Hotel Ads campaigns."""

        VIDEO: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 6
        """Video campaigns."""

        MULTI_CHANNEL: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 7
        """App Campaigns, and App Campaigns for Engagement, that run
        across multiple channels.
        """

        LOCAL: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 8
        """Local ads campaigns."""

        SMART: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 9
        """Smart campaigns."""

        PERFORMANCE_MAX: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 10
        """Performance Max campaigns."""

    class AdvertisingChannelType(_AdvertisingChannelType, metaclass=_AdvertisingChannelTypeEnumTypeWrapper):
        """Enum describing the various advertising channel types."""
        pass

    UNSPECIFIED: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    SEARCH: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 2
    """Search Network. Includes display bundled, and Search+ campaigns."""

    DISPLAY: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 3
    """Google Display Network only."""

    SHOPPING: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 4
    """Shopping campaigns serve on the shopping property
    and on google.com search results.
    """

    HOTEL: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 5
    """Hotel Ads campaigns."""

    VIDEO: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 6
    """Video campaigns."""

    MULTI_CHANNEL: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 7
    """App Campaigns, and App Campaigns for Engagement, that run
    across multiple channels.
    """

    LOCAL: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 8
    """Local ads campaigns."""

    SMART: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 9
    """Smart campaigns."""

    PERFORMANCE_MAX: AdvertisingChannelTypeEnum.AdvertisingChannelType.ValueType = ...  # 10
    """Performance Max campaigns."""


    def __init__(self,
        ) -> None: ...
global___AdvertisingChannelTypeEnum = AdvertisingChannelTypeEnum
