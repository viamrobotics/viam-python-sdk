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

class CampaignSharedSetErrorEnum(google.protobuf.message.Message):
    """Proto file describing campaign shared set errors.

    Container for enum describing possible campaign shared set errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CampaignSharedSetError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CampaignSharedSetErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CampaignSharedSetError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: CampaignSharedSetErrorEnum.CampaignSharedSetError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: CampaignSharedSetErrorEnum.CampaignSharedSetError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        SHARED_SET_ACCESS_DENIED: CampaignSharedSetErrorEnum.CampaignSharedSetError.ValueType = ...  # 2
        """The shared set belongs to another customer and permission isn't granted."""

    class CampaignSharedSetError(_CampaignSharedSetError, metaclass=_CampaignSharedSetErrorEnumTypeWrapper):
        """Enum describing possible campaign shared set errors."""
        pass

    UNSPECIFIED: CampaignSharedSetErrorEnum.CampaignSharedSetError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: CampaignSharedSetErrorEnum.CampaignSharedSetError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    SHARED_SET_ACCESS_DENIED: CampaignSharedSetErrorEnum.CampaignSharedSetError.ValueType = ...  # 2
    """The shared set belongs to another customer and permission isn't granted."""


    def __init__(self,
        ) -> None: ...
global___CampaignSharedSetErrorEnum = CampaignSharedSetErrorEnum
