# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/logging/v1/audit_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/bigquery/logging/v1/audit_data.proto\x12 google.cloud.bigquery.logging.v1\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\xe5\x11\n\tAuditData\x12h\n\x14table_insert_request\x18\x01 \x01(\x0b\x32\x34.google.cloud.bigquery.logging.v1.TableInsertRequestH\x00R\x12tableInsertRequest\x12h\n\x14table_update_request\x18\x10 \x01(\x0b\x32\x34.google.cloud.bigquery.logging.v1.TableUpdateRequestH\x00R\x12tableUpdateRequest\x12h\n\x14\x64\x61taset_list_request\x18\x02 \x01(\x0b\x32\x34.google.cloud.bigquery.logging.v1.DatasetListRequestH\x00R\x12\x64\x61tasetListRequest\x12n\n\x16\x64\x61taset_insert_request\x18\x03 \x01(\x0b\x32\x36.google.cloud.bigquery.logging.v1.DatasetInsertRequestH\x00R\x14\x64\x61tasetInsertRequest\x12n\n\x16\x64\x61taset_update_request\x18\x04 \x01(\x0b\x32\x36.google.cloud.bigquery.logging.v1.DatasetUpdateRequestH\x00R\x14\x64\x61tasetUpdateRequest\x12\x62\n\x12job_insert_request\x18\x05 \x01(\x0b\x32\x32.google.cloud.bigquery.logging.v1.JobInsertRequestH\x00R\x10jobInsertRequest\x12_\n\x11job_query_request\x18\x06 \x01(\x0b\x32\x31.google.cloud.bigquery.logging.v1.JobQueryRequestH\x00R\x0fjobQueryRequest\x12\x7f\n\x1djob_get_query_results_request\x18\x07 \x01(\x0b\x32;.google.cloud.bigquery.logging.v1.JobGetQueryResultsRequestH\x00R\x19jobGetQueryResultsRequest\x12o\n\x17table_data_list_request\x18\x08 \x01(\x0b\x32\x36.google.cloud.bigquery.logging.v1.TableDataListRequestH\x00R\x14tableDataListRequest\x12Y\n\x16set_iam_policy_request\x18\x14 \x01(\x0b\x32\".google.iam.v1.SetIamPolicyRequestH\x00R\x13setIamPolicyRequest\x12k\n\x15table_insert_response\x18\t \x01(\x0b\x32\x35.google.cloud.bigquery.logging.v1.TableInsertResponseH\x01R\x13tableInsertResponse\x12k\n\x15table_update_response\x18\n \x01(\x0b\x32\x35.google.cloud.bigquery.logging.v1.TableUpdateResponseH\x01R\x13tableUpdateResponse\x12q\n\x17\x64\x61taset_insert_response\x18\x0b \x01(\x0b\x32\x37.google.cloud.bigquery.logging.v1.DatasetInsertResponseH\x01R\x15\x64\x61tasetInsertResponse\x12q\n\x17\x64\x61taset_update_response\x18\x0c \x01(\x0b\x32\x37.google.cloud.bigquery.logging.v1.DatasetUpdateResponseH\x01R\x15\x64\x61tasetUpdateResponse\x12\x65\n\x13job_insert_response\x18\x12 \x01(\x0b\x32\x33.google.cloud.bigquery.logging.v1.JobInsertResponseH\x01R\x11jobInsertResponse\x12\x62\n\x12job_query_response\x18\r \x01(\x0b\x32\x32.google.cloud.bigquery.logging.v1.JobQueryResponseH\x01R\x10jobQueryResponse\x12\x82\x01\n\x1ejob_get_query_results_response\x18\x0e \x01(\x0b\x32<.google.cloud.bigquery.logging.v1.JobGetQueryResultsResponseH\x01R\x1ajobGetQueryResultsResponse\x12o\n\x17job_query_done_response\x18\x0f \x01(\x0b\x32\x36.google.cloud.bigquery.logging.v1.JobQueryDoneResponseH\x01R\x14jobQueryDoneResponse\x12@\n\x0fpolicy_response\x18\x15 \x01(\x0b\x32\x15.google.iam.v1.PolicyH\x01R\x0epolicyResponse\x12\x63\n\x13job_completed_event\x18\x11 \x01(\x0b\x32\x33.google.cloud.bigquery.logging.v1.JobCompletedEventR\x11jobCompletedEvent\x12i\n\x16table_data_read_events\x18\x13 \x03(\x0b\x32\x34.google.cloud.bigquery.logging.v1.TableDataReadEventR\x13tableDataReadEventsB\t\n\x07requestB\n\n\x08response\"Y\n\x12TableInsertRequest\x12\x43\n\x08resource\x18\x01 \x01(\x0b\x32\'.google.cloud.bigquery.logging.v1.TableR\x08resource\"Y\n\x12TableUpdateRequest\x12\x43\n\x08resource\x18\x01 \x01(\x0b\x32\'.google.cloud.bigquery.logging.v1.TableR\x08resource\"Z\n\x13TableInsertResponse\x12\x43\n\x08resource\x18\x01 \x01(\x0b\x32\'.google.cloud.bigquery.logging.v1.TableR\x08resource\"Z\n\x13TableUpdateResponse\x12\x43\n\x08resource\x18\x01 \x01(\x0b\x32\'.google.cloud.bigquery.logging.v1.TableR\x08resource\"/\n\x12\x44\x61tasetListRequest\x12\x19\n\x08list_all\x18\x01 \x01(\x08R\x07listAll\"]\n\x14\x44\x61tasetInsertRequest\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32).google.cloud.bigquery.logging.v1.DatasetR\x08resource\"^\n\x15\x44\x61tasetInsertResponse\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32).google.cloud.bigquery.logging.v1.DatasetR\x08resource\"]\n\x14\x44\x61tasetUpdateRequest\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32).google.cloud.bigquery.logging.v1.DatasetR\x08resource\"^\n\x15\x44\x61tasetUpdateResponse\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32).google.cloud.bigquery.logging.v1.DatasetR\x08resource\"U\n\x10JobInsertRequest\x12\x41\n\x08resource\x18\x01 \x01(\x0b\x32%.google.cloud.bigquery.logging.v1.JobR\x08resource\"V\n\x11JobInsertResponse\x12\x41\n\x08resource\x18\x01 \x01(\x0b\x32%.google.cloud.bigquery.logging.v1.JobR\x08resource\"\xd8\x01\n\x0fJobQueryRequest\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\x12\x1f\n\x0bmax_results\x18\x02 \x01(\rR\nmaxResults\x12V\n\x0f\x64\x65\x66\x61ult_dataset\x18\x03 \x01(\x0b\x32-.google.cloud.bigquery.logging.v1.DatasetNameR\x0e\x64\x65\x66\x61ultDataset\x12\x1d\n\nproject_id\x18\x04 \x01(\tR\tprojectId\x12\x17\n\x07\x64ry_run\x18\x05 \x01(\x08R\x06\x64ryRun\"p\n\x10JobQueryResponse\x12#\n\rtotal_results\x18\x01 \x01(\x04R\x0ctotalResults\x12\x37\n\x03job\x18\x02 \x01(\x0b\x32%.google.cloud.bigquery.logging.v1.JobR\x03job\"Y\n\x19JobGetQueryResultsRequest\x12\x1f\n\x0bmax_results\x18\x01 \x01(\rR\nmaxResults\x12\x1b\n\tstart_row\x18\x02 \x01(\x04R\x08startRow\"z\n\x1aJobGetQueryResultsResponse\x12#\n\rtotal_results\x18\x01 \x01(\x04R\x0ctotalResults\x12\x37\n\x03job\x18\x02 \x01(\x0b\x32%.google.cloud.bigquery.logging.v1.JobR\x03job\"O\n\x14JobQueryDoneResponse\x12\x37\n\x03job\x18\x01 \x01(\x0b\x32%.google.cloud.bigquery.logging.v1.JobR\x03job\"k\n\x11JobCompletedEvent\x12\x1d\n\nevent_name\x18\x01 \x01(\tR\teventName\x12\x37\n\x03job\x18\x02 \x01(\x0b\x32%.google.cloud.bigquery.logging.v1.JobR\x03job\"\x8d\x01\n\x12TableDataReadEvent\x12J\n\ntable_name\x18\x01 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\ttableName\x12+\n\x11referenced_fields\x18\x02 \x03(\tR\x10referencedFields\"T\n\x14TableDataListRequest\x12\x1b\n\tstart_row\x18\x01 \x01(\x04R\x08startRow\x12\x1f\n\x0bmax_results\x18\x02 \x01(\rR\nmaxResults\"\xca\x04\n\x05Table\x12J\n\ntable_name\x18\x01 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\ttableName\x12?\n\x04info\x18\x02 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.TableInfoR\x04info\x12\x1f\n\x0bschema_json\x18\x08 \x01(\tR\nschemaJson\x12I\n\x04view\x18\x04 \x01(\x0b\x32\x35.google.cloud.bigquery.logging.v1.TableViewDefinitionR\x04view\x12;\n\x0b\x65xpire_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nexpireTime\x12;\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12?\n\rtruncate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0ctruncateTime\x12;\n\x0bupdate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12P\n\nencryption\x18\n \x01(\x0b\x32\x30.google.cloud.bigquery.logging.v1.EncryptionInfoR\nencryption\"\xde\x01\n\tTableInfo\x12#\n\rfriendly_name\x18\x01 \x01(\tR\x0c\x66riendlyName\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12O\n\x06labels\x18\x03 \x03(\x0b\x32\x37.google.cloud.bigquery.logging.v1.TableInfo.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"+\n\x13TableViewDefinition\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\"\xb7\x03\n\x07\x44\x61taset\x12P\n\x0c\x64\x61taset_name\x18\x01 \x01(\x0b\x32-.google.cloud.bigquery.logging.v1.DatasetNameR\x0b\x64\x61tasetName\x12\x41\n\x04info\x18\x02 \x01(\x0b\x32-.google.cloud.bigquery.logging.v1.DatasetInfoR\x04info\x12;\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12?\n\x03\x61\x63l\x18\x06 \x01(\x0b\x32-.google.cloud.bigquery.logging.v1.BigQueryAclR\x03\x61\x63l\x12\\\n\x1d\x64\x65\x66\x61ult_table_expire_duration\x18\x08 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1a\x64\x65\x66\x61ultTableExpireDuration\"\xe2\x01\n\x0b\x44\x61tasetInfo\x12#\n\rfriendly_name\x18\x01 \x01(\tR\x0c\x66riendlyName\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12Q\n\x06labels\x18\x03 \x03(\x0b\x32\x39.google.cloud.bigquery.logging.v1.DatasetInfo.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xc1\x02\n\x0b\x42igQueryAcl\x12M\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x33.google.cloud.bigquery.logging.v1.BigQueryAcl.EntryR\x07\x65ntries\x1a\xe2\x01\n\x05\x45ntry\x12\x12\n\x04role\x18\x01 \x01(\tR\x04role\x12\x1f\n\x0bgroup_email\x18\x02 \x01(\tR\ngroupEmail\x12\x1d\n\nuser_email\x18\x03 \x01(\tR\tuserEmail\x12\x16\n\x06\x64omain\x18\x04 \x01(\tR\x06\x64omain\x12#\n\rspecial_group\x18\x05 \x01(\tR\x0cspecialGroup\x12H\n\tview_name\x18\x06 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\x08viewName\"\xd0\x02\n\x03Job\x12\x44\n\x08job_name\x18\x01 \x01(\x0b\x32).google.cloud.bigquery.logging.v1.JobNameR\x07jobName\x12_\n\x11job_configuration\x18\x02 \x01(\x0b\x32\x32.google.cloud.bigquery.logging.v1.JobConfigurationR\x10jobConfiguration\x12J\n\njob_status\x18\x03 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.JobStatusR\tjobStatus\x12V\n\x0ejob_statistics\x18\x04 \x01(\x0b\x32/.google.cloud.bigquery.logging.v1.JobStatisticsR\rjobStatistics\"\xfd\x0f\n\x10JobConfiguration\x12P\n\x05query\x18\x05 \x01(\x0b\x32\x38.google.cloud.bigquery.logging.v1.JobConfiguration.QueryH\x00R\x05query\x12M\n\x04load\x18\x06 \x01(\x0b\x32\x37.google.cloud.bigquery.logging.v1.JobConfiguration.LoadH\x00R\x04load\x12V\n\x07\x65xtract\x18\x07 \x01(\x0b\x32:.google.cloud.bigquery.logging.v1.JobConfiguration.ExtractH\x00R\x07\x65xtract\x12]\n\ntable_copy\x18\x08 \x01(\x0b\x32<.google.cloud.bigquery.logging.v1.JobConfiguration.TableCopyH\x00R\ttableCopy\x12\x17\n\x07\x64ry_run\x18\t \x01(\x08R\x06\x64ryRun\x12V\n\x06labels\x18\x03 \x03(\x0b\x32>.google.cloud.bigquery.logging.v1.JobConfiguration.LabelsEntryR\x06labels\x1a\xcd\x04\n\x05Query\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\x12X\n\x11\x64\x65stination_table\x18\x02 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\x10\x64\x65stinationTable\x12-\n\x12\x63reate_disposition\x18\x03 \x01(\tR\x11\x63reateDisposition\x12+\n\x11write_disposition\x18\x04 \x01(\tR\x10writeDisposition\x12V\n\x0f\x64\x65\x66\x61ult_dataset\x18\x05 \x01(\x0b\x32-.google.cloud.bigquery.logging.v1.DatasetNameR\x0e\x64\x65\x66\x61ultDataset\x12^\n\x11table_definitions\x18\x06 \x03(\x0b\x32\x31.google.cloud.bigquery.logging.v1.TableDefinitionR\x10tableDefinitions\x12%\n\x0equery_priority\x18\x07 \x01(\tR\rqueryPriority\x12r\n\x1c\x64\x65stination_table_encryption\x18\x08 \x01(\x0b\x32\x30.google.cloud.bigquery.logging.v1.EncryptionInfoR\x1a\x64\x65stinationTableEncryption\x12%\n\x0estatement_type\x18\t \x01(\tR\rstatementType\x1a\xf2\x02\n\x04Load\x12\x1f\n\x0bsource_uris\x18\x01 \x03(\tR\nsourceUris\x12\x1f\n\x0bschema_json\x18\x06 \x01(\tR\nschemaJson\x12X\n\x11\x64\x65stination_table\x18\x03 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\x10\x64\x65stinationTable\x12-\n\x12\x63reate_disposition\x18\x04 \x01(\tR\x11\x63reateDisposition\x12+\n\x11write_disposition\x18\x05 \x01(\tR\x10writeDisposition\x12r\n\x1c\x64\x65stination_table_encryption\x18\x07 \x01(\x0b\x32\x30.google.cloud.bigquery.logging.v1.EncryptionInfoR\x1a\x64\x65stinationTableEncryption\x1a\x84\x01\n\x07\x45xtract\x12)\n\x10\x64\x65stination_uris\x18\x01 \x03(\tR\x0f\x64\x65stinationUris\x12N\n\x0csource_table\x18\x02 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\x0bsourceTable\x1a\x87\x03\n\tTableCopy\x12P\n\rsource_tables\x18\x01 \x03(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\x0csourceTables\x12X\n\x11\x64\x65stination_table\x18\x02 \x01(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\x10\x64\x65stinationTable\x12-\n\x12\x63reate_disposition\x18\x03 \x01(\tR\x11\x63reateDisposition\x12+\n\x11write_disposition\x18\x04 \x01(\tR\x10writeDisposition\x12r\n\x1c\x64\x65stination_table_encryption\x18\x05 \x01(\x0b\x32\x30.google.cloud.bigquery.logging.v1.EncryptionInfoR\x1a\x64\x65stinationTableEncryption\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x0f\n\rconfiguration\"F\n\x0fTableDefinition\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bsource_uris\x18\x02 \x03(\tR\nsourceUris\"\x8c\x01\n\tJobStatus\x12\x14\n\x05state\x18\x01 \x01(\tR\x05state\x12(\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusR\x05\x65rror\x12?\n\x11\x61\x64\x64itional_errors\x18\x03 \x03(\x0b\x32\x12.google.rpc.StatusR\x10\x61\x64\x64itionalErrors\"\xaf\x07\n\rJobStatistics\x12;\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x39\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x32\n\x15total_processed_bytes\x18\x04 \x01(\x03R\x13totalProcessedBytes\x12,\n\x12total_billed_bytes\x18\x05 \x01(\x03R\x10totalBilledBytes\x12!\n\x0c\x62illing_tier\x18\x07 \x01(\x05R\x0b\x62illingTier\x12\"\n\rtotal_slot_ms\x18\x08 \x01(\x03R\x0btotalSlotMs\x12u\n\x11reservation_usage\x18\x0e \x03(\x0b\x32H.google.cloud.bigquery.logging.v1.JobStatistics.ReservationResourceUsageR\x10reservationUsage\x12X\n\x11referenced_tables\x18\t \x03(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\x10referencedTables\x12\x34\n\x16total_tables_processed\x18\n \x01(\x05R\x14totalTablesProcessed\x12V\n\x10referenced_views\x18\x0b \x03(\x0b\x32+.google.cloud.bigquery.logging.v1.TableNameR\x0freferencedViews\x12\x32\n\x15total_views_processed\x18\x0c \x01(\x05R\x13totalViewsProcessed\x12\x33\n\x16query_output_row_count\x18\x0f \x01(\x03R\x13queryOutputRowCount\x12\x35\n\x17total_load_output_bytes\x18\r \x01(\x03R\x14totalLoadOutputBytes\x1aG\n\x18ReservationResourceUsage\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x17\n\x07slot_ms\x18\x02 \x01(\x03R\x06slotMs\"K\n\x0b\x44\x61tasetName\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\"d\n\tTableName\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12\x19\n\x08table_id\x18\x03 \x01(\tR\x07tableId\"[\n\x07JobName\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x15\n\x06job_id\x18\x02 \x01(\tR\x05jobId\x12\x1a\n\x08location\x18\x03 \x01(\tR\x08location\"2\n\x0e\x45ncryptionInfo\x12 \n\x0ckms_key_name\x18\x01 \x01(\tR\nkmsKeyNameB\x81\x01\n$com.google.cloud.bigquery.logging.v1B\x0e\x41uditDataProtoP\x01ZGgoogle.golang.org/genproto/googleapis/cloud/bigquery/logging/v1;loggingb\x06proto3')



