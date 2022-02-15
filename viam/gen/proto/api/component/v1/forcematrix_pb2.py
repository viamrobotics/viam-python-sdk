"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/component/v1/forcematrix.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto"D\n\x06Matrix\x12\x12\n\x04rows\x18\x01 \x01(\rR\x04rows\x12\x12\n\x04cols\x18\x02 \x01(\rR\x04cols\x12\x12\n\x04data\x18\x03 \x03(\rR\x04data"9\n#ForceMatrixServiceReadMatrixRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"^\n$ForceMatrixServiceReadMatrixResponse\x126\n\x06matrix\x18\x01 \x01(\x0b2\x1e.proto.api.component.v1.MatrixR\x06matrix"9\n#ForceMatrixServiceDetectSlipRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"K\n$ForceMatrixServiceDetectSlipResponse\x12#\n\rslip_detected\x18\x01 \x01(\x08R\x0cslipDetected2\x9c\x03\n\x12ForceMatrixService\x12\xbd\x01\n\nReadMatrix\x12;.proto.api.component.v1.ForceMatrixServiceReadMatrixRequest\x1a<.proto.api.component.v1.ForceMatrixServiceReadMatrixResponse"4\x82\xd3\xe4\x93\x02.\x12,/api/v1/component/force_matrix/{name}/matrix\x12\xc5\x01\n\nDetectSlip\x12;.proto.api.component.v1.ForceMatrixServiceDetectSlipRequest\x1a<.proto.api.component.v1.ForceMatrixServiceDetectSlipResponse"<\x82\xd3\xe4\x93\x026\x124/api/v1/component/force_matrix/{name}/slip_detectionBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_MATRIX = DESCRIPTOR.message_types_by_name['Matrix']
_FORCEMATRIXSERVICEREADMATRIXREQUEST = DESCRIPTOR.message_types_by_name['ForceMatrixServiceReadMatrixRequest']
_FORCEMATRIXSERVICEREADMATRIXRESPONSE = DESCRIPTOR.message_types_by_name['ForceMatrixServiceReadMatrixResponse']
_FORCEMATRIXSERVICEDETECTSLIPREQUEST = DESCRIPTOR.message_types_by_name['ForceMatrixServiceDetectSlipRequest']
_FORCEMATRIXSERVICEDETECTSLIPRESPONSE = DESCRIPTOR.message_types_by_name['ForceMatrixServiceDetectSlipResponse']
Matrix = _reflection.GeneratedProtocolMessageType('Matrix', (_message.Message,), {'DESCRIPTOR': _MATRIX, '__module__': 'proto.api.component.v1.forcematrix_pb2'})
_sym_db.RegisterMessage(Matrix)
ForceMatrixServiceReadMatrixRequest = _reflection.GeneratedProtocolMessageType('ForceMatrixServiceReadMatrixRequest', (_message.Message,), {'DESCRIPTOR': _FORCEMATRIXSERVICEREADMATRIXREQUEST, '__module__': 'proto.api.component.v1.forcematrix_pb2'})
_sym_db.RegisterMessage(ForceMatrixServiceReadMatrixRequest)
ForceMatrixServiceReadMatrixResponse = _reflection.GeneratedProtocolMessageType('ForceMatrixServiceReadMatrixResponse', (_message.Message,), {'DESCRIPTOR': _FORCEMATRIXSERVICEREADMATRIXRESPONSE, '__module__': 'proto.api.component.v1.forcematrix_pb2'})
_sym_db.RegisterMessage(ForceMatrixServiceReadMatrixResponse)
ForceMatrixServiceDetectSlipRequest = _reflection.GeneratedProtocolMessageType('ForceMatrixServiceDetectSlipRequest', (_message.Message,), {'DESCRIPTOR': _FORCEMATRIXSERVICEDETECTSLIPREQUEST, '__module__': 'proto.api.component.v1.forcematrix_pb2'})
_sym_db.RegisterMessage(ForceMatrixServiceDetectSlipRequest)
ForceMatrixServiceDetectSlipResponse = _reflection.GeneratedProtocolMessageType('ForceMatrixServiceDetectSlipResponse', (_message.Message,), {'DESCRIPTOR': _FORCEMATRIXSERVICEDETECTSLIPRESPONSE, '__module__': 'proto.api.component.v1.forcematrix_pb2'})
_sym_db.RegisterMessage(ForceMatrixServiceDetectSlipResponse)
_FORCEMATRIXSERVICE = DESCRIPTOR.services_by_name['ForceMatrixService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _FORCEMATRIXSERVICE.methods_by_name['ReadMatrix']._options = None
    _FORCEMATRIXSERVICE.methods_by_name['ReadMatrix']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/api/v1/component/force_matrix/{name}/matrix'
    _FORCEMATRIXSERVICE.methods_by_name['DetectSlip']._options = None
    _FORCEMATRIXSERVICE.methods_by_name['DetectSlip']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/api/v1/component/force_matrix/{name}/slip_detection'
    _MATRIX._serialized_start = 98
    _MATRIX._serialized_end = 166
    _FORCEMATRIXSERVICEREADMATRIXREQUEST._serialized_start = 168
    _FORCEMATRIXSERVICEREADMATRIXREQUEST._serialized_end = 225
    _FORCEMATRIXSERVICEREADMATRIXRESPONSE._serialized_start = 227
    _FORCEMATRIXSERVICEREADMATRIXRESPONSE._serialized_end = 321
    _FORCEMATRIXSERVICEDETECTSLIPREQUEST._serialized_start = 323
    _FORCEMATRIXSERVICEDETECTSLIPREQUEST._serialized_end = 380
    _FORCEMATRIXSERVICEDETECTSLIPRESPONSE._serialized_start = 382
    _FORCEMATRIXSERVICEDETECTSLIPRESPONSE._serialized_end = 457
    _FORCEMATRIXSERVICE._serialized_start = 460
    _FORCEMATRIXSERVICE._serialized_end = 872