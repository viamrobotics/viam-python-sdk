# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/session.proto
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
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.dialogflow.v2beta1 import agent_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_agent__pb2
from google.cloud.dialogflow.v2beta1 import audio_config_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_audio__config__pb2
from google.cloud.dialogflow.v2beta1 import context_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_context__pb2
from google.cloud.dialogflow.v2beta1 import gcs_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_gcs__pb2
from google.cloud.dialogflow.v2beta1 import intent_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_intent__pb2
from google.cloud.dialogflow.v2beta1 import session_entity_type_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_session__entity__type__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/dialogflow/v2beta1/session.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/dialogflow/v2beta1/agent.proto\x1a\x32google/cloud/dialogflow/v2beta1/audio_config.proto\x1a-google/cloud/dialogflow/v2beta1/context.proto\x1a)google/cloud/dialogflow/v2beta1/gcs.proto\x1a,google/cloud/dialogflow/v2beta1/intent.proto\x1a\x39google/cloud/dialogflow/v2beta1/session_entity_type.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/rpc/status.proto\x1a\x18google/type/latlng.proto\"\xde\x03\n\x13\x44\x65tectIntentRequest\x12\x44\n\x07session\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!dialogflow.googleapis.com/SessionR\x07session\x12S\n\x0cquery_params\x18\x02 \x01(\x0b\x32\x30.google.cloud.dialogflow.v2beta1.QueryParametersR\x0bqueryParams\x12R\n\x0bquery_input\x18\x03 \x01(\x0b\x32+.google.cloud.dialogflow.v2beta1.QueryInputB\x04\xe2\x41\x01\x02R\nqueryInput\x12\x62\n\x13output_audio_config\x18\x04 \x01(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.OutputAudioConfigR\x11outputAudioConfig\x12S\n\x18output_audio_config_mask\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x15outputAudioConfigMask\x12\x1f\n\x0binput_audio\x18\x05 \x01(\x0cR\ninputAudio\"\xb4\x03\n\x14\x44\x65tectIntentResponse\x12\x1f\n\x0bresponse_id\x18\x01 \x01(\tR\nresponseId\x12O\n\x0cquery_result\x18\x02 \x01(\x0b\x32,.google.cloud.dialogflow.v2beta1.QueryResultR\x0bqueryResult\x12h\n\x19\x61lternative_query_results\x18\x05 \x03(\x0b\x32,.google.cloud.dialogflow.v2beta1.QueryResultR\x17\x61lternativeQueryResults\x12\x39\n\x0ewebhook_status\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\rwebhookStatus\x12!\n\x0coutput_audio\x18\x04 \x01(\x0cR\x0boutputAudio\x12\x62\n\x13output_audio_config\x18\x06 \x01(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.OutputAudioConfigR\x11outputAudioConfig\"\xa7\x06\n\x0fQueryParameters\x12\x1b\n\ttime_zone\x18\x01 \x01(\tR\x08timeZone\x12\x36\n\x0cgeo_location\x18\x02 \x01(\x0b\x32\x13.google.type.LatLngR\x0bgeoLocation\x12\x44\n\x08\x63ontexts\x18\x03 \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.ContextR\x08\x63ontexts\x12%\n\x0ereset_contexts\x18\x04 \x01(\x08R\rresetContexts\x12\x64\n\x14session_entity_types\x18\x05 \x03(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.SessionEntityTypeR\x12sessionEntityTypes\x12\x31\n\x07payload\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructR\x07payload\x12\x30\n\x14knowledge_base_names\x18\x0c \x03(\tR\x12knowledgeBaseNames\x12\x8a\x01\n!sentiment_analysis_request_config\x18\n \x01(\x0b\x32?.google.cloud.dialogflow.v2beta1.SentimentAnalysisRequestConfigR\x1esentimentAnalysisRequestConfig\x12H\n\nsub_agents\x18\r \x03(\x0b\x32).google.cloud.dialogflow.v2beta1.SubAgentR\tsubAgents\x12m\n\x0fwebhook_headers\x18\x0e \x03(\x0b\x32\x44.google.cloud.dialogflow.v2beta1.QueryParameters.WebhookHeadersEntryR\x0ewebhookHeaders\x1a\x41\n\x13WebhookHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xc0\x02\n\nQueryInput\x12V\n\x0c\x61udio_config\x18\x01 \x01(\x0b\x32\x31.google.cloud.dialogflow.v2beta1.InputAudioConfigH\x00R\x0b\x61udioConfig\x12@\n\x04text\x18\x02 \x01(\x0b\x32*.google.cloud.dialogflow.v2beta1.TextInputH\x00R\x04text\x12\x43\n\x05\x65vent\x18\x03 \x01(\x0b\x32+.google.cloud.dialogflow.v2beta1.EventInputH\x00R\x05\x65vent\x12J\n\x04\x64tmf\x18\x04 \x01(\x0b\x32\x34.google.cloud.dialogflow.v2beta1.TelephonyDtmfEventsH\x00R\x04\x64tmfB\x07\n\x05input\"\xbb\x08\n\x0bQueryResult\x12\x1d\n\nquery_text\x18\x01 \x01(\tR\tqueryText\x12#\n\rlanguage_code\x18\x0f \x01(\tR\x0clanguageCode\x12\x42\n\x1dspeech_recognition_confidence\x18\x02 \x01(\x02R\x1bspeechRecognitionConfidence\x12\x16\n\x06\x61\x63tion\x18\x03 \x01(\tR\x06\x61\x63tion\x12\x37\n\nparameters\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructR\nparameters\x12=\n\x1b\x61ll_required_params_present\x18\x05 \x01(\x08R\x18\x61llRequiredParamsPresent\x12\x30\n\x14\x63\x61ncels_slot_filling\x18\x15 \x01(\x08R\x12\x63\x61ncelsSlotFilling\x12)\n\x10\x66ulfillment_text\x18\x06 \x01(\tR\x0f\x66ulfillmentText\x12\x62\n\x14\x66ulfillment_messages\x18\x07 \x03(\x0b\x32/.google.cloud.dialogflow.v2beta1.Intent.MessageR\x13\x66ulfillmentMessages\x12%\n\x0ewebhook_source\x18\x08 \x01(\tR\rwebhookSource\x12@\n\x0fwebhook_payload\x18\t \x01(\x0b\x32\x17.google.protobuf.StructR\x0ewebhookPayload\x12Q\n\x0foutput_contexts\x18\n \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.ContextR\x0eoutputContexts\x12?\n\x06intent\x18\x0b \x01(\x0b\x32\'.google.cloud.dialogflow.v2beta1.IntentR\x06intent\x12>\n\x1bintent_detection_confidence\x18\x0c \x01(\x02R\x19intentDetectionConfidence\x12@\n\x0f\x64iagnostic_info\x18\x0e \x01(\x0b\x32\x17.google.protobuf.StructR\x0e\x64iagnosticInfo\x12t\n\x19sentiment_analysis_result\x18\x11 \x01(\x0b\x32\x38.google.cloud.dialogflow.v2beta1.SentimentAnalysisResultR\x17sentimentAnalysisResult\x12^\n\x11knowledge_answers\x18\x12 \x01(\x0b\x32\x31.google.cloud.dialogflow.v2beta1.KnowledgeAnswersR\x10knowledgeAnswers\"\xfd\x03\n\x10KnowledgeAnswers\x12R\n\x07\x61nswers\x18\x01 \x03(\x0b\x32\x38.google.cloud.dialogflow.v2beta1.KnowledgeAnswers.AnswerR\x07\x61nswers\x1a\x94\x03\n\x06\x41nswer\x12?\n\x06source\x18\x01 \x01(\tB\'\xfa\x41$\n\"dialogflow.googleapis.com/DocumentR\x06source\x12!\n\x0c\x66\x61q_question\x18\x02 \x01(\tR\x0b\x66\x61qQuestion\x12\x16\n\x06\x61nswer\x18\x03 \x01(\tR\x06\x61nswer\x12\x83\x01\n\x16match_confidence_level\x18\x04 \x01(\x0e\x32M.google.cloud.dialogflow.v2beta1.KnowledgeAnswers.Answer.MatchConfidenceLevelR\x14matchConfidenceLevel\x12)\n\x10match_confidence\x18\x05 \x01(\x02R\x0fmatchConfidence\"]\n\x14MatchConfidenceLevel\x12&\n\"MATCH_CONFIDENCE_LEVEL_UNSPECIFIED\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04HIGH\x10\x03\"\x96\x04\n\x1cStreamingDetectIntentRequest\x12\x44\n\x07session\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!dialogflow.googleapis.com/SessionR\x07session\x12S\n\x0cquery_params\x18\x02 \x01(\x0b\x32\x30.google.cloud.dialogflow.v2beta1.QueryParametersR\x0bqueryParams\x12R\n\x0bquery_input\x18\x03 \x01(\x0b\x32+.google.cloud.dialogflow.v2beta1.QueryInputB\x04\xe2\x41\x01\x02R\nqueryInput\x12-\n\x10single_utterance\x18\x04 \x01(\x08\x42\x02\x18\x01R\x0fsingleUtterance\x12\x62\n\x13output_audio_config\x18\x05 \x01(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.OutputAudioConfigR\x11outputAudioConfig\x12S\n\x18output_audio_config_mask\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x15outputAudioConfigMask\x12\x1f\n\x0binput_audio\x18\x06 \x01(\x0cR\ninputAudio\"\xa9\x04\n\x1dStreamingDetectIntentResponse\x12\x1f\n\x0bresponse_id\x18\x01 \x01(\tR\nresponseId\x12j\n\x12recognition_result\x18\x02 \x01(\x0b\x32;.google.cloud.dialogflow.v2beta1.StreamingRecognitionResultR\x11recognitionResult\x12O\n\x0cquery_result\x18\x03 \x01(\x0b\x32,.google.cloud.dialogflow.v2beta1.QueryResultR\x0bqueryResult\x12h\n\x19\x61lternative_query_results\x18\x07 \x03(\x0b\x32,.google.cloud.dialogflow.v2beta1.QueryResultR\x17\x61lternativeQueryResults\x12\x39\n\x0ewebhook_status\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusR\rwebhookStatus\x12!\n\x0coutput_audio\x18\x05 \x01(\x0cR\x0boutputAudio\x12\x62\n\x13output_audio_config\x18\x06 \x01(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.OutputAudioConfigR\x11outputAudioConfig\"\xa4\x05\n\x1aStreamingRecognitionResult\x12j\n\x0cmessage_type\x18\x01 \x01(\x0e\x32G.google.cloud.dialogflow.v2beta1.StreamingRecognitionResult.MessageTypeR\x0bmessageType\x12\x1e\n\ntranscript\x18\x02 \x01(\tR\ntranscript\x12\x19\n\x08is_final\x18\x03 \x01(\x08R\x07isFinal\x12\x1e\n\nconfidence\x18\x04 \x01(\x02R\nconfidence\x12\x1c\n\tstability\x18\x06 \x01(\x02R\tstability\x12Y\n\x10speech_word_info\x18\x07 \x03(\x0b\x32/.google.cloud.dialogflow.v2beta1.SpeechWordInfoR\x0espeechWordInfo\x12\x45\n\x11speech_end_offset\x18\x08 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0fspeechEndOffset\x12#\n\rlanguage_code\x18\n \x01(\tR\x0clanguageCode\x12U\n\x0b\x64tmf_digits\x18\x05 \x01(\x0b\x32\x34.google.cloud.dialogflow.v2beta1.TelephonyDtmfEventsR\ndtmfDigits\"\x82\x01\n\x0bMessageType\x12\x1c\n\x18MESSAGE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTRANSCRIPT\x10\x01\x12\x0f\n\x0b\x44TMF_DIGITS\x10\x03\x12\x1b\n\x17\x45ND_OF_SINGLE_UTTERANCE\x10\x02\x12\x17\n\x13PARTIAL_DTMF_DIGITS\x10\x04\"D\n\tTextInput\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12#\n\rlanguage_code\x18\x02 \x01(\tR\x0clanguageCode\"~\n\nEventInput\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x37\n\nparameters\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructR\nparameters\x12#\n\rlanguage_code\x18\x03 \x01(\tR\x0clanguageCode\"a\n\x1eSentimentAnalysisRequestConfig\x12?\n\x1c\x61nalyze_query_text_sentiment\x18\x01 \x01(\x08R\x19\x61nalyzeQueryTextSentiment\"w\n\x17SentimentAnalysisResult\x12\\\n\x14query_text_sentiment\x18\x01 \x01(\x0b\x32*.google.cloud.dialogflow.v2beta1.SentimentR\x12queryTextSentiment\"?\n\tSentiment\x12\x14\n\x05score\x18\x01 \x01(\x02R\x05score\x12\x1c\n\tmagnitude\x18\x02 \x01(\x02R\tmagnitude2\x8d\x06\n\x08Sessions\x12\xe7\x03\n\x0c\x44\x65tectIntent\x12\x34.google.cloud.dialogflow.v2beta1.DetectIntentRequest\x1a\x35.google.cloud.dialogflow.v2beta1.DetectIntentResponse\"\xe9\x02\xda\x41\x13session,query_input\x82\xd3\xe4\x93\x02\xcc\x02\";/v2beta1/{session=projects/*/agent/sessions/*}:detectIntent:\x01*ZW\"R/v2beta1/{session=projects/*/agent/environments/*/users/*/sessions/*}:detectIntent:\x01*ZL\"G/v2beta1/{session=projects/*/locations/*/agent/sessions/*}:detectIntent:\x01*Zc\"^/v2beta1/{session=projects/*/locations/*/agent/environments/*/users/*/sessions/*}:detectIntent:\x01*\x12\x9c\x01\n\x15StreamingDetectIntent\x12=.google.cloud.dialogflow.v2beta1.StreamingDetectIntentRequest\x1a>.google.cloud.dialogflow.v2beta1.StreamingDetectIntentResponse\"\x00(\x01\x30\x01\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xff\x03\n#com.google.cloud.dialogflow.v2beta1B\x0cSessionProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1\xea\x41\xd1\x02\n!dialogflow.googleapis.com/Session\x12+projects/{project}/agent/sessions/{session}\x12Sprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}\x12@projects/{project}/locations/{location}/agent/sessions/{session}\x12hprojects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}b\x06proto3')



