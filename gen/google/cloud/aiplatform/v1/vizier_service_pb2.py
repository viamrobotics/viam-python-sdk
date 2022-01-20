# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/vizier_service.proto
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
from google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from google.cloud.aiplatform.v1 import study_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_study__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/aiplatform/v1/vizier_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a&google/cloud/aiplatform/v1/study.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"O\n\x0fGetStudyRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/StudyR\x04name\"\x97\x01\n\x12\x43reateStudyRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12=\n\x05study\x18\x02 \x01(\x0b\x32!.google.cloud.aiplatform.v1.StudyB\x04\xe2\x41\x01\x02R\x05study\"\xa0\x01\n\x12ListStudiesRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12#\n\npage_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\x12!\n\tpage_size\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\"z\n\x13ListStudiesResponse\x12;\n\x07studies\x18\x01 \x03(\x0b\x32!.google.cloud.aiplatform.v1.StudyR\x07studies\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"R\n\x12\x44\x65leteStudyRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/StudyR\x04name\"\x81\x01\n\x12LookupStudyRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\'\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x64isplayName\"\xac\x01\n\x14SuggestTrialsRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/StudyR\x06parent\x12/\n\x10suggestion_count\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x02R\x0fsuggestionCount\x12!\n\tclient_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x63lientId\"\x8e\x02\n\x15SuggestTrialsResponse\x12\x39\n\x06trials\x18\x01 \x03(\x0b\x32!.google.cloud.aiplatform.v1.TrialR\x06trials\x12H\n\x0bstudy_state\x18\x02 \x01(\x0e\x32\'.google.cloud.aiplatform.v1.Study.StateR\nstudyState\x12\x39\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\"\x95\x01\n\x15SuggestTrialsMetadata\x12_\n\x10generic_metadata\x18\x01 \x01(\x0b\x32\x34.google.cloud.aiplatform.v1.GenericOperationMetadataR\x0fgenericMetadata\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08\x63lientId\"\x95\x01\n\x12\x43reateTrialRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/StudyR\x06parent\x12=\n\x05trial\x18\x02 \x01(\x0b\x32!.google.cloud.aiplatform.v1.TrialB\x04\xe2\x41\x01\x02R\x05trial\"O\n\x0fGetTrialRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/TrialR\x04name\"\x9d\x01\n\x11ListTrialsRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/StudyR\x06parent\x12#\n\npage_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\x12!\n\tpage_size\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\"w\n\x12ListTrialsResponse\x12\x39\n\x06trials\x18\x01 \x03(\x0b\x32!.google.cloud.aiplatform.v1.TrialR\x06trials\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xb6\x01\n\x1a\x41\x64\x64TrialMeasurementRequest\x12G\n\ntrial_name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/TrialR\ttrialName\x12O\n\x0bmeasurement\x18\x03 \x01(\x0b\x32\'.google.cloud.aiplatform.v1.MeasurementB\x04\xe2\x41\x01\x02R\x0bmeasurement\"\x94\x02\n\x14\x43ompleteTrialRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/TrialR\x04name\x12Z\n\x11\x66inal_measurement\x18\x02 \x01(\x0b\x32\'.google.cloud.aiplatform.v1.MeasurementB\x04\xe2\x41\x01\x01R\x10\x66inalMeasurement\x12/\n\x10trial_infeasible\x18\x03 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x0ftrialInfeasible\x12\x31\n\x11infeasible_reason\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\x10infeasibleReason\"R\n\x12\x44\x65leteTrialRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/TrialR\x04name\"n\n#CheckTrialEarlyStoppingStateRequest\x12G\n\ntrial_name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/TrialR\ttrialName\"G\n$CheckTrialEarlyStoppingStateResponse\x12\x1f\n\x0bshould_stop\x18\x01 \x01(\x08R\nshouldStop\"\xb4\x01\n%CheckTrialEarlyStoppingStateMetatdata\x12_\n\x10generic_metadata\x18\x01 \x01(\x0b\x32\x34.google.cloud.aiplatform.v1.GenericOperationMetadataR\x0fgenericMetadata\x12\x14\n\x05study\x18\x02 \x01(\tR\x05study\x12\x14\n\x05trial\x18\x03 \x01(\tR\x05trial\"P\n\x10StopTrialRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/TrialR\x04name\"\\\n\x18ListOptimalTrialsRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x61iplatform.googleapis.com/StudyR\x06parent\"e\n\x19ListOptimalTrialsResponse\x12H\n\x0eoptimal_trials\x18\x01 \x03(\x0b\x32!.google.cloud.aiplatform.v1.TrialR\roptimalTrials2\xd4\x16\n\rVizierService\x12\xab\x01\n\x0b\x43reateStudy\x12..google.cloud.aiplatform.v1.CreateStudyRequest\x1a!.google.cloud.aiplatform.v1.Study\"I\xda\x41\x0cparent,study\x82\xd3\xe4\x93\x02\x34\"+/v1/{parent=projects/*/locations/*}/studies:\x05study\x12\x96\x01\n\x08GetStudy\x12+.google.cloud.aiplatform.v1.GetStudyRequest\x1a!.google.cloud.aiplatform.v1.Study\":\xda\x41\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/studies/*}\x12\xac\x01\n\x0bListStudies\x12..google.cloud.aiplatform.v1.ListStudiesRequest\x1a/.google.cloud.aiplatform.v1.ListStudiesResponse\"<\xda\x41\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/locations/*}/studies\x12\x91\x01\n\x0b\x44\x65leteStudy\x12..google.cloud.aiplatform.v1.DeleteStudyRequest\x1a\x16.google.protobuf.Empty\":\xda\x41\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/locations/*/studies/*}\x12\xa8\x01\n\x0bLookupStudy\x12..google.cloud.aiplatform.v1.LookupStudyRequest\x1a!.google.cloud.aiplatform.v1.Study\"F\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x37\"2/v1/{parent=projects/*/locations/*}/studies:lookup:\x01*\x12\xda\x01\n\rSuggestTrials\x12\x30.google.cloud.aiplatform.v1.SuggestTrialsRequest\x1a\x1d.google.longrunning.Operation\"x\xca\x41.\n\x15SuggestTrialsResponse\x12\x15SuggestTrialsMetadata\x82\xd3\xe4\x93\x02\x41\"</v1/{parent=projects/*/locations/*/studies/*}/trials:suggest:\x01*\x12\xb4\x01\n\x0b\x43reateTrial\x12..google.cloud.aiplatform.v1.CreateTrialRequest\x1a!.google.cloud.aiplatform.v1.Trial\"R\xda\x41\x0cparent,trial\x82\xd3\xe4\x93\x02=\"4/v1/{parent=projects/*/locations/*/studies/*}/trials:\x05trial\x12\x9f\x01\n\x08GetTrial\x12+.google.cloud.aiplatform.v1.GetTrialRequest\x1a!.google.cloud.aiplatform.v1.Trial\"C\xda\x41\x04name\x82\xd3\xe4\x93\x02\x36\x12\x34/v1/{name=projects/*/locations/*/studies/*/trials/*}\x12\xb2\x01\n\nListTrials\x12-.google.cloud.aiplatform.v1.ListTrialsRequest\x1a..google.cloud.aiplatform.v1.ListTrialsResponse\"E\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x36\x12\x34/v1/{parent=projects/*/locations/*/studies/*}/trials\x12\xcb\x01\n\x13\x41\x64\x64TrialMeasurement\x12\x36.google.cloud.aiplatform.v1.AddTrialMeasurementRequest\x1a!.google.cloud.aiplatform.v1.Trial\"Y\x82\xd3\xe4\x93\x02S\"N/v1/{trial_name=projects/*/locations/*/studies/*/trials/*}:addTrialMeasurement:\x01*\x12\xae\x01\n\rCompleteTrial\x12\x30.google.cloud.aiplatform.v1.CompleteTrialRequest\x1a!.google.cloud.aiplatform.v1.Trial\"H\x82\xd3\xe4\x93\x02\x42\"=/v1/{name=projects/*/locations/*/studies/*/trials/*}:complete:\x01*\x12\x9a\x01\n\x0b\x44\x65leteTrial\x12..google.cloud.aiplatform.v1.DeleteTrialRequest\x1a\x16.google.protobuf.Empty\"C\xda\x41\x04name\x82\xd3\xe4\x93\x02\x36*4/v1/{name=projects/*/locations/*/studies/*/trials/*}\x12\xb3\x02\n\x1c\x43heckTrialEarlyStoppingState\x12?.google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateRequest\x1a\x1d.google.longrunning.Operation\"\xb2\x01\xca\x41M\n$CheckTrialEarlyStoppingStateResponse\x12%CheckTrialEarlyStoppingStateMetatdata\x82\xd3\xe4\x93\x02\\\"W/v1/{trial_name=projects/*/locations/*/studies/*/trials/*}:checkTrialEarlyStoppingState:\x01*\x12\xa2\x01\n\tStopTrial\x12,.google.cloud.aiplatform.v1.StopTrialRequest\x1a!.google.cloud.aiplatform.v1.Trial\"D\x82\xd3\xe4\x93\x02>\"9/v1/{name=projects/*/locations/*/studies/*/trials/*}:stop:\x01*\x12\xdc\x01\n\x11ListOptimalTrials\x12\x34.google.cloud.aiplatform.v1.ListOptimalTrialsRequest\x1a\x35.google.cloud.aiplatform.v1.ListOptimalTrialsResponse\"Z\xda\x41\x06parent\x82\xd3\xe4\x93\x02K\"F/v1/{parent=projects/*/locations/*/studies/*}/trials:listOptimalTrials:\x01*\x1aM\xca\x41\x19\x61iplatform.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xd6\x01\n\x1e\x63om.google.cloud.aiplatform.v1B\x12VizierServiceProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')



