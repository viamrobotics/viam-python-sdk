# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/recommender/v1/recommender_service.proto
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
import google.cloud.recommender.v1.insight_pb2
import google.cloud.recommender.v1.recommendation_pb2
import google.cloud.recommender.v1.recommender_service_pb2


class RecommenderBase(abc.ABC):

    @abc.abstractmethod
    async def ListInsights(self, stream: 'grpclib.server.Stream[google.cloud.recommender.v1.recommender_service_pb2.ListInsightsRequest, google.cloud.recommender.v1.recommender_service_pb2.ListInsightsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetInsight(self, stream: 'grpclib.server.Stream[google.cloud.recommender.v1.recommender_service_pb2.GetInsightRequest, google.cloud.recommender.v1.insight_pb2.Insight]') -> None:
        pass

    @abc.abstractmethod
    async def MarkInsightAccepted(self, stream: 'grpclib.server.Stream[google.cloud.recommender.v1.recommender_service_pb2.MarkInsightAcceptedRequest, google.cloud.recommender.v1.insight_pb2.Insight]') -> None:
        pass

    @abc.abstractmethod
    async def ListRecommendations(self, stream: 'grpclib.server.Stream[google.cloud.recommender.v1.recommender_service_pb2.ListRecommendationsRequest, google.cloud.recommender.v1.recommender_service_pb2.ListRecommendationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRecommendation(self, stream: 'grpclib.server.Stream[google.cloud.recommender.v1.recommender_service_pb2.GetRecommendationRequest, google.cloud.recommender.v1.recommendation_pb2.Recommendation]') -> None:
        pass

    @abc.abstractmethod
    async def MarkRecommendationClaimed(self, stream: 'grpclib.server.Stream[google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationClaimedRequest, google.cloud.recommender.v1.recommendation_pb2.Recommendation]') -> None:
        pass

    @abc.abstractmethod
    async def MarkRecommendationSucceeded(self, stream: 'grpclib.server.Stream[google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationSucceededRequest, google.cloud.recommender.v1.recommendation_pb2.Recommendation]') -> None:
        pass

    @abc.abstractmethod
    async def MarkRecommendationFailed(self, stream: 'grpclib.server.Stream[google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationFailedRequest, google.cloud.recommender.v1.recommendation_pb2.Recommendation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.recommender.v1.Recommender/ListInsights': grpclib.const.Handler(
                self.ListInsights,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.recommender.v1.recommender_service_pb2.ListInsightsRequest,
                google.cloud.recommender.v1.recommender_service_pb2.ListInsightsResponse,
            ),
            '/google.cloud.recommender.v1.Recommender/GetInsight': grpclib.const.Handler(
                self.GetInsight,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.recommender.v1.recommender_service_pb2.GetInsightRequest,
                google.cloud.recommender.v1.insight_pb2.Insight,
            ),
            '/google.cloud.recommender.v1.Recommender/MarkInsightAccepted': grpclib.const.Handler(
                self.MarkInsightAccepted,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.recommender.v1.recommender_service_pb2.MarkInsightAcceptedRequest,
                google.cloud.recommender.v1.insight_pb2.Insight,
            ),
            '/google.cloud.recommender.v1.Recommender/ListRecommendations': grpclib.const.Handler(
                self.ListRecommendations,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.recommender.v1.recommender_service_pb2.ListRecommendationsRequest,
                google.cloud.recommender.v1.recommender_service_pb2.ListRecommendationsResponse,
            ),
            '/google.cloud.recommender.v1.Recommender/GetRecommendation': grpclib.const.Handler(
                self.GetRecommendation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.recommender.v1.recommender_service_pb2.GetRecommendationRequest,
                google.cloud.recommender.v1.recommendation_pb2.Recommendation,
            ),
            '/google.cloud.recommender.v1.Recommender/MarkRecommendationClaimed': grpclib.const.Handler(
                self.MarkRecommendationClaimed,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationClaimedRequest,
                google.cloud.recommender.v1.recommendation_pb2.Recommendation,
            ),
            '/google.cloud.recommender.v1.Recommender/MarkRecommendationSucceeded': grpclib.const.Handler(
                self.MarkRecommendationSucceeded,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationSucceededRequest,
                google.cloud.recommender.v1.recommendation_pb2.Recommendation,
            ),
            '/google.cloud.recommender.v1.Recommender/MarkRecommendationFailed': grpclib.const.Handler(
                self.MarkRecommendationFailed,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationFailedRequest,
                google.cloud.recommender.v1.recommendation_pb2.Recommendation,
            ),
        }


class RecommenderStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListInsights = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.recommender.v1.Recommender/ListInsights',
            google.cloud.recommender.v1.recommender_service_pb2.ListInsightsRequest,
            google.cloud.recommender.v1.recommender_service_pb2.ListInsightsResponse,
        )
        self.GetInsight = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.recommender.v1.Recommender/GetInsight',
            google.cloud.recommender.v1.recommender_service_pb2.GetInsightRequest,
            google.cloud.recommender.v1.insight_pb2.Insight,
        )
        self.MarkInsightAccepted = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.recommender.v1.Recommender/MarkInsightAccepted',
            google.cloud.recommender.v1.recommender_service_pb2.MarkInsightAcceptedRequest,
            google.cloud.recommender.v1.insight_pb2.Insight,
        )
        self.ListRecommendations = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.recommender.v1.Recommender/ListRecommendations',
            google.cloud.recommender.v1.recommender_service_pb2.ListRecommendationsRequest,
            google.cloud.recommender.v1.recommender_service_pb2.ListRecommendationsResponse,
        )
        self.GetRecommendation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.recommender.v1.Recommender/GetRecommendation',
            google.cloud.recommender.v1.recommender_service_pb2.GetRecommendationRequest,
            google.cloud.recommender.v1.recommendation_pb2.Recommendation,
        )
        self.MarkRecommendationClaimed = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.recommender.v1.Recommender/MarkRecommendationClaimed',
            google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationClaimedRequest,
            google.cloud.recommender.v1.recommendation_pb2.Recommendation,
        )
        self.MarkRecommendationSucceeded = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.recommender.v1.Recommender/MarkRecommendationSucceeded',
            google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationSucceededRequest,
            google.cloud.recommender.v1.recommendation_pb2.Recommendation,
        )
        self.MarkRecommendationFailed = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.recommender.v1.Recommender/MarkRecommendationFailed',
            google.cloud.recommender.v1.recommender_service_pb2.MarkRecommendationFailedRequest,
            google.cloud.recommender.v1.recommendation_pb2.Recommendation,
        )
