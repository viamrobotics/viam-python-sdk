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

class SinkSettings(google.protobuf.message.Message):
    """Sink Settings for Security Command Center"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOGGING_SINK_PROJECT_FIELD_NUMBER: builtins.int
    logging_sink_project: typing.Text = ...
    """The resource name of the project to send logs to. This project must be
    part of the same organization where the Security Center API is
    enabled. The format is `projects/{project}`. If it is empty, we do
    not output logs. If a project ID is provided it will be normalized to a
    project number.
    """

    def __init__(self,
        *,
        logging_sink_project : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["logging_sink_project",b"logging_sink_project"]) -> None: ...
global___SinkSettings = SinkSettings
