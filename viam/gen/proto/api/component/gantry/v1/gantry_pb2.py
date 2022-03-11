"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*proto/api/component/gantry/v1/gantry.proto\x12\x1dproto.api.component.gantry.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"8\n\x13GetPositionResponse\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm"\xa5\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cpositions_mm\x18\x02 \x03(\x01R\x0bpositionsMm\x12E\n\x0bworld_state\x18\x03 \x01(\x0b2\x1f.proto.api.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01B\x0e\n\x0c_world_state"\x18\n\x16MoveToPositionResponse"\'\n\x11GetLengthsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"3\n\x12GetLengthsResponse\x12\x1d\n\nlengths_mm\x18\x01 \x03(\x01R\tlengthsMm"J\n\x06Status\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm\x12\x1d\n\nlengths_mm\x18\x02 \x03(\x01R\tlengthsMm2\x9e\x04\n\rGantryService\x12\xab\x01\n\x0bGetPosition\x121.proto.api.component.gantry.v1.GetPositionRequest\x1a2.proto.api.component.gantry.v1.GetPositionResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/gantry/{name}/position\x12\xb4\x01\n\x0eMoveToPosition\x124.proto.api.component.gantry.v1.MoveToPositionRequest\x1a5.proto.api.component.gantry.v1.MoveToPositionResponse"5\x82\xd3\xe4\x93\x02/\x1a-/viam/api/v1/component/gantry/{name}/position\x12\xa7\x01\n\nGetLengths\x120.proto.api.component.gantry.v1.GetLengthsRequest\x1a1.proto.api.component.gantry.v1.GetLengthsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/gantry/{name}/lengthsB[\n*com.viam.rdk.proto.api.component.gantry.v1Z-go.viam.com/rdk/proto/api/component/gantry/v1b\x06proto3')
_GETPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['GetPositionRequest']
_GETPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['GetPositionResponse']
_MOVETOPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['MoveToPositionRequest']
_MOVETOPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['MoveToPositionResponse']
_GETLENGTHSREQUEST = DESCRIPTOR.message_types_by_name['GetLengthsRequest']
_GETLENGTHSRESPONSE = DESCRIPTOR.message_types_by_name['GetLengthsResponse']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
GetPositionRequest = _reflection.GeneratedProtocolMessageType('GetPositionRequest', (_message.Message,), {'DESCRIPTOR': _GETPOSITIONREQUEST, '__module__': 'proto.api.component.gantry.v1.gantry_pb2'})
_sym_db.RegisterMessage(GetPositionRequest)
GetPositionResponse = _reflection.GeneratedProtocolMessageType('GetPositionResponse', (_message.Message,), {'DESCRIPTOR': _GETPOSITIONRESPONSE, '__module__': 'proto.api.component.gantry.v1.gantry_pb2'})
_sym_db.RegisterMessage(GetPositionResponse)
MoveToPositionRequest = _reflection.GeneratedProtocolMessageType('MoveToPositionRequest', (_message.Message,), {'DESCRIPTOR': _MOVETOPOSITIONREQUEST, '__module__': 'proto.api.component.gantry.v1.gantry_pb2'})
_sym_db.RegisterMessage(MoveToPositionRequest)
MoveToPositionResponse = _reflection.GeneratedProtocolMessageType('MoveToPositionResponse', (_message.Message,), {'DESCRIPTOR': _MOVETOPOSITIONRESPONSE, '__module__': 'proto.api.component.gantry.v1.gantry_pb2'})
_sym_db.RegisterMessage(MoveToPositionResponse)
GetLengthsRequest = _reflection.GeneratedProtocolMessageType('GetLengthsRequest', (_message.Message,), {'DESCRIPTOR': _GETLENGTHSREQUEST, '__module__': 'proto.api.component.gantry.v1.gantry_pb2'})
_sym_db.RegisterMessage(GetLengthsRequest)
GetLengthsResponse = _reflection.GeneratedProtocolMessageType('GetLengthsResponse', (_message.Message,), {'DESCRIPTOR': _GETLENGTHSRESPONSE, '__module__': 'proto.api.component.gantry.v1.gantry_pb2'})
_sym_db.RegisterMessage(GetLengthsResponse)
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {'DESCRIPTOR': _STATUS, '__module__': 'proto.api.component.gantry.v1.gantry_pb2'})
_sym_db.RegisterMessage(Status)
_GANTRYSERVICE = DESCRIPTOR.services_by_name['GantryService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n*com.viam.rdk.proto.api.component.gantry.v1Z-go.viam.com/rdk/proto/api/component/gantry/v1'
    _GANTRYSERVICE.methods_by_name['GetPosition']._options = None
    _GANTRYSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/gantry/{name}/position'
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._options = None
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x1a-/viam/api/v1/component/gantry/{name}/position'
    _GANTRYSERVICE.methods_by_name['GetLengths']._options = None
    _GANTRYSERVICE.methods_by_name['GetLengths']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/gantry/{name}/lengths'
    _GETPOSITIONREQUEST._serialized_start = 141
    _GETPOSITIONREQUEST._serialized_end = 181
    _GETPOSITIONRESPONSE._serialized_start = 183
    _GETPOSITIONRESPONSE._serialized_end = 239
    _MOVETOPOSITIONREQUEST._serialized_start = 242
    _MOVETOPOSITIONREQUEST._serialized_end = 407
    _MOVETOPOSITIONRESPONSE._serialized_start = 409
    _MOVETOPOSITIONRESPONSE._serialized_end = 433
    _GETLENGTHSREQUEST._serialized_start = 435
    _GETLENGTHSREQUEST._serialized_end = 474
    _GETLENGTHSRESPONSE._serialized_start = 476
    _GETLENGTHSRESPONSE._serialized_end = 527
    _STATUS._serialized_start = 529
    _STATUS._serialized_end = 603
    _GANTRYSERVICE._serialized_start = 606
    _GANTRYSERVICE._serialized_end = 1148