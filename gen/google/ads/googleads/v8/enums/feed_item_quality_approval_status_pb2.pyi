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

class FeedItemQualityApprovalStatusEnum(google.protobuf.message.Message):
    """Proto file describing feed item quality evaluation approval statuses.

    Container for enum describing possible quality evaluation approval statuses
    of a feed item.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FeedItemQualityApprovalStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _FeedItemQualityApprovalStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FeedItemQualityApprovalStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.ValueType = ...  # 0
        """No value has been specified."""

        UNKNOWN: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        APPROVED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.ValueType = ...  # 2
        """Meets all quality expectations."""

        DISAPPROVED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.ValueType = ...  # 3
        """Does not meet some quality expectations. The specific reason is found in
        the quality_disapproval_reasons field.
        """

    class FeedItemQualityApprovalStatus(_FeedItemQualityApprovalStatus, metaclass=_FeedItemQualityApprovalStatusEnumTypeWrapper):
        """The possible quality evaluation approval statuses of a feed item."""
        pass

    UNSPECIFIED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.ValueType = ...  # 0
    """No value has been specified."""

    UNKNOWN: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    APPROVED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.ValueType = ...  # 2
    """Meets all quality expectations."""

    DISAPPROVED: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus.ValueType = ...  # 3
    """Does not meet some quality expectations. The specific reason is found in
    the quality_disapproval_reasons field.
    """


    def __init__(self,
        ) -> None: ...
global___FeedItemQualityApprovalStatusEnum = FeedItemQualityApprovalStatusEnum
