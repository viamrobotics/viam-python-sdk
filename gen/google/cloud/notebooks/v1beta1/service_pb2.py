# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/notebooks/v1beta1/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.notebooks.v1beta1 import environment_pb2 as google_dot_cloud_dot_notebooks_dot_v1beta1_dot_environment__pb2
from google.cloud.notebooks.v1beta1 import instance_pb2 as google_dot_cloud_dot_notebooks_dot_v1beta1_dot_instance__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/notebooks/v1beta1/service.proto\x12\x1egoogle.cloud.notebooks.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x30google/cloud/notebooks/v1beta1/environment.proto\x1a-google/cloud/notebooks/v1beta1/instance.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/api/client.proto\"\xce\x02\n\x11OperationMetadata\x12;\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x16\n\x06target\x18\x03 \x01(\tR\x06target\x12\x12\n\x04verb\x18\x04 \x01(\tR\x04verb\x12%\n\x0estatus_message\x18\x05 \x01(\tR\rstatusMessage\x12\x35\n\x16requested_cancellation\x18\x06 \x01(\x08R\x15requestedCancellation\x12\x1f\n\x0b\x61pi_version\x18\x07 \x01(\tR\napiVersion\x12\x1a\n\x08\x65ndpoint\x18\x08 \x01(\tR\x08\x65ndpoint\"p\n\x14ListInstancesRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\xa9\x01\n\x15ListInstancesResponse\x12\x46\n\tinstances\x18\x01 \x03(\x0b\x32(.google.cloud.notebooks.v1beta1.InstanceR\tinstances\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x03 \x03(\tR\x0bunreachable\".\n\x12GetInstanceRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"\xa8\x01\n\x15\x43reateInstanceRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12%\n\x0binstance_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\ninstanceId\x12J\n\x08instance\x18\x03 \x01(\x0b\x32(.google.cloud.notebooks.v1beta1.InstanceB\x04\xe2\x41\x01\x02R\x08instance\"^\n\x17RegisterInstanceRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12%\n\x0binstance_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\ninstanceId\"\xb2\x01\n\x1dSetInstanceAcceleratorRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12R\n\x04type\x18\x02 \x01(\x0e\x32\x38.google.cloud.notebooks.v1beta1.Instance.AcceleratorTypeB\x04\xe2\x41\x01\x02R\x04type\x12#\n\ncore_count\x18\x03 \x01(\x03\x42\x04\xe2\x41\x01\x02R\tcoreCount\"b\n\x1dSetInstanceMachineTypeRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\'\n\x0cmachine_type\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0bmachineType\"\xcd\x01\n\x18SetInstanceLabelsRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\\\n\x06labels\x18\x02 \x03(\x0b\x32\x44.google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"1\n\x15\x44\x65leteInstanceRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"0\n\x14StartInstanceRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"/\n\x13StopInstanceRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"0\n\x14ResetInstanceRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"\xf2\x01\n\x19ReportInstanceInfoRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\x19\n\x05vm_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x04vmId\x12\x63\n\x08metadata\x18\x03 \x03(\x0b\x32G.google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest.MetadataEntryR\x08metadata\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"Q\n\x1cIsInstanceUpgradeableRequest\x12\x31\n\x11notebook_instance\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x10notebookInstance\"\x8d\x01\n\x1dIsInstanceUpgradeableResponse\x12 \n\x0bupgradeable\x18\x01 \x01(\x08R\x0bupgradeable\x12\'\n\x0fupgrade_version\x18\x02 \x01(\tR\x0eupgradeVersion\x12!\n\x0cupgrade_info\x18\x03 \x01(\tR\x0bupgradeInfo\"2\n\x16UpgradeInstanceRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"U\n\x1eUpgradeInstanceInternalRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\x19\n\x05vm_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x04vmId\"s\n\x17ListEnvironmentsRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\xb5\x01\n\x18ListEnvironmentsResponse\x12O\n\x0c\x65nvironments\x18\x01 \x03(\x0b\x32+.google.cloud.notebooks.v1beta1.EnvironmentR\x0c\x65nvironments\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x03 \x03(\tR\x0bunreachable\"1\n\x15GetEnvironmentRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"\xba\x01\n\x18\x43reateEnvironmentRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12+\n\x0e\x65nvironment_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\renvironmentId\x12S\n\x0b\x65nvironment\x18\x03 \x01(\x0b\x32+.google.cloud.notebooks.v1beta1.EnvironmentB\x04\xe2\x41\x01\x02R\x0b\x65nvironment\"4\n\x18\x44\x65leteEnvironmentRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name2\xf8\x1f\n\x0fNotebookService\x12\xb8\x01\n\rListInstances\x12\x34.google.cloud.notebooks.v1beta1.ListInstancesRequest\x1a\x35.google.cloud.notebooks.v1beta1.ListInstancesResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/v1beta1/{parent=projects/*/locations/*}/instances\x12\xa7\x01\n\x0bGetInstance\x12\x32.google.cloud.notebooks.v1beta1.GetInstanceRequest\x1a(.google.cloud.notebooks.v1beta1.Instance\":\x82\xd3\xe4\x93\x02\x34\x12\x32/v1beta1/{name=projects/*/locations/*/instances/*}\x12\xcc\x01\n\x0e\x43reateInstance\x12\x35.google.cloud.notebooks.v1beta1.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation\"d\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02>\"2/v1beta1/{parent=projects/*/locations/*}/instances:\x08instance\x12\xd2\x01\n\x10RegisterInstance\x12\x37.google.cloud.notebooks.v1beta1.RegisterInstanceRequest\x1a\x1d.google.longrunning.Operation\"f\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02@\";/v1beta1/{parent=projects/*/locations/*}/instances:register:\x01*\x12\xe4\x01\n\x16SetInstanceAccelerator\x12=.google.cloud.notebooks.v1beta1.SetInstanceAcceleratorRequest\x1a\x1d.google.longrunning.Operation\"l\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02\x46\x32\x41/v1beta1/{name=projects/*/locations/*/instances/*}:setAccelerator:\x01*\x12\xe4\x01\n\x16SetInstanceMachineType\x12=.google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest\x1a\x1d.google.longrunning.Operation\"l\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02\x46\x32\x41/v1beta1/{name=projects/*/locations/*/instances/*}:setMachineType:\x01*\x12\xd5\x01\n\x11SetInstanceLabels\x12\x38.google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest\x1a\x1d.google.longrunning.Operation\"g\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02\x41\x32</v1beta1/{name=projects/*/locations/*/instances/*}:setLabels:\x01*\x12\xcf\x01\n\x0e\x44\x65leteInstance\x12\x35.google.cloud.notebooks.v1beta1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation\"g\xca\x41*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02\x34*2/v1beta1/{name=projects/*/locations/*/instances/*}\x12\xc9\x01\n\rStartInstance\x12\x34.google.cloud.notebooks.v1beta1.StartInstanceRequest\x1a\x1d.google.longrunning.Operation\"c\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02=\"8/v1beta1/{name=projects/*/locations/*/instances/*}:start:\x01*\x12\xc6\x01\n\x0cStopInstance\x12\x33.google.cloud.notebooks.v1beta1.StopInstanceRequest\x1a\x1d.google.longrunning.Operation\"b\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02<\"7/v1beta1/{name=projects/*/locations/*/instances/*}:stop:\x01*\x12\xc9\x01\n\rResetInstance\x12\x34.google.cloud.notebooks.v1beta1.ResetInstanceRequest\x1a\x1d.google.longrunning.Operation\"c\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02=\"8/v1beta1/{name=projects/*/locations/*/instances/*}:reset:\x01*\x12\xd4\x01\n\x12ReportInstanceInfo\x12\x39.google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest\x1a\x1d.google.longrunning.Operation\"d\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02>\"9/v1beta1/{name=projects/*/locations/*/instances/*}:report:\x01*\x12\xeb\x01\n\x15IsInstanceUpgradeable\x12<.google.cloud.notebooks.v1beta1.IsInstanceUpgradeableRequest\x1a=.google.cloud.notebooks.v1beta1.IsInstanceUpgradeableResponse\"U\x82\xd3\xe4\x93\x02O\x12M/v1beta1/{notebook_instance=projects/*/locations/*/instances/*}:isUpgradeable\x12\xcf\x01\n\x0fUpgradeInstance\x12\x36.google.cloud.notebooks.v1beta1.UpgradeInstanceRequest\x1a\x1d.google.longrunning.Operation\"e\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02?\":/v1beta1/{name=projects/*/locations/*/instances/*}:upgrade:\x01*\x12\xe7\x01\n\x17UpgradeInstanceInternal\x12>.google.cloud.notebooks.v1beta1.UpgradeInstanceInternalRequest\x1a\x1d.google.longrunning.Operation\"m\xca\x41\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02G\"B/v1beta1/{name=projects/*/locations/*/instances/*}:upgradeInternal:\x01*\x12\xc4\x01\n\x10ListEnvironments\x12\x37.google.cloud.notebooks.v1beta1.ListEnvironmentsRequest\x1a\x38.google.cloud.notebooks.v1beta1.ListEnvironmentsResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v1beta1/{parent=projects/*/locations/*}/environments\x12\xb3\x01\n\x0eGetEnvironment\x12\x35.google.cloud.notebooks.v1beta1.GetEnvironmentRequest\x1a+.google.cloud.notebooks.v1beta1.Environment\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v1beta1/{name=projects/*/locations/*/environments/*}\x12\xdb\x01\n\x11\x43reateEnvironment\x12\x38.google.cloud.notebooks.v1beta1.CreateEnvironmentRequest\x1a\x1d.google.longrunning.Operation\"m\xca\x41 \n\x0b\x45nvironment\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02\x44\"5/v1beta1/{parent=projects/*/locations/*}/environments:\x0b\x65nvironment\x12\xd8\x01\n\x11\x44\x65leteEnvironment\x12\x38.google.cloud.notebooks.v1beta1.DeleteEnvironmentRequest\x1a\x1d.google.longrunning.Operation\"j\xca\x41*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02\x37*5/v1beta1/{name=projects/*/locations/*/environments/*}\x1aL\xca\x41\x18notebooks.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xe5\x01\n\"com.google.cloud.notebooks.v1beta1B\x0eNotebooksProtoP\x01ZGgoogle.golang.org/genproto/googleapis/cloud/notebooks/v1beta1;notebooks\xaa\x02\x1eGoogle.Cloud.Notebooks.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Notebooks\\V1beta1\xea\x02!Google::Cloud::Notebooks::V1beta1b\x06proto3')



_OPERATIONMETADATA = DESCRIPTOR.message_types_by_name['OperationMetadata']
_LISTINSTANCESREQUEST = DESCRIPTOR.message_types_by_name['ListInstancesRequest']
_LISTINSTANCESRESPONSE = DESCRIPTOR.message_types_by_name['ListInstancesResponse']
_GETINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['GetInstanceRequest']
_CREATEINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['CreateInstanceRequest']
_REGISTERINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['RegisterInstanceRequest']
_SETINSTANCEACCELERATORREQUEST = DESCRIPTOR.message_types_by_name['SetInstanceAcceleratorRequest']
_SETINSTANCEMACHINETYPEREQUEST = DESCRIPTOR.message_types_by_name['SetInstanceMachineTypeRequest']
_SETINSTANCELABELSREQUEST = DESCRIPTOR.message_types_by_name['SetInstanceLabelsRequest']
_SETINSTANCELABELSREQUEST_LABELSENTRY = _SETINSTANCELABELSREQUEST.nested_types_by_name['LabelsEntry']
_DELETEINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['DeleteInstanceRequest']
_STARTINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['StartInstanceRequest']
_STOPINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['StopInstanceRequest']
_RESETINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['ResetInstanceRequest']
_REPORTINSTANCEINFOREQUEST = DESCRIPTOR.message_types_by_name['ReportInstanceInfoRequest']
_REPORTINSTANCEINFOREQUEST_METADATAENTRY = _REPORTINSTANCEINFOREQUEST.nested_types_by_name['MetadataEntry']
_ISINSTANCEUPGRADEABLEREQUEST = DESCRIPTOR.message_types_by_name['IsInstanceUpgradeableRequest']
_ISINSTANCEUPGRADEABLERESPONSE = DESCRIPTOR.message_types_by_name['IsInstanceUpgradeableResponse']
_UPGRADEINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['UpgradeInstanceRequest']
_UPGRADEINSTANCEINTERNALREQUEST = DESCRIPTOR.message_types_by_name['UpgradeInstanceInternalRequest']
_LISTENVIRONMENTSREQUEST = DESCRIPTOR.message_types_by_name['ListEnvironmentsRequest']
_LISTENVIRONMENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListEnvironmentsResponse']
_GETENVIRONMENTREQUEST = DESCRIPTOR.message_types_by_name['GetEnvironmentRequest']
_CREATEENVIRONMENTREQUEST = DESCRIPTOR.message_types_by_name['CreateEnvironmentRequest']
_DELETEENVIRONMENTREQUEST = DESCRIPTOR.message_types_by_name['DeleteEnvironmentRequest']
OperationMetadata = _reflection.GeneratedProtocolMessageType('OperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONMETADATA,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.OperationMetadata)
  })
_sym_db.RegisterMessage(OperationMetadata)

ListInstancesRequest = _reflection.GeneratedProtocolMessageType('ListInstancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCESREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.ListInstancesRequest)
  })
_sym_db.RegisterMessage(ListInstancesRequest)

ListInstancesResponse = _reflection.GeneratedProtocolMessageType('ListInstancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCESRESPONSE,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.ListInstancesResponse)
  })
_sym_db.RegisterMessage(ListInstancesResponse)

GetInstanceRequest = _reflection.GeneratedProtocolMessageType('GetInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTANCEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.GetInstanceRequest)
  })
