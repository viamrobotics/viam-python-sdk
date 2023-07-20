"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n component/gantry/v1/gantry.proto\x12\x18viam.component.gantry.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"8\n\x13GetPositionResponse\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm"\xa8\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cpositions_mm\x18\x02 \x03(\x01R\x0bpositionsMm\x12)\n\x11speeds_mm_per_sec\x18\x03 \x03(\x01R\x0espeedsMmPerSec\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x18\n\x16MoveToPositionResponse"P\n\x0bHomeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"$\n\x0cHomeResponse\x12\x14\n\x05homed\x18\x01 \x01(\x08R\x05homed"V\n\x11GetLengthsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"3\n\x12GetLengthsResponse\x12\x1d\n\nlengths_mm\x18\x01 \x03(\x01R\tlengthsMm"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"g\n\x06Status\x12!\n\x0cpositions_mm\x18\x01 \x03(\x01R\x0bpositionsMm\x12\x1d\n\nlengths_mm\x18\x02 \x03(\x01R\tlengthsMm\x12\x1b\n\tis_moving\x18\x03 \x01(\x08R\x08isMoving"%\n\x0fIsMovingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x10IsMovingResponse\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving2\xda\t\n\rGantryService\x12\xa1\x01\n\x0bGetPosition\x12,.viam.component.gantry.v1.GetPositionRequest\x1a-.viam.component.gantry.v1.GetPositionResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/gantry/{name}/position\x12\xae\x01\n\x0eMoveToPosition\x12/.viam.component.gantry.v1.MoveToPositionRequest\x1a0.viam.component.gantry.v1.MoveToPositionResponse"9\xa0\x92)\x01\x82\xd3\xe4\x93\x02/\x1a-/viam/api/v1/component/gantry/{name}/position\x12\x88\x01\n\x04Home\x12%.viam.component.gantry.v1.HomeRequest\x1a&.viam.component.gantry.v1.HomeResponse"1\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/gantry/{name}/home\x12\x9d\x01\n\nGetLengths\x12+.viam.component.gantry.v1.GetLengthsRequest\x1a,.viam.component.gantry.v1.GetLengthsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/gantry/{name}/lengths\x12\x88\x01\n\x04Stop\x12%.viam.component.gantry.v1.StopRequest\x1a&.viam.component.gantry.v1.StopResponse"1\x82\xd3\xe4\x93\x02+")/viam/api/v1/component/gantry/{name}/stop\x12\x99\x01\n\x08IsMoving\x12).viam.component.gantry.v1.IsMovingRequest\x1a*.viam.component.gantry.v1.IsMovingResponse"6\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/gantry/{name}/is_moving\x12\x89\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/component/gantry/{name}/do_command\x12\x95\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/gantry/{name}/geometriesBC\n\x1ccom.viam.component.gantry.v1Z#go.viam.com/api/component/gantry/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.gantry.v1.gantry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1ccom.viam.component.gantry.v1Z#go.viam.com/api/component/gantry/v1'
    _GANTRYSERVICE.methods_by_name['GetPosition']._options = None
    _GANTRYSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/gantry/{name}/position'
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._options = None
    _GANTRYSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02/\x1a-/viam/api/v1/component/gantry/{name}/position'
    _GANTRYSERVICE.methods_by_name['Home']._options = None
    _GANTRYSERVICE.methods_by_name['Home']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/gantry/{name}/home'
    _GANTRYSERVICE.methods_by_name['GetLengths']._options = None
    _GANTRYSERVICE.methods_by_name['GetLengths']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/gantry/{name}/lengths'
    _GANTRYSERVICE.methods_by_name['Stop']._options = None
    _GANTRYSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/viam/api/v1/component/gantry/{name}/stop'
    _GANTRYSERVICE.methods_by_name['IsMoving']._options = None
    _GANTRYSERVICE.methods_by_name['IsMoving']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/gantry/{name}/is_moving'
    _GANTRYSERVICE.methods_by_name['DoCommand']._options = None
    _GANTRYSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/component/gantry/{name}/do_command'
    _GANTRYSERVICE.methods_by_name['GetGeometries']._options = None
    _GANTRYSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/gantry/{name}/geometries'
    _GETPOSITIONREQUEST._serialized_start = 146
    _GETPOSITIONREQUEST._serialized_end = 233
    _GETPOSITIONRESPONSE._serialized_start = 235
    _GETPOSITIONRESPONSE._serialized_end = 291
    _MOVETOPOSITIONREQUEST._serialized_start = 294
    _MOVETOPOSITIONREQUEST._serialized_end = 462
    _MOVETOPOSITIONRESPONSE._serialized_start = 464
    _MOVETOPOSITIONRESPONSE._serialized_end = 488
    _HOMEREQUEST._serialized_start = 490
    _HOMEREQUEST._serialized_end = 570
    _HOMERESPONSE._serialized_start = 572
    _HOMERESPONSE._serialized_end = 608
    _GETLENGTHSREQUEST._serialized_start = 610
    _GETLENGTHSREQUEST._serialized_end = 696
    _GETLENGTHSRESPONSE._serialized_start = 698
    _GETLENGTHSRESPONSE._serialized_end = 749
    _STOPREQUEST._serialized_start = 751
    _STOPREQUEST._serialized_end = 831
    _STOPRESPONSE._serialized_start = 833
    _STOPRESPONSE._serialized_end = 847
    _STATUS._serialized_start = 849
    _STATUS._serialized_end = 952
    _ISMOVINGREQUEST._serialized_start = 954
    _ISMOVINGREQUEST._serialized_end = 991
    _ISMOVINGRESPONSE._serialized_start = 993
    _ISMOVINGRESPONSE._serialized_end = 1040
    _GANTRYSERVICE._serialized_start = 1043
    _GANTRYSERVICE._serialized_end = 2285