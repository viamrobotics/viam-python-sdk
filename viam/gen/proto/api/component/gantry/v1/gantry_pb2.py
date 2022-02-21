"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*proto/api/component/gantry/v1/gantry.proto\x12\x1dproto.api.component.gantry.v1\x1a\x1cgoogle/api/annotations.proto"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"8\n\x13GetPositionResponse\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm"N\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cpositions_mm\x18\x02 \x03(\x01R\x0bpositionsMm"\x18\n\x16MoveToPositionResponse"\'\n\x11GetLengthsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"3\n\x12GetLengthsResponse\x12\x1d\n\nlengths_mm\x18\x01 \x03(\x01R\tlengthsMm2\x9f\x04\n\rGantryService\x12\xae\x01\n\x0bGetPosition\x121.proto.api.component.gantry.v1.GetPositionRequest\x1a2.proto.api.component.gantry.v1.GetPositionResponse"8\x82\xd3\xe4\x93\x022\x120/api/v1/component/gantry/{name}/current_position\x12\xb7\x01\n\x0eMoveToPosition\x124.proto.api.component.gantry.v1.MoveToPositionRequest\x1a5.proto.api.component.gantry.v1.MoveToPositionResponse"8\x82\xd3\xe4\x93\x022\x1a0/api/v1/component/gantry/{name}/move_to_position\x12\xa2\x01\n\nGetLengths\x120.proto.api.component.gantry.v1.GetLengthsRequest\x1a1.proto.api.component.gantry.v1.GetLengthsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/component/gantry/{name}/lengthsBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_GETPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['GetPositionRequest']
_GETPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['GetPositionResponse']
_MOVETOPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['MoveToPositionRequest']
_MOVETOPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['MoveToPositionResponse']
_GETLENGTHSREQUEST = DESCRIPTOR.message_types_by_name['GetLengthsRequest']
_GETLENGTHSRESPONSE = DESCRIPTOR.message_types_by_name['GetLengthsResponse']
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
_GANTRYSERVICE = DESCRIPTOR.services_by_name['GantryService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _GANTRYSERVICE.methods_by_name['GetPosition']._options = None
    _GANTRYSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/api/v1/component/gantry/{name}/current_position'
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._options = None
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\x82\xd3\xe4\x93\x022\x1a0/api/v1/component/gantry/{name}/move_to_position'
    _GANTRYSERVICE.methods_by_name['GetLengths']._options = None
    _GANTRYSERVICE.methods_by_name['GetLengths']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/api/v1/component/gantry/{name}/lengths"
    _GETPOSITIONREQUEST._serialized_start = 107
    _GETPOSITIONREQUEST._serialized_end = 147
    _GETPOSITIONRESPONSE._serialized_start = 149
    _GETPOSITIONRESPONSE._serialized_end = 205
    _MOVETOPOSITIONREQUEST._serialized_start = 207
    _MOVETOPOSITIONREQUEST._serialized_end = 285
    _MOVETOPOSITIONRESPONSE._serialized_start = 287
    _MOVETOPOSITIONRESPONSE._serialized_end = 311
    _GETLENGTHSREQUEST._serialized_start = 313
    _GETLENGTHSREQUEST._serialized_end = 352
    _GETLENGTHSRESPONSE._serialized_start = 354
    _GETLENGTHSRESPONSE._serialized_end = 405
    _GANTRYSERVICE._serialized_start = 408
    _GANTRYSERVICE._serialized_end = 951