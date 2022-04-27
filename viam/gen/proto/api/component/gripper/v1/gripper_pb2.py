"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,proto/api/component/gripper/v1/gripper.proto\x12\x1eproto.api.component.gripper.v1\x1a\x1cgoogle/api/annotations.proto"!\n\x0bOpenRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x0e\n\x0cOpenResponse"!\n\x0bGrabRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"(\n\x0cGrabResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success2\xc0\x02\n\x0eGripperService\x12\x95\x01\n\x04Open\x12+.proto.api.component.gripper.v1.OpenRequest\x1a,.proto.api.component.gripper.v1.OpenResponse"2\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/open\x12\x95\x01\n\x04Grab\x12+.proto.api.component.gripper.v1.GrabRequest\x1a,.proto.api.component.gripper.v1.GrabResponse"2\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/grabB]\n+com.viam.rdk.proto.api.component.gripper.v1Z.go.viam.com/rdk/proto/api/component/gripper/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.gripper.v1.gripper_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n+com.viam.rdk.proto.api.component.gripper.v1Z.go.viam.com/rdk/proto/api/component/gripper/v1'
    _GRIPPERSERVICE.methods_by_name['Open']._options = None
    _GRIPPERSERVICE.methods_by_name['Open']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/open'
    _GRIPPERSERVICE.methods_by_name['Grab']._options = None
    _GRIPPERSERVICE.methods_by_name['Grab']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/gripper/{name}/grab'
    _OPENREQUEST._serialized_start = 110
    _OPENREQUEST._serialized_end = 143
    _OPENRESPONSE._serialized_start = 145
    _OPENRESPONSE._serialized_end = 159
    _GRABREQUEST._serialized_start = 161
    _GRABREQUEST._serialized_end = 194
    _GRABRESPONSE._serialized_start = 196
    _GRABRESPONSE._serialized_end = 236
    _GRIPPERSERVICE._serialized_start = 239
    _GRIPPERSERVICE._serialized_end = 559