"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'component/switch/v1/switch.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n component/switch/v1/switch.proto\x12\x18viam.component.switch.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"s\n\x12SetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1a\n\x08position\x18\x02 \x01(\rR\x08position\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x15\n\x13SetPositionResponse"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"1\n\x13GetPositionResponse\x12\x1a\n\x08position\x18\x01 \x01(\rR\x08position"`\n\x1bGetNumberOfPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"f\n\x1cGetNumberOfPositionsResponse\x12.\n\x13number_of_positions\x18\x01 \x01(\rR\x11numberOfPositions\x12\x16\n\x06labels\x18\x02 \x03(\tR\x06labels2\xb9\x05\n\rSwitchService\x12\xa5\x01\n\x0bSetPosition\x12,.viam.component.switch.v1.SetPositionRequest\x1a-.viam.component.switch.v1.SetPositionResponse"9\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/switch/{name}/set_position\x12\xa5\x01\n\x0bGetPosition\x12,.viam.component.switch.v1.GetPositionRequest\x1a-.viam.component.switch.v1.GetPositionResponse"9\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/switch/{name}/get_position\x12\xcb\x01\n\x14GetNumberOfPositions\x125.viam.component.switch.v1.GetNumberOfPositionsRequest\x1a6.viam.component.switch.v1.GetNumberOfPositionsResponse"D\x82\xd3\xe4\x93\x02>\x1a</viam/api/v1/component/switch/{name}/get_number_of_positions\x12\x89\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/component/switch/{name}/do_commandBC\n\x1ccom.viam.component.switch.v1Z#go.viam.com/api/component/switch/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.switch.v1.switch_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.viam.component.switch.v1Z#go.viam.com/api/component/switch/v1'
    _globals['_SWITCHSERVICE'].methods_by_name['SetPosition']._loaded_options = None
    _globals['_SWITCHSERVICE'].methods_by_name['SetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/switch/{name}/set_position'
    _globals['_SWITCHSERVICE'].methods_by_name['GetPosition']._loaded_options = None
    _globals['_SWITCHSERVICE'].methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/switch/{name}/get_position'
    _globals['_SWITCHSERVICE'].methods_by_name['GetNumberOfPositions']._loaded_options = None
    _globals['_SWITCHSERVICE'].methods_by_name['GetNumberOfPositions']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x1a</viam/api/v1/component/switch/{name}/get_number_of_positions'
    _globals['_SWITCHSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_SWITCHSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/component/switch/{name}/do_command'
    _globals['_SETPOSITIONREQUEST']._serialized_start = 146
    _globals['_SETPOSITIONREQUEST']._serialized_end = 261
    _globals['_SETPOSITIONRESPONSE']._serialized_start = 263
    _globals['_SETPOSITIONRESPONSE']._serialized_end = 284
    _globals['_GETPOSITIONREQUEST']._serialized_start = 286
    _globals['_GETPOSITIONREQUEST']._serialized_end = 373
    _globals['_GETPOSITIONRESPONSE']._serialized_start = 375
    _globals['_GETPOSITIONRESPONSE']._serialized_end = 424
    _globals['_GETNUMBEROFPOSITIONSREQUEST']._serialized_start = 426
    _globals['_GETNUMBEROFPOSITIONSREQUEST']._serialized_end = 522
    _globals['_GETNUMBEROFPOSITIONSRESPONSE']._serialized_start = 524
    _globals['_GETNUMBEROFPOSITIONSRESPONSE']._serialized_end = 626
    _globals['_SWITCHSERVICE']._serialized_start = 629
    _globals['_SWITCHSERVICE']._serialized_end = 1326