_AUDITDATA = DESCRIPTOR.message_types_by_name['AuditData']
_TABLEINSERTREQUEST = DESCRIPTOR.message_types_by_name['TableInsertRequest']
_TABLEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['TableUpdateRequest']
_TABLEINSERTRESPONSE = DESCRIPTOR.message_types_by_name['TableInsertResponse']
_TABLEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['TableUpdateResponse']
_DATASETLISTREQUEST = DESCRIPTOR.message_types_by_name['DatasetListRequest']
_DATASETINSERTREQUEST = DESCRIPTOR.message_types_by_name['DatasetInsertRequest']
_DATASETINSERTRESPONSE = DESCRIPTOR.message_types_by_name['DatasetInsertResponse']
_DATASETUPDATEREQUEST = DESCRIPTOR.message_types_by_name['DatasetUpdateRequest']
_DATASETUPDATERESPONSE = DESCRIPTOR.message_types_by_name['DatasetUpdateResponse']
_JOBINSERTREQUEST = DESCRIPTOR.message_types_by_name['JobInsertRequest']
_JOBINSERTRESPONSE = DESCRIPTOR.message_types_by_name['JobInsertResponse']
_JOBQUERYREQUEST = DESCRIPTOR.message_types_by_name['JobQueryRequest']
_JOBQUERYRESPONSE = DESCRIPTOR.message_types_by_name['JobQueryResponse']
_JOBGETQUERYRESULTSREQUEST = DESCRIPTOR.message_types_by_name['JobGetQueryResultsRequest']
_JOBGETQUERYRESULTSRESPONSE = DESCRIPTOR.message_types_by_name['JobGetQueryResultsResponse']
_JOBQUERYDONERESPONSE = DESCRIPTOR.message_types_by_name['JobQueryDoneResponse']
_JOBCOMPLETEDEVENT = DESCRIPTOR.message_types_by_name['JobCompletedEvent']
_TABLEDATAREADEVENT = DESCRIPTOR.message_types_by_name['TableDataReadEvent']
_TABLEDATALISTREQUEST = DESCRIPTOR.message_types_by_name['TableDataListRequest']
_TABLE = DESCRIPTOR.message_types_by_name['Table']
_TABLEINFO = DESCRIPTOR.message_types_by_name['TableInfo']
_TABLEINFO_LABELSENTRY = _TABLEINFO.nested_types_by_name['LabelsEntry']
_TABLEVIEWDEFINITION = DESCRIPTOR.message_types_by_name['TableViewDefinition']
_DATASET = DESCRIPTOR.message_types_by_name['Dataset']
_DATASETINFO = DESCRIPTOR.message_types_by_name['DatasetInfo']
_DATASETINFO_LABELSENTRY = _DATASETINFO.nested_types_by_name['LabelsEntry']
_BIGQUERYACL = DESCRIPTOR.message_types_by_name['BigQueryAcl']
_BIGQUERYACL_ENTRY = _BIGQUERYACL.nested_types_by_name['Entry']
_JOB = DESCRIPTOR.message_types_by_name['Job']
_JOBCONFIGURATION = DESCRIPTOR.message_types_by_name['JobConfiguration']
_JOBCONFIGURATION_QUERY = _JOBCONFIGURATION.nested_types_by_name['Query']
_JOBCONFIGURATION_LOAD = _JOBCONFIGURATION.nested_types_by_name['Load']
_JOBCONFIGURATION_EXTRACT = _JOBCONFIGURATION.nested_types_by_name['Extract']
_JOBCONFIGURATION_TABLECOPY = _JOBCONFIGURATION.nested_types_by_name['TableCopy']
_JOBCONFIGURATION_LABELSENTRY = _JOBCONFIGURATION.nested_types_by_name['LabelsEntry']
_TABLEDEFINITION = DESCRIPTOR.message_types_by_name['TableDefinition']
_JOBSTATUS = DESCRIPTOR.message_types_by_name['JobStatus']
_JOBSTATISTICS = DESCRIPTOR.message_types_by_name['JobStatistics']
_JOBSTATISTICS_RESERVATIONRESOURCEUSAGE = _JOBSTATISTICS.nested_types_by_name['ReservationResourceUsage']
_DATASETNAME = DESCRIPTOR.message_types_by_name['DatasetName']
_TABLENAME = DESCRIPTOR.message_types_by_name['TableName']
_JOBNAME = DESCRIPTOR.message_types_by_name['JobName']
_ENCRYPTIONINFO = DESCRIPTOR.message_types_by_name['EncryptionInfo']
AuditData = _reflection.GeneratedProtocolMessageType('AuditData', (_message.Message,), {
  'DESCRIPTOR' : _AUDITDATA,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.AuditData)
  })
