"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'service/video/v1/video.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cservice/video/v1/video.proto\x12\x15viam.service.video.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc3\x02\n\x0fGetVideoRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\x0fstart_timestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0estartTimestamp\x12?\n\rend_timestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0cendTimestamp\x12\x1f\n\x0bvideo_codec\x18\x04 \x01(\tR\nvideoCodec\x12\'\n\x0fvideo_container\x18\x05 \x01(\tR\x0evideoContainer\x12\x1d\n\nrequest_id\x18\x06 \x01(\tR\trequestId\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"y\n\x10GetVideoResponse\x12\x1d\n\nvideo_data\x18\x01 \x01(\x0cR\tvideoData\x12\'\n\x0fvideo_container\x18\x02 \x01(\tR\x0evideoContainer\x12\x1d\n\nrequest_id\x18\x03 \x01(\tR\trequestId2\xb3\x02\n\x0cVideoService\x12\x99\x01\n\x08GetVideo\x12&.viam.service.video.v1.GetVideoRequest\x1a\'.viam.service.video.v1.GetVideoResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/video/{name}/get_video_stream0\x01\x12\x86\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"4\x82\xd3\xe4\x93\x02.",/viam/api/v1/service/video/{name}/do_commandB=\n\x19com.viam.service.video.v1Z go.viam.com/api/service/video/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.video.v1.video_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.viam.service.video.v1Z go.viam.com/api/service/video/v1'
    _globals['_VIDEOSERVICE'].methods_by_name['GetVideo']._loaded_options = None
    _globals['_VIDEOSERVICE'].methods_by_name['GetVideo']._serialized_options = b'\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/video/{name}/get_video_stream'
    _globals['_VIDEOSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_VIDEOSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02.",/viam/api/v1/service/video/{name}/do_command'
    _globals['_GETVIDEOREQUEST']._serialized_start = 173
    _globals['_GETVIDEOREQUEST']._serialized_end = 496
    _globals['_GETVIDEORESPONSE']._serialized_start = 498
    _globals['_GETVIDEORESPONSE']._serialized_end = 619
    _globals['_VIDEOSERVICE']._serialized_start = 622
    _globals['_VIDEOSERVICE']._serialized_end = 929