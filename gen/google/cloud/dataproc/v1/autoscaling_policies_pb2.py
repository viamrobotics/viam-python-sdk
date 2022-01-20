# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dataproc/v1/autoscaling_policies.proto
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
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/dataproc/v1/autoscaling_policies.proto\x12\x18google.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xfd\x05\n\x11\x41utoscalingPolicy\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x04name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x64\n\x0f\x62\x61sic_algorithm\x18\x03 \x01(\x0b\x32\x33.google.cloud.dataproc.v1.BasicAutoscalingAlgorithmB\x04\xe2\x41\x01\x02H\x00R\x0e\x62\x61sicAlgorithm\x12i\n\rworker_config\x18\x04 \x01(\x0b\x32>.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfigB\x04\xe2\x41\x01\x02R\x0cworkerConfig\x12|\n\x17secondary_worker_config\x18\x05 \x01(\x0b\x32>.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfigB\x04\xe2\x41\x01\x01R\x15secondaryWorkerConfig\x12U\n\x06labels\x18\x06 \x03(\x0b\x32\x37.google.cloud.dataproc.v1.AutoscalingPolicy.LabelsEntryB\x04\xe2\x41\x01\x01R\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:\xcf\x01\xea\x41\xcb\x01\n)dataproc.googleapis.com/AutoscalingPolicy\x12Pprojects/{project}/locations/{location}/autoscalingPolicies/{autoscaling_policy}\x12Lprojects/{project}/regions/{region}/autoscalingPolicies/{autoscaling_policy}B\x0b\n\talgorithm\"\xc2\x01\n\x19\x42\x61sicAutoscalingAlgorithm\x12[\n\x0byarn_config\x18\x01 \x01(\x0b\x32\x34.google.cloud.dataproc.v1.BasicYarnAutoscalingConfigB\x04\xe2\x41\x01\x02R\nyarnConfig\x12H\n\x0f\x63ooldown_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe2\x41\x01\x01R\x0e\x63ooldownPeriod\"\xf1\x02\n\x1a\x42\x61sicYarnAutoscalingConfig\x12\x63\n\x1dgraceful_decommission_timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe2\x41\x01\x02R\x1bgracefulDecommissionTimeout\x12,\n\x0fscale_up_factor\x18\x01 \x01(\x01\x42\x04\xe2\x41\x01\x02R\rscaleUpFactor\x12\x30\n\x11scale_down_factor\x18\x02 \x01(\x01\x42\x04\xe2\x41\x01\x02R\x0fscaleDownFactor\x12\x44\n\x1cscale_up_min_worker_fraction\x18\x03 \x01(\x01\x42\x04\xe2\x41\x01\x01R\x18scaleUpMinWorkerFraction\x12H\n\x1escale_down_min_worker_fraction\x18\x04 \x01(\x01\x42\x04\xe2\x41\x01\x01R\x1ascaleDownMinWorkerFraction\"\x9a\x01\n$InstanceGroupAutoscalingPolicyConfig\x12)\n\rmin_instances\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x0cminInstances\x12)\n\rmax_instances\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x02R\x0cmaxInstances\x12\x1c\n\x06weight\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x06weight\"\xb7\x01\n\x1e\x43reateAutoscalingPolicyRequest\x12J\n\x06parent\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\x12)dataproc.googleapis.com/AutoscalingPolicyR\x06parent\x12I\n\x06policy\x18\x02 \x01(\x0b\x32+.google.cloud.dataproc.v1.AutoscalingPolicyB\x04\xe2\x41\x01\x02R\x06policy\"e\n\x1bGetAutoscalingPolicyRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)dataproc.googleapis.com/AutoscalingPolicyR\x04name\"k\n\x1eUpdateAutoscalingPolicyRequest\x12I\n\x06policy\x18\x01 \x01(\x0b\x32+.google.cloud.dataproc.v1.AutoscalingPolicyB\x04\xe2\x41\x01\x02R\x06policy\"h\n\x1e\x44\x65leteAutoscalingPolicyRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)dataproc.googleapis.com/AutoscalingPolicyR\x04name\"\xb4\x01\n\x1eListAutoscalingPoliciesRequest\x12J\n\x06parent\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\x12)dataproc.googleapis.com/AutoscalingPolicyR\x06parent\x12!\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\"\x9e\x01\n\x1fListAutoscalingPoliciesResponse\x12M\n\x08policies\x18\x01 \x03(\x0b\x32+.google.cloud.dataproc.v1.AutoscalingPolicyB\x04\xe2\x41\x01\x03R\x08policies\x12,\n\x0fnext_page_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\rnextPageToken2\xae\x0b\n\x18\x41utoscalingPolicyService\x12\x9c\x02\n\x17\x43reateAutoscalingPolicy\x12\x38.google.cloud.dataproc.v1.CreateAutoscalingPolicyRequest\x1a+.google.cloud.dataproc.v1.AutoscalingPolicy\"\x99\x01\xda\x41\rparent,policy\x82\xd3\xe4\x93\x02\x82\x01\"7/v1/{parent=projects/*/locations/*}/autoscalingPolicies:\x06policyZ?\"5/v1/{parent=projects/*/regions/*}/autoscalingPolicies:\x06policy\x12\xa3\x02\n\x17UpdateAutoscalingPolicy\x12\x38.google.cloud.dataproc.v1.UpdateAutoscalingPolicyRequest\x1a+.google.cloud.dataproc.v1.AutoscalingPolicy\"\xa0\x01\xda\x41\x06policy\x82\xd3\xe4\x93\x02\x90\x01\x1a>/v1/{policy.name=projects/*/locations/*/autoscalingPolicies/*}:\x06policyZF\x1a</v1/{policy.name=projects/*/regions/*/autoscalingPolicies/*}:\x06policy\x12\xfb\x01\n\x14GetAutoscalingPolicy\x12\x35.google.cloud.dataproc.v1.GetAutoscalingPolicyRequest\x1a+.google.cloud.dataproc.v1.AutoscalingPolicy\"\x7f\xda\x41\x04name\x82\xd3\xe4\x93\x02r\x12\x37/v1/{name=projects/*/locations/*/autoscalingPolicies/*}Z7\x12\x35/v1/{name=projects/*/regions/*/autoscalingPolicies/*}\x12\x92\x02\n\x17ListAutoscalingPolicies\x12\x38.google.cloud.dataproc.v1.ListAutoscalingPoliciesRequest\x1a\x39.google.cloud.dataproc.v1.ListAutoscalingPoliciesResponse\"\x81\x01\xda\x41\x06parent\x82\xd3\xe4\x93\x02r\x12\x37/v1/{parent=projects/*/locations/*}/autoscalingPoliciesZ7\x12\x35/v1/{parent=projects/*/regions/*}/autoscalingPolicies\x12\xec\x01\n\x17\x44\x65leteAutoscalingPolicy\x12\x38.google.cloud.dataproc.v1.DeleteAutoscalingPolicyRequest\x1a\x16.google.protobuf.Empty\"\x7f\xda\x41\x04name\x82\xd3\xe4\x93\x02r*7/v1/{name=projects/*/locations/*/autoscalingPolicies/*}Z7*5/v1/{name=projects/*/regions/*/autoscalingPolicies/*}\x1aK\xca\x41\x17\x64\x61taproc.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xc4\x01\n\x1c\x63om.google.cloud.dataproc.v1B\x18\x41utoscalingPoliciesProtoP\x01Z@google.golang.org/genproto/googleapis/cloud/dataproc/v1;dataproc\xea\x41\x45\n\x1e\x64\x61taproc.googleapis.com/Region\x12#projects/{project}/regions/{region}b\x06proto3')



_AUTOSCALINGPOLICY = DESCRIPTOR.message_types_by_name['AutoscalingPolicy']
_AUTOSCALINGPOLICY_LABELSENTRY = _AUTOSCALINGPOLICY.nested_types_by_name['LabelsEntry']
_BASICAUTOSCALINGALGORITHM = DESCRIPTOR.message_types_by_name['BasicAutoscalingAlgorithm']
_BASICYARNAUTOSCALINGCONFIG = DESCRIPTOR.message_types_by_name['BasicYarnAutoscalingConfig']
_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG = DESCRIPTOR.message_types_by_name['InstanceGroupAutoscalingPolicyConfig']
_CREATEAUTOSCALINGPOLICYREQUEST = DESCRIPTOR.message_types_by_name['CreateAutoscalingPolicyRequest']
_GETAUTOSCALINGPOLICYREQUEST = DESCRIPTOR.message_types_by_name['GetAutoscalingPolicyRequest']
_UPDATEAUTOSCALINGPOLICYREQUEST = DESCRIPTOR.message_types_by_name['UpdateAutoscalingPolicyRequest']
_DELETEAUTOSCALINGPOLICYREQUEST = DESCRIPTOR.message_types_by_name['DeleteAutoscalingPolicyRequest']
_LISTAUTOSCALINGPOLICIESREQUEST = DESCRIPTOR.message_types_by_name['ListAutoscalingPoliciesRequest']
_LISTAUTOSCALINGPOLICIESRESPONSE = DESCRIPTOR.message_types_by_name['ListAutoscalingPoliciesResponse']
AutoscalingPolicy = _reflection.GeneratedProtocolMessageType('AutoscalingPolicy', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _AUTOSCALINGPOLICY_LABELSENTRY,
    '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.AutoscalingPolicy.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _AUTOSCALINGPOLICY,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.AutoscalingPolicy)
  })
_sym_db.RegisterMessage(AutoscalingPolicy)
_sym_db.RegisterMessage(AutoscalingPolicy.LabelsEntry)

BasicAutoscalingAlgorithm = _reflection.GeneratedProtocolMessageType('BasicAutoscalingAlgorithm', (_message.Message,), {
  'DESCRIPTOR' : _BASICAUTOSCALINGALGORITHM,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.BasicAutoscalingAlgorithm)
  })
_sym_db.RegisterMessage(BasicAutoscalingAlgorithm)

BasicYarnAutoscalingConfig = _reflection.GeneratedProtocolMessageType('BasicYarnAutoscalingConfig', (_message.Message,), {
  'DESCRIPTOR' : _BASICYARNAUTOSCALINGCONFIG,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.BasicYarnAutoscalingConfig)
  })
