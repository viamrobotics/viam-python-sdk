"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
from .... import common
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Format:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Format.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FORMAT_UNSPECIFIED: _Format.ValueType
    FORMAT_RAW_RGBA: _Format.ValueType
    FORMAT_RAW_DEPTH: _Format.ValueType
    FORMAT_JPEG: _Format.ValueType
    FORMAT_PNG: _Format.ValueType

class Format(_Format, metaclass=_FormatEnumTypeWrapper):
    ...
FORMAT_UNSPECIFIED: Format.ValueType
FORMAT_RAW_RGBA: Format.ValueType
FORMAT_RAW_DEPTH: Format.ValueType
FORMAT_JPEG: Format.ValueType
FORMAT_PNG: Format.ValueType
global___Format = Format

@typing_extensions.final
class GetImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a camera'
    mime_type: builtins.str
    'Requested MIME type of response'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., mime_type: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'mime_type', b'mime_type', 'name', b'name']) -> None:
        ...
global___GetImageRequest = GetImageRequest

@typing_extensions.final
class GetImageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MIME_TYPE_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    mime_type: builtins.str
    'Actual MIME type of response'
    image: builtins.bytes
    'Frame in bytes'

    def __init__(self, *, mime_type: builtins.str=..., image: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['image', b'image', 'mime_type', b'mime_type']) -> None:
        ...
global___GetImageResponse = GetImageResponse

@typing_extensions.final
class GetImagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a camera'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetImagesRequest = GetImagesRequest

@typing_extensions.final
class GetImagesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGES_FIELD_NUMBER: builtins.int
    RESPONSE_METADATA_FIELD_NUMBER: builtins.int

    @property
    def images(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Image]:
        """list of images returned from the camera system"""

    @property
    def response_metadata(self) -> common.v1.common_pb2.ResponseMetadata:
        """contains timestamp data"""

    def __init__(self, *, images: collections.abc.Iterable[global___Image] | None=..., response_metadata: common.v1.common_pb2.ResponseMetadata | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['response_metadata', b'response_metadata']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['images', b'images', 'response_metadata', b'response_metadata']) -> None:
        ...
global___GetImagesResponse = GetImagesResponse

@typing_extensions.final
class Image(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SOURCE_NAME_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    source_name: builtins.str
    'the name of the sensor where the image came from'
    format: global___Format.ValueType
    'format of the response image bytes'
    image: builtins.bytes
    'image in bytes'

    def __init__(self, *, source_name: builtins.str=..., format: global___Format.ValueType=..., image: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['format', b'format', 'image', b'image', 'source_name', b'source_name']) -> None:
        ...
global___Image = Image

@typing_extensions.final
class RenderFrameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a camera'
    mime_type: builtins.str
    'Requested MIME type of response'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., mime_type: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'mime_type', b'mime_type', 'name', b'name']) -> None:
        ...
global___RenderFrameRequest = RenderFrameRequest

@typing_extensions.final
class GetPointCloudRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a camera'
    mime_type: builtins.str
    'Requested MIME type of response'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., mime_type: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'mime_type', b'mime_type', 'name', b'name']) -> None:
        ...
global___GetPointCloudRequest = GetPointCloudRequest