_sym_db.RegisterMessage(GetInstanceRequest)

CreateInstanceRequest = _reflection.GeneratedProtocolMessageType('CreateInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEINSTANCEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.CreateInstanceRequest)
  })
_sym_db.RegisterMessage(CreateInstanceRequest)

RegisterInstanceRequest = _reflection.GeneratedProtocolMessageType('RegisterInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERINSTANCEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.RegisterInstanceRequest)
  })
_sym_db.RegisterMessage(RegisterInstanceRequest)

SetInstanceAcceleratorRequest = _reflection.GeneratedProtocolMessageType('SetInstanceAcceleratorRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETINSTANCEACCELERATORREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.SetInstanceAcceleratorRequest)
  })
_sym_db.RegisterMessage(SetInstanceAcceleratorRequest)

SetInstanceMachineTypeRequest = _reflection.GeneratedProtocolMessageType('SetInstanceMachineTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETINSTANCEMACHINETYPEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest)
  })
_sym_db.RegisterMessage(SetInstanceMachineTypeRequest)

SetInstanceLabelsRequest = _reflection.GeneratedProtocolMessageType('SetInstanceLabelsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SETINSTANCELABELSREQUEST_LABELSENTRY,
    '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SETINSTANCELABELSREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest)
  })
