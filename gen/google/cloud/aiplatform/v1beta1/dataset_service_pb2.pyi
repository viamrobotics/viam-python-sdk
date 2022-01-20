"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.aiplatform.v1beta1.annotation_pb2
import google.cloud.aiplatform.v1beta1.data_item_pb2
import google.cloud.aiplatform.v1beta1.dataset_pb2
import google.cloud.aiplatform.v1beta1.operation_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateDatasetRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.CreateDataset][google.cloud.aiplatform.v1beta1.DatasetService.CreateDataset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    DATASET_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The resource name of the Location to create the Dataset in.
    Format: `projects/{project}/locations/{location}`
    """

    @property
    def dataset(self) -> google.cloud.aiplatform.v1beta1.dataset_pb2.Dataset:
        """Required. The Dataset to create."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        dataset : typing.Optional[google.cloud.aiplatform.v1beta1.dataset_pb2.Dataset] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dataset",b"dataset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset",b"dataset","parent",b"parent"]) -> None: ...
global___CreateDatasetRequest = CreateDatasetRequest

class CreateDatasetOperationMetadata(google.protobuf.message.Message):
    """Runtime operation information for [DatasetService.CreateDataset][google.cloud.aiplatform.v1beta1.DatasetService.CreateDataset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GENERIC_METADATA_FIELD_NUMBER: builtins.int
    @property
    def generic_metadata(self) -> google.cloud.aiplatform.v1beta1.operation_pb2.GenericOperationMetadata:
        """The operation generic information."""
        pass
    def __init__(self,
        *,
        generic_metadata : typing.Optional[google.cloud.aiplatform.v1beta1.operation_pb2.GenericOperationMetadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["generic_metadata",b"generic_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["generic_metadata",b"generic_metadata"]) -> None: ...
global___CreateDatasetOperationMetadata = CreateDatasetOperationMetadata

class GetDatasetRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.GetDataset][google.cloud.aiplatform.v1beta1.DatasetService.GetDataset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    READ_MASK_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the Dataset resource."""

    @property
    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Mask specifying which fields to read."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        read_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","read_mask",b"read_mask"]) -> None: ...
global___GetDatasetRequest = GetDatasetRequest

class UpdateDatasetRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.UpdateDataset][google.cloud.aiplatform.v1beta1.DatasetService.UpdateDataset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATASET_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def dataset(self) -> google.cloud.aiplatform.v1beta1.dataset_pb2.Dataset:
        """Required. The Dataset which replaces the resource on the server."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Required. The update mask applies to the resource.
        For the `FieldMask` definition, see [google.protobuf.FieldMask][google.protobuf.FieldMask].
        Updatable fields:

          * `display_name`
          * `description`
          * `labels`
        """
        pass
    def __init__(self,
        *,
        dataset : typing.Optional[google.cloud.aiplatform.v1beta1.dataset_pb2.Dataset] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dataset",b"dataset","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataset",b"dataset","update_mask",b"update_mask"]) -> None: ...
global___UpdateDatasetRequest = UpdateDatasetRequest

class ListDatasetsRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.ListDatasets][google.cloud.aiplatform.v1beta1.DatasetService.ListDatasets]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    READ_MASK_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the Dataset's parent resource.
    Format: `projects/{project}/locations/{location}`
    """

    filter: typing.Text = ...
    """An expression for filtering the results of the request. For field names
    both snake_case and camelCase are supported.

      * `display_name`: supports = and !=
      * `metadata_schema_uri`: supports = and !=
      * `labels` supports general map functions that is:
        * `labels.key=value` - key:value equality
        * `labels.key:* or labels:key - key existence
        * A key including a space must be quoted. `labels."a key"`.

    Some examples:
      * `displayName="myDisplayName"`
      * `labels.myKey="myValue"`
    """

    page_size: builtins.int = ...
    """The standard list page size."""

    page_token: typing.Text = ...
    """The standard list page token."""

    @property
    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Mask specifying which fields to read."""
        pass
    order_by: typing.Text = ...
    """A comma-separated list of fields to order by, sorted in ascending order.
    Use "desc" after a field name for descending.
    Supported fields:
      * `display_name`
      * `create_time`
      * `update_time`
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        read_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","order_by",b"order_by","page_size",b"page_size","page_token",b"page_token","parent",b"parent","read_mask",b"read_mask"]) -> None: ...
global___ListDatasetsRequest = ListDatasetsRequest

class ListDatasetsResponse(google.protobuf.message.Message):
    """Response message for [DatasetService.ListDatasets][google.cloud.aiplatform.v1beta1.DatasetService.ListDatasets]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATASETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.aiplatform.v1beta1.dataset_pb2.Dataset]:
        """A list of Datasets that matches the specified filter in the request."""
        pass
    next_page_token: typing.Text = ...
    """The standard List next-page token."""

    def __init__(self,
        *,
        datasets : typing.Optional[typing.Iterable[google.cloud.aiplatform.v1beta1.dataset_pb2.Dataset]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["datasets",b"datasets","next_page_token",b"next_page_token"]) -> None: ...
global___ListDatasetsResponse = ListDatasetsResponse

class DeleteDatasetRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.DeleteDataset][google.cloud.aiplatform.v1beta1.DatasetService.DeleteDataset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the Dataset to delete.
    Format:
    `projects/{project}/locations/{location}/datasets/{dataset}`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteDatasetRequest = DeleteDatasetRequest

class ImportDataRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.ImportData][google.cloud.aiplatform.v1beta1.DatasetService.ImportData]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    IMPORT_CONFIGS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the Dataset resource.
    Format:
    `projects/{project}/locations/{location}/datasets/{dataset}`
    """

    @property
    def import_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.aiplatform.v1beta1.dataset_pb2.ImportDataConfig]:
        """Required. The desired input locations. The contents of all input locations will be
        imported in one batch.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        import_configs : typing.Optional[typing.Iterable[google.cloud.aiplatform.v1beta1.dataset_pb2.ImportDataConfig]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["import_configs",b"import_configs","name",b"name"]) -> None: ...
global___ImportDataRequest = ImportDataRequest

class ImportDataResponse(google.protobuf.message.Message):
    """Response message for [DatasetService.ImportData][google.cloud.aiplatform.v1beta1.DatasetService.ImportData]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ImportDataResponse = ImportDataResponse

class ImportDataOperationMetadata(google.protobuf.message.Message):
    """Runtime operation information for [DatasetService.ImportData][google.cloud.aiplatform.v1beta1.DatasetService.ImportData]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GENERIC_METADATA_FIELD_NUMBER: builtins.int
    @property
    def generic_metadata(self) -> google.cloud.aiplatform.v1beta1.operation_pb2.GenericOperationMetadata:
        """The common part of the operation metadata."""
        pass
    def __init__(self,
        *,
        generic_metadata : typing.Optional[google.cloud.aiplatform.v1beta1.operation_pb2.GenericOperationMetadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["generic_metadata",b"generic_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["generic_metadata",b"generic_metadata"]) -> None: ...
global___ImportDataOperationMetadata = ImportDataOperationMetadata

class ExportDataRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.ExportData][google.cloud.aiplatform.v1beta1.DatasetService.ExportData]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    EXPORT_CONFIG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the Dataset resource.
    Format:
    `projects/{project}/locations/{location}/datasets/{dataset}`
    """

    @property
    def export_config(self) -> google.cloud.aiplatform.v1beta1.dataset_pb2.ExportDataConfig:
        """Required. The desired output location."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        export_config : typing.Optional[google.cloud.aiplatform.v1beta1.dataset_pb2.ExportDataConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["export_config",b"export_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["export_config",b"export_config","name",b"name"]) -> None: ...
global___ExportDataRequest = ExportDataRequest

class ExportDataResponse(google.protobuf.message.Message):
    """Response message for [DatasetService.ExportData][google.cloud.aiplatform.v1beta1.DatasetService.ExportData]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXPORTED_FILES_FIELD_NUMBER: builtins.int
    @property
    def exported_files(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """All of the files that are exported in this export operation."""
        pass
    def __init__(self,
        *,
        exported_files : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exported_files",b"exported_files"]) -> None: ...
global___ExportDataResponse = ExportDataResponse

class ExportDataOperationMetadata(google.protobuf.message.Message):
    """Runtime operation information for [DatasetService.ExportData][google.cloud.aiplatform.v1beta1.DatasetService.ExportData]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GENERIC_METADATA_FIELD_NUMBER: builtins.int
    GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: builtins.int
    @property
    def generic_metadata(self) -> google.cloud.aiplatform.v1beta1.operation_pb2.GenericOperationMetadata:
        """The common part of the operation metadata."""
        pass
    gcs_output_directory: typing.Text = ...
    """A Google Cloud Storage directory which path ends with '/'. The exported
    data is stored in the directory.
    """

    def __init__(self,
        *,
        generic_metadata : typing.Optional[google.cloud.aiplatform.v1beta1.operation_pb2.GenericOperationMetadata] = ...,
        gcs_output_directory : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["generic_metadata",b"generic_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gcs_output_directory",b"gcs_output_directory","generic_metadata",b"generic_metadata"]) -> None: ...
global___ExportDataOperationMetadata = ExportDataOperationMetadata

class ListDataItemsRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.ListDataItems][google.cloud.aiplatform.v1beta1.DatasetService.ListDataItems]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    READ_MASK_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The resource name of the Dataset to list DataItems from.
    Format:
    `projects/{project}/locations/{location}/datasets/{dataset}`
    """

    filter: typing.Text = ...
    """The standard list filter."""

    page_size: builtins.int = ...
    """The standard list page size."""

    page_token: typing.Text = ...
    """The standard list page token."""

    @property
    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Mask specifying which fields to read."""
        pass
    order_by: typing.Text = ...
    """A comma-separated list of fields to order by, sorted in ascending order.
    Use "desc" after a field name for descending.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        read_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","order_by",b"order_by","page_size",b"page_size","page_token",b"page_token","parent",b"parent","read_mask",b"read_mask"]) -> None: ...
global___ListDataItemsRequest = ListDataItemsRequest

class ListDataItemsResponse(google.protobuf.message.Message):
    """Response message for [DatasetService.ListDataItems][google.cloud.aiplatform.v1beta1.DatasetService.ListDataItems]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_ITEMS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def data_items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.aiplatform.v1beta1.data_item_pb2.DataItem]:
        """A list of DataItems that matches the specified filter in the request."""
        pass
    next_page_token: typing.Text = ...
    """The standard List next-page token."""

    def __init__(self,
        *,
        data_items : typing.Optional[typing.Iterable[google.cloud.aiplatform.v1beta1.data_item_pb2.DataItem]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_items",b"data_items","next_page_token",b"next_page_token"]) -> None: ...
global___ListDataItemsResponse = ListDataItemsResponse

class GetAnnotationSpecRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.GetAnnotationSpec][google.cloud.aiplatform.v1beta1.DatasetService.GetAnnotationSpec]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    READ_MASK_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the AnnotationSpec resource.
    Format:
    `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`
    """

    @property
    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Mask specifying which fields to read."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        read_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","read_mask",b"read_mask"]) -> None: ...
global___GetAnnotationSpecRequest = GetAnnotationSpecRequest

class ListAnnotationsRequest(google.protobuf.message.Message):
    """Request message for [DatasetService.ListAnnotations][google.cloud.aiplatform.v1beta1.DatasetService.ListAnnotations]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    READ_MASK_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The resource name of the DataItem to list Annotations from.
    Format:
    `projects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}`
    """

    filter: typing.Text = ...
    """The standard list filter."""

    page_size: builtins.int = ...
    """The standard list page size."""

    page_token: typing.Text = ...
    """The standard list page token."""

    @property
    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Mask specifying which fields to read."""
        pass
    order_by: typing.Text = ...
    """A comma-separated list of fields to order by, sorted in ascending order.
    Use "desc" after a field name for descending.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        read_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","order_by",b"order_by","page_size",b"page_size","page_token",b"page_token","parent",b"parent","read_mask",b"read_mask"]) -> None: ...
global___ListAnnotationsRequest = ListAnnotationsRequest

class ListAnnotationsResponse(google.protobuf.message.Message):
    """Response message for [DatasetService.ListAnnotations][google.cloud.aiplatform.v1beta1.DatasetService.ListAnnotations]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def annotations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.aiplatform.v1beta1.annotation_pb2.Annotation]:
        """A list of Annotations that matches the specified filter in the request."""
        pass
    next_page_token: typing.Text = ...
    """The standard List next-page token."""

    def __init__(self,
        *,
        annotations : typing.Optional[typing.Iterable[google.cloud.aiplatform.v1beta1.annotation_pb2.Annotation]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotations",b"annotations","next_page_token",b"next_page_token"]) -> None: ...
global___ListAnnotationsResponse = ListAnnotationsResponse
