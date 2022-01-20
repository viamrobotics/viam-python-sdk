# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/networkmanagement/v1/reachability.proto
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
from google.cloud.networkmanagement.v1 import connectivity_test_pb2 as google_dot_cloud_dot_networkmanagement_dot_v1_dot_connectivity__test__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/networkmanagement/v1/reachability.proto\x12!google.cloud.networkmanagement.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x39google/cloud/networkmanagement/v1/connectivity_test.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xab\x01\n\x1cListConnectivityTestsRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\x12\x19\n\x08order_by\x18\x05 \x01(\tR\x07orderBy\"\xbc\x01\n\x1dListConnectivityTestsResponse\x12Q\n\tresources\x18\x01 \x03(\x0b\x32\x33.google.cloud.networkmanagement.v1.ConnectivityTestR\tresources\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x03 \x03(\tR\x0bunreachable\"6\n\x1aGetConnectivityTestRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"\xb3\x01\n\x1d\x43reateConnectivityTestRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12\x1d\n\x07test_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x06testId\x12U\n\x08resource\x18\x03 \x01(\x0b\x32\x33.google.cloud.networkmanagement.v1.ConnectivityTestB\x04\xe2\x41\x01\x02R\x08resource\"\xb9\x01\n\x1dUpdateConnectivityTestRequest\x12\x41\n\x0bupdate_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\x12U\n\x08resource\x18\x02 \x01(\x0b\x32\x33.google.cloud.networkmanagement.v1.ConnectivityTestB\x04\xe2\x41\x01\x02R\x08resource\"9\n\x1d\x44\x65leteConnectivityTestRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"8\n\x1cRerunConnectivityTestRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"\xa4\x02\n\x11OperationMetadata\x12;\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x16\n\x06target\x18\x03 \x01(\tR\x06target\x12\x12\n\x04verb\x18\x04 \x01(\tR\x04verb\x12#\n\rstatus_detail\x18\x05 \x01(\tR\x0cstatusDetail\x12)\n\x10\x63\x61ncel_requested\x18\x06 \x01(\x08R\x0f\x63\x61ncelRequested\x12\x1f\n\x0b\x61pi_version\x18\x07 \x01(\tR\napiVersion2\x96\r\n\x13ReachabilityService\x12\xe7\x01\n\x15ListConnectivityTests\x12?.google.cloud.networkmanagement.v1.ListConnectivityTestsRequest\x1a@.google.cloud.networkmanagement.v1.ListConnectivityTestsResponse\"K\xda\x41\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/global}/connectivityTests\x12\xd4\x01\n\x13GetConnectivityTest\x12=.google.cloud.networkmanagement.v1.GetConnectivityTestRequest\x1a\x33.google.cloud.networkmanagement.v1.ConnectivityTest\"I\xda\x41\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/global/connectivityTests/*}\x12\xac\x02\n\x16\x43reateConnectivityTest\x12@.google.cloud.networkmanagement.v1.CreateConnectivityTestRequest\x1a\x1d.google.longrunning.Operation\"\xb0\x01\xca\x41G\n2google.cloud.networkmanagement.v1.ConnectivityTest\x12\x11OperationMetadata\xda\x41\x17parent,test_id,resource\x82\xd3\xe4\x93\x02\x46\":/v1/{parent=projects/*/locations/global}/connectivityTests:\x08resource\x12\xb2\x02\n\x16UpdateConnectivityTest\x12@.google.cloud.networkmanagement.v1.UpdateConnectivityTestRequest\x1a\x1d.google.longrunning.Operation\"\xb6\x01\xca\x41G\n2google.cloud.networkmanagement.v1.ConnectivityTest\x12\x11OperationMetadata\xda\x41\x14update_mask,resource\x82\xd3\xe4\x93\x02O2C/v1/{resource.name=projects/*/locations/global/connectivityTests/*}:\x08resource\x12\x8f\x02\n\x15RerunConnectivityTest\x12?.google.cloud.networkmanagement.v1.RerunConnectivityTestRequest\x1a\x1d.google.longrunning.Operation\"\x95\x01\xca\x41G\n2google.cloud.networkmanagement.v1.ConnectivityTest\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02\x45\"@/v1/{name=projects/*/locations/global/connectivityTests/*}:rerun:\x01*\x12\xf1\x01\n\x16\x44\x65leteConnectivityTest\x12@.google.cloud.networkmanagement.v1.DeleteConnectivityTestRequest\x1a\x1d.google.longrunning.Operation\"v\xca\x41*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02<*:/v1/{name=projects/*/locations/global/connectivityTests/*}\x1aT\xca\x41 networkmanagement.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x86\x02\n%com.google.cloud.networkmanagement.v1B\x18ReachabilityServiceProtoP\x01ZRgoogle.golang.org/genproto/googleapis/cloud/networkmanagement/v1;networkmanagement\xaa\x02!Google.Cloud.NetworkManagement.V1\xca\x02!Google\\Cloud\\NetworkManagement\\V1\xea\x02$Google::Cloud::NetworkManagement::V1b\x06proto3')



_LISTCONNECTIVITYTESTSREQUEST = DESCRIPTOR.message_types_by_name['ListConnectivityTestsRequest']
_LISTCONNECTIVITYTESTSRESPONSE = DESCRIPTOR.message_types_by_name['ListConnectivityTestsResponse']
_GETCONNECTIVITYTESTREQUEST = DESCRIPTOR.message_types_by_name['GetConnectivityTestRequest']
_CREATECONNECTIVITYTESTREQUEST = DESCRIPTOR.message_types_by_name['CreateConnectivityTestRequest']
_UPDATECONNECTIVITYTESTREQUEST = DESCRIPTOR.message_types_by_name['UpdateConnectivityTestRequest']
_DELETECONNECTIVITYTESTREQUEST = DESCRIPTOR.message_types_by_name['DeleteConnectivityTestRequest']
_RERUNCONNECTIVITYTESTREQUEST = DESCRIPTOR.message_types_by_name['RerunConnectivityTestRequest']
_OPERATIONMETADATA = DESCRIPTOR.message_types_by_name['OperationMetadata']
ListConnectivityTestsRequest = _reflection.GeneratedProtocolMessageType('ListConnectivityTestsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONNECTIVITYTESTSREQUEST,
  '__module__' : 'google.cloud.networkmanagement.v1.reachability_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1.ListConnectivityTestsRequest)
  })
_sym_db.RegisterMessage(ListConnectivityTestsRequest)

ListConnectivityTestsResponse = _reflection.GeneratedProtocolMessageType('ListConnectivityTestsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONNECTIVITYTESTSRESPONSE,
  '__module__' : 'google.cloud.networkmanagement.v1.reachability_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1.ListConnectivityTestsResponse)
  })
