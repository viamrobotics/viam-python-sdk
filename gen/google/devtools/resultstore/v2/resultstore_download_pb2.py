# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/resultstore/v2/resultstore_download.proto
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
from google.devtools.resultstore.v2 import action_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_action__pb2
from google.devtools.resultstore.v2 import configuration_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_configuration__pb2
from google.devtools.resultstore.v2 import configured_target_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_configured__target__pb2
from google.devtools.resultstore.v2 import download_metadata_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_download__metadata__pb2
from google.devtools.resultstore.v2 import file_set_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__set__pb2
from google.devtools.resultstore.v2 import invocation_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_invocation__pb2
from google.devtools.resultstore.v2 import target_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_target__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/devtools/resultstore/v2/resultstore_download.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/action.proto\x1a\x32google/devtools/resultstore/v2/configuration.proto\x1a\x36google/devtools/resultstore/v2/configured_target.proto\x1a\x36google/devtools/resultstore/v2/download_metadata.proto\x1a-google/devtools/resultstore/v2/file_set.proto\x1a/google/devtools/resultstore/v2/invocation.proto\x1a+google/devtools/resultstore/v2/target.proto\"Z\n\x14GetInvocationRequest\x12\x42\n\x04name\x18\x01 \x01(\tB.\xe2\x41\x01\x02\xfa\x41\'\n%resultstore.googleapis.com/InvocationR\x04name\"\xd6\x01\n\x18SearchInvocationsRequest\x12\x1b\n\tpage_size\x18\x01 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x02 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x03 \x01(\x03H\x00R\x06offset\x12\x14\n\x05query\x18\x04 \x01(\tR\x05query\x12\x1d\n\nproject_id\x18\x05 \x01(\tR\tprojectId\x12\x1f\n\x0b\x65xact_match\x18\x07 \x01(\x08R\nexactMatchB\x0c\n\npage_start\"\x91\x01\n\x19SearchInvocationsResponse\x12L\n\x0binvocations\x18\x01 \x03(\x0b\x32*.google.devtools.resultstore.v2.InvocationR\x0binvocations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xc3\x01\n\x17\x45xportInvocationRequest\x12\x42\n\x04name\x18\x01 \x01(\tB.\xe2\x41\x01\x02\xfa\x41\'\n%resultstore.googleapis.com/InvocationR\x04name\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x03 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x04 \x01(\x03H\x00R\x06offsetB\x0c\n\npage_start\"\x90\x04\n\x18\x45xportInvocationResponse\x12J\n\ninvocation\x18\x01 \x01(\x0b\x32*.google.devtools.resultstore.v2.InvocationR\ninvocation\x12@\n\x07targets\x18\x02 \x03(\x0b\x32&.google.devtools.resultstore.v2.TargetR\x07targets\x12U\n\x0e\x63onfigurations\x18\x03 \x03(\x0b\x32-.google.devtools.resultstore.v2.ConfigurationR\x0e\x63onfigurations\x12_\n\x12\x63onfigured_targets\x18\x04 \x03(\x0b\x32\x30.google.devtools.resultstore.v2.ConfiguredTargetR\x11\x63onfiguredTargets\x12@\n\x07\x61\x63tions\x18\x05 \x03(\x0b\x32&.google.devtools.resultstore.v2.ActionR\x07\x61\x63tions\x12\x44\n\tfile_sets\x18\x06 \x03(\x0b\x32\'.google.devtools.resultstore.v2.FileSetR\x08\x66ileSets\x12&\n\x0fnext_page_token\x18\x07 \x01(\tR\rnextPageToken\"p\n$GetInvocationDownloadMetadataRequest\x12H\n\x04name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+resultstore.googleapis.com/DownloadMetadataR\x04name\"`\n\x17GetConfigurationRequest\x12\x45\n\x04name\x18\x01 \x01(\tB1\xe2\x41\x01\x02\xfa\x41*\n(resultstore.googleapis.com/ConfigurationR\x04name\"\xe1\x01\n\x19ListConfigurationsRequest\x12\x46\n\x06parent\x18\x01 \x01(\tB.\xe2\x41\x01\x02\xfa\x41\'\n%resultstore.googleapis.com/InvocationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x03 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x04 \x01(\x03H\x00R\x06offset\x12\x16\n\x06\x66ilter\x18\x05 \x01(\tR\x06\x66ilterB\x0c\n\npage_start\"\x9b\x01\n\x1aListConfigurationsResponse\x12U\n\x0e\x63onfigurations\x18\x01 \x03(\x0b\x32-.google.devtools.resultstore.v2.ConfigurationR\x0e\x63onfigurations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"R\n\x10GetTargetRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!resultstore.googleapis.com/TargetR\x04name\"\xda\x01\n\x12ListTargetsRequest\x12\x46\n\x06parent\x18\x01 \x01(\tB.\xe2\x41\x01\x02\xfa\x41\'\n%resultstore.googleapis.com/InvocationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x03 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x04 \x01(\x03H\x00R\x06offset\x12\x16\n\x06\x66ilter\x18\x05 \x01(\tR\x06\x66ilterB\x0c\n\npage_start\"\x7f\n\x13ListTargetsResponse\x12@\n\x07targets\x18\x01 \x03(\x0b\x32&.google.devtools.resultstore.v2.TargetR\x07targets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"f\n\x1aGetConfiguredTargetRequest\x12H\n\x04name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+resultstore.googleapis.com/ConfiguredTargetR\x04name\"\xe0\x01\n\x1cListConfiguredTargetsRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!resultstore.googleapis.com/TargetR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x03 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x04 \x01(\x03H\x00R\x06offset\x12\x16\n\x06\x66ilter\x18\x05 \x01(\tR\x06\x66ilterB\x0c\n\npage_start\"\xa8\x01\n\x1dListConfiguredTargetsResponse\x12_\n\x12\x63onfigured_targets\x18\x01 \x03(\x0b\x32\x30.google.devtools.resultstore.v2.ConfiguredTargetR\x11\x63onfiguredTargets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xa0\x02\n\x1eSearchConfiguredTargetsRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!resultstore.googleapis.com/TargetR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x03 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x04 \x01(\x03H\x00R\x06offset\x12\x14\n\x05query\x18\x05 \x01(\tR\x05query\x12\x1d\n\nproject_id\x18\x06 \x01(\tR\tprojectId\x12\x1f\n\x0b\x65xact_match\x18\x07 \x01(\x08R\nexactMatchB\x0c\n\npage_start\"\xaa\x01\n\x1fSearchConfiguredTargetsResponse\x12_\n\x12\x63onfigured_targets\x18\x01 \x03(\x0b\x32\x30.google.devtools.resultstore.v2.ConfiguredTargetR\x11\x63onfiguredTargets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"R\n\x10GetActionRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!resultstore.googleapis.com/ActionR\x04name\"\xe0\x01\n\x12ListActionsRequest\x12L\n\x06parent\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+resultstore.googleapis.com/ConfiguredTargetR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x03 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x04 \x01(\x03H\x00R\x06offset\x12\x16\n\x06\x66ilter\x18\x05 \x01(\tR\x06\x66ilterB\x0c\n\npage_start\"\x7f\n\x13ListActionsResponse\x12@\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32&.google.devtools.resultstore.v2.ActionR\x07\x61\x63tions\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\x8e\x02\n\x17\x42\x61tchListActionsRequest\x12\x46\n\x06parent\x18\x01 \x01(\tB.\xe2\x41\x01\x02\xfa\x41\'\n%resultstore.googleapis.com/InvocationR\x06parent\x12-\n\x12\x63onfigured_targets\x18\x02 \x03(\tR\x11\x63onfiguredTargets\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x04 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x05 \x01(\x03H\x00R\x06offset\x12\x16\n\x06\x66ilter\x18\x06 \x01(\tR\x06\x66ilterB\x0c\n\npage_start\"\xa1\x01\n\x18\x42\x61tchListActionsResponse\x12@\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32&.google.devtools.resultstore.v2.ActionR\x07\x61\x63tions\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1b\n\tnot_found\x18\x03 \x03(\tR\x08notFound\"T\n\x11GetFileSetRequest\x12?\n\x04name\x18\x01 \x01(\tB+\xe2\x41\x01\x02\xfa\x41$\n\"resultstore.googleapis.com/FileSetR\x04name\"\xdb\x01\n\x13ListFileSetsRequest\x12\x46\n\x06parent\x18\x01 \x01(\tB.\xe2\x41\x01\x02\xfa\x41\'\n%resultstore.googleapis.com/InvocationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x03 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x04 \x01(\x03H\x00R\x06offset\x12\x16\n\x06\x66ilter\x18\x05 \x01(\tR\x06\x66ilterB\x0c\n\npage_start\"\x84\x01\n\x14ListFileSetsResponse\x12\x44\n\tfile_sets\x18\x01 \x03(\x0b\x32\'.google.devtools.resultstore.v2.FileSetR\x08\x66ileSets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\x9f\x01\n\x17TraverseFileSetsRequest\x12\x1e\n\x04name\x18\x01 \x01(\tB\n\xe2\x41\x01\x02\xfa\x41\x03\n\x01*R\x04name\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1f\n\npage_token\x18\x03 \x01(\tH\x00R\tpageToken\x12\x18\n\x06offset\x18\x04 \x01(\x03H\x00R\x06offsetB\x0c\n\npage_start\"\x88\x01\n\x18TraverseFileSetsResponse\x12\x44\n\tfile_sets\x18\x01 \x03(\x0b\x32\'.google.devtools.resultstore.v2.FileSetR\x08\x66ileSets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken2\xb3\x1a\n\x13ResultStoreDownload\x12\x9a\x01\n\rGetInvocation\x12\x34.google.devtools.resultstore.v2.GetInvocationRequest\x1a*.google.devtools.resultstore.v2.Invocation\"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v2/{name=invocations/*}\x12\xa8\x01\n\x11SearchInvocations\x12\x38.google.devtools.resultstore.v2.SearchInvocationsRequest\x1a\x39.google.devtools.resultstore.v2.SearchInvocationsResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v2/invocations:search\x12\xb1\x01\n\x10\x45xportInvocation\x12\x37.google.devtools.resultstore.v2.ExportInvocationRequest\x1a\x38.google.devtools.resultstore.v2.ExportInvocationResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/v2/{name=invocations/*}:export:\x01*\x12\xd1\x01\n\x1dGetInvocationDownloadMetadata\x12\x44.google.devtools.resultstore.v2.GetInvocationDownloadMetadataRequest\x1a\x30.google.devtools.resultstore.v2.DownloadMetadata\"8\xda\x41\x04name\x82\xd3\xe4\x93\x02+\x12)/v2/{name=invocations/*/downloadMetadata}\x12\xad\x01\n\x10GetConfiguration\x12\x37.google.devtools.resultstore.v2.GetConfigurationRequest\x1a-.google.devtools.resultstore.v2.Configuration\"1\xda\x41\x04name\x82\xd3\xe4\x93\x02$\x12\"/v2/{name=invocations/*/configs/*}\x12\xc0\x01\n\x12ListConfigurations\x12\x39.google.devtools.resultstore.v2.ListConfigurationsRequest\x1a:.google.devtools.resultstore.v2.ListConfigurationsResponse\"3\xda\x41\x06parent\x82\xd3\xe4\x93\x02$\x12\"/v2/{parent=invocations/*}/configs\x12\x98\x01\n\tGetTarget\x12\x30.google.devtools.resultstore.v2.GetTargetRequest\x1a&.google.devtools.resultstore.v2.Target\"1\xda\x41\x04name\x82\xd3\xe4\x93\x02$\x12\"/v2/{name=invocations/*/targets/*}\x12\xab\x01\n\x0bListTargets\x12\x32.google.devtools.resultstore.v2.ListTargetsRequest\x1a\x33.google.devtools.resultstore.v2.ListTargetsResponse\"3\xda\x41\x06parent\x82\xd3\xe4\x93\x02$\x12\"/v2/{parent=invocations/*}/targets\x12\xca\x01\n\x13GetConfiguredTarget\x12:.google.devtools.resultstore.v2.GetConfiguredTargetRequest\x1a\x30.google.devtools.resultstore.v2.ConfiguredTarget\"E\xda\x41\x04name\x82\xd3\xe4\x93\x02\x38\x12\x36/v2/{name=invocations/*/targets/*/configuredTargets/*}\x12\xdd\x01\n\x15ListConfiguredTargets\x12<.google.devtools.resultstore.v2.ListConfiguredTargetsRequest\x1a=.google.devtools.resultstore.v2.ListConfiguredTargetsResponse\"G\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x38\x12\x36/v2/{parent=invocations/*/targets/*}/configuredTargets\x12\xe1\x01\n\x17SearchConfiguredTargets\x12>.google.devtools.resultstore.v2.SearchConfiguredTargetsRequest\x1a?.google.devtools.resultstore.v2.SearchConfiguredTargetsResponse\"E\x82\xd3\xe4\x93\x02?\x12=/v2/{parent=invocations/*/targets/*}/configuredTargets:search\x12\xb6\x01\n\tGetAction\x12\x30.google.devtools.resultstore.v2.GetActionRequest\x1a&.google.devtools.resultstore.v2.Action\"O\xda\x41\x04name\x82\xd3\xe4\x93\x02\x42\x12@/v2/{name=invocations/*/targets/*/configuredTargets/*/actions/*}\x12\xc9\x01\n\x0bListActions\x12\x32.google.devtools.resultstore.v2.ListActionsRequest\x1a\x33.google.devtools.resultstore.v2.ListActionsResponse\"Q\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x42\x12@/v2/{parent=invocations/*/targets/*/configuredTargets/*}/actions\x12\xbb\x01\n\x10\x42\x61tchListActions\x12\x37.google.devtools.resultstore.v2.BatchListActionsRequest\x1a\x38.google.devtools.resultstore.v2.BatchListActionsResponse\"4\x82\xd3\xe4\x93\x02.\x12,/v2/{parent=invocations/*}/actions:batchList\x12\x9c\x01\n\nGetFileSet\x12\x31.google.devtools.resultstore.v2.GetFileSetRequest\x1a\'.google.devtools.resultstore.v2.FileSet\"2\xda\x41\x04name\x82\xd3\xe4\x93\x02%\x12#/v2/{name=invocations/*/fileSets/*}\x12\xaf\x01\n\x0cListFileSets\x12\x33.google.devtools.resultstore.v2.ListFileSetsRequest\x1a\x34.google.devtools.resultstore.v2.ListFileSetsResponse\"4\xda\x41\x06parent\x82\xd3\xe4\x93\x02%\x12#/v2/{parent=invocations/*}/fileSets\x12\x9a\x02\n\x10TraverseFileSets\x12\x37.google.devtools.resultstore.v2.TraverseFileSetsRequest\x1a\x38.google.devtools.resultstore.v2.TraverseFileSetsResponse\"\x92\x01\x82\xd3\xe4\x93\x02\x8b\x01\x12\x34/v2/{name=invocations/*/fileSets/*}:traverseFileSetsZS\x12Q/v2/{name=invocations/*/targets/*/configuredTargets/*/actions/*}:traverseFileSets\x1aN\xca\x41\x1aresultstore.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x8b\x01\n\"com.google.devtools.resultstore.v2B\x18ResultStoreDownloadProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')



