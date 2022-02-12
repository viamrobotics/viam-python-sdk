"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$proto/api/component/v1/gripper.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto"/\n\x19GripperServiceOpenRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x1c\n\x1aGripperServiceOpenResponse"/\n\x19GripperServiceGrabRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"6\n\x1aGripperServiceGrabResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success2\xce\x02\n\x0eGripperService\x12\x9c\x01\n\x04Open\x121.proto.api.component.v1.GripperServiceOpenRequest\x1a2.proto.api.component.v1.GripperServiceOpenResponse"-\x82\xd3\xe4\x93\x02\'\x1a%/api/v1/component/gripper/{name}/open\x12\x9c\x01\n\x04Grab\x121.proto.api.component.v1.GripperServiceGrabRequest\x1a2.proto.api.component.v1.GripperServiceGrabResponse"-\x82\xd3\xe4\x93\x02\'\x1a%/api/v1/component/gripper/{name}/grabBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_GRIPPERSERVICEOPENREQUEST = DESCRIPTOR.message_types_by_name['GripperServiceOpenRequest']
_GRIPPERSERVICEOPENRESPONSE = DESCRIPTOR.message_types_by_name['GripperServiceOpenResponse']
_GRIPPERSERVICEGRABREQUEST = DESCRIPTOR.message_types_by_name['GripperServiceGrabRequest']
_GRIPPERSERVICEGRABRESPONSE = DESCRIPTOR.message_types_by_name['GripperServiceGrabResponse']
GripperServiceOpenRequest = _reflection.GeneratedProtocolMessageType('GripperServiceOpenRequest', (_message.Message,), {'DESCRIPTOR': _GRIPPERSERVICEOPENREQUEST, '__module__': 'proto.api.component.v1.gripper_pb2'})
_sym_db.RegisterMessage(GripperServiceOpenRequest)
GripperServiceOpenResponse = _reflection.GeneratedProtocolMessageType('GripperServiceOpenResponse', (_message.Message,), {'DESCRIPTOR': _GRIPPERSERVICEOPENRESPONSE, '__module__': 'proto.api.component.v1.gripper_pb2'})
_sym_db.RegisterMessage(GripperServiceOpenResponse)
GripperServiceGrabRequest = _reflection.GeneratedProtocolMessageType('GripperServiceGrabRequest', (_message.Message,), {'DESCRIPTOR': _GRIPPERSERVICEGRABREQUEST, '__module__': 'proto.api.component.v1.gripper_pb2'})
_sym_db.RegisterMessage(GripperServiceGrabRequest)
GripperServiceGrabResponse = _reflection.GeneratedProtocolMessageType('GripperServiceGrabResponse', (_message.Message,), {'DESCRIPTOR': _GRIPPERSERVICEGRABRESPONSE, '__module__': 'proto.api.component.v1.gripper_pb2'})
_sym_db.RegisterMessage(GripperServiceGrabResponse)
_GRIPPERSERVICE = DESCRIPTOR.services_by_name['GripperService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _GRIPPERSERVICE.methods_by_name['Open']._options = None
    _GRIPPERSERVICE.methods_by_name['Open']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x1a%/api/v1/component/gripper/{name}/open"
    _GRIPPERSERVICE.methods_by_name['Grab']._options = None
    _GRIPPERSERVICE.methods_by_name['Grab']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x1a%/api/v1/component/gripper/{name}/grab"
    _GRIPPERSERVICEOPENREQUEST._serialized_start = 94
    _GRIPPERSERVICEOPENREQUEST._serialized_end = 141
    _GRIPPERSERVICEOPENRESPONSE._serialized_start = 143
    _GRIPPERSERVICEOPENRESPONSE._serialized_end = 171
    _GRIPPERSERVICEGRABREQUEST._serialized_start = 173
    _GRIPPERSERVICEGRABREQUEST._serialized_end = 220
    _GRIPPERSERVICEGRABRESPONSE._serialized_start = 222
    _GRIPPERSERVICEGRABRESPONSE._serialized_end = 276
    _GRIPPERSERVICE._serialized_start = 279
    _GRIPPERSERVICE._serialized_end = 613