"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.dialogflow.v2.participant_pb2
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ConversationEvent(google.protobuf.message.Message):
    """Represents a notification sent to Pub/Sub subscribers for conversation
    lifecycle events.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TYPE_UNSPECIFIED: ConversationEvent.Type.ValueType = ...  # 0
        """Type not set."""

        CONVERSATION_STARTED: ConversationEvent.Type.ValueType = ...  # 1
        """A new conversation has been opened. This is fired when a telephone call
        is answered, or a conversation is created via the API.
        """

        CONVERSATION_FINISHED: ConversationEvent.Type.ValueType = ...  # 2
        """An existing conversation has closed. This is fired when a telephone call
        is terminated, or a conversation is closed via the API.
        """

        HUMAN_INTERVENTION_NEEDED: ConversationEvent.Type.ValueType = ...  # 3
        """An existing conversation has received notification from Dialogflow that
        human intervention is required.
        """

        NEW_MESSAGE: ConversationEvent.Type.ValueType = ...  # 5
        """An existing conversation has received a new message, either from API or
        telephony. It is configured in
        [ConversationProfile.new_message_event_notification_config][google.cloud.dialogflow.v2.ConversationProfile.new_message_event_notification_config]
        """

        UNRECOVERABLE_ERROR: ConversationEvent.Type.ValueType = ...  # 4
        """Unrecoverable error during a telephone call.

        In general non-recoverable errors only occur if something was
        misconfigured in the ConversationProfile corresponding to the call. After
        a non-recoverable error, Dialogflow may stop responding.

        We don't fire this event:

        * in an API call because we can directly return the error, or,
        * when we can recover from an error.
        """

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """Enumeration of the types of events available."""
        pass

    TYPE_UNSPECIFIED: ConversationEvent.Type.ValueType = ...  # 0
    """Type not set."""

    CONVERSATION_STARTED: ConversationEvent.Type.ValueType = ...  # 1
    """A new conversation has been opened. This is fired when a telephone call
    is answered, or a conversation is created via the API.
    """

    CONVERSATION_FINISHED: ConversationEvent.Type.ValueType = ...  # 2
    """An existing conversation has closed. This is fired when a telephone call
    is terminated, or a conversation is closed via the API.
    """

    HUMAN_INTERVENTION_NEEDED: ConversationEvent.Type.ValueType = ...  # 3
    """An existing conversation has received notification from Dialogflow that
    human intervention is required.
    """

    NEW_MESSAGE: ConversationEvent.Type.ValueType = ...  # 5
    """An existing conversation has received a new message, either from API or
    telephony. It is configured in
    [ConversationProfile.new_message_event_notification_config][google.cloud.dialogflow.v2.ConversationProfile.new_message_event_notification_config]
    """

    UNRECOVERABLE_ERROR: ConversationEvent.Type.ValueType = ...  # 4
    """Unrecoverable error during a telephone call.

    In general non-recoverable errors only occur if something was
    misconfigured in the ConversationProfile corresponding to the call. After
    a non-recoverable error, Dialogflow may stop responding.

    We don't fire this event:

    * in an API call because we can directly return the error, or,
    * when we can recover from an error.
    """


    CONVERSATION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ERROR_STATUS_FIELD_NUMBER: builtins.int
    NEW_MESSAGE_PAYLOAD_FIELD_NUMBER: builtins.int
    conversation: typing.Text = ...
    """The unique identifier of the conversation this notification
    refers to.
    Format: `projects/<Project ID>/conversations/<Conversation ID>`.
    """

    type: global___ConversationEvent.Type.ValueType = ...
    """The type of the event that this notification refers to."""

    @property
    def error_status(self) -> google.rpc.status_pb2.Status:
        """More detailed information about an error. Only set for type
        UNRECOVERABLE_ERROR_IN_PHONE_CALL.
        """
        pass
    @property
    def new_message_payload(self) -> google.cloud.dialogflow.v2.participant_pb2.Message:
        """Payload of NEW_MESSAGE event."""
        pass
    def __init__(self,
        *,
        conversation : typing.Text = ...,
        type : global___ConversationEvent.Type.ValueType = ...,
        error_status : typing.Optional[google.rpc.status_pb2.Status] = ...,
        new_message_payload : typing.Optional[google.cloud.dialogflow.v2.participant_pb2.Message] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error_status",b"error_status","new_message_payload",b"new_message_payload","payload",b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["conversation",b"conversation","error_status",b"error_status","new_message_payload",b"new_message_payload","payload",b"payload","type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["payload",b"payload"]) -> typing.Optional[typing_extensions.Literal["new_message_payload"]]: ...
global___ConversationEvent = ConversationEvent