_sym_db.RegisterMessage(AuditData)

TableInsertRequest = _reflection.GeneratedProtocolMessageType('TableInsertRequest', (_message.Message,), {
  'DESCRIPTOR' : _TABLEINSERTREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableInsertRequest)
  })
_sym_db.RegisterMessage(TableInsertRequest)

TableUpdateRequest = _reflection.GeneratedProtocolMessageType('TableUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _TABLEUPDATEREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableUpdateRequest)
  })
_sym_db.RegisterMessage(TableUpdateRequest)

TableInsertResponse = _reflection.GeneratedProtocolMessageType('TableInsertResponse', (_message.Message,), {
  'DESCRIPTOR' : _TABLEINSERTRESPONSE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableInsertResponse)
  })
_sym_db.RegisterMessage(TableInsertResponse)

TableUpdateResponse = _reflection.GeneratedProtocolMessageType('TableUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _TABLEUPDATERESPONSE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableUpdateResponse)
  })
_sym_db.RegisterMessage(TableUpdateResponse)

DatasetListRequest = _reflection.GeneratedProtocolMessageType('DatasetListRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATASETLISTREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.DatasetListRequest)
  })
_sym_db.RegisterMessage(DatasetListRequest)

DatasetInsertRequest = _reflection.GeneratedProtocolMessageType('DatasetInsertRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATASETINSERTREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.DatasetInsertRequest)
  })
