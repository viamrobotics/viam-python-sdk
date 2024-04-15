"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
The following is a list of messages that are used across multiple resource subtypes"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.descriptor_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _KinematicsFileFormat:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _KinematicsFileFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KinematicsFileFormat.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    KINEMATICS_FILE_FORMAT_UNSPECIFIED: _KinematicsFileFormat.ValueType
    KINEMATICS_FILE_FORMAT_SVA: _KinematicsFileFormat.ValueType
    KINEMATICS_FILE_FORMAT_URDF: _KinematicsFileFormat.ValueType

class KinematicsFileFormat(_KinematicsFileFormat, metaclass=_KinematicsFileFormatEnumTypeWrapper):
    ...
KINEMATICS_FILE_FORMAT_UNSPECIFIED: KinematicsFileFormat.ValueType
KINEMATICS_FILE_FORMAT_SVA: KinematicsFileFormat.ValueType
KINEMATICS_FILE_FORMAT_URDF: KinematicsFileFormat.ValueType
global___KinematicsFileFormat = KinematicsFileFormat

@typing_extensions.final
class ResourceName(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMESPACE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SUBTYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    type: builtins.str
    subtype: builtins.str
    name: builtins.str

    def __init__(self, *, namespace: builtins.str=..., type: builtins.str=..., subtype: builtins.str=..., name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'namespace', b'namespace', 'subtype', b'subtype', 'type', b'type']) -> None:
        ...
global___ResourceName = ResourceName

@typing_extensions.final
class BoardStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AnalogsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___AnalogStatus:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___AnalogStatus | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    @typing_extensions.final
    class DigitalInterruptsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___DigitalInterruptStatus:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___DigitalInterruptStatus | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    ANALOGS_FIELD_NUMBER: builtins.int
    DIGITAL_INTERRUPTS_FIELD_NUMBER: builtins.int

    @property
    def analogs(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___AnalogStatus]:
        ...

    @property
    def digital_interrupts(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___DigitalInterruptStatus]:
        ...

    def __init__(self, *, analogs: collections.abc.Mapping[builtins.str, global___AnalogStatus] | None=..., digital_interrupts: collections.abc.Mapping[builtins.str, global___DigitalInterruptStatus] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['analogs', b'analogs', 'digital_interrupts', b'digital_interrupts']) -> None:
        ...
global___BoardStatus = BoardStatus

@typing_extensions.final
class AnalogStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    "Current value of the analog reader of a robot's board"

    def __init__(self, *, value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['value', b'value']) -> None:
        ...
global___AnalogStatus = AnalogStatus

@typing_extensions.final
class DigitalInterruptStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    "Current value of the digital interrupt of a robot's board"

    def __init__(self, *, value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['value', b'value']) -> None:
        ...
global___DigitalInterruptStatus = DigitalInterruptStatus

