"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.automl.v1.dataset_pb2
import google.cloud.automl.v1.image_pb2
import google.cloud.automl.v1.io_pb2
import google.cloud.automl.v1.model_evaluation_pb2
import google.cloud.automl.v1.model_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateDatasetRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.CreateDataset][google.cloud.automl.v1.AutoMl.CreateDataset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    DATASET_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The resource name of the project to create the dataset for."""

    @property
    def dataset(self) -> google.cloud.automl.v1.dataset_pb2.Dataset:
        """Required. The dataset to create."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        dataset : typing.Optional[google.cloud.automl.v1.dataset_pb2.Dataset] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dataset",b"dataset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset",b"dataset","parent",b"parent"]) -> None: ...
global___CreateDatasetRequest = CreateDatasetRequest

class GetDatasetRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.GetDataset][google.cloud.automl.v1.AutoMl.GetDataset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the dataset to retrieve."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetDatasetRequest = GetDatasetRequest

class ListDatasetsRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.ListDatasets][google.cloud.automl.v1.AutoMl.ListDatasets]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The resource name of the project from which to list datasets."""

    filter: typing.Text = ...
    """An expression for filtering the results of the request.

      * `dataset_metadata` - for existence of the case (e.g.
                `image_classification_dataset_metadata:*`). Some examples of using the filter are:

      * `translation_dataset_metadata:*` --> The dataset has
                                             `translation_dataset_metadata`.
    """

    page_size: builtins.int = ...
    """Requested page size. Server may return fewer results than requested.
    If unspecified, server will pick a default size.
    """

    page_token: typing.Text = ...
    """A token identifying a page of results for the server to return
    Typically obtained via
    [ListDatasetsResponse.next_page_token][google.cloud.automl.v1.ListDatasetsResponse.next_page_token] of the previous
    [AutoMl.ListDatasets][google.cloud.automl.v1.AutoMl.ListDatasets] call.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListDatasetsRequest = ListDatasetsRequest

class ListDatasetsResponse(google.protobuf.message.Message):
    """Response message for [AutoMl.ListDatasets][google.cloud.automl.v1.AutoMl.ListDatasets]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATASETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.automl.v1.dataset_pb2.Dataset]:
        """The datasets read."""
        pass
    next_page_token: typing.Text = ...
    """A token to retrieve next page of results.
    Pass to [ListDatasetsRequest.page_token][google.cloud.automl.v1.ListDatasetsRequest.page_token] to obtain that page.
    """

    def __init__(self,
        *,
        datasets : typing.Optional[typing.Iterable[google.cloud.automl.v1.dataset_pb2.Dataset]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["datasets",b"datasets","next_page_token",b"next_page_token"]) -> None: ...
global___ListDatasetsResponse = ListDatasetsResponse

class UpdateDatasetRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.UpdateDataset][google.cloud.automl.v1.AutoMl.UpdateDataset]"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATASET_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def dataset(self) -> google.cloud.automl.v1.dataset_pb2.Dataset:
        """Required. The dataset which replaces the resource on the server."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Required. The update mask applies to the resource."""
        pass
    def __init__(self,
        *,
        dataset : typing.Optional[google.cloud.automl.v1.dataset_pb2.Dataset] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dataset",b"dataset","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset",b"dataset","update_mask",b"update_mask"]) -> None: ...
global___UpdateDatasetRequest = UpdateDatasetRequest

class DeleteDatasetRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.DeleteDataset][google.cloud.automl.v1.AutoMl.DeleteDataset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the dataset to delete."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteDatasetRequest = DeleteDatasetRequest

class ImportDataRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.ImportData][google.cloud.automl.v1.AutoMl.ImportData]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    INPUT_CONFIG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Dataset name. Dataset must already exist. All imported
    annotations and examples will be added.
    """

    @property
    def input_config(self) -> google.cloud.automl.v1.io_pb2.InputConfig:
        """Required. The desired input location and its domain specific semantics,
        if any.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        input_config : typing.Optional[google.cloud.automl.v1.io_pb2.InputConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["input_config",b"input_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["input_config",b"input_config","name",b"name"]) -> None: ...
global___ImportDataRequest = ImportDataRequest

class ExportDataRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.ExportData][google.cloud.automl.v1.AutoMl.ExportData]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    OUTPUT_CONFIG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the dataset."""

    @property
    def output_config(self) -> google.cloud.automl.v1.io_pb2.OutputConfig:
        """Required. The desired output location."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        output_config : typing.Optional[google.cloud.automl.v1.io_pb2.OutputConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["output_config",b"output_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","output_config",b"output_config"]) -> None: ...
global___ExportDataRequest = ExportDataRequest

class GetAnnotationSpecRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.GetAnnotationSpec][google.cloud.automl.v1.AutoMl.GetAnnotationSpec]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the annotation spec to retrieve."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetAnnotationSpecRequest = GetAnnotationSpecRequest

class CreateModelRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.CreateModel][google.cloud.automl.v1.AutoMl.CreateModel]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. Resource name of the parent project where the model is being created."""

    @property
    def model(self) -> google.cloud.automl.v1.model_pb2.Model:
        """Required. The model to create."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        model : typing.Optional[google.cloud.automl.v1.model_pb2.Model] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["model",b"model"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["model",b"model","parent",b"parent"]) -> None: ...
global___CreateModelRequest = CreateModelRequest

class GetModelRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.GetModel][google.cloud.automl.v1.AutoMl.GetModel]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Resource name of the model."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetModelRequest = GetModelRequest

class ListModelsRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.ListModels][google.cloud.automl.v1.AutoMl.ListModels]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. Resource name of the project, from which to list the models."""

    filter: typing.Text = ...
    """An expression for filtering the results of the request.

      * `model_metadata` - for existence of the case (e.g.
                `video_classification_model_metadata:*`).
      * `dataset_id` - for = or !=. Some examples of using the filter are:

      * `image_classification_model_metadata:*` --> The model has
                                         `image_classification_model_metadata`.
      * `dataset_id=5` --> The model was created from a dataset with ID 5.
    """

    page_size: builtins.int = ...
    """Requested page size."""

    page_token: typing.Text = ...
    """A token identifying a page of results for the server to return
    Typically obtained via
    [ListModelsResponse.next_page_token][google.cloud.automl.v1.ListModelsResponse.next_page_token] of the previous
    [AutoMl.ListModels][google.cloud.automl.v1.AutoMl.ListModels] call.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListModelsRequest = ListModelsRequest

class ListModelsResponse(google.protobuf.message.Message):
    """Response message for [AutoMl.ListModels][google.cloud.automl.v1.AutoMl.ListModels]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MODEL_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def model(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.automl.v1.model_pb2.Model]:
        """List of models in the requested page."""
        pass
    next_page_token: typing.Text = ...
    """A token to retrieve next page of results.
    Pass to [ListModelsRequest.page_token][google.cloud.automl.v1.ListModelsRequest.page_token] to obtain that page.
    """

    def __init__(self,
        *,
        model : typing.Optional[typing.Iterable[google.cloud.automl.v1.model_pb2.Model]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model",b"model","next_page_token",b"next_page_token"]) -> None: ...
global___ListModelsResponse = ListModelsResponse

class DeleteModelRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.DeleteModel][google.cloud.automl.v1.AutoMl.DeleteModel]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Resource name of the model being deleted."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteModelRequest = DeleteModelRequest

class UpdateModelRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.UpdateModel][google.cloud.automl.v1.AutoMl.UpdateModel]"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MODEL_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def model(self) -> google.cloud.automl.v1.model_pb2.Model:
        """Required. The model which replaces the resource on the server."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Required. The update mask applies to the resource."""
        pass
    def __init__(self,
        *,
        model : typing.Optional[google.cloud.automl.v1.model_pb2.Model] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["model",b"model","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["model",b"model","update_mask",b"update_mask"]) -> None: ...
global___UpdateModelRequest = UpdateModelRequest

class DeployModelRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.DeployModel][google.cloud.automl.v1.AutoMl.DeployModel]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IMAGE_OBJECT_DETECTION_MODEL_DEPLOYMENT_METADATA_FIELD_NUMBER: builtins.int
    IMAGE_CLASSIFICATION_MODEL_DEPLOYMENT_METADATA_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def image_object_detection_model_deployment_metadata(self) -> google.cloud.automl.v1.image_pb2.ImageObjectDetectionModelDeploymentMetadata:
        """Model deployment metadata specific to Image Object Detection."""
        pass
    @property
    def image_classification_model_deployment_metadata(self) -> google.cloud.automl.v1.image_pb2.ImageClassificationModelDeploymentMetadata:
        """Model deployment metadata specific to Image Classification."""
        pass
    name: typing.Text = ...
    """Required. Resource name of the model to deploy."""

    def __init__(self,
        *,
        image_object_detection_model_deployment_metadata : typing.Optional[google.cloud.automl.v1.image_pb2.ImageObjectDetectionModelDeploymentMetadata] = ...,
        image_classification_model_deployment_metadata : typing.Optional[google.cloud.automl.v1.image_pb2.ImageClassificationModelDeploymentMetadata] = ...,
        name : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["image_classification_model_deployment_metadata",b"image_classification_model_deployment_metadata","image_object_detection_model_deployment_metadata",b"image_object_detection_model_deployment_metadata","model_deployment_metadata",b"model_deployment_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_classification_model_deployment_metadata",b"image_classification_model_deployment_metadata","image_object_detection_model_deployment_metadata",b"image_object_detection_model_deployment_metadata","model_deployment_metadata",b"model_deployment_metadata","name",b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["model_deployment_metadata",b"model_deployment_metadata"]) -> typing.Optional[typing_extensions.Literal["image_object_detection_model_deployment_metadata","image_classification_model_deployment_metadata"]]: ...
global___DeployModelRequest = DeployModelRequest

class UndeployModelRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.UndeployModel][google.cloud.automl.v1.AutoMl.UndeployModel]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Resource name of the model to undeploy."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___UndeployModelRequest = UndeployModelRequest

class ExportModelRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel].
    Models need to be enabled for exporting, otherwise an error code will be
    returned.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    OUTPUT_CONFIG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the model to export."""

    @property
    def output_config(self) -> google.cloud.automl.v1.io_pb2.ModelExportOutputConfig:
        """Required. The desired output location and configuration."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        output_config : typing.Optional[google.cloud.automl.v1.io_pb2.ModelExportOutputConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["output_config",b"output_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","output_config",b"output_config"]) -> None: ...
