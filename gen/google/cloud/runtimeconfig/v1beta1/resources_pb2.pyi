"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _VariableState:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _VariableStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VariableState.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    VARIABLE_STATE_UNSPECIFIED: VariableState.ValueType = ...  # 0
    """Default variable state."""

    UPDATED: VariableState.ValueType = ...  # 1
    """The variable was updated, while `variables().watch` was executing."""

    DELETED: VariableState.ValueType = ...  # 2
    """The variable was deleted, while `variables().watch` was executing."""

class VariableState(_VariableState, metaclass=_VariableStateEnumTypeWrapper):
    """The `VariableState` describes the last known state of the variable and is
    used during a `variables().watch` call to distinguish the state of the
    variable.
    """
    pass

VARIABLE_STATE_UNSPECIFIED: VariableState.ValueType = ...  # 0
"""Default variable state."""

UPDATED: VariableState.ValueType = ...  # 1
"""The variable was updated, while `variables().watch` was executing."""

DELETED: VariableState.ValueType = ...  # 2
"""The variable was deleted, while `variables().watch` was executing."""

global___VariableState = VariableState


class RuntimeConfig(google.protobuf.message.Message):
    """A RuntimeConfig resource is the primary resource in the Cloud RuntimeConfig
    service. A RuntimeConfig resource consists of metadata and a hierarchy of
    variables.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource name of a runtime config. The name must have the format:

        projects/[PROJECT_ID]/configs/[CONFIG_NAME]

    The `[PROJECT_ID]` must be a valid project ID, and `[CONFIG_NAME]` is an
    arbitrary name that matches RFC 1035 segment specification. The length of
    `[CONFIG_NAME]` must be less than 64 bytes.

    You pick the RuntimeConfig resource name, but the server will validate that
    the name adheres to this format. After you create the resource, you cannot
    change the resource's name.
    """

    description: typing.Text = ...
    """An optional description of the RuntimeConfig object."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        description : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","name",b"name"]) -> None: ...
global___RuntimeConfig = RuntimeConfig

class Variable(google.protobuf.message.Message):
    """Describes a single variable within a RuntimeConfig resource.
    The name denotes the hierarchical variable name. For example,
    `ports/serving_port` is a valid variable name. The variable value is an
    opaque string and only leaf variables can have values (that is, variables
    that do not have any child variables).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the variable resource, in the format:

        projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_NAME]

    The `[PROJECT_ID]` must be a valid project ID, `[CONFIG_NAME]` must be a
    valid RuntimeConfig reource and `[VARIABLE_NAME]` follows Unix file system
    file path naming.

    The `[VARIABLE_NAME]` can contain ASCII letters, numbers, slashes and
    dashes. Slashes are used as path element separators and are not part of the
    `[VARIABLE_NAME]` itself, so `[VARIABLE_NAME]` must contain at least one
    non-slash character. Multiple slashes are coalesced into single slash
    character. Each path segment should follow RFC 1035 segment specification.
    The length of a `[VARIABLE_NAME]` must be less than 256 bytes.

    Once you create a variable, you cannot change the variable name.
    """

    value: builtins.bytes = ...
    """The binary value of the variable. The length of the value must be less
    than 4096 bytes. Empty values are also accepted. The value must be
    base64 encoded. Only one of `value` or `text` can be set.
    """

    text: typing.Text = ...
    """The string value of the variable. The length of the value must be less
    than 4096 bytes. Empty values are also accepted. For example,
    `text: "my text value"`. The string must be valid UTF-8.
    """

    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """[Output Only] The time of the last variable update."""
        pass
    state: global___VariableState.ValueType = ...
    """[Ouput only] The current state of the variable. The variable state
    indicates the outcome of the `variables().watch` call and is visible
    through the `get` and `list` calls.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        value : builtins.bytes = ...,
        text : typing.Text = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        state : global___VariableState.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["contents",b"contents","text",b"text","update_time",b"update_time","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["contents",b"contents","name",b"name","state",b"state","text",b"text","update_time",b"update_time","value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["contents",b"contents"]) -> typing.Optional[typing_extensions.Literal["value","text"]]: ...
global___Variable = Variable

