"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!proto/api/component/v1/base.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto"\x89\x01\n\x1eBaseServiceMoveStraightRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bdistance_mm\x18\x02 \x01(\x03R\ndistanceMm\x12\x1c\n\nmm_per_sec\x18\x03 \x01(\x01R\x08mmPerSec\x12\x14\n\x05block\x18\x04 \x01(\x08R\x05block"!\n\x1fBaseServiceMoveStraightResponse"\xa1\x01\n\x19BaseServiceMoveArcRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bdistance_mm\x18\x02 \x01(\x03R\ndistanceMm\x12\x1c\n\nmm_per_sec\x18\x03 \x01(\x01R\x08mmPerSec\x12\x1b\n\tangle_deg\x18\x04 \x01(\x01R\x08angleDeg\x12\x14\n\x05block\x18\x05 \x01(\x08R\x05block"\x1c\n\x1aBaseServiceMoveArcResponse"\x81\x01\n\x16BaseServiceSpinRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tangle_deg\x18\x02 \x01(\x01R\x08angleDeg\x12 \n\x0cdegs_per_sec\x18\x03 \x01(\x01R\ndegsPerSec\x12\x14\n\x05block\x18\x04 \x01(\x08R\x05block"\x19\n\x17BaseServiceSpinResponse",\n\x16BaseServiceStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x19\n\x17BaseServiceStopResponse2\x93\x05\n\x0bBaseService\x12\xb4\x01\n\x0cMoveStraight\x126.proto.api.component.v1.BaseServiceMoveStraightRequest\x1a7.proto.api.component.v1.BaseServiceMoveStraightResponse"3\x82\xd3\xe4\x93\x02-"+/api/v1/component/base/{name}/move_straight\x12\xa0\x01\n\x07MoveArc\x121.proto.api.component.v1.BaseServiceMoveArcRequest\x1a2.proto.api.component.v1.BaseServiceMoveArcResponse".\x82\xd3\xe4\x93\x02("&/api/v1/component/base/{name}/move_arc\x12\x93\x01\n\x04Spin\x12..proto.api.component.v1.BaseServiceSpinRequest\x1a/.proto.api.component.v1.BaseServiceSpinResponse"*\x82\xd3\xe4\x93\x02$""/api/v1/component/base/{name}/spin\x12\x93\x01\n\x04Stop\x12..proto.api.component.v1.BaseServiceStopRequest\x1a/.proto.api.component.v1.BaseServiceStopResponse"*\x82\xd3\xe4\x93\x02$""/api/v1/component/base/{name}/stopBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_BASESERVICEMOVESTRAIGHTREQUEST = DESCRIPTOR.message_types_by_name['BaseServiceMoveStraightRequest']
_BASESERVICEMOVESTRAIGHTRESPONSE = DESCRIPTOR.message_types_by_name['BaseServiceMoveStraightResponse']
_BASESERVICEMOVEARCREQUEST = DESCRIPTOR.message_types_by_name['BaseServiceMoveArcRequest']
_BASESERVICEMOVEARCRESPONSE = DESCRIPTOR.message_types_by_name['BaseServiceMoveArcResponse']
_BASESERVICESPINREQUEST = DESCRIPTOR.message_types_by_name['BaseServiceSpinRequest']
_BASESERVICESPINRESPONSE = DESCRIPTOR.message_types_by_name['BaseServiceSpinResponse']
_BASESERVICESTOPREQUEST = DESCRIPTOR.message_types_by_name['BaseServiceStopRequest']
_BASESERVICESTOPRESPONSE = DESCRIPTOR.message_types_by_name['BaseServiceStopResponse']
BaseServiceMoveStraightRequest = _reflection.GeneratedProtocolMessageType('BaseServiceMoveStraightRequest', (_message.Message,), {'DESCRIPTOR': _BASESERVICEMOVESTRAIGHTREQUEST, '__module__': 'proto.api.component.v1.base_pb2'})
_sym_db.RegisterMessage(BaseServiceMoveStraightRequest)
BaseServiceMoveStraightResponse = _reflection.GeneratedProtocolMessageType('BaseServiceMoveStraightResponse', (_message.Message,), {'DESCRIPTOR': _BASESERVICEMOVESTRAIGHTRESPONSE, '__module__': 'proto.api.component.v1.base_pb2'})
_sym_db.RegisterMessage(BaseServiceMoveStraightResponse)
BaseServiceMoveArcRequest = _reflection.GeneratedProtocolMessageType('BaseServiceMoveArcRequest', (_message.Message,), {'DESCRIPTOR': _BASESERVICEMOVEARCREQUEST, '__module__': 'proto.api.component.v1.base_pb2'})
_sym_db.RegisterMessage(BaseServiceMoveArcRequest)
BaseServiceMoveArcResponse = _reflection.GeneratedProtocolMessageType('BaseServiceMoveArcResponse', (_message.Message,), {'DESCRIPTOR': _BASESERVICEMOVEARCRESPONSE, '__module__': 'proto.api.component.v1.base_pb2'})
_sym_db.RegisterMessage(BaseServiceMoveArcResponse)
BaseServiceSpinRequest = _reflection.GeneratedProtocolMessageType('BaseServiceSpinRequest', (_message.Message,), {'DESCRIPTOR': _BASESERVICESPINREQUEST, '__module__': 'proto.api.component.v1.base_pb2'})
_sym_db.RegisterMessage(BaseServiceSpinRequest)
BaseServiceSpinResponse = _reflection.GeneratedProtocolMessageType('BaseServiceSpinResponse', (_message.Message,), {'DESCRIPTOR': _BASESERVICESPINRESPONSE, '__module__': 'proto.api.component.v1.base_pb2'})
_sym_db.RegisterMessage(BaseServiceSpinResponse)
BaseServiceStopRequest = _reflection.GeneratedProtocolMessageType('BaseServiceStopRequest', (_message.Message,), {'DESCRIPTOR': _BASESERVICESTOPREQUEST, '__module__': 'proto.api.component.v1.base_pb2'})
_sym_db.RegisterMessage(BaseServiceStopRequest)
BaseServiceStopResponse = _reflection.GeneratedProtocolMessageType('BaseServiceStopResponse', (_message.Message,), {'DESCRIPTOR': _BASESERVICESTOPRESPONSE, '__module__': 'proto.api.component.v1.base_pb2'})
_sym_db.RegisterMessage(BaseServiceStopResponse)
_BASESERVICE = DESCRIPTOR.services_by_name['BaseService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _BASESERVICE.methods_by_name['MoveStraight']._options = None
    _BASESERVICE.methods_by_name['MoveStraight']._serialized_options = b'\x82\xd3\xe4\x93\x02-"+/api/v1/component/base/{name}/move_straight'
    _BASESERVICE.methods_by_name['MoveArc']._options = None
    _BASESERVICE.methods_by_name['MoveArc']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/api/v1/component/base/{name}/move_arc'
    _BASESERVICE.methods_by_name['Spin']._options = None
    _BASESERVICE.methods_by_name['Spin']._serialized_options = b'\x82\xd3\xe4\x93\x02$""/api/v1/component/base/{name}/spin'
    _BASESERVICE.methods_by_name['Stop']._options = None
    _BASESERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02$""/api/v1/component/base/{name}/stop'
    _BASESERVICEMOVESTRAIGHTREQUEST._serialized_start = 92
    _BASESERVICEMOVESTRAIGHTREQUEST._serialized_end = 229
    _BASESERVICEMOVESTRAIGHTRESPONSE._serialized_start = 231
    _BASESERVICEMOVESTRAIGHTRESPONSE._serialized_end = 264
    _BASESERVICEMOVEARCREQUEST._serialized_start = 267
    _BASESERVICEMOVEARCREQUEST._serialized_end = 428
    _BASESERVICEMOVEARCRESPONSE._serialized_start = 430
    _BASESERVICEMOVEARCRESPONSE._serialized_end = 458
    _BASESERVICESPINREQUEST._serialized_start = 461
    _BASESERVICESPINREQUEST._serialized_end = 590
    _BASESERVICESPINRESPONSE._serialized_start = 592
    _BASESERVICESPINRESPONSE._serialized_end = 617
    _BASESERVICESTOPREQUEST._serialized_start = 619
    _BASESERVICESTOPREQUEST._serialized_end = 663
    _BASESERVICESTOPRESPONSE._serialized_start = 665
    _BASESERVICESTOPRESPONSE._serialized_end = 690
    _BASESERVICE._serialized_start = 693
    _BASESERVICE._serialized_end = 1352