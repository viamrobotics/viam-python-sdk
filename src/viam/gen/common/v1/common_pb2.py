"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'common/v1/common.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16common/v1/common.proto\x12\x0eviam.common.v1\x1a google/protobuf/descriptor.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xae\x01\n\x0cResourceName\x12\x1c\n\tnamespace\x18\x01 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x18\n\x07subtype\x18\x03 \x01(\tR\x07subtype\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x1f\n\x0bremote_path\x18\x05 \x03(\tR\nremotePath\x12\x1d\n\nlocal_name\x18\x06 \x01(\tR\tlocalName"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta"V\n\x0bOrientation\x12\x0f\n\x03o_x\x18\x01 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x02 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x03 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x04 \x01(\x01R\x05theta"`\n\x0bPoseInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12(\n\x04pose\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"3\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"%\n\x06Sphere\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm"C\n\x07Capsule\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm\x12\x1b\n\tlength_mm\x18\x02 \x01(\x01R\x08lengthMm"D\n\x10RectangularPrism\x120\n\x07dims_mm\x18\x01 \x01(\x0b2\x17.viam.common.v1.Vector3R\x06dimsMm"=\n\x04Mesh\x12!\n\x0ccontent_type\x18\x01 \x01(\tR\x0bcontentType\x12\x12\n\x04mesh\x18\x02 \x01(\x0cR\x04mesh"\xa8\x02\n\x08Geometry\x12,\n\x06center\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x06center\x120\n\x06sphere\x18\x02 \x01(\x0b2\x16.viam.common.v1.SphereH\x00R\x06sphere\x124\n\x03box\x18\x03 \x01(\x0b2 .viam.common.v1.RectangularPrismH\x00R\x03box\x123\n\x07capsule\x18\x05 \x01(\x0b2\x17.viam.common.v1.CapsuleH\x00R\x07capsule\x12*\n\x04mesh\x18\x06 \x01(\x0b2\x14.viam.common.v1.MeshH\x00R\x04mesh\x12\x14\n\x05label\x18\x04 \x01(\tR\x05labelB\x0f\n\rgeometry_type"v\n\x11GeometriesInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x128\n\ngeometries\x18\x02 \x03(\x0b2\x18.viam.common.v1.GeometryR\ngeometries"v\n\x10PointCloudObject\x12\x1f\n\x0bpoint_cloud\x18\x01 \x01(\x0cR\npointCloud\x12A\n\ngeometries\x18\x02 \x01(\x0b2!.viam.common.v1.GeometriesInFrameR\ngeometries"D\n\x08GeoPoint\x12\x1a\n\x08latitude\x18\x01 \x01(\x01R\x08latitude\x12\x1c\n\tlongitude\x18\x02 \x01(\x01R\tlongitude"}\n\x0bGeoGeometry\x124\n\x08location\x18\x01 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x08location\x128\n\ngeometries\x18\x02 \x03(\x0b2\x18.viam.common.v1.GeometryR\ngeometries"\xe2\x01\n\tTransform\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12P\n\x16pose_in_observer_frame\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x13poseInObserverFrame\x12F\n\x0fphysical_object\x18\x03 \x01(\x0b2\x18.viam.common.v1.GeometryH\x00R\x0ephysicalObject\x88\x01\x01B\x12\n\x10_physical_object"\x88\x01\n\nWorldState\x12?\n\tobstacles\x18\x01 \x03(\x0b2!.viam.common.v1.GeometriesInFrameR\tobstacles\x129\n\ntransforms\x18\x03 \x03(\x0b2\x19.viam.common.v1.TransformR\ntransforms"-\n\x0eActuatorStatus\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving"d\n\x10ResponseMetadata\x12@\n\x0bcaptured_at\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\ncapturedAt\x88\x01\x01B\x0e\n\x0c_captured_at"Y\n\x10DoCommandRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x121\n\x07command\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07command"D\n\x11DoCommandResponse\x12/\n\x06result\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x06result"Y\n\x14GetKinematicsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"~\n\x15GetKinematicsResponse\x12<\n\x06format\x18\x01 \x01(\x0e2$.viam.common.v1.KinematicsFileFormatR\x06format\x12\'\n\x0fkinematics_data\x18\x02 \x01(\x0cR\x0ekinematicsData"Y\n\x14GetGeometriesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"Q\n\x15GetGeometriesResponse\x128\n\ngeometries\x18\x01 \x03(\x0b2\x18.viam.common.v1.GeometryR\ngeometries"W\n\x12GetReadingsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xb9\x01\n\x13GetReadingsResponse\x12M\n\x08readings\x18\x01 \x03(\x0b21.viam.common.v1.GetReadingsResponse.ReadingsEntryR\x08readings\x1aS\n\rReadingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueR\x05value:\x028\x01"\x97\x02\n\x08LogEntry\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x14\n\x05level\x18\x02 \x01(\tR\x05level\x12.\n\x04time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12\x1f\n\x0blogger_name\x18\x04 \x01(\tR\nloggerName\x12\x18\n\x07message\x18\x05 \x01(\tR\x07message\x12/\n\x06caller\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x06caller\x12\x14\n\x05stack\x18\x07 \x01(\tR\x05stack\x12/\n\x06fields\x18\x08 \x03(\x0b2\x17.google.protobuf.StructR\x06fields*\x7f\n\x14KinematicsFileFormat\x12&\n"KINEMATICS_FILE_FORMAT_UNSPECIFIED\x10\x00\x12\x1e\n\x1aKINEMATICS_FILE_FORMAT_SVA\x10\x01\x12\x1f\n\x1bKINEMATICS_FILE_FORMAT_URDF\x10\x02:a\n\x1asafety_heartbeat_monitored\x12\x1e.google.protobuf.MethodOptions\x18\xa4\x92\x05 \x01(\x08R\x18safetyHeartbeatMonitored\x88\x01\x01B/\n\x12com.viam.common.v1Z\x19go.viam.com/api/common/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.viam.common.v1Z\x19go.viam.com/api/common/v1'
    _globals['_GETREADINGSRESPONSE_READINGSENTRY']._loaded_options = None
    _globals['_GETREADINGSRESPONSE_READINGSENTRY']._serialized_options = b'8\x01'
    _globals['_KINEMATICSFILEFORMAT']._serialized_start = 3285
    _globals['_KINEMATICSFILEFORMAT']._serialized_end = 3412
    _globals['_RESOURCENAME']._serialized_start = 140
    _globals['_RESOURCENAME']._serialized_end = 314
    _globals['_POSE']._serialized_start = 316
    _globals['_POSE']._serialized_end = 437
    _globals['_ORIENTATION']._serialized_start = 439
    _globals['_ORIENTATION']._serialized_end = 525
    _globals['_POSEINFRAME']._serialized_start = 527
    _globals['_POSEINFRAME']._serialized_end = 623
    _globals['_VECTOR3']._serialized_start = 625
    _globals['_VECTOR3']._serialized_end = 676
    _globals['_SPHERE']._serialized_start = 678
    _globals['_SPHERE']._serialized_end = 715
    _globals['_CAPSULE']._serialized_start = 717
    _globals['_CAPSULE']._serialized_end = 784
    _globals['_RECTANGULARPRISM']._serialized_start = 786
    _globals['_RECTANGULARPRISM']._serialized_end = 854
    _globals['_MESH']._serialized_start = 856
    _globals['_MESH']._serialized_end = 917
    _globals['_GEOMETRY']._serialized_start = 920
    _globals['_GEOMETRY']._serialized_end = 1216
    _globals['_GEOMETRIESINFRAME']._serialized_start = 1218
    _globals['_GEOMETRIESINFRAME']._serialized_end = 1336
    _globals['_POINTCLOUDOBJECT']._serialized_start = 1338
    _globals['_POINTCLOUDOBJECT']._serialized_end = 1456
    _globals['_GEOPOINT']._serialized_start = 1458
    _globals['_GEOPOINT']._serialized_end = 1526
    _globals['_GEOGEOMETRY']._serialized_start = 1528
    _globals['_GEOGEOMETRY']._serialized_end = 1653
    _globals['_TRANSFORM']._serialized_start = 1656
    _globals['_TRANSFORM']._serialized_end = 1882
    _globals['_WORLDSTATE']._serialized_start = 1885
    _globals['_WORLDSTATE']._serialized_end = 2021
    _globals['_ACTUATORSTATUS']._serialized_start = 2023
    _globals['_ACTUATORSTATUS']._serialized_end = 2068
    _globals['_RESPONSEMETADATA']._serialized_start = 2070
    _globals['_RESPONSEMETADATA']._serialized_end = 2170
    _globals['_DOCOMMANDREQUEST']._serialized_start = 2172
    _globals['_DOCOMMANDREQUEST']._serialized_end = 2261
    _globals['_DOCOMMANDRESPONSE']._serialized_start = 2263
    _globals['_DOCOMMANDRESPONSE']._serialized_end = 2331
    _globals['_GETKINEMATICSREQUEST']._serialized_start = 2333
    _globals['_GETKINEMATICSREQUEST']._serialized_end = 2422
    _globals['_GETKINEMATICSRESPONSE']._serialized_start = 2424
    _globals['_GETKINEMATICSRESPONSE']._serialized_end = 2550
    _globals['_GETGEOMETRIESREQUEST']._serialized_start = 2552
    _globals['_GETGEOMETRIESREQUEST']._serialized_end = 2641
    _globals['_GETGEOMETRIESRESPONSE']._serialized_start = 2643
    _globals['_GETGEOMETRIESRESPONSE']._serialized_end = 2724
    _globals['_GETREADINGSREQUEST']._serialized_start = 2726
    _globals['_GETREADINGSREQUEST']._serialized_end = 2813
    _globals['_GETREADINGSRESPONSE']._serialized_start = 2816
    _globals['_GETREADINGSRESPONSE']._serialized_end = 3001
    _globals['_GETREADINGSRESPONSE_READINGSENTRY']._serialized_start = 2918
    _globals['_GETREADINGSRESPONSE_READINGSENTRY']._serialized_end = 3001
    _globals['_LOGENTRY']._serialized_start = 3004
    _globals['_LOGENTRY']._serialized_end = 3283