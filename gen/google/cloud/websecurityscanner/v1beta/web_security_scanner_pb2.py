# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner/v1beta/web_security_scanner.proto
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
from google.cloud.websecurityscanner.v1beta import crawled_url_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_crawled__url__pb2
from google.cloud.websecurityscanner.v1beta import finding_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_finding__pb2
from google.cloud.websecurityscanner.v1beta import finding_type_stats_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_finding__type__stats__pb2
from google.cloud.websecurityscanner.v1beta import scan_config_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__config__pb2
from google.cloud.websecurityscanner.v1beta import scan_run_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/websecurityscanner/v1beta/web_security_scanner.proto\x12&google.cloud.websecurityscanner.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x38google/cloud/websecurityscanner/v1beta/crawled_url.proto\x1a\x34google/cloud/websecurityscanner/v1beta/finding.proto\x1a?google/cloud/websecurityscanner/v1beta/finding_type_stats.proto\x1a\x38google/cloud/websecurityscanner/v1beta/scan_config.proto\x1a\x35google/cloud/websecurityscanner/v1beta/scan_run.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"\xc2\x01\n\x17\x43reateScanConfigRequest\x12L\n\x06parent\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+cloudresourcemanager.googleapis.com/ProjectR\x06parent\x12Y\n\x0bscan_config\x18\x02 \x01(\x0b\x32\x32.google.cloud.websecurityscanner.v1beta.ScanConfigB\x04\xe2\x41\x01\x02R\nscanConfig\"d\n\x17\x44\x65leteScanConfigRequest\x12I\n\x04name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,websecurityscanner.googleapis.com/ScanConfigR\x04name\"a\n\x14GetScanConfigRequest\x12I\n\x04name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,websecurityscanner.googleapis.com/ScanConfigR\x04name\"\xa2\x01\n\x16ListScanConfigsRequest\x12L\n\x06parent\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+cloudresourcemanager.googleapis.com/ProjectR\x06parent\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\"\xb7\x01\n\x17UpdateScanConfigRequest\x12Y\n\x0bscan_config\x18\x02 \x01(\x0b\x32\x32.google.cloud.websecurityscanner.v1beta.ScanConfigB\x04\xe2\x41\x01\x02R\nscanConfig\x12\x41\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"\x98\x01\n\x17ListScanConfigsResponse\x12U\n\x0cscan_configs\x18\x01 \x03(\x0b\x32\x32.google.cloud.websecurityscanner.v1beta.ScanConfigR\x0bscanConfigs\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"`\n\x13StartScanRunRequest\x12I\n\x04name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,websecurityscanner.googleapis.com/ScanConfigR\x04name\"[\n\x11GetScanRunRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)websecurityscanner.googleapis.com/ScanRunR\x04name\"\xa0\x01\n\x13ListScanRunsRequest\x12M\n\x06parent\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,websecurityscanner.googleapis.com/ScanConfigR\x06parent\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\"\x8c\x01\n\x14ListScanRunsResponse\x12L\n\tscan_runs\x18\x01 \x03(\x0b\x32/.google.cloud.websecurityscanner.v1beta.ScanRunR\x08scanRuns\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\\\n\x12StopScanRunRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)websecurityscanner.googleapis.com/ScanRunR\x04name\"\xa0\x01\n\x16ListCrawledUrlsRequest\x12J\n\x06parent\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)websecurityscanner.googleapis.com/ScanRunR\x06parent\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\"\x98\x01\n\x17ListCrawledUrlsResponse\x12U\n\x0c\x63rawled_urls\x18\x01 \x03(\x0b\x32\x32.google.cloud.websecurityscanner.v1beta.CrawledUrlR\x0b\x63rawledUrls\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"[\n\x11GetFindingRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)websecurityscanner.googleapis.com/FindingR\x04name\"\xbb\x01\n\x13ListFindingsRequest\x12J\n\x06parent\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)websecurityscanner.googleapis.com/ScanRunR\x06parent\x12\x1c\n\x06\x66ilter\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x06\x66ilter\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x04 \x01(\x05R\x08pageSize\"\x8b\x01\n\x14ListFindingsResponse\x12K\n\x08\x66indings\x18\x01 \x03(\x0b\x32/.google.cloud.websecurityscanner.v1beta.FindingR\x08\x66indings\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"i\n\x1bListFindingTypeStatsRequest\x12J\n\x06parent\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)websecurityscanner.googleapis.com/ScanRunR\x06parent\"\x86\x01\n\x1cListFindingTypeStatsResponse\x12\x66\n\x12\x66inding_type_stats\x18\x01 \x03(\x0b\x32\x38.google.cloud.websecurityscanner.v1beta.FindingTypeStatsR\x10\x66indingTypeStats2\x8e\x16\n\x12WebSecurityScanner\x12\xda\x01\n\x10\x43reateScanConfig\x12?.google.cloud.websecurityscanner.v1beta.CreateScanConfigRequest\x1a\x32.google.cloud.websecurityscanner.v1beta.ScanConfig\"Q\xda\x41\x12parent,scan_config\x82\xd3\xe4\x93\x02\x36\"\'/v1beta/{parent=projects/*}/scanConfigs:\x0bscan_config\x12\xa3\x01\n\x10\x44\x65leteScanConfig\x12?.google.cloud.websecurityscanner.v1beta.DeleteScanConfigRequest\x1a\x16.google.protobuf.Empty\"6\xda\x41\x04name\x82\xd3\xe4\x93\x02)*\'/v1beta/{name=projects/*/scanConfigs/*}\x12\xb9\x01\n\rGetScanConfig\x12<.google.cloud.websecurityscanner.v1beta.GetScanConfigRequest\x1a\x32.google.cloud.websecurityscanner.v1beta.ScanConfig\"6\xda\x41\x04name\x82\xd3\xe4\x93\x02)\x12\'/v1beta/{name=projects/*/scanConfigs/*}\x12\xcc\x01\n\x0fListScanConfigs\x12>.google.cloud.websecurityscanner.v1beta.ListScanConfigsRequest\x1a?.google.cloud.websecurityscanner.v1beta.ListScanConfigsResponse\"8\xda\x41\x06parent\x82\xd3\xe4\x93\x02)\x12\'/v1beta/{parent=projects/*}/scanConfigs\x12\xeb\x01\n\x10UpdateScanConfig\x12?.google.cloud.websecurityscanner.v1beta.UpdateScanConfigRequest\x1a\x32.google.cloud.websecurityscanner.v1beta.ScanConfig\"b\xda\x41\x17scan_config,update_mask\x82\xd3\xe4\x93\x02\x42\x32\x33/v1beta/{scan_config.name=projects/*/scanConfigs/*}:\x0bscan_config\x12\xbd\x01\n\x0cStartScanRun\x12;.google.cloud.websecurityscanner.v1beta.StartScanRunRequest\x1a/.google.cloud.websecurityscanner.v1beta.ScanRun\"?\xda\x41\x04name\x82\xd3\xe4\x93\x02\x32\"-/v1beta/{name=projects/*/scanConfigs/*}:start:\x01*\x12\xbb\x01\n\nGetScanRun\x12\x39.google.cloud.websecurityscanner.v1beta.GetScanRunRequest\x1a/.google.cloud.websecurityscanner.v1beta.ScanRun\"A\xda\x41\x04name\x82\xd3\xe4\x93\x02\x34\x12\x32/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}\x12\xce\x01\n\x0cListScanRuns\x12;.google.cloud.websecurityscanner.v1beta.ListScanRunsRequest\x1a<.google.cloud.websecurityscanner.v1beta.ListScanRunsResponse\"C\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x34\x12\x32/v1beta/{parent=projects/*/scanConfigs/*}/scanRuns\x12\xc5\x01\n\x0bStopScanRun\x12:.google.cloud.websecurityscanner.v1beta.StopScanRunRequest\x1a/.google.cloud.websecurityscanner.v1beta.ScanRun\"I\xda\x41\x04name\x82\xd3\xe4\x93\x02<\"7/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}:stop:\x01*\x12\xe5\x01\n\x0fListCrawledUrls\x12>.google.cloud.websecurityscanner.v1beta.ListCrawledUrlsRequest\x1a?.google.cloud.websecurityscanner.v1beta.ListCrawledUrlsResponse\"Q\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x42\x12@/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls\x12\xc6\x01\n\nGetFinding\x12\x39.google.cloud.websecurityscanner.v1beta.GetFindingRequest\x1a/.google.cloud.websecurityscanner.v1beta.Finding\"L\xda\x41\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}\x12\xe0\x01\n\x0cListFindings\x12;.google.cloud.websecurityscanner.v1beta.ListFindingsRequest\x1a<.google.cloud.websecurityscanner.v1beta.ListFindingsResponse\"U\xda\x41\rparent,filter\x82\xd3\xe4\x93\x02?\x12=/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings\x12\xf9\x01\n\x14ListFindingTypeStats\x12\x43.google.cloud.websecurityscanner.v1beta.ListFindingTypeStatsRequest\x1a\x44.google.cloud.websecurityscanner.v1beta.ListFindingTypeStatsResponse\"V\xda\x41\x06parent\x82\xd3\xe4\x93\x02G\x12\x45/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats\x1aU\xca\x41!websecurityscanner.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x9f\x02\n*com.google.cloud.websecurityscanner.v1betaB\x17WebSecurityScannerProtoP\x01ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3')