@typing_extensions.final
class GetPointCloudResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MIME_TYPE_FIELD_NUMBER: builtins.int
    POINT_CLOUD_FIELD_NUMBER: builtins.int
    mime_type: builtins.str
    'Actual MIME type of response'
    point_cloud: builtins.bytes
    'Frame in bytes'

    def __init__(self, *, mime_type: builtins.str=..., point_cloud: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mime_type', b'mime_type', 'point_cloud', b'point_cloud']) -> None:
        ...
global___GetPointCloudResponse = GetPointCloudResponse

@typing_extensions.final
class GetPropertiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a camera'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetPropertiesRequest = GetPropertiesRequest

@typing_extensions.final
class GetPropertiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUPPORTS_PCD_FIELD_NUMBER: builtins.int
    INTRINSIC_PARAMETERS_FIELD_NUMBER: builtins.int
    DISTORTION_PARAMETERS_FIELD_NUMBER: builtins.int
    supports_pcd: builtins.bool
    'A boolean property determining whether the camera supports the return of pointcloud data'

    @property
    def intrinsic_parameters(self) -> global___IntrinsicParameters:
        """Parameters for doing a perspective of a 3D scene to a 2D plane
        If camera does not provide intrinsic parameters, leave the field empty
        Initializing the parameters with 0-values is considered an error
        """

    @property
    def distortion_parameters(self) -> global___DistortionParameters:
        """Parameters for modeling lens distortion in cameras
        If camera does not provide distortion parameters, leave the field empty
        Initializing the parameters with 0-values is considered an error
        """

    def __init__(self, *, supports_pcd: builtins.bool=..., intrinsic_parameters: global___IntrinsicParameters | None=..., distortion_parameters: global___DistortionParameters | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['distortion_parameters', b'distortion_parameters', 'intrinsic_parameters', b'intrinsic_parameters']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['distortion_parameters', b'distortion_parameters', 'intrinsic_parameters', b'intrinsic_parameters', 'supports_pcd', b'supports_pcd']) -> None:
        ...
global___GetPropertiesResponse = GetPropertiesResponse

@typing_extensions.final
class Webcams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WEBCAMS_FIELD_NUMBER: builtins.int

    @property
    def webcams(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Webcam]:
        ...

    def __init__(self, *, webcams: collections.abc.Iterable[global___Webcam] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['webcams', b'webcams']) -> None:
        ...
global___Webcams = Webcams

@typing_extensions.final
class Webcam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LABEL_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    label: builtins.str
    'Camera driver label (for internal use only)'
    status: builtins.str
    'Camera driver status'

    @property
    def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Property]:
        """Camera properties"""
    name: builtins.str
    'Camera human-readable driver name'
    id: builtins.str
    'Camera unique identifier'

    def __init__(self, *, label: builtins.str=..., status: builtins.str=..., properties: collections.abc.Iterable[global___Property] | None=..., name: builtins.str=..., id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'label', b'label', 'name', b'name', 'properties', b'properties', 'status', b'status']) -> None:
        ...
global___Webcam = Webcam

@typing_extensions.final
class Property(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WIDTH_PX_FIELD_NUMBER: builtins.int
    HEIGHT_PX_FIELD_NUMBER: builtins.int
    FRAME_FORMAT_FIELD_NUMBER: builtins.int
    FRAME_RATE_FIELD_NUMBER: builtins.int
    width_px: builtins.int
    'Video resolution width in px'
    height_px: builtins.int
    'Video resolution height in px'
    frame_format: builtins.str
    'Video frame format'
    frame_rate: builtins.float
    'Video frame rate in fps'

    def __init__(self, *, width_px: builtins.int=..., height_px: builtins.int=..., frame_format: builtins.str=..., frame_rate: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['frame_format', b'frame_format', 'frame_rate', b'frame_rate', 'height_px', b'height_px', 'width_px', b'width_px']) -> None:
        ...
global___Property = Property

@typing_extensions.final
class IntrinsicParameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WIDTH_PX_FIELD_NUMBER: builtins.int
    HEIGHT_PX_FIELD_NUMBER: builtins.int
    FOCAL_X_PX_FIELD_NUMBER: builtins.int
    FOCAL_Y_PX_FIELD_NUMBER: builtins.int
    CENTER_X_PX_FIELD_NUMBER: builtins.int
    CENTER_Y_PX_FIELD_NUMBER: builtins.int
    width_px: builtins.int
    height_px: builtins.int
    focal_x_px: builtins.float
    focal_y_px: builtins.float
    center_x_px: builtins.float
    center_y_px: builtins.float

    def __init__(self, *, width_px: builtins.int=..., height_px: builtins.int=..., focal_x_px: builtins.float=..., focal_y_px: builtins.float=..., center_x_px: builtins.float=..., center_y_px: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['center_x_px', b'center_x_px', 'center_y_px', b'center_y_px', 'focal_x_px', b'focal_x_px', 'focal_y_px', b'focal_y_px', 'height_px', b'height_px', 'width_px', b'width_px']) -> None:
        ...
global___IntrinsicParameters = IntrinsicParameters

@typing_extensions.final
class DistortionParameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODEL_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    model: builtins.str

    @property
    def parameters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        ...

    def __init__(self, *, model: builtins.str=..., parameters: collections.abc.Iterable[builtins.float] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['model', b'model', 'parameters', b'parameters']) -> None:
        ...
global___DistortionParameters = DistortionParameters
