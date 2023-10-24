from typing import Mapping

from grpclib.client import Channel

from viam import logging
from viam.proto.app.billing import (
        BillingServiceStub,
        GetCurrentMonthUsageRequest,
        GetCurrentMonthUsageResponse,
        GetInvoicePdfRequest,
        GetInvoicePdfResponse,
        GetInvoicesSummaryRequest,
        GetInvoicesSummaryResponse,
        GetOrgBillingInformationRequest,
        GetOrgBillingInformationResponse,
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
    async def get_current_month_usage(self, org_id: str) -> GetCurrentMonthUsageResponse:
        """Access data usage information for the current month for a given organization.

        Args:
            org_id (str): the ID of the organization to request usage data for

        Returns:
            viam.proto.app.billing.GetCurrentMonthUsageResponse: Current month usage information
        """
        request = GetCurrentMonthUsageRequest(org_id=org_id)
        return await self._billing_client.GetCurrentMonthUsage(request, metadata=self._metadata)

    async def get_invoice_pdf(self, invoice_id: str, org_id: str, dest: Optional[str] = None) -> bytes:
        """Access invoice PDF data and optionally save it to a provided file path.

        Args:
            invoice_id (str): the ID of the invoice being requested
            org_id (str): the ID of the org to request data from
            dest (Optional[str]): optional filepath to save the invoice to

        Returns:
            bytes: the invoice
        """
        request = GetInvoicePdfRequest(id=invoice_id, org_id=org_id)
        response: GetInvoicePdfResponse = await self._billing_client.GetInvoicePdf(request, metadata=self._metadata)
        data = response.chunk
        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{data}")
            except Exception as e:
                LOGGER.error(f"Failed to write invoide PDF to file {dest}", exc_info=e)
        return data

    async def get_invoices_summary(self, org_id: str) -> GetInvoicesSummaryResponse:
        """Access total outstanding balance plus invoice summaries for a given org.

        Args:
            org_id (str): the ID of the org to request data for

        Returns:
            viam.proto.app.billing.GetInvoicesSummaryResponse: Summary of org invoices
        """
        request = GetInvoicesSummaryRequest(org_id=org_id)
        return await self._billing_client.GetInvoicesSummary(request, metadata=self._metadata)

    async def get_org_billing_information(self, org_id: str) -> GetOrgBillingInformationResponse:
        """Access billing information (payment method, billing tier, etc.) for a given org.

        Args:
            org_id (str): the ID of the org to request data for

        Returns:
            viam.proto.app.billing.GetOrgBillingInformationResponse: The org billing information"""
        request = GetOrgBillingInformationRequest(org_id=org_id)
        return await self._billing_client.GetOrgBillingInformation(request, metadata=self._metadata)