_GETSTUDYREQUEST = DESCRIPTOR.message_types_by_name['GetStudyRequest']
_CREATESTUDYREQUEST = DESCRIPTOR.message_types_by_name['CreateStudyRequest']
_LISTSTUDIESREQUEST = DESCRIPTOR.message_types_by_name['ListStudiesRequest']
_LISTSTUDIESRESPONSE = DESCRIPTOR.message_types_by_name['ListStudiesResponse']
_DELETESTUDYREQUEST = DESCRIPTOR.message_types_by_name['DeleteStudyRequest']
_LOOKUPSTUDYREQUEST = DESCRIPTOR.message_types_by_name['LookupStudyRequest']
_SUGGESTTRIALSREQUEST = DESCRIPTOR.message_types_by_name['SuggestTrialsRequest']
_SUGGESTTRIALSRESPONSE = DESCRIPTOR.message_types_by_name['SuggestTrialsResponse']
_SUGGESTTRIALSMETADATA = DESCRIPTOR.message_types_by_name['SuggestTrialsMetadata']
_CREATETRIALREQUEST = DESCRIPTOR.message_types_by_name['CreateTrialRequest']
_GETTRIALREQUEST = DESCRIPTOR.message_types_by_name['GetTrialRequest']
_LISTTRIALSREQUEST = DESCRIPTOR.message_types_by_name['ListTrialsRequest']
_LISTTRIALSRESPONSE = DESCRIPTOR.message_types_by_name['ListTrialsResponse']
_ADDTRIALMEASUREMENTREQUEST = DESCRIPTOR.message_types_by_name['AddTrialMeasurementRequest']
_COMPLETETRIALREQUEST = DESCRIPTOR.message_types_by_name['CompleteTrialRequest']
_DELETETRIALREQUEST = DESCRIPTOR.message_types_by_name['DeleteTrialRequest']
_CHECKTRIALEARLYSTOPPINGSTATEREQUEST = DESCRIPTOR.message_types_by_name['CheckTrialEarlyStoppingStateRequest']
_CHECKTRIALEARLYSTOPPINGSTATERESPONSE = DESCRIPTOR.message_types_by_name['CheckTrialEarlyStoppingStateResponse']
_CHECKTRIALEARLYSTOPPINGSTATEMETATDATA = DESCRIPTOR.message_types_by_name['CheckTrialEarlyStoppingStateMetatdata']
_STOPTRIALREQUEST = DESCRIPTOR.message_types_by_name['StopTrialRequest']
_LISTOPTIMALTRIALSREQUEST = DESCRIPTOR.message_types_by_name['ListOptimalTrialsRequest']
_LISTOPTIMALTRIALSRESPONSE = DESCRIPTOR.message_types_by_name['ListOptimalTrialsResponse']
GetStudyRequest = _reflection.GeneratedProtocolMessageType('GetStudyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTUDYREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.GetStudyRequest)
  })
