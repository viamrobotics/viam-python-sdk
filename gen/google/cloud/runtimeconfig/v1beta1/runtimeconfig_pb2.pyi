"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.runtimeconfig.v1beta1.resources_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ListConfigsRequest(google.protobuf.message.Message):
    """Request for the `ListConfigs()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The [project
    ID](https://support.google.com/cloud/answer/6158840?hl=en&ref_topic=6158848)
    for this request, in the format `projects/[PROJECT_ID]`.
    """

    page_size: builtins.int = ...
    """Specifies the number of results to return per page. If there are fewer
    elements than the specified number, returns all elements.
    """

    page_token: typing.Text = ...
    """Specifies a page token to use. Set `pageToken` to a `nextPageToken`
    returned by a previous list request to get the next page of results.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListConfigsRequest = ListConfigsRequest

class ListConfigsResponse(google.protobuf.message.Message):
    """`ListConfigs()` returns the following response. The order of returned
    objects is arbitrary; that is, it is not ordered in any particular way.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONFIGS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig]:
        """A list of the configurations in the project. The order of returned
        objects is arbitrary; that is, it is not ordered in any particular way.
        """
        pass
    next_page_token: typing.Text = ...
    """This token allows you to get the next page of results for list requests.
    If the number of results is larger than `pageSize`, use the `nextPageToken`
    as a value for the query parameter `pageToken` in the next list request.
    Subsequent list requests will have their own `nextPageToken` to continue
    paging through the results
    """

    def __init__(self,
        *,
        configs : typing.Optional[typing.Iterable[google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["configs",b"configs","next_page_token",b"next_page_token"]) -> None: ...
global___ListConfigsResponse = ListConfigsResponse

class GetConfigRequest(google.protobuf.message.Message):
    """Gets a RuntimeConfig resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the RuntimeConfig resource to retrieve, in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetConfigRequest = GetConfigRequest

class CreateConfigRequest(google.protobuf.message.Message):
    """Creates a RuntimeConfig resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The [project
    ID](https://support.google.com/cloud/answer/6158840?hl=en&ref_topic=6158848)
    for this request, in the format `projects/[PROJECT_ID]`.
    """

    @property
    def config(self) -> google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig:
        """The RuntimeConfig to create."""
        pass
    request_id: typing.Text = ...
    """An optional but recommended unique `request_id`. If the server
    receives two `create()` requests  with the same
    `request_id`, then the second request will be ignored and the
    first resource created and stored in the backend is returned.
    Empty `request_id` fields are ignored.

    It is responsibility of the client to ensure uniqueness of the
    `request_id` strings.

    `request_id` strings are limited to 64 characters.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        config : typing.Optional[google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig] = ...,
        request_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","parent",b"parent","request_id",b"request_id"]) -> None: ...
global___CreateConfigRequest = CreateConfigRequest

class UpdateConfigRequest(google.protobuf.message.Message):
    """Request message for `UpdateConfig()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the RuntimeConfig resource to update, in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    """

    @property
    def config(self) -> google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig:
        """The config resource to update."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        config : typing.Optional[google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","name",b"name"]) -> None: ...
global___UpdateConfigRequest = UpdateConfigRequest

class DeleteConfigRequest(google.protobuf.message.Message):
    """Request for the `DeleteConfig()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The RuntimeConfig resource to delete, in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteConfigRequest = DeleteConfigRequest

class ListVariablesRequest(google.protobuf.message.Message):
    """Request for the `ListVariables()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    RETURN_VALUES_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The path to the RuntimeConfig resource for which you want to list
    variables. The configuration must exist beforehand; the path must by in the
    format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    """

    filter: typing.Text = ...
    """Filters variables by matching the specified filter. For example:

    `projects/example-project/config/[CONFIG_NAME]/variables/example-variable`.
    """

    page_size: builtins.int = ...
    """Specifies the number of results to return per page. If there are fewer
    elements than the specified number, returns all elements.
    """

    page_token: typing.Text = ...
    """Specifies a page token to use. Set `pageToken` to a `nextPageToken`
    returned by a previous list request to get the next page of results.
    """

    return_values: builtins.bool = ...
    """The flag indicates whether the user wants to return values of variables.
    If true, then only those variables that user has IAM GetVariable permission
    will be returned along with their values.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        return_values : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","parent",b"parent","return_values",b"return_values"]) -> None: ...
global___ListVariablesRequest = ListVariablesRequest

class ListVariablesResponse(google.protobuf.message.Message):
    """Response for the `ListVariables()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VARIABLES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def variables(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable]:
        """A list of variables and their values. The order of returned variable
        objects is arbitrary.
        """
        pass
    next_page_token: typing.Text = ...
    """This token allows you to get the next page of results for list requests.
    If the number of results is larger than `pageSize`, use the `nextPageToken`
    as a value for the query parameter `pageToken` in the next list request.
    Subsequent list requests will have their own `nextPageToken` to continue
    paging through the results
    """

    def __init__(self,
        *,
        variables : typing.Optional[typing.Iterable[google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","variables",b"variables"]) -> None: ...
global___ListVariablesResponse = ListVariablesResponse

class WatchVariableRequest(google.protobuf.message.Message):
    """Request for the `WatchVariable()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    NEWER_THAN_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the variable to watch, in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    """

    @property
    def newer_than(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """If specified, checks the current timestamp of the variable and if the
        current timestamp is newer than `newerThan` timestamp, the method returns
        immediately.

        If not specified or the variable has an older timestamp, the watcher waits
        for a the value to change before returning.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        newer_than : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["newer_than",b"newer_than"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","newer_than",b"newer_than"]) -> None: ...
global___WatchVariableRequest = WatchVariableRequest

class GetVariableRequest(google.protobuf.message.Message):
    """Request for the `GetVariable()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the variable to return, in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIBLE_NAME]`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetVariableRequest = GetVariableRequest

class CreateVariableRequest(google.protobuf.message.Message):
    """Request for the `CreateVariable()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    VARIABLE_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The path to the RutimeConfig resource that this variable should belong to.
    The configuration must exist beforehand; the path must by in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    """

    @property
    def variable(self) -> google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable:
        """The variable to create."""
        pass
    request_id: typing.Text = ...
    """An optional but recommended unique `request_id`. If the server
    receives two `create()` requests  with the same
    `request_id`, then the second request will be ignored and the
    first resource created and stored in the backend is returned.
    Empty `request_id` fields are ignored.

    It is responsibility of the client to ensure uniqueness of the
    `request_id` strings.

    `request_id` strings are limited to 64 characters.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        variable : typing.Optional[google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable] = ...,
        request_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["variable",b"variable"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","request_id",b"request_id","variable",b"variable"]) -> None: ...
global___CreateVariableRequest = CreateVariableRequest

class UpdateVariableRequest(google.protobuf.message.Message):
    """Request for the `UpdateVariable()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VARIABLE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the variable to update, in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_NAME]`
    """

    @property
    def variable(self) -> google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable:
        """The variable to update."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        variable : typing.Optional[google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["variable",b"variable"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","variable",b"variable"]) -> None: ...
global___UpdateVariableRequest = UpdateVariableRequest

class DeleteVariableRequest(google.protobuf.message.Message):
    """Request for the `DeleteVariable()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    RECURSIVE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the variable to delete, in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_NAME]`
    """

    recursive: builtins.bool = ...
    """Set to `true` to recursively delete multiple variables with the same
    prefix.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        recursive : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","recursive",b"recursive"]) -> None: ...
global___DeleteVariableRequest = DeleteVariableRequest

class ListWaitersRequest(google.protobuf.message.Message):
    """Request for the `ListWaiters()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The path to the configuration for which you want to get a list of waiters.
    The configuration must exist beforehand; the path must by in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`
    """

    page_size: builtins.int = ...
    """Specifies the number of results to return per page. If there are fewer
    elements than the specified number, returns all elements.
    """

    page_token: typing.Text = ...
    """Specifies a page token to use. Set `pageToken` to a `nextPageToken`
    returned by a previous list request to get the next page of results.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListWaitersRequest = ListWaitersRequest

class ListWaitersResponse(google.protobuf.message.Message):
    """Response for the `ListWaiters()` method.
    Order of returned waiter objects is arbitrary.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WAITERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def waiters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.runtimeconfig.v1beta1.resources_pb2.Waiter]:
        """Found waiters in the project."""
        pass
    next_page_token: typing.Text = ...
    """This token allows you to get the next page of results for list requests.
    If the number of results is larger than `pageSize`, use the `nextPageToken`
    as a value for the query parameter `pageToken` in the next list request.
    Subsequent list requests will have their own `nextPageToken` to continue
    paging through the results
    """

    def __init__(self,
        *,
        waiters : typing.Optional[typing.Iterable[google.cloud.runtimeconfig.v1beta1.resources_pb2.Waiter]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","waiters",b"waiters"]) -> None: ...
global___ListWaitersResponse = ListWaitersResponse

class GetWaiterRequest(google.protobuf.message.Message):
    """Request for the `GetWaiter()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The fully-qualified name of the Waiter resource object to retrieve, in the
    format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetWaiterRequest = GetWaiterRequest

class CreateWaiterRequest(google.protobuf.message.Message):
    """Request message for `CreateWaiter()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    WAITER_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The path to the configuration that will own the waiter.
    The configuration must exist beforehand; the path must by in the format:

    `projects/[PROJECT_ID]/configs/[CONFIG_NAME]`.
    """

    @property
    def waiter(self) -> google.cloud.runtimeconfig.v1beta1.resources_pb2.Waiter:
        """The Waiter resource to create."""
        pass
    request_id: typing.Text = ...
    """An optional but recommended unique `request_id`. If the server
    receives two `create()` requests  with the same
    `request_id`, then the second request will be ignored and the
    first resource created and stored in the backend is returned.
    Empty `request_id` fields are ignored.

    It is responsibility of the client to ensure uniqueness of the
    `request_id` strings.

    `request_id` strings are limited to 64 characters.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        waiter : typing.Optional[google.cloud.runtimeconfig.v1beta1.resources_pb2.Waiter] = ...,
        request_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["waiter",b"waiter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","request_id",b"request_id","waiter",b"waiter"]) -> None: ...
global___CreateWaiterRequest = CreateWaiterRequest

class DeleteWaiterRequest(google.protobuf.message.Message):
    """Request for the `DeleteWaiter()` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The Waiter resource to delete, in the format:

     `projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteWaiterRequest = DeleteWaiterRequest
