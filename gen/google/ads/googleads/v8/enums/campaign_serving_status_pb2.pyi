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

class CampaignServingStatusEnum(google.protobuf.message.Message):
    """Proto file describing Campaign serving statuses.

    Message describing Campaign serving statuses.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CampaignServingStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CampaignServingStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CampaignServingStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 0
        """No value has been specified."""

        UNKNOWN: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 1
        """The received value is not known in this version.

        This is a response-only value.
        """

        SERVING: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 2
        """Serving."""

        NONE: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 3
        """None."""

        ENDED: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 4
        """Ended."""

        PENDING: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 5
        """Pending."""

        SUSPENDED: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 6
        """Suspended."""

    class CampaignServingStatus(_CampaignServingStatus, metaclass=_CampaignServingStatusEnumTypeWrapper):
        """Possible serving statuses of a campaign."""
        pass

    UNSPECIFIED: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 0
    """No value has been specified."""

    UNKNOWN: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 1
    """The received value is not known in this version.

    This is a response-only value.
    """

    SERVING: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 2
    """Serving."""

    NONE: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 3
    """None."""

    ENDED: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 4
    """Ended."""

    PENDING: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 5
    """Pending."""

    SUSPENDED: CampaignServingStatusEnum.CampaignServingStatus.ValueType = ...  # 6
    """Suspended."""


    def __init__(self,
        ) -> None: ...
global___CampaignServingStatusEnum = CampaignServingStatusEnum
