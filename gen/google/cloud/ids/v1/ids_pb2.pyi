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

class Endpoint(google.protobuf.message.Message):
    """Endpoint describes a single IDS endpoint. It defines a forwarding rule to
    which packets can be sent for IDS inspection.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Severity:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SeverityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Severity.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        SEVERITY_UNSPECIFIED: Endpoint.Severity.ValueType = ...  # 0
        """Not set."""

        INFORMATIONAL: Endpoint.Severity.ValueType = ...  # 1
        """Informational alerts."""

        LOW: Endpoint.Severity.ValueType = ...  # 2
        """Low severity alerts."""

        MEDIUM: Endpoint.Severity.ValueType = ...  # 3
        """Medium severity alerts."""

        HIGH: Endpoint.Severity.ValueType = ...  # 4
        """High severity alerts."""

        CRITICAL: Endpoint.Severity.ValueType = ...  # 5
        """Critical severity alerts."""

    class Severity(_Severity, metaclass=_SeverityEnumTypeWrapper):
        """Threat severity levels."""
        pass

    SEVERITY_UNSPECIFIED: Endpoint.Severity.ValueType = ...  # 0
    """Not set."""

    INFORMATIONAL: Endpoint.Severity.ValueType = ...  # 1
    """Informational alerts."""

    LOW: Endpoint.Severity.ValueType = ...  # 2
    """Low severity alerts."""

    MEDIUM: Endpoint.Severity.ValueType = ...  # 3
    """Medium severity alerts."""

    HIGH: Endpoint.Severity.ValueType = ...  # 4
    """High severity alerts."""

    CRITICAL: Endpoint.Severity.ValueType = ...  # 5
    """Critical severity alerts."""


    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: Endpoint.State.ValueType = ...  # 0
        """Not set."""

        CREATING: Endpoint.State.ValueType = ...  # 1
        """Being created."""

        READY: Endpoint.State.ValueType = ...  # 2
        """Active and ready for traffic."""

        DELETING: Endpoint.State.ValueType = ...  # 3
        """Being deleted."""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Endpoint state"""
        pass

    STATE_UNSPECIFIED: Endpoint.State.ValueType = ...  # 0
    """Not set."""

    CREATING: Endpoint.State.ValueType = ...  # 1
    """Being created."""

    READY: Endpoint.State.ValueType = ...  # 2
    """Active and ready for traffic."""

    DELETING: Endpoint.State.ValueType = ...  # 3
    """Being deleted."""


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

    NAME_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    ENDPOINT_FORWARDING_RULE_FIELD_NUMBER: builtins.int
    ENDPOINT_IP_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SEVERITY_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    TRAFFIC_LOGS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The name of the endpoint."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The create time timestamp."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The update time timestamp."""
        pass
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """The labels of the endpoint."""
        pass
    network: typing.Text = ...
    """Required. The fully qualified URL of the network to which the IDS Endpoint is
    attached.
    """

    endpoint_forwarding_rule: typing.Text = ...
    """Output only. The fully qualified URL of the endpoint's ILB Forwarding Rule."""

    endpoint_ip: typing.Text = ...
    """Output only. The IP address of the IDS Endpoint's ILB."""

    description: typing.Text = ...
    """User-provided description of the endpoint"""

    severity: global___Endpoint.Severity.ValueType = ...
    """Required. Lowest threat severity that this endpoint will alert on."""

    state: global___Endpoint.State.ValueType = ...
    """Output only. Current state of the endpoint."""

    traffic_logs: builtins.bool = ...
    """Whether the endpoint should report traffic logs in addition to threat logs."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        network : typing.Text = ...,
        endpoint_forwarding_rule : typing.Text = ...,
        endpoint_ip : typing.Text = ...,
        description : typing.Text = ...,
        severity : global___Endpoint.Severity.ValueType = ...,
        state : global___Endpoint.State.ValueType = ...,
        traffic_logs : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","description",b"description","endpoint_forwarding_rule",b"endpoint_forwarding_rule","endpoint_ip",b"endpoint_ip","labels",b"labels","name",b"name","network",b"network","severity",b"severity","state",b"state","traffic_logs",b"traffic_logs","update_time",b"update_time"]) -> None: ...
global___Endpoint = Endpoint

class ListEndpointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent, which owns this collection of endpoints."""

    page_size: builtins.int = ...
    """Optional. The maximum number of endpoints to return. The service may return fewer
    than this value.
    """

    page_token: typing.Text = ...
    """Optional. A page token, received from a previous `ListEndpoints` call.
    Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListEndpoints` must
    match the call that provided the page token.
    """

    filter: typing.Text = ...
    """Optional. The filter expression, following the syntax outlined in
    https://google.aip.dev/160.
    """

    order_by: typing.Text = ...
    """Optional. One or more fields to compare and use to sort the output.
    See https://google.aip.dev/132#ordering.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        filter : typing.Text = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","order_by",b"order_by","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListEndpointsRequest = ListEndpointsRequest

class ListEndpointsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENDPOINTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    UNREACHABLE_FIELD_NUMBER: builtins.int
    @property
    def endpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Endpoint]:
        """The list of endpoints response."""
        pass
    next_page_token: typing.Text = ...
    """A token, which can be sent as `page_token` to retrieve the next page.
    If this field is omitted, there are no subsequent pages.
    """

    @property
    def unreachable(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Locations that could not be reached."""
        pass
    def __init__(self,
        *,
        endpoints : typing.Optional[typing.Iterable[global___Endpoint]] = ...,
        next_page_token : typing.Text = ...,
        unreachable : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoints",b"endpoints","next_page_token",b"next_page_token","unreachable",b"unreachable"]) -> None: ...
global___ListEndpointsResponse = ListEndpointsResponse

class GetEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the endpoint to retrieve.
    Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetEndpointRequest = GetEndpointRequest

class CreateEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    ENDPOINT_ID_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The endpoint's parent."""

    endpoint_id: typing.Text = ...
    """Required. The endpoint identifier. This will be part of the endpoint's
    resource name.
    This value must start with a lowercase letter followed by up to 62
    lowercase letters, numbers, or hyphens, and cannot end with a hyphen.
    Values that do not match this pattern will trigger an INVALID_ARGUMENT
    error.
    """

    @property
    def endpoint(self) -> global___Endpoint:
        """Required. The endpoint to create."""
        pass
    request_id: typing.Text = ...
    """An optional request ID to identify requests. Specify a unique request ID
    so that if you must retry your request, the server will know to ignore
    the request if it has already been completed. The server will guarantee
    that for at least 60 minutes since the first request.

    For example, consider a situation where you make an initial request and t
    he request times out. If you make the request again with the same request
    ID, the server can check if original operation with the same request ID
    was received, and if so, will ignore the second request. This prevents
    clients from accidentally creating duplicate commitments.

    The request ID must be a valid UUID with the exception that zero UUID is
    not supported (00000000-0000-0000-0000-000000000000).
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        endpoint_id : typing.Text = ...,
        endpoint : typing.Optional[global___Endpoint] = ...,
        request_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["endpoint",b"endpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint",b"endpoint","endpoint_id",b"endpoint_id","parent",b"parent","request_id",b"request_id"]) -> None: ...
global___CreateEndpointRequest = CreateEndpointRequest

class DeleteEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the endpoint to delete."""

    request_id: typing.Text = ...
    """An optional request ID to identify requests. Specify a unique request ID
    so that if you must retry your request, the server will know to ignore
    the request if it has already been completed. The server will guarantee
    that for at least 60 minutes after the first request.

    For example, consider a situation where you make an initial request and t
    he request times out. If you make the request again with the same request
    ID, the server can check if original operation with the same request ID
    was received, and if so, will ignore the second request. This prevents
    clients from accidentally creating duplicate commitments.

    The request ID must be a valid UUID with the exception that zero UUID is
    not supported (00000000-0000-0000-0000-000000000000).
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        request_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","request_id",b"request_id"]) -> None: ...
global___DeleteEndpointRequest = DeleteEndpointRequest

class OperationMetadata(google.protobuf.message.Message):
    """Represents the metadata of the long-running operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATE_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    VERB_FIELD_NUMBER: builtins.int
    STATUS_MESSAGE_FIELD_NUMBER: builtins.int
    REQUESTED_CANCELLATION_FIELD_NUMBER: builtins.int
    API_VERSION_FIELD_NUMBER: builtins.int
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time the operation was created."""
        pass
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time the operation finished running."""
        pass
    target: typing.Text = ...
    """Output only. Server-defined resource path for the target of the operation."""

    verb: typing.Text = ...
    """Output only. Name of the verb executed by the operation."""

    status_message: typing.Text = ...
    """Output only. Human-readable status of the operation, if any."""

    requested_cancellation: builtins.bool = ...
    """Output only. Identifies whether the user has requested cancellation
    of the operation. Operations that have successfully been cancelled
    have [Operation.error][] value with a [google.rpc.Status.code][google.rpc.Status.code] of 1,
    corresponding to `Code.CANCELLED`.
    """

    api_version: typing.Text = ...
    """Output only. API version used to start the operation."""

    def __init__(self,
        *,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        target : typing.Text = ...,
        verb : typing.Text = ...,
        status_message : typing.Text = ...,
        requested_cancellation : builtins.bool = ...,
        api_version : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","end_time",b"end_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version",b"api_version","create_time",b"create_time","end_time",b"end_time","requested_cancellation",b"requested_cancellation","status_message",b"status_message","target",b"target","verb",b"verb"]) -> None: ...
global___OperationMetadata = OperationMetadata