_DETECTINTENTREQUEST = DESCRIPTOR.message_types_by_name['DetectIntentRequest']
_DETECTINTENTRESPONSE = DESCRIPTOR.message_types_by_name['DetectIntentResponse']
_QUERYPARAMETERS = DESCRIPTOR.message_types_by_name['QueryParameters']
_QUERYPARAMETERS_WEBHOOKHEADERSENTRY = _QUERYPARAMETERS.nested_types_by_name['WebhookHeadersEntry']
_QUERYINPUT = DESCRIPTOR.message_types_by_name['QueryInput']
_QUERYRESULT = DESCRIPTOR.message_types_by_name['QueryResult']
_KNOWLEDGEANSWERS = DESCRIPTOR.message_types_by_name['KnowledgeAnswers']
_KNOWLEDGEANSWERS_ANSWER = _KNOWLEDGEANSWERS.nested_types_by_name['Answer']
_STREAMINGDETECTINTENTREQUEST = DESCRIPTOR.message_types_by_name['StreamingDetectIntentRequest']
_STREAMINGDETECTINTENTRESPONSE = DESCRIPTOR.message_types_by_name['StreamingDetectIntentResponse']
_STREAMINGRECOGNITIONRESULT = DESCRIPTOR.message_types_by_name['StreamingRecognitionResult']
_TEXTINPUT = DESCRIPTOR.message_types_by_name['TextInput']
_EVENTINPUT = DESCRIPTOR.message_types_by_name['EventInput']
_SENTIMENTANALYSISREQUESTCONFIG = DESCRIPTOR.message_types_by_name['SentimentAnalysisRequestConfig']
_SENTIMENTANALYSISRESULT = DESCRIPTOR.message_types_by_name['SentimentAnalysisResult']
_SENTIMENT = DESCRIPTOR.message_types_by_name['Sentiment']
_KNOWLEDGEANSWERS_ANSWER_MATCHCONFIDENCELEVEL = _KNOWLEDGEANSWERS_ANSWER.enum_types_by_name['MatchConfidenceLevel']
_STREAMINGRECOGNITIONRESULT_MESSAGETYPE = _STREAMINGRECOGNITIONRESULT.enum_types_by_name['MessageType']
DetectIntentRequest = _reflection.GeneratedProtocolMessageType('DetectIntentRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETECTINTENTREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.DetectIntentRequest)
  })
