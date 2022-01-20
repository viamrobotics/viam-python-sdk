"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Event(google.protobuf.message.Message):
    """An edge describing the relationship between an Artifact and an Execution in
    a lineage graph.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TYPE_UNSPECIFIED: Event.Type.ValueType = ...  # 0
        """Unspecified whether input or output of the Execution."""

        INPUT: Event.Type.ValueType = ...  # 1
        """An input of the Execution."""

        OUTPUT: Event.Type.ValueType = ...  # 2
        """An output of the Execution."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """Describes whether an Event's Artifact is the Execution's input or output."""
        pass

    TYPE_UNSPECIFIED: Event.Type.ValueType = ...  # 0
    """Unspecified whether input or output of the Execution."""

    INPUT: Event.Type.ValueType = ...  # 1
    """An input of the Execution."""

    OUTPUT: Event.Type.ValueType = ...  # 2
    """An output of the Execution."""


    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ARTIFACT_FIELD_NUMBER: builtins.int
    EXECUTION_FIELD_NUMBER: builtins.int
    EVENT_TIME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    artifact: typing.Text = ...
    """Required. The relative resource name of the Artifact in the Event."""

    execution: typing.Text = ...
    """Output only. The relative resource name of the Execution in the Event."""

    @property
    def event_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Time the Event occurred."""
        pass
    type: global___Event.Type.ValueType = ...
    """Required. The type of the Event."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """The labels with user-defined metadata to annotate Events.

        Label keys and values can be no longer than 64 characters
        (Unicode codepoints), can only contain lowercase letters, numeric
        characters, underscores and dashes. International characters are allowed.
        No more than 64 user labels can be associated with one Event (System
        labels are excluded).

        See https://goo.gl/xmQnxf for more information and examples of labels.
        System reserved label keys are prefixed with "aiplatform.googleapis.com/"
        and are immutable.
        """
        pass
    def __init__(self,
        *,
        artifact : typing.Text = ...,
        execution : typing.Text = ...,
        event_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        type : global___Event.Type.ValueType = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["event_time",b"event_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["artifact",b"artifact","event_time",b"event_time","execution",b"execution","labels",b"labels","type",b"type"]) -> None: ...
global___Event = Event