_GETINVOCATIONREQUEST = DESCRIPTOR.message_types_by_name['GetInvocationRequest']
_SEARCHINVOCATIONSREQUEST = DESCRIPTOR.message_types_by_name['SearchInvocationsRequest']
_SEARCHINVOCATIONSRESPONSE = DESCRIPTOR.message_types_by_name['SearchInvocationsResponse']
_EXPORTINVOCATIONREQUEST = DESCRIPTOR.message_types_by_name['ExportInvocationRequest']
_EXPORTINVOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['ExportInvocationResponse']
_GETINVOCATIONDOWNLOADMETADATAREQUEST = DESCRIPTOR.message_types_by_name['GetInvocationDownloadMetadataRequest']
_GETCONFIGURATIONREQUEST = DESCRIPTOR.message_types_by_name['GetConfigurationRequest']
_LISTCONFIGURATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListConfigurationsRequest']
_LISTCONFIGURATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListConfigurationsResponse']
_GETTARGETREQUEST = DESCRIPTOR.message_types_by_name['GetTargetRequest']
_LISTTARGETSREQUEST = DESCRIPTOR.message_types_by_name['ListTargetsRequest']
_LISTTARGETSRESPONSE = DESCRIPTOR.message_types_by_name['ListTargetsResponse']
_GETCONFIGUREDTARGETREQUEST = DESCRIPTOR.message_types_by_name['GetConfiguredTargetRequest']
_LISTCONFIGUREDTARGETSREQUEST = DESCRIPTOR.message_types_by_name['ListConfiguredTargetsRequest']
_LISTCONFIGUREDTARGETSRESPONSE = DESCRIPTOR.message_types_by_name['ListConfiguredTargetsResponse']
_SEARCHCONFIGUREDTARGETSREQUEST = DESCRIPTOR.message_types_by_name['SearchConfiguredTargetsRequest']
_SEARCHCONFIGUREDTARGETSRESPONSE = DESCRIPTOR.message_types_by_name['SearchConfiguredTargetsResponse']
_GETACTIONREQUEST = DESCRIPTOR.message_types_by_name['GetActionRequest']
_LISTACTIONSREQUEST = DESCRIPTOR.message_types_by_name['ListActionsRequest']
_LISTACTIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListActionsResponse']
_BATCHLISTACTIONSREQUEST = DESCRIPTOR.message_types_by_name['BatchListActionsRequest']
_BATCHLISTACTIONSRESPONSE = DESCRIPTOR.message_types_by_name['BatchListActionsResponse']
_GETFILESETREQUEST = DESCRIPTOR.message_types_by_name['GetFileSetRequest']
_LISTFILESETSREQUEST = DESCRIPTOR.message_types_by_name['ListFileSetsRequest']
_LISTFILESETSRESPONSE = DESCRIPTOR.message_types_by_name['ListFileSetsResponse']
_TRAVERSEFILESETSREQUEST = DESCRIPTOR.message_types_by_name['TraverseFileSetsRequest']
_TRAVERSEFILESETSRESPONSE = DESCRIPTOR.message_types_by_name['TraverseFileSetsResponse']
GetInvocationRequest = _reflection.GeneratedProtocolMessageType('GetInvocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINVOCATIONREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.GetInvocationRequest)
  })
