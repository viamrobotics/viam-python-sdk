"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _AlertFeedbackType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _AlertFeedbackTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AlertFeedbackType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ALERT_FEEDBACK_TYPE_UNSPECIFIED: AlertFeedbackType.ValueType = ...  # 0
    """The feedback type is not specified."""

    NOT_USEFUL: AlertFeedbackType.ValueType = ...  # 1
    """The alert report is not useful."""

    SOMEWHAT_USEFUL: AlertFeedbackType.ValueType = ...  # 2
    """The alert report is somewhat useful."""

    VERY_USEFUL: AlertFeedbackType.ValueType = ...  # 3
    """The alert report is very useful."""

class AlertFeedbackType(_AlertFeedbackType, metaclass=_AlertFeedbackTypeEnumTypeWrapper):
    """The type of alert feedback."""
    pass

ALERT_FEEDBACK_TYPE_UNSPECIFIED: AlertFeedbackType.ValueType = ...  # 0
"""The feedback type is not specified."""

NOT_USEFUL: AlertFeedbackType.ValueType = ...  # 1
"""The alert report is not useful."""

SOMEWHAT_USEFUL: AlertFeedbackType.ValueType = ...  # 2
"""The alert report is somewhat useful."""

VERY_USEFUL: AlertFeedbackType.ValueType = ...  # 3
"""The alert report is very useful."""

global___AlertFeedbackType = AlertFeedbackType


class Alert(google.protobuf.message.Message):
    """An alert affecting a customer."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    SECURITY_INVESTIGATION_TOOL_LINK_FIELD_NUMBER: builtins.int
    DELETED_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Output only. The unique identifier of the Google account of the customer."""

    alert_id: typing.Text = ...
    """Output only. The unique identifier for the alert."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time this alert was created."""
        pass
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Required. The time the event that caused this alert was started or
        detected.
        """
        pass
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Optional. The time the event that caused this alert ceased being active.
        If provided, the end time must not be earlier than the start time.
        If not provided, it indicates an ongoing alert.
        """
        pass
    type: typing.Text = ...
    """Required. The type of the alert.
    This is output only after alert is created.
    For a list of available alert types see
    [Google Workspace Alert
    types](https://developers.google.com/admin-sdk/alertcenter/reference/alert-types).
    """

    source: typing.Text = ...
    """Required. A unique identifier for the system that reported the alert.
    This is output only after alert is created.

    Supported sources are any of the following:

    * Google Operations
    * Mobile device management
    * Gmail phishing
    * Domain wide takeout
    * State sponsored attack
    * Google identity
    """

    @property
    def data(self) -> google.protobuf.any_pb2.Any:
        """Optional. The data associated with this alert, for example
        [google.apps.alertcenter.type.DeviceCompromised] [google.apps.alertcenter.type.DeviceCompromised].
        """
        pass
    security_investigation_tool_link: typing.Text = ...
    """Output only. An optional
    [Security Investigation Tool](https://support.google.com/a/answer/7575955)
    query for this alert.
    """

    deleted: builtins.bool = ...
    """Output only. `True` if this alert is marked for deletion."""

    @property
    def metadata(self) -> global___AlertMetadata:
        """Output only. The metadata associated with this alert."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time this alert was last updated."""
        pass
    etag: typing.Text = ...
    """Optional. `etag` is used for optimistic concurrency control as a way to help
    prevent simultaneous updates of an alert from overwriting each other.
    It is strongly suggested that systems make use of the `etag` in the
    read-modify-write cycle to perform alert updates in order to avoid race
    conditions: An `etag` is returned in the response which contains alerts,
    and systems are expected to put that etag in the request to update alert to
    ensure that their change will be applied to the same version of the alert.

    If no `etag` is provided in the call to update alert, then the existing
    alert is overwritten blindly.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        start_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        type : typing.Text = ...,
        source : typing.Text = ...,
        data : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        security_investigation_tool_link : typing.Text = ...,
        deleted : builtins.bool = ...,
        metadata : typing.Optional[global___AlertMetadata] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        etag : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","data",b"data","end_time",b"end_time","metadata",b"metadata","start_time",b"start_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","create_time",b"create_time","customer_id",b"customer_id","data",b"data","deleted",b"deleted","end_time",b"end_time","etag",b"etag","metadata",b"metadata","security_investigation_tool_link",b"security_investigation_tool_link","source",b"source","start_time",b"start_time","type",b"type","update_time",b"update_time"]) -> None: ...
global___Alert = Alert

class AlertFeedback(google.protobuf.message.Message):
    """A customer feedback about an alert."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    FEEDBACK_ID_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Output only. The unique identifier of the Google account of the customer."""

    alert_id: typing.Text = ...
    """Output only. The alert identifier."""

    feedback_id: typing.Text = ...
    """Output only. The unique identifier for the feedback."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time this feedback was created."""
        pass
    type: global___AlertFeedbackType.ValueType = ...
    """Required. The type of the feedback."""

    email: typing.Text = ...
    """Output only. The email of the user that provided the feedback."""

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        feedback_id : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        type : global___AlertFeedbackType.ValueType = ...,
        email : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","create_time",b"create_time","customer_id",b"customer_id","email",b"email","feedback_id",b"feedback_id","type",b"type"]) -> None: ...