global___ExportModelRequest = ExportModelRequest

class GetModelEvaluationRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.GetModelEvaluation][google.cloud.automl.v1.AutoMl.GetModelEvaluation]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Resource name for the model evaluation."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetModelEvaluationRequest = GetModelEvaluationRequest

class ListModelEvaluationsRequest(google.protobuf.message.Message):
    """Request message for [AutoMl.ListModelEvaluations][google.cloud.automl.v1.AutoMl.ListModelEvaluations]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. Resource name of the model to list the model evaluations for.
    If modelId is set as "-", this will list model evaluations from across all
    models of the parent location.
    """

    filter: typing.Text = ...
    """Required. An expression for filtering the results of the request.

      * `annotation_spec_id` - for =, !=  or existence. See example below for
                             the last.

    Some examples of using the filter are:

      * `annotation_spec_id!=4` --> The model evaluation was done for
                                annotation spec with ID different than 4.
      * `NOT annotation_spec_id:*` --> The model evaluation was done for
                                   aggregate of all annotation specs.
    """

    page_size: builtins.int = ...
    """Requested page size."""

    page_token: typing.Text = ...
    """A token identifying a page of results for the server to return.
    Typically obtained via
    [ListModelEvaluationsResponse.next_page_token][google.cloud.automl.v1.ListModelEvaluationsResponse.next_page_token] of the previous
    [AutoMl.ListModelEvaluations][google.cloud.automl.v1.AutoMl.ListModelEvaluations] call.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListModelEvaluationsRequest = ListModelEvaluationsRequest

class ListModelEvaluationsResponse(google.protobuf.message.Message):
    """Response message for [AutoMl.ListModelEvaluations][google.cloud.automl.v1.AutoMl.ListModelEvaluations]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MODEL_EVALUATION_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def model_evaluation(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.automl.v1.model_evaluation_pb2.ModelEvaluation]:
        """List of model evaluations in the requested page."""
        pass
    next_page_token: typing.Text = ...
    """A token to retrieve next page of results.
    Pass to the [ListModelEvaluationsRequest.page_token][google.cloud.automl.v1.ListModelEvaluationsRequest.page_token] field of a new
    [AutoMl.ListModelEvaluations][google.cloud.automl.v1.AutoMl.ListModelEvaluations] request to obtain that page.
    """

    def __init__(self,
        *,
        model_evaluation : typing.Optional[typing.Iterable[google.cloud.automl.v1.model_evaluation_pb2.ModelEvaluation]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_evaluation",b"model_evaluation","next_page_token",b"next_page_token"]) -> None: ...
global___ListModelEvaluationsResponse = ListModelEvaluationsResponse
