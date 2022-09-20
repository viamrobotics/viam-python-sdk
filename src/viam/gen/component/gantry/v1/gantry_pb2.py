"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n component/gantry/v1/gantry.proto\x12\x18viam.component.gantry.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"8\n\x13GetPositionResponse\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm"\xcf\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cpositions_mm\x18\x02 \x03(\x01R\x0bpositionsMm\x12@\n\x0bworld_state\x18\x03 \x01(\x0b2\x1a.viam.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_state"\x18\n\x16MoveToPositionResponse"V\n\x11GetLengthsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"3\n\x12GetLengthsResponse\x12\x1d\n\nlengths_mm\x18\x01 \x03(\x01R\tlengthsMm"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"g\n\x06Status\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm\x12\x1d\n\nlengths_mm\x18\x02 \x03(\x01R\tlengthsMm\x12\x1b\n\tis_moving\x18\x03 \x01(\x08R\x08isMoving2\x8b\x05\n\rGantryService\x12\xa1\x01\n\x0bGetPosition\x12,.viam.component.gantry.v1.GetPositionRequest\x1a-.viam.component.gantry.v1.GetPositionResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/gantry/{name}/position\x12\xaa\x01\n\x0eMoveToPosition\x12/.viam.component.gantry.v1.MoveToPositionRequest\x1a0.viam.component.gantry.v1.MoveToPositionResponse"5\x82\xd3\xe4\x93\x02/\x1a-/viam/api/v1/component/gantry/{name}/position\x12\x9d\x01\n\nGetLengths\x12+.viam.component.gantry.v1.GetLengthsRequest\x1a,.viam.component.gantry.v1.GetLengthsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/gantry/{name}/lengths\x12\x88\x01\n\x04Stop\x12%.viam.component.gantry.v1.StopRequest\x1a&.viam.component.gantry.v1.StopResponse"1\x82\xd3\xe4\x93\x02+")/viam/api/v1/component/gantry/{name}/stopBC\n\x1ccom.viam.component.gantry.v1Z#go.viam.com/api/component/gantry/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.gantry.v1.gantry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1ccom.viam.component.gantry.v1Z#go.viam.com/api/component/gantry/v1'
    _GANTRYSERVICE.methods_by_name['GetPosition']._options = None
    _GANTRYSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/gantry/{name}/position'
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._options = None
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x1a-/viam/api/v1/component/gantry/{name}/position'
    _GANTRYSERVICE.methods_by_name['GetLengths']._options = None
    _GANTRYSERVICE.methods_by_name['GetLengths']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/gantry/{name}/lengths'
    _GANTRYSERVICE.methods_by_name['Stop']._options = None
    _GANTRYSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/viam/api/v1/component/gantry/{name}/stop'
    _GETPOSITIONREQUEST._serialized_start = 146
    _GETPOSITIONREQUEST._serialized_end = 233
    _GETPOSITIONRESPONSE._serialized_start = 235
    _GETPOSITIONRESPONSE._serialized_end = 291
    _MOVETOPOSITIONREQUEST._serialized_start = 294
    _MOVETOPOSITIONREQUEST._serialized_end = 501
    _MOVETOPOSITIONRESPONSE._serialized_start = 503
    _MOVETOPOSITIONRESPONSE._serialized_end = 527
    _GETLENGTHSREQUEST._serialized_start = 529
    _GETLENGTHSREQUEST._serialized_end = 615
    _GETLENGTHSRESPONSE._serialized_start = 617
    _GETLENGTHSRESPONSE._serialized_end = 668
    _STOPREQUEST._serialized_start = 670
    _STOPREQUEST._serialized_end = 750
    _STOPRESPONSE._serialized_start = 752
    _STOPRESPONSE._serialized_end = 766
    _STATUS._serialized_start = 768
    _STATUS._serialized_end = 871
    _GANTRYSERVICE._serialized_start = 874
    _GANTRYSERVICE._serialized_end = 1525