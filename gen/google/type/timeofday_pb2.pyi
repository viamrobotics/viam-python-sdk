"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TimeOfDay(google.protobuf.message.Message):
    """Represents a time of day. The date and time zone are either not significant
    or are specified elsewhere. An API may choose to allow leap seconds. Related
    types are [google.type.Date][google.type.Date] and
    `google.protobuf.Timestamp`.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HOURS_FIELD_NUMBER: builtins.int
    MINUTES_FIELD_NUMBER: builtins.int
    SECONDS_FIELD_NUMBER: builtins.int
    NANOS_FIELD_NUMBER: builtins.int
    hours: builtins.int = ...
    """Hours of day in 24 hour format. Should be from 0 to 23. An API may choose
    to allow the value "24:00:00" for scenarios like business closing time.
    """

    minutes: builtins.int = ...
    """Minutes of hour of day. Must be from 0 to 59."""

    seconds: builtins.int = ...
    """Seconds of minutes of the time. Must normally be from 0 to 59. An API may
    allow the value 60 if it allows leap-seconds.
    """

    nanos: builtins.int = ...
    """Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999."""

    def __init__(self,
        *,
        hours : builtins.int = ...,
        minutes : builtins.int = ...,
        seconds : builtins.int = ...,
        nanos : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hours",b"hours","minutes",b"minutes","nanos",b"nanos","seconds",b"seconds"]) -> None: ...
global___TimeOfDay = TimeOfDay
