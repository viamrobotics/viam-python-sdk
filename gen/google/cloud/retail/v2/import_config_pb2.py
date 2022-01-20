# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/retail/v2/import_config.proto
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
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.retail.v2 import product_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_product__pb2
from google.cloud.retail.v2 import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_user__event__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/retail/v2/import_config.proto\x12\x16google.cloud.retail.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/retail/v2/product.proto\x1a\'google/cloud/retail/v2/user_event.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/date.proto\"Q\n\tGcsSource\x12#\n\ninput_uris\x18\x01 \x03(\tB\x04\xe2\x41\x01\x02R\tinputUris\x12\x1f\n\x0b\x64\x61ta_schema\x18\x02 \x01(\tR\ndataSchema\"\x87\x02\n\x0e\x42igQuerySource\x12:\n\x0epartition_date\x18\x06 \x01(\x0b\x32\x11.google.type.DateH\x00R\rpartitionDate\x12\x1d\n\nproject_id\x18\x05 \x01(\tR\tprojectId\x12#\n\ndataset_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tdatasetId\x12\x1f\n\x08table_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x07tableId\x12&\n\x0fgcs_staging_dir\x18\x03 \x01(\tR\rgcsStagingDir\x12\x1f\n\x0b\x64\x61ta_schema\x18\x04 \x01(\tR\ndataSchemaB\x0b\n\tpartition\"X\n\x13ProductInlineSource\x12\x41\n\x08products\x18\x01 \x03(\x0b\x32\x1f.google.cloud.retail.v2.ProductB\x04\xe2\x41\x01\x02R\x08products\"a\n\x15UserEventInlineSource\x12H\n\x0buser_events\x18\x01 \x03(\x0b\x32!.google.cloud.retail.v2.UserEventB\x04\xe2\x41\x01\x02R\nuserEvents\"D\n\x12ImportErrorsConfig\x12\x1f\n\ngcs_prefix\x18\x01 \x01(\tH\x00R\tgcsPrefixB\r\n\x0b\x64\x65stination\"\xdd\x04\n\x15ImportProductsRequest\x12=\n\x06parent\x18\x01 \x01(\tB%\xe2\x41\x01\x02\xfa\x41\x1e\n\x1cretail.googleapis.com/BranchR\x06parent\x12\x1d\n\nrequest_id\x18\x06 \x01(\tR\trequestId\x12S\n\x0cinput_config\x18\x02 \x01(\x0b\x32*.google.cloud.retail.v2.ProductInputConfigB\x04\xe2\x41\x01\x02R\x0binputConfig\x12O\n\rerrors_config\x18\x03 \x01(\x0b\x32*.google.cloud.retail.v2.ImportErrorsConfigR\x0c\x65rrorsConfig\x12;\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12q\n\x13reconciliation_mode\x18\x05 \x01(\x0e\x32@.google.cloud.retail.v2.ImportProductsRequest.ReconciliationModeR\x12reconciliationMode\x12:\n\x19notification_pubsub_topic\x18\x07 \x01(\tR\x17notificationPubsubTopic\"T\n\x12ReconciliationMode\x12#\n\x1fRECONCILIATION_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINCREMENTAL\x10\x01\x12\x08\n\x04\x46ULL\x10\x02\"\x81\x02\n\x17ImportUserEventsRequest\x12>\n\x06parent\x18\x01 \x01(\tB&\xe2\x41\x01\x02\xfa\x41\x1f\n\x1dretail.googleapis.com/CatalogR\x06parent\x12U\n\x0cinput_config\x18\x02 \x01(\x0b\x32,.google.cloud.retail.v2.UserEventInputConfigB\x04\xe2\x41\x01\x02R\x0binputConfig\x12O\n\rerrors_config\x18\x03 \x01(\x0b\x32*.google.cloud.retail.v2.ImportErrorsConfigR\x0c\x65rrorsConfig\"\xf5\x01\n\x1bImportCompletionDataRequest\x12>\n\x06parent\x18\x01 \x01(\tB&\xe2\x41\x01\x02\xfa\x41\x1f\n\x1dretail.googleapis.com/CatalogR\x06parent\x12Z\n\x0cinput_config\x18\x02 \x01(\x0b\x32\x31.google.cloud.retail.v2.CompletionDataInputConfigB\x04\xe2\x41\x01\x02R\x0binputConfig\x12:\n\x19notification_pubsub_topic\x18\x03 \x01(\tR\x17notificationPubsubTopic\"\x99\x02\n\x12ProductInputConfig\x12\x61\n\x15product_inline_source\x18\x01 \x01(\x0b\x32+.google.cloud.retail.v2.ProductInlineSourceH\x00R\x13productInlineSource\x12\x42\n\ngcs_source\x18\x02 \x01(\x0b\x32!.google.cloud.retail.v2.GcsSourceH\x00R\tgcsSource\x12R\n\x10\x62ig_query_source\x18\x03 \x01(\x0b\x32&.google.cloud.retail.v2.BigQuerySourceH\x00R\x0e\x62igQuerySourceB\x08\n\x06source\"\xb4\x02\n\x14UserEventInputConfig\x12n\n\x18user_event_inline_source\x18\x01 \x01(\x0b\x32-.google.cloud.retail.v2.UserEventInlineSourceB\x04\xe2\x41\x01\x02H\x00R\x15userEventInlineSource\x12H\n\ngcs_source\x18\x02 \x01(\x0b\x32!.google.cloud.retail.v2.GcsSourceB\x04\xe2\x41\x01\x02H\x00R\tgcsSource\x12X\n\x10\x62ig_query_source\x18\x03 \x01(\x0b\x32&.google.cloud.retail.v2.BigQuerySourceB\x04\xe2\x41\x01\x02H\x00R\x0e\x62igQuerySourceB\x08\n\x06source\"\x7f\n\x19\x43ompletionDataInputConfig\x12X\n\x10\x62ig_query_source\x18\x01 \x01(\x0b\x32&.google.cloud.retail.v2.BigQuerySourceB\x04\xe2\x41\x01\x02H\x00R\x0e\x62igQuerySourceB\x08\n\x06source\"\xaf\x02\n\x0eImportMetadata\x12;\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12#\n\rsuccess_count\x18\x03 \x01(\x03R\x0csuccessCount\x12#\n\rfailure_count\x18\x04 \x01(\x03R\x0c\x66\x61ilureCount\x12\x1d\n\nrequest_id\x18\x05 \x01(\tR\trequestId\x12:\n\x19notification_pubsub_topic\x18\x06 \x01(\tR\x17notificationPubsubTopic\"\xa2\x01\n\x16ImportProductsResponse\x12\x37\n\rerror_samples\x18\x01 \x03(\x0b\x32\x12.google.rpc.StatusR\x0c\x65rrorSamples\x12O\n\rerrors_config\x18\x02 \x01(\x0b\x32*.google.cloud.retail.v2.ImportErrorsConfigR\x0c\x65rrorsConfig\"\xfb\x01\n\x18ImportUserEventsResponse\x12\x37\n\rerror_samples\x18\x01 \x03(\x0b\x32\x12.google.rpc.StatusR\x0c\x65rrorSamples\x12O\n\rerrors_config\x18\x02 \x01(\x0b\x32*.google.cloud.retail.v2.ImportErrorsConfigR\x0c\x65rrorsConfig\x12U\n\x0eimport_summary\x18\x03 \x01(\x0b\x32..google.cloud.retail.v2.UserEventImportSummaryR\rimportSummary\"|\n\x16UserEventImportSummary\x12.\n\x13joined_events_count\x18\x01 \x01(\x03R\x11joinedEventsCount\x12\x32\n\x15unjoined_events_count\x18\x02 \x01(\x03R\x13unjoinedEventsCount\"W\n\x1cImportCompletionDataResponse\x12\x37\n\rerror_samples\x18\x01 \x03(\x0b\x32\x12.google.rpc.StatusR\x0c\x65rrorSamplesB\xc6\x01\n\x1a\x63om.google.cloud.retail.v2B\x11ImportConfigProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/retail/v2;retail\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')



