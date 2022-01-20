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

class ReportPhishingRequest(google.protobuf.message.Message):
    """The ReportPhishing request message."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the project for which the report will be created,
    in the format "projects/{project_number}".
    """

    uri: typing.Text = ...
    """Required. The URI that is being reported for phishing content to be analyzed."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        uri : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","uri",b"uri"]) -> None: ...
global___ReportPhishingRequest = ReportPhishingRequest

class ReportPhishingResponse(google.protobuf.message.Message):
    """The ReportPhishing (empty) response message."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ReportPhishingResponse = ReportPhishingResponse
