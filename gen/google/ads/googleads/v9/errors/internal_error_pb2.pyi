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

class InternalErrorEnum(google.protobuf.message.Message):
    """Proto file describing internal errors.

    Container for enum describing possible internal errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _InternalError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _InternalErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_InternalError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: InternalErrorEnum.InternalError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: InternalErrorEnum.InternalError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        INTERNAL_ERROR: InternalErrorEnum.InternalError.ValueType = ...  # 2
        """Google Ads API encountered unexpected internal error."""

        ERROR_CODE_NOT_PUBLISHED: InternalErrorEnum.InternalError.ValueType = ...  # 3
        """The intended error code doesn't exist in specified API version. It will
        be released in a future API version.
        """

        TRANSIENT_ERROR: InternalErrorEnum.InternalError.ValueType = ...  # 4
        """Google Ads API encountered an unexpected transient error. The user
        should retry their request in these cases.
        """

        DEADLINE_EXCEEDED: InternalErrorEnum.InternalError.ValueType = ...  # 5
        """The request took longer than a deadline."""

    class InternalError(_InternalError, metaclass=_InternalErrorEnumTypeWrapper):
        """Enum describing possible internal errors."""
        pass

    UNSPECIFIED: InternalErrorEnum.InternalError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: InternalErrorEnum.InternalError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    INTERNAL_ERROR: InternalErrorEnum.InternalError.ValueType = ...  # 2
    """Google Ads API encountered unexpected internal error."""

    ERROR_CODE_NOT_PUBLISHED: InternalErrorEnum.InternalError.ValueType = ...  # 3
    """The intended error code doesn't exist in specified API version. It will
    be released in a future API version.
    """

    TRANSIENT_ERROR: InternalErrorEnum.InternalError.ValueType = ...  # 4
    """Google Ads API encountered an unexpected transient error. The user
    should retry their request in these cases.
    """

    DEADLINE_EXCEEDED: InternalErrorEnum.InternalError.ValueType = ...  # 5
    """The request took longer than a deadline."""


    def __init__(self,
        ) -> None: ...
global___InternalErrorEnum = InternalErrorEnum
