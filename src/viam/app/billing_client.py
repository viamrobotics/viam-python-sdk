from typing import Mapping, Optional

from grpclib.client import Channel, Stream

from viam import logging
from viam.proto.app.billing import (
    BillingServiceStub,
    CreateInvoiceAndChargeImmediatelyRequest,
    CreateInvoiceAndChargeImmediatelyResponse,
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

    Establish a Connection::

        import asyncio

        from viam.rpc.dial import DialOptions, Credentials
        from viam.app.viam_client import ViamClient


        async def connect() -> ViamClient:
            # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
            dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
            return await ViamClient.create_from_dial_options(dial_options)


        async def main():
            # Make a ViamClient
            async with await connect() as viam_client:
                # Instantiate a BillingClient to run billing client API methods on
                billing_client = viam_client.billing_client

        if __name__ == '__main__':
            asyncio.run(main())

    For more information, see `Billing Client API <https://docs.viam.com/dev/reference/apis/billing-client/>`_.
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

        ::

           usage = await billing_client.get_current_month_usage("<ORG-ID>")

        Args:
            org_id (str): the ID of the organization to request usage data for

        Returns:
            viam.proto.app.billing.GetCurrentMonthUsageResponse: the current month usage information

        For more information, see `Billing Client API <https://docs.viam.com/dev/reference/apis/billing-client/#getcurrentmonthusage>`_.
        """
        request = GetCurrentMonthUsageRequest(org_id=org_id)
        return await self._billing_client.GetCurrentMonthUsage(request, metadata=self._metadata, timeout=timeout)

    async def get_invoice_pdf(self, invoice_id: str, org_id: str, dest: str, timeout: Optional[float] = None) -> None:
        """Access invoice PDF data and optionally save it to a provided file path.

        ::

            await billing_client.get_invoice_pdf("<INVOICE-ID>", "<ORG-ID>", "invoice.pdf")

        Args:
            invoice_id (str): the ID of the invoice being requested
            org_id (str): the ID of the org to request data from
            dest (str): the filepath to save the invoice to

        For more information, see `Billing Client API <https://docs.viam.com/dev/reference/apis/billing-client/#getinvoicepdf>`_.
        """
        stream: Stream[GetInvoicePdfRequest, GetInvoicePdfResponse]
        async with self._billing_client.GetInvoicePdf.open(timeout=timeout, metadata=self._metadata) as stream:
            await stream.send_message(GetInvoicePdfRequest(id=invoice_id, org_id=org_id), end=True)
            with open(dest, "wb") as file:
                async for response in stream:
                    file.write(response.chunk)

    async def get_invoices_summary(self, org_id: str, timeout: Optional[float] = None) -> GetInvoicesSummaryResponse:
        """Access total outstanding balance plus invoice summaries for a given org.

        ::

            summary = await billing_client.get_invoices_summary("<ORG-ID>")

        Args:
            org_id (str): the ID of the org to request data for

        Returns:
            viam.proto.app.billing.GetInvoicesSummaryResponse: the summaries of all org invoices

        For more information, see `Billing Client API <https://docs.viam.com/dev/reference/apis/billing-client/#getinvoicessummary>`_.
        """
        request = GetInvoicesSummaryRequest(org_id=org_id)
        return await self._billing_client.GetInvoicesSummary(request, metadata=self._metadata, timeout=timeout)

    async def get_org_billing_information(self, org_id: str, timeout: Optional[float] = None) -> GetOrgBillingInformationResponse:
        """Access billing information (payment method, billing tier, etc.) for a given org.

        ::

            information = await billing_client.get_org_billing_information("<ORG-ID>")

        Args:
            org_id (str): the ID of the org to request data for

        Returns:
            viam.proto.app.billing.GetOrgBillingInformationResponse: the org billing information

        For more information, see `Billing Client API <https://docs.viam.com/dev/reference/apis/billing-client/#getorgbillinginformation>`_.
        """
        request = GetOrgBillingInformationRequest(org_id=org_id)
        return await self._billing_client.GetOrgBillingInformation(request, metadata=self._metadata, timeout=timeout)

    async def create_invoice_and_charge_immediately(
        self,
        org_id_to_charge: str,
        amount: float,
        description: Optional[str] = None,
        org_id_for_branding: Optional[str] = None,
        disable_email: bool = False,
    ) -> CreateInvoiceAndChargeImmediatelyResponse:
        """Create a flat fee invoice and charge the organization on the spot. The caller must be an owner of the organization being charged.
        This function returns the invoice id once the payment intent is successfully sent for processing. Callers may poll the invoice for
        its status using the `get_invoices_summary` function and the returned invoice id. The status will be "payment_processing" if the
        payment is being processed, "paid" if it succeeds, or "outstanding" if it fails.

        ::

            invoice_id = await billing_client.create_invoice_and_charge_immediately(
                "<ORG-ID-TO-CHARGE>",
                <AMOUNT>,
                <DESCRIPTION>,
                "<ORG-ID-FOR-BRANDING>",
                False,
            )

        Args:
            org_id_to_charge (str): the organization to charge
            amount (float): the amount to charge in dollars
            description (str): a short description of the charge to display on the invoice PDF (must be 100 characters or less)
            org_id_for_branding (str): the organization whose branding to use in the invoice confirmation email
            disable_email (bool): whether or not to disable sending an email confirmation for the invoice

        Returns:
            viam.proto.app.billing.CreateInvoiceAndChargeImmediatelyResponse: the invoice id
        """
        request = CreateInvoiceAndChargeImmediatelyRequest(
            org_id_to_charge=org_id_to_charge,
            amount=amount,
            description=description,
            org_id_for_branding=org_id_for_branding,
            disable_email=disable_email,
        )
        return await self._billing_client.CreateInvoiceAndChargeImmediately(request, metadata=self._metadata)
