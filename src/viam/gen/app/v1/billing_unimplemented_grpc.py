import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
from ... import app
from .billing_grpc import BillingServiceBase as _BillingServiceBase

class UnimplementedBillingServiceBase(_BillingServiceBase):

    async def GetCurrentMonthUsage(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetCurrentMonthUsageRequest, app.v1.billing_pb2.GetCurrentMonthUsageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetOrgBillingInformation(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetOrgBillingInformationRequest, app.v1.billing_pb2.GetOrgBillingInformationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetInvoicesSummary(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoicesSummaryRequest, app.v1.billing_pb2.GetInvoicesSummaryResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetInvoicePdf(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoicePdfRequest, app.v1.billing_pb2.GetInvoicePdfResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)