_sym_db.RegisterMessage(GetInvocationRequest)

SearchInvocationsRequest = _reflection.GeneratedProtocolMessageType('SearchInvocationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHINVOCATIONSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.SearchInvocationsRequest)
  })
_sym_db.RegisterMessage(SearchInvocationsRequest)

SearchInvocationsResponse = _reflection.GeneratedProtocolMessageType('SearchInvocationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHINVOCATIONSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.SearchInvocationsResponse)
  })
_sym_db.RegisterMessage(SearchInvocationsResponse)

ExportInvocationRequest = _reflection.GeneratedProtocolMessageType('ExportInvocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTINVOCATIONREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ExportInvocationRequest)
  })
_sym_db.RegisterMessage(ExportInvocationRequest)

ExportInvocationResponse = _reflection.GeneratedProtocolMessageType('ExportInvocationResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTINVOCATIONRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ExportInvocationResponse)
  })
_sym_db.RegisterMessage(ExportInvocationResponse)

GetInvocationDownloadMetadataRequest = _reflection.GeneratedProtocolMessageType('GetInvocationDownloadMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINVOCATIONDOWNLOADMETADATAREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.GetInvocationDownloadMetadataRequest)
  })
_sym_db.RegisterMessage(GetInvocationDownloadMetadataRequest)

