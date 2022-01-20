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

class GoogleVoiceCallStatusEnum(google.protobuf.message.Message):
    """Proto file describing google voice call status.

    Container for enum describing possible statuses of a google voice call.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _GoogleVoiceCallStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _GoogleVoiceCallStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_GoogleVoiceCallStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        MISSED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus.ValueType = ...  # 2
        """The call was missed."""

        RECEIVED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus.ValueType = ...  # 3
        """The call was received."""

    class GoogleVoiceCallStatus(_GoogleVoiceCallStatus, metaclass=_GoogleVoiceCallStatusEnumTypeWrapper):
        """Possible statuses of a google voice call."""
        pass

    UNSPECIFIED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    MISSED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus.ValueType = ...  # 2
    """The call was missed."""

    RECEIVED: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus.ValueType = ...  # 3
    """The call was received."""


    def __init__(self,
        ) -> None: ...
global___GoogleVoiceCallStatusEnum = GoogleVoiceCallStatusEnum
