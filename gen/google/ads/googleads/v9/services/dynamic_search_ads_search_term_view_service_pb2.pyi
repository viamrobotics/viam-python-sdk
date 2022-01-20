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

class GetDynamicSearchAdsSearchTermViewRequest(google.protobuf.message.Message):
    """Request message for
    [DynamicSearchAdsSearchTermViewService.GetDynamicSearchAdsSearchTermView][google.ads.googleads.v9.services.DynamicSearchAdsSearchTermViewService.GetDynamicSearchAdsSearchTermView].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the dynamic search ads search term view to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetDynamicSearchAdsSearchTermViewRequest = GetDynamicSearchAdsSearchTermViewRequest