_sym_db.RegisterMessage(DatasetInsertRequest)

DatasetInsertResponse = _reflection.GeneratedProtocolMessageType('DatasetInsertResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATASETINSERTRESPONSE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.DatasetInsertResponse)
  })
_sym_db.RegisterMessage(DatasetInsertResponse)

DatasetUpdateRequest = _reflection.GeneratedProtocolMessageType('DatasetUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATASETUPDATEREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.DatasetUpdateRequest)
  })
_sym_db.RegisterMessage(DatasetUpdateRequest)

DatasetUpdateResponse = _reflection.GeneratedProtocolMessageType('DatasetUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATASETUPDATERESPONSE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.DatasetUpdateResponse)
  })
_sym_db.RegisterMessage(DatasetUpdateResponse)

JobInsertRequest = _reflection.GeneratedProtocolMessageType('JobInsertRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOBINSERTREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobInsertRequest)
  })
_sym_db.RegisterMessage(JobInsertRequest)

JobInsertResponse = _reflection.GeneratedProtocolMessageType('JobInsertResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOBINSERTRESPONSE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobInsertResponse)
  })
_sym_db.RegisterMessage(JobInsertResponse)

JobQueryRequest = _reflection.GeneratedProtocolMessageType('JobQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOBQUERYREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobQueryRequest)
  })
