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

class AssetSetAssetErrorEnum(google.protobuf.message.Message):
    """Proto file describing asset set asset errors.

    Container for enum describing possible asset set asset errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AssetSetAssetError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AssetSetAssetErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AssetSetAssetError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        INVALID_ASSET_TYPE: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 2
        """The asset type is not eligible to be linked to the specific type of asset
        set.
        """

        INVALID_ASSET_SET_TYPE: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 3
        """The asset set type is not eligible to contain the specified type of
        assets.
        """

        DUPLICATE_EXTERNAL_KEY: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 4
        """The asset contains duplicate external key with another asset in the asset
        set.
        """

    class AssetSetAssetError(_AssetSetAssetError, metaclass=_AssetSetAssetErrorEnumTypeWrapper):
        """Enum describing possible asset set asset errors."""
        pass

    UNSPECIFIED: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    INVALID_ASSET_TYPE: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 2
    """The asset type is not eligible to be linked to the specific type of asset
    set.
    """

    INVALID_ASSET_SET_TYPE: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 3
    """The asset set type is not eligible to contain the specified type of
    assets.
    """

    DUPLICATE_EXTERNAL_KEY: AssetSetAssetErrorEnum.AssetSetAssetError.ValueType = ...  # 4
    """The asset contains duplicate external key with another asset in the asset
    set.
    """


    def __init__(self,
        ) -> None: ...
global___AssetSetAssetErrorEnum = AssetSetAssetErrorEnum
