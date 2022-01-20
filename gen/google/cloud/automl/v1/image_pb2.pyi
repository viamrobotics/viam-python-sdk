"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.automl.v1.classification_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ImageClassificationDatasetMetadata(google.protobuf.message.Message):
    """Dataset metadata that is specific to image classification."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLASSIFICATION_TYPE_FIELD_NUMBER: builtins.int
    classification_type: google.cloud.automl.v1.classification_pb2.ClassificationType.ValueType = ...
    """Required. Type of the classification problem."""

    def __init__(self,
        *,
        classification_type : google.cloud.automl.v1.classification_pb2.ClassificationType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["classification_type",b"classification_type"]) -> None: ...
global___ImageClassificationDatasetMetadata = ImageClassificationDatasetMetadata

class ImageObjectDetectionDatasetMetadata(google.protobuf.message.Message):
    """Dataset metadata specific to image object detection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ImageObjectDetectionDatasetMetadata = ImageObjectDetectionDatasetMetadata

class ImageClassificationModelMetadata(google.protobuf.message.Message):
    """Model metadata for image classification."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BASE_MODEL_ID_FIELD_NUMBER: builtins.int
    TRAIN_BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: builtins.int
    TRAIN_COST_MILLI_NODE_HOURS_FIELD_NUMBER: builtins.int
    STOP_REASON_FIELD_NUMBER: builtins.int
    MODEL_TYPE_FIELD_NUMBER: builtins.int
    NODE_QPS_FIELD_NUMBER: builtins.int
    NODE_COUNT_FIELD_NUMBER: builtins.int
    base_model_id: typing.Text = ...
    """Optional. The ID of the `base` model. If it is specified, the new model
    will be created based on the `base` model. Otherwise, the new model will be
    created from scratch. The `base` model must be in the same
    `project` and `location` as the new model to create, and have the same
    `model_type`.
    """

    train_budget_milli_node_hours: builtins.int = ...
    """Optional. The train budget of creating this model, expressed in milli node
    hours i.e. 1,000 value in this field means 1 node hour. The actual
    `train_cost` will be equal or less than this value. If further model
    training ceases to provide any improvements, it will stop without using
    full budget and the stop_reason will be `MODEL_CONVERGED`.
    Note, node_hour  = actual_hour * number_of_nodes_invovled.
    For model type `cloud`(default), the train budget must be between 8,000
    and 800,000 milli node hours, inclusive. The default value is 192, 000
    which represents one day in wall time. For model type
    `mobile-low-latency-1`, `mobile-versatile-1`, `mobile-high-accuracy-1`,
    `mobile-core-ml-low-latency-1`, `mobile-core-ml-versatile-1`,
    `mobile-core-ml-high-accuracy-1`, the train budget must be between 1,000
    and 100,000 milli node hours, inclusive. The default value is 24, 000 which
    represents one day in wall time.
    """

    train_cost_milli_node_hours: builtins.int = ...
    """Output only. The actual train cost of creating this model, expressed in
    milli node hours, i.e. 1,000 value in this field means 1 node hour.
    Guaranteed to not exceed the train budget.
    """

    stop_reason: typing.Text = ...
    """Output only. The reason that this create model operation stopped,
    e.g. `BUDGET_REACHED`, `MODEL_CONVERGED`.
    """

    model_type: typing.Text = ...
    """Optional. Type of the model. The available values are:
    *   `cloud` - Model to be used via prediction calls to AutoML API.
                  This is the default value.
    *   `mobile-low-latency-1` - A model that, in addition to providing
                  prediction via AutoML API, can also be exported (see
                  [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile or edge device
                  with TensorFlow afterwards. Expected to have low latency, but
                  may have lower prediction quality than other models.
    *   `mobile-versatile-1` - A model that, in addition to providing
                  prediction via AutoML API, can also be exported (see
                  [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile or edge device
                  with TensorFlow afterwards.
    *   `mobile-high-accuracy-1` - A model that, in addition to providing
                  prediction via AutoML API, can also be exported (see
                  [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile or edge device
                  with TensorFlow afterwards.  Expected to have a higher
                  latency, but should also have a higher prediction quality
                  than other models.
    *   `mobile-core-ml-low-latency-1` - A model that, in addition to providing
                  prediction via AutoML API, can also be exported (see
                  [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile device with Core
                  ML afterwards. Expected to have low latency, but may have
                  lower prediction quality than other models.
    *   `mobile-core-ml-versatile-1` - A model that, in addition to providing
                  prediction via AutoML API, can also be exported (see
                  [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile device with Core
                  ML afterwards.
    *   `mobile-core-ml-high-accuracy-1` - A model that, in addition to
                  providing prediction via AutoML API, can also be exported
                  (see [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile device with
                  Core ML afterwards.  Expected to have a higher latency, but
                  should also have a higher prediction quality than other
                  models.
    """

    node_qps: builtins.float = ...
    """Output only. An approximate number of online prediction QPS that can
    be supported by this model per each node on which it is deployed.
    """

    node_count: builtins.int = ...
    """Output only. The number of nodes this model is deployed on. A node is an
    abstraction of a machine resource, which can handle online prediction QPS
    as given in the node_qps field.
    """

    def __init__(self,
        *,
        base_model_id : typing.Text = ...,
        train_budget_milli_node_hours : builtins.int = ...,
        train_cost_milli_node_hours : builtins.int = ...,
        stop_reason : typing.Text = ...,
        model_type : typing.Text = ...,
        node_qps : builtins.float = ...,
        node_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_model_id",b"base_model_id","model_type",b"model_type","node_count",b"node_count","node_qps",b"node_qps","stop_reason",b"stop_reason","train_budget_milli_node_hours",b"train_budget_milli_node_hours","train_cost_milli_node_hours",b"train_cost_milli_node_hours"]) -> None: ...
global___ImageClassificationModelMetadata = ImageClassificationModelMetadata

class ImageObjectDetectionModelMetadata(google.protobuf.message.Message):
    """Model metadata specific to image object detection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MODEL_TYPE_FIELD_NUMBER: builtins.int
    NODE_COUNT_FIELD_NUMBER: builtins.int
    NODE_QPS_FIELD_NUMBER: builtins.int
    STOP_REASON_FIELD_NUMBER: builtins.int
    TRAIN_BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: builtins.int
    TRAIN_COST_MILLI_NODE_HOURS_FIELD_NUMBER: builtins.int
    model_type: typing.Text = ...
    """Optional. Type of the model. The available values are:
    *   `cloud-high-accuracy-1` - (default) A model to be used via prediction
                  calls to AutoML API. Expected to have a higher latency, but
                  should also have a higher prediction quality than other
                  models.
    *   `cloud-low-latency-1` -  A model to be used via prediction
                  calls to AutoML API. Expected to have low latency, but may
                  have lower prediction quality than other models.
    *   `mobile-low-latency-1` - A model that, in addition to providing
                  prediction via AutoML API, can also be exported (see
                  [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile or edge device
                  with TensorFlow afterwards. Expected to have low latency, but
                  may have lower prediction quality than other models.
    *   `mobile-versatile-1` - A model that, in addition to providing
                  prediction via AutoML API, can also be exported (see
                  [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile or edge device
                  with TensorFlow afterwards.
    *   `mobile-high-accuracy-1` - A model that, in addition to providing
                  prediction via AutoML API, can also be exported (see
                  [AutoMl.ExportModel][google.cloud.automl.v1.AutoMl.ExportModel]) and used on a mobile or edge device
                  with TensorFlow afterwards.  Expected to have a higher
                  latency, but should also have a higher prediction quality
                  than other models.
    """

    node_count: builtins.int = ...
    """Output only. The number of nodes this model is deployed on. A node is an
    abstraction of a machine resource, which can handle online prediction QPS
    as given in the qps_per_node field.
    """

    node_qps: builtins.float = ...
    """Output only. An approximate number of online prediction QPS that can
    be supported by this model per each node on which it is deployed.
    """

    stop_reason: typing.Text = ...
    """Output only. The reason that this create model operation stopped,
    e.g. `BUDGET_REACHED`, `MODEL_CONVERGED`.
    """

    train_budget_milli_node_hours: builtins.int = ...
    """Optional. The train budget of creating this model, expressed in milli node
    hours i.e. 1,000 value in this field means 1 node hour. The actual
    `train_cost` will be equal or less than this value. If further model
    training ceases to provide any improvements, it will stop without using
    full budget and the stop_reason will be `MODEL_CONVERGED`.
    Note, node_hour  = actual_hour * number_of_nodes_invovled.
    For model type `cloud-high-accuracy-1`(default) and `cloud-low-latency-1`,
    the train budget must be between 20,000 and 900,000 milli node hours,
    inclusive. The default value is 216, 000 which represents one day in
    wall time.
    For model type `mobile-low-latency-1`, `mobile-versatile-1`,
    `mobile-high-accuracy-1`, `mobile-core-ml-low-latency-1`,
    `mobile-core-ml-versatile-1`, `mobile-core-ml-high-accuracy-1`, the train
    budget must be between 1,000 and 100,000 milli node hours, inclusive.
    The default value is 24, 000 which represents one day in wall time.
    """

    train_cost_milli_node_hours: builtins.int = ...
    """Output only. The actual train cost of creating this model, expressed in
    milli node hours, i.e. 1,000 value in this field means 1 node hour.
    Guaranteed to not exceed the train budget.
    """

    def __init__(self,
        *,
        model_type : typing.Text = ...,
        node_count : builtins.int = ...,
        node_qps : builtins.float = ...,
        stop_reason : typing.Text = ...,
        train_budget_milli_node_hours : builtins.int = ...,
        train_cost_milli_node_hours : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_type",b"model_type","node_count",b"node_count","node_qps",b"node_qps","stop_reason",b"stop_reason","train_budget_milli_node_hours",b"train_budget_milli_node_hours","train_cost_milli_node_hours",b"train_cost_milli_node_hours"]) -> None: ...
global___ImageObjectDetectionModelMetadata = ImageObjectDetectionModelMetadata

class ImageClassificationModelDeploymentMetadata(google.protobuf.message.Message):
    """Model deployment metadata specific to Image Classification."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NODE_COUNT_FIELD_NUMBER: builtins.int
    node_count: builtins.int = ...
    """Input only. The number of nodes to deploy the model on. A node is an
    abstraction of a machine resource, which can handle online prediction QPS
    as given in the model's
    [node_qps][google.cloud.automl.v1.ImageClassificationModelMetadata.node_qps].
    Must be between 1 and 100, inclusive on both ends.
    """

    def __init__(self,
        *,
        node_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["node_count",b"node_count"]) -> None: ...
global___ImageClassificationModelDeploymentMetadata = ImageClassificationModelDeploymentMetadata

class ImageObjectDetectionModelDeploymentMetadata(google.protobuf.message.Message):
    """Model deployment metadata specific to Image Object Detection."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NODE_COUNT_FIELD_NUMBER: builtins.int
    node_count: builtins.int = ...
    """Input only. The number of nodes to deploy the model on. A node is an
    abstraction of a machine resource, which can handle online prediction QPS
    as given in the model's
    [qps_per_node][google.cloud.automl.v1.ImageObjectDetectionModelMetadata.qps_per_node].
    Must be between 1 and 100, inclusive on both ends.
    """

    def __init__(self,
        *,
        node_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["node_count",b"node_count"]) -> None: ...
global___ImageObjectDetectionModelDeploymentMetadata = ImageObjectDetectionModelDeploymentMetadata