_sym_db.RegisterMessage(GetStudyRequest)

CreateStudyRequest = _reflection.GeneratedProtocolMessageType('CreateStudyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTUDYREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.CreateStudyRequest)
  })
_sym_db.RegisterMessage(CreateStudyRequest)

ListStudiesRequest = _reflection.GeneratedProtocolMessageType('ListStudiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSTUDIESREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ListStudiesRequest)
  })
_sym_db.RegisterMessage(ListStudiesRequest)

ListStudiesResponse = _reflection.GeneratedProtocolMessageType('ListStudiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSTUDIESRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ListStudiesResponse)
  })
_sym_db.RegisterMessage(ListStudiesResponse)

DeleteStudyRequest = _reflection.GeneratedProtocolMessageType('DeleteStudyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESTUDYREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.DeleteStudyRequest)
  })
_sym_db.RegisterMessage(DeleteStudyRequest)

LookupStudyRequest = _reflection.GeneratedProtocolMessageType('LookupStudyRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPSTUDYREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.LookupStudyRequest)
  })
_sym_db.RegisterMessage(LookupStudyRequest)

SuggestTrialsRequest = _reflection.GeneratedProtocolMessageType('SuggestTrialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTTRIALSREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.SuggestTrialsRequest)
  })
_sym_db.RegisterMessage(SuggestTrialsRequest)

