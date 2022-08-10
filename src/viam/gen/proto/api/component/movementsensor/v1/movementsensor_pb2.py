"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:proto/api/component/movementsensor/v1/movementsensor.proto\x12%proto.api.component.movementsensor.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto".\n\x18GetLinearVelocityRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"b\n\x19GetLinearVelocityResponse\x12E\n\x0flinear_velocity\x18\x01 \x01(\x0b2\x1c.proto.api.common.v1.Vector3R\x0elinearVelocity"/\n\x19GetAngularVelocityRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"e\n\x1aGetAngularVelocityResponse\x12G\n\x10angular_velocity\x18\x01 \x01(\x0b2\x1c.proto.api.common.v1.Vector3R\x0fangularVelocity".\n\x18GetCompassHeadingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"1\n\x19GetCompassHeadingResponse\x12\x14\n\x05value\x18\x01 \x01(\x01R\x05value"+\n\x15GetOrientationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\\\n\x16GetOrientationResponse\x12B\n\x0borientation\x18\x01 \x01(\x0b2 .proto.api.common.v1.OrientationR\x0borientation"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"u\n\x13GetPositionResponse\x12=\n\ncoordinate\x18\x01 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\ncoordinate\x12\x1f\n\x0baltitude_mm\x18\x02 \x01(\x02R\naltitudeMm"*\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\xb1\x02\n\x15GetPropertiesResponse\x12:\n\x19linear_velocity_supported\x18\x01 \x01(\x08R\x17linearVelocitySupported\x12<\n\x1aangular_velocity_supported\x18\x02 \x01(\x08R\x18angularVelocitySupported\x123\n\x15orientation_supported\x18\x03 \x01(\x08R\x14orientationSupported\x12-\n\x12position_supported\x18\x04 \x01(\x08R\x11positionSupported\x12:\n\x19compass_heading_supported\x18\x05 \x01(\x08R\x17compassHeadingSupported"(\n\x12GetAccuracyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\xc1\x01\n\x13GetAccuracyResponse\x12k\n\x0baccuracy_mm\x18\x01 \x03(\x0b2J.proto.api.component.movementsensor.v1.GetAccuracyResponse.AccuracyMmEntryR\naccuracyMm\x1a=\n\x0fAccuracyMmEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x02R\x05value:\x028\x012\xe4\x0b\n\x15MovementSensorService\x12\xdc\x01\n\x11GetLinearVelocity\x12?.proto.api.component.movementsensor.v1.GetLinearVelocityRequest\x1a@.proto.api.component.movementsensor.v1.GetLinearVelocityResponse"D\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/component/movementsensor/{name}/linear_velocity\x12\xe0\x01\n\x12GetAngularVelocity\x12@.proto.api.component.movementsensor.v1.GetAngularVelocityRequest\x1aA.proto.api.component.movementsensor.v1.GetAngularVelocityResponse"E\x82\xd3\xe4\x93\x02?\x12=/viam/api/v1/component/movementsensor/{name}/angular_velocity\x12\xdc\x01\n\x11GetCompassHeading\x12?.proto.api.component.movementsensor.v1.GetCompassHeadingRequest\x1a@.proto.api.component.movementsensor.v1.GetCompassHeadingResponse"D\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/component/movementsensor/{name}/compass_heading\x12\xcf\x01\n\x0eGetOrientation\x12<.proto.api.component.movementsensor.v1.GetOrientationRequest\x1a=.proto.api.component.movementsensor.v1.GetOrientationResponse"@\x82\xd3\xe4\x93\x02:\x128/viam/api/v1/component/movementsensor/{name}/orientation\x12\xc3\x01\n\x0bGetPosition\x129.proto.api.component.movementsensor.v1.GetPositionRequest\x1a:.proto.api.component.movementsensor.v1.GetPositionResponse"=\x82\xd3\xe4\x93\x027\x125/viam/api/v1/component/movementsensor/{name}/position\x12\xcb\x01\n\rGetProperties\x12;.proto.api.component.movementsensor.v1.GetPropertiesRequest\x1a<.proto.api.component.movementsensor.v1.GetPropertiesResponse"?\x82\xd3\xe4\x93\x029\x127/viam/api/v1/component/movementsensor/{name}/properties\x12\xc3\x01\n\x0bGetAccuracy\x129.proto.api.component.movementsensor.v1.GetAccuracyRequest\x1a:.proto.api.component.movementsensor.v1.GetAccuracyResponse"=\x82\xd3\xe4\x93\x027\x125/viam/api/v1/component/movementsensor/{name}/accuracyBk\n2com.viam.rdk.proto.api.component.movementsensor.v1Z5go.viam.com/rdk/proto/api/component/movementsensor/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.movementsensor.v1.movementsensor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.viam.rdk.proto.api.component.movementsensor.v1Z5go.viam.com/rdk/proto/api/component/movementsensor/v1'
    _GETACCURACYRESPONSE_ACCURACYMMENTRY._options = None
    _GETACCURACYRESPONSE_ACCURACYMMENTRY._serialized_options = b'8\x01'
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
    _GETLINEARVELOCITYREQUEST._serialized_start = 165
    _GETLINEARVELOCITYREQUEST._serialized_end = 211
    _GETLINEARVELOCITYRESPONSE._serialized_start = 213
    _GETLINEARVELOCITYRESPONSE._serialized_end = 311
    _GETANGULARVELOCITYREQUEST._serialized_start = 313
    _GETANGULARVELOCITYREQUEST._serialized_end = 360
    _GETANGULARVELOCITYRESPONSE._serialized_start = 362
    _GETANGULARVELOCITYRESPONSE._serialized_end = 463
    _GETCOMPASSHEADINGREQUEST._serialized_start = 465
    _GETCOMPASSHEADINGREQUEST._serialized_end = 511
    _GETCOMPASSHEADINGRESPONSE._serialized_start = 513
    _GETCOMPASSHEADINGRESPONSE._serialized_end = 562
    _GETORIENTATIONREQUEST._serialized_start = 564
    _GETORIENTATIONREQUEST._serialized_end = 607
    _GETORIENTATIONRESPONSE._serialized_start = 609
    _GETORIENTATIONRESPONSE._serialized_end = 701
    _GETPOSITIONREQUEST._serialized_start = 703
    _GETPOSITIONREQUEST._serialized_end = 743
    _GETPOSITIONRESPONSE._serialized_start = 745
    _GETPOSITIONRESPONSE._serialized_end = 862
    _GETPROPERTIESREQUEST._serialized_start = 864
    _GETPROPERTIESREQUEST._serialized_end = 906
    _GETPROPERTIESRESPONSE._serialized_start = 909
    _GETPROPERTIESRESPONSE._serialized_end = 1214
    _GETACCURACYREQUEST._serialized_start = 1216
    _GETACCURACYREQUEST._serialized_end = 1256
    _GETACCURACYRESPONSE._serialized_start = 1259
    _GETACCURACYRESPONSE._serialized_end = 1452
    _GETACCURACYRESPONSE_ACCURACYMMENTRY._serialized_start = 1391
    _GETACCURACYRESPONSE_ACCURACYMMENTRY._serialized_end = 1452
    _MOVEMENTSENSORSERVICE._serialized_start = 1455
    _MOVEMENTSENSORSERVICE._serialized_end = 2963