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
import typing
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MoveRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    WORLD_STATE_FIELD_NUMBER: builtins.int
    CONSTRAINTS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def destination(self) -> common.v1.common_pb2.PoseInFrame:
        ...

    @property
    def component_name(self) -> common.v1.common_pb2.ResourceName:
        ...

    @property
    def world_state(self) -> common.v1.common_pb2.WorldState:
        ...

    @property
    def constraints(self) -> global___Constraints:
        ...

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., destination: common.v1.common_pb2.PoseInFrame | None=..., component_name: common.v1.common_pb2.ResourceName | None=..., world_state: common.v1.common_pb2.WorldState | None=..., constraints: global___Constraints | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_constraints', b'_constraints', '_world_state', b'_world_state', 'component_name', b'component_name', 'constraints', b'constraints', 'destination', b'destination', 'extra', b'extra', 'world_state', b'world_state']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_constraints', b'_constraints', '_world_state', b'_world_state', 'component_name', b'component_name', 'constraints', b'constraints', 'destination', b'destination', 'extra', b'extra', 'name', b'name', 'world_state', b'world_state']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_constraints', b'_constraints']) -> typing_extensions.Literal['constraints'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_world_state', b'_world_state']) -> typing_extensions.Literal['world_state'] | None:
        ...
global___MoveRequest = MoveRequest

@typing_extensions.final
class MoveResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool

    def __init__(self, *, success: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['success', b'success']) -> None:
        ...
global___MoveResponse = MoveResponse

@typing_extensions.final
class MoveSingleComponentRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    WORLD_STATE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def destination(self) -> common.v1.common_pb2.PoseInFrame:
        ...

    @property
    def component_name(self) -> common.v1.common_pb2.ResourceName:
        ...

    @property
    def world_state(self) -> common.v1.common_pb2.WorldState:
        ...

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., destination: common.v1.common_pb2.PoseInFrame | None=..., component_name: common.v1.common_pb2.ResourceName | None=..., world_state: common.v1.common_pb2.WorldState | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'component_name', b'component_name', 'destination', b'destination', 'extra', b'extra', 'world_state', b'world_state']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'component_name', b'component_name', 'destination', b'destination', 'extra', b'extra', 'name', b'name', 'world_state', b'world_state']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_world_state', b'_world_state']) -> typing_extensions.Literal['world_state'] | None:
        ...
global___MoveSingleComponentRequest = MoveSingleComponentRequest

@typing_extensions.final
class MoveSingleComponentResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool

    def __init__(self, *, success: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['success', b'success']) -> None:
        ...
global___MoveSingleComponentResponse = MoveSingleComponentResponse

