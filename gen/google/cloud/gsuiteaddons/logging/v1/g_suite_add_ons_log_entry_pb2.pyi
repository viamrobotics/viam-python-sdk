"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GSuiteAddOnsLogEntry(google.protobuf.message.Message):
    """JSON payload of error messages that are logged to Cloud Logging. An error
    message (in English) is written to Cloud Logging (if not disabled) when an
    error is encountered while using an add-on.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEPLOYMENT_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    DEPLOYMENT_FUNCTION_FIELD_NUMBER: builtins.int
    deployment: typing.Text = ...
    """The deployment that caused the error. For add-ons built in Apps Script,
    this is the deployment ID defined by Apps Script. For add-ons built in
    other languages, this is the deployment ID defined in Google Cloud.
    """

    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """The error code and message."""
        pass
    deployment_function: typing.Text = ...
    """The function name that was running when the error occurred. This field
    might not always be set, for example, if an error happens when fetching the
    list of installed add-ons for a user.
    """

    def __init__(self,
        *,
        deployment : typing.Text = ...,
        error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        deployment_function : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deployment",b"deployment","deployment_function",b"deployment_function","error",b"error"]) -> None: ...
global___GSuiteAddOnsLogEntry = GSuiteAddOnsLogEntry