SuggestTrialsResponse = _reflection.GeneratedProtocolMessageType('SuggestTrialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTTRIALSRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.SuggestTrialsResponse)
  })
_sym_db.RegisterMessage(SuggestTrialsResponse)

SuggestTrialsMetadata = _reflection.GeneratedProtocolMessageType('SuggestTrialsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTTRIALSMETADATA,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.SuggestTrialsMetadata)
  })
_sym_db.RegisterMessage(SuggestTrialsMetadata)

CreateTrialRequest = _reflection.GeneratedProtocolMessageType('CreateTrialRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETRIALREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.CreateTrialRequest)
  })
_sym_db.RegisterMessage(CreateTrialRequest)

GetTrialRequest = _reflection.GeneratedProtocolMessageType('GetTrialRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRIALREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.GetTrialRequest)
  })
_sym_db.RegisterMessage(GetTrialRequest)

ListTrialsRequest = _reflection.GeneratedProtocolMessageType('ListTrialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIALSREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ListTrialsRequest)
  })
_sym_db.RegisterMessage(ListTrialsRequest)

ListTrialsResponse = _reflection.GeneratedProtocolMessageType('ListTrialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIALSRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ListTrialsResponse)
  })
_sym_db.RegisterMessage(ListTrialsResponse)

AddTrialMeasurementRequest = _reflection.GeneratedProtocolMessageType('AddTrialMeasurementRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDTRIALMEASUREMENTREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.AddTrialMeasurementRequest)
  })
_sym_db.RegisterMessage(AddTrialMeasurementRequest)

CompleteTrialRequest = _reflection.GeneratedProtocolMessageType('CompleteTrialRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETETRIALREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.CompleteTrialRequest)
  })
_sym_db.RegisterMessage(CompleteTrialRequest)

DeleteTrialRequest = _reflection.GeneratedProtocolMessageType('DeleteTrialRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETRIALREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.DeleteTrialRequest)
  })
_sym_db.RegisterMessage(DeleteTrialRequest)

CheckTrialEarlyStoppingStateRequest = _reflection.GeneratedProtocolMessageType('CheckTrialEarlyStoppingStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKTRIALEARLYSTOPPINGSTATEREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateRequest)
  })
_sym_db.RegisterMessage(CheckTrialEarlyStoppingStateRequest)

CheckTrialEarlyStoppingStateResponse = _reflection.GeneratedProtocolMessageType('CheckTrialEarlyStoppingStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKTRIALEARLYSTOPPINGSTATERESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateResponse)
  })
_sym_db.RegisterMessage(CheckTrialEarlyStoppingStateResponse)

CheckTrialEarlyStoppingStateMetatdata = _reflection.GeneratedProtocolMessageType('CheckTrialEarlyStoppingStateMetatdata', (_message.Message,), {
  'DESCRIPTOR' : _CHECKTRIALEARLYSTOPPINGSTATEMETATDATA,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateMetatdata)
  })
_sym_db.RegisterMessage(CheckTrialEarlyStoppingStateMetatdata)

StopTrialRequest = _reflection.GeneratedProtocolMessageType('StopTrialRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPTRIALREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StopTrialRequest)
  })
_sym_db.RegisterMessage(StopTrialRequest)

ListOptimalTrialsRequest = _reflection.GeneratedProtocolMessageType('ListOptimalTrialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPTIMALTRIALSREQUEST,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ListOptimalTrialsRequest)
  })