_sym_db.RegisterMessage(ListConnectivityTestsResponse)

GetConnectivityTestRequest = _reflection.GeneratedProtocolMessageType('GetConnectivityTestRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTIVITYTESTREQUEST,
  '__module__' : 'google.cloud.networkmanagement.v1.reachability_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1.GetConnectivityTestRequest)
  })
_sym_db.RegisterMessage(GetConnectivityTestRequest)

CreateConnectivityTestRequest = _reflection.GeneratedProtocolMessageType('CreateConnectivityTestRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONNECTIVITYTESTREQUEST,
  '__module__' : 'google.cloud.networkmanagement.v1.reachability_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1.CreateConnectivityTestRequest)
  })
_sym_db.RegisterMessage(CreateConnectivityTestRequest)

UpdateConnectivityTestRequest = _reflection.GeneratedProtocolMessageType('UpdateConnectivityTestRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONNECTIVITYTESTREQUEST,
  '__module__' : 'google.cloud.networkmanagement.v1.reachability_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1.UpdateConnectivityTestRequest)
  })
_sym_db.RegisterMessage(UpdateConnectivityTestRequest)

DeleteConnectivityTestRequest = _reflection.GeneratedProtocolMessageType('DeleteConnectivityTestRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECONNECTIVITYTESTREQUEST,
  '__module__' : 'google.cloud.networkmanagement.v1.reachability_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1.DeleteConnectivityTestRequest)
  })
_sym_db.RegisterMessage(DeleteConnectivityTestRequest)

RerunConnectivityTestRequest = _reflection.GeneratedProtocolMessageType('RerunConnectivityTestRequest', (_message.Message,), {
  'DESCRIPTOR' : _RERUNCONNECTIVITYTESTREQUEST,
  '__module__' : 'google.cloud.networkmanagement.v1.reachability_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1.RerunConnectivityTestRequest)
  })
_sym_db.RegisterMessage(RerunConnectivityTestRequest)

OperationMetadata = _reflection.GeneratedProtocolMessageType('OperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONMETADATA,
  '__module__' : 'google.cloud.networkmanagement.v1.reachability_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1.OperationMetadata)
  })
_sym_db.RegisterMessage(OperationMetadata)