GetConfigurationRequest = _reflection.GeneratedProtocolMessageType('GetConfigurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONFIGURATIONREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.GetConfigurationRequest)
  })
_sym_db.RegisterMessage(GetConfigurationRequest)

ListConfigurationsRequest = _reflection.GeneratedProtocolMessageType('ListConfigurationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONFIGURATIONSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListConfigurationsRequest)
  })
_sym_db.RegisterMessage(ListConfigurationsRequest)

ListConfigurationsResponse = _reflection.GeneratedProtocolMessageType('ListConfigurationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONFIGURATIONSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListConfigurationsResponse)
  })
_sym_db.RegisterMessage(ListConfigurationsResponse)

GetTargetRequest = _reflection.GeneratedProtocolMessageType('GetTargetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTARGETREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.GetTargetRequest)
  })
_sym_db.RegisterMessage(GetTargetRequest)

ListTargetsRequest = _reflection.GeneratedProtocolMessageType('ListTargetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGETSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListTargetsRequest)
  })
_sym_db.RegisterMessage(ListTargetsRequest)

ListTargetsResponse = _reflection.GeneratedProtocolMessageType('ListTargetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGETSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListTargetsResponse)
  })
_sym_db.RegisterMessage(ListTargetsResponse)