global___AlertFeedback = AlertFeedback

class AlertMetadata(google.protobuf.message.Message):
    """An alert metadata."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ASSIGNEE_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    SEVERITY_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Output only. The unique identifier of the Google account of the customer."""

    alert_id: typing.Text = ...
    """Output only. The alert identifier."""

    status: typing.Text = ...
    """The current status of the alert.
    The supported values are the following:

    * NOT_STARTED
    * IN_PROGRESS
    * CLOSED
    """

    assignee: typing.Text = ...
    """The email address of the user assigned to the alert."""

    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time this metadata was last updated."""
        pass
    severity: typing.Text = ...
    """The severity value of the alert. Alert Center will set this field at alert
    creation time, default's to an empty string when it could not be
    determined.
    The supported values for update actions on this field are the following:

    * HIGH
    * MEDIUM
    * LOW
    """

    etag: typing.Text = ...
    """Optional. `etag` is used for optimistic concurrency control as a way to
    help prevent simultaneous updates of an alert metadata from overwriting
    each other. It is strongly suggested that systems make use of the `etag` in
    the read-modify-write cycle to perform metatdata updates in order to avoid
    race conditions: An `etag` is returned in the response which contains alert
    metadata, and systems are expected to put that etag in the request to
    update alert metadata to ensure that their change will be applied to the
    same version of the alert metadata.

    If no `etag` is provided in the call to update alert metadata, then the
    existing alert metadata is overwritten blindly.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        status : typing.Text = ...,
        assignee : typing.Text = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        severity : typing.Text = ...,
        etag : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","assignee",b"assignee","customer_id",b"customer_id","etag",b"etag","severity",b"severity","status",b"status","update_time",b"update_time"]) -> None: ...
global___AlertMetadata = AlertMetadata

