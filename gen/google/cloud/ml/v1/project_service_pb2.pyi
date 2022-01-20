"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetConfigRequest(google.protobuf.message.Message):
    """Requests service account information associated with a project."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The project name.

    Authorization: requires `Viewer` role on the specified project.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetConfigRequest = GetConfigRequest

class GetConfigResponse(google.protobuf.message.Message):
    """Returns service account information associated with a project."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SERVICE_ACCOUNT_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_PROJECT_FIELD_NUMBER: builtins.int
    service_account: typing.Text = ...
    """The service account Cloud ML uses to access resources in the project."""

    service_account_project: builtins.int = ...
    """The project number for `service_account`."""

    def __init__(self,
        *,
        service_account : typing.Text = ...,
        service_account_project : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["service_account",b"service_account","service_account_project",b"service_account_project"]) -> None: ...
global___GetConfigResponse = GetConfigResponse