_sym_db.RegisterMessage(ListOptimalTrialsRequest)

ListOptimalTrialsResponse = _reflection.GeneratedProtocolMessageType('ListOptimalTrialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPTIMALTRIALSRESPONSE,
  '__module__' : 'google.cloud.aiplatform.v1.vizier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ListOptimalTrialsResponse)
  })
_sym_db.RegisterMessage(ListOptimalTrialsResponse)

_VIZIERSERVICE = DESCRIPTOR.services_by_name['VizierService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.aiplatform.v1B\022VizierServiceProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\252\002\032Google.Cloud.AIPlatform.V1\312\002\032Google\\Cloud\\AIPlatform\\V1\352\002\035Google::Cloud::AIPlatform::V1'
  _GETSTUDYREQUEST.fields_by_name['name']._options = None
  _GETSTUDYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Study'
  _CREATESTUDYREQUEST.fields_by_name['parent']._options = None
  _CREATESTUDYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _CREATESTUDYREQUEST.fields_by_name['study']._options = None
  _CREATESTUDYREQUEST.fields_by_name['study']._serialized_options = b'\342A\001\002'
  _LISTSTUDIESREQUEST.fields_by_name['parent']._options = None
  _LISTSTUDIESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _LISTSTUDIESREQUEST.fields_by_name['page_token']._options = None
  _LISTSTUDIESREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTSTUDIESREQUEST.fields_by_name['page_size']._options = None
  _LISTSTUDIESREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _DELETESTUDYREQUEST.fields_by_name['name']._options = None
  _DELETESTUDYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Study'
  _LOOKUPSTUDYREQUEST.fields_by_name['parent']._options = None
  _LOOKUPSTUDYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _LOOKUPSTUDYREQUEST.fields_by_name['display_name']._options = None
  _LOOKUPSTUDYREQUEST.fields_by_name['display_name']._serialized_options = b'\342A\001\002'
  _SUGGESTTRIALSREQUEST.fields_by_name['parent']._options = None
  _SUGGESTTRIALSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Study'
  _SUGGESTTRIALSREQUEST.fields_by_name['suggestion_count']._options = None
  _SUGGESTTRIALSREQUEST.fields_by_name['suggestion_count']._serialized_options = b'\342A\001\002'
  _SUGGESTTRIALSREQUEST.fields_by_name['client_id']._options = None
  _SUGGESTTRIALSREQUEST.fields_by_name['client_id']._serialized_options = b'\342A\001\002'
  _CREATETRIALREQUEST.fields_by_name['parent']._options = None
  _CREATETRIALREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Study'
  _CREATETRIALREQUEST.fields_by_name['trial']._options = None
  _CREATETRIALREQUEST.fields_by_name['trial']._serialized_options = b'\342A\001\002'
  _GETTRIALREQUEST.fields_by_name['name']._options = None
  _GETTRIALREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Trial'
  _LISTTRIALSREQUEST.fields_by_name['parent']._options = None
  _LISTTRIALSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Study'
  _LISTTRIALSREQUEST.fields_by_name['page_token']._options = None
  _LISTTRIALSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTTRIALSREQUEST.fields_by_name['page_size']._options = None
  _LISTTRIALSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _ADDTRIALMEASUREMENTREQUEST.fields_by_name['trial_name']._options = None
  _ADDTRIALMEASUREMENTREQUEST.fields_by_name['trial_name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Trial'
  _ADDTRIALMEASUREMENTREQUEST.fields_by_name['measurement']._options = None
  _ADDTRIALMEASUREMENTREQUEST.fields_by_name['measurement']._serialized_options = b'\342A\001\002'
  _COMPLETETRIALREQUEST.fields_by_name['name']._options = None
  _COMPLETETRIALREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Trial'
  _COMPLETETRIALREQUEST.fields_by_name['final_measurement']._options = None
  _COMPLETETRIALREQUEST.fields_by_name['final_measurement']._serialized_options = b'\342A\001\001'
  _COMPLETETRIALREQUEST.fields_by_name['trial_infeasible']._options = None
  _COMPLETETRIALREQUEST.fields_by_name['trial_infeasible']._serialized_options = b'\342A\001\001'
  _COMPLETETRIALREQUEST.fields_by_name['infeasible_reason']._options = None
  _COMPLETETRIALREQUEST.fields_by_name['infeasible_reason']._serialized_options = b'\342A\001\001'
  _DELETETRIALREQUEST.fields_by_name['name']._options = None
  _DELETETRIALREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Trial'
  _CHECKTRIALEARLYSTOPPINGSTATEREQUEST.fields_by_name['trial_name']._options = None
  _CHECKTRIALEARLYSTOPPINGSTATEREQUEST.fields_by_name['trial_name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Trial'
  _STOPTRIALREQUEST.fields_by_name['name']._options = None
  _STOPTRIALREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Trial'
  _LISTOPTIMALTRIALSREQUEST.fields_by_name['parent']._options = None
  _LISTOPTIMALTRIALSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A!\n\037aiplatform.googleapis.com/Study'
  _VIZIERSERVICE._options = None
  _VIZIERSERVICE._serialized_options = b'\312A\031aiplatform.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _VIZIERSERVICE.methods_by_name['CreateStudy']._options = None
  _VIZIERSERVICE.methods_by_name['CreateStudy']._serialized_options = b'\332A\014parent,study\202\323\344\223\0024\"+/v1/{parent=projects/*/locations/*}/studies:\005study'
  _VIZIERSERVICE.methods_by_name['GetStudy']._options = None
  _VIZIERSERVICE.methods_by_name['GetStudy']._serialized_options = b'\332A\004name\202\323\344\223\002-\022+/v1/{name=projects/*/locations/*/studies/*}'
  _VIZIERSERVICE.methods_by_name['ListStudies']._options = None
  _VIZIERSERVICE.methods_by_name['ListStudies']._serialized_options = b'\332A\006parent\202\323\344\223\002-\022+/v1/{parent=projects/*/locations/*}/studies'
  _VIZIERSERVICE.methods_by_name['DeleteStudy']._options = None
  _VIZIERSERVICE.methods_by_name['DeleteStudy']._serialized_options = b'\332A\004name\202\323\344\223\002-*+/v1/{name=projects/*/locations/*/studies/*}'
  _VIZIERSERVICE.methods_by_name['LookupStudy']._options = None
  _VIZIERSERVICE.methods_by_name['LookupStudy']._serialized_options = b'\332A\006parent\202\323\344\223\0027\"2/v1/{parent=projects/*/locations/*}/studies:lookup:\001*'
  _VIZIERSERVICE.methods_by_name['SuggestTrials']._options = None
  _VIZIERSERVICE.methods_by_name['SuggestTrials']._serialized_options = b'\312A.\n\025SuggestTrialsResponse\022\025SuggestTrialsMetadata\202\323\344\223\002A\"</v1/{parent=projects/*/locations/*/studies/*}/trials:suggest:\001*'
  _VIZIERSERVICE.methods_by_name['CreateTrial']._options = None
  _VIZIERSERVICE.methods_by_name['CreateTrial']._serialized_options = b'\332A\014parent,trial\202\323\344\223\002=\"4/v1/{parent=projects/*/locations/*/studies/*}/trials:\005trial'
  _VIZIERSERVICE.methods_by_name['GetTrial']._options = None
  _VIZIERSERVICE.methods_by_name['GetTrial']._serialized_options = b'\332A\004name\202\323\344\223\0026\0224/v1/{name=projects/*/locations/*/studies/*/trials/*}'
  _VIZIERSERVICE.methods_by_name['ListTrials']._options = None
  _VIZIERSERVICE.methods_by_name['ListTrials']._serialized_options = b'\332A\006parent\202\323\344\223\0026\0224/v1/{parent=projects/*/locations/*/studies/*}/trials'
  _VIZIERSERVICE.methods_by_name['AddTrialMeasurement']._options = None
  _VIZIERSERVICE.methods_by_name['AddTrialMeasurement']._serialized_options = b'\202\323\344\223\002S\"N/v1/{trial_name=projects/*/locations/*/studies/*/trials/*}:addTrialMeasurement:\001*'
  _VIZIERSERVICE.methods_by_name['CompleteTrial']._options = None
  _VIZIERSERVICE.methods_by_name['CompleteTrial']._serialized_options = b'\202\323\344\223\002B\"=/v1/{name=projects/*/locations/*/studies/*/trials/*}:complete:\001*'
  _VIZIERSERVICE.methods_by_name['DeleteTrial']._options = None
  _VIZIERSERVICE.methods_by_name['DeleteTrial']._serialized_options = b'\332A\004name\202\323\344\223\0026*4/v1/{name=projects/*/locations/*/studies/*/trials/*}'
  _VIZIERSERVICE.methods_by_name['CheckTrialEarlyStoppingState']._options = None
  _VIZIERSERVICE.methods_by_name['CheckTrialEarlyStoppingState']._serialized_options = b'\312AM\n$CheckTrialEarlyStoppingStateResponse\022%CheckTrialEarlyStoppingStateMetatdata\202\323\344\223\002\\\"W/v1/{trial_name=projects/*/locations/*/studies/*/trials/*}:checkTrialEarlyStoppingState:\001*'
  _VIZIERSERVICE.methods_by_name['StopTrial']._options = None
  _VIZIERSERVICE.methods_by_name['StopTrial']._serialized_options = b'\202\323\344\223\002>\"9/v1/{name=projects/*/locations/*/studies/*/trials/*}:stop:\001*'
  _VIZIERSERVICE.methods_by_name['ListOptimalTrials']._options = None
  _VIZIERSERVICE.methods_by_name['ListOptimalTrials']._serialized_options = b'\332A\006parent\202\323\344\223\002K\"F/v1/{parent=projects/*/locations/*/studies/*}/trials:listOptimalTrials:\001*'
  _GETSTUDYREQUEST._serialized_start=377
  _GETSTUDYREQUEST._serialized_end=456
  _CREATESTUDYREQUEST._serialized_start=459
  _CREATESTUDYREQUEST._serialized_end=610
  _LISTSTUDIESREQUEST._serialized_start=613
  _LISTSTUDIESREQUEST._serialized_end=773
  _LISTSTUDIESRESPONSE._serialized_start=775
  _LISTSTUDIESRESPONSE._serialized_end=897
  _DELETESTUDYREQUEST._serialized_start=899
  _DELETESTUDYREQUEST._serialized_end=981
  _LOOKUPSTUDYREQUEST._serialized_start=984
  _LOOKUPSTUDYREQUEST._serialized_end=1113
  _SUGGESTTRIALSREQUEST._serialized_start=1116
  _SUGGESTTRIALSREQUEST._serialized_end=1288
  _SUGGESTTRIALSRESPONSE._serialized_start=1291
  _SUGGESTTRIALSRESPONSE._serialized_end=1561
  _SUGGESTTRIALSMETADATA._serialized_start=1564
  _SUGGESTTRIALSMETADATA._serialized_end=1713
  _CREATETRIALREQUEST._serialized_start=1716
  _CREATETRIALREQUEST._serialized_end=1865
  _GETTRIALREQUEST._serialized_start=1867
  _GETTRIALREQUEST._serialized_end=1946
  _LISTTRIALSREQUEST._serialized_start=1949
  _LISTTRIALSREQUEST._serialized_end=2106
  _LISTTRIALSRESPONSE._serialized_start=2108
  _LISTTRIALSRESPONSE._serialized_end=2227
  _ADDTRIALMEASUREMENTREQUEST._serialized_start=2230
  _ADDTRIALMEASUREMENTREQUEST._serialized_end=2412
  _COMPLETETRIALREQUEST._serialized_start=2415
  _COMPLETETRIALREQUEST._serialized_end=2691
  _DELETETRIALREQUEST._serialized_start=2693
  _DELETETRIALREQUEST._serialized_end=2775
  _CHECKTRIALEARLYSTOPPINGSTATEREQUEST._serialized_start=2777
  _CHECKTRIALEARLYSTOPPINGSTATEREQUEST._serialized_end=2887
  _CHECKTRIALEARLYSTOPPINGSTATERESPONSE._serialized_start=2889
  _CHECKTRIALEARLYSTOPPINGSTATERESPONSE._serialized_end=2960
  _CHECKTRIALEARLYSTOPPINGSTATEMETATDATA._serialized_start=2963
  _CHECKTRIALEARLYSTOPPINGSTATEMETATDATA._serialized_end=3143
  _STOPTRIALREQUEST._serialized_start=3145
  _STOPTRIALREQUEST._serialized_end=3225
  _LISTOPTIMALTRIALSREQUEST._serialized_start=3227
  _LISTOPTIMALTRIALSREQUEST._serialized_end=3319
  _LISTOPTIMALTRIALSRESPONSE._serialized_start=3321
  _LISTOPTIMALTRIALSRESPONSE._serialized_end=3422
  _VIZIERSERVICE._serialized_start=3425
  _VIZIERSERVICE._serialized_end=6325
# @@protoc_insertion_point(module_scope)
