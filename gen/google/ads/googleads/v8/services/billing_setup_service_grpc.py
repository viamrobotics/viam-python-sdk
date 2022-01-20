# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/billing_setup_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.billing_setup_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v8.services.billing_setup_service_pb2


class BillingSetupServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetBillingSetup(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.billing_setup_service_pb2.GetBillingSetupRequest, google.ads.googleads.v8.resources.billing_setup_pb2.BillingSetup]') -> None:
        pass

    @abc.abstractmethod
    async def MutateBillingSetup(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.billing_setup_service_pb2.MutateBillingSetupRequest, google.ads.googleads.v8.services.billing_setup_service_pb2.MutateBillingSetupResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.BillingSetupService/GetBillingSetup': grpclib.const.Handler(
                self.GetBillingSetup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.billing_setup_service_pb2.GetBillingSetupRequest,
                google.ads.googleads.v8.resources.billing_setup_pb2.BillingSetup,
            ),
            '/google.ads.googleads.v8.services.BillingSetupService/MutateBillingSetup': grpclib.const.Handler(
                self.MutateBillingSetup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.billing_setup_service_pb2.MutateBillingSetupRequest,
                google.ads.googleads.v8.services.billing_setup_service_pb2.MutateBillingSetupResponse,
            ),
        }


class BillingSetupServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetBillingSetup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.BillingSetupService/GetBillingSetup',
            google.ads.googleads.v8.services.billing_setup_service_pb2.GetBillingSetupRequest,
            google.ads.googleads.v8.resources.billing_setup_pb2.BillingSetup,
        )
        self.MutateBillingSetup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.BillingSetupService/MutateBillingSetup',
            google.ads.googleads.v8.services.billing_setup_service_pb2.MutateBillingSetupRequest,
            google.ads.googleads.v8.services.billing_setup_service_pb2.MutateBillingSetupResponse,
        )
