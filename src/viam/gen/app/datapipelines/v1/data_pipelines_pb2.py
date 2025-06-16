"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'app/datapipelines/v1/data_pipelines.proto')
_sym_db = _symbol_database.Default()
from ....app.data.v1 import data_pb2 as app_dot_data_dot_v1_dot_data__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)app/datapipelines/v1/data_pipelines.proto\x12\x19viam.app.datapipelines.v1\x1a\x16app/data/v1/data.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x93\x03\n\x0cDataPipeline\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x1d\n\nmql_binary\x18\x04 \x03(\x0cR\tmqlBinary\x12\x1a\n\x08schedule\x18\x05 \x01(\tR\x08schedule\x12\x18\n\x07enabled\x18\x06 \x01(\x08R\x07enabled\x129\n\ncreated_on\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x129\n\nupdated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12V\n\x10data_source_type\x18\t \x01(\x0e2\'.viam.app.data.v1.TabularDataSourceTypeH\x00R\x0edataSourceType\x88\x01\x01B\x13\n\x11_data_source_type"(\n\x16GetDataPipelineRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"g\n\x17GetDataPipelineResponse\x12L\n\rdata_pipeline\x18\x01 \x01(\x0b2\'.viam.app.datapipelines.v1.DataPipelineR\x0cdataPipeline"C\n\x18ListDataPipelinesRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"k\n\x19ListDataPipelinesResponse\x12N\n\x0edata_pipelines\x18\x01 \x03(\x0b2\'.viam.app.datapipelines.v1.DataPipelineR\rdataPipelines"\xc2\x02\n\x19CreateDataPipelineRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1d\n\nmql_binary\x18\x03 \x03(\x0cR\tmqlBinary\x12\x1a\n\x08schedule\x18\x04 \x01(\tR\x08schedule\x12,\n\x0fenable_backfill\x18\x05 \x01(\x08H\x00R\x0eenableBackfill\x88\x01\x01\x12V\n\x10data_source_type\x18\x06 \x01(\x0e2\'.viam.app.data.v1.TabularDataSourceTypeH\x01R\x0edataSourceType\x88\x01\x01B\x12\n\x10_enable_backfillB\x13\n\x11_data_source_type",\n\x1aCreateDataPipelineResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\xe7\x01\n\x19UpdateDataPipelineRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1d\n\nmql_binary\x18\x03 \x03(\x0cR\tmqlBinary\x12\x1a\n\x08schedule\x18\x04 \x01(\tR\x08schedule\x12V\n\x10data_source_type\x18\x05 \x01(\x0e2\'.viam.app.data.v1.TabularDataSourceTypeH\x00R\x0edataSourceType\x88\x01\x01B\x13\n\x11_data_source_type"\x1c\n\x1aUpdateDataPipelineResponse"+\n\x19DeleteDataPipelineRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1c\n\x1aDeleteDataPipelineResponse"+\n\x19EnableDataPipelineRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1c\n\x1aEnableDataPipelineResponse",\n\x1aDisableDataPipelineRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1d\n\x1bDisableDataPipelineResponse"i\n\x1bListDataPipelineRunsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken"\xa7\x01\n\x1cListDataPipelineRunsResponse\x12\x1f\n\x0bpipeline_id\x18\x01 \x01(\tR\npipelineId\x12>\n\x04runs\x18\x02 \x03(\x0b2*.viam.app.datapipelines.v1.DataPipelineRunR\x04runs\x12&\n\x0fnext_page_token\x18\x03 \x01(\tR\rnextPageToken"\xe1\x02\n\x0fDataPipelineRun\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x129\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartTime\x125\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07endTime\x12B\n\x0fdata_start_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\rdataStartTime\x12>\n\rdata_end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0bdataEndTime\x12H\n\x06status\x18\x06 \x01(\x0e20.viam.app.datapipelines.v1.DataPipelineRunStatusR\x06status*\xdc\x01\n\x15DataPipelineRunStatus\x12(\n$DATA_PIPELINE_RUN_STATUS_UNSPECIFIED\x10\x00\x12&\n"DATA_PIPELINE_RUN_STATUS_SCHEDULED\x10\x01\x12$\n DATA_PIPELINE_RUN_STATUS_STARTED\x10\x02\x12&\n"DATA_PIPELINE_RUN_STATUS_COMPLETED\x10\x03\x12#\n\x1fDATA_PIPELINE_RUN_STATUS_FAILED\x10\x042\xb1\x08\n\x14DataPipelinesService\x12x\n\x0fGetDataPipeline\x121.viam.app.datapipelines.v1.GetDataPipelineRequest\x1a2.viam.app.datapipelines.v1.GetDataPipelineResponse\x12~\n\x11ListDataPipelines\x123.viam.app.datapipelines.v1.ListDataPipelinesRequest\x1a4.viam.app.datapipelines.v1.ListDataPipelinesResponse\x12\x81\x01\n\x12CreateDataPipeline\x124.viam.app.datapipelines.v1.CreateDataPipelineRequest\x1a5.viam.app.datapipelines.v1.CreateDataPipelineResponse\x12\x81\x01\n\x12UpdateDataPipeline\x124.viam.app.datapipelines.v1.UpdateDataPipelineRequest\x1a5.viam.app.datapipelines.v1.UpdateDataPipelineResponse\x12\x81\x01\n\x12DeleteDataPipeline\x124.viam.app.datapipelines.v1.DeleteDataPipelineRequest\x1a5.viam.app.datapipelines.v1.DeleteDataPipelineResponse\x12\x81\x01\n\x12EnableDataPipeline\x124.viam.app.datapipelines.v1.EnableDataPipelineRequest\x1a5.viam.app.datapipelines.v1.EnableDataPipelineResponse\x12\x84\x01\n\x13DisableDataPipeline\x125.viam.app.datapipelines.v1.DisableDataPipelineRequest\x1a6.viam.app.datapipelines.v1.DisableDataPipelineResponse\x12\x87\x01\n\x14ListDataPipelineRuns\x126.viam.app.datapipelines.v1.ListDataPipelineRunsRequest\x1a7.viam.app.datapipelines.v1.ListDataPipelineRunsResponseB&Z$go.viam.com/api/app/datapipelines/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.datapipelines.v1.data_pipelines_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z$go.viam.com/api/app/datapipelines/v1'
    _globals['_DATAPIPELINERUNSTATUS']._serialized_start = 2356
    _globals['_DATAPIPELINERUNSTATUS']._serialized_end = 2576
    _globals['_DATAPIPELINE']._serialized_start = 130
    _globals['_DATAPIPELINE']._serialized_end = 533
    _globals['_GETDATAPIPELINEREQUEST']._serialized_start = 535
    _globals['_GETDATAPIPELINEREQUEST']._serialized_end = 575
    _globals['_GETDATAPIPELINERESPONSE']._serialized_start = 577
    _globals['_GETDATAPIPELINERESPONSE']._serialized_end = 680
    _globals['_LISTDATAPIPELINESREQUEST']._serialized_start = 682
    _globals['_LISTDATAPIPELINESREQUEST']._serialized_end = 749
    _globals['_LISTDATAPIPELINESRESPONSE']._serialized_start = 751
    _globals['_LISTDATAPIPELINESRESPONSE']._serialized_end = 858
    _globals['_CREATEDATAPIPELINEREQUEST']._serialized_start = 861
    _globals['_CREATEDATAPIPELINEREQUEST']._serialized_end = 1183
    _globals['_CREATEDATAPIPELINERESPONSE']._serialized_start = 1185
    _globals['_CREATEDATAPIPELINERESPONSE']._serialized_end = 1229
    _globals['_UPDATEDATAPIPELINEREQUEST']._serialized_start = 1232
    _globals['_UPDATEDATAPIPELINEREQUEST']._serialized_end = 1463
    _globals['_UPDATEDATAPIPELINERESPONSE']._serialized_start = 1465
    _globals['_UPDATEDATAPIPELINERESPONSE']._serialized_end = 1493
    _globals['_DELETEDATAPIPELINEREQUEST']._serialized_start = 1495
    _globals['_DELETEDATAPIPELINEREQUEST']._serialized_end = 1538
    _globals['_DELETEDATAPIPELINERESPONSE']._serialized_start = 1540
    _globals['_DELETEDATAPIPELINERESPONSE']._serialized_end = 1568
    _globals['_ENABLEDATAPIPELINEREQUEST']._serialized_start = 1570
    _globals['_ENABLEDATAPIPELINEREQUEST']._serialized_end = 1613
    _globals['_ENABLEDATAPIPELINERESPONSE']._serialized_start = 1615
    _globals['_ENABLEDATAPIPELINERESPONSE']._serialized_end = 1643
    _globals['_DISABLEDATAPIPELINEREQUEST']._serialized_start = 1645
    _globals['_DISABLEDATAPIPELINEREQUEST']._serialized_end = 1689
    _globals['_DISABLEDATAPIPELINERESPONSE']._serialized_start = 1691
    _globals['_DISABLEDATAPIPELINERESPONSE']._serialized_end = 1720
    _globals['_LISTDATAPIPELINERUNSREQUEST']._serialized_start = 1722
    _globals['_LISTDATAPIPELINERUNSREQUEST']._serialized_end = 1827
    _globals['_LISTDATAPIPELINERUNSRESPONSE']._serialized_start = 1830
    _globals['_LISTDATAPIPELINERUNSRESPONSE']._serialized_end = 1997
    _globals['_DATAPIPELINERUN']._serialized_start = 2000
    _globals['_DATAPIPELINERUN']._serialized_end = 2353
    _globals['_DATAPIPELINESSERVICE']._serialized_start = 2579
    _globals['_DATAPIPELINESSERVICE']._serialized_end = 3652