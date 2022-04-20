"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proto/api/common/v1/common.proto\x12\x13proto.api.common.v1"n\n\x0cResourceName\x12\x1c\n\tnamespace\x18\x01 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x18\n\x07subtype\x18\x03 \x01(\tR\x07subtype\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name"\x90\x03\n\x0bBoardStatus\x12G\n\x07analogs\x18\x01 \x03(\x0b2-.proto.api.common.v1.BoardStatus.AnalogsEntryR\x07analogs\x12f\n\x12digital_interrupts\x18\x02 \x03(\x0b27.proto.api.common.v1.BoardStatus.DigitalInterruptsEntryR\x11digitalInterrupts\x1a]\n\x0cAnalogsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x127\n\x05value\x18\x02 \x01(\x0b2!.proto.api.common.v1.AnalogStatusR\x05value:\x028\x01\x1aq\n\x16DigitalInterruptsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12A\n\x05value\x18\x02 \x01(\x0b2+.proto.api.common.v1.DigitalInterruptStatusR\x05value:\x028\x01"$\n\x0cAnalogStatus\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value".\n\x16DigitalInterruptStatus\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta"e\n\x0bPoseInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12-\n\x04pose\x18\x02 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose"3\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"%\n\x06Sphere\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm"e\n\x10RectangularPrism\x12\x19\n\x08width_mm\x18\x01 \x01(\x01R\x07widthMm\x12\x1b\n\tlength_mm\x18\x02 \x01(\x01R\x08lengthMm\x12\x19\n\x08depth_mm\x18\x03 \x01(\x01R\x07depthMm"\xc0\x01\n\x08Geometry\x121\n\x06center\x18\x01 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x06center\x125\n\x06sphere\x18\x02 \x01(\x0b2\x1b.proto.api.common.v1.SphereH\x00R\x06sphere\x129\n\x03box\x18\x03 \x01(\x0b2%.proto.api.common.v1.RectangularPrismH\x00R\x03boxB\x0f\n\rgeometry_type"{\n\x11GeometriesInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12=\n\ngeometries\x18\x02 \x03(\x0b2\x1d.proto.api.common.v1.GeometryR\ngeometries"{\n\x10PointCloudObject\x12\x1f\n\x0bpoint_cloud\x18\x01 \x01(\x0cR\npointCloud\x12F\n\ngeometries\x18\x02 \x01(\x0b2&.proto.api.common.v1.GeometriesInFrameR\ngeometries"D\n\x08GeoPoint\x12\x1a\n\x08latitude\x18\x01 \x01(\x01R\x08latitude\x12\x1c\n\tlongitude\x18\x02 \x01(\x01R\tlongitude"\x8b\x01\n\tTransform\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12U\n\x16pose_in_observer_frame\x18\x02 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x13poseInObserverFrame"\x92\x01\n\nWorldState\x12D\n\tobstacles\x18\x01 \x03(\x0b2&.proto.api.common.v1.GeometriesInFrameR\tobstacles\x12>\n\ntransforms\x18\x02 \x03(\x0b2\x1e.proto.api.common.v1.TransformR\ntransformsBG\n com.viam.rdk.proto.api.common.v1Z#go.viam.com/rdk/proto/api/common/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.common.v1.common_pb2', globals())
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