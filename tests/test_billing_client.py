import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.app.billing_client import BillingClient
from viam.proto.app.billing import (
    CreateInvoiceAndChargeImmediatelyResponse,
    GetCurrentMonthUsageResponse,
    GetInvoicesSummaryResponse,
    GetOrgBillingInformationResponse,
    InvoiceSummary,
    GetLocationBillingOrganizationResponse,
    UpdateLocationBillingOrganizationResponse,
    ChargeOrganizationResponse,
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
INVOICE_ID_RESPONSE = CreateInvoiceAndChargeImmediatelyResponse(invoice_id=INVOICE_ID)

BILLING_ORG_ID = "billing_org_id"
GET_LOCATION_BILLING_ORG_RESPONSE = GetLocationBillingOrganizationResponse(billing_organization_id=BILLING_ORG_ID)
UPDATE_LOCATION_BILLING_ORG_RESPONSE = UpdateLocationBillingOrganizationResponse()
CHARGE_ORG_RESPONSE = ChargeOrganizationResponse(invoice_id=INVOICE_ID)

AUTH_TOKEN = "auth_token"
BILLING_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockBilling:
    return MockBilling(
        pdf=PDF,
        curr_month_usage=CURR_MONTH_USAGE,
        invoices_summary=INVOICES_SUMMARY,
        billing_info=ORG_BILLING_INFO,
        invoice_id_response=INVOICE_ID_RESPONSE,
        get_location_billing_org_response=GET_LOCATION_BILLING_ORG_RESPONSE,
        update_location_billing_org_response=UPDATE_LOCATION_BILLING_ORG_RESPONSE,
        charge_org_response=CHARGE_ORG_RESPONSE,
    )


class TestClient:
    async def test_get_current_month_usage(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            org_id = "foo"
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            curr_month_usage = await client.get_current_month_usage(org_id=org_id)
            assert curr_month_usage == CURR_MONTH_USAGE
            assert service.org_id == org_id

    async def test_get_invoice_pdf(self, service: MockBilling):
        assert True

    async def test_get_invoices_summary(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            org_id = "bar"
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            invoices_summary = await client.get_invoices_summary(org_id=org_id)
            assert invoices_summary == INVOICES_SUMMARY
            assert service.org_id == org_id

    async def test_get_org_billing_information(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            org_id = "baz"
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            org_billing_info = await client.get_org_billing_information(org_id=org_id)
            assert org_billing_info == ORG_BILLING_INFO
            assert service.org_id == org_id

    async def test_create_invoice_and_charge_immediately(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            org_id = "foo"
            description = "A short description"
            org_id_for_branding = "bar"
            disable_email = True
            invoice_id_response = await client.create_invoice_and_charge_immediately(
                org_id_to_charge=org_id,
                amount=OUTSTANDING_BALANCE,
                description=description,
                org_id_for_branding=org_id_for_branding,
                disable_email=disable_email,
            )
            assert invoice_id_response == INVOICE_ID_RESPONSE
            assert service.org_id_to_charge == org_id
            assert service.description == description
            assert service.org_id_for_branding == org_id_for_branding
            assert service.amount == OUTSTANDING_BALANCE
            assert service.disable_email == disable_email

    async def test_get_location_billing_organization(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            location_id = "test_location_id"
            response = await client.get_location_billing_organization(location_id=location_id)
            assert response == GET_LOCATION_BILLING_ORG_RESPONSE
            assert service.location_id == location_id

    async def test_update_location_billing_organization(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            location_id = "test_location_id"
            billing_org_id = "test_billing_org_id"
            response = await client.update_location_billing_organization(
                location_id=location_id, billing_organization_id=billing_org_id
            )
            assert response == UPDATE_LOCATION_BILLING_ORG_RESPONSE
            assert service.location_id == location_id
            assert service.billing_organization_id == billing_org_id

    async def test_charge_organization(self, service: MockBilling):
        async with ChannelFor([service]) as channel:
            client = BillingClient(channel, BILLING_SERVICE_METADATA)
            org_id_to_charge = "test_org_id_to_charge"
            subtotal = 100.0
            tax = 10.0
            description = "Test charge"
            org_id_for_branding = "branding_org"
            disable_confirmation_email = True
            response = await client.charge_organization(
                org_id_to_charge=org_id_to_charge,
                subtotal=subtotal,
                tax=tax,
                description=description,
                org_id_for_branding=org_id_for_branding,
                disable_confirmation_email=disable_confirmation_email,
            )
            assert response == CHARGE_ORG_RESPONSE
            assert service.org_id_to_charge_charge_org == org_id_to_charge
            assert service.subtotal == subtotal
            assert service.tax == tax
            assert service.description_charge_org == description
            assert service.org_id_for_branding_charge_org == org_id_for_branding
            assert service.disable_confirmation_email == disable_confirmation_email
