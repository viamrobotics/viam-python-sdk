"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
from .... import common
from .... import component
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetDetectionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the vision service'
    image: builtins.bytes
    'the image, encoded as bytes'
    width: builtins.int
    'the width of the image'
    height: builtins.int
    'the height of the image'
    mime_type: builtins.str
    'the actual MIME type of image'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., image: builtins.bytes=..., width: builtins.int=..., height: builtins.int=..., mime_type: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'height', b'height', 'image', b'image', 'mime_type', b'mime_type', 'name', b'name', 'width', b'width']) -> None:
        ...
global___GetDetectionsRequest = GetDetectionsRequest

@typing.final
class GetDetectionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DETECTIONS_FIELD_NUMBER: builtins.int

    @property
    def detections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Detection]:
        """the bounding boxes and labels"""

    def __init__(self, *, detections: collections.abc.Iterable[global___Detection] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['detections', b'detections']) -> None:
        ...
global___GetDetectionsResponse = GetDetectionsResponse

@typing.final
class GetDetectionsFromCameraRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CAMERA_NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the vision service'
    camera_name: builtins.str
    'name of camera source to use as input'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: builtins.str=..., camera_name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['camera_name', b'camera_name', 'extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetDetectionsFromCameraRequest = GetDetectionsFromCameraRequest

@typing.final
class GetDetectionsFromCameraResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DETECTIONS_FIELD_NUMBER: builtins.int

    @property
    def detections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Detection]:
        """the bounding boxes and labels"""

    def __init__(self, *, detections: collections.abc.Iterable[global___Detection] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['detections', b'detections']) -> None:
        ...
global___GetDetectionsFromCameraResponse = GetDetectionsFromCameraResponse

@typing.final
class Detection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    X_MIN_FIELD_NUMBER: builtins.int
    Y_MIN_FIELD_NUMBER: builtins.int
    X_MAX_FIELD_NUMBER: builtins.int
    Y_MAX_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    CLASS_NAME_FIELD_NUMBER: builtins.int
    X_MIN_NORMALIZED_FIELD_NUMBER: builtins.int
    Y_MIN_NORMALIZED_FIELD_NUMBER: builtins.int
    X_MAX_NORMALIZED_FIELD_NUMBER: builtins.int
    Y_MAX_NORMALIZED_FIELD_NUMBER: builtins.int
    x_min: builtins.int
    'the four corners of the box'
    y_min: builtins.int
    x_max: builtins.int
    y_max: builtins.int
    confidence: builtins.float
    'the confidence of the detection'
    class_name: builtins.str
    'label associated with the detected object'
    x_min_normalized: builtins.float
    'the four corners of the box, in proportion to the respective image dimension'
    y_min_normalized: builtins.float
    x_max_normalized: builtins.float
    y_max_normalized: builtins.float

    def __init__(self, *, x_min: builtins.int | None=..., y_min: builtins.int | None=..., x_max: builtins.int | None=..., y_max: builtins.int | None=..., confidence: builtins.float=..., class_name: builtins.str=..., x_min_normalized: builtins.float | None=..., y_min_normalized: builtins.float | None=..., x_max_normalized: builtins.float | None=..., y_max_normalized: builtins.float | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_x_max', b'_x_max', '_x_max_normalized', b'_x_max_normalized', '_x_min', b'_x_min', '_x_min_normalized', b'_x_min_normalized', '_y_max', b'_y_max', '_y_max_normalized', b'_y_max_normalized', '_y_min', b'_y_min', '_y_min_normalized', b'_y_min_normalized', 'x_max', b'x_max', 'x_max_normalized', b'x_max_normalized', 'x_min', b'x_min', 'x_min_normalized', b'x_min_normalized', 'y_max', b'y_max', 'y_max_normalized', b'y_max_normalized', 'y_min', b'y_min', 'y_min_normalized', b'y_min_normalized']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_x_max', b'_x_max', '_x_max_normalized', b'_x_max_normalized', '_x_min', b'_x_min', '_x_min_normalized', b'_x_min_normalized', '_y_max', b'_y_max', '_y_max_normalized', b'_y_max_normalized', '_y_min', b'_y_min', '_y_min_normalized', b'_y_min_normalized', 'class_name', b'class_name', 'confidence', b'confidence', 'x_max', b'x_max', 'x_max_normalized', b'x_max_normalized', 'x_min', b'x_min', 'x_min_normalized', b'x_min_normalized', 'y_max', b'y_max', 'y_max_normalized', b'y_max_normalized', 'y_min', b'y_min', 'y_min_normalized', b'y_min_normalized']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_x_max', b'_x_max']) -> typing.Literal['x_max'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_x_max_normalized', b'_x_max_normalized']) -> typing.Literal['x_max_normalized'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_x_min', b'_x_min']) -> typing.Literal['x_min'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_x_min_normalized', b'_x_min_normalized']) -> typing.Literal['x_min_normalized'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_y_max', b'_y_max']) -> typing.Literal['y_max'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_y_max_normalized', b'_y_max_normalized']) -> typing.Literal['y_max_normalized'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_y_min', b'_y_min']) -> typing.Literal['y_min'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_y_min_normalized', b'_y_min_normalized']) -> typing.Literal['y_min_normalized'] | None:
        ...
