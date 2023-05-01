"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
from .... import common
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetPositionRequest = GetPositionRequest

@typing_extensions.final
class GetPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int
    COMPONENT_REFERENCE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> common.v1.common_pb2.Pose:
        """Current position of the specified component in the SLAM Map"""
    component_reference: builtins.str
    'This is usually the name of the camera that is in the SLAM config'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional information in the response"""

    def __init__(self, *, pose: common.v1.common_pb2.Pose | None=..., component_reference: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra', 'pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['component_reference', b'component_reference', 'extra', b'extra', 'pose', b'pose']) -> None:
        ...
global___GetPositionResponse = GetPositionResponse

@typing_extensions.final
class GetPointCloudMapRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetPointCloudMapRequest = GetPointCloudMapRequest

@typing_extensions.final
class GetPointCloudMapResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINT_CLOUD_PCD_CHUNK_FIELD_NUMBER: builtins.int
    point_cloud_pcd_chunk: builtins.bytes
    'One chunk of the PointCloud.\n    For a given GetPointCloudMap request, concatenating all\n    GetPointCloudMapResponse.point_cloud_pcd_chunk values in the\n    order received result in the complete pointcloud in standard PCD\n    format where XY is the ground plane and positive Z is up, following\n    the Right Hand Rule.\n\n    Read more about the pointcloud format here:\n    https://pointclouds.org/documentation/tutorials/pcd_file_format.html\n\n    Viam expects pointcloud data with fields "x y z" or "x y z rgb", and for\n    this to be specified in the pointcloud header in the FIELDS entry. If color\n    data is included in the pointcloud, Viam\'s services assume that the color\n    value encodes a confidence score for that data point. Viam expects the\n    confidence score to be encoded in the blue parameter of the RGB value, on a\n    scale from 1-100.\n    '

    def __init__(self, *, point_cloud_pcd_chunk: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['point_cloud_pcd_chunk', b'point_cloud_pcd_chunk']) -> None:
        ...
global___GetPointCloudMapResponse = GetPointCloudMapResponse

@typing_extensions.final
class GetInternalStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetInternalStateRequest = GetInternalStateRequest

@typing_extensions.final
class GetInternalStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INTERNAL_STATE_CHUNK_FIELD_NUMBER: builtins.int
    internal_state_chunk: builtins.bytes
    'Chunk of the internal state of the SLAM algorithm required to continue\n    mapping/localization\n    '

    def __init__(self, *, internal_state_chunk: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['internal_state_chunk', b'internal_state_chunk']) -> None:
        ...
global___GetInternalStateResponse = GetInternalStateResponse