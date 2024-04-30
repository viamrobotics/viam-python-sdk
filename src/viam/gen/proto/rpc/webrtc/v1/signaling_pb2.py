"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#proto/rpc/webrtc/v1/signaling.proto\x12\x13proto.rpc.webrtc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xdf\x01\n\x0cICECandidate\x12\x1c\n\tcandidate\x18\x01 \x01(\tR\tcandidate\x12\x1c\n\x07sdp_mid\x18\x02 \x01(\tH\x00R\x06sdpMid\x88\x01\x01\x12+\n\x0fsdpm_line_index\x18\x03 \x01(\rH\x01R\rsdpmLineIndex\x88\x01\x01\x120\n\x11username_fragment\x18\x04 \x01(\tH\x02R\x10usernameFragment\x88\x01\x01B\n\n\x08_sdp_midB\x12\n\x10_sdpm_line_indexB\x14\n\x12_username_fragment"H\n\x0bCallRequest\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp\x12\'\n\x0fdisable_trickle\x18\x02 \x01(\x08R\x0edisableTrickle")\n\x15CallResponseInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp"Z\n\x17CallResponseUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\xb5\x01\n\x0cCallResponse\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12@\n\x04init\x18\x02 \x01(\x0b2*.proto.rpc.webrtc.v1.CallResponseInitStageH\x00R\x04init\x12F\n\x06update\x18\x03 \x01(\x0b2,.proto.rpc.webrtc.v1.CallResponseUpdateStageH\x00R\x06updateB\x07\n\x05stage"\xb6\x01\n\x11CallUpdateRequest\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12A\n\tcandidate\x18\x02 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateH\x00R\tcandidate\x12\x14\n\x04done\x18\x03 \x01(\x08H\x00R\x04done\x12*\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusH\x00R\x05errorB\x08\n\x06update"\x14\n\x12CallUpdateResponse"[\n\tICEServer\x12\x12\n\x04urls\x18\x01 \x03(\tR\x04urls\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username\x12\x1e\n\ncredential\x18\x03 \x01(\tR\ncredential"\x8d\x01\n\x0cWebRTCConfig\x12T\n\x16additional_ice_servers\x18\x01 \x03(\x0b2\x1e.proto.rpc.webrtc.v1.ICEServerR\x14additionalIceServers\x12\'\n\x0fdisable_trickle\x18\x02 \x01(\x08R\x0edisableTrickle"\xc0\x01\n\x16AnswerRequestInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp\x12J\n\x0foptional_config\x18\x02 \x01(\x0b2!.proto.rpc.webrtc.v1.WebRTCConfigR\x0eoptionalConfig\x12;\n\x08deadline\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x08deadline\x88\x01\x01B\x0b\n\t_deadline"[\n\x18AnswerRequestUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\x18\n\x16AnswerRequestDoneStage"E\n\x17AnswerRequestErrorStage\x12*\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusR\x06status"\xc1\x02\n\rAnswerRequest\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12A\n\x04init\x18\x02 \x01(\x0b2+.proto.rpc.webrtc.v1.AnswerRequestInitStageH\x00R\x04init\x12G\n\x06update\x18\x03 \x01(\x0b2-.proto.rpc.webrtc.v1.AnswerRequestUpdateStageH\x00R\x06update\x12A\n\x04done\x18\x04 \x01(\x0b2+.proto.rpc.webrtc.v1.AnswerRequestDoneStageH\x00R\x04done\x12D\n\x05error\x18\x05 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerRequestErrorStageH\x00R\x05errorB\x07\n\x05stage"+\n\x17AnswerResponseInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp"\\\n\x19AnswerResponseUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\x19\n\x17AnswerResponseDoneStage"F\n\x18AnswerResponseErrorStage\x12*\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusR\x06status"\xc6\x02\n\x0eAnswerResponse\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12B\n\x04init\x18\x02 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerResponseInitStageH\x00R\x04init\x12H\n\x06update\x18\x03 \x01(\x0b2..proto.rpc.webrtc.v1.AnswerResponseUpdateStageH\x00R\x06update\x12B\n\x04done\x18\x04 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerResponseDoneStageH\x00R\x04done\x12E\n\x05error\x18\x05 \x01(\x0b2-.proto.rpc.webrtc.v1.AnswerResponseErrorStageH\x00R\x05errorB\x07\n\x05stage"\x1d\n\x1bOptionalWebRTCConfigRequest"Y\n\x1cOptionalWebRTCConfigResponse\x129\n\x06config\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.WebRTCConfigR\x06config2\x86\x04\n\x10SignalingService\x12j\n\x04Call\x12 .proto.rpc.webrtc.v1.CallRequest\x1a!.proto.rpc.webrtc.v1.CallResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x13/rpc/webrtc/v1/call0\x01\x12\x81\x01\n\nCallUpdate\x12&.proto.rpc.webrtc.v1.CallUpdateRequest\x1a\'.proto.rpc.webrtc.v1.CallUpdateResponse""\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/rpc/webrtc/v1/call_update\x12U\n\x06Answer\x12#.proto.rpc.webrtc.v1.AnswerResponse\x1a".proto.rpc.webrtc.v1.AnswerRequest(\x010\x01\x12\xaa\x01\n\x14OptionalWebRTCConfig\x120.proto.rpc.webrtc.v1.OptionalWebRTCConfigRequest\x1a1.proto.rpc.webrtc.v1.OptionalWebRTCConfigResponse"-\x82\xd3\xe4\x93\x02\'\x12%/rpc/webrtc/v1/optional_webrtc_configB\'Z%go.viam.com/utils/proto/rpc/webrtc/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.rpc.webrtc.v1.signaling_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%go.viam.com/utils/proto/rpc/webrtc/v1'
    _SIGNALINGSERVICE.methods_by_name['Call']._options = None
    _SIGNALINGSERVICE.methods_by_name['Call']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x13/rpc/webrtc/v1/call'
    _SIGNALINGSERVICE.methods_by_name['CallUpdate']._options = None
    _SIGNALINGSERVICE.methods_by_name['CallUpdate']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/rpc/webrtc/v1/call_update'
    _SIGNALINGSERVICE.methods_by_name['OptionalWebRTCConfig']._options = None
    _SIGNALINGSERVICE.methods_by_name['OptionalWebRTCConfig']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/rpc/webrtc/v1/optional_webrtc_config"
    _ICECANDIDATE._serialized_start = 149
    _ICECANDIDATE._serialized_end = 372
    _CALLREQUEST._serialized_start = 374
    _CALLREQUEST._serialized_end = 446
    _CALLRESPONSEINITSTAGE._serialized_start = 448
    _CALLRESPONSEINITSTAGE._serialized_end = 489
    _CALLRESPONSEUPDATESTAGE._serialized_start = 491
    _CALLRESPONSEUPDATESTAGE._serialized_end = 581
    _CALLRESPONSE._serialized_start = 584
    _CALLRESPONSE._serialized_end = 765
    _CALLUPDATEREQUEST._serialized_start = 768
    _CALLUPDATEREQUEST._serialized_end = 950
    _CALLUPDATERESPONSE._serialized_start = 952
    _CALLUPDATERESPONSE._serialized_end = 972
    _ICESERVER._serialized_start = 974
    _ICESERVER._serialized_end = 1065
    _WEBRTCCONFIG._serialized_start = 1068
    _WEBRTCCONFIG._serialized_end = 1209
    _ANSWERREQUESTINITSTAGE._serialized_start = 1212
    _ANSWERREQUESTINITSTAGE._serialized_end = 1404
    _ANSWERREQUESTUPDATESTAGE._serialized_start = 1406
    _ANSWERREQUESTUPDATESTAGE._serialized_end = 1497
    _ANSWERREQUESTDONESTAGE._serialized_start = 1499
    _ANSWERREQUESTDONESTAGE._serialized_end = 1523
    _ANSWERREQUESTERRORSTAGE._serialized_start = 1525
    _ANSWERREQUESTERRORSTAGE._serialized_end = 1594
    _ANSWERREQUEST._serialized_start = 1597
    _ANSWERREQUEST._serialized_end = 1918
    _ANSWERRESPONSEINITSTAGE._serialized_start = 1920
    _ANSWERRESPONSEINITSTAGE._serialized_end = 1963
    _ANSWERRESPONSEUPDATESTAGE._serialized_start = 1965
    _ANSWERRESPONSEUPDATESTAGE._serialized_end = 2057
    _ANSWERRESPONSEDONESTAGE._serialized_start = 2059
    _ANSWERRESPONSEDONESTAGE._serialized_end = 2084
    _ANSWERRESPONSEERRORSTAGE._serialized_start = 2086
    _ANSWERRESPONSEERRORSTAGE._serialized_end = 2156
    _ANSWERRESPONSE._serialized_start = 2159
    _ANSWERRESPONSE._serialized_end = 2485
    _OPTIONALWEBRTCCONFIGREQUEST._serialized_start = 2487
    _OPTIONALWEBRTCCONFIGREQUEST._serialized_end = 2516
    _OPTIONALWEBRTCCONFIGRESPONSE._serialized_start = 2518
    _OPTIONALWEBRTCCONFIGRESPONSE._serialized_end = 2607
    _SIGNALINGSERVICE._serialized_start = 2610
    _SIGNALINGSERVICE._serialized_end = 3128