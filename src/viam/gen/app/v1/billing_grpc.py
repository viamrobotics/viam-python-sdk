import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
from ... import app

class BillingServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCurrentMonthUsage(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetCurrentMonthUsageRequest, app.v1.billing_pb2.GetCurrentMonthUsageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOrgBillingInformation(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetOrgBillingInformationRequest, app.v1.billing_pb2.GetOrgBillingInformationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetInvoicesSummary(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoicesSummaryRequest, app.v1.billing_pb2.GetInvoicesSummaryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetInvoicePdf(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoicePdfRequest, app.v1.billing_pb2.GetInvoicePdfResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.v1.BillingService/GetCurrentMonthUsage': grpclib.const.Handler(self.GetCurrentMonthUsage, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetCurrentMonthUsageRequest, app.v1.billing_pb2.GetCurrentMonthUsageResponse), '/viam.app.v1.BillingService/GetOrgBillingInformation': grpclib.const.Handler(self.GetOrgBillingInformation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetOrgBillingInformationRequest, app.v1.billing_pb2.GetOrgBillingInformationResponse), '/viam.app.v1.BillingService/GetInvoicesSummary': grpclib.const.Handler(self.GetInvoicesSummary, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetInvoicesSummaryRequest, app.v1.billing_pb2.GetInvoicesSummaryResponse), '/viam.app.v1.BillingService/GetInvoicePdf': grpclib.const.Handler(self.GetInvoicePdf, grpclib.const.Cardinality.UNARY_STREAM, app.v1.billing_pb2.GetInvoicePdfRequest, app.v1.billing_pb2.GetInvoicePdfResponse)}

class UnimplementedBillingServiceBase(BillingServiceBase):

    async def GetCurrentMonthUsage(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetCurrentMonthUsageRequest, app.v1.billing_pb2.GetCurrentMonthUsageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetOrgBillingInformation(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetOrgBillingInformationRequest, app.v1.billing_pb2.GetOrgBillingInformationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetInvoicesSummary(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoicesSummaryRequest, app.v1.billing_pb2.GetInvoicesSummaryResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetInvoicePdf(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoicePdfRequest, app.v1.billing_pb2.GetInvoicePdfResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class BillingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCurrentMonthUsage = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetCurrentMonthUsage', app.v1.billing_pb2.GetCurrentMonthUsageRequest, app.v1.billing_pb2.GetCurrentMonthUsageResponse)
        self.GetOrgBillingInformation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetOrgBillingInformation', app.v1.billing_pb2.GetOrgBillingInformationRequest, app.v1.billing_pb2.GetOrgBillingInformationResponse)
        self.GetInvoicesSummary = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetInvoicesSummary', app.v1.billing_pb2.GetInvoicesSummaryRequest, app.v1.billing_pb2.GetInvoicesSummaryResponse)
        self.GetInvoicePdf = grpclib.client.UnaryStreamMethod(channel, '/viam.app.v1.BillingService/GetInvoicePdf', app.v1.billing_pb2.GetInvoicePdfRequest, app.v1.billing_pb2.GetInvoicePdfResponse)