_sym_db.RegisterMessage(DetectIntentRequest)

DetectIntentResponse = _reflection.GeneratedProtocolMessageType('DetectIntentResponse', (_message.Message,), {
  'DESCRIPTOR' : _DETECTINTENTRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.DetectIntentResponse)
  })
_sym_db.RegisterMessage(DetectIntentResponse)

QueryParameters = _reflection.GeneratedProtocolMessageType('QueryParameters', (_message.Message,), {

  'WebhookHeadersEntry' : _reflection.GeneratedProtocolMessageType('WebhookHeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _QUERYPARAMETERS_WEBHOOKHEADERSENTRY,
    '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.QueryParameters.WebhookHeadersEntry)
    })
  ,
  'DESCRIPTOR' : _QUERYPARAMETERS,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.QueryParameters)
  })
_sym_db.RegisterMessage(QueryParameters)
_sym_db.RegisterMessage(QueryParameters.WebhookHeadersEntry)

QueryInput = _reflection.GeneratedProtocolMessageType('QueryInput', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINPUT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.QueryInput)
  })
_sym_db.RegisterMessage(QueryInput)

QueryResult = _reflection.GeneratedProtocolMessageType('QueryResult', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESULT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.QueryResult)
  })
_sym_db.RegisterMessage(QueryResult)

