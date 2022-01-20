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

class GetMobileDeviceConstantRequest(google.protobuf.message.Message):
    """Request message for [MobileDeviceConstantService.GetMobileDeviceConstant][google.ads.googleads.v7.services.MobileDeviceConstantService.GetMobileDeviceConstant]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. Resource name of the mobile device to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetMobileDeviceConstantRequest = GetMobileDeviceConstantRequest