class Settings(google.protobuf.message.Message):
    """Customer-level settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Notification(google.protobuf.message.Message):
        """Settings for callback notifications.
        For more details see [Google Workspace Alert
        Notification](https://developers.google.com/admin-sdk/alertcenter/guides/notifications).
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class _PayloadFormat:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _PayloadFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PayloadFormat.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
            PAYLOAD_FORMAT_UNSPECIFIED: Settings.Notification.PayloadFormat.ValueType = ...  # 0
            """Payload format is not specified (will use JSON as default)."""

            JSON: Settings.Notification.PayloadFormat.ValueType = ...  # 1
            """Use JSON."""

        class PayloadFormat(_PayloadFormat, metaclass=_PayloadFormatEnumTypeWrapper):
            """The format of the payload."""
            pass

        PAYLOAD_FORMAT_UNSPECIFIED: Settings.Notification.PayloadFormat.ValueType = ...  # 0
        """Payload format is not specified (will use JSON as default)."""

        JSON: Settings.Notification.PayloadFormat.ValueType = ...  # 1
        """Use JSON."""


        class CloudPubsubTopic(google.protobuf.message.Message):
            """A reference to a Cloud Pubsub topic.

            To register for notifications, the owner of the topic must grant
            `alerts-api-push-notifications@system.gserviceaccount.com` the
             `projects.topics.publish` permission.
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            TOPIC_NAME_FIELD_NUMBER: builtins.int
            PAYLOAD_FORMAT_FIELD_NUMBER: builtins.int
            topic_name: typing.Text = ...
            """The `name` field of a Cloud Pubsub [Topic]
            (https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#Topic).
            """

            payload_format: global___Settings.Notification.PayloadFormat.ValueType = ...
            """Optional. The format of the payload that would be sent.
            If not specified the format will be JSON.
            """

            def __init__(self,
                *,
                topic_name : typing.Text = ...,
                payload_format : global___Settings.Notification.PayloadFormat.ValueType = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["payload_format",b"payload_format","topic_name",b"topic_name"]) -> None: ...

        CLOUD_PUBSUB_TOPIC_FIELD_NUMBER: builtins.int
        @property
        def cloud_pubsub_topic(self) -> global___Settings.Notification.CloudPubsubTopic:
            """A Google Cloud Pub/sub topic destination."""
            pass
        def __init__(self,
            *,
            cloud_pubsub_topic : typing.Optional[global___Settings.Notification.CloudPubsubTopic] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["cloud_pubsub_topic",b"cloud_pubsub_topic","destination",b"destination"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["cloud_pubsub_topic",b"cloud_pubsub_topic","destination",b"destination"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["destination",b"destination"]) -> typing.Optional[typing_extensions.Literal["cloud_pubsub_topic"]]: ...

    NOTIFICATIONS_FIELD_NUMBER: builtins.int
    @property
    def notifications(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Settings.Notification]:
        """The list of notifications."""
        pass
    def __init__(self,
        *,
        notifications : typing.Optional[typing.Iterable[global___Settings.Notification]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["notifications",b"notifications"]) -> None: ...
global___Settings = Settings

class BatchDeleteAlertsRequest(google.protobuf.message.Message):
    """A request to perform batch delete on alerts."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alerts are associated with.
    """

    @property
    def alert_id(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. list of alert IDs."""
        pass
    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","customer_id",b"customer_id"]) -> None: ...
global___BatchDeleteAlertsRequest = BatchDeleteAlertsRequest

class BatchDeleteAlertsResponse(google.protobuf.message.Message):
    """Response to batch delete operation on alerts."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class FailedAlertStatusEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> google.rpc.status_pb2.Status: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[google.rpc.status_pb2.Status] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    SUCCESS_ALERT_IDS_FIELD_NUMBER: builtins.int
    FAILED_ALERT_STATUS_FIELD_NUMBER: builtins.int
    @property
    def success_alert_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The successful list of alert IDs."""
        pass
    @property
    def failed_alert_status(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, google.rpc.status_pb2.Status]:
        """The status details for each failed alert_id."""
        pass
    def __init__(self,
        *,
        success_alert_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        failed_alert_status : typing.Optional[typing.Mapping[typing.Text, google.rpc.status_pb2.Status]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["failed_alert_status",b"failed_alert_status","success_alert_ids",b"success_alert_ids"]) -> None: ...
global___BatchDeleteAlertsResponse = BatchDeleteAlertsResponse

class BatchUndeleteAlertsRequest(google.protobuf.message.Message):
    """A request to perform batch undelete on alerts."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alerts are associated with.
    """

    @property
    def alert_id(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. list of alert IDs."""
        pass
    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","customer_id",b"customer_id"]) -> None: ...
global___BatchUndeleteAlertsRequest = BatchUndeleteAlertsRequest

class BatchUndeleteAlertsResponse(google.protobuf.message.Message):
    """Response to batch undelete operation on alerts."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class FailedAlertStatusEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> google.rpc.status_pb2.Status: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[google.rpc.status_pb2.Status] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    SUCCESS_ALERT_IDS_FIELD_NUMBER: builtins.int
    FAILED_ALERT_STATUS_FIELD_NUMBER: builtins.int
    @property
    def success_alert_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The successful list of alert IDs."""
        pass
    @property
    def failed_alert_status(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, google.rpc.status_pb2.Status]:
        """The status details for each failed alert_id."""
        pass
    def __init__(self,
        *,
        success_alert_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        failed_alert_status : typing.Optional[typing.Mapping[typing.Text, google.rpc.status_pb2.Status]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["failed_alert_status",b"failed_alert_status","success_alert_ids",b"success_alert_ids"]) -> None: ...
global___BatchUndeleteAlertsResponse = BatchUndeleteAlertsResponse

class ListAlertsRequest(google.protobuf.message.Message):
    """An alert listing request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alerts are associated with.
    Inferred from the caller identity if not provided.
    """

    page_size: builtins.int = ...
    """Optional. The requested page size. Server may return fewer items than
    requested. If unspecified, server picks an appropriate default.
    """

    page_token: typing.Text = ...
    """Optional. A token identifying a page of results the server should return.
    If empty, a new iteration is started. To continue an iteration, pass in
    the value from the previous ListAlertsResponse's
    [next_page_token][google.apps.alertcenter.v1beta1.ListAlertsResponse.next_page_token] field.
    """

    filter: typing.Text = ...
    """Optional. A query string for filtering alert results.
    For more details, see [Query
    filters](https://developers.google.com/admin-sdk/alertcenter/guides/query-filters) and [Supported
    query filter
    fields](https://developers.google.com/admin-sdk/alertcenter/reference/filter-fields#alerts.list).
    """

    order_by: typing.Text = ...
    """Optional. The sort order of the list results.
    If not specified results may be returned in arbitrary order.
    You can sort the results in descending order based on the creation
    timestamp using `order_by="create_time desc"`.
    Currently, supported sorting are `create_time asc`, `create_time desc`,
    `update_time desc`
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        filter : typing.Text = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","filter",b"filter","order_by",b"order_by","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListAlertsRequest = ListAlertsRequest

class ListAlertsResponse(google.protobuf.message.Message):
    """Response message for an alert listing request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ALERTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def alerts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Alert]:
        """The list of alerts."""
        pass
    next_page_token: typing.Text = ...
    """The token for the next page. If not empty, indicates that there may be more
    alerts that match the listing request; this value can be used in a
    subsequent [ListAlertsRequest][google.apps.alertcenter.v1beta1.ListAlertsRequest] to get alerts continuing from last result
    of the current list call.
    """

    def __init__(self,
        *,
        alerts : typing.Optional[typing.Iterable[global___Alert]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alerts",b"alerts","next_page_token",b"next_page_token"]) -> None: ...
global___ListAlertsResponse = ListAlertsResponse

class GetAlertRequest(google.protobuf.message.Message):
    """Request for a specific alert."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alert is associated with.
    Inferred from the caller identity if not provided.
    """

    alert_id: typing.Text = ...
    """Required. The identifier of the alert to retrieve."""

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","customer_id",b"customer_id"]) -> None: ...
global___GetAlertRequest = GetAlertRequest

class DeleteAlertRequest(google.protobuf.message.Message):
    """A request to mark a specific alert for deletion."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alert is associated with.
    Inferred from the caller identity if not provided.
    """

    alert_id: typing.Text = ...
    """Required. The identifier of the alert to delete."""

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","customer_id",b"customer_id"]) -> None: ...
global___DeleteAlertRequest = DeleteAlertRequest

class UndeleteAlertRequest(google.protobuf.message.Message):
    """A request to undelete a specific alert that was marked for deletion."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alert is associated with.
    Inferred from the caller identity if not provided.
    """

    alert_id: typing.Text = ...
    """Required. The identifier of the alert to undelete."""

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","customer_id",b"customer_id"]) -> None: ...
global___UndeleteAlertRequest = UndeleteAlertRequest

class CreateAlertFeedbackRequest(google.protobuf.message.Message):
    """A request to create a new alert feedback."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    FEEDBACK_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alert is associated with.
    Inferred from the caller identity if not provided.
    """

    alert_id: typing.Text = ...
    """Required. The identifier of the alert this feedback belongs to."""

    @property
    def feedback(self) -> global___AlertFeedback:
        """Required. The new alert feedback to create."""
        pass
    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        feedback : typing.Optional[global___AlertFeedback] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["feedback",b"feedback"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","customer_id",b"customer_id","feedback",b"feedback"]) -> None: ...
global___CreateAlertFeedbackRequest = CreateAlertFeedbackRequest

class ListAlertFeedbackRequest(google.protobuf.message.Message):
    """An alert feedback listing request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alert feedback are associated with.
    Inferred from the caller identity if not provided.
    """

    alert_id: typing.Text = ...
    """Required. The alert identifier.
    The "-" wildcard could be used to represent all alerts.
    """

    filter: typing.Text = ...
    """Optional. A query string for filtering alert feedback results.
    For more details, see [Query
    filters](https://developers.google.com/admin-sdk/alertcenter/guides/query-filters) and [Supported
    query filter
    fields](https://developers.google.com/admin-sdk/alertcenter/reference/filter-fields#alerts.feedback.list).
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        filter : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","customer_id",b"customer_id","filter",b"filter"]) -> None: ...
global___ListAlertFeedbackRequest = ListAlertFeedbackRequest

class ListAlertFeedbackResponse(google.protobuf.message.Message):
    """Response message for an alert feedback listing request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FEEDBACK_FIELD_NUMBER: builtins.int
    @property
    def feedback(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AlertFeedback]:
        """The list of alert feedback.
        Feedback entries for each alert are ordered by creation time descending.
        """
        pass
    def __init__(self,
        *,
        feedback : typing.Optional[typing.Iterable[global___AlertFeedback]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["feedback",b"feedback"]) -> None: ...
global___ListAlertFeedbackResponse = ListAlertFeedbackResponse

class GetAlertMetadataRequest(google.protobuf.message.Message):
    """Get the alert metadata."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ALERT_ID_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alert metadata is associated with.
    Inferred from the caller identity if not provided.
    """

    alert_id: typing.Text = ...
    """Required. The identifier of the alert this metadata belongs to."""

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        alert_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id",b"alert_id","customer_id",b"customer_id"]) -> None: ...
global___GetAlertMetadataRequest = GetAlertMetadataRequest

class GetSettingsRequest(google.protobuf.message.Message):
    """Get the customer level settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alert settings are associated with.
    Inferred from the caller identity if not provided.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id"]) -> None: ...
global___GetSettingsRequest = GetSettingsRequest

class UpdateSettingsRequest(google.protobuf.message.Message):
    """Update the customer level settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Optional. The unique identifier of the Google Workspace organization
    account of the customer the alert settings are associated with.
    Inferred from the caller identity if not provided.
    """

    @property
    def settings(self) -> global___Settings:
        """The customer settings to update."""
        pass
    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        settings : typing.Optional[global___Settings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["settings",b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","settings",b"settings"]) -> None: ...
global___UpdateSettingsRequest = UpdateSettingsRequest
