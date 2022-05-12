"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#proto/rpc/webrtc/v1/signaling.proto\x12\x13proto.rpc.webrtc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/rpc/status.proto"\xdf\x01\n\x0cICECandidate\x12\x1c\n\tcandidate\x18\x01 \x01(\tR\tcandidate\x12\x1c\n\x07sdp_mid\x18\x02 \x01(\tH\x00R\x06sdpMid\x88\x01\x01\x12+\n\x0fsdpm_line_index\x18\x03 \x01(\rH\x01R\rsdpmLineIndex\x88\x01\x01\x120\n\x11username_fragment\x18\x04 \x01(\tH\x02R\x10usernameFragment\x88\x01\x01B\n\n\x08_sdp_midB\x12\n\x10_sdpm_line_indexB\x14\n\x12_username_fragment"H\n\x0bCallRequest\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp\x12\'\n\x0fdisable_trickle\x18\x02 \x01(\x08R\x0edisableTrickle")\n\x15CallResponseInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp"Z\n\x17CallResponseUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\xb5\x01\n\x0cCallResponse\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12@\n\x04init\x18\x02 \x01(\x0b2*.proto.rpc.webrtc.v1.CallResponseInitStageH\x00R\x04init\x12F\n\x06update\x18\x03 \x01(\x0b2,.proto.rpc.webrtc.v1.CallResponseUpdateStageH\x00R\x06updateB\x07\n\x05stage"\xb6\x01\n\x11CallUpdateRequest\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12A\n\tcandidate\x18\x02 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateH\x00R\tcandidate\x12\x14\n\x04done\x18\x03 \x01(\x08H\x00R\x04done\x12*\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusH\x00R\x05errorB\x08\n\x06update"\x14\n\x12CallUpdateResponse"[\n\tICEServer\x12\x12\n\x04urls\x18\x01 \x03(\tR\x04urls\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username\x12\x1e\n\ncredential\x18\x03 \x01(\tR\ncredential"\x8d\x01\n\x0cWebRTCConfig\x12T\n\x16additional_ice_servers\x18\x01 \x03(\x0b2\x1e.proto.rpc.webrtc.v1.ICEServerR\x14additionalIceServers\x12\'\n\x0fdisable_trickle\x18\x02 \x01(\x08R\x0edisableTrickle"v\n\x16AnswerRequestInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp\x12J\n\x0foptional_config\x18\x02 \x01(\x0b2!.proto.rpc.webrtc.v1.WebRTCConfigR\x0eoptionalConfig"[\n\x18AnswerRequestUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\x18\n\x16AnswerRequestDoneStage"E\n\x17AnswerRequestErrorStage\x12*\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusR\x06status"\xc1\x02\n\rAnswerRequest\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12A\n\x04init\x18\x02 \x01(\x0b2+.proto.rpc.webrtc.v1.AnswerRequestInitStageH\x00R\x04init\x12G\n\x06update\x18\x03 \x01(\x0b2-.proto.rpc.webrtc.v1.AnswerRequestUpdateStageH\x00R\x06update\x12A\n\x04done\x18\x04 \x01(\x0b2+.proto.rpc.webrtc.v1.AnswerRequestDoneStageH\x00R\x04done\x12D\n\x05error\x18\x05 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerRequestErrorStageH\x00R\x05errorB\x07\n\x05stage"+\n\x17AnswerResponseInitStage\x12\x10\n\x03sdp\x18\x01 \x01(\tR\x03sdp"\\\n\x19AnswerResponseUpdateStage\x12?\n\tcandidate\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.ICECandidateR\tcandidate"\x19\n\x17AnswerResponseDoneStage"F\n\x18AnswerResponseErrorStage\x12*\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusR\x06status"\xc6\x02\n\x0eAnswerResponse\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12B\n\x04init\x18\x02 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerResponseInitStageH\x00R\x04init\x12H\n\x06update\x18\x03 \x01(\x0b2..proto.rpc.webrtc.v1.AnswerResponseUpdateStageH\x00R\x06update\x12B\n\x04done\x18\x04 \x01(\x0b2,.proto.rpc.webrtc.v1.AnswerResponseDoneStageH\x00R\x04done\x12E\n\x05error\x18\x05 \x01(\x0b2-.proto.rpc.webrtc.v1.AnswerResponseErrorStageH\x00R\x05errorB\x07\n\x05stage"\x1d\n\x1bOptionalWebRTCConfigRequest"Y\n\x1cOptionalWebRTCConfigResponse\x129\n\x06config\x18\x01 \x01(\x0b2!.proto.rpc.webrtc.v1.WebRTCConfigR\x06config2\x86\x04\n\x10SignalingService\x12j\n\x04Call\x12 .proto.rpc.webrtc.v1.CallRequest\x1a!.proto.rpc.webrtc.v1.CallResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x13/rpc/webrtc/v1/call0\x01\x12\x81\x01\n\nCallUpdate\x12&.proto.rpc.webrtc.v1.CallUpdateRequest\x1a\'.proto.rpc.webrtc.v1.CallUpdateResponse""\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/rpc/webrtc/v1/call_update\x12U\n\x06Answer\x12#.proto.rpc.webrtc.v1.AnswerResponse\x1a".proto.rpc.webrtc.v1.AnswerRequest(\x010\x01\x12\xaa\x01\n\x14OptionalWebRTCConfig\x120.proto.rpc.webrtc.v1.OptionalWebRTCConfigRequest\x1a1.proto.rpc.webrtc.v1.OptionalWebRTCConfigResponse"-\x82\xd3\xe4\x93\x02\'\x12%/rpc/webrtc/v1/optional_webrtc_configB\'Z%go.viam.com/utils/proto/rpc/webrtc/v1b\x06proto3')
_ICECANDIDATE = DESCRIPTOR.message_types_by_name['ICECandidate']
_CALLREQUEST = DESCRIPTOR.message_types_by_name['CallRequest']
_CALLRESPONSEINITSTAGE = DESCRIPTOR.message_types_by_name['CallResponseInitStage']
_CALLRESPONSEUPDATESTAGE = DESCRIPTOR.message_types_by_name['CallResponseUpdateStage']
_CALLRESPONSE = DESCRIPTOR.message_types_by_name['CallResponse']
_CALLUPDATEREQUEST = DESCRIPTOR.message_types_by_name['CallUpdateRequest']
_CALLUPDATERESPONSE = DESCRIPTOR.message_types_by_name['CallUpdateResponse']
_ICESERVER = DESCRIPTOR.message_types_by_name['ICEServer']
_WEBRTCCONFIG = DESCRIPTOR.message_types_by_name['WebRTCConfig']
_ANSWERREQUESTINITSTAGE = DESCRIPTOR.message_types_by_name['AnswerRequestInitStage']
_ANSWERREQUESTUPDATESTAGE = DESCRIPTOR.message_types_by_name['AnswerRequestUpdateStage']
_ANSWERREQUESTDONESTAGE = DESCRIPTOR.message_types_by_name['AnswerRequestDoneStage']
_ANSWERREQUESTERRORSTAGE = DESCRIPTOR.message_types_by_name['AnswerRequestErrorStage']
_ANSWERREQUEST = DESCRIPTOR.message_types_by_name['AnswerRequest']
_ANSWERRESPONSEINITSTAGE = DESCRIPTOR.message_types_by_name['AnswerResponseInitStage']
_ANSWERRESPONSEUPDATESTAGE = DESCRIPTOR.message_types_by_name['AnswerResponseUpdateStage']
_ANSWERRESPONSEDONESTAGE = DESCRIPTOR.message_types_by_name['AnswerResponseDoneStage']
_ANSWERRESPONSEERRORSTAGE = DESCRIPTOR.message_types_by_name['AnswerResponseErrorStage']
_ANSWERRESPONSE = DESCRIPTOR.message_types_by_name['AnswerResponse']
_OPTIONALWEBRTCCONFIGREQUEST = DESCRIPTOR.message_types_by_name['OptionalWebRTCConfigRequest']
_OPTIONALWEBRTCCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['OptionalWebRTCConfigResponse']
ICECandidate = _reflection.GeneratedProtocolMessageType('ICECandidate', (_message.Message,), {'DESCRIPTOR': _ICECANDIDATE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'ICECandidate represents an ICE candidate. From https://github.com/pion\n  /webrtc/blob/5f6baf73255598a7b4a7c9400bb0381acc9aa3dc/icecandidateinit\n  .go'})
_sym_db.RegisterMessage(ICECandidate)
CallRequest = _reflection.GeneratedProtocolMessageType('CallRequest', (_message.Message,), {'DESCRIPTOR': _CALLREQUEST, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'CallRequest is the SDP offer that the controlling side is making.\n  \n  Attributes:\n      disable_trickle:\n          when disable_trickle is true, the init stage will be the only\n          stage to be received in the response and the caller can expect\n          the SDP to contain all ICE candidates.\n  '})
_sym_db.RegisterMessage(CallRequest)
CallResponseInitStage = _reflection.GeneratedProtocolMessageType('CallResponseInitStage', (_message.Message,), {'DESCRIPTOR': _CALLRESPONSEINITSTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'CallResponseInitStage is the first and a one time stage that\n  represents the initial response to starting a call.'})
_sym_db.RegisterMessage(CallResponseInitStage)
CallResponseUpdateStage = _reflection.GeneratedProtocolMessageType('CallResponseUpdateStage', (_message.Message,), {'DESCRIPTOR': _CALLRESPONSEUPDATESTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'CallResponseUpdateStage is multiply used to trickle in ICE candidates\n  from the controlled (answering) side.'})
_sym_db.RegisterMessage(CallResponseUpdateStage)
CallResponse = _reflection.GeneratedProtocolMessageType('CallResponse', (_message.Message,), {'DESCRIPTOR': _CALLRESPONSE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'CallResponse is the SDP answer that the controlled side responds with.'})
_sym_db.RegisterMessage(CallResponse)
CallUpdateRequest = _reflection.GeneratedProtocolMessageType('CallUpdateRequest', (_message.Message,), {'DESCRIPTOR': _CALLUPDATEREQUEST, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'CallUpdateRequest updates the call with additional info to the\n  controlled side.'})
_sym_db.RegisterMessage(CallUpdateRequest)
CallUpdateResponse = _reflection.GeneratedProtocolMessageType('CallUpdateResponse', (_message.Message,), {'DESCRIPTOR': _CALLUPDATERESPONSE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'CallUpdateResponse contains nothing in response to a call update.'})
_sym_db.RegisterMessage(CallUpdateResponse)
ICEServer = _reflection.GeneratedProtocolMessageType('ICEServer', (_message.Message,), {'DESCRIPTOR': _ICESERVER, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'ICEServer describes an ICE server.'})
_sym_db.RegisterMessage(ICEServer)
WebRTCConfig = _reflection.GeneratedProtocolMessageType('WebRTCConfig', (_message.Message,), {'DESCRIPTOR': _WEBRTCCONFIG, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'WebRTCConfig represents parts of a WebRTC config.\n  \n  Attributes:\n      disable_trickle:\n          disable_trickle indicates if Trickle ICE should be used.\n          Currently, both sides must both respect this setting.\n  '})
_sym_db.RegisterMessage(WebRTCConfig)
AnswerRequestInitStage = _reflection.GeneratedProtocolMessageType('AnswerRequestInitStage', (_message.Message,), {'DESCRIPTOR': _ANSWERREQUESTINITSTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerRequestInitStage is the first and a one time stage that\n  represents the callers initial SDP request to the controlled\n  (answerer) side.'})
_sym_db.RegisterMessage(AnswerRequestInitStage)
AnswerRequestUpdateStage = _reflection.GeneratedProtocolMessageType('AnswerRequestUpdateStage', (_message.Message,), {'DESCRIPTOR': _ANSWERREQUESTUPDATESTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerRequestUpdateStage is multiply used to trickle in ICE candidates\n  to the controlled (answerer) side.'})
_sym_db.RegisterMessage(AnswerRequestUpdateStage)
AnswerRequestDoneStage = _reflection.GeneratedProtocolMessageType('AnswerRequestDoneStage', (_message.Message,), {'DESCRIPTOR': _ANSWERREQUESTDONESTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerRequestDoneStage indicates the controller is done responding\n  with candidates.'})
_sym_db.RegisterMessage(AnswerRequestDoneStage)
AnswerRequestErrorStage = _reflection.GeneratedProtocolMessageType('AnswerRequestErrorStage', (_message.Message,), {'DESCRIPTOR': _ANSWERREQUESTERRORSTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerRequestErrorStage indicates the exchange has failed with an\n  error.'})
_sym_db.RegisterMessage(AnswerRequestErrorStage)
AnswerRequest = _reflection.GeneratedProtocolMessageType('AnswerRequest', (_message.Message,), {'DESCRIPTOR': _ANSWERREQUEST, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerRequest is the SDP offer that the controlling side is making via\n  the answering stream.\n  \n  Attributes:\n      done:\n          done is sent when the requester is done sending information\n      error:\n          error is sent any time before done\n  '})
_sym_db.RegisterMessage(AnswerRequest)
AnswerResponseInitStage = _reflection.GeneratedProtocolMessageType('AnswerResponseInitStage', (_message.Message,), {'DESCRIPTOR': _ANSWERRESPONSEINITSTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerResponseInitStage is the first and a one time stage that\n  represents the answerers initial SDP response to the controlling side.'})
_sym_db.RegisterMessage(AnswerResponseInitStage)
AnswerResponseUpdateStage = _reflection.GeneratedProtocolMessageType('AnswerResponseUpdateStage', (_message.Message,), {'DESCRIPTOR': _ANSWERRESPONSEUPDATESTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerResponseUpdateStage is multiply used to trickle in ICE\n  candidates to the controlling side.'})
_sym_db.RegisterMessage(AnswerResponseUpdateStage)
AnswerResponseDoneStage = _reflection.GeneratedProtocolMessageType('AnswerResponseDoneStage', (_message.Message,), {'DESCRIPTOR': _ANSWERRESPONSEDONESTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerResponseDoneStage indicates the answerer is done responding with\n  candidates.'})
_sym_db.RegisterMessage(AnswerResponseDoneStage)
AnswerResponseErrorStage = _reflection.GeneratedProtocolMessageType('AnswerResponseErrorStage', (_message.Message,), {'DESCRIPTOR': _ANSWERRESPONSEERRORSTAGE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerResponseErrorStage indicates the exchange has failed with an\n  error.'})
_sym_db.RegisterMessage(AnswerResponseErrorStage)
AnswerResponse = _reflection.GeneratedProtocolMessageType('AnswerResponse', (_message.Message,), {'DESCRIPTOR': _ANSWERRESPONSE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'AnswerResponse is the SDP answer that an answerer responds with.\n  \n  Attributes:\n      done:\n          done is sent when the answerer is done sending information\n      error:\n          error is sent any time before done\n  '})
_sym_db.RegisterMessage(AnswerResponse)
OptionalWebRTCConfigRequest = _reflection.GeneratedProtocolMessageType('OptionalWebRTCConfigRequest', (_message.Message,), {'DESCRIPTOR': _OPTIONALWEBRTCCONFIGREQUEST, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'OptionalWebRTCConfigRequest is the request for getting an optional\n  WebRTC config to use for the peer connection.'})
_sym_db.RegisterMessage(OptionalWebRTCConfigRequest)
OptionalWebRTCConfigResponse = _reflection.GeneratedProtocolMessageType('OptionalWebRTCConfigResponse', (_message.Message,), {'DESCRIPTOR': _OPTIONALWEBRTCCONFIGRESPONSE, '__module__': 'proto.rpc.webrtc.v1.signaling_pb2', '__doc__': 'OptionalWebRTCConfigResponse contains the optional WebRTC config to\n  use for the peer connection.'})
_sym_db.RegisterMessage(OptionalWebRTCConfigResponse)
_SIGNALINGSERVICE = DESCRIPTOR.services_by_name['SignalingService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%go.viam.com/utils/proto/rpc/webrtc/v1'
    _SIGNALINGSERVICE.methods_by_name['Call']._options = None
    _SIGNALINGSERVICE.methods_by_name['Call']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x13/rpc/webrtc/v1/call'
    _SIGNALINGSERVICE.methods_by_name['CallUpdate']._options = None
    _SIGNALINGSERVICE.methods_by_name['CallUpdate']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/rpc/webrtc/v1/call_update'
    _SIGNALINGSERVICE.methods_by_name['OptionalWebRTCConfig']._options = None
    _SIGNALINGSERVICE.methods_by_name['OptionalWebRTCConfig']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/rpc/webrtc/v1/optional_webrtc_config"
    _ICECANDIDATE._serialized_start = 116
    _ICECANDIDATE._serialized_end = 339
    _CALLREQUEST._serialized_start = 341
    _CALLREQUEST._serialized_end = 413
    _CALLRESPONSEINITSTAGE._serialized_start = 415
    _CALLRESPONSEINITSTAGE._serialized_end = 456
    _CALLRESPONSEUPDATESTAGE._serialized_start = 458
    _CALLRESPONSEUPDATESTAGE._serialized_end = 548
    _CALLRESPONSE._serialized_start = 551
    _CALLRESPONSE._serialized_end = 732
    _CALLUPDATEREQUEST._serialized_start = 735
    _CALLUPDATEREQUEST._serialized_end = 917
    _CALLUPDATERESPONSE._serialized_start = 919
    _CALLUPDATERESPONSE._serialized_end = 939
    _ICESERVER._serialized_start = 941
    _ICESERVER._serialized_end = 1032
    _WEBRTCCONFIG._serialized_start = 1035
    _WEBRTCCONFIG._serialized_end = 1176
    _ANSWERREQUESTINITSTAGE._serialized_start = 1178
    _ANSWERREQUESTINITSTAGE._serialized_end = 1296
    _ANSWERREQUESTUPDATESTAGE._serialized_start = 1298
    _ANSWERREQUESTUPDATESTAGE._serialized_end = 1389
    _ANSWERREQUESTDONESTAGE._serialized_start = 1391
    _ANSWERREQUESTDONESTAGE._serialized_end = 1415
    _ANSWERREQUESTERRORSTAGE._serialized_start = 1417
    _ANSWERREQUESTERRORSTAGE._serialized_end = 1486
    _ANSWERREQUEST._serialized_start = 1489
    _ANSWERREQUEST._serialized_end = 1810
    _ANSWERRESPONSEINITSTAGE._serialized_start = 1812
    _ANSWERRESPONSEINITSTAGE._serialized_end = 1855
    _ANSWERRESPONSEUPDATESTAGE._serialized_start = 1857
    _ANSWERRESPONSEUPDATESTAGE._serialized_end = 1949
    _ANSWERRESPONSEDONESTAGE._serialized_start = 1951
    _ANSWERRESPONSEDONESTAGE._serialized_end = 1976
    _ANSWERRESPONSEERRORSTAGE._serialized_start = 1978
    _ANSWERRESPONSEERRORSTAGE._serialized_end = 2048
    _ANSWERRESPONSE._serialized_start = 2051
    _ANSWERRESPONSE._serialized_end = 2377
    _OPTIONALWEBRTCCONFIGREQUEST._serialized_start = 2379
    _OPTIONALWEBRTCCONFIGREQUEST._serialized_end = 2408
    _OPTIONALWEBRTCCONFIGRESPONSE._serialized_start = 2410
    _OPTIONALWEBRTCCONFIGRESPONSE._serialized_end = 2499
    _SIGNALINGSERVICE._serialized_start = 2502
    _SIGNALINGSERVICE._serialized_end = 3020