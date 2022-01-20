# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/speech/v1p1beta1/cloud_speech.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.speech.v1p1beta1 import resource_pb2 as google_dot_cloud_dot_speech_dot_v1p1beta1_dot_resource__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/speech/v1p1beta1/cloud_speech.proto\x12\x1dgoogle.cloud.speech.v1p1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/cloud/speech/v1p1beta1/resource.proto\x1a#google/longrunning/operations.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"\xaf\x01\n\x10RecognizeRequest\x12N\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x30.google.cloud.speech.v1p1beta1.RecognitionConfigB\x04\xe2\x41\x01\x02R\x06\x63onfig\x12K\n\x05\x61udio\x18\x02 \x01(\x0b\x32/.google.cloud.speech.v1p1beta1.RecognitionAudioB\x04\xe2\x41\x01\x02R\x05\x61udio\"\x9c\x02\n\x1bLongRunningRecognizeRequest\x12N\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x30.google.cloud.speech.v1p1beta1.RecognitionConfigB\x04\xe2\x41\x01\x02R\x06\x63onfig\x12K\n\x05\x61udio\x18\x02 \x01(\x0b\x32/.google.cloud.speech.v1p1beta1.RecognitionAudioB\x04\xe2\x41\x01\x02R\x05\x61udio\x12`\n\routput_config\x18\x04 \x01(\x0b\x32\x35.google.cloud.speech.v1p1beta1.TranscriptOutputConfigB\x04\xe2\x41\x01\x01R\x0coutputConfig\"B\n\x16TranscriptOutputConfig\x12\x19\n\x07gcs_uri\x18\x01 \x01(\tH\x00R\x06gcsUriB\r\n\x0boutput_type\"\xbf\x01\n\x19StreamingRecognizeRequest\x12\x66\n\x10streaming_config\x18\x01 \x01(\x0b\x32\x39.google.cloud.speech.v1p1beta1.StreamingRecognitionConfigH\x00R\x0fstreamingConfig\x12%\n\raudio_content\x18\x02 \x01(\x0cH\x00R\x0c\x61udioContentB\x13\n\x11streaming_request\"\xc0\x01\n\x1aStreamingRecognitionConfig\x12N\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x30.google.cloud.speech.v1p1beta1.RecognitionConfigB\x04\xe2\x41\x01\x02R\x06\x63onfig\x12)\n\x10single_utterance\x18\x02 \x01(\x08R\x0fsingleUtterance\x12\'\n\x0finterim_results\x18\x03 \x01(\x08R\x0einterimResults\"\xeb\x0c\n\x11RecognitionConfig\x12Z\n\x08\x65ncoding\x18\x01 \x01(\x0e\x32>.google.cloud.speech.v1p1beta1.RecognitionConfig.AudioEncodingR\x08\x65ncoding\x12*\n\x11sample_rate_hertz\x18\x02 \x01(\x05R\x0fsampleRateHertz\x12.\n\x13\x61udio_channel_count\x18\x07 \x01(\x05R\x11\x61udioChannelCount\x12T\n\'enable_separate_recognition_per_channel\x18\x0c \x01(\x08R#enableSeparateRecognitionPerChannel\x12)\n\rlanguage_code\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x0clanguageCode\x12<\n\x1a\x61lternative_language_codes\x18\x12 \x03(\tR\x18\x61lternativeLanguageCodes\x12)\n\x10max_alternatives\x18\x04 \x01(\x05R\x0fmaxAlternatives\x12)\n\x10profanity_filter\x18\x05 \x01(\x08R\x0fprofanityFilter\x12O\n\nadaptation\x18\x14 \x01(\x0b\x32/.google.cloud.speech.v1p1beta1.SpeechAdaptationR\nadaptation\x12q\n\x18transcript_normalization\x18\x18 \x01(\x0b\x32\x36.google.cloud.speech.v1p1beta1.TranscriptNormalizationR\x17transcriptNormalization\x12U\n\x0fspeech_contexts\x18\x06 \x03(\x0b\x32,.google.cloud.speech.v1p1beta1.SpeechContextR\x0espeechContexts\x12\x37\n\x18\x65nable_word_time_offsets\x18\x08 \x01(\x08R\x15\x65nableWordTimeOffsets\x12\x34\n\x16\x65nable_word_confidence\x18\x0f \x01(\x08R\x14\x65nableWordConfidence\x12@\n\x1c\x65nable_automatic_punctuation\x18\x0b \x01(\x08R\x1a\x65nableAutomaticPunctuation\x12V\n\x19\x65nable_spoken_punctuation\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x17\x65nableSpokenPunctuation\x12L\n\x14\x65nable_spoken_emojis\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x12\x65nableSpokenEmojis\x12@\n\x1a\x65nable_speaker_diarization\x18\x10 \x01(\x08\x42\x02\x18\x01R\x18\x65nableSpeakerDiarization\x12>\n\x19\x64iarization_speaker_count\x18\x11 \x01(\x05\x42\x02\x18\x01R\x17\x64iarizationSpeakerCount\x12\x66\n\x12\x64iarization_config\x18\x13 \x01(\x0b\x32\x37.google.cloud.speech.v1p1beta1.SpeakerDiarizationConfigR\x11\x64iarizationConfig\x12N\n\x08metadata\x18\t \x01(\x0b\x32\x32.google.cloud.speech.v1p1beta1.RecognitionMetadataR\x08metadata\x12\x14\n\x05model\x18\r \x01(\tR\x05model\x12!\n\x0cuse_enhanced\x18\x0e \x01(\x08R\x0buseEnhanced\"\xa3\x01\n\rAudioEncoding\x12\x18\n\x14\x45NCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x08\n\x04\x46LAC\x10\x02\x12\t\n\x05MULAW\x10\x03\x12\x07\n\x03\x41MR\x10\x04\x12\n\n\x06\x41MR_WB\x10\x05\x12\x0c\n\x08OGG_OPUS\x10\x06\x12\x1a\n\x16SPEEX_WITH_HEADER_BYTE\x10\x07\x12\x07\n\x03MP3\x10\x08\x12\r\n\tWEBM_OPUS\x10\t\"\xd9\x01\n\x18SpeakerDiarizationConfig\x12<\n\x1a\x65nable_speaker_diarization\x18\x01 \x01(\x08R\x18\x65nableSpeakerDiarization\x12*\n\x11min_speaker_count\x18\x02 \x01(\x05R\x0fminSpeakerCount\x12*\n\x11max_speaker_count\x18\x03 \x01(\x05R\x0fmaxSpeakerCount\x12\'\n\x0bspeaker_tag\x18\x05 \x01(\x05\x42\x06\x18\x01\xe2\x41\x01\x03R\nspeakerTag\"\xff\t\n\x13RecognitionMetadata\x12m\n\x10interaction_type\x18\x01 \x01(\x0e\x32\x42.google.cloud.speech.v1p1beta1.RecognitionMetadata.InteractionTypeR\x0finteractionType\x12>\n\x1cindustry_naics_code_of_audio\x18\x03 \x01(\rR\x18industryNaicsCodeOfAudio\x12v\n\x13microphone_distance\x18\x04 \x01(\x0e\x32\x45.google.cloud.speech.v1p1beta1.RecognitionMetadata.MicrophoneDistanceR\x12microphoneDistance\x12t\n\x13original_media_type\x18\x05 \x01(\x0e\x32\x44.google.cloud.speech.v1p1beta1.RecognitionMetadata.OriginalMediaTypeR\x11originalMediaType\x12z\n\x15recording_device_type\x18\x06 \x01(\x0e\x32\x46.google.cloud.speech.v1p1beta1.RecognitionMetadata.RecordingDeviceTypeR\x13recordingDeviceType\x12\x32\n\x15recording_device_name\x18\x07 \x01(\tR\x13recordingDeviceName\x12,\n\x12original_mime_type\x18\x08 \x01(\tR\x10originalMimeType\x12\'\n\robfuscated_id\x18\t \x01(\x03\x42\x02\x18\x01R\x0cobfuscatedId\x12\x1f\n\x0b\x61udio_topic\x18\n \x01(\tR\naudioTopic\"\xc5\x01\n\x0fInteractionType\x12 \n\x1cINTERACTION_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nDISCUSSION\x10\x01\x12\x10\n\x0cPRESENTATION\x10\x02\x12\x0e\n\nPHONE_CALL\x10\x03\x12\r\n\tVOICEMAIL\x10\x04\x12\x1b\n\x17PROFESSIONALLY_PRODUCED\x10\x05\x12\x10\n\x0cVOICE_SEARCH\x10\x06\x12\x11\n\rVOICE_COMMAND\x10\x07\x12\r\n\tDICTATION\x10\x08\"d\n\x12MicrophoneDistance\x12#\n\x1fMICROPHONE_DISTANCE_UNSPECIFIED\x10\x00\x12\r\n\tNEARFIELD\x10\x01\x12\x0c\n\x08MIDFIELD\x10\x02\x12\x0c\n\x08\x46\x41RFIELD\x10\x03\"N\n\x11OriginalMediaType\x12#\n\x1fORIGINAL_MEDIA_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x41UDIO\x10\x01\x12\t\n\x05VIDEO\x10\x02\"\xa4\x01\n\x13RecordingDeviceType\x12%\n!RECORDING_DEVICE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nSMARTPHONE\x10\x01\x12\x06\n\x02PC\x10\x02\x12\x0e\n\nPHONE_LINE\x10\x03\x12\x0b\n\x07VEHICLE\x10\x04\x12\x18\n\x14OTHER_OUTDOOR_DEVICE\x10\x05\x12\x17\n\x13OTHER_INDOOR_DEVICE\x10\x06\"?\n\rSpeechContext\x12\x18\n\x07phrases\x18\x01 \x03(\tR\x07phrases\x12\x14\n\x05\x62oost\x18\x04 \x01(\x02R\x05\x62oost\"R\n\x10RecognitionAudio\x12\x1a\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00R\x07\x63ontent\x12\x12\n\x03uri\x18\x02 \x01(\tH\x00R\x03uriB\x0e\n\x0c\x61udio_source\"\xac\x01\n\x11RecognizeResponse\x12P\n\x07results\x18\x02 \x03(\x0b\x32\x36.google.cloud.speech.v1p1beta1.SpeechRecognitionResultR\x07results\x12\x45\n\x11total_billed_time\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0ftotalBilledTime\"\xca\x02\n\x1cLongRunningRecognizeResponse\x12P\n\x07results\x18\x02 \x03(\x0b\x32\x36.google.cloud.speech.v1p1beta1.SpeechRecognitionResultR\x07results\x12\x45\n\x11total_billed_time\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0ftotalBilledTime\x12Z\n\routput_config\x18\x06 \x01(\x0b\x32\x35.google.cloud.speech.v1p1beta1.TranscriptOutputConfigR\x0coutputConfig\x12\x35\n\x0coutput_error\x18\x07 \x01(\x0b\x32\x12.google.rpc.StatusR\x0boutputError\"\xc4\x02\n\x1cLongRunningRecognizeMetadata\x12)\n\x10progress_percent\x18\x01 \x01(\x05R\x0fprogressPercent\x12\x39\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x44\n\x10last_update_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0elastUpdateTime\x12\x16\n\x03uri\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\x03uri\x12`\n\routput_config\x18\x05 \x01(\x0b\x32\x35.google.cloud.speech.v1p1beta1.TranscriptOutputConfigB\x04\xe2\x41\x01\x03R\x0coutputConfig\"\xa7\x03\n\x1aStreamingRecognizeResponse\x12(\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.google.rpc.StatusR\x05\x65rror\x12S\n\x07results\x18\x02 \x03(\x0b\x32\x39.google.cloud.speech.v1p1beta1.StreamingRecognitionResultR\x07results\x12u\n\x11speech_event_type\x18\x04 \x01(\x0e\x32I.google.cloud.speech.v1p1beta1.StreamingRecognizeResponse.SpeechEventTypeR\x0fspeechEventType\x12\x45\n\x11total_billed_time\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0ftotalBilledTime\"L\n\x0fSpeechEventType\x12\x1c\n\x18SPEECH_EVENT_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x45ND_OF_SINGLE_UTTERANCE\x10\x01\"\xc5\x02\n\x1aStreamingRecognitionResult\x12_\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32;.google.cloud.speech.v1p1beta1.SpeechRecognitionAlternativeR\x0c\x61lternatives\x12\x19\n\x08is_final\x18\x02 \x01(\x08R\x07isFinal\x12\x1c\n\tstability\x18\x03 \x01(\x02R\tstability\x12\x41\n\x0fresult_end_time\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\rresultEndTime\x12\x1f\n\x0b\x63hannel_tag\x18\x05 \x01(\x05R\nchannelTag\x12)\n\rlanguage_code\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03R\x0clanguageCode\"\x89\x02\n\x17SpeechRecognitionResult\x12_\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32;.google.cloud.speech.v1p1beta1.SpeechRecognitionAlternativeR\x0c\x61lternatives\x12\x1f\n\x0b\x63hannel_tag\x18\x02 \x01(\x05R\nchannelTag\x12\x41\n\x0fresult_end_time\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\rresultEndTime\x12)\n\rlanguage_code\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\x0clanguageCode\"\x9d\x01\n\x1cSpeechRecognitionAlternative\x12\x1e\n\ntranscript\x18\x01 \x01(\tR\ntranscript\x12\x1e\n\nconfidence\x18\x02 \x01(\x02R\nconfidence\x12=\n\x05words\x18\x03 \x03(\x0b\x32\'.google.cloud.speech.v1p1beta1.WordInfoR\x05words\"\xd5\x01\n\x08WordInfo\x12\x38\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\tstartTime\x12\x34\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x07\x65ndTime\x12\x12\n\x04word\x18\x03 \x01(\tR\x04word\x12\x1e\n\nconfidence\x18\x04 \x01(\x02R\nconfidence\x12%\n\x0bspeaker_tag\x18\x05 \x01(\x05\x42\x04\xe2\x41\x01\x03R\nspeakerTag2\x82\x05\n\x06Speech\x12\xa5\x01\n\tRecognize\x12/.google.cloud.speech.v1p1beta1.RecognizeRequest\x1a\x30.google.cloud.speech.v1p1beta1.RecognizeResponse\"5\xda\x41\x0c\x63onfig,audio\x82\xd3\xe4\x93\x02 \"\x1b/v1p1beta1/speech:recognize:\x01*\x12\xf2\x01\n\x14LongRunningRecognize\x12:.google.cloud.speech.v1p1beta1.LongRunningRecognizeRequest\x1a\x1d.google.longrunning.Operation\"\x7f\xca\x41<\n\x1cLongRunningRecognizeResponse\x12\x1cLongRunningRecognizeMetadata\xda\x41\x0c\x63onfig,audio\x82\xd3\xe4\x93\x02+\"&/v1p1beta1/speech:longrunningrecognize:\x01*\x12\x8f\x01\n\x12StreamingRecognize\x12\x38.google.cloud.speech.v1p1beta1.StreamingRecognizeRequest\x1a\x39.google.cloud.speech.v1p1beta1.StreamingRecognizeResponse\"\x00(\x01\x30\x01\x1aI\xca\x41\x15speech.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x80\x01\n!com.google.cloud.speech.v1p1beta1B\x0bSpeechProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/speech/v1p1beta1;speech\xf8\x01\x01\xa2\x02\x03GCSb\x06proto3')



_RECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['RecognizeRequest']
_LONGRUNNINGRECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['LongRunningRecognizeRequest']
_TRANSCRIPTOUTPUTCONFIG = DESCRIPTOR.message_types_by_name['TranscriptOutputConfig']
_STREAMINGRECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['StreamingRecognizeRequest']
_STREAMINGRECOGNITIONCONFIG = DESCRIPTOR.message_types_by_name['StreamingRecognitionConfig']
_RECOGNITIONCONFIG = DESCRIPTOR.message_types_by_name['RecognitionConfig']
_SPEAKERDIARIZATIONCONFIG = DESCRIPTOR.message_types_by_name['SpeakerDiarizationConfig']
_RECOGNITIONMETADATA = DESCRIPTOR.message_types_by_name['RecognitionMetadata']
_SPEECHCONTEXT = DESCRIPTOR.message_types_by_name['SpeechContext']
_RECOGNITIONAUDIO = DESCRIPTOR.message_types_by_name['RecognitionAudio']
_RECOGNIZERESPONSE = DESCRIPTOR.message_types_by_name['RecognizeResponse']
_LONGRUNNINGRECOGNIZERESPONSE = DESCRIPTOR.message_types_by_name['LongRunningRecognizeResponse']
_LONGRUNNINGRECOGNIZEMETADATA = DESCRIPTOR.message_types_by_name['LongRunningRecognizeMetadata']
_STREAMINGRECOGNIZERESPONSE = DESCRIPTOR.message_types_by_name['StreamingRecognizeResponse']
_STREAMINGRECOGNITIONRESULT = DESCRIPTOR.message_types_by_name['StreamingRecognitionResult']
_SPEECHRECOGNITIONRESULT = DESCRIPTOR.message_types_by_name['SpeechRecognitionResult']
_SPEECHRECOGNITIONALTERNATIVE = DESCRIPTOR.message_types_by_name['SpeechRecognitionAlternative']
_WORDINFO = DESCRIPTOR.message_types_by_name['WordInfo']
_RECOGNITIONCONFIG_AUDIOENCODING = _RECOGNITIONCONFIG.enum_types_by_name['AudioEncoding']
_RECOGNITIONMETADATA_INTERACTIONTYPE = _RECOGNITIONMETADATA.enum_types_by_name['InteractionType']
_RECOGNITIONMETADATA_MICROPHONEDISTANCE = _RECOGNITIONMETADATA.enum_types_by_name['MicrophoneDistance']
_RECOGNITIONMETADATA_ORIGINALMEDIATYPE = _RECOGNITIONMETADATA.enum_types_by_name['OriginalMediaType']
_RECOGNITIONMETADATA_RECORDINGDEVICETYPE = _RECOGNITIONMETADATA.enum_types_by_name['RecordingDeviceType']
_STREAMINGRECOGNIZERESPONSE_SPEECHEVENTTYPE = _STREAMINGRECOGNIZERESPONSE.enum_types_by_name['SpeechEventType']
RecognizeRequest = _reflection.GeneratedProtocolMessageType('RecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZEREQUEST,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.RecognizeRequest)
  })
