"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.frequency_cap_event_type_pb2
import google.ads.googleads.v8.enums.frequency_cap_level_pb2
import google.ads.googleads.v8.enums.frequency_cap_time_unit_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FrequencyCapEntry(google.protobuf.message.Message):
    """Proto file describing frequency caps.

    A rule specifying the maximum number of times an ad (or some set of ads) can
    be shown to a user over a particular time period.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    CAP_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___FrequencyCapKey:
        """The key of a particular frequency cap. There can be no more
        than one frequency cap with the same key.
        """
        pass
    cap: builtins.int = ...
    """Maximum number of events allowed during the time range by this cap."""

    def __init__(self,
        *,
        key : typing.Optional[global___FrequencyCapKey] = ...,
        cap : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_cap",b"_cap","cap",b"cap","key",b"key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_cap",b"_cap","cap",b"cap","key",b"key"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_cap",b"_cap"]) -> typing.Optional[typing_extensions.Literal["cap"]]: ...
global___FrequencyCapEntry = FrequencyCapEntry

class FrequencyCapKey(google.protobuf.message.Message):
    """A group of fields used as keys for a frequency cap.
    There can be no more than one frequency cap with the same key.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LEVEL_FIELD_NUMBER: builtins.int
    EVENT_TYPE_FIELD_NUMBER: builtins.int
    TIME_UNIT_FIELD_NUMBER: builtins.int
    TIME_LENGTH_FIELD_NUMBER: builtins.int
    level: google.ads.googleads.v8.enums.frequency_cap_level_pb2.FrequencyCapLevelEnum.FrequencyCapLevel.ValueType = ...
    """The level on which the cap is to be applied (e.g. ad group ad, ad group).
    The cap is applied to all the entities of this level.
    """

    event_type: google.ads.googleads.v8.enums.frequency_cap_event_type_pb2.FrequencyCapEventTypeEnum.FrequencyCapEventType.ValueType = ...
    """The type of event that the cap applies to (e.g. impression)."""

    time_unit: google.ads.googleads.v8.enums.frequency_cap_time_unit_pb2.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...
    """Unit of time the cap is defined at (e.g. day, week)."""

    time_length: builtins.int = ...
    """Number of time units the cap lasts."""

    def __init__(self,
        *,
        level : google.ads.googleads.v8.enums.frequency_cap_level_pb2.FrequencyCapLevelEnum.FrequencyCapLevel.ValueType = ...,
        event_type : google.ads.googleads.v8.enums.frequency_cap_event_type_pb2.FrequencyCapEventTypeEnum.FrequencyCapEventType.ValueType = ...,
        time_unit : google.ads.googleads.v8.enums.frequency_cap_time_unit_pb2.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit.ValueType = ...,
        time_length : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_time_length",b"_time_length","time_length",b"time_length"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_time_length",b"_time_length","event_type",b"event_type","level",b"level","time_length",b"time_length","time_unit",b"time_unit"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_time_length",b"_time_length"]) -> typing.Optional[typing_extensions.Literal["time_length"]]: ...
global___FrequencyCapKey = FrequencyCapKey