_CREATESCANCONFIGREQUEST = DESCRIPTOR.message_types_by_name['CreateScanConfigRequest']
_DELETESCANCONFIGREQUEST = DESCRIPTOR.message_types_by_name['DeleteScanConfigRequest']
_GETSCANCONFIGREQUEST = DESCRIPTOR.message_types_by_name['GetScanConfigRequest']
_LISTSCANCONFIGSREQUEST = DESCRIPTOR.message_types_by_name['ListScanConfigsRequest']
_UPDATESCANCONFIGREQUEST = DESCRIPTOR.message_types_by_name['UpdateScanConfigRequest']
_LISTSCANCONFIGSRESPONSE = DESCRIPTOR.message_types_by_name['ListScanConfigsResponse']
_STARTSCANRUNREQUEST = DESCRIPTOR.message_types_by_name['StartScanRunRequest']
_GETSCANRUNREQUEST = DESCRIPTOR.message_types_by_name['GetScanRunRequest']
_LISTSCANRUNSREQUEST = DESCRIPTOR.message_types_by_name['ListScanRunsRequest']
_LISTSCANRUNSRESPONSE = DESCRIPTOR.message_types_by_name['ListScanRunsResponse']
_STOPSCANRUNREQUEST = DESCRIPTOR.message_types_by_name['StopScanRunRequest']
_LISTCRAWLEDURLSREQUEST = DESCRIPTOR.message_types_by_name['ListCrawledUrlsRequest']
_LISTCRAWLEDURLSRESPONSE = DESCRIPTOR.message_types_by_name['ListCrawledUrlsResponse']
_GETFINDINGREQUEST = DESCRIPTOR.message_types_by_name['GetFindingRequest']
_LISTFINDINGSREQUEST = DESCRIPTOR.message_types_by_name['ListFindingsRequest']
_LISTFINDINGSRESPONSE = DESCRIPTOR.message_types_by_name['ListFindingsResponse']
_LISTFINDINGTYPESTATSREQUEST = DESCRIPTOR.message_types_by_name['ListFindingTypeStatsRequest']
_LISTFINDINGTYPESTATSRESPONSE = DESCRIPTOR.message_types_by_name['ListFindingTypeStatsResponse']
CreateScanConfigRequest = _reflection.GeneratedProtocolMessageType('CreateScanConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESCANCONFIGREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.CreateScanConfigRequest)
  })
