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

class CallTrackingDisplayLocationEnum(google.protobuf.message.Message):
    """Proto file describing call tracking display location.

    Container for enum describing possible call tracking display locations.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CallTrackingDisplayLocation:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CallTrackingDisplayLocationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CallTrackingDisplayLocation.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        AD: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation.ValueType = ...  # 2
        """The phone call placed from the ad."""

        LANDING_PAGE: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation.ValueType = ...  # 3
        """The phone call placed from the landing page ad points to."""

    class CallTrackingDisplayLocation(_CallTrackingDisplayLocation, metaclass=_CallTrackingDisplayLocationEnumTypeWrapper):
        """Possible call tracking display locations."""
        pass

    UNSPECIFIED: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    AD: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation.ValueType = ...  # 2
    """The phone call placed from the ad."""

    LANDING_PAGE: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation.ValueType = ...  # 3
    """The phone call placed from the landing page ad points to."""


    def __init__(self,
        ) -> None: ...
global___CallTrackingDisplayLocationEnum = CallTrackingDisplayLocationEnum
