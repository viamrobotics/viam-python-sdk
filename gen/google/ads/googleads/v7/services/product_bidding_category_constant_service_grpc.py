# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/product_bidding_category_constant_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.resources.product_bidding_category_constant_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v7.services.product_bidding_category_constant_service_pb2


class ProductBiddingCategoryConstantServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetProductBiddingCategoryConstant(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.product_bidding_category_constant_service_pb2.GetProductBiddingCategoryConstantRequest, google.ads.googleads.v7.resources.product_bidding_category_constant_pb2.ProductBiddingCategoryConstant]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.ProductBiddingCategoryConstantService/GetProductBiddingCategoryConstant': grpclib.const.Handler(
                self.GetProductBiddingCategoryConstant,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.product_bidding_category_constant_service_pb2.GetProductBiddingCategoryConstantRequest,
                google.ads.googleads.v7.resources.product_bidding_category_constant_pb2.ProductBiddingCategoryConstant,
            ),
        }


class ProductBiddingCategoryConstantServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetProductBiddingCategoryConstant = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.ProductBiddingCategoryConstantService/GetProductBiddingCategoryConstant',
            google.ads.googleads.v7.services.product_bidding_category_constant_service_pb2.GetProductBiddingCategoryConstantRequest,
            google.ads.googleads.v7.resources.product_bidding_category_constant_pb2.ProductBiddingCategoryConstant,
        )