_sym_db.RegisterMessage(CreateScanConfigRequest)

DeleteScanConfigRequest = _reflection.GeneratedProtocolMessageType('DeleteScanConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESCANCONFIGREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.DeleteScanConfigRequest)
  })
_sym_db.RegisterMessage(DeleteScanConfigRequest)

GetScanConfigRequest = _reflection.GeneratedProtocolMessageType('GetScanConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSCANCONFIGREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.GetScanConfigRequest)
  })
_sym_db.RegisterMessage(GetScanConfigRequest)

ListScanConfigsRequest = _reflection.GeneratedProtocolMessageType('ListScanConfigsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSCANCONFIGSREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListScanConfigsRequest)
  })
_sym_db.RegisterMessage(ListScanConfigsRequest)

UpdateScanConfigRequest = _reflection.GeneratedProtocolMessageType('UpdateScanConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESCANCONFIGREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.UpdateScanConfigRequest)
  })
_sym_db.RegisterMessage(UpdateScanConfigRequest)

ListScanConfigsResponse = _reflection.GeneratedProtocolMessageType('ListScanConfigsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSCANCONFIGSRESPONSE,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListScanConfigsResponse)
  })
_sym_db.RegisterMessage(ListScanConfigsResponse)

StartScanRunRequest = _reflection.GeneratedProtocolMessageType('StartScanRunRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTSCANRUNREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.StartScanRunRequest)
  })