_sym_db.RegisterMessage(SetInstanceLabelsRequest)
_sym_db.RegisterMessage(SetInstanceLabelsRequest.LabelsEntry)

DeleteInstanceRequest = _reflection.GeneratedProtocolMessageType('DeleteInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEINSTANCEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.DeleteInstanceRequest)
  })
_sym_db.RegisterMessage(DeleteInstanceRequest)

StartInstanceRequest = _reflection.GeneratedProtocolMessageType('StartInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTINSTANCEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.StartInstanceRequest)
  })
_sym_db.RegisterMessage(StartInstanceRequest)

StopInstanceRequest = _reflection.GeneratedProtocolMessageType('StopInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPINSTANCEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.StopInstanceRequest)
  })
_sym_db.RegisterMessage(StopInstanceRequest)

ResetInstanceRequest = _reflection.GeneratedProtocolMessageType('ResetInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETINSTANCEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.ResetInstanceRequest)
  })
_sym_db.RegisterMessage(ResetInstanceRequest)

ReportInstanceInfoRequest = _reflection.GeneratedProtocolMessageType('ReportInstanceInfoRequest', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _REPORTINSTANCEINFOREQUEST_METADATAENTRY,
    '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _REPORTINSTANCEINFOREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest)
  })
_sym_db.RegisterMessage(ReportInstanceInfoRequest)
_sym_db.RegisterMessage(ReportInstanceInfoRequest.MetadataEntry)

