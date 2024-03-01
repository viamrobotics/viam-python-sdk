"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
from .... import common
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetPosesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    BODY_NAMES_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of the pose tracker'

    @property
    def body_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of the bodies whose poses are being requested. In the event
        this parameter is not supplied or is an empty list, all available
        poses are returned
        """

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., body_names: collections.abc.Iterable[builtins.str] | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['body_names', b'body_names', 'extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetPosesRequest = GetPosesRequest

@typing_extensions.final
class GetPosesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class BodyPosesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> common.v1.common_pb2.PoseInFrame:
            ...

        def __init__(self, *, key: builtins.str=..., value: common.v1.common_pb2.PoseInFrame | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    BODY_POSES_FIELD_NUMBER: builtins.int

    @property
    def body_poses(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, common.v1.common_pb2.PoseInFrame]:
        """Mapping of each body name to the pose representing the center of the body."""

    def __init__(self, *, body_poses: collections.abc.Mapping[builtins.str, common.v1.common_pb2.PoseInFrame] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['body_poses', b'body_poses']) -> None:
        ...
global___GetPosesResponse = GetPosesResponse