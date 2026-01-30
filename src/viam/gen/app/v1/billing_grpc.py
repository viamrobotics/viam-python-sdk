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

    @abc.abstractmethod
    async def SendPaymentRequiredEmail(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.SendPaymentRequiredEmailRequest, app.v1.billing_pb2.SendPaymentRequiredEmailResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAvailableBillingTiers(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetAvailableBillingTiersRequest, app.v1.billing_pb2.GetAvailableBillingTiersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateOrganizationBillingTier(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.UpdateOrganizationBillingTierRequest, app.v1.billing_pb2.UpdateOrganizationBillingTierResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLocationBillingOrganization(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetLocationBillingOrganizationRequest, app.v1.billing_pb2.GetLocationBillingOrganizationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateLocationBillingOrganization(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.UpdateLocationBillingOrganizationRequest, app.v1.billing_pb2.UpdateLocationBillingOrganizationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ChargeOrganization(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.ChargeOrganizationRequest, app.v1.billing_pb2.ChargeOrganizationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateInvoiceAndChargeImmediately(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.CreateInvoiceAndChargeImmediatelyRequest, app.v1.billing_pb2.CreateInvoiceAndChargeImmediatelyResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.v1.BillingService/GetCurrentMonthUsage': grpclib.const.Handler(self.GetCurrentMonthUsage, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetCurrentMonthUsageRequest, app.v1.billing_pb2.GetCurrentMonthUsageResponse), '/viam.app.v1.BillingService/GetOrgBillingInformation': grpclib.const.Handler(self.GetOrgBillingInformation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetOrgBillingInformationRequest, app.v1.billing_pb2.GetOrgBillingInformationResponse), '/viam.app.v1.BillingService/GetInvoicesSummary': grpclib.const.Handler(self.GetInvoicesSummary, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetInvoicesSummaryRequest, app.v1.billing_pb2.GetInvoicesSummaryResponse), '/viam.app.v1.BillingService/GetInvoicePdf': grpclib.const.Handler(self.GetInvoicePdf, grpclib.const.Cardinality.UNARY_STREAM, app.v1.billing_pb2.GetInvoicePdfRequest, app.v1.billing_pb2.GetInvoicePdfResponse), '/viam.app.v1.BillingService/SendPaymentRequiredEmail': grpclib.const.Handler(self.SendPaymentRequiredEmail, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.SendPaymentRequiredEmailRequest, app.v1.billing_pb2.SendPaymentRequiredEmailResponse), '/viam.app.v1.BillingService/GetAvailableBillingTiers': grpclib.const.Handler(self.GetAvailableBillingTiers, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetAvailableBillingTiersRequest, app.v1.billing_pb2.GetAvailableBillingTiersResponse), '/viam.app.v1.BillingService/UpdateOrganizationBillingTier': grpclib.const.Handler(self.UpdateOrganizationBillingTier, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.UpdateOrganizationBillingTierRequest, app.v1.billing_pb2.UpdateOrganizationBillingTierResponse), '/viam.app.v1.BillingService/GetLocationBillingOrganization': grpclib.const.Handler(self.GetLocationBillingOrganization, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.GetLocationBillingOrganizationRequest, app.v1.billing_pb2.GetLocationBillingOrganizationResponse), '/viam.app.v1.BillingService/UpdateLocationBillingOrganization': grpclib.const.Handler(self.UpdateLocationBillingOrganization, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.UpdateLocationBillingOrganizationRequest, app.v1.billing_pb2.UpdateLocationBillingOrganizationResponse), '/viam.app.v1.BillingService/ChargeOrganization': grpclib.const.Handler(self.ChargeOrganization, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.ChargeOrganizationRequest, app.v1.billing_pb2.ChargeOrganizationResponse), '/viam.app.v1.BillingService/CreateInvoiceAndChargeImmediately': grpclib.const.Handler(self.CreateInvoiceAndChargeImmediately, grpclib.const.Cardinality.UNARY_UNARY, app.v1.billing_pb2.CreateInvoiceAndChargeImmediatelyRequest, app.v1.billing_pb2.CreateInvoiceAndChargeImmediatelyResponse)}

class UnimplementedBillingServiceBase(BillingServiceBase):

    async def GetCurrentMonthUsage(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetCurrentMonthUsageRequest, app.v1.billing_pb2.GetCurrentMonthUsageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetOrgBillingInformation(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetOrgBillingInformationRequest, app.v1.billing_pb2.GetOrgBillingInformationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetInvoicesSummary(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoicesSummaryRequest, app.v1.billing_pb2.GetInvoicesSummaryResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetInvoicePdf(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetInvoicePdfRequest, app.v1.billing_pb2.GetInvoicePdfResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SendPaymentRequiredEmail(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.SendPaymentRequiredEmailRequest, app.v1.billing_pb2.SendPaymentRequiredEmailResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetAvailableBillingTiers(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetAvailableBillingTiersRequest, app.v1.billing_pb2.GetAvailableBillingTiersResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateOrganizationBillingTier(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.UpdateOrganizationBillingTierRequest, app.v1.billing_pb2.UpdateOrganizationBillingTierResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetLocationBillingOrganization(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.GetLocationBillingOrganizationRequest, app.v1.billing_pb2.GetLocationBillingOrganizationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateLocationBillingOrganization(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.UpdateLocationBillingOrganizationRequest, app.v1.billing_pb2.UpdateLocationBillingOrganizationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ChargeOrganization(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.ChargeOrganizationRequest, app.v1.billing_pb2.ChargeOrganizationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateInvoiceAndChargeImmediately(self, stream: 'grpclib.server.Stream[app.v1.billing_pb2.CreateInvoiceAndChargeImmediatelyRequest, app.v1.billing_pb2.CreateInvoiceAndChargeImmediatelyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class BillingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCurrentMonthUsage = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetCurrentMonthUsage', app.v1.billing_pb2.GetCurrentMonthUsageRequest, app.v1.billing_pb2.GetCurrentMonthUsageResponse)
        self.GetOrgBillingInformation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetOrgBillingInformation', app.v1.billing_pb2.GetOrgBillingInformationRequest, app.v1.billing_pb2.GetOrgBillingInformationResponse)
        self.GetInvoicesSummary = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetInvoicesSummary', app.v1.billing_pb2.GetInvoicesSummaryRequest, app.v1.billing_pb2.GetInvoicesSummaryResponse)
        self.GetInvoicePdf = grpclib.client.UnaryStreamMethod(channel, '/viam.app.v1.BillingService/GetInvoicePdf', app.v1.billing_pb2.GetInvoicePdfRequest, app.v1.billing_pb2.GetInvoicePdfResponse)
        self.SendPaymentRequiredEmail = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/SendPaymentRequiredEmail', app.v1.billing_pb2.SendPaymentRequiredEmailRequest, app.v1.billing_pb2.SendPaymentRequiredEmailResponse)
        self.GetAvailableBillingTiers = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetAvailableBillingTiers', app.v1.billing_pb2.GetAvailableBillingTiersRequest, app.v1.billing_pb2.GetAvailableBillingTiersResponse)
        self.UpdateOrganizationBillingTier = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/UpdateOrganizationBillingTier', app.v1.billing_pb2.UpdateOrganizationBillingTierRequest, app.v1.billing_pb2.UpdateOrganizationBillingTierResponse)
        self.GetLocationBillingOrganization = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/GetLocationBillingOrganization', app.v1.billing_pb2.GetLocationBillingOrganizationRequest, app.v1.billing_pb2.GetLocationBillingOrganizationResponse)
        self.UpdateLocationBillingOrganization = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/UpdateLocationBillingOrganization', app.v1.billing_pb2.UpdateLocationBillingOrganizationRequest, app.v1.billing_pb2.UpdateLocationBillingOrganizationResponse)
        self.ChargeOrganization = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/ChargeOrganization', app.v1.billing_pb2.ChargeOrganizationRequest, app.v1.billing_pb2.ChargeOrganizationResponse)
        self.CreateInvoiceAndChargeImmediately = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.BillingService/CreateInvoiceAndChargeImmediately', app.v1.billing_pb2.CreateInvoiceAndChargeImmediatelyRequest, app.v1.billing_pb2.CreateInvoiceAndChargeImmediatelyResponse)