@typing_extensions.final
class GetPoseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    DESTINATION_FRAME_FIELD_NUMBER: builtins.int
    SUPPLEMENTAL_TRANSFORMS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def component_name(self) -> common.v1.common_pb2.ResourceName:
        """the component whose pose is being requested"""
    destination_frame: builtins.str
    'the reference frame in which the component\'s pose\n    should be provided, if unset this defaults\n    to the "world" reference frame\n    '

    @property
    def supplemental_transforms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.Transform]:
        """pose information on any additional reference frames that are needed
        to compute the component's pose
        """

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., component_name: common.v1.common_pb2.ResourceName | None=..., destination_frame: builtins.str=..., supplemental_transforms: collections.abc.Iterable[common.v1.common_pb2.Transform] | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['component_name', b'component_name', 'extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['component_name', b'component_name', 'destination_frame', b'destination_frame', 'extra', b'extra', 'name', b'name', 'supplemental_transforms', b'supplemental_transforms']) -> None:
        ...
global___GetPoseRequest = GetPoseRequest

@typing_extensions.final
class GetPoseResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> common.v1.common_pb2.PoseInFrame:
        ...

    def __init__(self, *, pose: common.v1.common_pb2.PoseInFrame | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> None:
        ...
global___GetPoseResponse = GetPoseResponse

@typing_extensions.final
class Constraints(google.protobuf.message.Message):
    """Constraints specifies all enumerated constraints to be passed to Viam's motion planning, along with any optional parameters"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LINEAR_CONSTRAINT_FIELD_NUMBER: builtins.int
    ORIENTATION_CONSTRAINT_FIELD_NUMBER: builtins.int
    COLLISION_SPECIFICATION_FIELD_NUMBER: builtins.int

    @property
    def linear_constraint(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LinearConstraint]:
        """Typed message for a specific constraint"""

    @property
    def orientation_constraint(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OrientationConstraint]:
        ...

    @property
    def collision_specification(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CollisionSpecification]:
        """Arc constraint, Time constraint, and others will be added here when they are supported"""

    def __init__(self, *, linear_constraint: collections.abc.Iterable[global___LinearConstraint] | None=..., orientation_constraint: collections.abc.Iterable[global___OrientationConstraint] | None=..., collision_specification: collections.abc.Iterable[global___CollisionSpecification] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['collision_specification', b'collision_specification', 'linear_constraint', b'linear_constraint', 'orientation_constraint', b'orientation_constraint']) -> None:
        ...
global___Constraints = Constraints

@typing_extensions.final
class LinearConstraint(google.protobuf.message.Message):
    """LinearConstraint specifies that the component being moved should move linearly relative to its goal. It does not constrain the motion of components other than the `component_name` specified in motion.Move"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LINE_TOLERANCE_MM_FIELD_NUMBER: builtins.int
    ORIENTATION_TOLERANCE_DEGS_FIELD_NUMBER: builtins.int
    line_tolerance_mm: builtins.float
    'Max linear deviation from straight-line between start and goal, in mm.'
    orientation_tolerance_degs: builtins.float
    'Max allowable orientation deviation, in degrees, while on the shortest path between start / goal states'

    def __init__(self, *, line_tolerance_mm: builtins.float | None=..., orientation_tolerance_degs: builtins.float | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_line_tolerance_mm', b'_line_tolerance_mm', '_orientation_tolerance_degs', b'_orientation_tolerance_degs', 'line_tolerance_mm', b'line_tolerance_mm', 'orientation_tolerance_degs', b'orientation_tolerance_degs']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_line_tolerance_mm', b'_line_tolerance_mm', '_orientation_tolerance_degs', b'_orientation_tolerance_degs', 'line_tolerance_mm', b'line_tolerance_mm', 'orientation_tolerance_degs', b'orientation_tolerance_degs']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_line_tolerance_mm', b'_line_tolerance_mm']) -> typing_extensions.Literal['line_tolerance_mm'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_orientation_tolerance_degs', b'_orientation_tolerance_degs']) -> typing_extensions.Literal['orientation_tolerance_degs'] | None:
        ...
global___LinearConstraint = LinearConstraint

@typing_extensions.final
class OrientationConstraint(google.protobuf.message.Message):
    """OrientationConstraint specifies that the component being moved will not deviate its orientation beyond some threshold relative to the goal. It does not constrain the motion of components other than the `component_name` specified in motion.Move"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORIENTATION_TOLERANCE_DEGS_FIELD_NUMBER: builtins.int
    orientation_tolerance_degs: builtins.float
    'Max allowable orientation deviation, in degrees, while on the shortest path between start / goal states'

    def __init__(self, *, orientation_tolerance_degs: builtins.float | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_orientation_tolerance_degs', b'_orientation_tolerance_degs', 'orientation_tolerance_degs', b'orientation_tolerance_degs']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_orientation_tolerance_degs', b'_orientation_tolerance_degs', 'orientation_tolerance_degs', b'orientation_tolerance_degs']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_orientation_tolerance_degs', b'_orientation_tolerance_degs']) -> typing_extensions.Literal['orientation_tolerance_degs'] | None:
        ...
global___OrientationConstraint = OrientationConstraint

@typing_extensions.final
class CollisionSpecification(google.protobuf.message.Message):
    """CollisionSpecification is used to selectively apply obstacle avoidance to specific parts of the robot"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AllowedFrameCollisions(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        FRAME1_FIELD_NUMBER: builtins.int
        FRAME2_FIELD_NUMBER: builtins.int
        frame1: builtins.str
        frame2: builtins.str

        def __init__(self, *, frame1: builtins.str=..., frame2: builtins.str=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['frame1', b'frame1', 'frame2', b'frame2']) -> None:
            ...
    ALLOWS_FIELD_NUMBER: builtins.int

    @property
    def allows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CollisionSpecification.AllowedFrameCollisions]:
        """Pairs of frame which should be allowed to collide with one another"""

    def __init__(self, *, allows: collections.abc.Iterable[global___CollisionSpecification.AllowedFrameCollisions] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['allows', b'allows']) -> None:
        ...
global___CollisionSpecification = CollisionSpecification