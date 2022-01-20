"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.devtools.clouddebugger.v2.data_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SetBreakpointRequest(google.protobuf.message.Message):
    """Request to set a breakpoint"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEBUGGEE_ID_FIELD_NUMBER: builtins.int
    BREAKPOINT_FIELD_NUMBER: builtins.int
    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    debuggee_id: typing.Text = ...
    """Required. ID of the debuggee where the breakpoint is to be set."""

    @property
    def breakpoint(self) -> google.devtools.clouddebugger.v2.data_pb2.Breakpoint:
        """Required. Breakpoint specification to set.
        The field `location` of the breakpoint must be set.
        """
        pass
    client_version: typing.Text = ...
    """Required. The client version making the call.
    Schema: `domain/type/version` (e.g., `google.com/intellij/v1`).
    """

    def __init__(self,
        *,
        debuggee_id : typing.Text = ...,
        breakpoint : typing.Optional[google.devtools.clouddebugger.v2.data_pb2.Breakpoint] = ...,
        client_version : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["breakpoint",b"breakpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["breakpoint",b"breakpoint","client_version",b"client_version","debuggee_id",b"debuggee_id"]) -> None: ...
global___SetBreakpointRequest = SetBreakpointRequest

class SetBreakpointResponse(google.protobuf.message.Message):
    """Response for setting a breakpoint."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BREAKPOINT_FIELD_NUMBER: builtins.int
    @property
    def breakpoint(self) -> google.devtools.clouddebugger.v2.data_pb2.Breakpoint:
        """Breakpoint resource.
        The field `id` is guaranteed to be set (in addition to the echoed fileds).
        """
        pass
    def __init__(self,
        *,
        breakpoint : typing.Optional[google.devtools.clouddebugger.v2.data_pb2.Breakpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["breakpoint",b"breakpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["breakpoint",b"breakpoint"]) -> None: ...
global___SetBreakpointResponse = SetBreakpointResponse

class GetBreakpointRequest(google.protobuf.message.Message):
    """Request to get breakpoint information."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEBUGGEE_ID_FIELD_NUMBER: builtins.int
    BREAKPOINT_ID_FIELD_NUMBER: builtins.int
    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    debuggee_id: typing.Text = ...
    """Required. ID of the debuggee whose breakpoint to get."""

    breakpoint_id: typing.Text = ...
    """Required. ID of the breakpoint to get."""

    client_version: typing.Text = ...
    """Required. The client version making the call.
    Schema: `domain/type/version` (e.g., `google.com/intellij/v1`).
    """

    def __init__(self,
        *,
        debuggee_id : typing.Text = ...,
        breakpoint_id : typing.Text = ...,
        client_version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["breakpoint_id",b"breakpoint_id","client_version",b"client_version","debuggee_id",b"debuggee_id"]) -> None: ...
global___GetBreakpointRequest = GetBreakpointRequest

class GetBreakpointResponse(google.protobuf.message.Message):
    """Response for getting breakpoint information."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BREAKPOINT_FIELD_NUMBER: builtins.int
    @property
    def breakpoint(self) -> google.devtools.clouddebugger.v2.data_pb2.Breakpoint:
        """Complete breakpoint state.
        The fields `id` and `location` are guaranteed to be set.
        """
        pass
    def __init__(self,
        *,
        breakpoint : typing.Optional[google.devtools.clouddebugger.v2.data_pb2.Breakpoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["breakpoint",b"breakpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["breakpoint",b"breakpoint"]) -> None: ...
global___GetBreakpointResponse = GetBreakpointResponse

class DeleteBreakpointRequest(google.protobuf.message.Message):
    """Request to delete a breakpoint."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEBUGGEE_ID_FIELD_NUMBER: builtins.int
    BREAKPOINT_ID_FIELD_NUMBER: builtins.int
    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    debuggee_id: typing.Text = ...
    """Required. ID of the debuggee whose breakpoint to delete."""

    breakpoint_id: typing.Text = ...
    """Required. ID of the breakpoint to delete."""

    client_version: typing.Text = ...
    """Required. The client version making the call.
    Schema: `domain/type/version` (e.g., `google.com/intellij/v1`).
    """

    def __init__(self,
        *,
        debuggee_id : typing.Text = ...,
        breakpoint_id : typing.Text = ...,
        client_version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["breakpoint_id",b"breakpoint_id","client_version",b"client_version","debuggee_id",b"debuggee_id"]) -> None: ...
global___DeleteBreakpointRequest = DeleteBreakpointRequest

class ListBreakpointsRequest(google.protobuf.message.Message):
    """Request to list breakpoints."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class BreakpointActionValue(google.protobuf.message.Message):
        """Wrapper message for `Breakpoint.Action`. Defines a filter on the action
        field of breakpoints.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        VALUE_FIELD_NUMBER: builtins.int
        value: google.devtools.clouddebugger.v2.data_pb2.Breakpoint.Action.ValueType = ...
        """Only breakpoints with the specified action will pass the filter."""

        def __init__(self,
            *,
            value : google.devtools.clouddebugger.v2.data_pb2.Breakpoint.Action.ValueType = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...

    DEBUGGEE_ID_FIELD_NUMBER: builtins.int
    INCLUDE_ALL_USERS_FIELD_NUMBER: builtins.int
    INCLUDE_INACTIVE_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    STRIP_RESULTS_FIELD_NUMBER: builtins.int
    WAIT_TOKEN_FIELD_NUMBER: builtins.int
    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    debuggee_id: typing.Text = ...
    """Required. ID of the debuggee whose breakpoints to list."""

    include_all_users: builtins.bool = ...
    """When set to `true`, the response includes the list of breakpoints set by
    any user. Otherwise, it includes only breakpoints set by the caller.
    """

    include_inactive: builtins.bool = ...
    """When set to `true`, the response includes active and inactive
    breakpoints. Otherwise, it includes only active breakpoints.
    """

    @property
    def action(self) -> global___ListBreakpointsRequest.BreakpointActionValue:
        """When set, the response includes only breakpoints with the specified action."""
        pass
    strip_results: builtins.bool = ...
    """This field is deprecated. The following fields are always stripped out of
    the result: `stack_frames`, `evaluated_expressions` and `variable_table`.
    """

    wait_token: typing.Text = ...
    """A wait token that, if specified, blocks the call until the breakpoints
    list has changed, or a server selected timeout has expired.  The value
    should be set from the last response. The error code
    `google.rpc.Code.ABORTED` (RPC) is returned on wait timeout, which
    should be called again with the same `wait_token`.
    """

    client_version: typing.Text = ...
    """Required. The client version making the call.
    Schema: `domain/type/version` (e.g., `google.com/intellij/v1`).
    """

    def __init__(self,
        *,
        debuggee_id : typing.Text = ...,
        include_all_users : builtins.bool = ...,
        include_inactive : builtins.bool = ...,
        action : typing.Optional[global___ListBreakpointsRequest.BreakpointActionValue] = ...,
        strip_results : builtins.bool = ...,
        wait_token : typing.Text = ...,
        client_version : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["action",b"action"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action",b"action","client_version",b"client_version","debuggee_id",b"debuggee_id","include_all_users",b"include_all_users","include_inactive",b"include_inactive","strip_results",b"strip_results","wait_token",b"wait_token"]) -> None: ...
global___ListBreakpointsRequest = ListBreakpointsRequest

class ListBreakpointsResponse(google.protobuf.message.Message):
    """Response for listing breakpoints."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BREAKPOINTS_FIELD_NUMBER: builtins.int
    NEXT_WAIT_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def breakpoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.devtools.clouddebugger.v2.data_pb2.Breakpoint]:
        """List of breakpoints matching the request.
        The fields `id` and `location` are guaranteed to be set on each breakpoint.
        The fields: `stack_frames`, `evaluated_expressions` and `variable_table`
        are cleared on each breakpoint regardless of its status.
        """
        pass
    next_wait_token: typing.Text = ...
    """A wait token that can be used in the next call to `list` (REST) or
    `ListBreakpoints` (RPC) to block until the list of breakpoints has changes.
    """

    def __init__(self,
        *,
        breakpoints : typing.Optional[typing.Iterable[google.devtools.clouddebugger.v2.data_pb2.Breakpoint]] = ...,
        next_wait_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["breakpoints",b"breakpoints","next_wait_token",b"next_wait_token"]) -> None: ...
global___ListBreakpointsResponse = ListBreakpointsResponse

class ListDebuggeesRequest(google.protobuf.message.Message):
    """Request to list debuggees."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_FIELD_NUMBER: builtins.int
    INCLUDE_INACTIVE_FIELD_NUMBER: builtins.int
    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    project: typing.Text = ...
    """Required. Project number of a Google Cloud project whose debuggees to list."""

    include_inactive: builtins.bool = ...
    """When set to `true`, the result includes all debuggees. Otherwise, the
    result includes only debuggees that are active.
    """

    client_version: typing.Text = ...
    """Required. The client version making the call.
    Schema: `domain/type/version` (e.g., `google.com/intellij/v1`).
    """

    def __init__(self,
        *,
        project : typing.Text = ...,
        include_inactive : builtins.bool = ...,
        client_version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_version",b"client_version","include_inactive",b"include_inactive","project",b"project"]) -> None: ...
global___ListDebuggeesRequest = ListDebuggeesRequest

class ListDebuggeesResponse(google.protobuf.message.Message):
    """Response for listing debuggees."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEBUGGEES_FIELD_NUMBER: builtins.int
    @property
    def debuggees(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.devtools.clouddebugger.v2.data_pb2.Debuggee]:
        """List of debuggees accessible to the calling user.
        The fields `debuggee.id` and `description` are guaranteed to be set.
        The `description` field is a human readable field provided by agents and
        can be displayed to users.
        """
        pass
    def __init__(self,
        *,
        debuggees : typing.Optional[typing.Iterable[google.devtools.clouddebugger.v2.data_pb2.Debuggee]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["debuggees",b"debuggees"]) -> None: ...
global___ListDebuggeesResponse = ListDebuggeesResponse