_sym_db.RegisterMessage(RecognizeRequest)

LongRunningRecognizeRequest = _reflection.GeneratedProtocolMessageType('LongRunningRecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _LONGRUNNINGRECOGNIZEREQUEST,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.LongRunningRecognizeRequest)
  })
_sym_db.RegisterMessage(LongRunningRecognizeRequest)

TranscriptOutputConfig = _reflection.GeneratedProtocolMessageType('TranscriptOutputConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIPTOUTPUTCONFIG,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.TranscriptOutputConfig)
  })
_sym_db.RegisterMessage(TranscriptOutputConfig)

StreamingRecognizeRequest = _reflection.GeneratedProtocolMessageType('StreamingRecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNIZEREQUEST,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.StreamingRecognizeRequest)
  })
_sym_db.RegisterMessage(StreamingRecognizeRequest)

StreamingRecognitionConfig = _reflection.GeneratedProtocolMessageType('StreamingRecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONCONFIG,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.StreamingRecognitionConfig)
  })
_sym_db.RegisterMessage(StreamingRecognitionConfig)

RecognitionConfig = _reflection.GeneratedProtocolMessageType('RecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONCONFIG,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.RecognitionConfig)
  })
_sym_db.RegisterMessage(RecognitionConfig)

SpeakerDiarizationConfig = _reflection.GeneratedProtocolMessageType('SpeakerDiarizationConfig', (_message.Message,), {
  'DESCRIPTOR' : _SPEAKERDIARIZATIONCONFIG,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.SpeakerDiarizationConfig)
  })