@typing_extensions.final
class Pose(google.protobuf.message.Message):
    """Pose is a combination of location and orientation.
    Location is expressed as distance which is represented by x , y, z coordinates. Orientation is expressed as an orientation vector which
    is represented by o_x, o_y, o_z and theta. The o_x, o_y, o_z coordinates represent the point on the cartesian unit sphere that the end of
    the arm is pointing to (with the origin as reference). That unit vector forms an axis around which theta rotates. This means that
    incrementing / decrementing theta will perform an inline rotation of the end effector.
    Theta is defined as rotation between two planes: the first being defined by the origin, the point (0,0,1), and the rx, ry, rz point, and the
    second being defined by the origin, the rx, ry, rz point and the local Z axis. Therefore, if theta is kept at zero as the north/south pole
    is circled, the Roll will correct itself to remain in-line.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    O_X_FIELD_NUMBER: builtins.int
    O_Y_FIELD_NUMBER: builtins.int
    O_Z_FIELD_NUMBER: builtins.int
    THETA_FIELD_NUMBER: builtins.int
    x: builtins.float
    'millimeters from the origin'
    y: builtins.float
    'millimeters from the origin'
    z: builtins.float
    'millimeters from the origin'
    o_x: builtins.float
    'z component of a vector defining axis of rotation'
    o_y: builtins.float
    'x component of a vector defining axis of rotation'
    o_z: builtins.float
    'y component of a vector defining axis of rotation'
    theta: builtins.float
    'degrees'

    def __init__(self, *, x: builtins.float=..., y: builtins.float=..., z: builtins.float=..., o_x: builtins.float=..., o_y: builtins.float=..., o_z: builtins.float=..., theta: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['o_x', b'o_x', 'o_y', b'o_y', 'o_z', b'o_z', 'theta', b'theta', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
        ...
global___Pose = Pose

@typing_extensions.final
class Orientation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    O_X_FIELD_NUMBER: builtins.int
    O_Y_FIELD_NUMBER: builtins.int
    O_Z_FIELD_NUMBER: builtins.int
    THETA_FIELD_NUMBER: builtins.int
    o_x: builtins.float
    'x component of a vector defining axis of rotation'
    o_y: builtins.float
    'y component of a vector defining axis of rotation'
    o_z: builtins.float
    'z component of a vector defining axis of rotation'
    theta: builtins.float
    'degrees'

    def __init__(self, *, o_x: builtins.float=..., o_y: builtins.float=..., o_z: builtins.float=..., theta: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['o_x', b'o_x', 'o_y', b'o_y', 'o_z', b'o_z', 'theta', b'theta']) -> None:
        ...
global___Orientation = Orientation

@typing_extensions.final
class PoseInFrame(google.protobuf.message.Message):
    """PoseInFrame contains a pose and the and the reference frame in which it was observed"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFERENCE_FRAME_FIELD_NUMBER: builtins.int
    POSE_FIELD_NUMBER: builtins.int
    reference_frame: builtins.str

    @property
    def pose(self) -> global___Pose:
        ...

    def __init__(self, *, reference_frame: builtins.str=..., pose: global___Pose | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose', 'reference_frame', b'reference_frame']) -> None:
        ...
global___PoseInFrame = PoseInFrame

@typing_extensions.final
class Vector3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float

    def __init__(self, *, x: builtins.float=..., y: builtins.float=..., z: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['x', b'x', 'y', b'y', 'z', b'z']) -> None:
        ...
global___Vector3 = Vector3

@typing_extensions.final
class Sphere(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RADIUS_MM_FIELD_NUMBER: builtins.int
    radius_mm: builtins.float

    def __init__(self, *, radius_mm: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['radius_mm', b'radius_mm']) -> None:
        ...
global___Sphere = Sphere

@typing_extensions.final
class Capsule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RADIUS_MM_FIELD_NUMBER: builtins.int
    LENGTH_MM_FIELD_NUMBER: builtins.int
    radius_mm: builtins.float
    length_mm: builtins.float

    def __init__(self, *, radius_mm: builtins.float=..., length_mm: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['length_mm', b'length_mm', 'radius_mm', b'radius_mm']) -> None:
        ...
global___Capsule = Capsule

@typing_extensions.final
class RectangularPrism(google.protobuf.message.Message):
    """RectangularPrism contains a Vector3 field corresponding to the X, Y, Z dimensions of the prism in mms
    These dimensions are with respect to the referenceframe in which the RectangularPrism is defined
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DIMS_MM_FIELD_NUMBER: builtins.int

    @property
    def dims_mm(self) -> global___Vector3:
        ...

    def __init__(self, *, dims_mm: global___Vector3 | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['dims_mm', b'dims_mm']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['dims_mm', b'dims_mm']) -> None:
        ...
global___RectangularPrism = RectangularPrism

@typing_extensions.final
class Geometry(google.protobuf.message.Message):
    """Geometry contains the dimensions of a given geometry and the pose of its center. The geometry is one of either a sphere or a box."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CENTER_FIELD_NUMBER: builtins.int
    SPHERE_FIELD_NUMBER: builtins.int
    BOX_FIELD_NUMBER: builtins.int
    CAPSULE_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int

    @property
    def center(self) -> global___Pose:
        """Pose of a geometries center point"""

    @property
    def sphere(self) -> global___Sphere:
        ...

    @property
    def box(self) -> global___RectangularPrism:
        ...

    @property
    def capsule(self) -> global___Capsule:
        ...
    label: builtins.str
    'Label of the geometry. If none supplied, will be an empty string.'

    def __init__(self, *, center: global___Pose | None=..., sphere: global___Sphere | None=..., box: global___RectangularPrism | None=..., capsule: global___Capsule | None=..., label: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['box', b'box', 'capsule', b'capsule', 'center', b'center', 'geometry_type', b'geometry_type', 'sphere', b'sphere']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['box', b'box', 'capsule', b'capsule', 'center', b'center', 'geometry_type', b'geometry_type', 'label', b'label', 'sphere', b'sphere']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['geometry_type', b'geometry_type']) -> typing_extensions.Literal['sphere', 'box', 'capsule'] | None:
        ...
global___Geometry = Geometry

@typing_extensions.final
class GeometriesInFrame(google.protobuf.message.Message):
    """GeometriesinFrame contains the dimensions of a given geometry, pose of its center point, and the reference frame by which it was
    observed.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFERENCE_FRAME_FIELD_NUMBER: builtins.int
    GEOMETRIES_FIELD_NUMBER: builtins.int
    reference_frame: builtins.str
    'Reference frame of the observer of the geometry'

    @property
    def geometries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Geometry]:
        """Dimensional type"""

    def __init__(self, *, reference_frame: builtins.str=..., geometries: collections.abc.Iterable[global___Geometry] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['geometries', b'geometries', 'reference_frame', b'reference_frame']) -> None:
        ...
global___GeometriesInFrame = GeometriesInFrame

@typing_extensions.final
class PointCloudObject(google.protobuf.message.Message):
    """PointCloudObject contains an image in bytes with point cloud data of all of the objects captured by a given observer as well as a
    repeated list of geometries which respresents the center point and geometry of each of the objects within the point cloud
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINT_CLOUD_FIELD_NUMBER: builtins.int
    GEOMETRIES_FIELD_NUMBER: builtins.int
    point_cloud: builtins.bytes
    'image frame expressed in bytes'

    @property
    def geometries(self) -> global___GeometriesInFrame:
        """volume of a given geometry"""

    def __init__(self, *, point_cloud: builtins.bytes=..., geometries: global___GeometriesInFrame | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['geometries', b'geometries']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['geometries', b'geometries', 'point_cloud', b'point_cloud']) -> None:
        ...
global___PointCloudObject = PointCloudObject

@typing_extensions.final
class GeoPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LATITUDE_FIELD_NUMBER: builtins.int
    LONGITUDE_FIELD_NUMBER: builtins.int
    latitude: builtins.float
    longitude: builtins.float

    def __init__(self, *, latitude: builtins.float=..., longitude: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['latitude', b'latitude', 'longitude', b'longitude']) -> None:
        ...
global___GeoPoint = GeoPoint

@typing_extensions.final
class GeoObstacle(google.protobuf.message.Message):
    """GeoObstacle contains information about the geometric structure of an obstacle and the location of the obstacle,
    captured in latitude and longitude.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCATION_FIELD_NUMBER: builtins.int
    GEOMETRIES_FIELD_NUMBER: builtins.int

    @property
    def location(self) -> global___GeoPoint:
        """Location of the obstacle"""

    @property
    def geometries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Geometry]:
        """Geometries that describe the obstacle, where embedded Pose data is with respect to the specified location"""

    def __init__(self, *, location: global___GeoPoint | None=..., geometries: collections.abc.Iterable[global___Geometry] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['geometries', b'geometries', 'location', b'location']) -> None:
        ...
global___GeoObstacle = GeoObstacle

@typing_extensions.final
class Transform(google.protobuf.message.Message):
    """Transform contains a pose and two reference frames. The first reference frame is the starting reference frame, and the second reference
    frame is the observer reference frame. The second reference frame has a pose which represents the pose of an object in the first
    reference frame as observed within the second reference frame.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFERENCE_FRAME_FIELD_NUMBER: builtins.int
    POSE_IN_OBSERVER_FRAME_FIELD_NUMBER: builtins.int
    PHYSICAL_OBJECT_FIELD_NUMBER: builtins.int
    reference_frame: builtins.str
    'the name of a given reference frame'

    @property
    def pose_in_observer_frame(self) -> global___PoseInFrame:
        """the pose of the above reference frame with respect to a different observer reference frame"""

    @property
    def physical_object(self) -> global___Geometry:
        ...

    def __init__(self, *, reference_frame: builtins.str=..., pose_in_observer_frame: global___PoseInFrame | None=..., physical_object: global___Geometry | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_physical_object', b'_physical_object', 'physical_object', b'physical_object', 'pose_in_observer_frame', b'pose_in_observer_frame']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_physical_object', b'_physical_object', 'physical_object', b'physical_object', 'pose_in_observer_frame', b'pose_in_observer_frame', 'reference_frame', b'reference_frame']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_physical_object', b'_physical_object']) -> typing_extensions.Literal['physical_object'] | None:
        ...
global___Transform = Transform

@typing_extensions.final
class WorldState(google.protobuf.message.Message):
    """WorldState contains information about the physical environment around a given robot. All of the fields within this message are optional,
    they can include information about the physical dimensions of an obstacle, the freespace of a robot, and any desired transforms between a
    given reference frame and a new target reference frame.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OBSTACLES_FIELD_NUMBER: builtins.int
    TRANSFORMS_FIELD_NUMBER: builtins.int

    @property
    def obstacles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GeometriesInFrame]:
        """a list of obstacles expressed as a geometry and the reference frame in which it was observed; this field is optional"""

    @property
    def transforms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Transform]:
        """a list of Transforms, optionally with geometries. Used as supplemental transforms to transform a pose from one reference frame to another, or to attach moving geometries to the frame system. This field is optional"""

    def __init__(self, *, obstacles: collections.abc.Iterable[global___GeometriesInFrame] | None=..., transforms: collections.abc.Iterable[global___Transform] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['obstacles', b'obstacles', 'transforms', b'transforms']) -> None:
        ...
global___WorldState = WorldState

@typing_extensions.final
class ActuatorStatus(google.protobuf.message.Message):
    """ActuatorStatus is a generic status for resources that only need to return actuator status."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_MOVING_FIELD_NUMBER: builtins.int
    is_moving: builtins.bool

    def __init__(self, *, is_moving: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['is_moving', b'is_moving']) -> None:
        ...
global___ActuatorStatus = ActuatorStatus

@typing_extensions.final
class ResponseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CAPTURED_AT_FIELD_NUMBER: builtins.int

    @property
    def captured_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """captured_at is the time at which the resource as close as physically possible, captured
        the data in the response.
        Note: If correlating between other resources, be sure that the means
        of measuring the capture are similar enough such that comparison can be made between them.
        """

    def __init__(self, *, captured_at: google.protobuf.timestamp_pb2.Timestamp | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_captured_at', b'_captured_at', 'captured_at', b'captured_at']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_captured_at', b'_captured_at', 'captured_at', b'captured_at']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_captured_at', b'_captured_at']) -> typing_extensions.Literal['captured_at'] | None:
        ...
global___ResponseMetadata = ResponseMetadata

@typing_extensions.final
class DoCommandRequest(google.protobuf.message.Message):
    """DoCommandRequest represents a generic DoCommand input"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def command(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: builtins.str=..., command: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['command', b'command']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['command', b'command', 'name', b'name']) -> None:
        ...
global___DoCommandRequest = DoCommandRequest

@typing_extensions.final
class DoCommandResponse(google.protobuf.message.Message):
    """DoCommandResponse represents a generic DoCommand output"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int

    @property
    def result(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, result: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['result', b'result']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['result', b'result']) -> None:
        ...
global___DoCommandResponse = DoCommandResponse

@typing_extensions.final
class GetKinematicsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'The component name'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetKinematicsRequest = GetKinematicsRequest

@typing_extensions.final
class GetKinematicsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FORMAT_FIELD_NUMBER: builtins.int
    KINEMATICS_DATA_FIELD_NUMBER: builtins.int
    format: global___KinematicsFileFormat.ValueType
    'The kinematics of the component, in either URDF format or in Viam’s kinematic parameter format (spatial vector algebra)\n    https://docs.viam.com/internals/kinematic-chain-config/#kinematic-parameters\n    '
    kinematics_data: builtins.bytes
    'The byte contents of the file'

    def __init__(self, *, format: global___KinematicsFileFormat.ValueType=..., kinematics_data: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['format', b'format', 'kinematics_data', b'kinematics_data']) -> None:
        ...
global___GetKinematicsResponse = GetKinematicsResponse

@typing_extensions.final
class GetGeometriesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'The component name'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetGeometriesRequest = GetGeometriesRequest

@typing_extensions.final
class GetGeometriesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GEOMETRIES_FIELD_NUMBER: builtins.int

    @property
    def geometries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Geometry]:
        """All geometries associated with the component, in their current configuration, in the frame of that component."""

    def __init__(self, *, geometries: collections.abc.Iterable[global___Geometry] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['geometries', b'geometries']) -> None:
        ...
global___GetGeometriesResponse = GetGeometriesResponse

@typing_extensions.final
class GetReadingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a sensor'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetReadingsRequest = GetReadingsRequest

@typing_extensions.final
class GetReadingsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ReadingsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> google.protobuf.struct_pb2.Value:
            ...

        def __init__(self, *, key: builtins.str=..., value: google.protobuf.struct_pb2.Value | None=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    READINGS_FIELD_NUMBER: builtins.int

    @property
    def readings(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, google.protobuf.struct_pb2.Value]:
        ...

    def __init__(self, *, readings: collections.abc.Mapping[builtins.str, google.protobuf.struct_pb2.Value] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['readings', b'readings']) -> None:
        ...
global___GetReadingsResponse = GetReadingsResponse

@typing_extensions.final
class LogEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HOST_FIELD_NUMBER: builtins.int
    LEVEL_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    LOGGER_NAME_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    CALLER_FIELD_NUMBER: builtins.int
    STACK_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    host: builtins.str
    level: builtins.str

    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    logger_name: builtins.str
    message: builtins.str

    @property
    def caller(self) -> google.protobuf.struct_pb2.Struct:
        ...
    stack: builtins.str

    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Struct]:
        ...

    def __init__(self, *, host: builtins.str=..., level: builtins.str=..., time: google.protobuf.timestamp_pb2.Timestamp | None=..., logger_name: builtins.str=..., message: builtins.str=..., caller: google.protobuf.struct_pb2.Struct | None=..., stack: builtins.str=..., fields: collections.abc.Iterable[google.protobuf.struct_pb2.Struct] | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['caller', b'caller', 'time', b'time']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['caller', b'caller', 'fields', b'fields', 'host', b'host', 'level', b'level', 'logger_name', b'logger_name', 'message', b'message', 'stack', b'stack', 'time', b'time']) -> None:
        ...
global___LogEntry = LogEntry
SAFETY_HEARTBEAT_MONITORED_FIELD_NUMBER: builtins.int
safety_heartbeat_monitored: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.MethodOptions, builtins.bool]
'safety_heartbeat_monitored is used on methods to signify that if a session is in use\nand the session was the last to call this method, the resource associated with the\nmethod will be stopped.\n'
