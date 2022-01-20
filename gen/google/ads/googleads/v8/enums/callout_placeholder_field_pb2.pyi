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

class CalloutPlaceholderFieldEnum(google.protobuf.message.Message):
    """Proto file describing Callout placeholder fields.

    Values for Callout placeholder fields.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CalloutPlaceholderField:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CalloutPlaceholderFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CalloutPlaceholderField.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: CalloutPlaceholderFieldEnum.CalloutPlaceholderField.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: CalloutPlaceholderFieldEnum.CalloutPlaceholderField.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        CALLOUT_TEXT: CalloutPlaceholderFieldEnum.CalloutPlaceholderField.ValueType = ...  # 2
        """Data Type: STRING. Callout text."""

    class CalloutPlaceholderField(_CalloutPlaceholderField, metaclass=_CalloutPlaceholderFieldEnumTypeWrapper):
        """Possible values for Callout placeholder fields."""
        pass

    UNSPECIFIED: CalloutPlaceholderFieldEnum.CalloutPlaceholderField.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: CalloutPlaceholderFieldEnum.CalloutPlaceholderField.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    CALLOUT_TEXT: CalloutPlaceholderFieldEnum.CalloutPlaceholderField.ValueType = ...  # 2
    """Data Type: STRING. Callout text."""


    def __init__(self,
        ) -> None: ...
global___CalloutPlaceholderFieldEnum = CalloutPlaceholderFieldEnum