GetConfiguredTargetRequest = _reflection.GeneratedProtocolMessageType('GetConfiguredTargetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONFIGUREDTARGETREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.GetConfiguredTargetRequest)
  })
_sym_db.RegisterMessage(GetConfiguredTargetRequest)

ListConfiguredTargetsRequest = _reflection.GeneratedProtocolMessageType('ListConfiguredTargetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONFIGUREDTARGETSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListConfiguredTargetsRequest)
  })
_sym_db.RegisterMessage(ListConfiguredTargetsRequest)

ListConfiguredTargetsResponse = _reflection.GeneratedProtocolMessageType('ListConfiguredTargetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONFIGUREDTARGETSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListConfiguredTargetsResponse)
  })
_sym_db.RegisterMessage(ListConfiguredTargetsResponse)

SearchConfiguredTargetsRequest = _reflection.GeneratedProtocolMessageType('SearchConfiguredTargetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHCONFIGUREDTARGETSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.SearchConfiguredTargetsRequest)
  })
_sym_db.RegisterMessage(SearchConfiguredTargetsRequest)

SearchConfiguredTargetsResponse = _reflection.GeneratedProtocolMessageType('SearchConfiguredTargetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHCONFIGUREDTARGETSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.SearchConfiguredTargetsResponse)
  })
_sym_db.RegisterMessage(SearchConfiguredTargetsResponse)

