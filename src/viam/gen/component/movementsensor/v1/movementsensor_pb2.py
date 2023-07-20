"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0component/movementsensor/v1/movementsensor.proto\x12 viam.component.movementsensor.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"]\n\x18GetLinearVelocityRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"]\n\x19GetLinearVelocityResponse\x12@\n\x0flinear_velocity\x18\x01 \x01(\x0b2\x17.viam.common.v1.Vector3R\x0elinearVelocity"^\n\x19GetAngularVelocityRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"`\n\x1aGetAngularVelocityResponse\x12B\n\x10angular_velocity\x18\x01 \x01(\x0b2\x17.viam.common.v1.Vector3R\x0fangularVelocity"]\n\x18GetCompassHeadingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"1\n\x19GetCompassHeadingResponse\x12\x14\n\x05value\x18\x01 \x01(\x01R\x05value"Z\n\x15GetOrientationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"W\n\x16GetOrientationResponse\x12=\n\x0borientation\x18\x01 \x01(\x0b2\x1b.viam.common.v1.OrientationR\x0borientation"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"n\n\x13GetPositionResponse\x128\n\ncoordinate\x18\x01 \x01(\x0b2\x18.viam.common.v1.GeoPointR\ncoordinate\x12\x1d\n\naltitude_m\x18\x02 \x01(\x02R\taltitudeM"Y\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xf5\x02\n\x15GetPropertiesResponse\x12:\n\x19linear_velocity_supported\x18\x01 \x01(\x08R\x17linearVelocitySupported\x12<\n\x1aangular_velocity_supported\x18\x02 \x01(\x08R\x18angularVelocitySupported\x123\n\x15orientation_supported\x18\x03 \x01(\x08R\x14orientationSupported\x12-\n\x12position_supported\x18\x04 \x01(\x08R\x11positionSupported\x12:\n\x19compass_heading_supported\x18\x05 \x01(\x08R\x17compassHeadingSupported\x12B\n\x1dlinear_acceleration_supported\x18\x06 \x01(\x08R\x1blinearAccelerationSupported"W\n\x12GetAccuracyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xb3\x01\n\x13GetAccuracyResponse\x12_\n\x08accuracy\x18\x01 \x03(\x0b2C.viam.component.movementsensor.v1.GetAccuracyResponse.AccuracyEntryR\x08accuracy\x1a;\n\rAccuracyEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x02R\x05value:\x028\x01"a\n\x1cGetLinearAccelerationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"i\n\x1dGetLinearAccelerationResponse\x12H\n\x13linear_acceleration\x18\x01 \x01(\x0b2\x17.viam.common.v1.Vector3R\x12linearAcceleration2\xb7\x0f\n\x15MovementSensorService\x12\xd2\x01\n\x11GetLinearVelocity\x12:.viam.component.movementsensor.v1.GetLinearVelocityRequest\x1a;.viam.component.movementsensor.v1.GetLinearVelocityResponse"D\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/component/movementsensor/{name}/linear_velocity\x12\xd6\x01\n\x12GetAngularVelocity\x12;.viam.component.movementsensor.v1.GetAngularVelocityRequest\x1a<.viam.component.movementsensor.v1.GetAngularVelocityResponse"E\x82\xd3\xe4\x93\x02?\x12=/viam/api/v1/component/movementsensor/{name}/angular_velocity\x12\xd2\x01\n\x11GetCompassHeading\x12:.viam.component.movementsensor.v1.GetCompassHeadingRequest\x1a;.viam.component.movementsensor.v1.GetCompassHeadingResponse"D\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/component/movementsensor/{name}/compass_heading\x12\xc5\x01\n\x0eGetOrientation\x127.viam.component.movementsensor.v1.GetOrientationRequest\x1a8.viam.component.movementsensor.v1.GetOrientationResponse"@\x82\xd3\xe4\x93\x02:\x128/viam/api/v1/component/movementsensor/{name}/orientation\x12\xb9\x01\n\x0bGetPosition\x124.viam.component.movementsensor.v1.GetPositionRequest\x1a5.viam.component.movementsensor.v1.GetPositionResponse"=\x82\xd3\xe4\x93\x027\x125/viam/api/v1/component/movementsensor/{name}/position\x12\xc1\x01\n\rGetProperties\x126.viam.component.movementsensor.v1.GetPropertiesRequest\x1a7.viam.component.movementsensor.v1.GetPropertiesResponse"?\x82\xd3\xe4\x93\x029\x127/viam/api/v1/component/movementsensor/{name}/properties\x12\xb9\x01\n\x0bGetAccuracy\x124.viam.component.movementsensor.v1.GetAccuracyRequest\x1a5.viam.component.movementsensor.v1.GetAccuracyResponse"=\x82\xd3\xe4\x93\x027\x125/viam/api/v1/component/movementsensor/{name}/accuracy\x12\xe2\x01\n\x15GetLinearAcceleration\x12>.viam.component.movementsensor.v1.GetLinearAccelerationRequest\x1a?.viam.component.movementsensor.v1.GetLinearAccelerationResponse"H\x82\xd3\xe4\x93\x02B\x12@/viam/api/v1/component/movementsensor/{name}/linear_acceleration\x12\x91\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"?\x82\xd3\xe4\x93\x029"7/viam/api/v1/component/movementsensor/{name}/do_command\x12\x9d\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"?\x82\xd3\xe4\x93\x029\x127/viam/api/v1/component/movementsensor/{name}/geometriesBS\n$com.viam.component.movementsensor.v1Z+go.viam.com/api/component/movementsensor/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.movementsensor.v1.movementsensor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n$com.viam.component.movementsensor.v1Z+go.viam.com/api/component/movementsensor/v1'
    _GETACCURACYRESPONSE_ACCURACYENTRY._options = None
    _GETACCURACYRESPONSE_ACCURACYENTRY._serialized_options = b'8\x01'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetLinearVelocity']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetLinearVelocity']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/component/movementsensor/{name}/linear_velocity'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetAngularVelocity']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetAngularVelocity']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/viam/api/v1/component/movementsensor/{name}/angular_velocity'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetCompassHeading']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetCompassHeading']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/component/movementsensor/{name}/compass_heading'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetOrientation']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetOrientation']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/viam/api/v1/component/movementsensor/{name}/orientation'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetPosition']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/viam/api/v1/component/movementsensor/{name}/position'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetProperties']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/viam/api/v1/component/movementsensor/{name}/properties'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetAccuracy']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetAccuracy']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/viam/api/v1/component/movementsensor/{name}/accuracy'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetLinearAcceleration']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetLinearAcceleration']._serialized_options = b'\x82\xd3\xe4\x93\x02B\x12@/viam/api/v1/component/movementsensor/{name}/linear_acceleration'
    _MOVEMENTSENSORSERVICE.methods_by_name['DoCommand']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x029"7/viam/api/v1/component/movementsensor/{name}/do_command'
    _MOVEMENTSENSORSERVICE.methods_by_name['GetGeometries']._options = None
    _MOVEMENTSENSORSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/viam/api/v1/component/movementsensor/{name}/geometries'
    _GETLINEARVELOCITYREQUEST._serialized_start = 170
    _GETLINEARVELOCITYREQUEST._serialized_end = 263
    _GETLINEARVELOCITYRESPONSE._serialized_start = 265
    _GETLINEARVELOCITYRESPONSE._serialized_end = 358
    _GETANGULARVELOCITYREQUEST._serialized_start = 360
    _GETANGULARVELOCITYREQUEST._serialized_end = 454
    _GETANGULARVELOCITYRESPONSE._serialized_start = 456
    _GETANGULARVELOCITYRESPONSE._serialized_end = 552
    _GETCOMPASSHEADINGREQUEST._serialized_start = 554
    _GETCOMPASSHEADINGREQUEST._serialized_end = 647
    _GETCOMPASSHEADINGRESPONSE._serialized_start = 649
    _GETCOMPASSHEADINGRESPONSE._serialized_end = 698
    _GETORIENTATIONREQUEST._serialized_start = 700
    _GETORIENTATIONREQUEST._serialized_end = 790
    _GETORIENTATIONRESPONSE._serialized_start = 792
    _GETORIENTATIONRESPONSE._serialized_end = 879
    _GETPOSITIONREQUEST._serialized_start = 881
    _GETPOSITIONREQUEST._serialized_end = 968
    _GETPOSITIONRESPONSE._serialized_start = 970
    _GETPOSITIONRESPONSE._serialized_end = 1080
    _GETPROPERTIESREQUEST._serialized_start = 1082
    _GETPROPERTIESREQUEST._serialized_end = 1171
    _GETPROPERTIESRESPONSE._serialized_start = 1174
    _GETPROPERTIESRESPONSE._serialized_end = 1547
    _GETACCURACYREQUEST._serialized_start = 1549
    _GETACCURACYREQUEST._serialized_end = 1636
    _GETACCURACYRESPONSE._serialized_start = 1639
    _GETACCURACYRESPONSE._serialized_end = 1818
    _GETACCURACYRESPONSE_ACCURACYENTRY._serialized_start = 1759
    _GETACCURACYRESPONSE_ACCURACYENTRY._serialized_end = 1818
    _GETLINEARACCELERATIONREQUEST._serialized_start = 1820
    _GETLINEARACCELERATIONREQUEST._serialized_end = 1917
    _GETLINEARACCELERATIONRESPONSE._serialized_start = 1919
    _GETLINEARACCELERATIONRESPONSE._serialized_end = 2024
    _MOVEMENTSENSORSERVICE._serialized_start = 2027
    _MOVEMENTSENSORSERVICE._serialized_end = 4002