_sym_db.RegisterMessage(BasicYarnAutoscalingConfig)

InstanceGroupAutoscalingPolicyConfig = _reflection.GeneratedProtocolMessageType('InstanceGroupAutoscalingPolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig)
  })
_sym_db.RegisterMessage(InstanceGroupAutoscalingPolicyConfig)

CreateAutoscalingPolicyRequest = _reflection.GeneratedProtocolMessageType('CreateAutoscalingPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAUTOSCALINGPOLICYREQUEST,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.CreateAutoscalingPolicyRequest)
  })
_sym_db.RegisterMessage(CreateAutoscalingPolicyRequest)

GetAutoscalingPolicyRequest = _reflection.GeneratedProtocolMessageType('GetAutoscalingPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUTOSCALINGPOLICYREQUEST,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.GetAutoscalingPolicyRequest)
  })
_sym_db.RegisterMessage(GetAutoscalingPolicyRequest)

UpdateAutoscalingPolicyRequest = _reflection.GeneratedProtocolMessageType('UpdateAutoscalingPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAUTOSCALINGPOLICYREQUEST,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.UpdateAutoscalingPolicyRequest)
  })
_sym_db.RegisterMessage(UpdateAutoscalingPolicyRequest)

DeleteAutoscalingPolicyRequest = _reflection.GeneratedProtocolMessageType('DeleteAutoscalingPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAUTOSCALINGPOLICYREQUEST,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.DeleteAutoscalingPolicyRequest)
  })
