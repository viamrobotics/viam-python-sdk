"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#proto/api/component/v1/gantry.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto"5\n\x1fGantryServiceGetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"E\n GantryServiceGetPositionResponse\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm"[\n"GantryServiceMoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cpositions_mm\x18\x02 \x03(\x01R\x0bpositionsMm"%\n#GantryServiceMoveToPositionResponse"4\n\x1eGantryServiceGetLengthsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"@\n\x1fGantryServiceGetLengthsResponse\x12\x1d\n\nlengths_mm\x18\x01 \x03(\x01R\tlengthsMm2\xc3\x04\n\rGantryService\x12\xba\x01\n\x0bGetPosition\x127.proto.api.component.v1.GantryServiceGetPositionRequest\x1a8.proto.api.component.v1.GantryServiceGetPositionResponse"8\x82\xd3\xe4\x93\x022\x120/api/v1/component/gantry/{name}/current_position\x12\xc3\x01\n\x0eMoveToPosition\x12:.proto.api.component.v1.GantryServiceMoveToPositionRequest\x1a;.proto.api.component.v1.GantryServiceMoveToPositionResponse"8\x82\xd3\xe4\x93\x022\x1a0/api/v1/component/gantry/{name}/move_to_position\x12\xae\x01\n\nGetLengths\x126.proto.api.component.v1.GantryServiceGetLengthsRequest\x1a7.proto.api.component.v1.GantryServiceGetLengthsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/component/gantry/{name}/lengthsBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_GANTRYSERVICEGETPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['GantryServiceGetPositionRequest']
_GANTRYSERVICEGETPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['GantryServiceGetPositionResponse']
_GANTRYSERVICEMOVETOPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['GantryServiceMoveToPositionRequest']
_GANTRYSERVICEMOVETOPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['GantryServiceMoveToPositionResponse']
_GANTRYSERVICEGETLENGTHSREQUEST = DESCRIPTOR.message_types_by_name['GantryServiceGetLengthsRequest']
_GANTRYSERVICEGETLENGTHSRESPONSE = DESCRIPTOR.message_types_by_name['GantryServiceGetLengthsResponse']
GantryServiceGetPositionRequest = _reflection.GeneratedProtocolMessageType('GantryServiceGetPositionRequest', (_message.Message,), {'DESCRIPTOR': _GANTRYSERVICEGETPOSITIONREQUEST, '__module__': 'proto.api.component.v1.gantry_pb2'})
_sym_db.RegisterMessage(GantryServiceGetPositionRequest)
GantryServiceGetPositionResponse = _reflection.GeneratedProtocolMessageType('GantryServiceGetPositionResponse', (_message.Message,), {'DESCRIPTOR': _GANTRYSERVICEGETPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.gantry_pb2'})
_sym_db.RegisterMessage(GantryServiceGetPositionResponse)
GantryServiceMoveToPositionRequest = _reflection.GeneratedProtocolMessageType('GantryServiceMoveToPositionRequest', (_message.Message,), {'DESCRIPTOR': _GANTRYSERVICEMOVETOPOSITIONREQUEST, '__module__': 'proto.api.component.v1.gantry_pb2'})
_sym_db.RegisterMessage(GantryServiceMoveToPositionRequest)
GantryServiceMoveToPositionResponse = _reflection.GeneratedProtocolMessageType('GantryServiceMoveToPositionResponse', (_message.Message,), {'DESCRIPTOR': _GANTRYSERVICEMOVETOPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.gantry_pb2'})
_sym_db.RegisterMessage(GantryServiceMoveToPositionResponse)
GantryServiceGetLengthsRequest = _reflection.GeneratedProtocolMessageType('GantryServiceGetLengthsRequest', (_message.Message,), {'DESCRIPTOR': _GANTRYSERVICEGETLENGTHSREQUEST, '__module__': 'proto.api.component.v1.gantry_pb2'})
_sym_db.RegisterMessage(GantryServiceGetLengthsRequest)
GantryServiceGetLengthsResponse = _reflection.GeneratedProtocolMessageType('GantryServiceGetLengthsResponse', (_message.Message,), {'DESCRIPTOR': _GANTRYSERVICEGETLENGTHSRESPONSE, '__module__': 'proto.api.component.v1.gantry_pb2'})
_sym_db.RegisterMessage(GantryServiceGetLengthsResponse)
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
    _GANTRYSERVICEGETPOSITIONREQUEST._serialized_start = 93
    _GANTRYSERVICEGETPOSITIONREQUEST._serialized_end = 146
    _GANTRYSERVICEGETPOSITIONRESPONSE._serialized_start = 148
    _GANTRYSERVICEGETPOSITIONRESPONSE._serialized_end = 217
    _GANTRYSERVICEMOVETOPOSITIONREQUEST._serialized_start = 219
    _GANTRYSERVICEMOVETOPOSITIONREQUEST._serialized_end = 310
    _GANTRYSERVICEMOVETOPOSITIONRESPONSE._serialized_start = 312
    _GANTRYSERVICEMOVETOPOSITIONRESPONSE._serialized_end = 349
    _GANTRYSERVICEGETLENGTHSREQUEST._serialized_start = 351
    _GANTRYSERVICEGETLENGTHSREQUEST._serialized_end = 403
    _GANTRYSERVICEGETLENGTHSRESPONSE._serialized_start = 405
    _GANTRYSERVICEGETLENGTHSRESPONSE._serialized_end = 469
    _GANTRYSERVICE._serialized_start = 472
    _GANTRYSERVICE._serialized_end = 1051