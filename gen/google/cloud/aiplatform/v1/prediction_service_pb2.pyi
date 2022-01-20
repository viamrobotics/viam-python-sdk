"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.api.httpbody_pb2
import google.cloud.aiplatform.v1.explanation_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PredictRequest(google.protobuf.message.Message):
    """Request message for [PredictionService.Predict][google.cloud.aiplatform.v1.PredictionService.Predict]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENDPOINT_FIELD_NUMBER: builtins.int
    INSTANCES_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    endpoint: typing.Text = ...
    """Required. The name of the Endpoint requested to serve the prediction.
    Format:
    `projects/{project}/locations/{location}/endpoints/{endpoint}`
    """

    @property
    def instances(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Value]:
        """Required. The instances that are the input to the prediction call.
        A DeployedModel may have an upper limit on the number of instances it
        supports per request, and when it is exceeded the prediction call errors
        in case of AutoML Models, or, in case of customer created Models, the
        behaviour is as documented by that Model.
        The schema of any single instance may be specified via Endpoint's
        DeployedModels' [Model's][google.cloud.aiplatform.v1.DeployedModel.model]
        [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata]
        [instance_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.instance_schema_uri].
        """
        pass
    @property
    def parameters(self) -> google.protobuf.struct_pb2.Value:
        """The parameters that govern the prediction. The schema of the parameters may
        be specified via Endpoint's DeployedModels' [Model's ][google.cloud.aiplatform.v1.DeployedModel.model]
        [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata]
        [parameters_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.parameters_schema_uri].
        """
        pass
    def __init__(self,
        *,
        endpoint : typing.Text = ...,
        instances : typing.Optional[typing.Iterable[google.protobuf.struct_pb2.Value]] = ...,
        parameters : typing.Optional[google.protobuf.struct_pb2.Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint",b"endpoint","instances",b"instances","parameters",b"parameters"]) -> None: ...
global___PredictRequest = PredictRequest

class PredictResponse(google.protobuf.message.Message):
    """Response message for [PredictionService.Predict][google.cloud.aiplatform.v1.PredictionService.Predict]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PREDICTIONS_FIELD_NUMBER: builtins.int
    DEPLOYED_MODEL_ID_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    MODEL_DISPLAY_NAME_FIELD_NUMBER: builtins.int
    @property
    def predictions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Value]:
        """The predictions that are the output of the predictions call.
        The schema of any single prediction may be specified via Endpoint's
        DeployedModels' [Model's ][google.cloud.aiplatform.v1.DeployedModel.model]
        [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata]
        [prediction_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.prediction_schema_uri].
        """
        pass
    deployed_model_id: typing.Text = ...
    """ID of the Endpoint's DeployedModel that served this prediction."""

    model: typing.Text = ...
    """Output only. The resource name of the Model which is deployed as the DeployedModel that
    this prediction hits.
    """

    model_display_name: typing.Text = ...
    """Output only. The [display name][google.cloud.aiplatform.v1.Model.display_name] of the Model which is deployed as
    the DeployedModel that this prediction hits.
    """

    def __init__(self,
        *,
        predictions : typing.Optional[typing.Iterable[google.protobuf.struct_pb2.Value]] = ...,
        deployed_model_id : typing.Text = ...,
        model : typing.Text = ...,
        model_display_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["deployed_model_id",b"deployed_model_id","model",b"model","model_display_name",b"model_display_name","predictions",b"predictions"]) -> None: ...
global___PredictResponse = PredictResponse

