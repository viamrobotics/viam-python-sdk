# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/gaming/v1/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/gaming/v1/common.proto\x12\x16google.cloud.gaming.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xe2\x04\n\x11OperationMetadata\x12\x41\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12;\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12\x1c\n\x06target\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x06target\x12\x18\n\x04verb\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\x04verb\x12+\n\x0estatus_message\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\rstatusMessage\x12;\n\x16requested_cancellation\x18\x06 \x01(\x08\x42\x04\xe2\x41\x01\x03R\x15requestedCancellation\x12%\n\x0b\x61pi_version\x18\x07 \x01(\tB\x04\xe2\x41\x01\x03R\napiVersion\x12&\n\x0bunreachable\x18\x08 \x03(\tB\x04\xe2\x41\x01\x03R\x0bunreachable\x12o\n\x10operation_status\x18\t \x03(\x0b\x32>.google.cloud.gaming.v1.OperationMetadata.OperationStatusEntryB\x04\xe2\x41\x01\x03R\x0foperationStatus\x1ak\n\x14OperationStatusEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12=\n\x05value\x18\x02 \x01(\x0b\x32\'.google.cloud.gaming.v1.OperationStatusR\x05value:\x02\x38\x01\"\x8e\x02\n\x0fOperationStatus\x12\x18\n\x04\x64one\x18\x01 \x01(\x08\x42\x04\xe2\x41\x01\x03R\x04\x64one\x12P\n\nerror_code\x18\x02 \x01(\x0e\x32\x31.google.cloud.gaming.v1.OperationStatus.ErrorCodeR\terrorCode\x12#\n\rerror_message\x18\x03 \x01(\tR\x0c\x65rrorMessage\"j\n\tErrorCode\x12\x1a\n\x16\x45RROR_CODE_UNSPECIFIED\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x15\n\x11PERMISSION_DENIED\x10\x02\x12\x16\n\x12\x43LUSTER_CONNECTION\x10\x03\"\x95\x01\n\rLabelSelector\x12I\n\x06labels\x18\x01 \x03(\x0b\x32\x31.google.cloud.gaming.v1.LabelSelector.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\'\n\rRealmSelector\x12\x16\n\x06realms\x18\x01 \x03(\tR\x06realms\"\xe0\x01\n\x08Schedule\x12\x39\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x45\n\x11\x63ron_job_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0f\x63ronJobDuration\x12\x1b\n\tcron_spec\x18\x04 \x01(\tR\x08\x63ronSpec\"W\n\nSpecSource\x12\x35\n\x17game_server_config_name\x18\x01 \x01(\tR\x14gameServerConfigName\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\xa3\x05\n\rTargetDetails\x12\x37\n\x18game_server_cluster_name\x18\x01 \x01(\tR\x15gameServerClusterName\x12=\n\x1bgame_server_deployment_name\x18\x02 \x01(\tR\x18gameServerDeploymentName\x12]\n\rfleet_details\x18\x03 \x03(\x0b\x32\x38.google.cloud.gaming.v1.TargetDetails.TargetFleetDetailsR\x0c\x66leetDetails\x1a\xba\x03\n\x12TargetFleetDetails\x12Z\n\x05\x66leet\x18\x01 \x01(\x0b\x32\x44.google.cloud.gaming.v1.TargetDetails.TargetFleetDetails.TargetFleetR\x05\x66leet\x12n\n\nautoscaler\x18\x02 \x01(\x0b\x32N.google.cloud.gaming.v1.TargetDetails.TargetFleetDetails.TargetFleetAutoscalerR\nautoscaler\x1a\x66\n\x0bTargetFleet\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x43\n\x0bspec_source\x18\x02 \x01(\x0b\x32\".google.cloud.gaming.v1.SpecSourceR\nspecSource\x1ap\n\x15TargetFleetAutoscaler\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x43\n\x0bspec_source\x18\x02 \x01(\x0b\x32\".google.cloud.gaming.v1.SpecSourceR\nspecSource\"N\n\x0bTargetState\x12?\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32%.google.cloud.gaming.v1.TargetDetailsR\x07\x64\x65tails\"\xd0\x06\n\x14\x44\x65ployedFleetDetails\x12\x61\n\x0e\x64\x65ployed_fleet\x18\x01 \x01(\x0b\x32:.google.cloud.gaming.v1.DeployedFleetDetails.DeployedFleetR\rdeployedFleet\x12u\n\x13\x64\x65ployed_autoscaler\x18\x02 \x01(\x0b\x32\x44.google.cloud.gaming.v1.DeployedFleetDetails.DeployedFleetAutoscalerR\x12\x64\x65ployedAutoscaler\x1a\xa8\x03\n\rDeployedFleet\x12\x14\n\x05\x66leet\x18\x01 \x01(\tR\x05\x66leet\x12\x1d\n\nfleet_spec\x18\x02 \x01(\tR\tfleetSpec\x12\x43\n\x0bspec_source\x18\x03 \x01(\x0b\x32\".google.cloud.gaming.v1.SpecSourceR\nspecSource\x12\x66\n\x06status\x18\x05 \x01(\x0b\x32N.google.cloud.gaming.v1.DeployedFleetDetails.DeployedFleet.DeployedFleetStatusR\x06status\x1a\xb4\x01\n\x13\x44\x65ployedFleetStatus\x12%\n\x0eready_replicas\x18\x01 \x01(\x03R\rreadyReplicas\x12-\n\x12\x61llocated_replicas\x18\x02 \x01(\x03R\x11\x61llocatedReplicas\x12+\n\x11reserved_replicas\x18\x03 \x01(\x03R\x10reservedReplicas\x12\x1a\n\x08replicas\x18\x04 \x01(\x03R\x08replicas\x1a\xb2\x01\n\x17\x44\x65ployedFleetAutoscaler\x12\x1e\n\nautoscaler\x18\x01 \x01(\tR\nautoscaler\x12\x43\n\x0bspec_source\x18\x04 \x01(\x0b\x32\".google.cloud.gaming.v1.SpecSourceR\nspecSource\x12\x32\n\x15\x66leet_autoscaler_spec\x18\x03 \x01(\tR\x13\x66leetAutoscalerSpecB\\\n\x1a\x63om.google.cloud.gaming.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/gaming/v1;gamingb\x06proto3')



