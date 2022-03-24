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

class FrameConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    POSE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...

    @property
    def pose(self) -> proto.api.common.v1.common_pb2.Pose:
        ...

    def __init__(self, *, parent: typing.Text=..., pose: typing.Optional[proto.api.common.v1.common_pb2.Pose]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['parent', b'parent', 'pose', b'pose']) -> None:
        ...
global___FrameConfig = FrameConfig

class Config(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FRAME_CONFIG_FIELD_NUMBER: builtins.int
    MODEL_JSON_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    @property
    def frame_config(self) -> global___FrameConfig:
        ...
    model_json: builtins.bytes = ...

    def __init__(self, *, name: typing.Text=..., frame_config: typing.Optional[global___FrameConfig]=..., model_json: builtins.bytes=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['frame_config', b'frame_config']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['frame_config', b'frame_config', 'model_json', b'model_json', 'name', b'name']) -> None:
        ...
global___Config = Config

class ConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___ConfigRequest = ConfigRequest

class ConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FRAME_SYSTEM_CONFIGS_FIELD_NUMBER: builtins.int

    @property
    def frame_system_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Config]:
        ...

    def __init__(self, *, frame_system_configs: typing.Optional[typing.Iterable[global___Config]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['frame_system_configs', b'frame_system_configs']) -> None:
        ...
global___ConfigResponse = ConfigResponse

class TransformPoseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOURCE_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int

    @property
    def source(self) -> proto.api.common.v1.common_pb2.PoseInFrame:
        ...
    destination: typing.Text = ...

    def __init__(self, *, source: typing.Optional[proto.api.common.v1.common_pb2.PoseInFrame]=..., destination: typing.Text=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['source', b'source']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['destination', b'destination', 'source', b'source']) -> None:
        ...
global___TransformPoseRequest = TransformPoseRequest

class TransformPoseResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    POSE_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> proto.api.common.v1.common_pb2.PoseInFrame:
        ...

    def __init__(self, *, pose: typing.Optional[proto.api.common.v1.common_pb2.PoseInFrame]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> None:
        ...
global___TransformPoseResponse = TransformPoseResponse