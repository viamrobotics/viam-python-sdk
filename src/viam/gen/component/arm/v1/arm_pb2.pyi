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
class GetEndPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of an arm'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetEndPositionRequest = GetEndPositionRequest

@typing_extensions.final
class GetEndPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> common.v1.common_pb2.Pose:
        """Returns 6d pose of the end effector relative to the base, represented by X,Y,Z coordinates which express
        millimeters and theta, ox, oy, oz coordinates which express an orientation vector
        """

    def __init__(self, *, pose: common.v1.common_pb2.Pose | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> None:
        ...
global___GetEndPositionResponse = GetEndPositionResponse

@typing_extensions.final
class JointPositions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUES_FIELD_NUMBER: builtins.int

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """A list of joint positions. Rotations values are in degrees, translational values in mm.
        The numbers are ordered spatially from the base toward the end effector
        This is used in GetJointPositionsResponse and MoveToJointPositionsRequest
        """

    def __init__(self, *, values: collections.abc.Iterable[builtins.float] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['values', b'values']) -> None:
        ...
global___JointPositions = JointPositions

@typing_extensions.final
class GetJointPositionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of an arm'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetJointPositionsRequest = GetJointPositionsRequest

@typing_extensions.final
class GetJointPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSITIONS_FIELD_NUMBER: builtins.int

    @property
    def positions(self) -> global___JointPositions:
        """a list JointPositions"""

    def __init__(self, *, positions: global___JointPositions | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['positions', b'positions']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['positions', b'positions']) -> None:
        ...
global___GetJointPositionsResponse = GetJointPositionsResponse

@typing_extensions.final
class MoveToPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    TO_FIELD_NUMBER: builtins.int
    WORLD_STATE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of an arm'

    @property
    def to(self) -> common.v1.common_pb2.Pose:
        ...

    @property
    def world_state(self) -> common.v1.common_pb2.WorldState:
        ...

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., to: common.v1.common_pb2.Pose | None=..., world_state: common.v1.common_pb2.WorldState | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'extra', b'extra', 'to', b'to', 'world_state', b'world_state']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'extra', b'extra', 'name', b'name', 'to', b'to', 'world_state', b'world_state']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_world_state', b'_world_state']) -> typing_extensions.Literal['world_state'] | None:
        ...
global___MoveToPositionRequest = MoveToPositionRequest

@typing_extensions.final
class MoveToPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___MoveToPositionResponse = MoveToPositionResponse

@typing_extensions.final
class MoveToJointPositionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    POSITIONS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of an arm'

    @property
    def positions(self) -> global___JointPositions:
        """A list of joint positions
        There should be 1 entry in the list per joint DOF, ordered spatially from the base toward the end effector
        """

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., positions: global___JointPositions | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra', 'positions', b'positions']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'positions', b'positions']) -> None:
        ...
global___MoveToJointPositionsRequest = MoveToJointPositionsRequest

@typing_extensions.final
class MoveToJointPositionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___MoveToJointPositionsResponse = MoveToJointPositionsResponse

@typing_extensions.final
class StopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of an arm'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___StopRequest = StopRequest

@typing_extensions.final
class StopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___StopResponse = StopResponse

@typing_extensions.final
class Status(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    END_POSITION_FIELD_NUMBER: builtins.int
    JOINT_POSITIONS_FIELD_NUMBER: builtins.int
    IS_MOVING_FIELD_NUMBER: builtins.int

    @property
    def end_position(self) -> common.v1.common_pb2.Pose:
        ...

    @property
    def joint_positions(self) -> global___JointPositions:
        ...
    is_moving: builtins.bool

    def __init__(self, *, end_position: common.v1.common_pb2.Pose | None=..., joint_positions: global___JointPositions | None=..., is_moving: builtins.bool=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['end_position', b'end_position', 'joint_positions', b'joint_positions']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['end_position', b'end_position', 'is_moving', b'is_moving', 'joint_positions', b'joint_positions']) -> None:
        ...
global___Status = Status

@typing_extensions.final
class IsMovingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___IsMovingRequest = IsMovingRequest

@typing_extensions.final
class IsMovingResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_MOVING_FIELD_NUMBER: builtins.int
    is_moving: builtins.bool

    def __init__(self, *, is_moving: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['is_moving', b'is_moving']) -> None:
        ...
global___IsMovingResponse = IsMovingResponse