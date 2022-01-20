# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/customer_negative_criterion_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.enums.response_content_type_pb2
import google.ads.googleads.v8.resources.customer_negative_criterion_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.rpc.status_pb2
import google.ads.googleads.v8.services.customer_negative_criterion_service_pb2


class CustomerNegativeCriterionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCustomerNegativeCriterion(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.GetCustomerNegativeCriterionRequest, google.ads.googleads.v8.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion]') -> None:
        pass

    @abc.abstractmethod
    async def MutateCustomerNegativeCriteria(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaRequest, google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.CustomerNegativeCriterionService/GetCustomerNegativeCriterion': grpclib.const.Handler(
                self.GetCustomerNegativeCriterion,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.GetCustomerNegativeCriterionRequest,
                google.ads.googleads.v8.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion,
            ),
            '/google.ads.googleads.v8.services.CustomerNegativeCriterionService/MutateCustomerNegativeCriteria': grpclib.const.Handler(
                self.MutateCustomerNegativeCriteria,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaRequest,
                google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaResponse,
            ),
        }


class CustomerNegativeCriterionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCustomerNegativeCriterion = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.CustomerNegativeCriterionService/GetCustomerNegativeCriterion',
            google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.GetCustomerNegativeCriterionRequest,
            google.ads.googleads.v8.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion,
        )
        self.MutateCustomerNegativeCriteria = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.CustomerNegativeCriterionService/MutateCustomerNegativeCriteria',
            google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaRequest,
            google.ads.googleads.v8.services.customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaResponse,
        )