_sym_db.RegisterMessage(JobQueryRequest)

JobQueryResponse = _reflection.GeneratedProtocolMessageType('JobQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOBQUERYRESPONSE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobQueryResponse)
  })
_sym_db.RegisterMessage(JobQueryResponse)

JobGetQueryResultsRequest = _reflection.GeneratedProtocolMessageType('JobGetQueryResultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOBGETQUERYRESULTSREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobGetQueryResultsRequest)
  })
_sym_db.RegisterMessage(JobGetQueryResultsRequest)

JobGetQueryResultsResponse = _reflection.GeneratedProtocolMessageType('JobGetQueryResultsResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOBGETQUERYRESULTSRESPONSE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobGetQueryResultsResponse)
  })
_sym_db.RegisterMessage(JobGetQueryResultsResponse)

JobQueryDoneResponse = _reflection.GeneratedProtocolMessageType('JobQueryDoneResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOBQUERYDONERESPONSE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobQueryDoneResponse)
  })
_sym_db.RegisterMessage(JobQueryDoneResponse)

JobCompletedEvent = _reflection.GeneratedProtocolMessageType('JobCompletedEvent', (_message.Message,), {
  'DESCRIPTOR' : _JOBCOMPLETEDEVENT,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobCompletedEvent)
  })