_sym_db.RegisterMessage(StartScanRunRequest)

GetScanRunRequest = _reflection.GeneratedProtocolMessageType('GetScanRunRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSCANRUNREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.GetScanRunRequest)
  })
_sym_db.RegisterMessage(GetScanRunRequest)

ListScanRunsRequest = _reflection.GeneratedProtocolMessageType('ListScanRunsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSCANRUNSREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListScanRunsRequest)
  })
_sym_db.RegisterMessage(ListScanRunsRequest)

ListScanRunsResponse = _reflection.GeneratedProtocolMessageType('ListScanRunsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSCANRUNSRESPONSE,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListScanRunsResponse)
  })
_sym_db.RegisterMessage(ListScanRunsResponse)

StopScanRunRequest = _reflection.GeneratedProtocolMessageType('StopScanRunRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPSCANRUNREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.StopScanRunRequest)
  })
_sym_db.RegisterMessage(StopScanRunRequest)

ListCrawledUrlsRequest = _reflection.GeneratedProtocolMessageType('ListCrawledUrlsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCRAWLEDURLSREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListCrawledUrlsRequest)
  })
_sym_db.RegisterMessage(ListCrawledUrlsRequest)

ListCrawledUrlsResponse = _reflection.GeneratedProtocolMessageType('ListCrawledUrlsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCRAWLEDURLSRESPONSE,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListCrawledUrlsResponse)
  })
_sym_db.RegisterMessage(ListCrawledUrlsResponse)

GetFindingRequest = _reflection.GeneratedProtocolMessageType('GetFindingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFINDINGREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.GetFindingRequest)
  })
_sym_db.RegisterMessage(GetFindingRequest)

ListFindingsRequest = _reflection.GeneratedProtocolMessageType('ListFindingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFINDINGSREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListFindingsRequest)
  })
_sym_db.RegisterMessage(ListFindingsRequest)

ListFindingsResponse = _reflection.GeneratedProtocolMessageType('ListFindingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFINDINGSRESPONSE,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListFindingsResponse)
  })
_sym_db.RegisterMessage(ListFindingsResponse)

ListFindingTypeStatsRequest = _reflection.GeneratedProtocolMessageType('ListFindingTypeStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFINDINGTYPESTATSREQUEST,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListFindingTypeStatsRequest)
  })
_sym_db.RegisterMessage(ListFindingTypeStatsRequest)

ListFindingTypeStatsResponse = _reflection.GeneratedProtocolMessageType('ListFindingTypeStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFINDINGTYPESTATSRESPONSE,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ListFindingTypeStatsResponse)
  })
_sym_db.RegisterMessage(ListFindingTypeStatsResponse)