_sym_db.RegisterMessage(SpeakerDiarizationConfig)

RecognitionMetadata = _reflection.GeneratedProtocolMessageType('RecognitionMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONMETADATA,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.RecognitionMetadata)
  })
_sym_db.RegisterMessage(RecognitionMetadata)

SpeechContext = _reflection.GeneratedProtocolMessageType('SpeechContext', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHCONTEXT,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.SpeechContext)
  })
_sym_db.RegisterMessage(SpeechContext)

RecognitionAudio = _reflection.GeneratedProtocolMessageType('RecognitionAudio', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONAUDIO,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.RecognitionAudio)
  })
_sym_db.RegisterMessage(RecognitionAudio)

RecognizeResponse = _reflection.GeneratedProtocolMessageType('RecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZERESPONSE,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.RecognizeResponse)
  })
_sym_db.RegisterMessage(RecognizeResponse)

LongRunningRecognizeResponse = _reflection.GeneratedProtocolMessageType('LongRunningRecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _LONGRUNNINGRECOGNIZERESPONSE,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.LongRunningRecognizeResponse)
  })
_sym_db.RegisterMessage(LongRunningRecognizeResponse)

LongRunningRecognizeMetadata = _reflection.GeneratedProtocolMessageType('LongRunningRecognizeMetadata', (_message.Message,), {
  'DESCRIPTOR' : _LONGRUNNINGRECOGNIZEMETADATA,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.LongRunningRecognizeMetadata)
  })
