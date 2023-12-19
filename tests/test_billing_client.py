import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.app.billing_client import BillingClient
from viam.proto.app.billing import (
    GetCurrentMonthUsageResponse,
    GetInvoicesSummaryResponse,
    GetOrgBillingInformationResponse,
    InvoiceSummary,
)

from .mocks.services import MockBilling

PDF = b"abc123"
CLOUD_STORAGE_USAGE_COST = 100.0
DATA_UPLOAD_USAGE_COST = 101.0
DATA_EGRES_USAGE_COST = 102.0
REMOTE_CONTROL_USAGE_COST = 103.0
STANDARD_COMPUTE_USAGE_COST = 104.0
DISCOUNT_AMOUNT = 0.0
TOTAL_USAGE_WITH_DISCOUNT = 105.0
TOTAL_USAGE_WITHOUT_DISCOUNT = 106.0
OUTSTANDING_BALANCE = 1000.0
SECONDS_START = 978310861
NANOS_START = 0
SECONDS_END = 998310861
NANOS_END = 0
SECONDS_PAID = 988310861
NANOS_PAID = 0
START_TS = Timestamp(seconds=SECONDS_START, nanos=NANOS_END)
PAID_DATE_TS = Timestamp(seconds=SECONDS_PAID, nanos=NANOS_PAID)
END_TS = Timestamp(seconds=SECONDS_END, nanos=NANOS_END)
INVOICE_ID = "invoice"
STATUS = "status"
PAYMENT_TYPE = 1
EMAIL = "email@fake.com"
BILLING_TIER = "tier"
INVOICE = InvoiceSummary(
    id=INVOICE_ID,
    invoice_date=START_TS,
    invoice_amount=OUTSTANDING_BALANCE,
    status=STATUS,
    due_date=END_TS,
    paid_date=PAID_DATE_TS,
)
INVOICES = [INVOICE]
CURR_MONTH_USAGE = GetCurrentMonthUsageResponse(
    start_date=START_TS,
    end_date=END_TS,
    cloud_storage_usage_cost=CLOUD_STORAGE_USAGE_COST,
    data_upload_usage_cost=DATA_UPLOAD_USAGE_COST,
    data_egres_usage_cost=DATA_EGRES_USAGE_COST,
    remote_control_usage_cost=REMOTE_CONTROL_USAGE_COST,
    standard_compute_usage_cost=STANDARD_COMPUTE_USAGE_COST,
    discount_amount=DISCOUNT_AMOUNT,
    total_usage_with_discount=TOTAL_USAGE_WITH_DISCOUNT,
    total_usage_without_discount=TOTAL_USAGE_WITHOUT_DISCOUNT,
)
INVOICES_SUMMARY = GetInvoicesSummaryResponse(outstanding_balance=OUTSTANDING_BALANCE, invoices=INVOICES)
ORG_BILLING_INFO = GetOrgBillingInformationResponse(
    type=PAYMENT_TYPE,
    billing_email=EMAIL,
    billing_tier=BILLING_TIER,
)

AUTH_TOKEN = "auth_token"
BILLING_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockBilling:
    return MockBilling(
        pdf=PDF,
        curr_month_usage=CURR_MONTH_USAGE,
        invoices_summary=INVOICES_SUMMARY,
        billing_info=ORG_BILLING_INFO,
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_get_current_month_usage(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            org_id = "foo"
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            curr_month_usage = await client.get_current_month_usage(org_id=org_id)
            assert curr_month_usage == CURR_MONTH_USAGE
            assert service.org_id == org_id

    @pytest.mark.asyncio
    async def test_get_invoice_pdf(self, service: MockBilling):
        assert True

    @pytest.mark.asyncio
    async def test_get_invoices_summary(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            org_id = "bar"
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            invoices_summary = await client.get_invoices_summary(org_id=org_id)
            assert invoices_summary == INVOICES_SUMMARY
            assert service.org_id == org_id

    @pytest.mark.asyncio
    async def test_get_org_billing_information(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            org_id = "baz"
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            org_billing_info = await client.get_org_billing_information(org_id=org_id)
            assert org_billing_info == ORG_BILLING_INFO
            assert service.org_id == org_id
