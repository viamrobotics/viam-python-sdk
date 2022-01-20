# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/bidding_strategy_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.enums.response_content_type_pb2
import google.ads.googleads.v7.resources.bidding_strategy_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v7.services.bidding_strategy_service_pb2


class BiddingStrategyServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetBiddingStrategy(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.bidding_strategy_service_pb2.GetBiddingStrategyRequest, google.ads.googleads.v7.resources.bidding_strategy_pb2.BiddingStrategy]') -> None:
        pass

    @abc.abstractmethod
    async def MutateBiddingStrategies(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.bidding_strategy_service_pb2.MutateBiddingStrategiesRequest, google.ads.googleads.v7.services.bidding_strategy_service_pb2.MutateBiddingStrategiesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.BiddingStrategyService/GetBiddingStrategy': grpclib.const.Handler(
                self.GetBiddingStrategy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.bidding_strategy_service_pb2.GetBiddingStrategyRequest,
                google.ads.googleads.v7.resources.bidding_strategy_pb2.BiddingStrategy,
            ),
            '/google.ads.googleads.v7.services.BiddingStrategyService/MutateBiddingStrategies': grpclib.const.Handler(
                self.MutateBiddingStrategies,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.bidding_strategy_service_pb2.MutateBiddingStrategiesRequest,
                google.ads.googleads.v7.services.bidding_strategy_service_pb2.MutateBiddingStrategiesResponse,
            ),
        }


class BiddingStrategyServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetBiddingStrategy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.BiddingStrategyService/GetBiddingStrategy',
            google.ads.googleads.v7.services.bidding_strategy_service_pb2.GetBiddingStrategyRequest,
            google.ads.googleads.v7.resources.bidding_strategy_pb2.BiddingStrategy,
        )
        self.MutateBiddingStrategies = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.BiddingStrategyService/MutateBiddingStrategies',
            google.ads.googleads.v7.services.bidding_strategy_service_pb2.MutateBiddingStrategiesRequest,
            google.ads.googleads.v7.services.bidding_strategy_service_pb2.MutateBiddingStrategiesResponse,
        )
