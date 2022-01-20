"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.automl.v1.io_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class OperationMetadata(google.protobuf.message.Message):
    """Metadata used across all long running operations returned by AutoML API."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELETE_DETAILS_FIELD_NUMBER: builtins.int
    DEPLOY_MODEL_DETAILS_FIELD_NUMBER: builtins.int
    UNDEPLOY_MODEL_DETAILS_FIELD_NUMBER: builtins.int
    CREATE_MODEL_DETAILS_FIELD_NUMBER: builtins.int
    CREATE_DATASET_DETAILS_FIELD_NUMBER: builtins.int
    IMPORT_DATA_DETAILS_FIELD_NUMBER: builtins.int
    BATCH_PREDICT_DETAILS_FIELD_NUMBER: builtins.int
    EXPORT_DATA_DETAILS_FIELD_NUMBER: builtins.int
    EXPORT_MODEL_DETAILS_FIELD_NUMBER: builtins.int
    PROGRESS_PERCENT_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURES_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    @property
    def delete_details(self) -> global___DeleteOperationMetadata:
        """Details of a Delete operation."""
        pass
    @property
    def deploy_model_details(self) -> global___DeployModelOperationMetadata:
        """Details of a DeployModel operation."""
        pass
    @property
    def undeploy_model_details(self) -> global___UndeployModelOperationMetadata:
        """Details of an UndeployModel operation."""
        pass
    @property
    def create_model_details(self) -> global___CreateModelOperationMetadata:
        """Details of CreateModel operation."""
        pass
    @property
    def create_dataset_details(self) -> global___CreateDatasetOperationMetadata:
        """Details of CreateDataset operation."""
        pass
    @property
    def import_data_details(self) -> global___ImportDataOperationMetadata:
        """Details of ImportData operation."""
        pass
    @property
    def batch_predict_details(self) -> global___BatchPredictOperationMetadata:
        """Details of BatchPredict operation."""
        pass
    @property
    def export_data_details(self) -> global___ExportDataOperationMetadata:
        """Details of ExportData operation."""
        pass
    @property
    def export_model_details(self) -> global___ExportModelOperationMetadata:
        """Details of ExportModel operation."""
        pass
    progress_percent: builtins.int = ...
    """Output only. Progress of operation. Range: [0, 100].
    Not used currently.
    """

    @property
    def partial_failures(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.rpc.status_pb2.Status]:
        """Output only. Partial failures encountered.
        E.g. single files that couldn't be read.
        This field should never exceed 20 entries.
        Status details field will contain standard GCP error details.
        """
        pass
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Time when the operation was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Time when the operation was updated for the last time."""
        pass
    def __init__(self,
        *,
        delete_details : typing.Optional[global___DeleteOperationMetadata] = ...,
        deploy_model_details : typing.Optional[global___DeployModelOperationMetadata] = ...,
        undeploy_model_details : typing.Optional[global___UndeployModelOperationMetadata] = ...,
        create_model_details : typing.Optional[global___CreateModelOperationMetadata] = ...,
        create_dataset_details : typing.Optional[global___CreateDatasetOperationMetadata] = ...,
        import_data_details : typing.Optional[global___ImportDataOperationMetadata] = ...,
        batch_predict_details : typing.Optional[global___BatchPredictOperationMetadata] = ...,
        export_data_details : typing.Optional[global___ExportDataOperationMetadata] = ...,
        export_model_details : typing.Optional[global___ExportModelOperationMetadata] = ...,
        progress_percent : builtins.int = ...,
        partial_failures : typing.Optional[typing.Iterable[google.rpc.status_pb2.Status]] = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["batch_predict_details",b"batch_predict_details","create_dataset_details",b"create_dataset_details","create_model_details",b"create_model_details","create_time",b"create_time","delete_details",b"delete_details","deploy_model_details",b"deploy_model_details","details",b"details","export_data_details",b"export_data_details","export_model_details",b"export_model_details","import_data_details",b"import_data_details","undeploy_model_details",b"undeploy_model_details","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["batch_predict_details",b"batch_predict_details","create_dataset_details",b"create_dataset_details","create_model_details",b"create_model_details","create_time",b"create_time","delete_details",b"delete_details","deploy_model_details",b"deploy_model_details","details",b"details","export_data_details",b"export_data_details","export_model_details",b"export_model_details","import_data_details",b"import_data_details","partial_failures",b"partial_failures","progress_percent",b"progress_percent","undeploy_model_details",b"undeploy_model_details","update_time",b"update_time"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["details",b"details"]) -> typing.Optional[typing_extensions.Literal["delete_details","deploy_model_details","undeploy_model_details","create_model_details","create_dataset_details","import_data_details","batch_predict_details","export_data_details","export_model_details"]]: ...
global___OperationMetadata = OperationMetadata

class DeleteOperationMetadata(google.protobuf.message.Message):
    """Details of operations that perform deletes of any entities."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___DeleteOperationMetadata = DeleteOperationMetadata

class DeployModelOperationMetadata(google.protobuf.message.Message):
    """Details of DeployModel operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___DeployModelOperationMetadata = DeployModelOperationMetadata

class UndeployModelOperationMetadata(google.protobuf.message.Message):
    """Details of UndeployModel operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___UndeployModelOperationMetadata = UndeployModelOperationMetadata

class CreateDatasetOperationMetadata(google.protobuf.message.Message):
    """Details of CreateDataset operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___CreateDatasetOperationMetadata = CreateDatasetOperationMetadata

class CreateModelOperationMetadata(google.protobuf.message.Message):
    """Details of CreateModel operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___CreateModelOperationMetadata = CreateModelOperationMetadata

class ImportDataOperationMetadata(google.protobuf.message.Message):
    """Details of ImportData operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ImportDataOperationMetadata = ImportDataOperationMetadata

class ExportDataOperationMetadata(google.protobuf.message.Message):
    """Details of ExportData operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ExportDataOutputInfo(google.protobuf.message.Message):
        """Further describes this export data's output.
        Supplements
        [OutputConfig][google.cloud.automl.v1.OutputConfig].
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: builtins.int
        gcs_output_directory: typing.Text = ...
        """The full path of the Google Cloud Storage directory created, into which
        the exported data is written.
        """

        def __init__(self,
            *,
            gcs_output_directory : typing.Text = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["gcs_output_directory",b"gcs_output_directory","output_location",b"output_location"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["gcs_output_directory",b"gcs_output_directory","output_location",b"output_location"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["output_location",b"output_location"]) -> typing.Optional[typing_extensions.Literal["gcs_output_directory"]]: ...

    OUTPUT_INFO_FIELD_NUMBER: builtins.int
    @property
    def output_info(self) -> global___ExportDataOperationMetadata.ExportDataOutputInfo:
        """Output only. Information further describing this export data's output."""
        pass
    def __init__(self,
        *,
        output_info : typing.Optional[global___ExportDataOperationMetadata.ExportDataOutputInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["output_info",b"output_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["output_info",b"output_info"]) -> None: ...
global___ExportDataOperationMetadata = ExportDataOperationMetadata

class BatchPredictOperationMetadata(google.protobuf.message.Message):
    """Details of BatchPredict operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class BatchPredictOutputInfo(google.protobuf.message.Message):
        """Further describes this batch predict's output.
        Supplements
        [BatchPredictOutputConfig][google.cloud.automl.v1.BatchPredictOutputConfig].
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: builtins.int
        gcs_output_directory: typing.Text = ...
        """The full path of the Google Cloud Storage directory created, into which
        the prediction output is written.
        """

        def __init__(self,
            *,
            gcs_output_directory : typing.Text = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["gcs_output_directory",b"gcs_output_directory","output_location",b"output_location"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["gcs_output_directory",b"gcs_output_directory","output_location",b"output_location"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["output_location",b"output_location"]) -> typing.Optional[typing_extensions.Literal["gcs_output_directory"]]: ...

    INPUT_CONFIG_FIELD_NUMBER: builtins.int
    OUTPUT_INFO_FIELD_NUMBER: builtins.int
    @property
    def input_config(self) -> google.cloud.automl.v1.io_pb2.BatchPredictInputConfig:
        """Output only. The input config that was given upon starting this
        batch predict operation.
        """
        pass
    @property
    def output_info(self) -> global___BatchPredictOperationMetadata.BatchPredictOutputInfo:
        """Output only. Information further describing this batch predict's output."""
        pass
    def __init__(self,
        *,
        input_config : typing.Optional[google.cloud.automl.v1.io_pb2.BatchPredictInputConfig] = ...,
        output_info : typing.Optional[global___BatchPredictOperationMetadata.BatchPredictOutputInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["input_config",b"input_config","output_info",b"output_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["input_config",b"input_config","output_info",b"output_info"]) -> None: ...
global___BatchPredictOperationMetadata = BatchPredictOperationMetadata

class ExportModelOperationMetadata(google.protobuf.message.Message):
    """Details of ExportModel operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ExportModelOutputInfo(google.protobuf.message.Message):
        """Further describes the output of model export.
        Supplements
        [ModelExportOutputConfig][google.cloud.automl.v1.ModelExportOutputConfig].
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: builtins.int
        gcs_output_directory: typing.Text = ...
        """The full path of the Google Cloud Storage directory created, into which
        the model will be exported.
        """

        def __init__(self,
            *,
            gcs_output_directory : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["gcs_output_directory",b"gcs_output_directory"]) -> None: ...

    OUTPUT_INFO_FIELD_NUMBER: builtins.int
    @property
    def output_info(self) -> global___ExportModelOperationMetadata.ExportModelOutputInfo:
        """Output only. Information further describing the output of this model
        export.
        """
        pass
    def __init__(self,
        *,
        output_info : typing.Optional[global___ExportModelOperationMetadata.ExportModelOutputInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["output_info",b"output_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["output_info",b"output_info"]) -> None: ...
global___ExportModelOperationMetadata = ExportModelOperationMetadata