_sym_db.RegisterMessage(JobCompletedEvent)

TableDataReadEvent = _reflection.GeneratedProtocolMessageType('TableDataReadEvent', (_message.Message,), {
  'DESCRIPTOR' : _TABLEDATAREADEVENT,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableDataReadEvent)
  })
_sym_db.RegisterMessage(TableDataReadEvent)

TableDataListRequest = _reflection.GeneratedProtocolMessageType('TableDataListRequest', (_message.Message,), {
  'DESCRIPTOR' : _TABLEDATALISTREQUEST,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableDataListRequest)
  })
_sym_db.RegisterMessage(TableDataListRequest)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {
  'DESCRIPTOR' : _TABLE,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.Table)
  })
_sym_db.RegisterMessage(Table)

TableInfo = _reflection.GeneratedProtocolMessageType('TableInfo', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TABLEINFO_LABELSENTRY,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableInfo.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _TABLEINFO,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableInfo)
  })
_sym_db.RegisterMessage(TableInfo)
_sym_db.RegisterMessage(TableInfo.LabelsEntry)

TableViewDefinition = _reflection.GeneratedProtocolMessageType('TableViewDefinition', (_message.Message,), {
  'DESCRIPTOR' : _TABLEVIEWDEFINITION,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableViewDefinition)
  })
_sym_db.RegisterMessage(TableViewDefinition)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.Dataset)
  })
_sym_db.RegisterMessage(Dataset)

DatasetInfo = _reflection.GeneratedProtocolMessageType('DatasetInfo', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASETINFO_LABELSENTRY,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.DatasetInfo.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _DATASETINFO,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.DatasetInfo)
  })
_sym_db.RegisterMessage(DatasetInfo)
_sym_db.RegisterMessage(DatasetInfo.LabelsEntry)

BigQueryAcl = _reflection.GeneratedProtocolMessageType('BigQueryAcl', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _BIGQUERYACL_ENTRY,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.BigQueryAcl.Entry)
    })
  ,
  'DESCRIPTOR' : _BIGQUERYACL,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.BigQueryAcl)
  })
