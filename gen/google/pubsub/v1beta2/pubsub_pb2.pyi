"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Topic(google.protobuf.message.Message):
    """A topic resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the topic."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___Topic = Topic

class PubsubMessage(google.protobuf.message.Message):
    """A message data and its attributes."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class AttributesEntry(google.protobuf.message.Message):
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

    DATA_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    MESSAGE_ID_FIELD_NUMBER: builtins.int
    data: builtins.bytes = ...
    """The message payload. For JSON requests, the value of this field must be
    base64-encoded.
    """

    @property
    def attributes(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Optional attributes for this message."""
        pass
    message_id: typing.Text = ...
    """ID of this message assigned by the server at publication time. Guaranteed
    to be unique within the topic. This value may be read by a subscriber
    that receives a PubsubMessage via a Pull call or a push delivery. It must
    not be populated by a publisher in a Publish call.
    """

    def __init__(self,
        *,
        data : builtins.bytes = ...,
        attributes : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        message_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attributes",b"attributes","data",b"data","message_id",b"message_id"]) -> None: ...
global___PubsubMessage = PubsubMessage

class GetTopicRequest(google.protobuf.message.Message):
    """Request for the GetTopic method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOPIC_FIELD_NUMBER: builtins.int
    topic: typing.Text = ...
    """The name of the topic to get."""

    def __init__(self,
        *,
        topic : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["topic",b"topic"]) -> None: ...
global___GetTopicRequest = GetTopicRequest

class PublishRequest(google.protobuf.message.Message):
    """Request for the Publish method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOPIC_FIELD_NUMBER: builtins.int
    MESSAGES_FIELD_NUMBER: builtins.int
    topic: typing.Text = ...
    """The messages in the request will be published on this topic."""

    @property
    def messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PubsubMessage]:
        """The messages to publish."""
        pass
    def __init__(self,
        *,
        topic : typing.Text = ...,
        messages : typing.Optional[typing.Iterable[global___PubsubMessage]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["messages",b"messages","topic",b"topic"]) -> None: ...
global___PublishRequest = PublishRequest

class PublishResponse(google.protobuf.message.Message):
    """Response for the Publish method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MESSAGE_IDS_FIELD_NUMBER: builtins.int
    @property
    def message_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The server-assigned ID of each published message, in the same order as
        the messages in the request. IDs are guaranteed to be unique within
        the topic.
        """
        pass
    def __init__(self,
        *,
        message_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message_ids",b"message_ids"]) -> None: ...
global___PublishResponse = PublishResponse

class ListTopicsRequest(google.protobuf.message.Message):
    """Request for the ListTopics method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    project: typing.Text = ...
    """The name of the cloud project that topics belong to."""

    page_size: builtins.int = ...
    """Maximum number of topics to return."""

    page_token: typing.Text = ...
    """The value returned by the last ListTopicsResponse; indicates that this is
    a continuation of a prior ListTopics call, and that the system should
    return the next page of data.
    """

    def __init__(self,
        *,
        project : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","project",b"project"]) -> None: ...
global___ListTopicsRequest = ListTopicsRequest

class ListTopicsResponse(google.protobuf.message.Message):
    """Response for the ListTopics method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOPICS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def topics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Topic]:
        """The resulting topics."""
        pass
    next_page_token: typing.Text = ...
    """If not empty, indicates that there may be more topics that match the
    request; this value should be passed in a new ListTopicsRequest.
    """

    def __init__(self,
        *,
        topics : typing.Optional[typing.Iterable[global___Topic]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","topics",b"topics"]) -> None: ...
global___ListTopicsResponse = ListTopicsResponse

class ListTopicSubscriptionsRequest(google.protobuf.message.Message):
    """Request for the ListTopicSubscriptions method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOPIC_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    topic: typing.Text = ...
    """The name of the topic that subscriptions are attached to."""

    page_size: builtins.int = ...
    """Maximum number of subscription names to return."""

    page_token: typing.Text = ...
    """The value returned by the last ListTopicSubscriptionsResponse; indicates
    that this is a continuation of a prior ListTopicSubscriptions call, and
    that the system should return the next page of data.
    """

    def __init__(self,
        *,
        topic : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","topic",b"topic"]) -> None: ...
global___ListTopicSubscriptionsRequest = ListTopicSubscriptionsRequest

class ListTopicSubscriptionsResponse(google.protobuf.message.Message):
    """Response for the ListTopicSubscriptions method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSCRIPTIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def subscriptions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The names of the subscriptions that match the request."""
        pass
    next_page_token: typing.Text = ...
    """If not empty, indicates that there may be more subscriptions that match
    the request; this value should be passed in a new
    ListTopicSubscriptionsRequest to get more subscriptions.
    """

    def __init__(self,
        *,
        subscriptions : typing.Optional[typing.Iterable[typing.Text]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","subscriptions",b"subscriptions"]) -> None: ...
global___ListTopicSubscriptionsResponse = ListTopicSubscriptionsResponse

class DeleteTopicRequest(google.protobuf.message.Message):
    """Request for the DeleteTopic method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOPIC_FIELD_NUMBER: builtins.int
    topic: typing.Text = ...
    """Name of the topic to delete."""

    def __init__(self,
        *,
        topic : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["topic",b"topic"]) -> None: ...
global___DeleteTopicRequest = DeleteTopicRequest

class Subscription(google.protobuf.message.Message):
    """A subscription resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TOPIC_FIELD_NUMBER: builtins.int
    PUSH_CONFIG_FIELD_NUMBER: builtins.int
    ACK_DEADLINE_SECONDS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the subscription."""

    topic: typing.Text = ...
    """The name of the topic from which this subscription is receiving messages.
    This will be present if and only if the subscription has not been detached
    from its topic.
    """

    @property
    def push_config(self) -> global___PushConfig:
        """If push delivery is used with this subscription, this field is
        used to configure it. An empty pushConfig signifies that the subscriber
        will pull and ack messages using API methods.
        """
        pass
    ack_deadline_seconds: builtins.int = ...
    """This value is the maximum time after a subscriber receives a message
    before the subscriber should acknowledge the message. After message
    delivery but before the ack deadline expires and before the message is
    acknowledged, it is an outstanding message and will not be delivered
    again during that time (on a best-effort basis).

    For pull delivery this value
    is used as the initial value for the ack deadline. It may be overridden
    for a specific message by calling ModifyAckDeadline.

    For push delivery, this value is also used to set the request timeout for
    the call to the push endpoint.

    If the subscriber never acknowledges the message, the Pub/Sub
    system will eventually redeliver the message.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        topic : typing.Text = ...,
        push_config : typing.Optional[global___PushConfig] = ...,
        ack_deadline_seconds : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["push_config",b"push_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ack_deadline_seconds",b"ack_deadline_seconds","name",b"name","push_config",b"push_config","topic",b"topic"]) -> None: ...
global___Subscription = Subscription

class PushConfig(google.protobuf.message.Message):
    """Configuration for a push delivery endpoint."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class AttributesEntry(google.protobuf.message.Message):
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

    PUSH_ENDPOINT_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    push_endpoint: typing.Text = ...
    """A URL locating the endpoint to which messages should be pushed.
    For example, a Webhook endpoint might use "https://example.com/push".
    """

    @property
    def attributes(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Endpoint configuration attributes.

        Every endpoint has a set of API supported attributes that can be used to
        control different aspects of the message delivery.

        The currently supported attribute is `x-goog-version`, which you can
        use to change the format of the push message. This attribute
        indicates the version of the data expected by the endpoint. This
        controls the shape of the envelope (i.e. its fields and metadata).
        The endpoint version is based on the version of the Pub/Sub
        API.

        If not present during the CreateSubscription call, it will default to
        the version of the API used to make such call. If not present during a
        ModifyPushConfig call, its value will not be changed. GetSubscription
        calls will always return a valid version, even if the subscription was
        created without this attribute.

        The possible values for this attribute are:

        * `v1beta1`: uses the push format defined in the v1beta1 Pub/Sub API.
        * `v1beta2`: uses the push format defined in the v1beta2 Pub/Sub API.
        """
        pass
    def __init__(self,
        *,
        push_endpoint : typing.Text = ...,
        attributes : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attributes",b"attributes","push_endpoint",b"push_endpoint"]) -> None: ...
global___PushConfig = PushConfig

class ReceivedMessage(google.protobuf.message.Message):
    """A message and its corresponding acknowledgment ID."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ACK_ID_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    ack_id: typing.Text = ...
    """This ID can be used to acknowledge the received message."""

    @property
    def message(self) -> global___PubsubMessage:
        """The message."""
        pass
    def __init__(self,
        *,
        ack_id : typing.Text = ...,
        message : typing.Optional[global___PubsubMessage] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message",b"message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ack_id",b"ack_id","message",b"message"]) -> None: ...
global___ReceivedMessage = ReceivedMessage

class GetSubscriptionRequest(google.protobuf.message.Message):
    """Request for the GetSubscription method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    subscription: typing.Text = ...
    """The name of the subscription to get."""

    def __init__(self,
        *,
        subscription : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subscription",b"subscription"]) -> None: ...
global___GetSubscriptionRequest = GetSubscriptionRequest

class ListSubscriptionsRequest(google.protobuf.message.Message):
    """Request for the ListSubscriptions method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    project: typing.Text = ...
    """The name of the cloud project that subscriptions belong to."""

    page_size: builtins.int = ...
    """Maximum number of subscriptions to return."""

    page_token: typing.Text = ...
    """The value returned by the last ListSubscriptionsResponse; indicates that
    this is a continuation of a prior ListSubscriptions call, and that the
    system should return the next page of data.
    """

    def __init__(self,
        *,
        project : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","project",b"project"]) -> None: ...
global___ListSubscriptionsRequest = ListSubscriptionsRequest

class ListSubscriptionsResponse(google.protobuf.message.Message):
    """Response for the ListSubscriptions method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSCRIPTIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def subscriptions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Subscription]:
        """The subscriptions that match the request."""
        pass
    next_page_token: typing.Text = ...
    """If not empty, indicates that there may be more subscriptions that match
    the request; this value should be passed in a new ListSubscriptionsRequest
    to get more subscriptions.
    """

    def __init__(self,
        *,
        subscriptions : typing.Optional[typing.Iterable[global___Subscription]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","subscriptions",b"subscriptions"]) -> None: ...
global___ListSubscriptionsResponse = ListSubscriptionsResponse

class DeleteSubscriptionRequest(google.protobuf.message.Message):
    """Request for the DeleteSubscription method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    subscription: typing.Text = ...
    """The subscription to delete."""

    def __init__(self,
        *,
        subscription : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subscription",b"subscription"]) -> None: ...
global___DeleteSubscriptionRequest = DeleteSubscriptionRequest

class ModifyPushConfigRequest(google.protobuf.message.Message):
    """Request for the ModifyPushConfig method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    PUSH_CONFIG_FIELD_NUMBER: builtins.int
    subscription: typing.Text = ...
    """The name of the subscription."""

    @property
    def push_config(self) -> global___PushConfig:
        """The push configuration for future deliveries.

        An empty pushConfig indicates that the Pub/Sub system should
        stop pushing messages from the given subscription and allow
        messages to be pulled and acknowledged - effectively pausing
        the subscription if Pull is not called.
        """
        pass
    def __init__(self,
        *,
        subscription : typing.Text = ...,
        push_config : typing.Optional[global___PushConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["push_config",b"push_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["push_config",b"push_config","subscription",b"subscription"]) -> None: ...
global___ModifyPushConfigRequest = ModifyPushConfigRequest

class PullRequest(google.protobuf.message.Message):
    """Request for the Pull method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    RETURN_IMMEDIATELY_FIELD_NUMBER: builtins.int
    MAX_MESSAGES_FIELD_NUMBER: builtins.int
    subscription: typing.Text = ...
    """The subscription from which messages should be pulled."""

    return_immediately: builtins.bool = ...
    """If this is specified as true the system will respond immediately even if
    it is not able to return a message in the Pull response. Otherwise the
    system is allowed to wait until at least one message is available rather
    than returning no messages. The client may cancel the request if it does
    not wish to wait any longer for the response.
    """

    max_messages: builtins.int = ...
    """The maximum number of messages returned for this request. The Pub/Sub
    system may return fewer than the number specified.
    """

    def __init__(self,
        *,
        subscription : typing.Text = ...,
        return_immediately : builtins.bool = ...,
        max_messages : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_messages",b"max_messages","return_immediately",b"return_immediately","subscription",b"subscription"]) -> None: ...
global___PullRequest = PullRequest

class PullResponse(google.protobuf.message.Message):
    """Response for the Pull method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RECEIVED_MESSAGES_FIELD_NUMBER: builtins.int
    @property
    def received_messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ReceivedMessage]:
        """Received Pub/Sub messages. The Pub/Sub system will return zero messages if
        there are no more available in the backlog. The Pub/Sub system may return
        fewer than the maxMessages requested even if there are more messages
        available in the backlog.
        """
        pass
    def __init__(self,
        *,
        received_messages : typing.Optional[typing.Iterable[global___ReceivedMessage]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["received_messages",b"received_messages"]) -> None: ...
global___PullResponse = PullResponse

class ModifyAckDeadlineRequest(google.protobuf.message.Message):
    """Request for the ModifyAckDeadline method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    ACK_ID_FIELD_NUMBER: builtins.int
    ACK_DEADLINE_SECONDS_FIELD_NUMBER: builtins.int
    subscription: typing.Text = ...
    """The name of the subscription."""

    ack_id: typing.Text = ...
    """The acknowledgment ID."""

    ack_deadline_seconds: builtins.int = ...
    """The new ack deadline with respect to the time this request was sent to the
    Pub/Sub system. Must be >= 0. For example, if the value is 10, the new ack
    deadline will expire 10 seconds after the ModifyAckDeadline call was made.
    Specifying zero may immediately make the message available for another pull
    request.
    """

    def __init__(self,
        *,
        subscription : typing.Text = ...,
        ack_id : typing.Text = ...,
        ack_deadline_seconds : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ack_deadline_seconds",b"ack_deadline_seconds","ack_id",b"ack_id","subscription",b"subscription"]) -> None: ...
global___ModifyAckDeadlineRequest = ModifyAckDeadlineRequest

class AcknowledgeRequest(google.protobuf.message.Message):
    """Request for the Acknowledge method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    ACK_IDS_FIELD_NUMBER: builtins.int
    subscription: typing.Text = ...
    """The subscription whose message is being acknowledged."""

    @property
    def ack_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The acknowledgment ID for the messages being acknowledged that was returned
        by the Pub/Sub system in the Pull response. Must not be empty.
        """
        pass
    def __init__(self,
        *,
        subscription : typing.Text = ...,
        ack_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ack_ids",b"ack_ids","subscription",b"subscription"]) -> None: ...
global___AcknowledgeRequest = AcknowledgeRequest
