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

class Folder(google.protobuf.message.Message):
    """Message that contains the resource name and display name of a folder
    resource.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_FOLDER_FIELD_NUMBER: builtins.int
    RESOURCE_FOLDER_DISPLAY_NAME_FIELD_NUMBER: builtins.int
    resource_folder: typing.Text = ...
    """Full resource name of this folder. See:
    https://cloud.google.com/apis/design/resource_names#full_resource_name
    """

    resource_folder_display_name: typing.Text = ...
    """The user defined display name for this folder."""

    def __init__(self,
        *,
        resource_folder : typing.Text = ...,
        resource_folder_display_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_folder",b"resource_folder","resource_folder_display_name",b"resource_folder_display_name"]) -> None: ...
global___Folder = Folder