_sym_db.RegisterMessage(BigQueryAcl)
_sym_db.RegisterMessage(BigQueryAcl.Entry)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.Job)
  })
_sym_db.RegisterMessage(Job)

JobConfiguration = _reflection.GeneratedProtocolMessageType('JobConfiguration', (_message.Message,), {

  'Query' : _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
    'DESCRIPTOR' : _JOBCONFIGURATION_QUERY,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobConfiguration.Query)
    })
  ,

  'Load' : _reflection.GeneratedProtocolMessageType('Load', (_message.Message,), {
    'DESCRIPTOR' : _JOBCONFIGURATION_LOAD,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobConfiguration.Load)
    })
  ,

  'Extract' : _reflection.GeneratedProtocolMessageType('Extract', (_message.Message,), {
    'DESCRIPTOR' : _JOBCONFIGURATION_EXTRACT,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobConfiguration.Extract)
    })
  ,

  'TableCopy' : _reflection.GeneratedProtocolMessageType('TableCopy', (_message.Message,), {
    'DESCRIPTOR' : _JOBCONFIGURATION_TABLECOPY,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobConfiguration.TableCopy)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _JOBCONFIGURATION_LABELSENTRY,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobConfiguration.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _JOBCONFIGURATION,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobConfiguration)
  })
_sym_db.RegisterMessage(JobConfiguration)
_sym_db.RegisterMessage(JobConfiguration.Query)
_sym_db.RegisterMessage(JobConfiguration.Load)
_sym_db.RegisterMessage(JobConfiguration.Extract)
_sym_db.RegisterMessage(JobConfiguration.TableCopy)
_sym_db.RegisterMessage(JobConfiguration.LabelsEntry)

TableDefinition = _reflection.GeneratedProtocolMessageType('TableDefinition', (_message.Message,), {
  'DESCRIPTOR' : _TABLEDEFINITION,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableDefinition)
  })
_sym_db.RegisterMessage(TableDefinition)

JobStatus = _reflection.GeneratedProtocolMessageType('JobStatus', (_message.Message,), {
  'DESCRIPTOR' : _JOBSTATUS,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobStatus)
  })
_sym_db.RegisterMessage(JobStatus)

JobStatistics = _reflection.GeneratedProtocolMessageType('JobStatistics', (_message.Message,), {

  'ReservationResourceUsage' : _reflection.GeneratedProtocolMessageType('ReservationResourceUsage', (_message.Message,), {
    'DESCRIPTOR' : _JOBSTATISTICS_RESERVATIONRESOURCEUSAGE,
    '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobStatistics.ReservationResourceUsage)
    })
  ,
  'DESCRIPTOR' : _JOBSTATISTICS,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobStatistics)
  })
_sym_db.RegisterMessage(JobStatistics)
_sym_db.RegisterMessage(JobStatistics.ReservationResourceUsage)

DatasetName = _reflection.GeneratedProtocolMessageType('DatasetName', (_message.Message,), {
  'DESCRIPTOR' : _DATASETNAME,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.DatasetName)
  })
_sym_db.RegisterMessage(DatasetName)

TableName = _reflection.GeneratedProtocolMessageType('TableName', (_message.Message,), {
  'DESCRIPTOR' : _TABLENAME,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.TableName)
  })
_sym_db.RegisterMessage(TableName)

JobName = _reflection.GeneratedProtocolMessageType('JobName', (_message.Message,), {
  'DESCRIPTOR' : _JOBNAME,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.JobName)
  })
_sym_db.RegisterMessage(JobName)

EncryptionInfo = _reflection.GeneratedProtocolMessageType('EncryptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTIONINFO,
  '__module__' : 'google.cloud.bigquery.logging.v1.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.logging.v1.EncryptionInfo)
  })
