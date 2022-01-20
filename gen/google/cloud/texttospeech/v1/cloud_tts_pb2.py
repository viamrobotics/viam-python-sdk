# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/texttospeech/v1/cloud_tts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/texttospeech/v1/cloud_tts.proto\x12\x1cgoogle.cloud.texttospeech.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\">\n\x11ListVoicesRequest\x12)\n\rlanguage_code\x18\x01 \x01(\tB\x04\xe2\x41\x01\x01R\x0clanguageCode\"Q\n\x12ListVoicesResponse\x12;\n\x06voices\x18\x01 \x03(\x0b\x32#.google.cloud.texttospeech.v1.VoiceR\x06voices\"\xcd\x01\n\x05Voice\x12%\n\x0elanguage_codes\x18\x01 \x03(\tR\rlanguageCodes\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12N\n\x0bssml_gender\x18\x03 \x01(\x0e\x32-.google.cloud.texttospeech.v1.SsmlVoiceGenderR\nssmlGender\x12\x39\n\x19natural_sample_rate_hertz\x18\x04 \x01(\x05R\x16naturalSampleRateHertz\"\x87\x02\n\x17SynthesizeSpeechRequest\x12H\n\x05input\x18\x01 \x01(\x0b\x32,.google.cloud.texttospeech.v1.SynthesisInputB\x04\xe2\x41\x01\x02R\x05input\x12N\n\x05voice\x18\x02 \x01(\x0b\x32\x32.google.cloud.texttospeech.v1.VoiceSelectionParamsB\x04\xe2\x41\x01\x02R\x05voice\x12R\n\x0c\x61udio_config\x18\x03 \x01(\x0b\x32).google.cloud.texttospeech.v1.AudioConfigB\x04\xe2\x41\x01\x02R\x0b\x61udioConfig\"L\n\x0eSynthesisInput\x12\x14\n\x04text\x18\x01 \x01(\tH\x00R\x04text\x12\x14\n\x04ssml\x18\x02 \x01(\tH\x00R\x04ssmlB\x0e\n\x0cinput_source\"\xa5\x01\n\x14VoiceSelectionParams\x12)\n\rlanguage_code\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0clanguageCode\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12N\n\x0bssml_gender\x18\x03 \x01(\x0e\x32-.google.cloud.texttospeech.v1.SsmlVoiceGenderR\nssmlGender\"\xc4\x02\n\x0b\x41udioConfig\x12X\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32+.google.cloud.texttospeech.v1.AudioEncodingB\x04\xe2\x41\x01\x02R\raudioEncoding\x12*\n\rspeaking_rate\x18\x02 \x01(\x01\x42\x05\xe2\x41\x02\x04\x01R\x0cspeakingRate\x12\x1b\n\x05pitch\x18\x03 \x01(\x01\x42\x05\xe2\x41\x02\x04\x01R\x05pitch\x12+\n\x0evolume_gain_db\x18\x04 \x01(\x01\x42\x05\xe2\x41\x02\x04\x01R\x0cvolumeGainDb\x12\x30\n\x11sample_rate_hertz\x18\x05 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x0fsampleRateHertz\x12\x33\n\x12\x65\x66\x66\x65\x63ts_profile_id\x18\x06 \x03(\tB\x05\xe2\x41\x02\x04\x01R\x10\x65\x66\x66\x65\x63tsProfileId\"?\n\x18SynthesizeSpeechResponse\x12#\n\raudio_content\x18\x01 \x01(\x0cR\x0c\x61udioContent*W\n\x0fSsmlVoiceGender\x12!\n\x1dSSML_VOICE_GENDER_UNSPECIFIED\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\x12\x0b\n\x07NEUTRAL\x10\x03*i\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x0c\n\x08OGG_OPUS\x10\x03\x12\t\n\x05MULAW\x10\x05\x12\x08\n\x04\x41LAW\x10\x06\x32\xb4\x03\n\x0cTextToSpeech\x12\x93\x01\n\nListVoices\x12/.google.cloud.texttospeech.v1.ListVoicesRequest\x1a\x30.google.cloud.texttospeech.v1.ListVoicesResponse\"\"\xda\x41\rlanguage_code\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/voices\x12\xbc\x01\n\x10SynthesizeSpeech\x12\x35.google.cloud.texttospeech.v1.SynthesizeSpeechRequest\x1a\x36.google.cloud.texttospeech.v1.SynthesizeSpeechResponse\"9\xda\x41\x18input,voice,audio_config\x82\xd3\xe4\x93\x02\x18\"\x13/v1/text:synthesize:\x01*\x1aO\xca\x41\x1btexttospeech.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xbc\x02\n com.google.cloud.texttospeech.v1B\x11TextToSpeechProtoP\x01ZHgoogle.golang.org/genproto/googleapis/cloud/texttospeech/v1;texttospeech\xf8\x01\x01\xaa\x02\x1cGoogle.Cloud.TextToSpeech.V1\xca\x02\x1cGoogle\\Cloud\\TextToSpeech\\V1\xea\x02\x1fGoogle::Cloud::TextToSpeech::V1\xea\x41U\n\x1b\x61utoml.googleapis.com/Model\x12\x36projects/{project}/locations/{location}/models/{model}b\x06proto3')

