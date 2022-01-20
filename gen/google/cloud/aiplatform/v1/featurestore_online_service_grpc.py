# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/aiplatform/v1/featurestore_online_service.proto
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
import google.api.resource_pb2
import google.cloud.aiplatform.v1.feature_selector_pb2
import google.cloud.aiplatform.v1.types_pb2
import google.protobuf.timestamp_pb2
import google.cloud.aiplatform.v1.featurestore_online_service_pb2


class FeaturestoreOnlineServingServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ReadFeatureValues(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesRequest, google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamingReadFeatureValues(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.featurestore_online_service_pb2.StreamingReadFeatureValuesRequest, google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.aiplatform.v1.FeaturestoreOnlineServingService/ReadFeatureValues': grpclib.const.Handler(
                self.ReadFeatureValues,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesRequest,
                google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesResponse,
            ),
            '/google.cloud.aiplatform.v1.FeaturestoreOnlineServingService/StreamingReadFeatureValues': grpclib.const.Handler(
                self.StreamingReadFeatureValues,
                grpclib.const.Cardinality.UNARY_STREAM,
                google.cloud.aiplatform.v1.featurestore_online_service_pb2.StreamingReadFeatureValuesRequest,
                google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesResponse,
            ),
        }


class FeaturestoreOnlineServingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ReadFeatureValues = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.FeaturestoreOnlineServingService/ReadFeatureValues',
            google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesRequest,
            google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesResponse,
        )
        self.StreamingReadFeatureValues = grpclib.client.UnaryStreamMethod(
            channel,
            '/google.cloud.aiplatform.v1.FeaturestoreOnlineServingService/StreamingReadFeatureValues',
            google.cloud.aiplatform.v1.featurestore_online_service_pb2.StreamingReadFeatureValuesRequest,
            google.cloud.aiplatform.v1.featurestore_online_service_pb2.ReadFeatureValuesResponse,
        )