_OPERATIONMETADATA = DESCRIPTOR.message_types_by_name['OperationMetadata']
_OPERATIONMETADATA_OPERATIONSTATUSENTRY = _OPERATIONMETADATA.nested_types_by_name['OperationStatusEntry']
_OPERATIONSTATUS = DESCRIPTOR.message_types_by_name['OperationStatus']
_LABELSELECTOR = DESCRIPTOR.message_types_by_name['LabelSelector']
_LABELSELECTOR_LABELSENTRY = _LABELSELECTOR.nested_types_by_name['LabelsEntry']
_REALMSELECTOR = DESCRIPTOR.message_types_by_name['RealmSelector']
_SCHEDULE = DESCRIPTOR.message_types_by_name['Schedule']
_SPECSOURCE = DESCRIPTOR.message_types_by_name['SpecSource']
_TARGETDETAILS = DESCRIPTOR.message_types_by_name['TargetDetails']
_TARGETDETAILS_TARGETFLEETDETAILS = _TARGETDETAILS.nested_types_by_name['TargetFleetDetails']
_TARGETDETAILS_TARGETFLEETDETAILS_TARGETFLEET = _TARGETDETAILS_TARGETFLEETDETAILS.nested_types_by_name['TargetFleet']
_TARGETDETAILS_TARGETFLEETDETAILS_TARGETFLEETAUTOSCALER = _TARGETDETAILS_TARGETFLEETDETAILS.nested_types_by_name['TargetFleetAutoscaler']
_TARGETSTATE = DESCRIPTOR.message_types_by_name['TargetState']
_DEPLOYEDFLEETDETAILS = DESCRIPTOR.message_types_by_name['DeployedFleetDetails']
_DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET = _DEPLOYEDFLEETDETAILS.nested_types_by_name['DeployedFleet']
_DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET_DEPLOYEDFLEETSTATUS = _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET.nested_types_by_name['DeployedFleetStatus']
_DEPLOYEDFLEETDETAILS_DEPLOYEDFLEETAUTOSCALER = _DEPLOYEDFLEETDETAILS.nested_types_by_name['DeployedFleetAutoscaler']
_OPERATIONSTATUS_ERRORCODE = _OPERATIONSTATUS.enum_types_by_name['ErrorCode']
OperationMetadata = _reflection.GeneratedProtocolMessageType('OperationMetadata', (_message.Message,), {

  'OperationStatusEntry' : _reflection.GeneratedProtocolMessageType('OperationStatusEntry', (_message.Message,), {
    'DESCRIPTOR' : _OPERATIONMETADATA_OPERATIONSTATUSENTRY,
    '__module__' : 'google.cloud.gaming.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.OperationMetadata.OperationStatusEntry)
    })
  ,
  'DESCRIPTOR' : _OPERATIONMETADATA,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.OperationMetadata)
  })
_sym_db.RegisterMessage(OperationMetadata)
_sym_db.RegisterMessage(OperationMetadata.OperationStatusEntry)

OperationStatus = _reflection.GeneratedProtocolMessageType('OperationStatus', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONSTATUS,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.OperationStatus)
  })
_sym_db.RegisterMessage(OperationStatus)

