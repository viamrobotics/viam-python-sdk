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

class MobileAppCategoryConstant(google.protobuf.message.Message):
    """Proto file describing the Mobile App Category Constant resource.

    A mobile application category constant.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Output only. The resource name of the mobile app category constant.
    Mobile app category constant resource names have the form:

    `mobileAppCategoryConstants/{mobile_app_category_id}`
    """

    id: builtins.int = ...
    """Output only. The ID of the mobile app category constant."""

    name: typing.Text = ...
    """Output only. Mobile app category name."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : typing.Optional[builtins.int] = ...,
        name : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_id",b"_id","_name",b"_name","id",b"id","name",b"name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_id",b"_id","_name",b"_name","id",b"id","name",b"name","resource_name",b"resource_name"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
global___MobileAppCategoryConstant = MobileAppCategoryConstant
