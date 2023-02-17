"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16common/v1/common.proto\x12\x0eviam.common.v1\x1a google/protobuf/descriptor.proto\x1a\x1cgoogle/protobuf/struct.proto"n\n\x0cResourceName\x12\x1c\n\tnamespace\x18\x01 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x18\n\x07subtype\x18\x03 \x01(\tR\x07subtype\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name"\xfc\x02\n\x0bBoardStatus\x12B\n\x07analogs\x18\x01 \x03(\x0b2(.viam.common.v1.BoardStatus.AnalogsEntryR\x07analogs\x12a\n\x12digital_interrupts\x18\x02 \x03(\x0b22.viam.common.v1.BoardStatus.DigitalInterruptsEntryR\x11digitalInterrupts\x1aX\n\x0cAnalogsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x122\n\x05value\x18\x02 \x01(\x0b2\x1c.viam.common.v1.AnalogStatusR\x05value:\x028\x01\x1al\n\x16DigitalInterruptsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b2&.viam.common.v1.DigitalInterruptStatusR\x05value:\x028\x01"$\n\x0cAnalogStatus\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value".\n\x16DigitalInterruptStatus\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta"V\n\x0bOrientation\x12\x0f\n\x03o_x\x18\x01 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x02 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x03 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x04 \x01(\x01R\x05theta"`\n\x0bPoseInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12(\n\x04pose\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"3\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"%\n\x06Sphere\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm"C\n\x07Capsule\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm\x12\x1b\n\tlength_mm\x18\x02 \x01(\x01R\x08lengthMm"D\n\x10RectangularPrism\x120\n\x07dims_mm\x18\x01 \x01(\x0b2\x17.viam.common.v1.Vector3R\x06dimsMm"\xfc\x01\n\x08Geometry\x12,\n\x06center\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x06center\x120\n\x06sphere\x18\x02 \x01(\x0b2\x16.viam.common.v1.SphereH\x00R\x06sphere\x124\n\x03box\x18\x03 \x01(\x0b2 .viam.common.v1.RectangularPrismH\x00R\x03box\x123\n\x07capsule\x18\x05 \x01(\x0b2\x17.viam.common.v1.CapsuleH\x00R\x07capsule\x12\x14\n\x05label\x18\x04 \x01(\tR\x05labelB\x0f\n\rgeometry_type"v\n\x11GeometriesInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x128\n\ngeometries\x18\x02 \x03(\x0b2\x18.viam.common.v1.GeometryR\ngeometries"v\n\x10PointCloudObject\x12\x1f\n\x0bpoint_cloud\x18\x01 \x01(\x0cR\npointCloud\x12A\n\ngeometries\x18\x02 \x01(\x0b2!.viam.common.v1.GeometriesInFrameR\ngeometries"D\n\x08GeoPoint\x12\x1a\n\x08latitude\x18\x01 \x01(\x01R\x08latitude\x12\x1c\n\tlongitude\x18\x02 \x01(\x01R\tlongitude"\xe2\x01\n\tTransform\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12P\n\x16pose_in_observer_frame\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x13poseInObserverFrame\x12F\n\x0fphysical_object\x18\x03 \x01(\x0b2\x18.viam.common.v1.GeometryH\x00R\x0ephysicalObject\x88\x01\x01B\x12\n\x10_physical_object"\x88\x01\n\nWorldState\x12?\n\tobstacles\x18\x01 \x03(\x0b2!.viam.common.v1.GeometriesInFrameR\tobstacles\x129\n\ntransforms\x18\x03 \x03(\x0b2\x19.viam.common.v1.TransformR\ntransforms"-\n\x0eActuatorStatus\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving"Y\n\x10DoCommandRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x121\n\x07command\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07command"D\n\x11DoCommandResponse\x12/\n\x06result\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x06result:a\n\x1asafety_heartbeat_monitored\x12\x1e.google.protobuf.MethodOptions\x18\xa4\x92\x05 \x01(\x08R\x18safetyHeartbeatMonitored\x88\x01\x01B/\n\x12com.viam.common.v1Z\x19go.viam.com/api/common/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(safety_heartbeat_monitored)
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x12com.viam.common.v1Z\x19go.viam.com/api/common/v1'
    _BOARDSTATUS_ANALOGSENTRY._options = None
    _BOARDSTATUS_ANALOGSENTRY._serialized_options = b'8\x01'
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._options = None
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_options = b'8\x01'
    _RESOURCENAME._serialized_start = 106
    _RESOURCENAME._serialized_end = 216
    _BOARDSTATUS._serialized_start = 219
    _BOARDSTATUS._serialized_end = 599
    _BOARDSTATUS_ANALOGSENTRY._serialized_start = 401
    _BOARDSTATUS_ANALOGSENTRY._serialized_end = 489
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_start = 491
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_end = 599
    _ANALOGSTATUS._serialized_start = 601
    _ANALOGSTATUS._serialized_end = 637
    _DIGITALINTERRUPTSTATUS._serialized_start = 639
    _DIGITALINTERRUPTSTATUS._serialized_end = 685
    _POSE._serialized_start = 687
    _POSE._serialized_end = 808
    _ORIENTATION._serialized_start = 810
    _ORIENTATION._serialized_end = 896
    _POSEINFRAME._serialized_start = 898
    _POSEINFRAME._serialized_end = 994
    _VECTOR3._serialized_start = 996
    _VECTOR3._serialized_end = 1047
    _SPHERE._serialized_start = 1049
    _SPHERE._serialized_end = 1086
    _CAPSULE._serialized_start = 1088
    _CAPSULE._serialized_end = 1155
    _RECTANGULARPRISM._serialized_start = 1157
    _RECTANGULARPRISM._serialized_end = 1225
    _GEOMETRY._serialized_start = 1228
    _GEOMETRY._serialized_end = 1480
    _GEOMETRIESINFRAME._serialized_start = 1482
    _GEOMETRIESINFRAME._serialized_end = 1600
    _POINTCLOUDOBJECT._serialized_start = 1602
    _POINTCLOUDOBJECT._serialized_end = 1720
    _GEOPOINT._serialized_start = 1722
    _GEOPOINT._serialized_end = 1790
    _TRANSFORM._serialized_start = 1793
    _TRANSFORM._serialized_end = 2019
    _WORLDSTATE._serialized_start = 2022
    _WORLDSTATE._serialized_end = 2158
    _ACTUATORSTATUS._serialized_start = 2160
    _ACTUATORSTATUS._serialized_end = 2205
    _DOCOMMANDREQUEST._serialized_start = 2207
    _DOCOMMANDREQUEST._serialized_end = 2296
    _DOCOMMANDRESPONSE._serialized_start = 2298
    _DOCOMMANDRESPONSE._serialized_end = 2366