LabelSelector = _reflection.GeneratedProtocolMessageType('LabelSelector', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LABELSELECTOR_LABELSENTRY,
    '__module__' : 'google.cloud.gaming.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.LabelSelector.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LABELSELECTOR,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.LabelSelector)
  })
_sym_db.RegisterMessage(LabelSelector)
_sym_db.RegisterMessage(LabelSelector.LabelsEntry)

RealmSelector = _reflection.GeneratedProtocolMessageType('RealmSelector', (_message.Message,), {
  'DESCRIPTOR' : _REALMSELECTOR,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.RealmSelector)
  })
_sym_db.RegisterMessage(RealmSelector)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULE,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.Schedule)
  })
_sym_db.RegisterMessage(Schedule)

SpecSource = _reflection.GeneratedProtocolMessageType('SpecSource', (_message.Message,), {
  'DESCRIPTOR' : _SPECSOURCE,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.SpecSource)
  })
_sym_db.RegisterMessage(SpecSource)

TargetDetails = _reflection.GeneratedProtocolMessageType('TargetDetails', (_message.Message,), {

  'TargetFleetDetails' : _reflection.GeneratedProtocolMessageType('TargetFleetDetails', (_message.Message,), {

    'TargetFleet' : _reflection.GeneratedProtocolMessageType('TargetFleet', (_message.Message,), {
      'DESCRIPTOR' : _TARGETDETAILS_TARGETFLEETDETAILS_TARGETFLEET,
      '__module__' : 'google.cloud.gaming.v1.common_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.TargetDetails.TargetFleetDetails.TargetFleet)
      })
    ,

    'TargetFleetAutoscaler' : _reflection.GeneratedProtocolMessageType('TargetFleetAutoscaler', (_message.Message,), {
      'DESCRIPTOR' : _TARGETDETAILS_TARGETFLEETDETAILS_TARGETFLEETAUTOSCALER,
      '__module__' : 'google.cloud.gaming.v1.common_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.TargetDetails.TargetFleetDetails.TargetFleetAutoscaler)
      })
    ,
    'DESCRIPTOR' : _TARGETDETAILS_TARGETFLEETDETAILS,
    '__module__' : 'google.cloud.gaming.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.TargetDetails.TargetFleetDetails)
    })
  ,
  'DESCRIPTOR' : _TARGETDETAILS,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.TargetDetails)
  })
_sym_db.RegisterMessage(TargetDetails)
_sym_db.RegisterMessage(TargetDetails.TargetFleetDetails)
_sym_db.RegisterMessage(TargetDetails.TargetFleetDetails.TargetFleet)
_sym_db.RegisterMessage(TargetDetails.TargetFleetDetails.TargetFleetAutoscaler)

TargetState = _reflection.GeneratedProtocolMessageType('TargetState', (_message.Message,), {
  'DESCRIPTOR' : _TARGETSTATE,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.TargetState)
  })
_sym_db.RegisterMessage(TargetState)

DeployedFleetDetails = _reflection.GeneratedProtocolMessageType('DeployedFleetDetails', (_message.Message,), {

  'DeployedFleet' : _reflection.GeneratedProtocolMessageType('DeployedFleet', (_message.Message,), {

    'DeployedFleetStatus' : _reflection.GeneratedProtocolMessageType('DeployedFleetStatus', (_message.Message,), {
      'DESCRIPTOR' : _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET_DEPLOYEDFLEETSTATUS,
      '__module__' : 'google.cloud.gaming.v1.common_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.DeployedFleetDetails.DeployedFleet.DeployedFleetStatus)
      })
    ,
    'DESCRIPTOR' : _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET,
    '__module__' : 'google.cloud.gaming.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.DeployedFleetDetails.DeployedFleet)
    })
  ,

  'DeployedFleetAutoscaler' : _reflection.GeneratedProtocolMessageType('DeployedFleetAutoscaler', (_message.Message,), {
    'DESCRIPTOR' : _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEETAUTOSCALER,
    '__module__' : 'google.cloud.gaming.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.DeployedFleetDetails.DeployedFleetAutoscaler)
    })
  ,
  'DESCRIPTOR' : _DEPLOYEDFLEETDETAILS,
  '__module__' : 'google.cloud.gaming.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.DeployedFleetDetails)
  })