GetActionRequest = _reflection.GeneratedProtocolMessageType('GetActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIONREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.GetActionRequest)
  })
_sym_db.RegisterMessage(GetActionRequest)

ListActionsRequest = _reflection.GeneratedProtocolMessageType('ListActionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTACTIONSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListActionsRequest)
  })
_sym_db.RegisterMessage(ListActionsRequest)

ListActionsResponse = _reflection.GeneratedProtocolMessageType('ListActionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTACTIONSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListActionsResponse)
  })
_sym_db.RegisterMessage(ListActionsResponse)

BatchListActionsRequest = _reflection.GeneratedProtocolMessageType('BatchListActionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHLISTACTIONSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.BatchListActionsRequest)
  })
_sym_db.RegisterMessage(BatchListActionsRequest)

BatchListActionsResponse = _reflection.GeneratedProtocolMessageType('BatchListActionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHLISTACTIONSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.BatchListActionsResponse)
  })
_sym_db.RegisterMessage(BatchListActionsResponse)

GetFileSetRequest = _reflection.GeneratedProtocolMessageType('GetFileSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFILESETREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.GetFileSetRequest)
  })
_sym_db.RegisterMessage(GetFileSetRequest)

ListFileSetsRequest = _reflection.GeneratedProtocolMessageType('ListFileSetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESETSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListFileSetsRequest)
  })
_sym_db.RegisterMessage(ListFileSetsRequest)

ListFileSetsResponse = _reflection.GeneratedProtocolMessageType('ListFileSetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESETSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ListFileSetsResponse)
  })
_sym_db.RegisterMessage(ListFileSetsResponse)

TraverseFileSetsRequest = _reflection.GeneratedProtocolMessageType('TraverseFileSetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAVERSEFILESETSREQUEST,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.TraverseFileSetsRequest)
  })
_sym_db.RegisterMessage(TraverseFileSetsRequest)

TraverseFileSetsResponse = _reflection.GeneratedProtocolMessageType('TraverseFileSetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAVERSEFILESETSRESPONSE,
  '__module__' : 'google.devtools.resultstore.v2.resultstore_download_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.TraverseFileSetsResponse)
  })
_sym_db.RegisterMessage(TraverseFileSetsResponse)