KnowledgeAnswers = _reflection.GeneratedProtocolMessageType('KnowledgeAnswers', (_message.Message,), {

  'Answer' : _reflection.GeneratedProtocolMessageType('Answer', (_message.Message,), {
    'DESCRIPTOR' : _KNOWLEDGEANSWERS_ANSWER,
    '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.KnowledgeAnswers.Answer)
    })
  ,
  'DESCRIPTOR' : _KNOWLEDGEANSWERS,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.KnowledgeAnswers)
  })
_sym_db.RegisterMessage(KnowledgeAnswers)
_sym_db.RegisterMessage(KnowledgeAnswers.Answer)

StreamingDetectIntentRequest = _reflection.GeneratedProtocolMessageType('StreamingDetectIntentRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGDETECTINTENTREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.StreamingDetectIntentRequest)
  })
_sym_db.RegisterMessage(StreamingDetectIntentRequest)

StreamingDetectIntentResponse = _reflection.GeneratedProtocolMessageType('StreamingDetectIntentResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGDETECTINTENTRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.StreamingDetectIntentResponse)
  })
_sym_db.RegisterMessage(StreamingDetectIntentResponse)

StreamingRecognitionResult = _reflection.GeneratedProtocolMessageType('StreamingRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONRESULT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.StreamingRecognitionResult)
  })