_SSMLVOICEGENDER = DESCRIPTOR.enum_types_by_name['SsmlVoiceGender']
SsmlVoiceGender = enum_type_wrapper.EnumTypeWrapper(_SSMLVOICEGENDER)
_AUDIOENCODING = DESCRIPTOR.enum_types_by_name['AudioEncoding']
AudioEncoding = enum_type_wrapper.EnumTypeWrapper(_AUDIOENCODING)
SSML_VOICE_GENDER_UNSPECIFIED = 0
MALE = 1
FEMALE = 2
NEUTRAL = 3
AUDIO_ENCODING_UNSPECIFIED = 0
LINEAR16 = 1
MP3 = 2
OGG_OPUS = 3
MULAW = 5
ALAW = 6


_LISTVOICESREQUEST = DESCRIPTOR.message_types_by_name['ListVoicesRequest']
_LISTVOICESRESPONSE = DESCRIPTOR.message_types_by_name['ListVoicesResponse']
_VOICE = DESCRIPTOR.message_types_by_name['Voice']
_SYNTHESIZESPEECHREQUEST = DESCRIPTOR.message_types_by_name['SynthesizeSpeechRequest']
_SYNTHESISINPUT = DESCRIPTOR.message_types_by_name['SynthesisInput']
_VOICESELECTIONPARAMS = DESCRIPTOR.message_types_by_name['VoiceSelectionParams']
_AUDIOCONFIG = DESCRIPTOR.message_types_by_name['AudioConfig']
_SYNTHESIZESPEECHRESPONSE = DESCRIPTOR.message_types_by_name['SynthesizeSpeechResponse']
ListVoicesRequest = _reflection.GeneratedProtocolMessageType('ListVoicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOICESREQUEST,
  '__module__' : 'google.cloud.texttospeech.v1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.ListVoicesRequest)
  })
_sym_db.RegisterMessage(ListVoicesRequest)

ListVoicesResponse = _reflection.GeneratedProtocolMessageType('ListVoicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOICESRESPONSE,
  '__module__' : 'google.cloud.texttospeech.v1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.ListVoicesResponse)
  })
_sym_db.RegisterMessage(ListVoicesResponse)

Voice = _reflection.GeneratedProtocolMessageType('Voice', (_message.Message,), {
  'DESCRIPTOR' : _VOICE,
  '__module__' : 'google.cloud.texttospeech.v1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.Voice)
  })
_sym_db.RegisterMessage(Voice)

SynthesizeSpeechRequest = _reflection.GeneratedProtocolMessageType('SynthesizeSpeechRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZESPEECHREQUEST,
  '__module__' : 'google.cloud.texttospeech.v1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.SynthesizeSpeechRequest)
  })
_sym_db.RegisterMessage(SynthesizeSpeechRequest)

SynthesisInput = _reflection.GeneratedProtocolMessageType('SynthesisInput', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESISINPUT,
  '__module__' : 'google.cloud.texttospeech.v1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.SynthesisInput)
  })
_sym_db.RegisterMessage(SynthesisInput)

VoiceSelectionParams = _reflection.GeneratedProtocolMessageType('VoiceSelectionParams', (_message.Message,), {
  'DESCRIPTOR' : _VOICESELECTIONPARAMS,
  '__module__' : 'google.cloud.texttospeech.v1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.VoiceSelectionParams)
  })
_sym_db.RegisterMessage(VoiceSelectionParams)

AudioConfig = _reflection.GeneratedProtocolMessageType('AudioConfig', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCONFIG,
  '__module__' : 'google.cloud.texttospeech.v1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.AudioConfig)
  })
_sym_db.RegisterMessage(AudioConfig)

SynthesizeSpeechResponse = _reflection.GeneratedProtocolMessageType('SynthesizeSpeechResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZESPEECHRESPONSE,
  '__module__' : 'google.cloud.texttospeech.v1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.SynthesizeSpeechResponse)
  })
_sym_db.RegisterMessage(SynthesizeSpeechResponse)

