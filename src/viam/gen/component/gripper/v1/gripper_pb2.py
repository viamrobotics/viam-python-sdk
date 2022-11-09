"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"component/gripper/v1/gripper.proto\x12\x19viam.component.gripper.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"P\n\x0bOpenRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cOpenResponse"P\n\x0bGrabRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"W\n\x0cGrabResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse2\xba\x03\n\x0eGripperService\x12\x8b\x01\n\x04Open\x12&.viam.component.gripper.v1.OpenRequest\x1a\'.viam.component.gripper.v1.OpenResponse"2\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/open\x12\x8b\x01\n\x04Grab\x12&.viam.component.gripper.v1.GrabRequest\x1a\'.viam.component.gripper.v1.GrabResponse"2\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/grab\x12\x8b\x01\n\x04Stop\x12&.viam.component.gripper.v1.StopRequest\x1a\'.viam.component.gripper.v1.StopResponse"2\x82\xd3\xe4\x93\x02,"*/viam/api/v1/component/gripper/{name}/stopBE\n\x1dcom.viam.component.gripper.v1Z$go.viam.com/api/component/gripper/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.gripper.v1.gripper_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1dcom.viam.component.gripper.v1Z$go.viam.com/api/component/gripper/v1'
    _GRIPPERSERVICE.methods_by_name['Open']._options = None
    _GRIPPERSERVICE.methods_by_name['Open']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/open'
    _GRIPPERSERVICE.methods_by_name['Grab']._options = None
    _GRIPPERSERVICE.methods_by_name['Grab']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/grab'
    _GRIPPERSERVICE.methods_by_name['Stop']._options = None
    _GRIPPERSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02,"*/viam/api/v1/component/gripper/{name}/stop'
    _OPENREQUEST._serialized_start = 125
    _OPENREQUEST._serialized_end = 205
    _OPENRESPONSE._serialized_start = 207
    _OPENRESPONSE._serialized_end = 221
    _GRABREQUEST._serialized_start = 223
    _GRABREQUEST._serialized_end = 303
    _GRABRESPONSE._serialized_start = 305
    _GRABRESPONSE._serialized_end = 392
    _STOPREQUEST._serialized_start = 394
    _STOPREQUEST._serialized_end = 474
    _STOPRESPONSE._serialized_start = 476
    _STOPRESPONSE._serialized_end = 490
    _GRIPPERSERVICE._serialized_start = 493
    _GRIPPERSERVICE._serialized_end = 935