"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import proto.api.common.v1.common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CameraServiceFrameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a camera"""

    mime_type: typing.Text = ...
    """Requested MIME type of response"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        mime_type : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mime_type",b"mime_type","name",b"name"]) -> None: ...
global___CameraServiceFrameRequest = CameraServiceFrameRequest

class CameraServiceFrameResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MIME_TYPE_FIELD_NUMBER: builtins.int
    FRAME_FIELD_NUMBER: builtins.int
    DIM_X_FIELD_NUMBER: builtins.int
    DIM_Y_FIELD_NUMBER: builtins.int
    mime_type: typing.Text = ...
    """Actual MIME type of response"""

    frame: builtins.bytes = ...
    """Frame in bytes"""

    dim_x: builtins.int = ...
    """Width of frame"""

    dim_y: builtins.int = ...
    """Height of frame"""

    def __init__(self,
        *,
        mime_type : typing.Text = ...,
        frame : builtins.bytes = ...,
        dim_x : builtins.int = ...,
        dim_y : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dim_x",b"dim_x","dim_y",b"dim_y","frame",b"frame","mime_type",b"mime_type"]) -> None: ...
global___CameraServiceFrameResponse = CameraServiceFrameResponse

class CameraServiceRenderFrameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a camera"""

    mime_type: typing.Text = ...
    """Requested MIME type of response"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        mime_type : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mime_type",b"mime_type","name",b"name"]) -> None: ...
global___CameraServiceRenderFrameRequest = CameraServiceRenderFrameRequest

class CameraServicePointCloudRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a camera"""

    mime_type: typing.Text = ...
    """Requested MIME type of response"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        mime_type : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mime_type",b"mime_type","name",b"name"]) -> None: ...
global___CameraServicePointCloudRequest = CameraServicePointCloudRequest

class CameraServicePointCloudResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MIME_TYPE_FIELD_NUMBER: builtins.int
    FRAME_FIELD_NUMBER: builtins.int
    mime_type: typing.Text = ...
    """Actual MIME type of response"""

    frame: builtins.bytes = ...
    """Frame in bytes"""

    def __init__(self,
        *,
        mime_type : typing.Text = ...,
        frame : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["frame",b"frame","mime_type",b"mime_type"]) -> None: ...
global___CameraServicePointCloudResponse = CameraServicePointCloudResponse

class CameraServiceObjectPointCloudsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    MIN_POINTS_IN_PLANE_FIELD_NUMBER: builtins.int
    MIN_POINTS_IN_SEGMENT_FIELD_NUMBER: builtins.int
    CLUSTERING_RADIUS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of a camera"""

    mime_type: typing.Text = ...
    """Requested MIME type of response"""

    min_points_in_plane: builtins.int = ...
    """Minimum points in plane"""

    min_points_in_segment: builtins.int = ...
    """Minimum points in segment"""

    clustering_radius: builtins.float = ...
    """Clustering radius"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        mime_type : typing.Text = ...,
        min_points_in_plane : builtins.int = ...,
        min_points_in_segment : builtins.int = ...,
        clustering_radius : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["clustering_radius",b"clustering_radius","mime_type",b"mime_type","min_points_in_plane",b"min_points_in_plane","min_points_in_segment",b"min_points_in_segment","name",b"name"]) -> None: ...
global___CameraServiceObjectPointCloudsRequest = CameraServiceObjectPointCloudsRequest

class CameraServiceObjectPointCloudsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MIME_TYPE_FIELD_NUMBER: builtins.int
    OBJECTS_FIELD_NUMBER: builtins.int
    mime_type: typing.Text = ...
    """Actual MIME type of response"""

    @property
    def objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PointCloudObject]:
        """List of objects in the scene"""
        pass
    def __init__(self,
        *,
        mime_type : typing.Text = ...,
        objects : typing.Optional[typing.Iterable[global___PointCloudObject]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mime_type",b"mime_type","objects",b"objects"]) -> None: ...
global___CameraServiceObjectPointCloudsResponse = CameraServiceObjectPointCloudsResponse

class PointCloudObject(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FRAME_FIELD_NUMBER: builtins.int
    CENTER_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    frame: builtins.bytes = ...
    """Frame of object in bytes"""

    @property
    def center(self) -> proto.api.common.v1.common_pb2.Vector3:
        """Center of object in vector form"""
        pass
    @property
    def bounding_box(self) -> proto.api.common.v1.common_pb2.BoxGeometry:
        """Bounding box of object"""
        pass
    def __init__(self,
        *,
        frame : builtins.bytes = ...,
        center : typing.Optional[proto.api.common.v1.common_pb2.Vector3] = ...,
        bounding_box : typing.Optional[proto.api.common.v1.common_pb2.BoxGeometry] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","center",b"center"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","center",b"center","frame",b"frame"]) -> None: ...
global___PointCloudObject = PointCloudObject