_REACHABILITYSERVICE = DESCRIPTOR.services_by_name['ReachabilityService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.cloud.networkmanagement.v1B\030ReachabilityServiceProtoP\001ZRgoogle.golang.org/genproto/googleapis/cloud/networkmanagement/v1;networkmanagement\252\002!Google.Cloud.NetworkManagement.V1\312\002!Google\\Cloud\\NetworkManagement\\V1\352\002$Google::Cloud::NetworkManagement::V1'
  _LISTCONNECTIVITYTESTSREQUEST.fields_by_name['parent']._options = None
  _LISTCONNECTIVITYTESTSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _GETCONNECTIVITYTESTREQUEST.fields_by_name['name']._options = None
  _GETCONNECTIVITYTESTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _CREATECONNECTIVITYTESTREQUEST.fields_by_name['parent']._options = None
  _CREATECONNECTIVITYTESTREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _CREATECONNECTIVITYTESTREQUEST.fields_by_name['test_id']._options = None
  _CREATECONNECTIVITYTESTREQUEST.fields_by_name['test_id']._serialized_options = b'\342A\001\002'
  _CREATECONNECTIVITYTESTREQUEST.fields_by_name['resource']._options = None
  _CREATECONNECTIVITYTESTREQUEST.fields_by_name['resource']._serialized_options = b'\342A\001\002'
  _UPDATECONNECTIVITYTESTREQUEST.fields_by_name['update_mask']._options = None
  _UPDATECONNECTIVITYTESTREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _UPDATECONNECTIVITYTESTREQUEST.fields_by_name['resource']._options = None
  _UPDATECONNECTIVITYTESTREQUEST.fields_by_name['resource']._serialized_options = b'\342A\001\002'
  _DELETECONNECTIVITYTESTREQUEST.fields_by_name['name']._options = None
  _DELETECONNECTIVITYTESTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _RERUNCONNECTIVITYTESTREQUEST.fields_by_name['name']._options = None
  _RERUNCONNECTIVITYTESTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _REACHABILITYSERVICE._options = None
  _REACHABILITYSERVICE._serialized_options = b'\312A networkmanagement.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _REACHABILITYSERVICE.methods_by_name['ListConnectivityTests']._options = None
  _REACHABILITYSERVICE.methods_by_name['ListConnectivityTests']._serialized_options = b'\332A\006parent\202\323\344\223\002<\022:/v1/{parent=projects/*/locations/global}/connectivityTests'
  _REACHABILITYSERVICE.methods_by_name['GetConnectivityTest']._options = None
  _REACHABILITYSERVICE.methods_by_name['GetConnectivityTest']._serialized_options = b'\332A\004name\202\323\344\223\002<\022:/v1/{name=projects/*/locations/global/connectivityTests/*}'
  _REACHABILITYSERVICE.methods_by_name['CreateConnectivityTest']._options = None
  _REACHABILITYSERVICE.methods_by_name['CreateConnectivityTest']._serialized_options = b'\312AG\n2google.cloud.networkmanagement.v1.ConnectivityTest\022\021OperationMetadata\332A\027parent,test_id,resource\202\323\344\223\002F\":/v1/{parent=projects/*/locations/global}/connectivityTests:\010resource'
  _REACHABILITYSERVICE.methods_by_name['UpdateConnectivityTest']._options = None
  _REACHABILITYSERVICE.methods_by_name['UpdateConnectivityTest']._serialized_options = b'\312AG\n2google.cloud.networkmanagement.v1.ConnectivityTest\022\021OperationMetadata\332A\024update_mask,resource\202\323\344\223\002O2C/v1/{resource.name=projects/*/locations/global/connectivityTests/*}:\010resource'
  _REACHABILITYSERVICE.methods_by_name['RerunConnectivityTest']._options = None
  _REACHABILITYSERVICE.methods_by_name['RerunConnectivityTest']._serialized_options = b'\312AG\n2google.cloud.networkmanagement.v1.ConnectivityTest\022\021OperationMetadata\202\323\344\223\002E\"@/v1/{name=projects/*/locations/global/connectivityTests/*}:rerun:\001*'
  _REACHABILITYSERVICE.methods_by_name['DeleteConnectivityTest']._options = None
  _REACHABILITYSERVICE.methods_by_name['DeleteConnectivityTest']._serialized_options = b'\312A*\n\025google.protobuf.Empty\022\021OperationMetadata\332A\004name\202\323\344\223\002<*:/v1/{name=projects/*/locations/global/connectivityTests/*}'
  _LISTCONNECTIVITYTESTSREQUEST._serialized_start=370
  _LISTCONNECTIVITYTESTSREQUEST._serialized_end=541
  _LISTCONNECTIVITYTESTSRESPONSE._serialized_start=544
  _LISTCONNECTIVITYTESTSRESPONSE._serialized_end=732
  _GETCONNECTIVITYTESTREQUEST._serialized_start=734
  _GETCONNECTIVITYTESTREQUEST._serialized_end=788
  _CREATECONNECTIVITYTESTREQUEST._serialized_start=791
  _CREATECONNECTIVITYTESTREQUEST._serialized_end=970
  _UPDATECONNECTIVITYTESTREQUEST._serialized_start=973
  _UPDATECONNECTIVITYTESTREQUEST._serialized_end=1158
  _DELETECONNECTIVITYTESTREQUEST._serialized_start=1160
  _DELETECONNECTIVITYTESTREQUEST._serialized_end=1217
  _RERUNCONNECTIVITYTESTREQUEST._serialized_start=1219
  _RERUNCONNECTIVITYTESTREQUEST._serialized_end=1275
  _OPERATIONMETADATA._serialized_start=1278
  _OPERATIONMETADATA._serialized_end=1570
  _REACHABILITYSERVICE._serialized_start=1573
  _REACHABILITYSERVICE._serialized_end=3259
# @@protoc_insertion_point(module_scope)
