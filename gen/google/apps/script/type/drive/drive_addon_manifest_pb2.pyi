"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.apps.script.type.extension_point_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class DriveAddOnManifest(google.protobuf.message.Message):
    """Manifest section specific to Drive Add-ons.

    Drive add-on manifest.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HOMEPAGE_TRIGGER_FIELD_NUMBER: builtins.int
    ON_ITEMS_SELECTED_TRIGGER_FIELD_NUMBER: builtins.int
    @property
    def homepage_trigger(self) -> google.apps.script.type.extension_point_pb2.HomepageExtensionPoint:
        """If present, this overrides the configuration from
        `addOns.common.homepageTrigger`.
        """
        pass
    @property
    def on_items_selected_trigger(self) -> global___DriveExtensionPoint:
        """Corresponds to behvior that should execute when items are selected
        in relevant Drive view (e.g. the My Drive Doclist).
        """
        pass
    def __init__(self,
        *,
        homepage_trigger : typing.Optional[google.apps.script.type.extension_point_pb2.HomepageExtensionPoint] = ...,
        on_items_selected_trigger : typing.Optional[global___DriveExtensionPoint] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["homepage_trigger",b"homepage_trigger","on_items_selected_trigger",b"on_items_selected_trigger"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["homepage_trigger",b"homepage_trigger","on_items_selected_trigger",b"on_items_selected_trigger"]) -> None: ...
global___DriveAddOnManifest = DriveAddOnManifest

class DriveExtensionPoint(google.protobuf.message.Message):
    """A generic extension point with common features, e.g. something that simply
    needs a corresponding run function to work.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RUN_FUNCTION_FIELD_NUMBER: builtins.int
    run_function: typing.Text = ...
    """Required. The endpoint to execute when this extension point is
    activated.
    """

    def __init__(self,
        *,
        run_function : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_function",b"run_function"]) -> None: ...
global___DriveExtensionPoint = DriveExtensionPoint
