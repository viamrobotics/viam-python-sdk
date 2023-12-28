from typing import Mapping, Optional

from grpclib.client import Channel, Stream

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

    async def get_current_month_usage(self, org_id: str, timeout: Optional[float] = None) -> GetCurrentMonthUsageResponse:
        """Access data usage information for the current month for a given organization.

        Args:
            org_id (str): the ID of the organization to request usage data for

        Returns:
            viam.proto.app.billing.GetCurrentMonthUsageResponse: Current month usage information
        """
        request = GetCurrentMonthUsageRequest(org_id=org_id)
        return await self._billing_client.GetCurrentMonthUsage(request, metadata=self._metadata, timeout=timeout)

    async def get_invoice_pdf(self, invoice_id: str, org_id: str, dest: str, timeout: Optional[float] = None) -> None:
        """Access invoice PDF data and optionally save it to a provided file path.

        Args:
            invoice_id (str): the ID of the invoice being requested
            org_id (str): the ID of the org to request data from
            dest (str): filepath to save the invoice to
        """
        stream: Stream[GetInvoicePdfRequest, GetInvoicePdfResponse]
        async with self._billing_client.GetInvoicePdf.open(timeout=timeout, metadata=self._metadata) as stream:
            await stream.send_message(GetInvoicePdfRequest(id=invoice_id, org_id=org_id), end=True)
            with open(dest, "wb") as file:
                async for response in stream:
                    file.write(response.chunk)

    async def get_invoices_summary(self, org_id: str, timeout: Optional[float] = None) -> GetInvoicesSummaryResponse:
        """Access total outstanding balance plus invoice summaries for a given org.

        Args:
            org_id (str): the ID of the org to request data for

        Returns:
            viam.proto.app.billing.GetInvoicesSummaryResponse: Summary of org invoices
        """
        request = GetInvoicesSummaryRequest(org_id=org_id)
        return await self._billing_client.GetInvoicesSummary(request, metadata=self._metadata, timeout=timeout)

    async def get_org_billing_information(self, org_id: str, timeout: Optional[float] = None) -> GetOrgBillingInformationResponse:
        """Access billing information (payment method, billing tier, etc.) for a given org.

        Args:
            org_id (str): the ID of the org to request data for

        Returns:
            viam.proto.app.billing.GetOrgBillingInformationResponse: The org billing information"""
        request = GetOrgBillingInformationRequest(org_id=org_id)
        return await self._billing_client.GetOrgBillingInformation(request, metadata=self._metadata, timeout=timeout)