_TEXTTOSPEECH = DESCRIPTOR.services_by_name['TextToSpeech']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.google.cloud.texttospeech.v1B\021TextToSpeechProtoP\001ZHgoogle.golang.org/genproto/googleapis/cloud/texttospeech/v1;texttospeech\370\001\001\252\002\034Google.Cloud.TextToSpeech.V1\312\002\034Google\\Cloud\\TextToSpeech\\V1\352\002\037Google::Cloud::TextToSpeech::V1\352AU\n\033automl.googleapis.com/Model\0226projects/{project}/locations/{location}/models/{model}'
  _LISTVOICESREQUEST.fields_by_name['language_code']._options = None
  _LISTVOICESREQUEST.fields_by_name['language_code']._serialized_options = b'\342A\001\001'
  _SYNTHESIZESPEECHREQUEST.fields_by_name['input']._options = None
  _SYNTHESIZESPEECHREQUEST.fields_by_name['input']._serialized_options = b'\342A\001\002'
  _SYNTHESIZESPEECHREQUEST.fields_by_name['voice']._options = None
  _SYNTHESIZESPEECHREQUEST.fields_by_name['voice']._serialized_options = b'\342A\001\002'
  _SYNTHESIZESPEECHREQUEST.fields_by_name['audio_config']._options = None
  _SYNTHESIZESPEECHREQUEST.fields_by_name['audio_config']._serialized_options = b'\342A\001\002'
  _VOICESELECTIONPARAMS.fields_by_name['language_code']._options = None
  _VOICESELECTIONPARAMS.fields_by_name['language_code']._serialized_options = b'\342A\001\002'
  _AUDIOCONFIG.fields_by_name['audio_encoding']._options = None
  _AUDIOCONFIG.fields_by_name['audio_encoding']._serialized_options = b'\342A\001\002'
  _AUDIOCONFIG.fields_by_name['speaking_rate']._options = None
  _AUDIOCONFIG.fields_by_name['speaking_rate']._serialized_options = b'\342A\002\004\001'
  _AUDIOCONFIG.fields_by_name['pitch']._options = None
  _AUDIOCONFIG.fields_by_name['pitch']._serialized_options = b'\342A\002\004\001'
  _AUDIOCONFIG.fields_by_name['volume_gain_db']._options = None
  _AUDIOCONFIG.fields_by_name['volume_gain_db']._serialized_options = b'\342A\002\004\001'
  _AUDIOCONFIG.fields_by_name['sample_rate_hertz']._options = None
  _AUDIOCONFIG.fields_by_name['sample_rate_hertz']._serialized_options = b'\342A\001\001'
  _AUDIOCONFIG.fields_by_name['effects_profile_id']._options = None
  _AUDIOCONFIG.fields_by_name['effects_profile_id']._serialized_options = b'\342A\002\004\001'
  _TEXTTOSPEECH._options = None
  _TEXTTOSPEECH._serialized_options = b'\312A\033texttospeech.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _TEXTTOSPEECH.methods_by_name['ListVoices']._options = None
  _TEXTTOSPEECH.methods_by_name['ListVoices']._serialized_options = b'\332A\rlanguage_code\202\323\344\223\002\014\022\n/v1/voices'
  _TEXTTOSPEECH.methods_by_name['SynthesizeSpeech']._options = None
  _TEXTTOSPEECH.methods_by_name['SynthesizeSpeech']._serialized_options = b'\332A\030input,voice,audio_config\202\323\344\223\002\030\"\023/v1/text:synthesize:\001*'
  _SSMLVOICEGENDER._serialized_start=1452
  _SSMLVOICEGENDER._serialized_end=1539
  _AUDIOENCODING._serialized_start=1541
  _AUDIOENCODING._serialized_end=1646
  _LISTVOICESREQUEST._serialized_start=193
  _LISTVOICESREQUEST._serialized_end=255
  _LISTVOICESRESPONSE._serialized_start=257
  _LISTVOICESRESPONSE._serialized_end=338
  _VOICE._serialized_start=341
  _VOICE._serialized_end=546
  _SYNTHESIZESPEECHREQUEST._serialized_start=549
  _SYNTHESIZESPEECHREQUEST._serialized_end=812
  _SYNTHESISINPUT._serialized_start=814
  _SYNTHESISINPUT._serialized_end=890
  _VOICESELECTIONPARAMS._serialized_start=893
  _VOICESELECTIONPARAMS._serialized_end=1058
  _AUDIOCONFIG._serialized_start=1061
  _AUDIOCONFIG._serialized_end=1385
  _SYNTHESIZESPEECHRESPONSE._serialized_start=1387
  _SYNTHESIZESPEECHRESPONSE._serialized_end=1450
  _TEXTTOSPEECH._serialized_start=1649
  _TEXTTOSPEECH._serialized_end=2085
# @@protoc_insertion_point(module_scope)