IsInstanceUpgradeableRequest = _reflection.GeneratedProtocolMessageType('IsInstanceUpgradeableRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISINSTANCEUPGRADEABLEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.IsInstanceUpgradeableRequest)
  })
_sym_db.RegisterMessage(IsInstanceUpgradeableRequest)

IsInstanceUpgradeableResponse = _reflection.GeneratedProtocolMessageType('IsInstanceUpgradeableResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISINSTANCEUPGRADEABLERESPONSE,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.IsInstanceUpgradeableResponse)
  })
_sym_db.RegisterMessage(IsInstanceUpgradeableResponse)

UpgradeInstanceRequest = _reflection.GeneratedProtocolMessageType('UpgradeInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPGRADEINSTANCEREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.UpgradeInstanceRequest)
  })
_sym_db.RegisterMessage(UpgradeInstanceRequest)

UpgradeInstanceInternalRequest = _reflection.GeneratedProtocolMessageType('UpgradeInstanceInternalRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPGRADEINSTANCEINTERNALREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.UpgradeInstanceInternalRequest)
  })
_sym_db.RegisterMessage(UpgradeInstanceInternalRequest)

ListEnvironmentsRequest = _reflection.GeneratedProtocolMessageType('ListEnvironmentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTENVIRONMENTSREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.ListEnvironmentsRequest)
  })