_sym_db.RegisterMessage(DeleteAutoscalingPolicyRequest)

ListAutoscalingPoliciesRequest = _reflection.GeneratedProtocolMessageType('ListAutoscalingPoliciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTOSCALINGPOLICIESREQUEST,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.ListAutoscalingPoliciesRequest)
  })
_sym_db.RegisterMessage(ListAutoscalingPoliciesRequest)

ListAutoscalingPoliciesResponse = _reflection.GeneratedProtocolMessageType('ListAutoscalingPoliciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTOSCALINGPOLICIESRESPONSE,
  '__module__' : 'google.cloud.dataproc.v1.autoscaling_policies_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.v1.ListAutoscalingPoliciesResponse)
  })
_sym_db.RegisterMessage(ListAutoscalingPoliciesResponse)

_AUTOSCALINGPOLICYSERVICE = DESCRIPTOR.services_by_name['AutoscalingPolicyService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.google.cloud.dataproc.v1B\030AutoscalingPoliciesProtoP\001Z@google.golang.org/genproto/googleapis/cloud/dataproc/v1;dataproc\352AE\n\036dataproc.googleapis.com/Region\022#projects/{project}/regions/{region}'
  _AUTOSCALINGPOLICY_LABELSENTRY._options = None
  _AUTOSCALINGPOLICY_LABELSENTRY._serialized_options = b'8\001'
  _AUTOSCALINGPOLICY.fields_by_name['name']._options = None
  _AUTOSCALINGPOLICY.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _AUTOSCALINGPOLICY.fields_by_name['basic_algorithm']._options = None
  _AUTOSCALINGPOLICY.fields_by_name['basic_algorithm']._serialized_options = b'\342A\001\002'
  _AUTOSCALINGPOLICY.fields_by_name['worker_config']._options = None
  _AUTOSCALINGPOLICY.fields_by_name['worker_config']._serialized_options = b'\342A\001\002'
  _AUTOSCALINGPOLICY.fields_by_name['secondary_worker_config']._options = None
  _AUTOSCALINGPOLICY.fields_by_name['secondary_worker_config']._serialized_options = b'\342A\001\001'
  _AUTOSCALINGPOLICY.fields_by_name['labels']._options = None
  _AUTOSCALINGPOLICY.fields_by_name['labels']._serialized_options = b'\342A\001\001'
  _AUTOSCALINGPOLICY._options = None
  _AUTOSCALINGPOLICY._serialized_options = b'\352A\313\001\n)dataproc.googleapis.com/AutoscalingPolicy\022Pprojects/{project}/locations/{location}/autoscalingPolicies/{autoscaling_policy}\022Lprojects/{project}/regions/{region}/autoscalingPolicies/{autoscaling_policy}'
  _BASICAUTOSCALINGALGORITHM.fields_by_name['yarn_config']._options = None
  _BASICAUTOSCALINGALGORITHM.fields_by_name['yarn_config']._serialized_options = b'\342A\001\002'
  _BASICAUTOSCALINGALGORITHM.fields_by_name['cooldown_period']._options = None
  _BASICAUTOSCALINGALGORITHM.fields_by_name['cooldown_period']._serialized_options = b'\342A\001\001'
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['graceful_decommission_timeout']._options = None
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['graceful_decommission_timeout']._serialized_options = b'\342A\001\002'
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_up_factor']._options = None
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_up_factor']._serialized_options = b'\342A\001\002'
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_down_factor']._options = None
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_down_factor']._serialized_options = b'\342A\001\002'
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_up_min_worker_fraction']._options = None
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_up_min_worker_fraction']._serialized_options = b'\342A\001\001'
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_down_min_worker_fraction']._options = None
  _BASICYARNAUTOSCALINGCONFIG.fields_by_name['scale_down_min_worker_fraction']._serialized_options = b'\342A\001\001'
  _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['min_instances']._options = None
  _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['min_instances']._serialized_options = b'\342A\001\001'
  _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['max_instances']._options = None
  _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['max_instances']._serialized_options = b'\342A\001\002'
  _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['weight']._options = None
  _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG.fields_by_name['weight']._serialized_options = b'\342A\001\001'
  _CREATEAUTOSCALINGPOLICYREQUEST.fields_by_name['parent']._options = None
  _CREATEAUTOSCALINGPOLICYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A+\022)dataproc.googleapis.com/AutoscalingPolicy'
  _CREATEAUTOSCALINGPOLICYREQUEST.fields_by_name['policy']._options = None
  _CREATEAUTOSCALINGPOLICYREQUEST.fields_by_name['policy']._serialized_options = b'\342A\001\002'
  _GETAUTOSCALINGPOLICYREQUEST.fields_by_name['name']._options = None
  _GETAUTOSCALINGPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A+\n)dataproc.googleapis.com/AutoscalingPolicy'
  _UPDATEAUTOSCALINGPOLICYREQUEST.fields_by_name['policy']._options = None
  _UPDATEAUTOSCALINGPOLICYREQUEST.fields_by_name['policy']._serialized_options = b'\342A\001\002'
  _DELETEAUTOSCALINGPOLICYREQUEST.fields_by_name['name']._options = None
  _DELETEAUTOSCALINGPOLICYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A+\n)dataproc.googleapis.com/AutoscalingPolicy'
  _LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['parent']._options = None
  _LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A+\022)dataproc.googleapis.com/AutoscalingPolicy'
  _LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['page_size']._options = None
  _LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['page_token']._options = None
  _LISTAUTOSCALINGPOLICIESREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTAUTOSCALINGPOLICIESRESPONSE.fields_by_name['policies']._options = None
  _LISTAUTOSCALINGPOLICIESRESPONSE.fields_by_name['policies']._serialized_options = b'\342A\001\003'
  _LISTAUTOSCALINGPOLICIESRESPONSE.fields_by_name['next_page_token']._options = None
  _LISTAUTOSCALINGPOLICIESRESPONSE.fields_by_name['next_page_token']._serialized_options = b'\342A\001\003'
  _AUTOSCALINGPOLICYSERVICE._options = None
  _AUTOSCALINGPOLICYSERVICE._serialized_options = b'\312A\027dataproc.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['CreateAutoscalingPolicy']._options = None
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['CreateAutoscalingPolicy']._serialized_options = b'\332A\rparent,policy\202\323\344\223\002\202\001\"7/v1/{parent=projects/*/locations/*}/autoscalingPolicies:\006policyZ?\"5/v1/{parent=projects/*/regions/*}/autoscalingPolicies:\006policy'
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['UpdateAutoscalingPolicy']._options = None
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['UpdateAutoscalingPolicy']._serialized_options = b'\332A\006policy\202\323\344\223\002\220\001\032>/v1/{policy.name=projects/*/locations/*/autoscalingPolicies/*}:\006policyZF\032</v1/{policy.name=projects/*/regions/*/autoscalingPolicies/*}:\006policy'
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['GetAutoscalingPolicy']._options = None
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['GetAutoscalingPolicy']._serialized_options = b'\332A\004name\202\323\344\223\002r\0227/v1/{name=projects/*/locations/*/autoscalingPolicies/*}Z7\0225/v1/{name=projects/*/regions/*/autoscalingPolicies/*}'
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['ListAutoscalingPolicies']._options = None
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['ListAutoscalingPolicies']._serialized_options = b'\332A\006parent\202\323\344\223\002r\0227/v1/{parent=projects/*/locations/*}/autoscalingPoliciesZ7\0225/v1/{parent=projects/*/regions/*}/autoscalingPolicies'
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['DeleteAutoscalingPolicy']._options = None
  _AUTOSCALINGPOLICYSERVICE.methods_by_name['DeleteAutoscalingPolicy']._serialized_options = b'\332A\004name\202\323\344\223\002r*7/v1/{name=projects/*/locations/*/autoscalingPolicies/*}Z7*5/v1/{name=projects/*/regions/*/autoscalingPolicies/*}'
  _AUTOSCALINGPOLICY._serialized_start=258
  _AUTOSCALINGPOLICY._serialized_end=1023
  _AUTOSCALINGPOLICY_LABELSENTRY._serialized_start=743
  _AUTOSCALINGPOLICY_LABELSENTRY._serialized_end=800
  _BASICAUTOSCALINGALGORITHM._serialized_start=1026
  _BASICAUTOSCALINGALGORITHM._serialized_end=1220
  _BASICYARNAUTOSCALINGCONFIG._serialized_start=1223
  _BASICYARNAUTOSCALINGCONFIG._serialized_end=1592
  _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG._serialized_start=1595
  _INSTANCEGROUPAUTOSCALINGPOLICYCONFIG._serialized_end=1749
  _CREATEAUTOSCALINGPOLICYREQUEST._serialized_start=1752
  _CREATEAUTOSCALINGPOLICYREQUEST._serialized_end=1935
  _GETAUTOSCALINGPOLICYREQUEST._serialized_start=1937
  _GETAUTOSCALINGPOLICYREQUEST._serialized_end=2038
  _UPDATEAUTOSCALINGPOLICYREQUEST._serialized_start=2040
  _UPDATEAUTOSCALINGPOLICYREQUEST._serialized_end=2147
  _DELETEAUTOSCALINGPOLICYREQUEST._serialized_start=2149
  _DELETEAUTOSCALINGPOLICYREQUEST._serialized_end=2253
  _LISTAUTOSCALINGPOLICIESREQUEST._serialized_start=2256
  _LISTAUTOSCALINGPOLICIESREQUEST._serialized_end=2436
  _LISTAUTOSCALINGPOLICIESRESPONSE._serialized_start=2439
  _LISTAUTOSCALINGPOLICIESRESPONSE._serialized_end=2597
  _AUTOSCALINGPOLICYSERVICE._serialized_start=2600
  _AUTOSCALINGPOLICYSERVICE._serialized_end=4054
# @@protoc_insertion_point(module_scope)