_GCSSOURCE = DESCRIPTOR.message_types_by_name['GcsSource']
_BIGQUERYSOURCE = DESCRIPTOR.message_types_by_name['BigQuerySource']
_PRODUCTINLINESOURCE = DESCRIPTOR.message_types_by_name['ProductInlineSource']
_USEREVENTINLINESOURCE = DESCRIPTOR.message_types_by_name['UserEventInlineSource']
_IMPORTERRORSCONFIG = DESCRIPTOR.message_types_by_name['ImportErrorsConfig']
_IMPORTPRODUCTSREQUEST = DESCRIPTOR.message_types_by_name['ImportProductsRequest']
_IMPORTUSEREVENTSREQUEST = DESCRIPTOR.message_types_by_name['ImportUserEventsRequest']
_IMPORTCOMPLETIONDATAREQUEST = DESCRIPTOR.message_types_by_name['ImportCompletionDataRequest']
_PRODUCTINPUTCONFIG = DESCRIPTOR.message_types_by_name['ProductInputConfig']
_USEREVENTINPUTCONFIG = DESCRIPTOR.message_types_by_name['UserEventInputConfig']
_COMPLETIONDATAINPUTCONFIG = DESCRIPTOR.message_types_by_name['CompletionDataInputConfig']
_IMPORTMETADATA = DESCRIPTOR.message_types_by_name['ImportMetadata']
_IMPORTPRODUCTSRESPONSE = DESCRIPTOR.message_types_by_name['ImportProductsResponse']
_IMPORTUSEREVENTSRESPONSE = DESCRIPTOR.message_types_by_name['ImportUserEventsResponse']
_USEREVENTIMPORTSUMMARY = DESCRIPTOR.message_types_by_name['UserEventImportSummary']
_IMPORTCOMPLETIONDATARESPONSE = DESCRIPTOR.message_types_by_name['ImportCompletionDataResponse']
_IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE = _IMPORTPRODUCTSREQUEST.enum_types_by_name['ReconciliationMode']
GcsSource = _reflection.GeneratedProtocolMessageType('GcsSource', (_message.Message,), {
  'DESCRIPTOR' : _GCSSOURCE,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.GcsSource)
  })
