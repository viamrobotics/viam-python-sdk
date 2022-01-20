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

class LocationView(google.protobuf.message.Message):
    """Proto file describing the location view resource.

    A location view summarizes the performance of campaigns by
    Location criteria.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Output only. The resource name of the location view.
    Location view resource names have the form:

    `customers/{customer_id}/locationViews/{campaign_id}~{criterion_id}`
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___LocationView = LocationView
