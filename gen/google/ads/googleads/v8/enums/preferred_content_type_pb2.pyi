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

class PreferredContentTypeEnum(google.protobuf.message.Message):
    """Proto file describing preferred content criterion type.

    Container for enumeration of preferred content criterion type.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _PreferredContentType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _PreferredContentTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PreferredContentType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: PreferredContentTypeEnum.PreferredContentType.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: PreferredContentTypeEnum.PreferredContentType.ValueType = ...  # 1
        """The value is unknown in this version."""

        YOUTUBE_TOP_CONTENT: PreferredContentTypeEnum.PreferredContentType.ValueType = ...  # 400
        """Represents top content on YouTube."""

    class PreferredContentType(_PreferredContentType, metaclass=_PreferredContentTypeEnumTypeWrapper):
        """Enumerates preferred content criterion type."""
        pass

    UNSPECIFIED: PreferredContentTypeEnum.PreferredContentType.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: PreferredContentTypeEnum.PreferredContentType.ValueType = ...  # 1
    """The value is unknown in this version."""

    YOUTUBE_TOP_CONTENT: PreferredContentTypeEnum.PreferredContentType.ValueType = ...  # 400
    """Represents top content on YouTube."""


    def __init__(self,
        ) -> None: ...
global___PreferredContentTypeEnum = PreferredContentTypeEnum
