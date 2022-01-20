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

class GetDetailedDemographicRequest(google.protobuf.message.Message):
    """Request message for [DetailedDemographicService.GetDetailedDemographic][google.ads.googleads.v8.services.DetailedDemographicService.GetDetailedDemographic]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. Resource name of the DetailedDemographic to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetDetailedDemographicRequest = GetDetailedDemographicRequest
