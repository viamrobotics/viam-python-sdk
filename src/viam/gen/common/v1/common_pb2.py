"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16common/v1/common.proto\x12\x0eviam.common.v1"n\n\x0cResourceName\x12\x1c\n\tnamespace\x18\x01 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x18\n\x07subtype\x18\x03 \x01(\tR\x07subtype\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name"\xfc\x02\n\x0bBoardStatus\x12B\n\x07analogs\x18\x01 \x03(\x0b2(.viam.common.v1.BoardStatus.AnalogsEntryR\x07analogs\x12a\n\x12digital_interrupts\x18\x02 \x03(\x0b22.viam.common.v1.BoardStatus.DigitalInterruptsEntryR\x11digitalInterrupts\x1aX\n\x0cAnalogsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x122\n\x05value\x18\x02 \x01(\x0b2\x1c.viam.common.v1.AnalogStatusR\x05value:\x028\x01\x1al\n\x16DigitalInterruptsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b2&.viam.common.v1.DigitalInterruptStatusR\x05value:\x028\x01"$\n\x0cAnalogStatus\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value".\n\x16DigitalInterruptStatus\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta"V\n\x0bOrientation\x12\x0f\n\x03o_x\x18\x01 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x02 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x03 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x04 \x01(\x01R\x05theta"`\n\x0bPoseInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12(\n\x04pose\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"3\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"%\n\x06Sphere\x12\x1b\n\tradius_mm\x18\x01 \x01(\x01R\x08radiusMm"D\n\x10RectangularPrism\x120\n\x07dims_mm\x18\x01 \x01(\x0b2\x17.viam.common.v1.Vector3R\x06dimsMm"\xb1\x01\n\x08Geometry\x12,\n\x06center\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x06center\x120\n\x06sphere\x18\x02 \x01(\x0b2\x16.viam.common.v1.SphereH\x00R\x06sphere\x124\n\x03box\x18\x03 \x01(\x0b2 .viam.common.v1.RectangularPrismH\x00R\x03boxB\x0f\n\rgeometry_type"v\n\x11GeometriesInFrame\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x128\n\ngeometries\x18\x02 \x03(\x0b2\x18.viam.common.v1.GeometryR\ngeometries"v\n\x10PointCloudObject\x12\x1f\n\x0bpoint_cloud\x18\x01 \x01(\x0cR\npointCloud\x12A\n\ngeometries\x18\x02 \x01(\x0b2!.viam.common.v1.GeometriesInFrameR\ngeometries"D\n\x08GeoPoint\x12\x1a\n\x08latitude\x18\x01 \x01(\x01R\x08latitude\x12\x1c\n\tlongitude\x18\x02 \x01(\x01R\tlongitude"\x86\x01\n\tTransform\x12\'\n\x0freference_frame\x18\x01 \x01(\tR\x0ereferenceFrame\x12P\n\x16pose_in_observer_frame\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x13poseInObserverFrame"\xda\x01\n\nWorldState\x12?\n\tobstacles\x18\x01 \x03(\x0b2!.viam.common.v1.GeometriesInFrameR\tobstacles\x12P\n\x12interaction_spaces\x18\x02 \x03(\x0b2!.viam.common.v1.GeometriesInFrameR\x11interactionSpaces\x129\n\ntransforms\x18\x03 \x03(\x0b2\x19.viam.common.v1.TransformR\ntransforms"-\n\x0eActuatorStatus\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMovingB/\n\x12com.viam.common.v1Z\x19go.viam.com/api/common/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x12com.viam.common.v1Z\x19go.viam.com/api/common/v1'
    _BOARDSTATUS_ANALOGSENTRY._options = None
    _BOARDSTATUS_ANALOGSENTRY._serialized_options = b'8\x01'
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._options = None
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_options = b'8\x01'
    _RESOURCENAME._serialized_start = 42
    _RESOURCENAME._serialized_end = 152
    _BOARDSTATUS._serialized_start = 155
    _BOARDSTATUS._serialized_end = 535
    _BOARDSTATUS_ANALOGSENTRY._serialized_start = 337
    _BOARDSTATUS_ANALOGSENTRY._serialized_end = 425
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_start = 427
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_end = 535
    _ANALOGSTATUS._serialized_start = 537
    _ANALOGSTATUS._serialized_end = 573
    _DIGITALINTERRUPTSTATUS._serialized_start = 575
    _DIGITALINTERRUPTSTATUS._serialized_end = 621
    _POSE._serialized_start = 623
    _POSE._serialized_end = 744
    _ORIENTATION._serialized_start = 746
    _ORIENTATION._serialized_end = 832
    _POSEINFRAME._serialized_start = 834
    _POSEINFRAME._serialized_end = 930
    _VECTOR3._serialized_start = 932
    _VECTOR3._serialized_end = 983
    _SPHERE._serialized_start = 985
    _SPHERE._serialized_end = 1022
    _RECTANGULARPRISM._serialized_start = 1024
    _RECTANGULARPRISM._serialized_end = 1092
    _GEOMETRY._serialized_start = 1095
    _GEOMETRY._serialized_end = 1272
    _GEOMETRIESINFRAME._serialized_start = 1274
    _GEOMETRIESINFRAME._serialized_end = 1392
    _POINTCLOUDOBJECT._serialized_start = 1394
    _POINTCLOUDOBJECT._serialized_end = 1512
    _GEOPOINT._serialized_start = 1514
    _GEOPOINT._serialized_end = 1582
    _TRANSFORM._serialized_start = 1585
    _TRANSFORM._serialized_end = 1719
    _WORLDSTATE._serialized_start = 1722
    _WORLDSTATE._serialized_end = 1940
    _ACTUATORSTATUS._serialized_start = 1942
    _ACTUATORSTATUS._serialized_end = 1987