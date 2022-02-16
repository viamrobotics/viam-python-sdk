"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
from ..... import proto
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ObjectManipulationServiceDoGrabRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CAMERA_NAME_FIELD_NUMBER: builtins.int
    CAMERA_POINT_FIELD_NUMBER: builtins.int
    GRIPPER_NAME_FIELD_NUMBER: builtins.int
    ARM_NAME_FIELD_NUMBER: builtins.int
    camera_name: typing.Text = ...

    @property
    def camera_point(self) -> proto.api.common.v1.common_pb2.Vector3:
        ...
    gripper_name: typing.Text = ...
    arm_name: typing.Text = ...

    def __init__(self, *, camera_name: typing.Text=..., camera_point: typing.Optional[proto.api.common.v1.common_pb2.Vector3]=..., gripper_name: typing.Text=..., arm_name: typing.Text=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['camera_point', b'camera_point']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['arm_name', b'arm_name', 'camera_name', b'camera_name', 'camera_point', b'camera_point', 'gripper_name', b'gripper_name']) -> None:
        ...
global___ObjectManipulationServiceDoGrabRequest = ObjectManipulationServiceDoGrabRequest

class ObjectManipulationServiceDoGrabResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool = ...

    def __init__(self, *, success: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['success', b'success']) -> None:
        ...
global___ObjectManipulationServiceDoGrabResponse = ObjectManipulationServiceDoGrabResponse