class EndCondition(google.protobuf.message.Message):
    """The condition that a Waiter resource is waiting for."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Cardinality(google.protobuf.message.Message):
        """A Cardinality condition for the Waiter resource. A cardinality condition is
        met when the number of variables under a specified path prefix reaches a
        predefined number. For example, if you set a Cardinality condition where
        the `path` is set to `/foo` and the number of paths is set to 2, the
        following variables would meet the condition in a RuntimeConfig resource:

        + `/foo/variable1 = "value1"`
        + `/foo/variable2 = "value2"`
        + `/bar/variable3 = "value3"`

        It would not would not satisify the same condition with the `number` set to
        3, however, because there is only 2 paths that start with `/foo`.
        Cardinality conditions are recursive; all subtrees under the specific
        path prefix are counted.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        PATH_FIELD_NUMBER: builtins.int
        NUMBER_FIELD_NUMBER: builtins.int
        path: typing.Text = ...
        """The root of the variable subtree to monitor. For example, `/foo`."""

        number: builtins.int = ...
        """The number variables under the `path` that must exist to meet this
        condition. Defaults to 1 if not specified.
        """

        def __init__(self,
            *,
            path : typing.Text = ...,
            number : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["number",b"number","path",b"path"]) -> None: ...

    CARDINALITY_FIELD_NUMBER: builtins.int
    @property
    def cardinality(self) -> global___EndCondition.Cardinality:
        """The cardinality of the `EndCondition`."""
        pass
    def __init__(self,
        *,
        cardinality : typing.Optional[global___EndCondition.Cardinality] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cardinality",b"cardinality","condition",b"condition"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cardinality",b"cardinality","condition",b"condition"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["condition",b"condition"]) -> typing.Optional[typing_extensions.Literal["cardinality"]]: ...
global___EndCondition = EndCondition

class Waiter(google.protobuf.message.Message):
    """A Waiter resource waits for some end condition within a RuntimeConfig
    resource to be met before it returns. For example, assume you have a
    distributed system where each node writes to a Variable resource indidicating
    the node's readiness as part of the startup process.

    You then configure a Waiter resource with the success condition set to wait
    until some number of nodes have checked in. Afterwards, your application
    runs some arbitrary code after the condition has been met and the waiter
    returns successfully.

    Once created, a Waiter resource is immutable.

    To learn more about using waiters, read the
    [Creating a
    Waiter](/deployment-manager/runtime-configurator/creating-a-waiter)
    documentation.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    FAILURE_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    DONE_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the Waiter resource, in the format:

        projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]

    The `[PROJECT_ID]` must be a valid Google Cloud project ID,
    the `[CONFIG_NAME]` must be a valid RuntimeConfig resource, the
    `[WAITER_NAME]` must match RFC 1035 segment specification, and the length
    of `[WAITER_NAME]` must be less than 64 bytes.

    After you create a Waiter resource, you cannot change the resource name.
    """

    @property
    def timeout(self) -> google.protobuf.duration_pb2.Duration:
        """[Required] Specifies the timeout of the waiter in seconds, beginning from
        the instant that `waiters().create` method is called. If this time elapses
        before the success or failure conditions are met, the waiter fails and sets
        the `error` code to `DEADLINE_EXCEEDED`.
        """
        pass
    @property
    def failure(self) -> global___EndCondition:
        """[Optional] The failure condition of this waiter. If this condition is met,
        `done` will be set to `true` and the `error` code will be set to `ABORTED`.
        The failure condition takes precedence over the success condition. If both
        conditions are met, a failure will be indicated. This value is optional; if
        no failure condition is set, the only failure scenario will be a timeout.
        """
        pass
    @property
    def success(self) -> global___EndCondition:
        """[Required] The success condition. If this condition is met, `done` will be
        set to `true` and the `error` value will remain unset. The failure
        condition takes precedence over the success condition. If both conditions
        are met, a failure will be indicated.
        """
        pass
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """[Output Only] The instant at which this Waiter resource was created. Adding
        the value of `timeout` to this instant yields the timeout deadline for the
        waiter.
        """
        pass
    done: builtins.bool = ...
    """[Output Only] If the value is `false`, it means the waiter is still waiting
    for one of its conditions to be met.

    If true, the waiter has finished. If the waiter finished due to a timeout
    or failure, `error` will be set.
    """

    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """[Output Only] If the waiter ended due to a failure or timeout, this value
        will be set.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        timeout : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        failure : typing.Optional[global___EndCondition] = ...,
        success : typing.Optional[global___EndCondition] = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        done : builtins.bool = ...,
        error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","error",b"error","failure",b"failure","success",b"success","timeout",b"timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","done",b"done","error",b"error","failure",b"failure","name",b"name","success",b"success","timeout",b"timeout"]) -> None: ...
global___Waiter = Waiter