_sym_db.RegisterMessage(LongRunningRecognizeMetadata)

StreamingRecognizeResponse = _reflection.GeneratedProtocolMessageType('StreamingRecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNIZERESPONSE,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.StreamingRecognizeResponse)
  })
_sym_db.RegisterMessage(StreamingRecognizeResponse)

StreamingRecognitionResult = _reflection.GeneratedProtocolMessageType('StreamingRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONRESULT,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.StreamingRecognitionResult)
  })
_sym_db.RegisterMessage(StreamingRecognitionResult)

SpeechRecognitionResult = _reflection.GeneratedProtocolMessageType('SpeechRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONRESULT,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.SpeechRecognitionResult)
  })
_sym_db.RegisterMessage(SpeechRecognitionResult)

SpeechRecognitionAlternative = _reflection.GeneratedProtocolMessageType('SpeechRecognitionAlternative', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONALTERNATIVE,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.SpeechRecognitionAlternative)
  })
_sym_db.RegisterMessage(SpeechRecognitionAlternative)

WordInfo = _reflection.GeneratedProtocolMessageType('WordInfo', (_message.Message,), {
  'DESCRIPTOR' : _WORDINFO,
  '__module__' : 'google.cloud.speech.v1p1beta1.cloud_speech_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.speech.v1p1beta1.WordInfo)
  })