_WEBSECURITYSCANNER = DESCRIPTOR.services_by_name['WebSecurityScanner']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*com.google.cloud.websecurityscanner.v1betaB\027WebSecurityScannerProtoP\001ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\252\002&Google.Cloud.WebSecurityScanner.V1Beta\312\002&Google\\Cloud\\WebSecurityScanner\\V1beta\352\002)Google::Cloud::WebSecurityScanner::V1beta'
  _CREATESCANCONFIGREQUEST.fields_by_name['parent']._options = None
  _CREATESCANCONFIGREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A-\n+cloudresourcemanager.googleapis.com/Project'
  _CREATESCANCONFIGREQUEST.fields_by_name['scan_config']._options = None
  _CREATESCANCONFIGREQUEST.fields_by_name['scan_config']._serialized_options = b'\342A\001\002'
  _DELETESCANCONFIGREQUEST.fields_by_name['name']._options = None
  _DELETESCANCONFIGREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A.\n,websecurityscanner.googleapis.com/ScanConfig'
  _GETSCANCONFIGREQUEST.fields_by_name['name']._options = None
  _GETSCANCONFIGREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A.\n,websecurityscanner.googleapis.com/ScanConfig'
  _LISTSCANCONFIGSREQUEST.fields_by_name['parent']._options = None
  _LISTSCANCONFIGSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A-\n+cloudresourcemanager.googleapis.com/Project'
  _UPDATESCANCONFIGREQUEST.fields_by_name['scan_config']._options = None
  _UPDATESCANCONFIGREQUEST.fields_by_name['scan_config']._serialized_options = b'\342A\001\002'
  _UPDATESCANCONFIGREQUEST.fields_by_name['update_mask']._options = None
  _UPDATESCANCONFIGREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _STARTSCANRUNREQUEST.fields_by_name['name']._options = None
  _STARTSCANRUNREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A.\n,websecurityscanner.googleapis.com/ScanConfig'
  _GETSCANRUNREQUEST.fields_by_name['name']._options = None
  _GETSCANRUNREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A+\n)websecurityscanner.googleapis.com/ScanRun'
  _LISTSCANRUNSREQUEST.fields_by_name['parent']._options = None
  _LISTSCANRUNSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A.\n,websecurityscanner.googleapis.com/ScanConfig'
  _STOPSCANRUNREQUEST.fields_by_name['name']._options = None
  _STOPSCANRUNREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A+\n)websecurityscanner.googleapis.com/ScanRun'
  _LISTCRAWLEDURLSREQUEST.fields_by_name['parent']._options = None
  _LISTCRAWLEDURLSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A+\n)websecurityscanner.googleapis.com/ScanRun'
  _GETFINDINGREQUEST.fields_by_name['name']._options = None
  _GETFINDINGREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A+\n)websecurityscanner.googleapis.com/Finding'
  _LISTFINDINGSREQUEST.fields_by_name['parent']._options = None
  _LISTFINDINGSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A+\n)websecurityscanner.googleapis.com/ScanRun'
  _LISTFINDINGSREQUEST.fields_by_name['filter']._options = None
  _LISTFINDINGSREQUEST.fields_by_name['filter']._serialized_options = b'\342A\001\002'
  _LISTFINDINGTYPESTATSREQUEST.fields_by_name['parent']._options = None
  _LISTFINDINGTYPESTATSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A+\n)websecurityscanner.googleapis.com/ScanRun'
  _WEBSECURITYSCANNER._options = None
  _WEBSECURITYSCANNER._serialized_options = b'\312A!websecurityscanner.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _WEBSECURITYSCANNER.methods_by_name['CreateScanConfig']._options = None
  _WEBSECURITYSCANNER.methods_by_name['CreateScanConfig']._serialized_options = b'\332A\022parent,scan_config\202\323\344\223\0026\"\'/v1beta/{parent=projects/*}/scanConfigs:\013scan_config'
  _WEBSECURITYSCANNER.methods_by_name['DeleteScanConfig']._options = None
  _WEBSECURITYSCANNER.methods_by_name['DeleteScanConfig']._serialized_options = b'\332A\004name\202\323\344\223\002)*\'/v1beta/{name=projects/*/scanConfigs/*}'
  _WEBSECURITYSCANNER.methods_by_name['GetScanConfig']._options = None
  _WEBSECURITYSCANNER.methods_by_name['GetScanConfig']._serialized_options = b'\332A\004name\202\323\344\223\002)\022\'/v1beta/{name=projects/*/scanConfigs/*}'
  _WEBSECURITYSCANNER.methods_by_name['ListScanConfigs']._options = None
  _WEBSECURITYSCANNER.methods_by_name['ListScanConfigs']._serialized_options = b'\332A\006parent\202\323\344\223\002)\022\'/v1beta/{parent=projects/*}/scanConfigs'
  _WEBSECURITYSCANNER.methods_by_name['UpdateScanConfig']._options = None
  _WEBSECURITYSCANNER.methods_by_name['UpdateScanConfig']._serialized_options = b'\332A\027scan_config,update_mask\202\323\344\223\002B23/v1beta/{scan_config.name=projects/*/scanConfigs/*}:\013scan_config'
  _WEBSECURITYSCANNER.methods_by_name['StartScanRun']._options = None
  _WEBSECURITYSCANNER.methods_by_name['StartScanRun']._serialized_options = b'\332A\004name\202\323\344\223\0022\"-/v1beta/{name=projects/*/scanConfigs/*}:start:\001*'
  _WEBSECURITYSCANNER.methods_by_name['GetScanRun']._options = None
  _WEBSECURITYSCANNER.methods_by_name['GetScanRun']._serialized_options = b'\332A\004name\202\323\344\223\0024\0222/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}'
  _WEBSECURITYSCANNER.methods_by_name['ListScanRuns']._options = None
  _WEBSECURITYSCANNER.methods_by_name['ListScanRuns']._serialized_options = b'\332A\006parent\202\323\344\223\0024\0222/v1beta/{parent=projects/*/scanConfigs/*}/scanRuns'
  _WEBSECURITYSCANNER.methods_by_name['StopScanRun']._options = None
  _WEBSECURITYSCANNER.methods_by_name['StopScanRun']._serialized_options = b'\332A\004name\202\323\344\223\002<\"7/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}:stop:\001*'
  _WEBSECURITYSCANNER.methods_by_name['ListCrawledUrls']._options = None
  _WEBSECURITYSCANNER.methods_by_name['ListCrawledUrls']._serialized_options = b'\332A\006parent\202\323\344\223\002B\022@/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls'
  _WEBSECURITYSCANNER.methods_by_name['GetFinding']._options = None
  _WEBSECURITYSCANNER.methods_by_name['GetFinding']._serialized_options = b'\332A\004name\202\323\344\223\002?\022=/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}'
  _WEBSECURITYSCANNER.methods_by_name['ListFindings']._options = None
  _WEBSECURITYSCANNER.methods_by_name['ListFindings']._serialized_options = b'\332A\rparent,filter\202\323\344\223\002?\022=/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings'
  _WEBSECURITYSCANNER.methods_by_name['ListFindingTypeStats']._options = None
  _WEBSECURITYSCANNER.methods_by_name['ListFindingTypeStats']._serialized_options = b'\332A\006parent\202\323\344\223\002G\022E/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats'
  _CREATESCANCONFIGREQUEST._serialized_start=578
  _CREATESCANCONFIGREQUEST._serialized_end=772
  _DELETESCANCONFIGREQUEST._serialized_start=774
  _DELETESCANCONFIGREQUEST._serialized_end=874
  _GETSCANCONFIGREQUEST._serialized_start=876
  _GETSCANCONFIGREQUEST._serialized_end=973
  _LISTSCANCONFIGSREQUEST._serialized_start=976
  _LISTSCANCONFIGSREQUEST._serialized_end=1138
  _UPDATESCANCONFIGREQUEST._serialized_start=1141
  _UPDATESCANCONFIGREQUEST._serialized_end=1324
  _LISTSCANCONFIGSRESPONSE._serialized_start=1327
  _LISTSCANCONFIGSRESPONSE._serialized_end=1479
  _STARTSCANRUNREQUEST._serialized_start=1481
  _STARTSCANRUNREQUEST._serialized_end=1577
  _GETSCANRUNREQUEST._serialized_start=1579
  _GETSCANRUNREQUEST._serialized_end=1670
  _LISTSCANRUNSREQUEST._serialized_start=1673
  _LISTSCANRUNSREQUEST._serialized_end=1833
  _LISTSCANRUNSRESPONSE._serialized_start=1836
  _LISTSCANRUNSRESPONSE._serialized_end=1976
  _STOPSCANRUNREQUEST._serialized_start=1978
  _STOPSCANRUNREQUEST._serialized_end=2070
  _LISTCRAWLEDURLSREQUEST._serialized_start=2073
  _LISTCRAWLEDURLSREQUEST._serialized_end=2233
  _LISTCRAWLEDURLSRESPONSE._serialized_start=2236
  _LISTCRAWLEDURLSRESPONSE._serialized_end=2388
  _GETFINDINGREQUEST._serialized_start=2390
  _GETFINDINGREQUEST._serialized_end=2481
  _LISTFINDINGSREQUEST._serialized_start=2484
  _LISTFINDINGSREQUEST._serialized_end=2671
  _LISTFINDINGSRESPONSE._serialized_start=2674
  _LISTFINDINGSRESPONSE._serialized_end=2813
  _LISTFINDINGTYPESTATSREQUEST._serialized_start=2815
  _LISTFINDINGTYPESTATSREQUEST._serialized_end=2920
  _LISTFINDINGTYPESTATSRESPONSE._serialized_start=2923
  _LISTFINDINGTYPESTATSRESPONSE._serialized_end=3057
  _WEBSECURITYSCANNER._serialized_start=3060
  _WEBSECURITYSCANNER._serialized_end=5890
# @@protoc_insertion_point(module_scope)
