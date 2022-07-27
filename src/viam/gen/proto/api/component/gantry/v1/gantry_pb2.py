"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*proto/api/component/gantry/v1/gantry.proto\x12\x1dproto.api.component.gantry.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"8\n\x13GetPositionResponse\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm"\xd4\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cpositions_mm\x18\x02 \x03(\x01R\x0bpositionsMm\x12E\n\x0bworld_state\x18\x03 \x01(\x0b2\x1f.proto.api.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_state"\x18\n\x16MoveToPositionResponse"V\n\x11GetLengthsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"3\n\x12GetLengthsResponse\x12\x1d\n\nlengths_mm\x18\x01 \x03(\x01R\tlengthsMm"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"g\n\x06Status\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm\x12\x1d\n\nlengths_mm\x18\x02 \x03(\x01R\tlengthsMm\x12\x1b\n\tis_moving\x18\x03 \x01(\x08R\x08isMoving2\xb3\x05\n\rGantryService\x12\xab\x01\n\x0bGetPosition\x121.proto.api.component.gantry.v1.GetPositionRequest\x1a2.proto.api.component.gantry.v1.GetPositionResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/gantry/{name}/position\x12\xb4\x01\n\x0eMoveToPosition\x124.proto.api.component.gantry.v1.MoveToPositionRequest\x1a5.proto.api.component.gantry.v1.MoveToPositionResponse"5\x82\xd3\xe4\x93\x02/\x1a-/viam/api/v1/component/gantry/{name}/position\x12\xa7\x01\n\nGetLengths\x120.proto.api.component.gantry.v1.GetLengthsRequest\x1a1.proto.api.component.gantry.v1.GetLengthsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/gantry/{name}/lengths\x12\x92\x01\n\x04Stop\x12*.proto.api.component.gantry.v1.StopRequest\x1a+.proto.api.component.gantry.v1.StopResponse"1\x82\xd3\xe4\x93\x02+")/viam/api/v1/component/gantry/{name}/stopB[\n*com.viam.rdk.proto.api.component.gantry.v1Z-go.viam.com/rdk/proto/api/component/gantry/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.gantry.v1.gantry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n*com.viam.rdk.proto.api.component.gantry.v1Z-go.viam.com/rdk/proto/api/component/gantry/v1'
    _GANTRYSERVICE.methods_by_name['GetPosition']._options = None
    _GANTRYSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/gantry/{name}/position'
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._options = None
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x1a-/viam/api/v1/component/gantry/{name}/position'
    _GANTRYSERVICE.methods_by_name['GetLengths']._options = None
    _GANTRYSERVICE.methods_by_name['GetLengths']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/gantry/{name}/lengths'
    _GANTRYSERVICE.methods_by_name['Stop']._options = None
    _GANTRYSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/viam/api/v1/component/gantry/{name}/stop'
    _GETPOSITIONREQUEST._serialized_start = 171
    _GETPOSITIONREQUEST._serialized_end = 258
    _GETPOSITIONRESPONSE._serialized_start = 260
    _GETPOSITIONRESPONSE._serialized_end = 316
    _MOVETOPOSITIONREQUEST._serialized_start = 319
    _MOVETOPOSITIONREQUEST._serialized_end = 531
    _MOVETOPOSITIONRESPONSE._serialized_start = 533
    _MOVETOPOSITIONRESPONSE._serialized_end = 557
    _GETLENGTHSREQUEST._serialized_start = 559
    _GETLENGTHSREQUEST._serialized_end = 645
    _GETLENGTHSRESPONSE._serialized_start = 647
    _GETLENGTHSRESPONSE._serialized_end = 698
    _STOPREQUEST._serialized_start = 700
    _STOPREQUEST._serialized_end = 780
    _STOPRESPONSE._serialized_start = 782
    _STOPRESPONSE._serialized_end = 796
    _STATUS._serialized_start = 798
    _STATUS._serialized_end = 901
    _GANTRYSERVICE._serialized_start = 904
    _GANTRYSERVICE._serialized_end = 1595