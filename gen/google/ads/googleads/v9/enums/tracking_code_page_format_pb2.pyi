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

class TrackingCodePageFormatEnum(google.protobuf.message.Message):
    """Container for enum describing the format of the web page where the tracking
    tag and snippet will be installed.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _TrackingCodePageFormat:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TrackingCodePageFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TrackingCodePageFormat.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: TrackingCodePageFormatEnum.TrackingCodePageFormat.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: TrackingCodePageFormatEnum.TrackingCodePageFormat.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        HTML: TrackingCodePageFormatEnum.TrackingCodePageFormat.ValueType = ...  # 2
        """Standard HTML page format."""

        AMP: TrackingCodePageFormatEnum.TrackingCodePageFormat.ValueType = ...  # 3
        """Google AMP page format."""

    class TrackingCodePageFormat(_TrackingCodePageFormat, metaclass=_TrackingCodePageFormatEnumTypeWrapper):
        """The format of the web page where the tracking tag and snippet will be
        installed.
        """
        pass

    UNSPECIFIED: TrackingCodePageFormatEnum.TrackingCodePageFormat.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: TrackingCodePageFormatEnum.TrackingCodePageFormat.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    HTML: TrackingCodePageFormatEnum.TrackingCodePageFormat.ValueType = ...  # 2
    """Standard HTML page format."""

    AMP: TrackingCodePageFormatEnum.TrackingCodePageFormat.ValueType = ...  # 3
    """Google AMP page format."""


    def __init__(self,
        ) -> None: ...
global___TrackingCodePageFormatEnum = TrackingCodePageFormatEnum