global___Detection = Detection

@typing.final
class GetClassificationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    N_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the vision service'
    image: builtins.bytes
    'the image encoded as bytes'
    width: builtins.int
    'the width of the image'
    height: builtins.int
    'the height of the image'
    mime_type: builtins.str
    'the actual MIME type of image'
    n: builtins.int
    'the number of classifications desired'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., image: builtins.bytes=..., width: builtins.int=..., height: builtins.int=..., mime_type: builtins.str=..., n: builtins.int=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'height', b'height', 'image', b'image', 'mime_type', b'mime_type', 'n', b'n', 'name', b'name', 'width', b'width']) -> None:
        ...
global___GetClassificationsRequest = GetClassificationsRequest

@typing.final
class GetClassificationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLASSIFICATIONS_FIELD_NUMBER: builtins.int

    @property
    def classifications(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Classification]:
        ...

    def __init__(self, *, classifications: collections.abc.Iterable[global___Classification] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['classifications', b'classifications']) -> None:
        ...
global___GetClassificationsResponse = GetClassificationsResponse

@typing.final
class GetClassificationsFromCameraRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CAMERA_NAME_FIELD_NUMBER: builtins.int
    N_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the vision service'
    camera_name: builtins.str
    'the image encoded as bytes'
    n: builtins.int
    'the number of classifications desired'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., camera_name: builtins.str=..., n: builtins.int=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['camera_name', b'camera_name', 'extra', b'extra', 'n', b'n', 'name', b'name']) -> None:
        ...
global___GetClassificationsFromCameraRequest = GetClassificationsFromCameraRequest

@typing.final
class GetClassificationsFromCameraResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLASSIFICATIONS_FIELD_NUMBER: builtins.int

    @property
    def classifications(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Classification]:
        ...

    def __init__(self, *, classifications: collections.abc.Iterable[global___Classification] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['classifications', b'classifications']) -> None:
        ...
global___GetClassificationsFromCameraResponse = GetClassificationsFromCameraResponse