_sym_db.RegisterMessage(WordInfo)

_SPEECH = DESCRIPTOR.services_by_name['Speech']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.speech.v1p1beta1B\013SpeechProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/speech/v1p1beta1;speech\370\001\001\242\002\003GCS'
  _RECOGNIZEREQUEST.fields_by_name['config']._options = None
  _RECOGNIZEREQUEST.fields_by_name['config']._serialized_options = b'\342A\001\002'
  _RECOGNIZEREQUEST.fields_by_name['audio']._options = None
  _RECOGNIZEREQUEST.fields_by_name['audio']._serialized_options = b'\342A\001\002'
  _LONGRUNNINGRECOGNIZEREQUEST.fields_by_name['config']._options = None
  _LONGRUNNINGRECOGNIZEREQUEST.fields_by_name['config']._serialized_options = b'\342A\001\002'
  _LONGRUNNINGRECOGNIZEREQUEST.fields_by_name['audio']._options = None
  _LONGRUNNINGRECOGNIZEREQUEST.fields_by_name['audio']._serialized_options = b'\342A\001\002'
  _LONGRUNNINGRECOGNIZEREQUEST.fields_by_name['output_config']._options = None
  _LONGRUNNINGRECOGNIZEREQUEST.fields_by_name['output_config']._serialized_options = b'\342A\001\001'
  _STREAMINGRECOGNITIONCONFIG.fields_by_name['config']._options = None
  _STREAMINGRECOGNITIONCONFIG.fields_by_name['config']._serialized_options = b'\342A\001\002'
  _RECOGNITIONCONFIG.fields_by_name['language_code']._options = None
  _RECOGNITIONCONFIG.fields_by_name['language_code']._serialized_options = b'\342A\001\002'
  _RECOGNITIONCONFIG.fields_by_name['enable_speaker_diarization']._options = None
  _RECOGNITIONCONFIG.fields_by_name['enable_speaker_diarization']._serialized_options = b'\030\001'
  _RECOGNITIONCONFIG.fields_by_name['diarization_speaker_count']._options = None
  _RECOGNITIONCONFIG.fields_by_name['diarization_speaker_count']._serialized_options = b'\030\001'
  _SPEAKERDIARIZATIONCONFIG.fields_by_name['speaker_tag']._options = None
  _SPEAKERDIARIZATIONCONFIG.fields_by_name['speaker_tag']._serialized_options = b'\030\001\342A\001\003'
  _RECOGNITIONMETADATA.fields_by_name['obfuscated_id']._options = None
  _RECOGNITIONMETADATA.fields_by_name['obfuscated_id']._serialized_options = b'\030\001'
  _LONGRUNNINGRECOGNIZEMETADATA.fields_by_name['uri']._options = None
  _LONGRUNNINGRECOGNIZEMETADATA.fields_by_name['uri']._serialized_options = b'\342A\001\003'
  _LONGRUNNINGRECOGNIZEMETADATA.fields_by_name['output_config']._options = None
  _LONGRUNNINGRECOGNIZEMETADATA.fields_by_name['output_config']._serialized_options = b'\342A\001\003'
  _STREAMINGRECOGNITIONRESULT.fields_by_name['language_code']._options = None
  _STREAMINGRECOGNITIONRESULT.fields_by_name['language_code']._serialized_options = b'\342A\001\003'
  _SPEECHRECOGNITIONRESULT.fields_by_name['language_code']._options = None
  _SPEECHRECOGNITIONRESULT.fields_by_name['language_code']._serialized_options = b'\342A\001\003'
  _WORDINFO.fields_by_name['speaker_tag']._options = None
  _WORDINFO.fields_by_name['speaker_tag']._serialized_options = b'\342A\001\003'
  _SPEECH._options = None
  _SPEECH._serialized_options = b'\312A\025speech.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _SPEECH.methods_by_name['Recognize']._options = None
  _SPEECH.methods_by_name['Recognize']._serialized_options = b'\332A\014config,audio\202\323\344\223\002 \"\033/v1p1beta1/speech:recognize:\001*'
  _SPEECH.methods_by_name['LongRunningRecognize']._options = None
  _SPEECH.methods_by_name['LongRunningRecognize']._serialized_options = b'\312A<\n\034LongRunningRecognizeResponse\022\034LongRunningRecognizeMetadata\332A\014config,audio\202\323\344\223\002+\"&/v1p1beta1/speech:longrunningrecognize:\001*'
  _RECOGNIZEREQUEST._serialized_start=404
  _RECOGNIZEREQUEST._serialized_end=579
  _LONGRUNNINGRECOGNIZEREQUEST._serialized_start=582
  _LONGRUNNINGRECOGNIZEREQUEST._serialized_end=866
  _TRANSCRIPTOUTPUTCONFIG._serialized_start=868
  _TRANSCRIPTOUTPUTCONFIG._serialized_end=934
  _STREAMINGRECOGNIZEREQUEST._serialized_start=937
  _STREAMINGRECOGNIZEREQUEST._serialized_end=1128
  _STREAMINGRECOGNITIONCONFIG._serialized_start=1131
  _STREAMINGRECOGNITIONCONFIG._serialized_end=1323
  _RECOGNITIONCONFIG._serialized_start=1326
  _RECOGNITIONCONFIG._serialized_end=2969
  _RECOGNITIONCONFIG_AUDIOENCODING._serialized_start=2806
  _RECOGNITIONCONFIG_AUDIOENCODING._serialized_end=2969
  _SPEAKERDIARIZATIONCONFIG._serialized_start=2972
  _SPEAKERDIARIZATIONCONFIG._serialized_end=3189
  _RECOGNITIONMETADATA._serialized_start=3192
  _RECOGNITIONMETADATA._serialized_end=4471
  _RECOGNITIONMETADATA_INTERACTIONTYPE._serialized_start=3925
  _RECOGNITIONMETADATA_INTERACTIONTYPE._serialized_end=4122
  _RECOGNITIONMETADATA_MICROPHONEDISTANCE._serialized_start=4124
  _RECOGNITIONMETADATA_MICROPHONEDISTANCE._serialized_end=4224
  _RECOGNITIONMETADATA_ORIGINALMEDIATYPE._serialized_start=4226
  _RECOGNITIONMETADATA_ORIGINALMEDIATYPE._serialized_end=4304
  _RECOGNITIONMETADATA_RECORDINGDEVICETYPE._serialized_start=4307
  _RECOGNITIONMETADATA_RECORDINGDEVICETYPE._serialized_end=4471
  _SPEECHCONTEXT._serialized_start=4473
  _SPEECHCONTEXT._serialized_end=4536
  _RECOGNITIONAUDIO._serialized_start=4538
  _RECOGNITIONAUDIO._serialized_end=4620
  _RECOGNIZERESPONSE._serialized_start=4623
  _RECOGNIZERESPONSE._serialized_end=4795
  _LONGRUNNINGRECOGNIZERESPONSE._serialized_start=4798
  _LONGRUNNINGRECOGNIZERESPONSE._serialized_end=5128
  _LONGRUNNINGRECOGNIZEMETADATA._serialized_start=5131
  _LONGRUNNINGRECOGNIZEMETADATA._serialized_end=5455
  _STREAMINGRECOGNIZERESPONSE._serialized_start=5458
  _STREAMINGRECOGNIZERESPONSE._serialized_end=5881
  _STREAMINGRECOGNIZERESPONSE_SPEECHEVENTTYPE._serialized_start=5805
  _STREAMINGRECOGNIZERESPONSE_SPEECHEVENTTYPE._serialized_end=5881
  _STREAMINGRECOGNITIONRESULT._serialized_start=5884
  _STREAMINGRECOGNITIONRESULT._serialized_end=6209
  _SPEECHRECOGNITIONRESULT._serialized_start=6212
  _SPEECHRECOGNITIONRESULT._serialized_end=6477
  _SPEECHRECOGNITIONALTERNATIVE._serialized_start=6480
  _SPEECHRECOGNITIONALTERNATIVE._serialized_end=6637
  _WORDINFO._serialized_start=6640
  _WORDINFO._serialized_end=6853
  _SPEECH._serialized_start=6856
  _SPEECH._serialized_end=7498
# @@protoc_insertion_point(module_scope)
