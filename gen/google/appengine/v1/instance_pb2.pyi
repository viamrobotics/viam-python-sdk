"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Instance(google.protobuf.message.Message):
    """An Instance resource is the computing unit that App Engine uses to
    automatically scale an application.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Availability:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AvailabilityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Availability.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: Instance.Availability.ValueType = ...  # 0
        RESIDENT: Instance.Availability.ValueType = ...  # 1
        DYNAMIC: Instance.Availability.ValueType = ...  # 2
    class Availability(_Availability, metaclass=_AvailabilityEnumTypeWrapper):
        """Availability of the instance."""
        pass

    UNSPECIFIED: Instance.Availability.ValueType = ...  # 0
    RESIDENT: Instance.Availability.ValueType = ...  # 1
    DYNAMIC: Instance.Availability.ValueType = ...  # 2

    class Liveness(google.protobuf.message.Message):
        """Wrapper for LivenessState enum."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class _LivenessState:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _LivenessStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LivenessState.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
            LIVENESS_STATE_UNSPECIFIED: Instance.Liveness.LivenessState.ValueType = ...  # 0
            """There is no liveness health check for the instance. Only applicable for
            instances in App Engine standard environment.
            """

            UNKNOWN: Instance.Liveness.LivenessState.ValueType = ...  # 1
            """The health checking system is aware of the instance but its health is
            not known at the moment.
            """

            HEALTHY: Instance.Liveness.LivenessState.ValueType = ...  # 2
            """The instance is reachable i.e. a connection to the application health
            checking endpoint can be established, and conforms to the requirements
            defined by the health check.
            """

            UNHEALTHY: Instance.Liveness.LivenessState.ValueType = ...  # 3
            """The instance is reachable, but does not conform to the requirements
            defined by the health check.
            """

            DRAINING: Instance.Liveness.LivenessState.ValueType = ...  # 4
            """The instance is being drained. The existing connections to the instance
            have time to complete, but the new ones are being refused.
            """

            TIMEOUT: Instance.Liveness.LivenessState.ValueType = ...  # 5
            """The instance is unreachable i.e. a connection to the application health
            checking endpoint cannot be established, or the server does not respond
            within the specified timeout.
            """

        class LivenessState(_LivenessState, metaclass=_LivenessStateEnumTypeWrapper):
            """Liveness health check status for Flex instances."""
            pass

        LIVENESS_STATE_UNSPECIFIED: Instance.Liveness.LivenessState.ValueType = ...  # 0
        """There is no liveness health check for the instance. Only applicable for
        instances in App Engine standard environment.
        """

        UNKNOWN: Instance.Liveness.LivenessState.ValueType = ...  # 1
        """The health checking system is aware of the instance but its health is
        not known at the moment.
        """

        HEALTHY: Instance.Liveness.LivenessState.ValueType = ...  # 2
        """The instance is reachable i.e. a connection to the application health
        checking endpoint can be established, and conforms to the requirements
        defined by the health check.
        """

        UNHEALTHY: Instance.Liveness.LivenessState.ValueType = ...  # 3
        """The instance is reachable, but does not conform to the requirements
        defined by the health check.
        """

        DRAINING: Instance.Liveness.LivenessState.ValueType = ...  # 4
        """The instance is being drained. The existing connections to the instance
        have time to complete, but the new ones are being refused.
        """

        TIMEOUT: Instance.Liveness.LivenessState.ValueType = ...  # 5
        """The instance is unreachable i.e. a connection to the application health
        checking endpoint cannot be established, or the server does not respond
        within the specified timeout.
        """


        def __init__(self,
            ) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    APP_ENGINE_RELEASE_FIELD_NUMBER: builtins.int
    AVAILABILITY_FIELD_NUMBER: builtins.int
    VM_NAME_FIELD_NUMBER: builtins.int
    VM_ZONE_NAME_FIELD_NUMBER: builtins.int
    VM_ID_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    REQUESTS_FIELD_NUMBER: builtins.int
    ERRORS_FIELD_NUMBER: builtins.int
    QPS_FIELD_NUMBER: builtins.int
    AVERAGE_LATENCY_FIELD_NUMBER: builtins.int
    MEMORY_USAGE_FIELD_NUMBER: builtins.int
    VM_STATUS_FIELD_NUMBER: builtins.int
    VM_DEBUG_ENABLED_FIELD_NUMBER: builtins.int
    VM_IP_FIELD_NUMBER: builtins.int
    VM_LIVENESS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. Full path to the Instance resource in the API.
    Example: `apps/myapp/services/default/versions/v1/instances/instance-1`.
    """

    id: typing.Text = ...
    """Output only. Relative name of the instance within the version.
    Example: `instance-1`.
    """

    app_engine_release: typing.Text = ...
    """Output only. App Engine release this instance is running on."""

    availability: global___Instance.Availability.ValueType = ...
    """Output only. Availability of the instance."""

    vm_name: typing.Text = ...
    """Output only. Name of the virtual machine where this instance lives. Only applicable
    for instances in App Engine flexible environment.
    """

    vm_zone_name: typing.Text = ...
    """Output only. Zone where the virtual machine is located. Only applicable for instances
    in App Engine flexible environment.
    """

    vm_id: typing.Text = ...
    """Output only. Virtual machine ID of this instance. Only applicable for instances in
    App Engine flexible environment.
    """

    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Time that this instance was started.

        @OutputOnly
        """
        pass
    requests: builtins.int = ...
    """Output only. Number of requests since this instance was started."""

    errors: builtins.int = ...
    """Output only. Number of errors since this instance was started."""

    qps: builtins.float = ...
    """Output only. Average queries per second (QPS) over the last minute."""

    average_latency: builtins.int = ...
    """Output only. Average latency (ms) over the last minute."""

    memory_usage: builtins.int = ...
    """Output only. Total memory in use (bytes)."""

    vm_status: typing.Text = ...
    """Output only. Status of the virtual machine where this instance lives. Only applicable
    for instances in App Engine flexible environment.
    """

    vm_debug_enabled: builtins.bool = ...
    """Output only. Whether this instance is in debug mode. Only applicable for instances in
    App Engine flexible environment.
    """

    vm_ip: typing.Text = ...
    """Output only. The IP address of this instance. Only applicable for instances in App
    Engine flexible environment.
    """

    vm_liveness: global___Instance.Liveness.LivenessState.ValueType = ...
    """Output only. The liveness health check of this instance. Only applicable for instances
    in App Engine flexible environment.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        id : typing.Text = ...,
        app_engine_release : typing.Text = ...,
        availability : global___Instance.Availability.ValueType = ...,
        vm_name : typing.Text = ...,
        vm_zone_name : typing.Text = ...,
        vm_id : typing.Text = ...,
        start_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        requests : builtins.int = ...,
        errors : builtins.int = ...,
        qps : builtins.float = ...,
        average_latency : builtins.int = ...,
        memory_usage : builtins.int = ...,
        vm_status : typing.Text = ...,
        vm_debug_enabled : builtins.bool = ...,
        vm_ip : typing.Text = ...,
        vm_liveness : global___Instance.Liveness.LivenessState.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["start_time",b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_engine_release",b"app_engine_release","availability",b"availability","average_latency",b"average_latency","errors",b"errors","id",b"id","memory_usage",b"memory_usage","name",b"name","qps",b"qps","requests",b"requests","start_time",b"start_time","vm_debug_enabled",b"vm_debug_enabled","vm_id",b"vm_id","vm_ip",b"vm_ip","vm_liveness",b"vm_liveness","vm_name",b"vm_name","vm_status",b"vm_status","vm_zone_name",b"vm_zone_name"]) -> None: ...
global___Instance = Instance
