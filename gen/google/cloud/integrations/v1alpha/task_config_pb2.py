# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/integrations/v1alpha/task_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.integrations.v1alpha import event_parameter_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_event__parameter__pb2
from google.cloud.integrations.v1alpha import json_validation_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_json__validation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/integrations/v1alpha/task_config.proto\x12!google.cloud.integrations.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x37google/cloud/integrations/v1alpha/event_parameter.proto\x1a\x37google/cloud/integrations/v1alpha/json_validation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe6\n\n\nTaskConfig\x12\x18\n\x04task\x18\x01 \x01(\tB\x04\xe2\x41\x01\x01R\x04task\x12\x1d\n\x07task_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x06taskId\x12\x63\n\nparameters\x18\x03 \x03(\x0b\x32=.google.cloud.integrations.v1alpha.TaskConfig.ParametersEntryB\x04\xe2\x41\x01\x01R\nparameters\x12]\n\x0e\x66\x61ilure_policy\x18\x04 \x01(\x0b\x32\x30.google.cloud.integrations.v1alpha.FailurePolicyB\x04\xe2\x41\x01\x01R\rfailurePolicy\x12}\n\x1fsynchronous_call_failure_policy\x18\x05 \x01(\x0b\x32\x30.google.cloud.integrations.v1alpha.FailurePolicyB\x04\xe2\x41\x01\x01R\x1csynchronousCallFailurePolicy\x12P\n\nnext_tasks\x18\x06 \x03(\x0b\x32+.google.cloud.integrations.v1alpha.NextTaskB\x04\xe2\x41\x01\x01R\tnextTasks\x12\x8b\x01\n\x1bnext_tasks_execution_policy\x18\x07 \x01(\x0e\x32\x46.google.cloud.integrations.v1alpha.TaskConfig.NextTasksExecutionPolicyB\x04\xe2\x41\x01\x01R\x18nextTasksExecutionPolicy\x12\x81\x01\n\x17task_execution_strategy\x18\x08 \x01(\x0e\x32\x43.google.cloud.integrations.v1alpha.TaskConfig.TaskExecutionStrategyB\x04\xe2\x41\x01\x01R\x15taskExecutionStrategy\x12\'\n\x0c\x64isplay_name\x18\t \x01(\tB\x04\xe2\x41\x01\x01R\x0b\x64isplayName\x12]\n\x0esuccess_policy\x18\n \x01(\x0b\x32\x30.google.cloud.integrations.v1alpha.SuccessPolicyB\x04\xe2\x41\x01\x01R\rsuccessPolicy\x12s\n\x16json_validation_option\x18\x0b \x01(\x0e\x32\x37.google.cloud.integrations.v1alpha.JsonValidationOptionB\x04\xe2\x41\x01\x01R\x14jsonValidationOption\x1ap\n\x0fParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.google.cloud.integrations.v1alpha.EventParameterR\x05value:\x02\x38\x01\"o\n\x18NextTasksExecutionPolicy\x12+\n\'NEXT_TASKS_EXECUTION_POLICY_UNSPECIFIED\x10\x00\x12\x11\n\rRUN_ALL_MATCH\x10\x01\x12\x13\n\x0fRUN_FIRST_MATCH\x10\x02\"\x97\x01\n\x15TaskExecutionStrategy\x12\'\n#TASK_EXECUTION_STRATEGY_UNSPECIFIED\x10\x00\x12\x14\n\x10WHEN_ALL_SUCCEED\x10\x01\x12\x14\n\x10WHEN_ANY_SUCCEED\x10\x02\x12)\n%WHEN_ALL_TASKS_AND_CONDITIONS_SUCCEED\x10\x03\"\xb6\x01\n\rSuccessPolicy\x12\\\n\x0b\x66inal_state\x18\x01 \x01(\x0e\x32;.google.cloud.integrations.v1alpha.SuccessPolicy.FinalStateR\nfinalState\"G\n\nFinalState\x12\x1b\n\x17\x46INAL_STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\r\n\tSUSPENDED\x10\x02\"\x92\x03\n\rFailurePolicy\x12\x65\n\x0eretry_strategy\x18\x01 \x01(\x0e\x32>.google.cloud.integrations.v1alpha.FailurePolicy.RetryStrategyR\rretryStrategy\x12\x1f\n\x0bmax_retries\x18\x02 \x01(\x05R\nmaxRetries\x12?\n\rinterval_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cintervalTime\"\xb7\x01\n\rRetryStrategy\x12\x1e\n\x1aRETRY_STRATEGY_UNSPECIFIED\x10\x00\x12\n\n\x06IGNORE\x10\x01\x12\x08\n\x04NONE\x10\x02\x12\t\n\x05\x46\x41TAL\x10\x03\x12\x12\n\x0e\x46IXED_INTERVAL\x10\x04\x12\x12\n\x0eLINEAR_BACKOFF\x10\x05\x12\x17\n\x13\x45XPONENTIAL_BACKOFF\x10\x06\x12$\n RESTART_INTEGRATION_WITH_BACKOFF\x10\x07\"\x8a\x01\n\x08NextTask\x12$\n\x0etask_config_id\x18\x01 \x01(\tR\x0ctaskConfigId\x12\x17\n\x07task_id\x18\x02 \x01(\tR\x06taskId\x12\x1c\n\tcondition\x18\x03 \x01(\tR\tcondition\x12!\n\x0c\x64isplay_name\x18\x04 \x01(\tR\x0b\x64isplayNameB\x89\x01\n%com.google.cloud.integrations.v1alphaB\x0fTaskConfigProtoP\x01ZMgoogle.golang.org/genproto/googleapis/cloud/integrations/v1alpha;integrationsb\x06proto3')



_TASKCONFIG = DESCRIPTOR.message_types_by_name['TaskConfig']
_TASKCONFIG_PARAMETERSENTRY = _TASKCONFIG.nested_types_by_name['ParametersEntry']
_SUCCESSPOLICY = DESCRIPTOR.message_types_by_name['SuccessPolicy']
_FAILUREPOLICY = DESCRIPTOR.message_types_by_name['FailurePolicy']
_NEXTTASK = DESCRIPTOR.message_types_by_name['NextTask']
_TASKCONFIG_NEXTTASKSEXECUTIONPOLICY = _TASKCONFIG.enum_types_by_name['NextTasksExecutionPolicy']
_TASKCONFIG_TASKEXECUTIONSTRATEGY = _TASKCONFIG.enum_types_by_name['TaskExecutionStrategy']
_SUCCESSPOLICY_FINALSTATE = _SUCCESSPOLICY.enum_types_by_name['FinalState']
_FAILUREPOLICY_RETRYSTRATEGY = _FAILUREPOLICY.enum_types_by_name['RetryStrategy']
TaskConfig = _reflection.GeneratedProtocolMessageType('TaskConfig', (_message.Message,), {

  'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
    'DESCRIPTOR' : _TASKCONFIG_PARAMETERSENTRY,
    '__module__' : 'google.cloud.integrations.v1alpha.task_config_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.TaskConfig.ParametersEntry)
    })
  ,
  'DESCRIPTOR' : _TASKCONFIG,
  '__module__' : 'google.cloud.integrations.v1alpha.task_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.TaskConfig)
  })
_sym_db.RegisterMessage(TaskConfig)
_sym_db.RegisterMessage(TaskConfig.ParametersEntry)

SuccessPolicy = _reflection.GeneratedProtocolMessageType('SuccessPolicy', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESSPOLICY,
  '__module__' : 'google.cloud.integrations.v1alpha.task_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.SuccessPolicy)
  })
_sym_db.RegisterMessage(SuccessPolicy)

FailurePolicy = _reflection.GeneratedProtocolMessageType('FailurePolicy', (_message.Message,), {
  'DESCRIPTOR' : _FAILUREPOLICY,
  '__module__' : 'google.cloud.integrations.v1alpha.task_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.FailurePolicy)
  })
_sym_db.RegisterMessage(FailurePolicy)

NextTask = _reflection.GeneratedProtocolMessageType('NextTask', (_message.Message,), {
  'DESCRIPTOR' : _NEXTTASK,
  '__module__' : 'google.cloud.integrations.v1alpha.task_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.NextTask)
  })
_sym_db.RegisterMessage(NextTask)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.cloud.integrations.v1alphaB\017TaskConfigProtoP\001ZMgoogle.golang.org/genproto/googleapis/cloud/integrations/v1alpha;integrations'
  _TASKCONFIG_PARAMETERSENTRY._options = None
  _TASKCONFIG_PARAMETERSENTRY._serialized_options = b'8\001'
  _TASKCONFIG.fields_by_name['task']._options = None
  _TASKCONFIG.fields_by_name['task']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['task_id']._options = None
  _TASKCONFIG.fields_by_name['task_id']._serialized_options = b'\342A\001\002'
  _TASKCONFIG.fields_by_name['parameters']._options = None
  _TASKCONFIG.fields_by_name['parameters']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['failure_policy']._options = None
  _TASKCONFIG.fields_by_name['failure_policy']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['synchronous_call_failure_policy']._options = None
  _TASKCONFIG.fields_by_name['synchronous_call_failure_policy']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['next_tasks']._options = None
  _TASKCONFIG.fields_by_name['next_tasks']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['next_tasks_execution_policy']._options = None
  _TASKCONFIG.fields_by_name['next_tasks_execution_policy']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['task_execution_strategy']._options = None
  _TASKCONFIG.fields_by_name['task_execution_strategy']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['display_name']._options = None
  _TASKCONFIG.fields_by_name['display_name']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['success_policy']._options = None
  _TASKCONFIG.fields_by_name['success_policy']._serialized_options = b'\342A\001\001'
  _TASKCONFIG.fields_by_name['json_validation_option']._options = None
  _TASKCONFIG.fields_by_name['json_validation_option']._serialized_options = b'\342A\001\001'
  _TASKCONFIG._serialized_start=271
  _TASKCONFIG._serialized_end=1653
  _TASKCONFIG_PARAMETERSENTRY._serialized_start=1274
  _TASKCONFIG_PARAMETERSENTRY._serialized_end=1386
  _TASKCONFIG_NEXTTASKSEXECUTIONPOLICY._serialized_start=1388
  _TASKCONFIG_NEXTTASKSEXECUTIONPOLICY._serialized_end=1499
  _TASKCONFIG_TASKEXECUTIONSTRATEGY._serialized_start=1502
  _TASKCONFIG_TASKEXECUTIONSTRATEGY._serialized_end=1653
  _SUCCESSPOLICY._serialized_start=1656
  _SUCCESSPOLICY._serialized_end=1838
  _SUCCESSPOLICY_FINALSTATE._serialized_start=1767
  _SUCCESSPOLICY_FINALSTATE._serialized_end=1838
  _FAILUREPOLICY._serialized_start=1841
  _FAILUREPOLICY._serialized_end=2243
  _FAILUREPOLICY_RETRYSTRATEGY._serialized_start=2060
  _FAILUREPOLICY_RETRYSTRATEGY._serialized_end=2243
  _NEXTTASK._serialized_start=2246
  _NEXTTASK._serialized_end=2384
# @@protoc_insertion_point(module_scope)
