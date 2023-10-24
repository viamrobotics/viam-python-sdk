from typing import Mapping

from grpclib.client import Channel

from viam import logging
from viam.proto.app.billing import (
        BillingServiceStub,
        GetBillingSummaryRequest,
        GetBillingSummaryResponse,
        GetCurrentMonthUsageRequest,
        GetCurrentMonthUsageResponse,
        GetCurrentMonthUsageSummaryRequest,
        GetCurrentMonthUsageSummaryResponse,
        GetInvoiceHistoryRequest,
        GetInvoiceHistoryResponse,
        GetInvoicePdfRequest,
        GetInvoicePdfResponse,
        GetInvoicesSummaryRequest,
        GetInvoicesSummaryResponse,
        GetItemizedInvoiceRequest,
        GetItemizedInvoiceResponse,
        GetOrgBillingInformationRequest,
        GetOrgBillingInformationResponse,
        GetUnpaidBalanceRequest,
        GetUnpaidBalanceResponse,
)

LOGGER = logging.getLogger(__name__)


class BillingClient:
    """gRPC client for retrieving billing data from app.

    Constructor is used by `ViamClient` to instantiate relevant service stubs. Calls to
    `BillingClient` methods should be made through `ViamClient`.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create a `BillingClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): Connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._billing_client = BillingServiceStub(channel)
        self._channel = channel

    _billing_client: BillingServiceStub
    _channel: Channel
    _metadata: Mapping[str, str]

    # CR erodkin: add timeouts
    async def get_billing_summary(self, org_id: str) -> GetBillingSummaryResponse:
        request = GetBillingSummaryRequest(org_id=org_id)
        return await self._billing_client.GetBillingSummary(request, metadata=self._metadata)

    async def get_current_month_usage(self, org_id: str) -> GetCurrentMonthUsageResponse:
        request = GetCurrentMonthUsageRequest(org_id=org_id)
        return await self._billing_client.GetCurrentMonthUsage(request, metadata=self._metadata)

    async def get_current_month_usage_summary(self, org_id: str) -> GetCurrentMonthUsageSummaryResponse:
        request = GetCurrentMonthUsageRequest(org_id=org_id)
        return await self._billing_client.GetCurrentMonthUsageSummary(request, metadata=self._metadata)

    async def get_invoice_history(self, org_id: str) -> GetInvoiceHistoryResponse:
        request = GetInvoiceHistoryRequest(org_id=org_id)
        return await self._billing_client.GetInvoiceHistory(request, metadata=self._metadata)

    async def get_invoice_pdf(self, id: str, org_id: str) -> GetInvoicePdfResponse:
        request = GetInvoicePdfRequest(id=id, org_id=org_id)
        return await self._billing_client.GetInvoicePdf(request, metadata=self._metadata)

    async def get_invoices_summary(self, org_id: str) -> GetInvoicesSummaryResponse:
        request = GetInvoicesSummaryRequest(org_id=org_id)
        return await self._billing_client.GetInvoicesSummary(request, metadata=self._metadata)

    async def get_itemized_invoice(self, id: str) -> GetItemizedInvoiceResponse:
        request = GetItemizedInvoiceRequest(id=id)
        return await self._billing_client.GetItemizedInvoice(request, metadata=self._metadata)

    async def get_org_billing_information(self, org_id: str) -> GetOrgBillingInformationResponse:
        request = GetOrgBillingInformationRequest(org_id=org_id)
        return await self._billing_client.GetOrgBillingInformation(request, metadata=self._metadata)

    async def get_unpaid_balance(self, org_id: str) -> GetUnpaidBalanceResponse:
        request = GetUnpaidBalanceRequest(org_id=org_id)
        return await self._billing_client.GetUnpaidBalance(request, metadata=self._metadata)