@typing.final
class Classification(google.protobuf.message.Message):
    """the general form of the output from a classifier"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLASS_NAME_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    class_name: builtins.str
    'the class name'
    confidence: builtins.float
    'the confidence score of the classification'

    def __init__(self, *, class_name: builtins.str=..., confidence: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['class_name', b'class_name', 'confidence', b'confidence']) -> None:
        ...
global___Classification = Classification

@typing.final
class GetObjectPointCloudsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CAMERA_NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    camera_name: builtins.str
    'Name of a camera'
    mime_type: builtins.str
    'Requested MIME type of response'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., camera_name: builtins.str=..., mime_type: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['camera_name', b'camera_name', 'extra', b'extra', 'mime_type', b'mime_type', 'name', b'name']) -> None:
        ...
global___GetObjectPointCloudsRequest = GetObjectPointCloudsRequest

@typing.final
class GetObjectPointCloudsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MIME_TYPE_FIELD_NUMBER: builtins.int
    OBJECTS_FIELD_NUMBER: builtins.int
    mime_type: builtins.str
    'Actual MIME type of response'

    @property
    def objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.PointCloudObject]:
        """List of objects in the scene"""

    def __init__(self, *, mime_type: builtins.str=..., objects: collections.abc.Iterable[common.v1.common_pb2.PointCloudObject] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['mime_type', b'mime_type', 'objects', b'objects']) -> None:
        ...
global___GetObjectPointCloudsResponse = GetObjectPointCloudsResponse

@typing.final
class GetPropertiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the vision service'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetPropertiesRequest = GetPropertiesRequest

@typing.final
class CaptureAllFromCameraRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CAMERA_NAME_FIELD_NUMBER: builtins.int
    RETURN_IMAGE_FIELD_NUMBER: builtins.int
    RETURN_CLASSIFICATIONS_FIELD_NUMBER: builtins.int
    RETURN_DETECTIONS_FIELD_NUMBER: builtins.int
    RETURN_OBJECT_POINT_CLOUDS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'name of the vision service'
    camera_name: builtins.str
    'name of camera source to use as input'
    return_image: builtins.bool
    'whether or not including the image in the response'
    return_classifications: builtins.bool
    'whether or not including classifications in the response'
    return_detections: builtins.bool
    'whether or not including detections in the response'
    return_object_point_clouds: builtins.bool
    'whether or not including pcd in the response'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: builtins.str=..., camera_name: builtins.str=..., return_image: builtins.bool=..., return_classifications: builtins.bool=..., return_detections: builtins.bool=..., return_object_point_clouds: builtins.bool=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['camera_name', b'camera_name', 'extra', b'extra', 'name', b'name', 'return_classifications', b'return_classifications', 'return_detections', b'return_detections', 'return_image', b'return_image', 'return_object_point_clouds', b'return_object_point_clouds']) -> None:
        ...
global___CaptureAllFromCameraRequest = CaptureAllFromCameraRequest

@typing.final
class CaptureAllFromCameraResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGE_FIELD_NUMBER: builtins.int
    DETECTIONS_FIELD_NUMBER: builtins.int
    CLASSIFICATIONS_FIELD_NUMBER: builtins.int
    OBJECTS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int

    @property
    def image(self) -> component.camera.v1.camera_pb2.Image:
        ...

    @property
    def detections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Detection]:
        ...

    @property
    def classifications(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Classification]:
        ...

    @property
    def objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.PointCloudObject]:
        ...

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, image: component.camera.v1.camera_pb2.Image | None=..., detections: collections.abc.Iterable[global___Detection] | None=..., classifications: collections.abc.Iterable[global___Classification] | None=..., objects: collections.abc.Iterable[common.v1.common_pb2.PointCloudObject] | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra', 'image', b'image']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['classifications', b'classifications', 'detections', b'detections', 'extra', b'extra', 'image', b'image', 'objects', b'objects']) -> None:
        ...
global___CaptureAllFromCameraResponse = CaptureAllFromCameraResponse

@typing.final
class GetPropertiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLASSIFICATIONS_SUPPORTED_FIELD_NUMBER: builtins.int
    DETECTIONS_SUPPORTED_FIELD_NUMBER: builtins.int
    OBJECT_POINT_CLOUDS_SUPPORTED_FIELD_NUMBER: builtins.int
    classifications_supported: builtins.bool
    'whether or not classifactions are supported by the vision service'
    detections_supported: builtins.bool
    'whether or not detections are supported by the vision service'
    object_point_clouds_supported: builtins.bool
    'whether or not 3d segmentation is supported by the vision service'

    def __init__(self, *, classifications_supported: builtins.bool=..., detections_supported: builtins.bool=..., object_point_clouds_supported: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['classifications_supported', b'classifications_supported', 'detections_supported', b'detections_supported', 'object_point_clouds_supported', b'object_point_clouds_supported']) -> None:
        ...
global___GetPropertiesResponse = GetPropertiesResponse