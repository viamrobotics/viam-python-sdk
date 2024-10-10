"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'component/gripper/v1/gripper.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"component/gripper/v1/gripper.proto\x12\x19viam.component.gripper.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"P\n\x0bOpenRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cOpenResponse"P\n\x0bGrabRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"W\n\x0cGrabResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"%\n\x0fIsMovingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x10IsMovingResponse\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving2\x87\x07\n\x0eGripperService\x12\x8f\x01\n\x04Open\x12&.viam.component.gripper.v1.OpenRequest\x1a\'.viam.component.gripper.v1.OpenResponse"6\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/open\x12\x8f\x01\n\x04Grab\x12&.viam.component.gripper.v1.GrabRequest\x1a\'.viam.component.gripper.v1.GrabResponse"6\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/grab\x12\x8b\x01\n\x04Stop\x12&.viam.component.gripper.v1.StopRequest\x1a\'.viam.component.gripper.v1.StopResponse"2\x82\xd3\xe4\x93\x02,"*/viam/api/v1/component/gripper/{name}/stop\x12\x9c\x01\n\x08IsMoving\x12*.viam.component.gripper.v1.IsMovingRequest\x1a+.viam.component.gripper.v1.IsMovingResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/gripper/{name}/is_moving\x12\x8a\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/gripper/{name}/do_command\x12\x96\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/gripper/{name}/geometriesBE\n\x1dcom.viam.component.gripper.v1Z$go.viam.com/api/component/gripper/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.gripper.v1.gripper_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.viam.component.gripper.v1Z$go.viam.com/api/component/gripper/v1'
    _globals['_GRIPPERSERVICE'].methods_by_name['Open']._loaded_options = None
    _globals['_GRIPPERSERVICE'].methods_by_name['Open']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/open'
    _globals['_GRIPPERSERVICE'].methods_by_name['Grab']._loaded_options = None
    _globals['_GRIPPERSERVICE'].methods_by_name['Grab']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/grab'
    _globals['_GRIPPERSERVICE'].methods_by_name['Stop']._loaded_options = None
    _globals['_GRIPPERSERVICE'].methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02,"*/viam/api/v1/component/gripper/{name}/stop'
    _globals['_GRIPPERSERVICE'].methods_by_name['IsMoving']._loaded_options = None
    _globals['_GRIPPERSERVICE'].methods_by_name['IsMoving']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/gripper/{name}/is_moving'
    _globals['_GRIPPERSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_GRIPPERSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/gripper/{name}/do_command'
    _globals['_GRIPPERSERVICE'].methods_by_name['GetGeometries']._loaded_options = None
    _globals['_GRIPPERSERVICE'].methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/gripper/{name}/geometries'
    _globals['_OPENREQUEST']._serialized_start = 149
    _globals['_OPENREQUEST']._serialized_end = 229
    _globals['_OPENRESPONSE']._serialized_start = 231
    _globals['_OPENRESPONSE']._serialized_end = 245
    _globals['_GRABREQUEST']._serialized_start = 247
    _globals['_GRABREQUEST']._serialized_end = 327
    _globals['_GRABRESPONSE']._serialized_start = 329
    _globals['_GRABRESPONSE']._serialized_end = 416
    _globals['_STOPREQUEST']._serialized_start = 418
    _globals['_STOPREQUEST']._serialized_end = 498
    _globals['_STOPRESPONSE']._serialized_start = 500
    _globals['_STOPRESPONSE']._serialized_end = 514
    _globals['_ISMOVINGREQUEST']._serialized_start = 516
    _globals['_ISMOVINGREQUEST']._serialized_end = 553
    _globals['_ISMOVINGRESPONSE']._serialized_start = 555
    _globals['_ISMOVINGRESPONSE']._serialized_end = 602
    _globals['_GRIPPERSERVICE']._serialized_start = 605
    _globals['_GRIPPERSERVICE']._serialized_end = 1508