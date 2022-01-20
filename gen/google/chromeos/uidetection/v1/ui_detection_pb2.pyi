"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class UiDetectionRequest(google.protobuf.message.Message):
    """Request message for UI detection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IMAGE_PNG_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    image_png: builtins.bytes = ...
    """Required. Required field that represents a PNG image."""

    @property
    def request(self) -> global___DetectionRequest:
        """Required. Required field that indicates the detection type."""
        pass
    def __init__(self,
        *,
        image_png : builtins.bytes = ...,
        request : typing.Optional[global___DetectionRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_png",b"image_png","request",b"request"]) -> None: ...
global___UiDetectionRequest = UiDetectionRequest

class DetectionRequest(google.protobuf.message.Message):
    """Detection type specifies what to detect in the image."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORD_DETECTION_REQUEST_FIELD_NUMBER: builtins.int
    TEXT_BLOCK_DETECTION_REQUEST_FIELD_NUMBER: builtins.int
    CUSTOM_ICON_DETECTION_REQUEST_FIELD_NUMBER: builtins.int
    @property
    def word_detection_request(self) -> global___WordDetectionRequest:
        """Detection type for word detection."""
        pass
    @property
    def text_block_detection_request(self) -> global___TextBlockDetectionRequest:
        """Detection type for text block detection."""
        pass
    @property
    def custom_icon_detection_request(self) -> global___CustomIconDetectionRequest:
        """Detection type for custom icon detection."""
        pass
    def __init__(self,
        *,
        word_detection_request : typing.Optional[global___WordDetectionRequest] = ...,
        text_block_detection_request : typing.Optional[global___TextBlockDetectionRequest] = ...,
        custom_icon_detection_request : typing.Optional[global___CustomIconDetectionRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["custom_icon_detection_request",b"custom_icon_detection_request","detection_request_type",b"detection_request_type","text_block_detection_request",b"text_block_detection_request","word_detection_request",b"word_detection_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["custom_icon_detection_request",b"custom_icon_detection_request","detection_request_type",b"detection_request_type","text_block_detection_request",b"text_block_detection_request","word_detection_request",b"word_detection_request"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["detection_request_type",b"detection_request_type"]) -> typing.Optional[typing_extensions.Literal["word_detection_request","text_block_detection_request","custom_icon_detection_request"]]: ...
global___DetectionRequest = DetectionRequest

class WordDetectionRequest(google.protobuf.message.Message):
    """Detection type for word detection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORD_FIELD_NUMBER: builtins.int
    word: typing.Text = ...
    """Required. The word to locate in the image."""

    def __init__(self,
        *,
        word : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["word",b"word"]) -> None: ...
global___WordDetectionRequest = WordDetectionRequest

class TextBlockDetectionRequest(google.protobuf.message.Message):
    """Detection type for text block detection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORDS_FIELD_NUMBER: builtins.int
    @property
    def words(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. The text block consisting a list of words to locate im the image."""
        pass
    def __init__(self,
        *,
        words : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["words",b"words"]) -> None: ...
global___TextBlockDetectionRequest = TextBlockDetectionRequest

class CustomIconDetectionRequest(google.protobuf.message.Message):
    """Detection type for custom icon detection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ICON_PNG_FIELD_NUMBER: builtins.int
    icon_png: builtins.bytes = ...
    """Required. Required field that represents an icon in PNG format."""

    def __init__(self,
        *,
        icon_png : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["icon_png",b"icon_png"]) -> None: ...
global___CustomIconDetectionRequest = CustomIconDetectionRequest

class UiDetectionResponse(google.protobuf.message.Message):
    """Response message for UI detection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BOUNDING_BOXES_FIELD_NUMBER: builtins.int
    @property
    def bounding_boxes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BoundingBox]:
        """Locations of matching UI elements."""
        pass
    def __init__(self,
        *,
        bounding_boxes : typing.Optional[typing.Iterable[global___BoundingBox]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_boxes",b"bounding_boxes"]) -> None: ...
global___UiDetectionResponse = UiDetectionResponse

class BoundingBox(google.protobuf.message.Message):
    """The location of a UI element.
    A bounding box is reprensented by its top-left point [left, top]
    and its bottom-right point [right, bottom].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TEXT_FIELD_NUMBER: builtins.int
    TOP_FIELD_NUMBER: builtins.int
    LEFT_FIELD_NUMBER: builtins.int
    BOTTOM_FIELD_NUMBER: builtins.int
    RIGHT_FIELD_NUMBER: builtins.int
    text: typing.Text = ...
    """The text found in the bounding box."""

    top: builtins.int = ...
    """The y-coordinate of the top-left point."""

    left: builtins.int = ...
    """The x-coordinate of the top-left point."""

    bottom: builtins.int = ...
    """The y-coordinate of the bottom-right point."""

    right: builtins.int = ...
    """The x-coordinate of the bottom-right point."""

    def __init__(self,
        *,
        text : typing.Text = ...,
        top : builtins.int = ...,
        left : builtins.int = ...,
        bottom : builtins.int = ...,
        right : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bottom",b"bottom","left",b"left","right",b"right","text",b"text","top",b"top"]) -> None: ...
global___BoundingBox = BoundingBox
