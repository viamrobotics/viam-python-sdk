"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proto/api/common/v1/common.proto\x12\x13proto.api.common.v1"n\n\x0cResourceName\x12\x1c\n\tnamespace\x18\x01 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x18\n\x07subtype\x18\x03 \x01(\tR\x07subtype\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name"\x90\x03\n\x0bBoardStatus\x12G\n\x07analogs\x18\x01 \x03(\x0b2-.proto.api.common.v1.BoardStatus.AnalogsEntryR\x07analogs\x12f\n\x12digital_interrupts\x18\x02 \x03(\x0b27.proto.api.common.v1.BoardStatus.DigitalInterruptsEntryR\x11digitalInterrupts\x1a]\n\x0cAnalogsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x127\n\x05value\x18\x02 \x01(\x0b2!.proto.api.common.v1.AnalogStatusR\x05value:\x028\x01\x1aq\n\x16DigitalInterruptsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12A\n\x05value\x18\x02 \x01(\x0b2+.proto.api.common.v1.DigitalInterruptStatusR\x05value:\x028\x01"$\n\x0cAnalogStatus\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value".\n\x16DigitalInterruptStatus\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta"e\n\x0bPoseInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12-\n\x04pose\x18\x02 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose"3\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"%\n\x06Sphere\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm"e\n\x10RectangularPrism\x12\x19\n\x08width_mm\x18\x01 \x01(\x01R\x07widthMm\x12\x1b\n\tlength_mm\x18\x02 \x01(\x01R\x08lengthMm\x12\x19\n\x08depth_mm\x18\x03 \x01(\x01R\x07depthMm"\xc0\x01\n\x08Geometry\x121\n\x06center\x18\x01 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x06center\x125\n\x06sphere\x18\x02 \x01(\x0b2\x1b.proto.api.common.v1.SphereH\x00R\x06sphere\x129\n\x03box\x18\x03 \x01(\x0b2%.proto.api.common.v1.RectangularPrismH\x00R\x03boxB\x0f\n\rgeometry_type"{\n\x11GeometriesInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12=\n\ngeometries\x18\x02 \x03(\x0b2\x1d.proto.api.common.v1.GeometryR\ngeometries"{\n\x10PointCloudObject\x12\x1f\n\x0bpoint_cloud\x18\x01 \x01(\x0cR\npointCloud\x12F\n\ngeometries\x18\x02 \x01(\x0b2&.proto.api.common.v1.GeometriesInFrameR\ngeometries"D\n\x08GeoPoint\x12\x1a\n\x08latitude\x18\x01 \x01(\x01R\x08latitude\x12\x1c\n\tlongitude\x18\x02 \x01(\x01R\tlongitude"\x8b\x01\n\tTransform\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12U\n\x16pose_in_observer_frame\x18\x02 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x13poseInObserverFrame"\x92\x01\n\nWorldState\x12D\n\tobstacles\x18\x01 \x03(\x0b2&.proto.api.common.v1.GeometriesInFrameR\tobstacles\x12>\n\ntransforms\x18\x02 \x03(\x0b2\x1e.proto.api.common.v1.TransformR\ntransformsBG\n com.viam.rdk.proto.api.common.v1Z#go.viam.com/rdk/proto/api/common/v1b\x06proto3')
_RESOURCENAME = DESCRIPTOR.message_types_by_name['ResourceName']
_BOARDSTATUS = DESCRIPTOR.message_types_by_name['BoardStatus']
_BOARDSTATUS_ANALOGSENTRY = _BOARDSTATUS.nested_types_by_name['AnalogsEntry']
_BOARDSTATUS_DIGITALINTERRUPTSENTRY = _BOARDSTATUS.nested_types_by_name['DigitalInterruptsEntry']
_ANALOGSTATUS = DESCRIPTOR.message_types_by_name['AnalogStatus']
_DIGITALINTERRUPTSTATUS = DESCRIPTOR.message_types_by_name['DigitalInterruptStatus']
_POSE = DESCRIPTOR.message_types_by_name['Pose']
_POSEINFRAME = DESCRIPTOR.message_types_by_name['PoseInFrame']
_VECTOR3 = DESCRIPTOR.message_types_by_name['Vector3']
_SPHERE = DESCRIPTOR.message_types_by_name['Sphere']
_RECTANGULARPRISM = DESCRIPTOR.message_types_by_name['RectangularPrism']
_GEOMETRY = DESCRIPTOR.message_types_by_name['Geometry']
_GEOMETRIESINFRAME = DESCRIPTOR.message_types_by_name['GeometriesInFrame']
_POINTCLOUDOBJECT = DESCRIPTOR.message_types_by_name['PointCloudObject']
_GEOPOINT = DESCRIPTOR.message_types_by_name['GeoPoint']
_TRANSFORM = DESCRIPTOR.message_types_by_name['Transform']
_WORLDSTATE = DESCRIPTOR.message_types_by_name['WorldState']
ResourceName = _reflection.GeneratedProtocolMessageType('ResourceName', (_message.Message,), {'DESCRIPTOR': _RESOURCENAME, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(ResourceName)
BoardStatus = _reflection.GeneratedProtocolMessageType('BoardStatus', (_message.Message,), {'AnalogsEntry': _reflection.GeneratedProtocolMessageType('AnalogsEntry', (_message.Message,), {'DESCRIPTOR': _BOARDSTATUS_ANALOGSENTRY, '__module__': 'proto.api.common.v1.common_pb2'}), 'DigitalInterruptsEntry': _reflection.GeneratedProtocolMessageType('DigitalInterruptsEntry', (_message.Message,), {'DESCRIPTOR': _BOARDSTATUS_DIGITALINTERRUPTSENTRY, '__module__': 'proto.api.common.v1.common_pb2'}), 'DESCRIPTOR': _BOARDSTATUS, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(BoardStatus)
_sym_db.RegisterMessage(BoardStatus.AnalogsEntry)
_sym_db.RegisterMessage(BoardStatus.DigitalInterruptsEntry)
AnalogStatus = _reflection.GeneratedProtocolMessageType('AnalogStatus', (_message.Message,), {'DESCRIPTOR': _ANALOGSTATUS, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': 'Attributes:\n      value:\n          Current value of the analog reader of a robot’s board\n  '})
_sym_db.RegisterMessage(AnalogStatus)
DigitalInterruptStatus = _reflection.GeneratedProtocolMessageType('DigitalInterruptStatus', (_message.Message,), {'DESCRIPTOR': _DIGITALINTERRUPTSTATUS, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': 'Attributes:\n      value:\n          Current value of the digital interrupt of a robot’s board\n  '})
_sym_db.RegisterMessage(DigitalInterruptStatus)
Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {'DESCRIPTOR': _POSE, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': ' Pose is a combination of location and orientation. Location is\n  expressed as distance which is represented by x , y, z coordinates.\n  Orientation is expressed as an orientation vector which is represented\n  by o_x, o_y, o_z and theta. The o_x, o_y, o_z coordinates represent\n  the point on the cartesian unit sphere that the end of the arm is\n  pointing to (with the origin as reference). That unit vector forms an\n  axis around which theta rotates. This means that incrementing /\n  decrementing theta will perform an inline rotation of the end\n  effector. Theta is defined as rotation between two planes: the first\n  being defined by the origin, the point (0,0,1), and the rx, ry, rz\n  point, and the second being defined by the origin, the rx, ry, rz\n  point and the local Z axis. Therefore, if theta is kept at zero as the\n  north/south pole is circled, the Roll will correct itself to remain\n  in-line.\n  \n  Attributes:\n      x:\n          millimeters from the origin\n      y:\n          millimeters from the origin\n      z:\n          millimeters from the origin\n      o_x:\n          z component of a vector defining axis of rotation\n      o_y:\n          x component of a vector defining axis of rotation\n      o_z:\n          y component of a vector defining axis of rotation\n      theta:\n          degrees\n  '})
_sym_db.RegisterMessage(Pose)
PoseInFrame = _reflection.GeneratedProtocolMessageType('PoseInFrame', (_message.Message,), {'DESCRIPTOR': _POSEINFRAME, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': 'PoseInFrame contains a pose and the and the reference frame in which\n  it was observed'})
_sym_db.RegisterMessage(PoseInFrame)
Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), {'DESCRIPTOR': _VECTOR3, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(Vector3)
Sphere = _reflection.GeneratedProtocolMessageType('Sphere', (_message.Message,), {'DESCRIPTOR': _SPHERE, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(Sphere)
RectangularPrism = _reflection.GeneratedProtocolMessageType('RectangularPrism', (_message.Message,), {'DESCRIPTOR': _RECTANGULARPRISM, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(RectangularPrism)
Geometry = _reflection.GeneratedProtocolMessageType('Geometry', (_message.Message,), {'DESCRIPTOR': _GEOMETRY, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': 'Geometry contains the dimensions of a given geometry and the pose of\n  its center. The geometry is one of either a sphere or a box.\n  \n  Attributes:\n      center:\n          Pose of a gemetries center point\n      geometry_type:\n          Deminsions of a give geometry. This can be a sphere or box\n  '})
_sym_db.RegisterMessage(Geometry)
GeometriesInFrame = _reflection.GeneratedProtocolMessageType('GeometriesInFrame', (_message.Message,), {'DESCRIPTOR': _GEOMETRIESINFRAME, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': 'GeometriesinFrame contains the dimensions of a given geometry, pose of\n  its center point, and the reference frame by which it was observed.\n  \n  Attributes:\n      reference_frame:\n          Reference frame of the observer of the geometry\n      geometries:\n          Dimensional type\n  '})
_sym_db.RegisterMessage(GeometriesInFrame)
PointCloudObject = _reflection.GeneratedProtocolMessageType('PointCloudObject', (_message.Message,), {'DESCRIPTOR': _POINTCLOUDOBJECT, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': 'PointCloudObject contains an image in bytes with point cloud data of\n  all of the objects captured by a given observer as well as a repeated\n  list of geometries which respresents the center point and geometry of\n  each of the objects within the point cloud\n  \n  Attributes:\n      point_cloud:\n          image frame expressed in bytes\n      geometries:\n          volume of a given geometry\n  '})
_sym_db.RegisterMessage(PointCloudObject)
GeoPoint = _reflection.GeneratedProtocolMessageType('GeoPoint', (_message.Message,), {'DESCRIPTOR': _GEOPOINT, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(GeoPoint)
Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), {'DESCRIPTOR': _TRANSFORM, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': 'Transform contains a pose and two reference frames. The first\n  reference frame is the starting reference frame, and the second\n  reference frame is the observer reference frame. The second reference\n  frame has a pose which represents the pose of an object in the first\n  reference frame as observed within the second reference frame.\n  \n  Attributes:\n      reference_frame:\n          the name of a given reference frame\n      pose_in_observer_frame:\n          the pose of the above reference frame with respect to a\n          different observer reference frame\n  '})
_sym_db.RegisterMessage(Transform)
WorldState = _reflection.GeneratedProtocolMessageType('WorldState', (_message.Message,), {'DESCRIPTOR': _WORLDSTATE, '__module__': 'proto.api.common.v1.common_pb2', '__doc__': 'WorldState contains information about the physical environment around\n  a given robot. All of the fields within this message are optional,\n  they can include information about the physical dimensions of an\n  obstacle, the freespace of a robot, and any desired transforms between\n  a given reference frame and a new target reference frame.\n  \n  Attributes:\n      obstacles:\n          a list of obstacles expressed as a geomtry and the reference\n          frame in which it was observed; this field is optional\n      transforms:\n          a list of Transforms needed to transform a pose from one\n          reference frame to another; this field is optional\n  '})
_sym_db.RegisterMessage(WorldState)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.viam.rdk.proto.api.common.v1Z#go.viam.com/rdk/proto/api/common/v1'
    _BOARDSTATUS_ANALOGSENTRY._options = None
    _BOARDSTATUS_ANALOGSENTRY._serialized_options = b'8\x01'
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._options = None
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_options = b'8\x01'
    _RESOURCENAME._serialized_start = 57
    _RESOURCENAME._serialized_end = 167
    _BOARDSTATUS._serialized_start = 170
    _BOARDSTATUS._serialized_end = 570
    _BOARDSTATUS_ANALOGSENTRY._serialized_start = 362
    _BOARDSTATUS_ANALOGSENTRY._serialized_end = 455
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_start = 457
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_end = 570
    _ANALOGSTATUS._serialized_start = 572
    _ANALOGSTATUS._serialized_end = 608
    _DIGITALINTERRUPTSTATUS._serialized_start = 610
    _DIGITALINTERRUPTSTATUS._serialized_end = 656
    _POSE._serialized_start = 658
    _POSE._serialized_end = 779
    _POSEINFRAME._serialized_start = 781
    _POSEINFRAME._serialized_end = 882
    _VECTOR3._serialized_start = 884
    _VECTOR3._serialized_end = 935
    _SPHERE._serialized_start = 937
    _SPHERE._serialized_end = 974
    _RECTANGULARPRISM._serialized_start = 976
    _RECTANGULARPRISM._serialized_end = 1077
    _GEOMETRY._serialized_start = 1080
    _GEOMETRY._serialized_end = 1272
    _GEOMETRIESINFRAME._serialized_start = 1274
    _GEOMETRIESINFRAME._serialized_end = 1397
    _POINTCLOUDOBJECT._serialized_start = 1399
    _POINTCLOUDOBJECT._serialized_end = 1522
    _GEOPOINT._serialized_start = 1524
    _GEOPOINT._serialized_end = 1592
    _TRANSFORM._serialized_start = 1595
    _TRANSFORM._serialized_end = 1734
    _WORLDSTATE._serialized_start = 1737
    _WORLDSTATE._serialized_end = 1883