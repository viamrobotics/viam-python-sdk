"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 5, '', 'proto/rpc/webrtc/v1/signaling.proto')
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#proto/rpc/webrtc/v1/signaling.proto\x12\x13proto.rpc.webrtc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xdf\x01\n\x0cICECandidate\x12\x1c\n\tcandidate\x18\x01 \x01(\tR\tcandidate\x12\x1c\n\x07sdp_mid\x18\x02 \x01(\tH\x00R\x06sdpMid\x88\x01\x01\x12+\n\x0fsdpm_line_index\x18\x03 \x01(\rH\x01R\rsdpmLineIndex\x88\x01\x01\x120\n\x11username_fragment\x18\x04 \x01(\tH\x02R\x10usernameFragment\x88\x01\x01B\n\n\x08_sdp_midB\x12\n\x10_sdpm_line_indexB\x14\n\x12_username_fragment"H\n\x0bCallRequest\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp\x12\'\n\x0fdisable_trickle\x18\x02 \x01(\x08R\x0edisableTrickle")\n\x15CallResponseInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp"Z\n\x17CallResponseUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\xb5\x01\n\x0cCallResponse\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12@\n\x04init\x18\x02 \x01(\x0b2*.proto.rpc.webrtc.v1.CallResponseInitStageH\x00R\x04init\x12F\n\x06update\x18\x03 \x01(\x0b2,.proto.rpc.webrtc.v1.CallResponseUpdateStageH\x00R\x06updateB\x07\n\x05stage"\xb6\x01\n\x11CallUpdateRequest\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12A\n\tcandidate\x18\x02 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateH\x00R\tcandidate\x12\x14\n\x04done\x18\x03 \x01(\x08H\x00R\x04done\x12*\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusH\x00R\x05errorB\x08\n\x06update"\x14\n\x12CallUpdateResponse"[\n\tICEServer\x12\x12\n\x04urls\x18\x01 \x03(\tR\x04urls\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username\x12\x1e\n\ncredential\x18\x03 \x01(\tR\ncredential"\x8d\x01\n\x0cWebRTCConfig\x12T\n\x16additional_ice_servers\x18\x01 \x03(\x0b2\x1e.proto.rpc.webrtc.v1.ICEServerR\x14additionalIceServers\x12\'\n\x0fdisable_trickle\x18\x02 \x01(\x08R\x0edisableTrickle"\xac\x03\n\x16AnswerRequestInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp\x12J\n\x0foptional_config\x18\x02 \x01(\x0b2!.proto.rpc.webrtc.v1.WebRTCConfigR\x0eoptionalConfig\x12;\n\x08deadline\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x08deadline\x88\x01\x01\x12,\n\x12caller_auth_entity\x18\x04 \x01(\tR\x10callerAuthEntity\x12u\n\x14caller_auth_metadata\x18\x05 \x03(\x0b2C.proto.rpc.webrtc.v1.AnswerRequestInitStage.CallerAuthMetadataEntryR\x12callerAuthMetadata\x1aE\n\x17CallerAuthMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01B\x0b\n\t_deadline"[\n\x18AnswerRequestUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\x18\n\x16AnswerRequestDoneStage"E\n\x17AnswerRequestErrorStage\x12*\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusR\x06status"\x1d\n\x1bAnswerRequestHeartbeatStage"\x93\x03\n\rAnswerRequest\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12A\n\x04init\x18\x02 \x01(\x0b2+.proto.rpc.webrtc.v1.AnswerRequestInitStageH\x00R\x04init\x12G\n\x06update\x18\x03 \x01(\x0b2-.proto.rpc.webrtc.v1.AnswerRequestUpdateStageH\x00R\x06update\x12A\n\x04done\x18\x04 \x01(\x0b2+.proto.rpc.webrtc.v1.AnswerRequestDoneStageH\x00R\x04done\x12D\n\x05error\x18\x05 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerRequestErrorStageH\x00R\x05error\x12P\n\theartbeat\x18\x06 \x01(\x0b20.proto.rpc.webrtc.v1.AnswerRequestHeartbeatStageH\x00R\theartbeatB\x07\n\x05stage"+\n\x17AnswerResponseInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp"\\\n\x19AnswerResponseUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\x19\n\x17AnswerResponseDoneStage"F\n\x18AnswerResponseErrorStage\x12*\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusR\x06status"\xc6\x02\n\x0eAnswerResponse\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12B\n\x04init\x18\x02 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerResponseInitStageH\x00R\x04init\x12H\n\x06update\x18\x03 \x01(\x0b2..proto.rpc.webrtc.v1.AnswerResponseUpdateStageH\x00R\x06update\x12B\n\x04done\x18\x04 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerResponseDoneStageH\x00R\x04done\x12E\n\x05error\x18\x05 \x01(\x0b2-.proto.rpc.webrtc.v1.AnswerResponseErrorStageH\x00R\x05errorB\x07\n\x05stage"\x1d\n\x1bOptionalWebRTCConfigRequest"Y\n\x1cOptionalWebRTCConfigResponse\x129\n\x06config\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.WebRTCConfigR\x06config"u\n\x13ConnectionCandidate\x129\n\x04type\x18\x01 \x01(\x0e2%.proto.rpc.webrtc.v1.ICECandidateTypeR\x04type\x12#\n\rrelay_address\x18\x02 \x01(\tR\x0crelayAddress"\x81\x03\n\x1fReportConnectionMetadataRequest\x12>\n\x05local\x18\x01 \x01(\x0b2(.proto.rpc.webrtc.v1.ConnectionCandidateR\x05local\x12@\n\x06remote\x18\x02 \x01(\x0b2(.proto.rpc.webrtc.v1.ConnectionCandidateR\x06remote\x12C\n\rreached_stage\x18\x03 \x01(\x0e2\x1e.proto.rpc.webrtc.v1.DialStageR\x0creachedStage\x12\x1f\n\x0bduration_ms\x18\x04 \x01(\rR\ndurationMs\x12S\n\x0esignaling_path\x18\x05 \x01(\x0e2,.proto.rpc.webrtc.v1.ConnectionSignalingPathR\rsignalingPath\x12!\n\x0cfailure_code\x18\x06 \x01(\x05R\x0bfailureCode""\n ReportConnectionMetadataResponse*\x8e\x01\n\x10ICECandidateType\x12"\n\x1eICE_CANDIDATE_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17ICE_CANDIDATE_TYPE_HOST\x10\x01\x12\x1b\n\x17ICE_CANDIDATE_TYPE_STUN\x10\x02\x12\x1c\n\x18ICE_CANDIDATE_TYPE_RELAY\x10\x03*\xf8\x01\n\tDialStage\x12\x1a\n\x16DIAL_STAGE_UNSPECIFIED\x10\x00\x12"\n\x1eDIAL_STAGE_SIGNALING_CONNECTED\x10\x01\x12\x1d\n\x19DIAL_STAGE_CONFIG_FETCHED\x10\x02\x12\x19\n\x15DIAL_STAGE_OFFER_SENT\x10\x03\x12\x1e\n\x1aDIAL_STAGE_ANSWER_RECEIVED\x10\x04\x12\x1c\n\x18DIAL_STAGE_ICE_CONNECTED\x10\x05\x12\x1d\n\x19DIAL_STAGE_DTLS_CONNECTED\x10\x06\x12\x14\n\x10DIAL_STAGE_READY\x10\x07*\xc1\x01\n\x17ConnectionSignalingPath\x12)\n%CONNECTION_SIGNALING_PATH_UNSPECIFIED\x10\x00\x12,\n(CONNECTION_SIGNALING_PATH_CLOUD_SIGNALED\x10\x01\x12(\n$CONNECTION_SIGNALING_PATH_MDNS_LOCAL\x10\x02\x12#\n\x1fCONNECTION_SIGNALING_PATH_LOCAL\x10\x032\xc3\x05\n\x10SignalingService\x12j\n\x04Call\x12 .proto.rpc.webrtc.v1.CallRequest\x1a!.proto.rpc.webrtc.v1.CallResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x13/rpc/webrtc/v1/call0\x01\x12\x81\x01\n\nCallUpdate\x12&.proto.rpc.webrtc.v1.CallUpdateRequest\x1a\'.proto.rpc.webrtc.v1.CallUpdateResponse""\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/rpc/webrtc/v1/call_update\x12U\n\x06Answer\x12#.proto.rpc.webrtc.v1.AnswerResponse\x1a".proto.rpc.webrtc.v1.AnswerRequest(\x010\x01\x12\xaa\x01\n\x14OptionalWebRTCConfig\x120.proto.rpc.webrtc.v1.OptionalWebRTCConfigRequest\x1a1.proto.rpc.webrtc.v1.OptionalWebRTCConfigResponse"-\x82\xd3\xe4\x93\x02\'\x12%/rpc/webrtc/v1/optional_webrtc_config\x12\xba\x01\n\x18ReportConnectionMetadata\x124.proto.rpc.webrtc.v1.ReportConnectionMetadataRequest\x1a5.proto.rpc.webrtc.v1.ReportConnectionMetadataResponse"1\x82\xd3\xe4\x93\x02+")/rpc/webrtc/v1/report_connection_metadataB\'Z%go.viam.com/utils/proto/rpc/webrtc/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.rpc.webrtc.v1.signaling_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z%go.viam.com/utils/proto/rpc/webrtc/v1'
    _globals['_ANSWERREQUESTINITSTAGE_CALLERAUTHMETADATAENTRY']._loaded_options = None
    _globals['_ANSWERREQUESTINITSTAGE_CALLERAUTHMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_SIGNALINGSERVICE'].methods_by_name['Call']._loaded_options = None
    _globals['_SIGNALINGSERVICE'].methods_by_name['Call']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x13/rpc/webrtc/v1/call'
    _globals['_SIGNALINGSERVICE'].methods_by_name['CallUpdate']._loaded_options = None
    _globals['_SIGNALINGSERVICE'].methods_by_name['CallUpdate']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/rpc/webrtc/v1/call_update'
    _globals['_SIGNALINGSERVICE'].methods_by_name['OptionalWebRTCConfig']._loaded_options = None
    _globals['_SIGNALINGSERVICE'].methods_by_name['OptionalWebRTCConfig']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/rpc/webrtc/v1/optional_webrtc_config"
    _globals['_SIGNALINGSERVICE'].methods_by_name['ReportConnectionMetadata']._loaded_options = None
    _globals['_SIGNALINGSERVICE'].methods_by_name['ReportConnectionMetadata']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/rpc/webrtc/v1/report_connection_metadata'
    _globals['_ICECANDIDATETYPE']._serialized_start = 3502
    _globals['_ICECANDIDATETYPE']._serialized_end = 3644
    _globals['_DIALSTAGE']._serialized_start = 3647
    _globals['_DIALSTAGE']._serialized_end = 3895
    _globals['_CONNECTIONSIGNALINGPATH']._serialized_start = 3898
    _globals['_CONNECTIONSIGNALINGPATH']._serialized_end = 4091
    _globals['_ICECANDIDATE']._serialized_start = 149
    _globals['_ICECANDIDATE']._serialized_end = 372
    _globals['_CALLREQUEST']._serialized_start = 374
    _globals['_CALLREQUEST']._serialized_end = 446
    _globals['_CALLRESPONSEINITSTAGE']._serialized_start = 448
    _globals['_CALLRESPONSEINITSTAGE']._serialized_end = 489
    _globals['_CALLRESPONSEUPDATESTAGE']._serialized_start = 491
    _globals['_CALLRESPONSEUPDATESTAGE']._serialized_end = 581
    _globals['_CALLRESPONSE']._serialized_start = 584
    _globals['_CALLRESPONSE']._serialized_end = 765
    _globals['_CALLUPDATEREQUEST']._serialized_start = 768
    _globals['_CALLUPDATEREQUEST']._serialized_end = 950
    _globals['_CALLUPDATERESPONSE']._serialized_start = 952
    _globals['_CALLUPDATERESPONSE']._serialized_end = 972
    _globals['_ICESERVER']._serialized_start = 974
    _globals['_ICESERVER']._serialized_end = 1065
    _globals['_WEBRTCCONFIG']._serialized_start = 1068
    _globals['_WEBRTCCONFIG']._serialized_end = 1209
    _globals['_ANSWERREQUESTINITSTAGE']._serialized_start = 1212
    _globals['_ANSWERREQUESTINITSTAGE']._serialized_end = 1640
    _globals['_ANSWERREQUESTINITSTAGE_CALLERAUTHMETADATAENTRY']._serialized_start = 1558
    _globals['_ANSWERREQUESTINITSTAGE_CALLERAUTHMETADATAENTRY']._serialized_end = 1627
    _globals['_ANSWERREQUESTUPDATESTAGE']._serialized_start = 1642
    _globals['_ANSWERREQUESTUPDATESTAGE']._serialized_end = 1733
    _globals['_ANSWERREQUESTDONESTAGE']._serialized_start = 1735
    _globals['_ANSWERREQUESTDONESTAGE']._serialized_end = 1759
    _globals['_ANSWERREQUESTERRORSTAGE']._serialized_start = 1761
    _globals['_ANSWERREQUESTERRORSTAGE']._serialized_end = 1830
    _globals['_ANSWERREQUESTHEARTBEATSTAGE']._serialized_start = 1832
    _globals['_ANSWERREQUESTHEARTBEATSTAGE']._serialized_end = 1861
    _globals['_ANSWERREQUEST']._serialized_start = 1864
    _globals['_ANSWERREQUEST']._serialized_end = 2267
    _globals['_ANSWERRESPONSEINITSTAGE']._serialized_start = 2269
    _globals['_ANSWERRESPONSEINITSTAGE']._serialized_end = 2312
    _globals['_ANSWERRESPONSEUPDATESTAGE']._serialized_start = 2314
    _globals['_ANSWERRESPONSEUPDATESTAGE']._serialized_end = 2406
    _globals['_ANSWERRESPONSEDONESTAGE']._serialized_start = 2408
    _globals['_ANSWERRESPONSEDONESTAGE']._serialized_end = 2433
    _globals['_ANSWERRESPONSEERRORSTAGE']._serialized_start = 2435
    _globals['_ANSWERRESPONSEERRORSTAGE']._serialized_end = 2505
    _globals['_ANSWERRESPONSE']._serialized_start = 2508
    _globals['_ANSWERRESPONSE']._serialized_end = 2834
    _globals['_OPTIONALWEBRTCCONFIGREQUEST']._serialized_start = 2836
    _globals['_OPTIONALWEBRTCCONFIGREQUEST']._serialized_end = 2865
    _globals['_OPTIONALWEBRTCCONFIGRESPONSE']._serialized_start = 2867
    _globals['_OPTIONALWEBRTCCONFIGRESPONSE']._serialized_end = 2956
    _globals['_CONNECTIONCANDIDATE']._serialized_start = 2958
    _globals['_CONNECTIONCANDIDATE']._serialized_end = 3075
    _globals['_REPORTCONNECTIONMETADATAREQUEST']._serialized_start = 3078
    _globals['_REPORTCONNECTIONMETADATAREQUEST']._serialized_end = 3463
    _globals['_REPORTCONNECTIONMETADATARESPONSE']._serialized_start = 3465
    _globals['_REPORTCONNECTIONMETADATARESPONSE']._serialized_end = 3499
    _globals['_SIGNALINGSERVICE']._serialized_start = 4094
    _globals['_SIGNALINGSERVICE']._serialized_end = 4801