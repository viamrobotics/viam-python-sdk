"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
from ...... import proto
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetObjectPointCloudsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    MIN_POINTS_IN_PLANE_FIELD_NUMBER: builtins.int
    MIN_POINTS_IN_SEGMENT_FIELD_NUMBER: builtins.int
    CLUSTERING_RADIUS_MM_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    'Name of a camera'
    mime_type: typing.Text = ...
    'Requested MIME type of response'
    min_points_in_plane: builtins.int = ...
    'Minimum points in plane'
    min_points_in_segment: builtins.int = ...
    'Minimum points in segment'
    clustering_radius_mm: builtins.float = ...
    'Clustering radius in mm'

    def __init__(self, *, name: typing.Text=..., mime_type: typing.Text=..., min_points_in_plane: builtins.int=..., min_points_in_segment: builtins.int=..., clustering_radius_mm: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['clustering_radius_mm', b'clustering_radius_mm', 'mime_type', b'mime_type', 'min_points_in_plane', b'min_points_in_plane', 'min_points_in_segment', b'min_points_in_segment', 'name', b'name']) -> None:
        ...
global___GetObjectPointCloudsRequest = GetObjectPointCloudsRequest

class GetObjectPointCloudsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MIME_TYPE_FIELD_NUMBER: builtins.int
    OBJECTS_FIELD_NUMBER: builtins.int
    mime_type: typing.Text = ...
    'Actual MIME type of response'

    @property
    def objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[proto.api.common.v1.common_pb2.PointCloudObject]:
        """List of objects in the scene"""
        pass

    def __init__(self, *, mime_type: typing.Text=..., objects: typing.Optional[typing.Iterable[proto.api.common.v1.common_pb2.PointCloudObject]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mime_type', b'mime_type', 'objects', b'objects']) -> None:
        ...
global___GetObjectPointCloudsResponse = GetObjectPointCloudsResponse