_sym_db.RegisterMessage(DeployedFleetDetails)
_sym_db.RegisterMessage(DeployedFleetDetails.DeployedFleet)
_sym_db.RegisterMessage(DeployedFleetDetails.DeployedFleet.DeployedFleetStatus)
_sym_db.RegisterMessage(DeployedFleetDetails.DeployedFleetAutoscaler)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.google.cloud.gaming.v1P\001Z<google.golang.org/genproto/googleapis/cloud/gaming/v1;gaming'
  _OPERATIONMETADATA_OPERATIONSTATUSENTRY._options = None
  _OPERATIONMETADATA_OPERATIONSTATUSENTRY._serialized_options = b'8\001'
  _OPERATIONMETADATA.fields_by_name['create_time']._options = None
  _OPERATIONMETADATA.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _OPERATIONMETADATA.fields_by_name['end_time']._options = None
  _OPERATIONMETADATA.fields_by_name['end_time']._serialized_options = b'\342A\001\003'
  _OPERATIONMETADATA.fields_by_name['target']._options = None
  _OPERATIONMETADATA.fields_by_name['target']._serialized_options = b'\342A\001\003'
  _OPERATIONMETADATA.fields_by_name['verb']._options = None
  _OPERATIONMETADATA.fields_by_name['verb']._serialized_options = b'\342A\001\003'
  _OPERATIONMETADATA.fields_by_name['status_message']._options = None
  _OPERATIONMETADATA.fields_by_name['status_message']._serialized_options = b'\342A\001\003'
  _OPERATIONMETADATA.fields_by_name['requested_cancellation']._options = None
  _OPERATIONMETADATA.fields_by_name['requested_cancellation']._serialized_options = b'\342A\001\003'
  _OPERATIONMETADATA.fields_by_name['api_version']._options = None
  _OPERATIONMETADATA.fields_by_name['api_version']._serialized_options = b'\342A\001\003'
  _OPERATIONMETADATA.fields_by_name['unreachable']._options = None
  _OPERATIONMETADATA.fields_by_name['unreachable']._serialized_options = b'\342A\001\003'
  _OPERATIONMETADATA.fields_by_name['operation_status']._options = None
  _OPERATIONMETADATA.fields_by_name['operation_status']._serialized_options = b'\342A\001\003'
  _OPERATIONSTATUS.fields_by_name['done']._options = None
  _OPERATIONSTATUS.fields_by_name['done']._serialized_options = b'\342A\001\003'
  _LABELSELECTOR_LABELSENTRY._options = None
  _LABELSELECTOR_LABELSENTRY._serialized_options = b'8\001'
  _OPERATIONMETADATA._serialized_start=192
  _OPERATIONMETADATA._serialized_end=802
  _OPERATIONMETADATA_OPERATIONSTATUSENTRY._serialized_start=695
  _OPERATIONMETADATA_OPERATIONSTATUSENTRY._serialized_end=802
  _OPERATIONSTATUS._serialized_start=805
  _OPERATIONSTATUS._serialized_end=1075
  _OPERATIONSTATUS_ERRORCODE._serialized_start=969
  _OPERATIONSTATUS_ERRORCODE._serialized_end=1075
  _LABELSELECTOR._serialized_start=1078
  _LABELSELECTOR._serialized_end=1227
  _LABELSELECTOR_LABELSENTRY._serialized_start=1170
  _LABELSELECTOR_LABELSENTRY._serialized_end=1227
  _REALMSELECTOR._serialized_start=1229
  _REALMSELECTOR._serialized_end=1268
  _SCHEDULE._serialized_start=1271
  _SCHEDULE._serialized_end=1495
  _SPECSOURCE._serialized_start=1497
  _SPECSOURCE._serialized_end=1584
  _TARGETDETAILS._serialized_start=1587
  _TARGETDETAILS._serialized_end=2262
  _TARGETDETAILS_TARGETFLEETDETAILS._serialized_start=1820
  _TARGETDETAILS_TARGETFLEETDETAILS._serialized_end=2262
  _TARGETDETAILS_TARGETFLEETDETAILS_TARGETFLEET._serialized_start=2046
  _TARGETDETAILS_TARGETFLEETDETAILS_TARGETFLEET._serialized_end=2148
  _TARGETDETAILS_TARGETFLEETDETAILS_TARGETFLEETAUTOSCALER._serialized_start=2150
  _TARGETDETAILS_TARGETFLEETDETAILS_TARGETFLEETAUTOSCALER._serialized_end=2262
  _TARGETSTATE._serialized_start=2264
  _TARGETSTATE._serialized_end=2342
  _DEPLOYEDFLEETDETAILS._serialized_start=2345
  _DEPLOYEDFLEETDETAILS._serialized_end=3193
  _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET._serialized_start=2588
  _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET._serialized_end=3012
  _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET_DEPLOYEDFLEETSTATUS._serialized_start=2832
  _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEET_DEPLOYEDFLEETSTATUS._serialized_end=3012
  _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEETAUTOSCALER._serialized_start=3015
  _DEPLOYEDFLEETDETAILS_DEPLOYEDFLEETAUTOSCALER._serialized_end=3193
# @@protoc_insertion_point(module_scope)
