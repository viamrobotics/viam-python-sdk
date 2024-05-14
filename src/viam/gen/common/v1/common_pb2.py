"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16common/v1/common.proto\x12\x0eviam.common.v1\x1a google/protobuf/descriptor.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"n\n\x0cResourceName\x12\x1c\n\tnamespace\x18\x01 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x18\n\x07subtype\x18\x03 \x01(\tR\x07subtype\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta"V\n\x0bOrientation\x12\x0f\n\x03o_x\x18\x01 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x02 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x03 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x04 \x01(\x01R\x05theta"`\n\x0bPoseInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12(\n\x04pose\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"3\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"%\n\x06Sphere\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm"C\n\x07Capsule\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm\x12\x1b\n\tlength_mm\x18\x02 \x01(\x01R\x08lengthMm"D\n\x10RectangularPrism\x120\n\x07dims_mm\x18\x01 \x01(\x0b2\x17.viam.common.v1.Vector3R\x06dimsMm"\xfc\x01\n\x08Geometry\x12,\n\x06center\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x06center\x120\n\x06sphere\x18\x02 \x01(\x0b2\x16.viam.common.v1.SphereH\x00R\x06sphere\x124\n\x03box\x18\x03 \x01(\x0b2 .viam.common.v1.RectangularPrismH\x00R\x03box\x123\n\x07capsule\x18\x05 \x01(\x0b2\x17.viam.common.v1.CapsuleH\x00R\x07capsule\x12\x14\n\x05label\x18\x04 \x01(\tR\x05labelB\x0f\n\rgeometry_type"v\n\x11GeometriesInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x128\n\ngeometries\x18\x02 \x03(\x0b2\x18.viam.common.v1.GeometryR\ngeometries"v\n\x10PointCloudObject\x12\x1f\n\x0bpoint_cloud\x18\x01 \x01(\x0cR\npointCloud\x12A\n\ngeometries\x18\x02 \x01(\x0b2!.viam.common.v1.GeometriesInFrameR\ngeometries"D\n\x08GeoPoint\x12\x1a\n\x08latitude\x18\x01 \x01(\x01R\x08latitude\x12\x1c\n\tlongitude\x18\x02 \x01(\x01R\tlongitude"}\n\x0bGeoGeometry\x124\n\x08location\x18\x01 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x08location\x128\n\ngeometries\x18\x02 \x03(\x0b2\x18.viam.common.v1.GeometryR\ngeometries"\xe2\x01\n\tTransform\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12P\n\x16pose_in_observer_frame\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x13poseInObserverFrame\x12F\n\x0fphysical_object\x18\x03 \x01(\x0b2\x18.viam.common.v1.GeometryH\x00R\x0ephysicalObject\x88\x01\x01B\x12\n\x10_physical_object"\x88\x01\n\nWorldState\x12?\n\tobstacles\x18\x01 \x03(\x0b2!.viam.common.v1.GeometriesInFrameR\tobstacles\x129\n\ntransforms\x18\x03 \x03(\x0b2\x19.viam.common.v1.TransformR\ntransforms"-\n\x0eActuatorStatus\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving"d\n\x10ResponseMetadata\x12@\n\x0bcaptured_at\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\ncapturedAt\x88\x01\x01B\x0e\n\x0c_captured_at"Y\n\x10DoCommandRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x121\n\x07command\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07command"D\n\x11DoCommandResponse\x12/\n\x06result\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x06result"Y\n\x14GetKinematicsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"~\n\x15GetKinematicsResponse\x12<\n\x06format\x18\x01 \x01(\x0e2$.viam.common.v1.KinematicsFileFormatR\x06format\x12\'\n\x0fkinematics_data\x18\x02 \x01(\x0cR\x0ekinematicsData"Y\n\x14GetGeometriesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"Q\n\x15GetGeometriesResponse\x128\n\ngeometries\x18\x01 \x03(\x0b2\x18.viam.common.v1.GeometryR\ngeometries"W\n\x12GetReadingsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xb9\x01\n\x13GetReadingsResponse\x12M\n\x08readings\x18\x01 \x03(\x0b21.viam.common.v1.GetReadingsResponse.ReadingsEntryR\x08readings\x1aS\n\rReadingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueR\x05value:\x028\x01"\x97\x02\n\x08LogEntry\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x14\n\x05level\x18\x02 \x01(\tR\x05level\x12.\n\x04time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12\x1f\n\x0blogger_name\x18\x04 \x01(\tR\nloggerName\x12\x18\n\x07message\x18\x05 \x01(\tR\x07message\x12/\n\x06caller\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x06caller\x12\x14\n\x05stack\x18\x07 \x01(\tR\x05stack\x12/\n\x06fields\x18\x08 \x03(\x0b2\x17.google.protobuf.StructR\x06fields*\x7f\n\x14KinematicsFileFormat\x12&\n"KINEMATICS_FILE_FORMAT_UNSPECIFIED\x10\x00\x12\x1e\n\x1aKINEMATICS_FILE_FORMAT_SVA\x10\x01\x12\x1f\n\x1bKINEMATICS_FILE_FORMAT_URDF\x10\x02:a\n\x1asafety_heartbeat_monitored\x12\x1e.google.protobuf.MethodOptions\x18\xa4\x92\x05 \x01(\x08R\x18safetyHeartbeatMonitored\x88\x01\x01B/\n\x12com.viam.common.v1Z\x19go.viam.com/api/common/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(safety_heartbeat_monitored)
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x12com.viam.common.v1Z\x19go.viam.com/api/common/v1'
    _GETREADINGSRESPONSE_READINGSENTRY._options = None
    _GETREADINGSRESPONSE_READINGSENTRY._serialized_options = b'8\x01'
    _KINEMATICSFILEFORMAT._serialized_start = 3113
    _KINEMATICSFILEFORMAT._serialized_end = 3240
    _RESOURCENAME._serialized_start = 139
    _RESOURCENAME._serialized_end = 249
    _POSE._serialized_start = 251
    _POSE._serialized_end = 372
    _ORIENTATION._serialized_start = 374
    _ORIENTATION._serialized_end = 460
    _POSEINFRAME._serialized_start = 462
    _POSEINFRAME._serialized_end = 558
    _VECTOR3._serialized_start = 560
    _VECTOR3._serialized_end = 611
    _SPHERE._serialized_start = 613
    _SPHERE._serialized_end = 650
    _CAPSULE._serialized_start = 652
    _CAPSULE._serialized_end = 719
    _RECTANGULARPRISM._serialized_start = 721
    _RECTANGULARPRISM._serialized_end = 789
    _GEOMETRY._serialized_start = 792
    _GEOMETRY._serialized_end = 1044
    _GEOMETRIESINFRAME._serialized_start = 1046
    _GEOMETRIESINFRAME._serialized_end = 1164
    _POINTCLOUDOBJECT._serialized_start = 1166
    _POINTCLOUDOBJECT._serialized_end = 1284
    _GEOPOINT._serialized_start = 1286
    _GEOPOINT._serialized_end = 1354
    _GEOGEOMETRY._serialized_start = 1356
    _GEOGEOMETRY._serialized_end = 1481
    _TRANSFORM._serialized_start = 1484
    _TRANSFORM._serialized_end = 1710
    _WORLDSTATE._serialized_start = 1713
    _WORLDSTATE._serialized_end = 1849
    _ACTUATORSTATUS._serialized_start = 1851
    _ACTUATORSTATUS._serialized_end = 1896
    _RESPONSEMETADATA._serialized_start = 1898
    _RESPONSEMETADATA._serialized_end = 1998
    _DOCOMMANDREQUEST._serialized_start = 2000
    _DOCOMMANDREQUEST._serialized_end = 2089
    _DOCOMMANDRESPONSE._serialized_start = 2091
    _DOCOMMANDRESPONSE._serialized_end = 2159
    _GETKINEMATICSREQUEST._serialized_start = 2161
    _GETKINEMATICSREQUEST._serialized_end = 2250
    _GETKINEMATICSRESPONSE._serialized_start = 2252
    _GETKINEMATICSRESPONSE._serialized_end = 2378
    _GETGEOMETRIESREQUEST._serialized_start = 2380
    _GETGEOMETRIESREQUEST._serialized_end = 2469
    _GETGEOMETRIESRESPONSE._serialized_start = 2471
    _GETGEOMETRIESRESPONSE._serialized_end = 2552
    _GETREADINGSREQUEST._serialized_start = 2554
    _GETREADINGSREQUEST._serialized_end = 2641
    _GETREADINGSRESPONSE._serialized_start = 2644
    _GETREADINGSRESPONSE._serialized_end = 2829
    _GETREADINGSRESPONSE_READINGSENTRY._serialized_start = 2746
    _GETREADINGSRESPONSE_READINGSENTRY._serialized_end = 2829
    _LOGENTRY._serialized_start = 2832
    _LOGENTRY._serialized_end = 3111