import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
from ... import app

class BillingServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCurrentMonthUsageSummary(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetCurrentMonthUsageSummaryRequest, app.v1.billing_pb2.GetCurrentMonthUsageSummaryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetUnpaidBalance(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetUnpaidBalanceRequest, app.v1.billing_pb2.GetUnpaidBalanceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetInvoiceHistory(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoiceHistoryRequest, app.v1.billing_pb2.GetInvoiceHistoryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetItemizedInvoice(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetItemizedInvoiceRequest, app.v1.billing_pb2.GetItemizedInvoiceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetBillingSummary(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetBillingSummaryRequest, app.v1.billing_pb2.GetBillingSummaryResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.v1.BillingService/GetCurrentMonthUsageSummary': grpclib.const.Handler(self.GetCurrentMonthUsageSummary, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetCurrentMonthUsageSummaryRequest, app.v1.billing_pb2.GetCurrentMonthUsageSummaryResponse), '/viam.app.v1.BillingService/GetUnpaidBalance': grpclib.const.Handler(self.GetUnpaidBalance, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetUnpaidBalanceRequest, app.v1.billing_pb2.GetUnpaidBalanceResponse), '/viam.app.v1.BillingService/GetInvoiceHistory': grpclib.const.Handler(self.GetInvoiceHistory, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetInvoiceHistoryRequest, app.v1.billing_pb2.GetInvoiceHistoryResponse), '/viam.app.v1.BillingService/GetItemizedInvoice': grpclib.const.Handler(self.GetItemizedInvoice, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetItemizedInvoiceRequest, app.v1.billing_pb2.GetItemizedInvoiceResponse), '/viam.app.v1.BillingService/GetBillingSummary': grpclib.const.Handler(self.GetBillingSummary, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetBillingSummaryRequest, app.v1.billing_pb2.GetBillingSummaryResponse)}

class BillingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCurrentMonthUsageSummary = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetCurrentMonthUsageSummary', app.v1.billing_pb2.GetCurrentMonthUsageSummaryRequest, app.v1.billing_pb2.GetCurrentMonthUsageSummaryResponse)
        self.GetUnpaidBalance = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetUnpaidBalance', app.v1.billing_pb2.GetUnpaidBalanceRequest, app.v1.billing_pb2.GetUnpaidBalanceResponse)
        self.GetInvoiceHistory = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetInvoiceHistory', app.v1.billing_pb2.GetInvoiceHistoryRequest, app.v1.billing_pb2.GetInvoiceHistoryResponse)
        self.GetItemizedInvoice = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetItemizedInvoice', app.v1.billing_pb2.GetItemizedInvoiceRequest, app.v1.billing_pb2.GetItemizedInvoiceResponse)
        self.GetBillingSummary = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetBillingSummary', app.v1.billing_pb2.GetBillingSummaryRequest, app.v1.billing_pb2.GetBillingSummaryResponse)