_sym_db.RegisterMessage(ListEnvironmentsRequest)

ListEnvironmentsResponse = _reflection.GeneratedProtocolMessageType('ListEnvironmentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTENVIRONMENTSRESPONSE,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.ListEnvironmentsResponse)
  })
_sym_db.RegisterMessage(ListEnvironmentsResponse)

GetEnvironmentRequest = _reflection.GeneratedProtocolMessageType('GetEnvironmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETENVIRONMENTREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.GetEnvironmentRequest)
  })
_sym_db.RegisterMessage(GetEnvironmentRequest)

CreateEnvironmentRequest = _reflection.GeneratedProtocolMessageType('CreateEnvironmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENVIRONMENTREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.CreateEnvironmentRequest)
  })
_sym_db.RegisterMessage(CreateEnvironmentRequest)

DeleteEnvironmentRequest = _reflection.GeneratedProtocolMessageType('DeleteEnvironmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENVIRONMENTREQUEST,
  '__module__' : 'google.cloud.notebooks.v1beta1.service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1beta1.DeleteEnvironmentRequest)
  })
_sym_db.RegisterMessage(DeleteEnvironmentRequest)

_NOTEBOOKSERVICE = DESCRIPTOR.services_by_name['NotebookService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.cloud.notebooks.v1beta1B\016NotebooksProtoP\001ZGgoogle.golang.org/genproto/googleapis/cloud/notebooks/v1beta1;notebooks\252\002\036Google.Cloud.Notebooks.V1Beta1\312\002\036Google\\Cloud\\Notebooks\\V1beta1\352\002!Google::Cloud::Notebooks::V1beta1'
  _LISTINSTANCESREQUEST.fields_by_name['parent']._options = None
  _LISTINSTANCESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _GETINSTANCEREQUEST.fields_by_name['name']._options = None
  _GETINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _CREATEINSTANCEREQUEST.fields_by_name['parent']._options = None
  _CREATEINSTANCEREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _CREATEINSTANCEREQUEST.fields_by_name['instance_id']._options = None
  _CREATEINSTANCEREQUEST.fields_by_name['instance_id']._serialized_options = b'\342A\001\002'
  _CREATEINSTANCEREQUEST.fields_by_name['instance']._options = None
  _CREATEINSTANCEREQUEST.fields_by_name['instance']._serialized_options = b'\342A\001\002'
  _REGISTERINSTANCEREQUEST.fields_by_name['parent']._options = None
  _REGISTERINSTANCEREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _REGISTERINSTANCEREQUEST.fields_by_name['instance_id']._options = None
  _REGISTERINSTANCEREQUEST.fields_by_name['instance_id']._serialized_options = b'\342A\001\002'
  _SETINSTANCEACCELERATORREQUEST.fields_by_name['name']._options = None
  _SETINSTANCEACCELERATORREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _SETINSTANCEACCELERATORREQUEST.fields_by_name['type']._options = None
  _SETINSTANCEACCELERATORREQUEST.fields_by_name['type']._serialized_options = b'\342A\001\002'
  _SETINSTANCEACCELERATORREQUEST.fields_by_name['core_count']._options = None
  _SETINSTANCEACCELERATORREQUEST.fields_by_name['core_count']._serialized_options = b'\342A\001\002'
  _SETINSTANCEMACHINETYPEREQUEST.fields_by_name['name']._options = None
  _SETINSTANCEMACHINETYPEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _SETINSTANCEMACHINETYPEREQUEST.fields_by_name['machine_type']._options = None
  _SETINSTANCEMACHINETYPEREQUEST.fields_by_name['machine_type']._serialized_options = b'\342A\001\002'
  _SETINSTANCELABELSREQUEST_LABELSENTRY._options = None
  _SETINSTANCELABELSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _SETINSTANCELABELSREQUEST.fields_by_name['name']._options = None
  _SETINSTANCELABELSREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _DELETEINSTANCEREQUEST.fields_by_name['name']._options = None
  _DELETEINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _STARTINSTANCEREQUEST.fields_by_name['name']._options = None
  _STARTINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _STOPINSTANCEREQUEST.fields_by_name['name']._options = None
  _STOPINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _RESETINSTANCEREQUEST.fields_by_name['name']._options = None
  _RESETINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _REPORTINSTANCEINFOREQUEST_METADATAENTRY._options = None
  _REPORTINSTANCEINFOREQUEST_METADATAENTRY._serialized_options = b'8\001'
  _REPORTINSTANCEINFOREQUEST.fields_by_name['name']._options = None
  _REPORTINSTANCEINFOREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _REPORTINSTANCEINFOREQUEST.fields_by_name['vm_id']._options = None
  _REPORTINSTANCEINFOREQUEST.fields_by_name['vm_id']._serialized_options = b'\342A\001\002'
  _ISINSTANCEUPGRADEABLEREQUEST.fields_by_name['notebook_instance']._options = None
  _ISINSTANCEUPGRADEABLEREQUEST.fields_by_name['notebook_instance']._serialized_options = b'\342A\001\002'
  _UPGRADEINSTANCEREQUEST.fields_by_name['name']._options = None
  _UPGRADEINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _UPGRADEINSTANCEINTERNALREQUEST.fields_by_name['name']._options = None
  _UPGRADEINSTANCEINTERNALREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _UPGRADEINSTANCEINTERNALREQUEST.fields_by_name['vm_id']._options = None
  _UPGRADEINSTANCEINTERNALREQUEST.fields_by_name['vm_id']._serialized_options = b'\342A\001\002'
  _LISTENVIRONMENTSREQUEST.fields_by_name['parent']._options = None
  _LISTENVIRONMENTSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _GETENVIRONMENTREQUEST.fields_by_name['name']._options = None
  _GETENVIRONMENTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _CREATEENVIRONMENTREQUEST.fields_by_name['parent']._options = None
  _CREATEENVIRONMENTREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _CREATEENVIRONMENTREQUEST.fields_by_name['environment_id']._options = None
  _CREATEENVIRONMENTREQUEST.fields_by_name['environment_id']._serialized_options = b'\342A\001\002'
  _CREATEENVIRONMENTREQUEST.fields_by_name['environment']._options = None
  _CREATEENVIRONMENTREQUEST.fields_by_name['environment']._serialized_options = b'\342A\001\002'
  _DELETEENVIRONMENTREQUEST.fields_by_name['name']._options = None
  _DELETEENVIRONMENTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _NOTEBOOKSERVICE._options = None
  _NOTEBOOKSERVICE._serialized_options = b'\312A\030notebooks.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _NOTEBOOKSERVICE.methods_by_name['ListInstances']._options = None
  _NOTEBOOKSERVICE.methods_by_name['ListInstances']._serialized_options = b'\202\323\344\223\0024\0222/v1beta1/{parent=projects/*/locations/*}/instances'
  _NOTEBOOKSERVICE.methods_by_name['GetInstance']._options = None
  _NOTEBOOKSERVICE.methods_by_name['GetInstance']._serialized_options = b'\202\323\344\223\0024\0222/v1beta1/{name=projects/*/locations/*/instances/*}'
  _NOTEBOOKSERVICE.methods_by_name['CreateInstance']._options = None
  _NOTEBOOKSERVICE.methods_by_name['CreateInstance']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002>\"2/v1beta1/{parent=projects/*/locations/*}/instances:\010instance'
  _NOTEBOOKSERVICE.methods_by_name['RegisterInstance']._options = None
  _NOTEBOOKSERVICE.methods_by_name['RegisterInstance']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002@\";/v1beta1/{parent=projects/*/locations/*}/instances:register:\001*'
  _NOTEBOOKSERVICE.methods_by_name['SetInstanceAccelerator']._options = None
  _NOTEBOOKSERVICE.methods_by_name['SetInstanceAccelerator']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002F2A/v1beta1/{name=projects/*/locations/*/instances/*}:setAccelerator:\001*'
  _NOTEBOOKSERVICE.methods_by_name['SetInstanceMachineType']._options = None
  _NOTEBOOKSERVICE.methods_by_name['SetInstanceMachineType']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002F2A/v1beta1/{name=projects/*/locations/*/instances/*}:setMachineType:\001*'
  _NOTEBOOKSERVICE.methods_by_name['SetInstanceLabels']._options = None
  _NOTEBOOKSERVICE.methods_by_name['SetInstanceLabels']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002A2</v1beta1/{name=projects/*/locations/*/instances/*}:setLabels:\001*'
  _NOTEBOOKSERVICE.methods_by_name['DeleteInstance']._options = None
  _NOTEBOOKSERVICE.methods_by_name['DeleteInstance']._serialized_options = b'\312A*\n\025google.protobuf.Empty\022\021OperationMetadata\202\323\344\223\0024*2/v1beta1/{name=projects/*/locations/*/instances/*}'
  _NOTEBOOKSERVICE.methods_by_name['StartInstance']._options = None
  _NOTEBOOKSERVICE.methods_by_name['StartInstance']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002=\"8/v1beta1/{name=projects/*/locations/*/instances/*}:start:\001*'
  _NOTEBOOKSERVICE.methods_by_name['StopInstance']._options = None
  _NOTEBOOKSERVICE.methods_by_name['StopInstance']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002<\"7/v1beta1/{name=projects/*/locations/*/instances/*}:stop:\001*'
  _NOTEBOOKSERVICE.methods_by_name['ResetInstance']._options = None
  _NOTEBOOKSERVICE.methods_by_name['ResetInstance']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002=\"8/v1beta1/{name=projects/*/locations/*/instances/*}:reset:\001*'
  _NOTEBOOKSERVICE.methods_by_name['ReportInstanceInfo']._options = None
  _NOTEBOOKSERVICE.methods_by_name['ReportInstanceInfo']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002>\"9/v1beta1/{name=projects/*/locations/*/instances/*}:report:\001*'
  _NOTEBOOKSERVICE.methods_by_name['IsInstanceUpgradeable']._options = None
  _NOTEBOOKSERVICE.methods_by_name['IsInstanceUpgradeable']._serialized_options = b'\202\323\344\223\002O\022M/v1beta1/{notebook_instance=projects/*/locations/*/instances/*}:isUpgradeable'
  _NOTEBOOKSERVICE.methods_by_name['UpgradeInstance']._options = None
  _NOTEBOOKSERVICE.methods_by_name['UpgradeInstance']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002?\":/v1beta1/{name=projects/*/locations/*/instances/*}:upgrade:\001*'
  _NOTEBOOKSERVICE.methods_by_name['UpgradeInstanceInternal']._options = None
  _NOTEBOOKSERVICE.methods_by_name['UpgradeInstanceInternal']._serialized_options = b'\312A\035\n\010Instance\022\021OperationMetadata\202\323\344\223\002G\"B/v1beta1/{name=projects/*/locations/*/instances/*}:upgradeInternal:\001*'
  _NOTEBOOKSERVICE.methods_by_name['ListEnvironments']._options = None
  _NOTEBOOKSERVICE.methods_by_name['ListEnvironments']._serialized_options = b'\202\323\344\223\0027\0225/v1beta1/{parent=projects/*/locations/*}/environments'
  _NOTEBOOKSERVICE.methods_by_name['GetEnvironment']._options = None
  _NOTEBOOKSERVICE.methods_by_name['GetEnvironment']._serialized_options = b'\202\323\344\223\0027\0225/v1beta1/{name=projects/*/locations/*/environments/*}'
  _NOTEBOOKSERVICE.methods_by_name['CreateEnvironment']._options = None
  _NOTEBOOKSERVICE.methods_by_name['CreateEnvironment']._serialized_options = b'\312A \n\013Environment\022\021OperationMetadata\202\323\344\223\002D\"5/v1beta1/{parent=projects/*/locations/*}/environments:\013environment'
  _NOTEBOOKSERVICE.methods_by_name['DeleteEnvironment']._options = None
  _NOTEBOOKSERVICE.methods_by_name['DeleteEnvironment']._serialized_options = b'\312A*\n\025google.protobuf.Empty\022\021OperationMetadata\202\323\344\223\0027*5/v1beta1/{name=projects/*/locations/*/environments/*}'
  _OPERATIONMETADATA._serialized_start=336
  _OPERATIONMETADATA._serialized_end=670
  _LISTINSTANCESREQUEST._serialized_start=672
  _LISTINSTANCESREQUEST._serialized_end=784
  _LISTINSTANCESRESPONSE._serialized_start=787
  _LISTINSTANCESRESPONSE._serialized_end=956
  _GETINSTANCEREQUEST._serialized_start=958
  _GETINSTANCEREQUEST._serialized_end=1004
  _CREATEINSTANCEREQUEST._serialized_start=1007
  _CREATEINSTANCEREQUEST._serialized_end=1175
  _REGISTERINSTANCEREQUEST._serialized_start=1177
  _REGISTERINSTANCEREQUEST._serialized_end=1271
  _SETINSTANCEACCELERATORREQUEST._serialized_start=1274
  _SETINSTANCEACCELERATORREQUEST._serialized_end=1452
  _SETINSTANCEMACHINETYPEREQUEST._serialized_start=1454
  _SETINSTANCEMACHINETYPEREQUEST._serialized_end=1552
  _SETINSTANCELABELSREQUEST._serialized_start=1555
  _SETINSTANCELABELSREQUEST._serialized_end=1760
  _SETINSTANCELABELSREQUEST_LABELSENTRY._serialized_start=1703
  _SETINSTANCELABELSREQUEST_LABELSENTRY._serialized_end=1760
  _DELETEINSTANCEREQUEST._serialized_start=1762
  _DELETEINSTANCEREQUEST._serialized_end=1811
  _STARTINSTANCEREQUEST._serialized_start=1813
  _STARTINSTANCEREQUEST._serialized_end=1861
  _STOPINSTANCEREQUEST._serialized_start=1863
  _STOPINSTANCEREQUEST._serialized_end=1910
  _RESETINSTANCEREQUEST._serialized_start=1912
  _RESETINSTANCEREQUEST._serialized_end=1960
  _REPORTINSTANCEINFOREQUEST._serialized_start=1963
  _REPORTINSTANCEINFOREQUEST._serialized_end=2205
  _REPORTINSTANCEINFOREQUEST_METADATAENTRY._serialized_start=2146
  _REPORTINSTANCEINFOREQUEST_METADATAENTRY._serialized_end=2205
  _ISINSTANCEUPGRADEABLEREQUEST._serialized_start=2207
  _ISINSTANCEUPGRADEABLEREQUEST._serialized_end=2288
  _ISINSTANCEUPGRADEABLERESPONSE._serialized_start=2291
  _ISINSTANCEUPGRADEABLERESPONSE._serialized_end=2432
  _UPGRADEINSTANCEREQUEST._serialized_start=2434
  _UPGRADEINSTANCEREQUEST._serialized_end=2484
  _UPGRADEINSTANCEINTERNALREQUEST._serialized_start=2486
  _UPGRADEINSTANCEINTERNALREQUEST._serialized_end=2571
  _LISTENVIRONMENTSREQUEST._serialized_start=2573
  _LISTENVIRONMENTSREQUEST._serialized_end=2688
  _LISTENVIRONMENTSRESPONSE._serialized_start=2691
  _LISTENVIRONMENTSRESPONSE._serialized_end=2872
  _GETENVIRONMENTREQUEST._serialized_start=2874
  _GETENVIRONMENTREQUEST._serialized_end=2923
  _CREATEENVIRONMENTREQUEST._serialized_start=2926
  _CREATEENVIRONMENTREQUEST._serialized_end=3112
  _DELETEENVIRONMENTREQUEST._serialized_start=3114
  _DELETEENVIRONMENTREQUEST._serialized_end=3166
  _NOTEBOOKSERVICE._serialized_start=3169
  _NOTEBOOKSERVICE._serialized_end=7257
# @@protoc_insertion_point(module_scope)
