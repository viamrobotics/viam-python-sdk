# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/bidding_strategy_simulation_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.bidding_strategy_simulation_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v9.services.bidding_strategy_simulation_service_pb2


class BiddingStrategySimulationServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetBiddingStrategySimulation(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.bidding_strategy_simulation_service_pb2.GetBiddingStrategySimulationRequest, google.ads.googleads.v9.resources.bidding_strategy_simulation_pb2.BiddingStrategySimulation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.BiddingStrategySimulationService/GetBiddingStrategySimulation': grpclib.const.Handler(
                self.GetBiddingStrategySimulation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.bidding_strategy_simulation_service_pb2.GetBiddingStrategySimulationRequest,
                google.ads.googleads.v9.resources.bidding_strategy_simulation_pb2.BiddingStrategySimulation,
            ),
        }


class BiddingStrategySimulationServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetBiddingStrategySimulation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.BiddingStrategySimulationService/GetBiddingStrategySimulation',
            google.ads.googleads.v9.services.bidding_strategy_simulation_service_pb2.GetBiddingStrategySimulationRequest,
            google.ads.googleads.v9.resources.bidding_strategy_simulation_pb2.BiddingStrategySimulation,
        )
