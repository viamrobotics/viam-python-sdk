"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/api/robot/v1/robot.proto\x12\x12proto.api.robot.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\x16\n\x14ResourceNamesRequest"X\n\x15ResourceNamesResponse\x12?\n\tresources\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\tresources"\xa0\x01\n\tOperation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06method\x18\x02 \x01(\tR\x06method\x125\n\targuments\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\targuments\x124\n\x07started\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07started"\x16\n\x14GetOperationsRequest"V\n\x15GetOperationsResponse\x12=\n\noperations\x18\x01 \x03(\x0b2\x1d.proto.api.robot.v1.OperationR\noperations"(\n\x16CancelOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x19\n\x17CancelOperationResponse"*\n\x18BlockForOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1b\n\x19BlockForOperationResponse2\xd6\x04\n\x0cRobotService\x12\x8a\x01\n\rGetOperations\x12(.proto.api.robot.v1.GetOperationsRequest\x1a).proto.api.robot.v1.GetOperationsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list\x12\x89\x01\n\rResourceNames\x12(.proto.api.robot.v1.ResourceNamesRequest\x1a).proto.api.robot.v1.ResourceNamesResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list\x12\x92\x01\n\x0fCancelOperation\x12*.proto.api.robot.v1.CancelOperationRequest\x1a+.proto.api.robot.v1.CancelOperationResponse"&\x82\xd3\xe4\x93\x02 "\x1e/viam/api/v1/operations/cancel\x12\x97\x01\n\x11BlockForOperation\x12,.proto.api.robot.v1.BlockForOperationRequest\x1a-.proto.api.robot.v1.BlockForOperationResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1d/viam/api/v1/operations/blockBE\n\x1fcom.viam.rdk.proto.api.robot.v1Z"go.viam.com/rdk/proto/api/robot/v1b\x06proto3')
_RESOURCENAMESREQUEST = DESCRIPTOR.message_types_by_name['ResourceNamesRequest']
_RESOURCENAMESRESPONSE = DESCRIPTOR.message_types_by_name['ResourceNamesResponse']
_OPERATION = DESCRIPTOR.message_types_by_name['Operation']
_GETOPERATIONSREQUEST = DESCRIPTOR.message_types_by_name['GetOperationsRequest']
_GETOPERATIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetOperationsResponse']
_CANCELOPERATIONREQUEST = DESCRIPTOR.message_types_by_name['CancelOperationRequest']
_CANCELOPERATIONRESPONSE = DESCRIPTOR.message_types_by_name['CancelOperationResponse']
_BLOCKFOROPERATIONREQUEST = DESCRIPTOR.message_types_by_name['BlockForOperationRequest']
_BLOCKFOROPERATIONRESPONSE = DESCRIPTOR.message_types_by_name['BlockForOperationResponse']
ResourceNamesRequest = _reflection.GeneratedProtocolMessageType('ResourceNamesRequest', (_message.Message,), {'DESCRIPTOR': _RESOURCENAMESREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ResourceNamesRequest)
ResourceNamesResponse = _reflection.GeneratedProtocolMessageType('ResourceNamesResponse', (_message.Message,), {'DESCRIPTOR': _RESOURCENAMESRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ResourceNamesResponse)
Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {'DESCRIPTOR': _OPERATION, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(Operation)
GetOperationsRequest = _reflection.GeneratedProtocolMessageType('GetOperationsRequest', (_message.Message,), {'DESCRIPTOR': _GETOPERATIONSREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(GetOperationsRequest)
GetOperationsResponse = _reflection.GeneratedProtocolMessageType('GetOperationsResponse', (_message.Message,), {'DESCRIPTOR': _GETOPERATIONSRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(GetOperationsResponse)
CancelOperationRequest = _reflection.GeneratedProtocolMessageType('CancelOperationRequest', (_message.Message,), {'DESCRIPTOR': _CANCELOPERATIONREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(CancelOperationRequest)
CancelOperationResponse = _reflection.GeneratedProtocolMessageType('CancelOperationResponse', (_message.Message,), {'DESCRIPTOR': _CANCELOPERATIONRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(CancelOperationResponse)
BlockForOperationRequest = _reflection.GeneratedProtocolMessageType('BlockForOperationRequest', (_message.Message,), {'DESCRIPTOR': _BLOCKFOROPERATIONREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(BlockForOperationRequest)
BlockForOperationResponse = _reflection.GeneratedProtocolMessageType('BlockForOperationResponse', (_message.Message,), {'DESCRIPTOR': _BLOCKFOROPERATIONRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(BlockForOperationResponse)
_ROBOTSERVICE = DESCRIPTOR.services_by_name['RobotService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.viam.rdk.proto.api.robot.v1Z"go.viam.com/rdk/proto/api/robot/v1'
    _ROBOTSERVICE.methods_by_name['GetOperations']._options = None
    _ROBOTSERVICE.methods_by_name['GetOperations']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list'
    _ROBOTSERVICE.methods_by_name['ResourceNames']._options = None
    _ROBOTSERVICE.methods_by_name['ResourceNames']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list'
    _ROBOTSERVICE.methods_by_name['CancelOperation']._options = None
    _ROBOTSERVICE.methods_by_name['CancelOperation']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1e/viam/api/v1/operations/cancel'
    _ROBOTSERVICE.methods_by_name['BlockForOperation']._options = None
    _ROBOTSERVICE.methods_by_name['BlockForOperation']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1d/viam/api/v1/operations/block'
    _RESOURCENAMESREQUEST._serialized_start = 181
    _RESOURCENAMESREQUEST._serialized_end = 203
    _RESOURCENAMESRESPONSE._serialized_start = 205
    _RESOURCENAMESRESPONSE._serialized_end = 293
    _OPERATION._serialized_start = 296
    _OPERATION._serialized_end = 456
    _GETOPERATIONSREQUEST._serialized_start = 458
    _GETOPERATIONSREQUEST._serialized_end = 480
    _GETOPERATIONSRESPONSE._serialized_start = 482
    _GETOPERATIONSRESPONSE._serialized_end = 568
    _CANCELOPERATIONREQUEST._serialized_start = 570
    _CANCELOPERATIONREQUEST._serialized_end = 610
    _CANCELOPERATIONRESPONSE._serialized_start = 612
    _CANCELOPERATIONRESPONSE._serialized_end = 637
    _BLOCKFOROPERATIONREQUEST._serialized_start = 639
    _BLOCKFOROPERATIONREQUEST._serialized_end = 681
    _BLOCKFOROPERATIONRESPONSE._serialized_start = 683
    _BLOCKFOROPERATIONRESPONSE._serialized_end = 710
    _ROBOTSERVICE._serialized_start = 713
    _ROBOTSERVICE._serialized_end = 1311