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

class ResourceAccessDeniedErrorEnum(google.protobuf.message.Message):
    """Proto file describing resource access denied errors.

    Container for enum describing possible resource access denied errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ResourceAccessDeniedError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ResourceAccessDeniedErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ResourceAccessDeniedError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        WRITE_ACCESS_DENIED: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError.ValueType = ...  # 3
        """User did not have write access."""

    class ResourceAccessDeniedError(_ResourceAccessDeniedError, metaclass=_ResourceAccessDeniedErrorEnumTypeWrapper):
        """Enum describing possible resource access denied errors."""
        pass

    UNSPECIFIED: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    WRITE_ACCESS_DENIED: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError.ValueType = ...  # 3
    """User did not have write access."""


    def __init__(self,
        ) -> None: ...
global___ResourceAccessDeniedErrorEnum = ResourceAccessDeniedErrorEnum