_sym_db.RegisterMessage(StreamingRecognitionResult)

TextInput = _reflection.GeneratedProtocolMessageType('TextInput', (_message.Message,), {
  'DESCRIPTOR' : _TEXTINPUT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.TextInput)
  })
_sym_db.RegisterMessage(TextInput)

EventInput = _reflection.GeneratedProtocolMessageType('EventInput', (_message.Message,), {
  'DESCRIPTOR' : _EVENTINPUT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.EventInput)
  })
_sym_db.RegisterMessage(EventInput)

SentimentAnalysisRequestConfig = _reflection.GeneratedProtocolMessageType('SentimentAnalysisRequestConfig', (_message.Message,), {
  'DESCRIPTOR' : _SENTIMENTANALYSISREQUESTCONFIG,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.SentimentAnalysisRequestConfig)
  })
_sym_db.RegisterMessage(SentimentAnalysisRequestConfig)

SentimentAnalysisResult = _reflection.GeneratedProtocolMessageType('SentimentAnalysisResult', (_message.Message,), {
  'DESCRIPTOR' : _SENTIMENTANALYSISRESULT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.SentimentAnalysisResult)
  })
_sym_db.RegisterMessage(SentimentAnalysisResult)

Sentiment = _reflection.GeneratedProtocolMessageType('Sentiment', (_message.Message,), {
  'DESCRIPTOR' : _SENTIMENT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.session_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.Sentiment)
  })
_sym_db.RegisterMessage(Sentiment)

