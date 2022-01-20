# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/prediction_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.httpbody_pb2
import google.api.resource_pb2
import google.cloud.aiplatform.v1beta1.explanation_pb2
import google.protobuf.struct_pb2
import google.cloud.aiplatform.v1beta1.prediction_service_pb2


class PredictionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Predict(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.prediction_service_pb2.PredictRequest, google.cloud.aiplatform.v1beta1.prediction_service_pb2.PredictResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RawPredict(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.prediction_service_pb2.RawPredictRequest, google.api.httpbody_pb2.HttpBody]') -> None:
        pass

    @abc.abstractmethod
    async def Explain(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.prediction_service_pb2.ExplainRequest, google.cloud.aiplatform.v1beta1.prediction_service_pb2.ExplainResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.aiplatform.v1beta1.PredictionService/Predict': grpclib.const.Handler(
                self.Predict,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.prediction_service_pb2.PredictRequest,
                google.cloud.aiplatform.v1beta1.prediction_service_pb2.PredictResponse,
            ),
            '/google.cloud.aiplatform.v1beta1.PredictionService/RawPredict': grpclib.const.Handler(
                self.RawPredict,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.prediction_service_pb2.RawPredictRequest,
                google.api.httpbody_pb2.HttpBody,
            ),
            '/google.cloud.aiplatform.v1beta1.PredictionService/Explain': grpclib.const.Handler(
                self.Explain,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.prediction_service_pb2.ExplainRequest,
                google.cloud.aiplatform.v1beta1.prediction_service_pb2.ExplainResponse,
            ),
        }


class PredictionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Predict = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.PredictionService/Predict',
            google.cloud.aiplatform.v1beta1.prediction_service_pb2.PredictRequest,
            google.cloud.aiplatform.v1beta1.prediction_service_pb2.PredictResponse,
        )
        self.RawPredict = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.PredictionService/RawPredict',
            google.cloud.aiplatform.v1beta1.prediction_service_pb2.RawPredictRequest,
            google.api.httpbody_pb2.HttpBody,
        )
        self.Explain = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.PredictionService/Explain',
            google.cloud.aiplatform.v1beta1.prediction_service_pb2.ExplainRequest,
            google.cloud.aiplatform.v1beta1.prediction_service_pb2.ExplainResponse,
        )