_sym_db.RegisterMessage(EncryptionInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.cloud.bigquery.logging.v1B\016AuditDataProtoP\001ZGgoogle.golang.org/genproto/googleapis/cloud/bigquery/logging/v1;logging'
  _TABLEINFO_LABELSENTRY._options = None
  _TABLEINFO_LABELSENTRY._serialized_options = b'8\001'
  _DATASETINFO_LABELSENTRY._options = None
  _DATASETINFO_LABELSENTRY._serialized_options = b'8\001'
  _JOBCONFIGURATION_LABELSENTRY._options = None
  _JOBCONFIGURATION_LABELSENTRY._serialized_options = b'8\001'
  _AUDITDATA._serialized_start=238
  _AUDITDATA._serialized_end=2515
  _TABLEINSERTREQUEST._serialized_start=2517
  _TABLEINSERTREQUEST._serialized_end=2606
  _TABLEUPDATEREQUEST._serialized_start=2608
  _TABLEUPDATEREQUEST._serialized_end=2697
  _TABLEINSERTRESPONSE._serialized_start=2699
  _TABLEINSERTRESPONSE._serialized_end=2789
  _TABLEUPDATERESPONSE._serialized_start=2791
  _TABLEUPDATERESPONSE._serialized_end=2881
  _DATASETLISTREQUEST._serialized_start=2883
  _DATASETLISTREQUEST._serialized_end=2930
  _DATASETINSERTREQUEST._serialized_start=2932
  _DATASETINSERTREQUEST._serialized_end=3025
  _DATASETINSERTRESPONSE._serialized_start=3027
  _DATASETINSERTRESPONSE._serialized_end=3121
  _DATASETUPDATEREQUEST._serialized_start=3123
  _DATASETUPDATEREQUEST._serialized_end=3216
  _DATASETUPDATERESPONSE._serialized_start=3218
  _DATASETUPDATERESPONSE._serialized_end=3312
  _JOBINSERTREQUEST._serialized_start=3314
  _JOBINSERTREQUEST._serialized_end=3399
  _JOBINSERTRESPONSE._serialized_start=3401
  _JOBINSERTRESPONSE._serialized_end=3487
  _JOBQUERYREQUEST._serialized_start=3490
  _JOBQUERYREQUEST._serialized_end=3706
  _JOBQUERYRESPONSE._serialized_start=3708
  _JOBQUERYRESPONSE._serialized_end=3820
  _JOBGETQUERYRESULTSREQUEST._serialized_start=3822
  _JOBGETQUERYRESULTSREQUEST._serialized_end=3911
  _JOBGETQUERYRESULTSRESPONSE._serialized_start=3913
  _JOBGETQUERYRESULTSRESPONSE._serialized_end=4035
  _JOBQUERYDONERESPONSE._serialized_start=4037
  _JOBQUERYDONERESPONSE._serialized_end=4116
  _JOBCOMPLETEDEVENT._serialized_start=4118
  _JOBCOMPLETEDEVENT._serialized_end=4225
  _TABLEDATAREADEVENT._serialized_start=4228
  _TABLEDATAREADEVENT._serialized_end=4369
  _TABLEDATALISTREQUEST._serialized_start=4371
  _TABLEDATALISTREQUEST._serialized_end=4455
  _TABLE._serialized_start=4458
  _TABLE._serialized_end=5044
  _TABLEINFO._serialized_start=5047
  _TABLEINFO._serialized_end=5269
  _TABLEINFO_LABELSENTRY._serialized_start=5212
  _TABLEINFO_LABELSENTRY._serialized_end=5269
  _TABLEVIEWDEFINITION._serialized_start=5271
  _TABLEVIEWDEFINITION._serialized_end=5314
  _DATASET._serialized_start=5317
  _DATASET._serialized_end=5756
  _DATASETINFO._serialized_start=5759
  _DATASETINFO._serialized_end=5985
  _DATASETINFO_LABELSENTRY._serialized_start=5212
  _DATASETINFO_LABELSENTRY._serialized_end=5269
  _BIGQUERYACL._serialized_start=5988
  _BIGQUERYACL._serialized_end=6309
  _BIGQUERYACL_ENTRY._serialized_start=6083
  _BIGQUERYACL_ENTRY._serialized_end=6309
  _JOB._serialized_start=6312
  _JOB._serialized_end=6648
  _JOBCONFIGURATION._serialized_start=6651
  _JOBCONFIGURATION._serialized_end=8696
  _JOBCONFIGURATION_QUERY._serialized_start=7129
  _JOBCONFIGURATION_QUERY._serialized_end=7718
  _JOBCONFIGURATION_LOAD._serialized_start=7721
  _JOBCONFIGURATION_LOAD._serialized_end=8091
  _JOBCONFIGURATION_EXTRACT._serialized_start=8094
  _JOBCONFIGURATION_EXTRACT._serialized_end=8226
  _JOBCONFIGURATION_TABLECOPY._serialized_start=8229
  _JOBCONFIGURATION_TABLECOPY._serialized_end=8620
  _JOBCONFIGURATION_LABELSENTRY._serialized_start=5212
  _JOBCONFIGURATION_LABELSENTRY._serialized_end=5269
  _TABLEDEFINITION._serialized_start=8698
  _TABLEDEFINITION._serialized_end=8768
  _JOBSTATUS._serialized_start=8771
  _JOBSTATUS._serialized_end=8911
  _JOBSTATISTICS._serialized_start=8914
  _JOBSTATISTICS._serialized_end=9857
  _JOBSTATISTICS_RESERVATIONRESOURCEUSAGE._serialized_start=9786
  _JOBSTATISTICS_RESERVATIONRESOURCEUSAGE._serialized_end=9857
  _DATASETNAME._serialized_start=9859
  _DATASETNAME._serialized_end=9934
  _TABLENAME._serialized_start=9936
  _TABLENAME._serialized_end=10036
  _JOBNAME._serialized_start=10038
  _JOBNAME._serialized_end=10129
  _ENCRYPTIONINFO._serialized_start=10131
  _ENCRYPTIONINFO._serialized_end=10181
# @@protoc_insertion_point(module_scope)
