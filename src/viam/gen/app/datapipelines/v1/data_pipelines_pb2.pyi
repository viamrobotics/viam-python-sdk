"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DataPipeline(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MQL_BINARY_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    CREATED_ON_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    organization_id: builtins.str
    'The associated Viam organization ID.'
    name: builtins.str
    'A unique identifier at the org level.'
    schedule: builtins.str
    'A cron expression representing the expected execution schedule in UTC (note this also\n    defines the input time window; an hourly schedule would process 1 hour of data at a time).\n    '
    enabled: builtins.bool
    'Whether or not the pipeline is enabled.'

    @property
    def mql_binary(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """A MongoDB aggregation pipeline as a list of BSON documents, where
        each document is one stage in the pipeline.
        """

    @property
    def created_on(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time the pipeline was created."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time the pipeline was last updated."""

    def __init__(self, *, id: builtins.str=..., organization_id: builtins.str=..., name: builtins.str=..., mql_binary: collections.abc.Iterable[builtins.bytes] | None=..., schedule: builtins.str=..., enabled: builtins.bool=..., created_on: google.protobuf.timestamp_pb2.Timestamp | None=..., updated_at: google.protobuf.timestamp_pb2.Timestamp | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['created_on', b'created_on', 'updated_at', b'updated_at']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['created_on', b'created_on', 'enabled', b'enabled', 'id', b'id', 'mql_binary', b'mql_binary', 'name', b'name', 'organization_id', b'organization_id', 'schedule', b'schedule', 'updated_at', b'updated_at']) -> None:
        ...
global___DataPipeline = DataPipeline

@typing.final
class GetDataPipelineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    'The ID of the data pipeline to retrieve.'

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['id', b'id']) -> None:
        ...
global___GetDataPipelineRequest = GetDataPipelineRequest

@typing.final
class GetDataPipelineResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_PIPELINE_FIELD_NUMBER: builtins.int

    @property
    def data_pipeline(self) -> global___DataPipeline:
        ...

    def __init__(self, *, data_pipeline: global___DataPipeline | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['data_pipeline', b'data_pipeline']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['data_pipeline', b'data_pipeline']) -> None:
        ...
global___GetDataPipelineResponse = GetDataPipelineResponse

@typing.final
class ListDataPipelinesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    'The associated Viam organization ID.'

    def __init__(self, *, organization_id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['organization_id', b'organization_id']) -> None:
        ...
global___ListDataPipelinesRequest = ListDataPipelinesRequest

@typing.final
class ListDataPipelinesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_PIPELINES_FIELD_NUMBER: builtins.int

    @property
    def data_pipelines(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DataPipeline]:
        ...

    def __init__(self, *, data_pipelines: collections.abc.Iterable[global___DataPipeline] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['data_pipelines', b'data_pipelines']) -> None:
        ...
global___ListDataPipelinesResponse = ListDataPipelinesResponse

@typing.final
class CreateDataPipelineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MQL_BINARY_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    'The associated Viam organization ID.'
    name: builtins.str
    'A unique identifier at the org level.'
    schedule: builtins.str
    'A cron expression representing the expected execution schedule in UTC (note this also\n    defines the input time window; an hourly schedule would process 1 hour of data at a time).\n    '

    @property
    def mql_binary(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """A MongoDB aggregation pipeline as a list of BSON documents, where
        each document is one stage in the pipeline.
        """

    def __init__(self, *, organization_id: builtins.str=..., name: builtins.str=..., mql_binary: collections.abc.Iterable[builtins.bytes] | None=..., schedule: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['mql_binary', b'mql_binary', 'name', b'name', 'organization_id', b'organization_id', 'schedule', b'schedule']) -> None:
        ...
global___CreateDataPipelineRequest = CreateDataPipelineRequest

@typing.final
class CreateDataPipelineResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    'The ID of the newly created data pipeline.'

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['id', b'id']) -> None:
        ...
global___CreateDataPipelineResponse = CreateDataPipelineResponse

@typing.final
class UpdateDataPipelineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MQL_BINARY_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    id: builtins.str
    'The ID of the data pipeline to update.'
    name: builtins.str
    'A unique identifier at the org level.'
    schedule: builtins.str
    'A cron expression representing the expected execution schedule in UTC (note this also\n    defines the input time window; an hourly schedule would process 1 hour of data at a time).\n    '
    enabled: builtins.bool
    'Whether or not the pipeline is enabled.'

    @property
    def mql_binary(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """A MongoDB aggregation pipeline as a list of BSON documents, where
        each document is one stage in the pipeline.
        """

    def __init__(self, *, id: builtins.str=..., name: builtins.str=..., mql_binary: collections.abc.Iterable[builtins.bytes] | None=..., schedule: builtins.str=..., enabled: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['enabled', b'enabled', 'id', b'id', 'mql_binary', b'mql_binary', 'name', b'name', 'schedule', b'schedule']) -> None:
        ...
global___UpdateDataPipelineRequest = UpdateDataPipelineRequest

@typing.final
class UpdateDataPipelineResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___UpdateDataPipelineResponse = UpdateDataPipelineResponse

@typing.final
class DeleteDataPipelineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    'The ID of the data pipeline to delete.'

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['id', b'id']) -> None:
        ...
global___DeleteDataPipelineRequest = DeleteDataPipelineRequest

@typing.final
class DeleteDataPipelineResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___DeleteDataPipelineResponse = DeleteDataPipelineResponse