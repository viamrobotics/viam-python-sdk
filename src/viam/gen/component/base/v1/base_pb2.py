"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccomponent/base/v1/base.proto\x12\x16viam.component.base.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\x97\x01\n\x13MoveStraightRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bdistance_mm\x18\x02 \x01(\x03R\ndistanceMm\x12\x1c\n\nmm_per_sec\x18\x03 \x01(\x01R\x08mmPerSec\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x16\n\x14MoveStraightResponse"\x8f\x01\n\x0bSpinRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tangle_deg\x18\x02 \x01(\x01R\x08angleDeg\x12 \n\x0cdegs_per_sec\x18\x03 \x01(\x01R\ndegsPerSec\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cSpinResponse"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"\xb8\x01\n\x0fSetPowerRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12/\n\x06linear\x18\x02 \x01(\x0b2\x17.viam.common.v1.Vector3R\x06linear\x121\n\x07angular\x18\x03 \x01(\x0b2\x17.viam.common.v1.Vector3R\x07angular\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x12\n\x10SetPowerResponse"\xbb\x01\n\x12SetVelocityRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12/\n\x06linear\x18\x02 \x01(\x0b2\x17.viam.common.v1.Vector3R\x06linear\x121\n\x07angular\x18\x03 \x01(\x0b2\x17.viam.common.v1.Vector3R\x07angular\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x15\n\x13SetVelocityResponse"%\n\x0fIsMovingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x10IsMovingResponse\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving"Y\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xac\x01\n\x15GetPropertiesResponse\x12!\n\x0cwidth_meters\x18\x01 \x01(\x01R\x0bwidthMeters\x122\n\x15turning_radius_meters\x18\x02 \x01(\x01R\x13turningRadiusMeters\x12<\n\x1awheel_circumference_meters\x18\x03 \x01(\x01R\x18wheelCircumferenceMeters2\xe1\n\n\x0bBaseService\x12\xa7\x01\n\x0cMoveStraight\x12+.viam.component.base.v1.MoveStraightRequest\x1a,.viam.component.base.v1.MoveStraightResponse"<\xa0\x92)\x01\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/base/{name}/move_straight\x12\x86\x01\n\x04Spin\x12#.viam.component.base.v1.SpinRequest\x1a$.viam.component.base.v1.SpinResponse"3\xa0\x92)\x01\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/component/base/{name}/spin\x12\x97\x01\n\x08SetPower\x12\'.viam.component.base.v1.SetPowerRequest\x1a(.viam.component.base.v1.SetPowerResponse"8\xa0\x92)\x01\x82\xd3\xe4\x93\x02.",/viam/api/v1/component/base/{name}/set_power\x12\xa3\x01\n\x0bSetVelocity\x12*.viam.component.base.v1.SetVelocityRequest\x1a+.viam.component.base.v1.SetVelocityResponse";\xa0\x92)\x01\x82\xd3\xe4\x93\x021"//viam/api/v1/component/base/{name}/set_velocity\x12\x82\x01\n\x04Stop\x12#.viam.component.base.v1.StopRequest\x1a$.viam.component.base.v1.StopResponse"/\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/component/base/{name}/stop\x12\x93\x01\n\x08IsMoving\x12\'.viam.component.base.v1.IsMovingRequest\x1a(.viam.component.base.v1.IsMovingResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/base/{name}/is_moving\x12\x87\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/component/base/{name}/do_command\x12\x93\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/base/{name}/geometries\x12\xa3\x01\n\rGetProperties\x12,.viam.component.base.v1.GetPropertiesRequest\x1a-.viam.component.base.v1.GetPropertiesResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/base/{name}/propertiesB?\n\x1acom.viam.component.base.v1Z!go.viam.com/api/component/base/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.base.v1.base_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1acom.viam.component.base.v1Z!go.viam.com/api/component/base/v1'
    _BASESERVICE.methods_by_name['MoveStraight']._options = None
    _BASESERVICE.methods_by_name['MoveStraight']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/base/{name}/move_straight'
    _BASESERVICE.methods_by_name['Spin']._options = None
    _BASESERVICE.methods_by_name['Spin']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/component/base/{name}/spin'
    _BASESERVICE.methods_by_name['SetPower']._options = None
    _BASESERVICE.methods_by_name['SetPower']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02.",/viam/api/v1/component/base/{name}/set_power'
    _BASESERVICE.methods_by_name['SetVelocity']._options = None
    _BASESERVICE.methods_by_name['SetVelocity']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x021"//viam/api/v1/component/base/{name}/set_velocity'
    _BASESERVICE.methods_by_name['Stop']._options = None
    _BASESERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/component/base/{name}/stop'
    _BASESERVICE.methods_by_name['IsMoving']._options = None
    _BASESERVICE.methods_by_name['IsMoving']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/base/{name}/is_moving'
    _BASESERVICE.methods_by_name['DoCommand']._options = None
    _BASESERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/component/base/{name}/do_command'
    _BASESERVICE.methods_by_name['GetGeometries']._options = None
    _BASESERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/base/{name}/geometries'
    _BASESERVICE.methods_by_name['GetProperties']._options = None
    _BASESERVICE.methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/base/{name}/properties'
    _MOVESTRAIGHTREQUEST._serialized_start = 141
    _MOVESTRAIGHTREQUEST._serialized_end = 292
    _MOVESTRAIGHTRESPONSE._serialized_start = 294
    _MOVESTRAIGHTRESPONSE._serialized_end = 316
    _SPINREQUEST._serialized_start = 319
    _SPINREQUEST._serialized_end = 462
    _SPINRESPONSE._serialized_start = 464
    _SPINRESPONSE._serialized_end = 478
    _STOPREQUEST._serialized_start = 480
    _STOPREQUEST._serialized_end = 560
    _STOPRESPONSE._serialized_start = 562
    _STOPRESPONSE._serialized_end = 576
    _SETPOWERREQUEST._serialized_start = 579
    _SETPOWERREQUEST._serialized_end = 763
    _SETPOWERRESPONSE._serialized_start = 765
    _SETPOWERRESPONSE._serialized_end = 783
    _SETVELOCITYREQUEST._serialized_start = 786
    _SETVELOCITYREQUEST._serialized_end = 973
    _SETVELOCITYRESPONSE._serialized_start = 975
    _SETVELOCITYRESPONSE._serialized_end = 996
    _ISMOVINGREQUEST._serialized_start = 998
    _ISMOVINGREQUEST._serialized_end = 1035
    _ISMOVINGRESPONSE._serialized_start = 1037
    _ISMOVINGRESPONSE._serialized_end = 1084
    _GETPROPERTIESREQUEST._serialized_start = 1086
    _GETPROPERTIESREQUEST._serialized_end = 1175
    _GETPROPERTIESRESPONSE._serialized_start = 1178
    _GETPROPERTIESRESPONSE._serialized_end = 1350
    _BASESERVICE._serialized_start = 1353
    _BASESERVICE._serialized_end = 2730