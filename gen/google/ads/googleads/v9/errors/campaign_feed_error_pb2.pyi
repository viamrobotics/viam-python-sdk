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

class CampaignFeedErrorEnum(google.protobuf.message.Message):
    """Proto file describing campaign feed errors.

    Container for enum describing possible campaign feed errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CampaignFeedError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CampaignFeedErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CampaignFeedError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 2
        """An active feed already exists for this campaign and placeholder type."""

        CANNOT_CREATE_FOR_REMOVED_FEED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 4
        """The specified feed is removed."""

        CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 5
        """The CampaignFeed already exists. UPDATE should be used to modify the
        existing CampaignFeed.
        """

        CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 6
        """Cannot update removed campaign feed."""

        INVALID_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 7
        """Invalid placeholder type."""

        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 8
        """Feed mapping for this placeholder type does not exist."""

        NO_EXISTING_LOCATION_CUSTOMER_FEED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 9
        """Location CampaignFeeds cannot be created unless there is a location
        CustomerFeed for the specified feed.
        """

    class CampaignFeedError(_CampaignFeedError, metaclass=_CampaignFeedErrorEnumTypeWrapper):
        """Enum describing possible campaign feed errors."""
        pass

    UNSPECIFIED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 2
    """An active feed already exists for this campaign and placeholder type."""

    CANNOT_CREATE_FOR_REMOVED_FEED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 4
    """The specified feed is removed."""

    CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 5
    """The CampaignFeed already exists. UPDATE should be used to modify the
    existing CampaignFeed.
    """

    CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 6
    """Cannot update removed campaign feed."""

    INVALID_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 7
    """Invalid placeholder type."""

    MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 8
    """Feed mapping for this placeholder type does not exist."""

    NO_EXISTING_LOCATION_CUSTOMER_FEED: CampaignFeedErrorEnum.CampaignFeedError.ValueType = ...  # 9
    """Location CampaignFeeds cannot be created unless there is a location
    CustomerFeed for the specified feed.
    """


    def __init__(self,
        ) -> None: ...
global___CampaignFeedErrorEnum = CampaignFeedErrorEnum