_sym_db.RegisterMessage(GcsSource)

BigQuerySource = _reflection.GeneratedProtocolMessageType('BigQuerySource', (_message.Message,), {
  'DESCRIPTOR' : _BIGQUERYSOURCE,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.BigQuerySource)
  })
_sym_db.RegisterMessage(BigQuerySource)

ProductInlineSource = _reflection.GeneratedProtocolMessageType('ProductInlineSource', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTINLINESOURCE,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ProductInlineSource)
  })
_sym_db.RegisterMessage(ProductInlineSource)

UserEventInlineSource = _reflection.GeneratedProtocolMessageType('UserEventInlineSource', (_message.Message,), {
  'DESCRIPTOR' : _USEREVENTINLINESOURCE,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.UserEventInlineSource)
  })
_sym_db.RegisterMessage(UserEventInlineSource)

ImportErrorsConfig = _reflection.GeneratedProtocolMessageType('ImportErrorsConfig', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTERRORSCONFIG,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ImportErrorsConfig)
  })
_sym_db.RegisterMessage(ImportErrorsConfig)

ImportProductsRequest = _reflection.GeneratedProtocolMessageType('ImportProductsRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTPRODUCTSREQUEST,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ImportProductsRequest)
  })
_sym_db.RegisterMessage(ImportProductsRequest)

ImportUserEventsRequest = _reflection.GeneratedProtocolMessageType('ImportUserEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTUSEREVENTSREQUEST,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ImportUserEventsRequest)
  })
_sym_db.RegisterMessage(ImportUserEventsRequest)

ImportCompletionDataRequest = _reflection.GeneratedProtocolMessageType('ImportCompletionDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTCOMPLETIONDATAREQUEST,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ImportCompletionDataRequest)
  })
