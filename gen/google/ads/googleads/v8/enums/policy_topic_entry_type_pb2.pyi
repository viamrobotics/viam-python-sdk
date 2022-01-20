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

class PolicyTopicEntryTypeEnum(google.protobuf.message.Message):
    """Proto file describing policy topic entry types.

    Container for enum describing possible policy topic entry types.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _PolicyTopicEntryType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _PolicyTopicEntryTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PolicyTopicEntryType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 0
        """No value has been specified."""

        UNKNOWN: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 1
        """The received value is not known in this version.

        This is a response-only value.
        """

        PROHIBITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 2
        """The resource will not be served."""

        LIMITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 4
        """The resource will not be served under some circumstances."""

        FULLY_LIMITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 8
        """The resource cannot serve at all because of the current targeting
        criteria.
        """

        DESCRIPTIVE: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 5
        """May be of interest, but does not limit how the resource is served."""

        BROADENING: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 6
        """Could increase coverage beyond normal."""

        AREA_OF_INTEREST_ONLY: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 7
        """Constrained for all targeted countries, but may serve in other countries
        through area of interest.
        """

    class PolicyTopicEntryType(_PolicyTopicEntryType, metaclass=_PolicyTopicEntryTypeEnumTypeWrapper):
        """The possible policy topic entry types."""
        pass

    UNSPECIFIED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 0
    """No value has been specified."""

    UNKNOWN: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 1
    """The received value is not known in this version.

    This is a response-only value.
    """

    PROHIBITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 2
    """The resource will not be served."""

    LIMITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 4
    """The resource will not be served under some circumstances."""

    FULLY_LIMITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 8
    """The resource cannot serve at all because of the current targeting
    criteria.
    """

    DESCRIPTIVE: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 5
    """May be of interest, but does not limit how the resource is served."""

    BROADENING: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 6
    """Could increase coverage beyond normal."""

    AREA_OF_INTEREST_ONLY: PolicyTopicEntryTypeEnum.PolicyTopicEntryType.ValueType = ...  # 7
    """Constrained for all targeted countries, but may serve in other countries
    through area of interest.
    """


    def __init__(self,
        ) -> None: ...
global___PolicyTopicEntryTypeEnum = PolicyTopicEntryTypeEnum
