"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.extension_setting_device_pb2
import google.ads.googleads.v8.enums.extension_type_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AdGroupExtensionSetting(google.protobuf.message.Message):
    """Proto file describing the AdGroupExtensionSetting resource.

    An ad group extension setting.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    EXTENSION_TYPE_FIELD_NUMBER: builtins.int
    AD_GROUP_FIELD_NUMBER: builtins.int
    EXTENSION_FEED_ITEMS_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the ad group extension setting.
    AdGroupExtensionSetting resource names have the form:

    `customers/{customer_id}/adGroupExtensionSettings/{ad_group_id}~{extension_type}`
    """

    extension_type: google.ads.googleads.v8.enums.extension_type_pb2.ExtensionTypeEnum.ExtensionType.ValueType = ...
    """Immutable. The extension type of the ad group extension setting."""

    ad_group: typing.Text = ...
    """Immutable. The resource name of the ad group. The linked extension feed items will
    serve under this ad group.
    AdGroup resource names have the form:

    `customers/{customer_id}/adGroups/{ad_group_id}`
    """

    @property
    def extension_feed_items(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The resource names of the extension feed items to serve under the ad group.
        ExtensionFeedItem resource names have the form:

        `customers/{customer_id}/extensionFeedItems/{feed_item_id}`
        """
        pass
    device: google.ads.googleads.v8.enums.extension_setting_device_pb2.ExtensionSettingDeviceEnum.ExtensionSettingDevice.ValueType = ...
    """The device for which the extensions will serve. Optional."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        extension_type : google.ads.googleads.v8.enums.extension_type_pb2.ExtensionTypeEnum.ExtensionType.ValueType = ...,
        ad_group : typing.Optional[typing.Text] = ...,
        extension_feed_items : typing.Optional[typing.Iterable[typing.Text]] = ...,
        device : google.ads.googleads.v8.enums.extension_setting_device_pb2.ExtensionSettingDeviceEnum.ExtensionSettingDevice.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_ad_group",b"_ad_group","ad_group",b"ad_group"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_ad_group",b"_ad_group","ad_group",b"ad_group","device",b"device","extension_feed_items",b"extension_feed_items","extension_type",b"extension_type","resource_name",b"resource_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_ad_group",b"_ad_group"]) -> typing.Optional[typing_extensions.Literal["ad_group"]]: ...
global___AdGroupExtensionSetting = AdGroupExtensionSetting