_sym_db.RegisterMessage(ImportCompletionDataRequest)

ProductInputConfig = _reflection.GeneratedProtocolMessageType('ProductInputConfig', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTINPUTCONFIG,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ProductInputConfig)
  })
_sym_db.RegisterMessage(ProductInputConfig)

UserEventInputConfig = _reflection.GeneratedProtocolMessageType('UserEventInputConfig', (_message.Message,), {
  'DESCRIPTOR' : _USEREVENTINPUTCONFIG,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.UserEventInputConfig)
  })
_sym_db.RegisterMessage(UserEventInputConfig)

CompletionDataInputConfig = _reflection.GeneratedProtocolMessageType('CompletionDataInputConfig', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETIONDATAINPUTCONFIG,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.CompletionDataInputConfig)
  })
_sym_db.RegisterMessage(CompletionDataInputConfig)

ImportMetadata = _reflection.GeneratedProtocolMessageType('ImportMetadata', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTMETADATA,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ImportMetadata)
  })
_sym_db.RegisterMessage(ImportMetadata)

ImportProductsResponse = _reflection.GeneratedProtocolMessageType('ImportProductsResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTPRODUCTSRESPONSE,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ImportProductsResponse)
  })
_sym_db.RegisterMessage(ImportProductsResponse)

ImportUserEventsResponse = _reflection.GeneratedProtocolMessageType('ImportUserEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTUSEREVENTSRESPONSE,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ImportUserEventsResponse)
  })
_sym_db.RegisterMessage(ImportUserEventsResponse)

UserEventImportSummary = _reflection.GeneratedProtocolMessageType('UserEventImportSummary', (_message.Message,), {
  'DESCRIPTOR' : _USEREVENTIMPORTSUMMARY,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.UserEventImportSummary)
  })
_sym_db.RegisterMessage(UserEventImportSummary)

ImportCompletionDataResponse = _reflection.GeneratedProtocolMessageType('ImportCompletionDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTCOMPLETIONDATARESPONSE,
  '__module__' : 'google.cloud.retail.v2.import_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2.ImportCompletionDataResponse)
  })
