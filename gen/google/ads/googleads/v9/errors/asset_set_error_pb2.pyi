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

class AssetSetErrorEnum(google.protobuf.message.Message):
    """Proto file describing asset set errors.

    Container for enum describing possible asset set errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AssetSetError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AssetSetErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AssetSetError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: AssetSetErrorEnum.AssetSetError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: AssetSetErrorEnum.AssetSetError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        DUPLICATE_ASSET_SET_NAME: AssetSetErrorEnum.AssetSetError.ValueType = ...  # 2
        """The asset set name matches that of another enabled asset set."""

    class AssetSetError(_AssetSetError, metaclass=_AssetSetErrorEnumTypeWrapper):
        """Enum describing possible asset set errors."""
        pass

    UNSPECIFIED: AssetSetErrorEnum.AssetSetError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: AssetSetErrorEnum.AssetSetError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    DUPLICATE_ASSET_SET_NAME: AssetSetErrorEnum.AssetSetError.ValueType = ...  # 2
    """The asset set name matches that of another enabled asset set."""


    def __init__(self,
        ) -> None: ...
global___AssetSetErrorEnum = AssetSetErrorEnum
