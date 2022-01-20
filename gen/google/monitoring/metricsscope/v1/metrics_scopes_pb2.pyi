"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.monitoring.metricsscope.v1.metrics_scope_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetMetricsScopeRequest(google.protobuf.message.Message):
    """Request for the `GetMetricsScope` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the `Metrics Scope`.
    Example:
    `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetMetricsScopeRequest = GetMetricsScopeRequest

class ListMetricsScopesByMonitoredProjectRequest(google.protobuf.message.Message):
    """Request for the `ListMetricsScopesByMonitoredProject` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MONITORED_RESOURCE_CONTAINER_FIELD_NUMBER: builtins.int
    monitored_resource_container: typing.Text = ...
    """Required. The resource name of the `Monitored Project` being requested.
    Example:
    `projects/{MONITORED_PROJECT_ID_OR_NUMBER}`
    """

    def __init__(self,
        *,
        monitored_resource_container : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["monitored_resource_container",b"monitored_resource_container"]) -> None: ...
global___ListMetricsScopesByMonitoredProjectRequest = ListMetricsScopesByMonitoredProjectRequest

class ListMetricsScopesByMonitoredProjectResponse(google.protobuf.message.Message):
    """Response for the `ListMetricsScopesByMonitoredProject` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    METRICS_SCOPES_FIELD_NUMBER: builtins.int
    @property
    def metrics_scopes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.monitoring.metricsscope.v1.metrics_scope_pb2.MetricsScope]:
        """A set of all metrics scopes that the specified monitored project has been
        added to.
        """
        pass
    def __init__(self,
        *,
        metrics_scopes : typing.Optional[typing.Iterable[google.monitoring.metricsscope.v1.metrics_scope_pb2.MetricsScope]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["metrics_scopes",b"metrics_scopes"]) -> None: ...
global___ListMetricsScopesByMonitoredProjectResponse = ListMetricsScopesByMonitoredProjectResponse

class CreateMonitoredProjectRequest(google.protobuf.message.Message):
    """Request for the `CreateMonitoredProject` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    MONITORED_PROJECT_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The resource name of the existing `Metrics Scope` that will monitor this
    project.
    Example:
    `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}`
    """

    @property
    def monitored_project(self) -> google.monitoring.metricsscope.v1.metrics_scope_pb2.MonitoredProject:
        """Required. The initial `MonitoredProject` configuration.
        Specify only the `monitored_project.name` field. All other fields are
        ignored. The `monitored_project.name` must be in the format:
        `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}`
        """
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        monitored_project : typing.Optional[google.monitoring.metricsscope.v1.metrics_scope_pb2.MonitoredProject] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["monitored_project",b"monitored_project"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["monitored_project",b"monitored_project","parent",b"parent"]) -> None: ...
global___CreateMonitoredProjectRequest = CreateMonitoredProjectRequest

class DeleteMonitoredProjectRequest(google.protobuf.message.Message):
    """Request for the `DeleteMonitoredProject` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the `MonitoredProject`.
    Example:
    `locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}`

    Authorization requires the following [Google
    IAM](https://cloud.google.com/iam) permissions on both the `Metrics Scope`
    and on the `MonitoredProject`: `monitoring.metricsScopes.link`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteMonitoredProjectRequest = DeleteMonitoredProjectRequest

class OperationMetadata(google.protobuf.message.Message):
    """Contains metadata for longrunning operation for the edit Metrics Scope
    endpoints.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: OperationMetadata.State.ValueType = ...  # 0
        """Invalid."""

        CREATED: OperationMetadata.State.ValueType = ...  # 1
        """Request has been received."""

        RUNNING: OperationMetadata.State.ValueType = ...  # 2
        """Request is actively being processed."""

        DONE: OperationMetadata.State.ValueType = ...  # 3
        """The batch processing is done."""

        CANCELLED: OperationMetadata.State.ValueType = ...  # 4
        """The batch processing was cancelled."""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Batch operation states."""
        pass

    STATE_UNSPECIFIED: OperationMetadata.State.ValueType = ...  # 0
    """Invalid."""

    CREATED: OperationMetadata.State.ValueType = ...  # 1
    """Request has been received."""

    RUNNING: OperationMetadata.State.ValueType = ...  # 2
    """Request is actively being processed."""

    DONE: OperationMetadata.State.ValueType = ...  # 3
    """The batch processing is done."""

    CANCELLED: OperationMetadata.State.ValueType = ...  # 4
    """The batch processing was cancelled."""


    STATE_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    state: global___OperationMetadata.State.ValueType = ...
    """Current state of the batch operation."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the batch request was received."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time when the operation result was last updated."""
        pass
    def __init__(self,
        *,
        state : global___OperationMetadata.State.ValueType = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","state",b"state","update_time",b"update_time"]) -> None: ...
global___OperationMetadata = OperationMetadata