class RawPredictRequest(google.protobuf.message.Message):
    """Request message for [PredictionService.RawPredict][google.cloud.aiplatform.v1.PredictionService.RawPredict]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENDPOINT_FIELD_NUMBER: builtins.int
    HTTP_BODY_FIELD_NUMBER: builtins.int
    endpoint: typing.Text = ...
    """Required. The name of the Endpoint requested to serve the prediction.
    Format:
    `projects/{project}/locations/{location}/endpoints/{endpoint}`
    """

    @property
    def http_body(self) -> google.api.httpbody_pb2.HttpBody:
        """The prediction input. Supports HTTP headers and arbitrary data payload.

        A [DeployedModel][google.cloud.aiplatform.v1.DeployedModel] may have an upper limit on the number of instances it
        supports per request. When this limit it is exceeded for an AutoML model,
        the [RawPredict][google.cloud.aiplatform.v1.PredictionService.RawPredict] method returns an error.
        When this limit is exceeded for a custom-trained model, the behavior varies
        depending on the model.

        You can specify the schema for each instance in the
        [predict_schemata.instance_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.instance_schema_uri]
        field when you create a [Model][google.cloud.aiplatform.v1.Model]. This schema applies when you deploy the
        `Model` as a `DeployedModel` to an [Endpoint][google.cloud.aiplatform.v1.Endpoint] and use the `RawPredict`
        method.
        """
        pass
    def __init__(self,
        *,
        endpoint : typing.Text = ...,
        http_body : typing.Optional[google.api.httpbody_pb2.HttpBody] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["http_body",b"http_body"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint",b"endpoint","http_body",b"http_body"]) -> None: ...
global___RawPredictRequest = RawPredictRequest

class ExplainRequest(google.protobuf.message.Message):
    """Request message for [PredictionService.Explain][google.cloud.aiplatform.v1.PredictionService.Explain]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENDPOINT_FIELD_NUMBER: builtins.int
    INSTANCES_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    EXPLANATION_SPEC_OVERRIDE_FIELD_NUMBER: builtins.int
    DEPLOYED_MODEL_ID_FIELD_NUMBER: builtins.int
    endpoint: typing.Text = ...
    """Required. The name of the Endpoint requested to serve the explanation.
    Format:
    `projects/{project}/locations/{location}/endpoints/{endpoint}`
    """

    @property
    def instances(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Value]:
        """Required. The instances that are the input to the explanation call.
        A DeployedModel may have an upper limit on the number of instances it
        supports per request, and when it is exceeded the explanation call errors
        in case of AutoML Models, or, in case of customer created Models, the
        behaviour is as documented by that Model.
        The schema of any single instance may be specified via Endpoint's
        DeployedModels' [Model's][google.cloud.aiplatform.v1.DeployedModel.model]
        [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata]
        [instance_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.instance_schema_uri].
        """
        pass
    @property
    def parameters(self) -> google.protobuf.struct_pb2.Value:
        """The parameters that govern the prediction. The schema of the parameters may
        be specified via Endpoint's DeployedModels' [Model's ][google.cloud.aiplatform.v1.DeployedModel.model]
        [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata]
        [parameters_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.parameters_schema_uri].
        """
        pass
    @property
    def explanation_spec_override(self) -> google.cloud.aiplatform.v1.explanation_pb2.ExplanationSpecOverride:
        """If specified, overrides the
        [explanation_spec][google.cloud.aiplatform.v1.DeployedModel.explanation_spec] of the DeployedModel.
        Can be used for explaining prediction results with different
        configurations, such as:
         - Explaining top-5 predictions results as opposed to top-1;
         - Increasing path count or step count of the attribution methods to reduce
           approximate errors;
         - Using different baselines for explaining the prediction results.
        """
        pass
    deployed_model_id: typing.Text = ...
    """If specified, this ExplainRequest will be served by the chosen
    DeployedModel, overriding [Endpoint.traffic_split][google.cloud.aiplatform.v1.Endpoint.traffic_split].
    """

    def __init__(self,
        *,
        endpoint : typing.Text = ...,
        instances : typing.Optional[typing.Iterable[google.protobuf.struct_pb2.Value]] = ...,
        parameters : typing.Optional[google.protobuf.struct_pb2.Value] = ...,
        explanation_spec_override : typing.Optional[google.cloud.aiplatform.v1.explanation_pb2.ExplanationSpecOverride] = ...,
        deployed_model_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["explanation_spec_override",b"explanation_spec_override","parameters",b"parameters"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deployed_model_id",b"deployed_model_id","endpoint",b"endpoint","explanation_spec_override",b"explanation_spec_override","instances",b"instances","parameters",b"parameters"]) -> None: ...
global___ExplainRequest = ExplainRequest

class ExplainResponse(google.protobuf.message.Message):
    """Response message for [PredictionService.Explain][google.cloud.aiplatform.v1.PredictionService.Explain]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXPLANATIONS_FIELD_NUMBER: builtins.int
    DEPLOYED_MODEL_ID_FIELD_NUMBER: builtins.int
    PREDICTIONS_FIELD_NUMBER: builtins.int
    @property
    def explanations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.aiplatform.v1.explanation_pb2.Explanation]:
        """The explanations of the Model's [PredictResponse.predictions][google.cloud.aiplatform.v1.PredictResponse.predictions].

        It has the same number of elements as [instances][google.cloud.aiplatform.v1.ExplainRequest.instances]
        to be explained.
        """
        pass
    deployed_model_id: typing.Text = ...
    """ID of the Endpoint's DeployedModel that served this explanation."""

    @property
    def predictions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Value]:
        """The predictions that are the output of the predictions call.
        Same as [PredictResponse.predictions][google.cloud.aiplatform.v1.PredictResponse.predictions].
        """
        pass
    def __init__(self,
        *,
        explanations : typing.Optional[typing.Iterable[google.cloud.aiplatform.v1.explanation_pb2.Explanation]] = ...,
        deployed_model_id : typing.Text = ...,
        predictions : typing.Optional[typing.Iterable[google.protobuf.struct_pb2.Value]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["deployed_model_id",b"deployed_model_id","explanations",b"explanations","predictions",b"predictions"]) -> None: ...
global___ExplainResponse = ExplainResponse
