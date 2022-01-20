# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/payments_account_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.payments_account_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.ads.googleads.v8.services.payments_account_service_pb2


class PaymentsAccountServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListPaymentsAccounts(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.payments_account_service_pb2.ListPaymentsAccountsRequest, google.ads.googleads.v8.services.payments_account_service_pb2.ListPaymentsAccountsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.PaymentsAccountService/ListPaymentsAccounts': grpclib.const.Handler(
                self.ListPaymentsAccounts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.payments_account_service_pb2.ListPaymentsAccountsRequest,
                google.ads.googleads.v8.services.payments_account_service_pb2.ListPaymentsAccountsResponse,
            ),
        }


class PaymentsAccountServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListPaymentsAccounts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.PaymentsAccountService/ListPaymentsAccounts',
            google.ads.googleads.v8.services.payments_account_service_pb2.ListPaymentsAccountsRequest,
            google.ads.googleads.v8.services.payments_account_service_pb2.ListPaymentsAccountsResponse,
        )