_RESULTSTOREDOWNLOAD = DESCRIPTOR.services_by_name['ResultStoreDownload']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.devtools.resultstore.v2B\030ResultStoreDownloadProtoP\001ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
  _GETINVOCATIONREQUEST.fields_by_name['name']._options = None
  _GETINVOCATIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\'\n%resultstore.googleapis.com/Invocation'
  _EXPORTINVOCATIONREQUEST.fields_by_name['name']._options = None
  _EXPORTINVOCATIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\'\n%resultstore.googleapis.com/Invocation'
  _GETINVOCATIONDOWNLOADMETADATAREQUEST.fields_by_name['name']._options = None
  _GETINVOCATIONDOWNLOADMETADATAREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A-\n+resultstore.googleapis.com/DownloadMetadata'
  _GETCONFIGURATIONREQUEST.fields_by_name['name']._options = None
  _GETCONFIGURATIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A*\n(resultstore.googleapis.com/Configuration'
  _LISTCONFIGURATIONSREQUEST.fields_by_name['parent']._options = None
  _LISTCONFIGURATIONSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\'\n%resultstore.googleapis.com/Invocation'
  _GETTARGETREQUEST.fields_by_name['name']._options = None
  _GETTARGETREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A#\n!resultstore.googleapis.com/Target'
  _LISTTARGETSREQUEST.fields_by_name['parent']._options = None
  _LISTTARGETSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\'\n%resultstore.googleapis.com/Invocation'
  _GETCONFIGUREDTARGETREQUEST.fields_by_name['name']._options = None
  _GETCONFIGUREDTARGETREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A-\n+resultstore.googleapis.com/ConfiguredTarget'
  _LISTCONFIGUREDTARGETSREQUEST.fields_by_name['parent']._options = None
  _LISTCONFIGUREDTARGETSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!resultstore.googleapis.com/Target'
  _SEARCHCONFIGUREDTARGETSREQUEST.fields_by_name['parent']._options = None
  _SEARCHCONFIGUREDTARGETSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!resultstore.googleapis.com/Target'
  _GETACTIONREQUEST.fields_by_name['name']._options = None
  _GETACTIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A#\n!resultstore.googleapis.com/Action'
  _LISTACTIONSREQUEST.fields_by_name['parent']._options = None
  _LISTACTIONSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A-\n+resultstore.googleapis.com/ConfiguredTarget'
  _BATCHLISTACTIONSREQUEST.fields_by_name['parent']._options = None
  _BATCHLISTACTIONSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\'\n%resultstore.googleapis.com/Invocation'
  _GETFILESETREQUEST.fields_by_name['name']._options = None
  _GETFILESETREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A$\n\"resultstore.googleapis.com/FileSet'
  _LISTFILESETSREQUEST.fields_by_name['parent']._options = None
  _LISTFILESETSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\'\n%resultstore.googleapis.com/Invocation'
  _TRAVERSEFILESETSREQUEST.fields_by_name['name']._options = None
  _TRAVERSEFILESETSREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\003\n\001*'
  _RESULTSTOREDOWNLOAD._options = None
  _RESULTSTOREDOWNLOAD._serialized_options = b'\312A\032resultstore.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _RESULTSTOREDOWNLOAD.methods_by_name['GetInvocation']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['GetInvocation']._serialized_options = b'\332A\004name\202\323\344\223\002\032\022\030/v2/{name=invocations/*}'
  _RESULTSTOREDOWNLOAD.methods_by_name['SearchInvocations']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['SearchInvocations']._serialized_options = b'\202\323\344\223\002\030\022\026/v2/invocations:search'
  _RESULTSTOREDOWNLOAD.methods_by_name['ExportInvocation']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['ExportInvocation']._serialized_options = b'\202\323\344\223\002$\"\037/v2/{name=invocations/*}:export:\001*'
  _RESULTSTOREDOWNLOAD.methods_by_name['GetInvocationDownloadMetadata']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['GetInvocationDownloadMetadata']._serialized_options = b'\332A\004name\202\323\344\223\002+\022)/v2/{name=invocations/*/downloadMetadata}'
  _RESULTSTOREDOWNLOAD.methods_by_name['GetConfiguration']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['GetConfiguration']._serialized_options = b'\332A\004name\202\323\344\223\002$\022\"/v2/{name=invocations/*/configs/*}'
  _RESULTSTOREDOWNLOAD.methods_by_name['ListConfigurations']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['ListConfigurations']._serialized_options = b'\332A\006parent\202\323\344\223\002$\022\"/v2/{parent=invocations/*}/configs'
  _RESULTSTOREDOWNLOAD.methods_by_name['GetTarget']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['GetTarget']._serialized_options = b'\332A\004name\202\323\344\223\002$\022\"/v2/{name=invocations/*/targets/*}'
  _RESULTSTOREDOWNLOAD.methods_by_name['ListTargets']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['ListTargets']._serialized_options = b'\332A\006parent\202\323\344\223\002$\022\"/v2/{parent=invocations/*}/targets'
  _RESULTSTOREDOWNLOAD.methods_by_name['GetConfiguredTarget']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['GetConfiguredTarget']._serialized_options = b'\332A\004name\202\323\344\223\0028\0226/v2/{name=invocations/*/targets/*/configuredTargets/*}'
  _RESULTSTOREDOWNLOAD.methods_by_name['ListConfiguredTargets']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['ListConfiguredTargets']._serialized_options = b'\332A\006parent\202\323\344\223\0028\0226/v2/{parent=invocations/*/targets/*}/configuredTargets'
  _RESULTSTOREDOWNLOAD.methods_by_name['SearchConfiguredTargets']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['SearchConfiguredTargets']._serialized_options = b'\202\323\344\223\002?\022=/v2/{parent=invocations/*/targets/*}/configuredTargets:search'
  _RESULTSTOREDOWNLOAD.methods_by_name['GetAction']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['GetAction']._serialized_options = b'\332A\004name\202\323\344\223\002B\022@/v2/{name=invocations/*/targets/*/configuredTargets/*/actions/*}'
  _RESULTSTOREDOWNLOAD.methods_by_name['ListActions']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['ListActions']._serialized_options = b'\332A\006parent\202\323\344\223\002B\022@/v2/{parent=invocations/*/targets/*/configuredTargets/*}/actions'
  _RESULTSTOREDOWNLOAD.methods_by_name['BatchListActions']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['BatchListActions']._serialized_options = b'\202\323\344\223\002.\022,/v2/{parent=invocations/*}/actions:batchList'
  _RESULTSTOREDOWNLOAD.methods_by_name['GetFileSet']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['GetFileSet']._serialized_options = b'\332A\004name\202\323\344\223\002%\022#/v2/{name=invocations/*/fileSets/*}'
  _RESULTSTOREDOWNLOAD.methods_by_name['ListFileSets']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['ListFileSets']._serialized_options = b'\332A\006parent\202\323\344\223\002%\022#/v2/{parent=invocations/*}/fileSets'
  _RESULTSTOREDOWNLOAD.methods_by_name['TraverseFileSets']._options = None
  _RESULTSTOREDOWNLOAD.methods_by_name['TraverseFileSets']._serialized_options = b'\202\323\344\223\002\213\001\0224/v2/{name=invocations/*/fileSets/*}:traverseFileSetsZS\022Q/v2/{name=invocations/*/targets/*/configuredTargets/*/actions/*}:traverseFileSets'
  _GETINVOCATIONREQUEST._serialized_start=558
  _GETINVOCATIONREQUEST._serialized_end=648
  _SEARCHINVOCATIONSREQUEST._serialized_start=651
  _SEARCHINVOCATIONSREQUEST._serialized_end=865
  _SEARCHINVOCATIONSRESPONSE._serialized_start=868
  _SEARCHINVOCATIONSRESPONSE._serialized_end=1013
  _EXPORTINVOCATIONREQUEST._serialized_start=1016
  _EXPORTINVOCATIONREQUEST._serialized_end=1211
  _EXPORTINVOCATIONRESPONSE._serialized_start=1214
  _EXPORTINVOCATIONRESPONSE._serialized_end=1742
  _GETINVOCATIONDOWNLOADMETADATAREQUEST._serialized_start=1744
  _GETINVOCATIONDOWNLOADMETADATAREQUEST._serialized_end=1856
  _GETCONFIGURATIONREQUEST._serialized_start=1858
  _GETCONFIGURATIONREQUEST._serialized_end=1954
  _LISTCONFIGURATIONSREQUEST._serialized_start=1957
  _LISTCONFIGURATIONSREQUEST._serialized_end=2182
  _LISTCONFIGURATIONSRESPONSE._serialized_start=2185
  _LISTCONFIGURATIONSRESPONSE._serialized_end=2340
  _GETTARGETREQUEST._serialized_start=2342
  _GETTARGETREQUEST._serialized_end=2424
  _LISTTARGETSREQUEST._serialized_start=2427
  _LISTTARGETSREQUEST._serialized_end=2645
  _LISTTARGETSRESPONSE._serialized_start=2647
  _LISTTARGETSRESPONSE._serialized_end=2774
  _GETCONFIGUREDTARGETREQUEST._serialized_start=2776
  _GETCONFIGUREDTARGETREQUEST._serialized_end=2878
  _LISTCONFIGUREDTARGETSREQUEST._serialized_start=2881
  _LISTCONFIGUREDTARGETSREQUEST._serialized_end=3105
  _LISTCONFIGUREDTARGETSRESPONSE._serialized_start=3108
  _LISTCONFIGUREDTARGETSRESPONSE._serialized_end=3276
  _SEARCHCONFIGUREDTARGETSREQUEST._serialized_start=3279
  _SEARCHCONFIGUREDTARGETSREQUEST._serialized_end=3567
  _SEARCHCONFIGUREDTARGETSRESPONSE._serialized_start=3570
  _SEARCHCONFIGUREDTARGETSRESPONSE._serialized_end=3740
  _GETACTIONREQUEST._serialized_start=3742
  _GETACTIONREQUEST._serialized_end=3824
  _LISTACTIONSREQUEST._serialized_start=3827
  _LISTACTIONSREQUEST._serialized_end=4051
  _LISTACTIONSRESPONSE._serialized_start=4053
  _LISTACTIONSRESPONSE._serialized_end=4180
  _BATCHLISTACTIONSREQUEST._serialized_start=4183
  _BATCHLISTACTIONSREQUEST._serialized_end=4453
  _BATCHLISTACTIONSRESPONSE._serialized_start=4456
  _BATCHLISTACTIONSRESPONSE._serialized_end=4617
  _GETFILESETREQUEST._serialized_start=4619
  _GETFILESETREQUEST._serialized_end=4703
  _LISTFILESETSREQUEST._serialized_start=4706
  _LISTFILESETSREQUEST._serialized_end=4925
  _LISTFILESETSRESPONSE._serialized_start=4928
  _LISTFILESETSRESPONSE._serialized_end=5060
  _TRAVERSEFILESETSREQUEST._serialized_start=5063
  _TRAVERSEFILESETSREQUEST._serialized_end=5222
  _TRAVERSEFILESETSRESPONSE._serialized_start=5225
  _TRAVERSEFILESETSRESPONSE._serialized_end=5361
  _RESULTSTOREDOWNLOAD._serialized_start=5364
  _RESULTSTOREDOWNLOAD._serialized_end=8743
# @@protoc_insertion_point(module_scope)