_sym_db.RegisterMessage(ImportCompletionDataResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.google.cloud.retail.v2B\021ImportConfigProtoP\001Z<google.golang.org/genproto/googleapis/cloud/retail/v2;retail\242\002\006RETAIL\252\002\026Google.Cloud.Retail.V2\312\002\026Google\\Cloud\\Retail\\V2\352\002\031Google::Cloud::Retail::V2'
  _GCSSOURCE.fields_by_name['input_uris']._options = None
  _GCSSOURCE.fields_by_name['input_uris']._serialized_options = b'\342A\001\002'
  _BIGQUERYSOURCE.fields_by_name['dataset_id']._options = None
  _BIGQUERYSOURCE.fields_by_name['dataset_id']._serialized_options = b'\342A\001\002'
  _BIGQUERYSOURCE.fields_by_name['table_id']._options = None
  _BIGQUERYSOURCE.fields_by_name['table_id']._serialized_options = b'\342A\001\002'
  _PRODUCTINLINESOURCE.fields_by_name['products']._options = None
  _PRODUCTINLINESOURCE.fields_by_name['products']._serialized_options = b'\342A\001\002'
  _USEREVENTINLINESOURCE.fields_by_name['user_events']._options = None
  _USEREVENTINLINESOURCE.fields_by_name['user_events']._serialized_options = b'\342A\001\002'
  _IMPORTPRODUCTSREQUEST.fields_by_name['parent']._options = None
  _IMPORTPRODUCTSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\036\n\034retail.googleapis.com/Branch'
  _IMPORTPRODUCTSREQUEST.fields_by_name['input_config']._options = None
  _IMPORTPRODUCTSREQUEST.fields_by_name['input_config']._serialized_options = b'\342A\001\002'
  _IMPORTUSEREVENTSREQUEST.fields_by_name['parent']._options = None
  _IMPORTUSEREVENTSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\037\n\035retail.googleapis.com/Catalog'
  _IMPORTUSEREVENTSREQUEST.fields_by_name['input_config']._options = None
  _IMPORTUSEREVENTSREQUEST.fields_by_name['input_config']._serialized_options = b'\342A\001\002'
  _IMPORTCOMPLETIONDATAREQUEST.fields_by_name['parent']._options = None
  _IMPORTCOMPLETIONDATAREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\037\n\035retail.googleapis.com/Catalog'
  _IMPORTCOMPLETIONDATAREQUEST.fields_by_name['input_config']._options = None
  _IMPORTCOMPLETIONDATAREQUEST.fields_by_name['input_config']._serialized_options = b'\342A\001\002'
  _USEREVENTINPUTCONFIG.fields_by_name['user_event_inline_source']._options = None
  _USEREVENTINPUTCONFIG.fields_by_name['user_event_inline_source']._serialized_options = b'\342A\001\002'
  _USEREVENTINPUTCONFIG.fields_by_name['gcs_source']._options = None
  _USEREVENTINPUTCONFIG.fields_by_name['gcs_source']._serialized_options = b'\342A\001\002'
  _USEREVENTINPUTCONFIG.fields_by_name['big_query_source']._options = None
  _USEREVENTINPUTCONFIG.fields_by_name['big_query_source']._serialized_options = b'\342A\001\002'
  _COMPLETIONDATAINPUTCONFIG.fields_by_name['big_query_source']._options = None
  _COMPLETIONDATAINPUTCONFIG.fields_by_name['big_query_source']._serialized_options = b'\342A\001\002'
  _GCSSOURCE._serialized_start=355
  _GCSSOURCE._serialized_end=436
  _BIGQUERYSOURCE._serialized_start=439
  _BIGQUERYSOURCE._serialized_end=702
  _PRODUCTINLINESOURCE._serialized_start=704
  _PRODUCTINLINESOURCE._serialized_end=792
  _USEREVENTINLINESOURCE._serialized_start=794
  _USEREVENTINLINESOURCE._serialized_end=891
  _IMPORTERRORSCONFIG._serialized_start=893
  _IMPORTERRORSCONFIG._serialized_end=961
  _IMPORTPRODUCTSREQUEST._serialized_start=964
  _IMPORTPRODUCTSREQUEST._serialized_end=1569
  _IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE._serialized_start=1485
  _IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE._serialized_end=1569
  _IMPORTUSEREVENTSREQUEST._serialized_start=1572
  _IMPORTUSEREVENTSREQUEST._serialized_end=1829
  _IMPORTCOMPLETIONDATAREQUEST._serialized_start=1832
  _IMPORTCOMPLETIONDATAREQUEST._serialized_end=2077
  _PRODUCTINPUTCONFIG._serialized_start=2080
  _PRODUCTINPUTCONFIG._serialized_end=2361
  _USEREVENTINPUTCONFIG._serialized_start=2364
  _USEREVENTINPUTCONFIG._serialized_end=2672
  _COMPLETIONDATAINPUTCONFIG._serialized_start=2674
  _COMPLETIONDATAINPUTCONFIG._serialized_end=2801
  _IMPORTMETADATA._serialized_start=2804
  _IMPORTMETADATA._serialized_end=3107
  _IMPORTPRODUCTSRESPONSE._serialized_start=3110
  _IMPORTPRODUCTSRESPONSE._serialized_end=3272
  _IMPORTUSEREVENTSRESPONSE._serialized_start=3275
  _IMPORTUSEREVENTSRESPONSE._serialized_end=3526
  _USEREVENTIMPORTSUMMARY._serialized_start=3528
  _USEREVENTIMPORTSUMMARY._serialized_end=3652
  _IMPORTCOMPLETIONDATARESPONSE._serialized_start=3654
  _IMPORTCOMPLETIONDATARESPONSE._serialized_end=3741
# @@protoc_insertion_point(module_scope)