_SESSIONS = DESCRIPTOR.services_by_name['Sessions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\014SessionProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1\352A\321\002\n!dialogflow.googleapis.com/Session\022+projects/{project}/agent/sessions/{session}\022Sprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}\022@projects/{project}/locations/{location}/agent/sessions/{session}\022hprojects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}'
  _DETECTINTENTREQUEST.fields_by_name['session']._options = None
  _DETECTINTENTREQUEST.fields_by_name['session']._serialized_options = b'\342A\001\002\372A#\n!dialogflow.googleapis.com/Session'
  _DETECTINTENTREQUEST.fields_by_name['query_input']._options = None
  _DETECTINTENTREQUEST.fields_by_name['query_input']._serialized_options = b'\342A\001\002'
  _QUERYPARAMETERS_WEBHOOKHEADERSENTRY._options = None
  _QUERYPARAMETERS_WEBHOOKHEADERSENTRY._serialized_options = b'8\001'
  _KNOWLEDGEANSWERS_ANSWER.fields_by_name['source']._options = None
  _KNOWLEDGEANSWERS_ANSWER.fields_by_name['source']._serialized_options = b'\372A$\n\"dialogflow.googleapis.com/Document'
  _STREAMINGDETECTINTENTREQUEST.fields_by_name['session']._options = None
  _STREAMINGDETECTINTENTREQUEST.fields_by_name['session']._serialized_options = b'\342A\001\002\372A#\n!dialogflow.googleapis.com/Session'
  _STREAMINGDETECTINTENTREQUEST.fields_by_name['query_input']._options = None
  _STREAMINGDETECTINTENTREQUEST.fields_by_name['query_input']._serialized_options = b'\342A\001\002'
  _STREAMINGDETECTINTENTREQUEST.fields_by_name['single_utterance']._options = None
  _STREAMINGDETECTINTENTREQUEST.fields_by_name['single_utterance']._serialized_options = b'\030\001'
  _SESSIONS._options = None
  _SESSIONS._serialized_options = b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
  _SESSIONS.methods_by_name['DetectIntent']._options = None
  _SESSIONS.methods_by_name['DetectIntent']._serialized_options = b'\332A\023session,query_input\202\323\344\223\002\314\002\";/v2beta1/{session=projects/*/agent/sessions/*}:detectIntent:\001*ZW\"R/v2beta1/{session=projects/*/agent/environments/*/users/*/sessions/*}:detectIntent:\001*ZL\"G/v2beta1/{session=projects/*/locations/*/agent/sessions/*}:detectIntent:\001*Zc\"^/v2beta1/{session=projects/*/locations/*/agent/environments/*/users/*/sessions/*}:detectIntent:\001*'
  _DETECTINTENTREQUEST._serialized_start=637
  _DETECTINTENTREQUEST._serialized_end=1115
  _DETECTINTENTRESPONSE._serialized_start=1118
  _DETECTINTENTRESPONSE._serialized_end=1554
  _QUERYPARAMETERS._serialized_start=1557
  _QUERYPARAMETERS._serialized_end=2364
  _QUERYPARAMETERS_WEBHOOKHEADERSENTRY._serialized_start=2299
  _QUERYPARAMETERS_WEBHOOKHEADERSENTRY._serialized_end=2364
  _QUERYINPUT._serialized_start=2367
  _QUERYINPUT._serialized_end=2687
  _QUERYRESULT._serialized_start=2690
  _QUERYRESULT._serialized_end=3773
  _KNOWLEDGEANSWERS._serialized_start=3776
  _KNOWLEDGEANSWERS._serialized_end=4285
  _KNOWLEDGEANSWERS_ANSWER._serialized_start=3881
  _KNOWLEDGEANSWERS_ANSWER._serialized_end=4285
  _KNOWLEDGEANSWERS_ANSWER_MATCHCONFIDENCELEVEL._serialized_start=4192
  _KNOWLEDGEANSWERS_ANSWER_MATCHCONFIDENCELEVEL._serialized_end=4285
  _STREAMINGDETECTINTENTREQUEST._serialized_start=4288
  _STREAMINGDETECTINTENTREQUEST._serialized_end=4822
  _STREAMINGDETECTINTENTRESPONSE._serialized_start=4825
  _STREAMINGDETECTINTENTRESPONSE._serialized_end=5378
  _STREAMINGRECOGNITIONRESULT._serialized_start=5381
  _STREAMINGRECOGNITIONRESULT._serialized_end=6057
  _STREAMINGRECOGNITIONRESULT_MESSAGETYPE._serialized_start=5927
  _STREAMINGRECOGNITIONRESULT_MESSAGETYPE._serialized_end=6057
  _TEXTINPUT._serialized_start=6059
  _TEXTINPUT._serialized_end=6127
  _EVENTINPUT._serialized_start=6129
  _EVENTINPUT._serialized_end=6255
  _SENTIMENTANALYSISREQUESTCONFIG._serialized_start=6257
  _SENTIMENTANALYSISREQUESTCONFIG._serialized_end=6354
  _SENTIMENTANALYSISRESULT._serialized_start=6356
  _SENTIMENTANALYSISRESULT._serialized_end=6475
  _SENTIMENT._serialized_start=6477
  _SENTIMENT._serialized_end=6540
  _SESSIONS._serialized_start=6543
  _SESSIONS._serialized_end=7324
# @@protoc_insertion_point(module_scope)
