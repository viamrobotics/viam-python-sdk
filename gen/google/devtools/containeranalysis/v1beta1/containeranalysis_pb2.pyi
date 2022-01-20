"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ScanConfig(google.protobuf.message.Message):
    """A scan configuration specifies whether Cloud components in a project have a
    particular type of analysis being run. For example, it can configure whether
    vulnerability scanning is being done on Docker images or not.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The name of the scan configuration in the form of
    `projects/[PROJECT_ID]/scanConfigs/[SCAN_CONFIG_ID]`.
    """

    description: typing.Text = ...
    """Output only. A human-readable description of what the scan configuration
    does.
    """

    enabled: builtins.bool = ...
    """Whether the scan is enabled."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time this scan config was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time this scan config was last updated."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        description : typing.Text = ...,
        enabled : builtins.bool = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","description",b"description","enabled",b"enabled","name",b"name","update_time",b"update_time"]) -> None: ...
global___ScanConfig = ScanConfig

class GetScanConfigRequest(google.protobuf.message.Message):
    """Request to get a scan configuration."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the scan configuration in the form of
    `projects/[PROJECT_ID]/scanConfigs/[SCAN_CONFIG_ID]`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetScanConfigRequest = GetScanConfigRequest

class ListScanConfigsRequest(google.protobuf.message.Message):
    """Request to list scan configurations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the project to list scan configurations for in the form of
    `projects/[PROJECT_ID]`.
    """

    filter: typing.Text = ...
    """Required. The filter expression."""

    page_size: builtins.int = ...
    """The number of scan configs to return in the list."""

    page_token: typing.Text = ...
    """Token to provide to skip to a particular spot in the list."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListScanConfigsRequest = ListScanConfigsRequest

class ListScanConfigsResponse(google.protobuf.message.Message):
    """Response for listing scan configurations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SCAN_CONFIGS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def scan_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ScanConfig]:
        """The scan configurations requested."""
        pass
    next_page_token: typing.Text = ...
    """The next pagination token in the list response. It should be used as
    `page_token` for the following request. An empty value means no more
    results.
    """

    def __init__(self,
        *,
        scan_configs : typing.Optional[typing.Iterable[global___ScanConfig]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","scan_configs",b"scan_configs"]) -> None: ...
global___ListScanConfigsResponse = ListScanConfigsResponse

class UpdateScanConfigRequest(google.protobuf.message.Message):
    """A request to update a scan configuration."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    SCAN_CONFIG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the scan configuration in the form of
    `projects/[PROJECT_ID]/scanConfigs/[SCAN_CONFIG_ID]`.
    """

    @property
    def scan_config(self) -> global___ScanConfig:
        """Required. The updated scan configuration."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        scan_config : typing.Optional[global___ScanConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["scan_config",b"scan_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","scan_config",b"scan_config"]) -> None: ...
global___UpdateScanConfigRequest = UpdateScanConfigRequest
