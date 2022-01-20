"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.common.dates_pb2
import google.ads.googleads.v8.enums.invoice_type_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Invoice(google.protobuf.message.Message):
    """Proto file describing the Invoice resource.

    An invoice. All invoice information is snapshotted to match the PDF invoice.
    For invoices older than the launch of InvoiceService, the snapshotted
    information may not match the PDF invoice.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class AccountBudgetSummary(google.protobuf.message.Message):
        """Represents a summarized account budget billable cost."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        CUSTOMER_FIELD_NUMBER: builtins.int
        CUSTOMER_DESCRIPTIVE_NAME_FIELD_NUMBER: builtins.int
        ACCOUNT_BUDGET_FIELD_NUMBER: builtins.int
        ACCOUNT_BUDGET_NAME_FIELD_NUMBER: builtins.int
        PURCHASE_ORDER_NUMBER_FIELD_NUMBER: builtins.int
        SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
        TAX_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
        TOTAL_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
        BILLABLE_ACTIVITY_DATE_RANGE_FIELD_NUMBER: builtins.int
        customer: typing.Text = ...
        """Output only. The resource name of the customer associated with this account budget.
        This contains the customer ID, which appears on the invoice PDF as
        "Account ID".
        Customer resource names have the form:

        `customers/{customer_id}`
        """

        customer_descriptive_name: typing.Text = ...
        """Output only. The descriptive name of the account budget’s customer. It appears on the
        invoice PDF as "Account".
        """

        account_budget: typing.Text = ...
        """Output only. The resource name of the account budget associated with this summarized
        billable cost.
        AccountBudget resource names have the form:

        `customers/{customer_id}/accountBudgets/{account_budget_id}`
        """

        account_budget_name: typing.Text = ...
        """Output only. The name of the account budget. It appears on the invoice PDF as "Account
        budget".
        """

        purchase_order_number: typing.Text = ...
        """Output only. The purchase order number of the account budget. It appears on the
        invoice PDF as "Purchase order".
        """

        subtotal_amount_micros: builtins.int = ...
        """Output only. The pretax subtotal amount attributable to this budget during the service
        period, in micros.
        """

        tax_amount_micros: builtins.int = ...
        """Output only. The tax amount attributable to this budget during the service period, in
        micros.
        """

        total_amount_micros: builtins.int = ...
        """Output only. The total amount attributable to this budget during the service period,
        in micros. This equals the sum of the account budget subtotal amount and
        the account budget tax amount.
        """

        @property
        def billable_activity_date_range(self) -> google.ads.googleads.v8.common.dates_pb2.DateRange:
            """Output only. The billable activity date range of the account budget, within the
            service date range of this invoice. The end date is inclusive. This can
            be different from the account budget's start and end time.
            """
            pass
        def __init__(self,
            *,
            customer : typing.Optional[typing.Text] = ...,
            customer_descriptive_name : typing.Optional[typing.Text] = ...,
            account_budget : typing.Optional[typing.Text] = ...,
            account_budget_name : typing.Optional[typing.Text] = ...,
            purchase_order_number : typing.Optional[typing.Text] = ...,
            subtotal_amount_micros : typing.Optional[builtins.int] = ...,
            tax_amount_micros : typing.Optional[builtins.int] = ...,
            total_amount_micros : typing.Optional[builtins.int] = ...,
            billable_activity_date_range : typing.Optional[google.ads.googleads.v8.common.dates_pb2.DateRange] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["_account_budget",b"_account_budget","_account_budget_name",b"_account_budget_name","_customer",b"_customer","_customer_descriptive_name",b"_customer_descriptive_name","_purchase_order_number",b"_purchase_order_number","_subtotal_amount_micros",b"_subtotal_amount_micros","_tax_amount_micros",b"_tax_amount_micros","_total_amount_micros",b"_total_amount_micros","account_budget",b"account_budget","account_budget_name",b"account_budget_name","billable_activity_date_range",b"billable_activity_date_range","customer",b"customer","customer_descriptive_name",b"customer_descriptive_name","purchase_order_number",b"purchase_order_number","subtotal_amount_micros",b"subtotal_amount_micros","tax_amount_micros",b"tax_amount_micros","total_amount_micros",b"total_amount_micros"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["_account_budget",b"_account_budget","_account_budget_name",b"_account_budget_name","_customer",b"_customer","_customer_descriptive_name",b"_customer_descriptive_name","_purchase_order_number",b"_purchase_order_number","_subtotal_amount_micros",b"_subtotal_amount_micros","_tax_amount_micros",b"_tax_amount_micros","_total_amount_micros",b"_total_amount_micros","account_budget",b"account_budget","account_budget_name",b"account_budget_name","billable_activity_date_range",b"billable_activity_date_range","customer",b"customer","customer_descriptive_name",b"customer_descriptive_name","purchase_order_number",b"purchase_order_number","subtotal_amount_micros",b"subtotal_amount_micros","tax_amount_micros",b"tax_amount_micros","total_amount_micros",b"total_amount_micros"]) -> None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_account_budget",b"_account_budget"]) -> typing.Optional[typing_extensions.Literal["account_budget"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_account_budget_name",b"_account_budget_name"]) -> typing.Optional[typing_extensions.Literal["account_budget_name"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_customer",b"_customer"]) -> typing.Optional[typing_extensions.Literal["customer"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_customer_descriptive_name",b"_customer_descriptive_name"]) -> typing.Optional[typing_extensions.Literal["customer_descriptive_name"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_purchase_order_number",b"_purchase_order_number"]) -> typing.Optional[typing_extensions.Literal["purchase_order_number"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_subtotal_amount_micros",b"_subtotal_amount_micros"]) -> typing.Optional[typing_extensions.Literal["subtotal_amount_micros"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_tax_amount_micros",b"_tax_amount_micros"]) -> typing.Optional[typing_extensions.Literal["tax_amount_micros"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_total_amount_micros",b"_total_amount_micros"]) -> typing.Optional[typing_extensions.Literal["total_amount_micros"]]: ...

    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    BILLING_SETUP_FIELD_NUMBER: builtins.int
    PAYMENTS_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    PAYMENTS_PROFILE_ID_FIELD_NUMBER: builtins.int
    ISSUE_DATE_FIELD_NUMBER: builtins.int
    DUE_DATE_FIELD_NUMBER: builtins.int
    SERVICE_DATE_RANGE_FIELD_NUMBER: builtins.int
    CURRENCY_CODE_FIELD_NUMBER: builtins.int
    ADJUSTMENTS_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    ADJUSTMENTS_TAX_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    ADJUSTMENTS_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    REGULATORY_COSTS_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    REGULATORY_COSTS_TAX_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    REGULATORY_COSTS_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    TAX_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    TOTAL_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    CORRECTED_INVOICE_FIELD_NUMBER: builtins.int
    REPLACED_INVOICES_FIELD_NUMBER: builtins.int
    PDF_URL_FIELD_NUMBER: builtins.int
    ACCOUNT_BUDGET_SUMMARIES_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Output only. The resource name of the invoice. Multiple customers can share a given
    invoice, so multiple resource names may point to the same invoice.
    Invoice resource names have the form:

    `customers/{customer_id}/invoices/{invoice_id}`
    """

    id: typing.Text = ...
    """Output only. The ID of the invoice. It appears on the invoice PDF as "Invoice number"."""

    type: google.ads.googleads.v8.enums.invoice_type_pb2.InvoiceTypeEnum.InvoiceType.ValueType = ...
    """Output only. The type of invoice."""

    billing_setup: typing.Text = ...
    """Output only. The resource name of this invoice’s billing setup.

    `customers/{customer_id}/billingSetups/{billing_setup_id}`
    """

    payments_account_id: typing.Text = ...
    """Output only. A 16 digit ID used to identify the payments account associated with the
    billing setup, e.g. "1234-5678-9012-3456". It appears on the invoice PDF as
    "Billing Account Number".
    """

    payments_profile_id: typing.Text = ...
    """Output only. A 12 digit ID used to identify the payments profile associated with the
    billing setup, e.g. "1234-5678-9012". It appears on the invoice PDF as
    "Billing ID".
    """

    issue_date: typing.Text = ...
    """Output only. The issue date in yyyy-mm-dd format. It appears on the invoice PDF as
    either "Issue date" or "Invoice date".
    """

    due_date: typing.Text = ...
    """Output only. The due date in yyyy-mm-dd format."""

    @property
    def service_date_range(self) -> google.ads.googleads.v8.common.dates_pb2.DateRange:
        """Output only. The service period date range of this invoice. The end date is inclusive."""
        pass
    currency_code: typing.Text = ...
    """Output only. The currency code. All costs are returned in this currency. A subset of the
    currency codes derived from the ISO 4217 standard is supported.
    """

    adjustments_subtotal_amount_micros: builtins.int = ...
    """Output only. The pretax subtotal amount of invoice level adjustments, in micros."""

    adjustments_tax_amount_micros: builtins.int = ...
    """Output only. The sum of taxes on the invoice level adjustments, in micros."""

    adjustments_total_amount_micros: builtins.int = ...
    """Output only. The total amount of invoice level adjustments, in micros."""

    regulatory_costs_subtotal_amount_micros: builtins.int = ...
    """Output only. The pretax subtotal amount of invoice level regulatory costs, in micros."""

    regulatory_costs_tax_amount_micros: builtins.int = ...
    """Output only. The sum of taxes on the invoice level regulatory costs, in micros."""

    regulatory_costs_total_amount_micros: builtins.int = ...
    """Output only. The total amount of invoice level regulatory costs, in micros."""

    subtotal_amount_micros: builtins.int = ...
    """Output only. The pretax subtotal amount, in micros. This equals the
    sum of the AccountBudgetSummary subtotal amounts,
    Invoice.adjustments_subtotal_amount_micros, and
    Invoice.regulatory_costs_subtotal_amount_micros.
    Starting with v6, the Invoice.regulatory_costs_subtotal_amount_micros is no
    longer included.
    """

    tax_amount_micros: builtins.int = ...
    """Output only. The sum of all taxes on the invoice, in micros. This equals the sum of the
    AccountBudgetSummary tax amounts, plus taxes not associated with a specific
    account budget.
    """

    total_amount_micros: builtins.int = ...
    """Output only. The total amount, in micros. This equals the sum of
    Invoice.subtotal_amount_micros and Invoice.tax_amount_micros.
    Starting with v6, Invoice.regulatory_costs_subtotal_amount_micros is
    also added as it is no longer already included in
    Invoice.tax_amount_micros.
    """

    corrected_invoice: typing.Text = ...
    """Output only. The resource name of the original invoice corrected, wrote off, or canceled
    by this invoice, if applicable. If `corrected_invoice` is set,
    `replaced_invoices` will not be set.
    Invoice resource names have the form:

    `customers/{customer_id}/invoices/{invoice_id}`
    """

    @property
    def replaced_invoices(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Output only. The resource name of the original invoice(s) being rebilled or replaced by
        this invoice, if applicable. There might be multiple replaced invoices due
        to invoice consolidation. The replaced invoices may not belong to the same
        payments account. If `replaced_invoices` is set, `corrected_invoice` will
        not be set.
        Invoice resource names have the form:

        `customers/{customer_id}/invoices/{invoice_id}`
        """
        pass
    pdf_url: typing.Text = ...
    """Output only. The URL to a PDF copy of the invoice. Users need to pass in their OAuth
    token to request the PDF with this URL.
    """

    @property
    def account_budget_summaries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Invoice.AccountBudgetSummary]:
        """Output only. The list of summarized account budget information associated with this
        invoice.
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : typing.Optional[typing.Text] = ...,
        type : google.ads.googleads.v8.enums.invoice_type_pb2.InvoiceTypeEnum.InvoiceType.ValueType = ...,
        billing_setup : typing.Optional[typing.Text] = ...,
        payments_account_id : typing.Optional[typing.Text] = ...,
        payments_profile_id : typing.Optional[typing.Text] = ...,
        issue_date : typing.Optional[typing.Text] = ...,
        due_date : typing.Optional[typing.Text] = ...,
        service_date_range : typing.Optional[google.ads.googleads.v8.common.dates_pb2.DateRange] = ...,
        currency_code : typing.Optional[typing.Text] = ...,
        adjustments_subtotal_amount_micros : builtins.int = ...,
        adjustments_tax_amount_micros : builtins.int = ...,
        adjustments_total_amount_micros : builtins.int = ...,
        regulatory_costs_subtotal_amount_micros : builtins.int = ...,
        regulatory_costs_tax_amount_micros : builtins.int = ...,
        regulatory_costs_total_amount_micros : builtins.int = ...,
        subtotal_amount_micros : typing.Optional[builtins.int] = ...,
        tax_amount_micros : typing.Optional[builtins.int] = ...,
        total_amount_micros : typing.Optional[builtins.int] = ...,
        corrected_invoice : typing.Optional[typing.Text] = ...,
        replaced_invoices : typing.Optional[typing.Iterable[typing.Text]] = ...,
        pdf_url : typing.Optional[typing.Text] = ...,
        account_budget_summaries : typing.Optional[typing.Iterable[global___Invoice.AccountBudgetSummary]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_billing_setup",b"_billing_setup","_corrected_invoice",b"_corrected_invoice","_currency_code",b"_currency_code","_due_date",b"_due_date","_id",b"_id","_issue_date",b"_issue_date","_payments_account_id",b"_payments_account_id","_payments_profile_id",b"_payments_profile_id","_pdf_url",b"_pdf_url","_subtotal_amount_micros",b"_subtotal_amount_micros","_tax_amount_micros",b"_tax_amount_micros","_total_amount_micros",b"_total_amount_micros","billing_setup",b"billing_setup","corrected_invoice",b"corrected_invoice","currency_code",b"currency_code","due_date",b"due_date","id",b"id","issue_date",b"issue_date","payments_account_id",b"payments_account_id","payments_profile_id",b"payments_profile_id","pdf_url",b"pdf_url","service_date_range",b"service_date_range","subtotal_amount_micros",b"subtotal_amount_micros","tax_amount_micros",b"tax_amount_micros","total_amount_micros",b"total_amount_micros"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_billing_setup",b"_billing_setup","_corrected_invoice",b"_corrected_invoice","_currency_code",b"_currency_code","_due_date",b"_due_date","_id",b"_id","_issue_date",b"_issue_date","_payments_account_id",b"_payments_account_id","_payments_profile_id",b"_payments_profile_id","_pdf_url",b"_pdf_url","_subtotal_amount_micros",b"_subtotal_amount_micros","_tax_amount_micros",b"_tax_amount_micros","_total_amount_micros",b"_total_amount_micros","account_budget_summaries",b"account_budget_summaries","adjustments_subtotal_amount_micros",b"adjustments_subtotal_amount_micros","adjustments_tax_amount_micros",b"adjustments_tax_amount_micros","adjustments_total_amount_micros",b"adjustments_total_amount_micros","billing_setup",b"billing_setup","corrected_invoice",b"corrected_invoice","currency_code",b"currency_code","due_date",b"due_date","id",b"id","issue_date",b"issue_date","payments_account_id",b"payments_account_id","payments_profile_id",b"payments_profile_id","pdf_url",b"pdf_url","regulatory_costs_subtotal_amount_micros",b"regulatory_costs_subtotal_amount_micros","regulatory_costs_tax_amount_micros",b"regulatory_costs_tax_amount_micros","regulatory_costs_total_amount_micros",b"regulatory_costs_total_amount_micros","replaced_invoices",b"replaced_invoices","resource_name",b"resource_name","service_date_range",b"service_date_range","subtotal_amount_micros",b"subtotal_amount_micros","tax_amount_micros",b"tax_amount_micros","total_amount_micros",b"total_amount_micros","type",b"type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_billing_setup",b"_billing_setup"]) -> typing.Optional[typing_extensions.Literal["billing_setup"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_corrected_invoice",b"_corrected_invoice"]) -> typing.Optional[typing_extensions.Literal["corrected_invoice"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_currency_code",b"_currency_code"]) -> typing.Optional[typing_extensions.Literal["currency_code"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_due_date",b"_due_date"]) -> typing.Optional[typing_extensions.Literal["due_date"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_issue_date",b"_issue_date"]) -> typing.Optional[typing_extensions.Literal["issue_date"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_payments_account_id",b"_payments_account_id"]) -> typing.Optional[typing_extensions.Literal["payments_account_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_payments_profile_id",b"_payments_profile_id"]) -> typing.Optional[typing_extensions.Literal["payments_profile_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_pdf_url",b"_pdf_url"]) -> typing.Optional[typing_extensions.Literal["pdf_url"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_subtotal_amount_micros",b"_subtotal_amount_micros"]) -> typing.Optional[typing_extensions.Literal["subtotal_amount_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_tax_amount_micros",b"_tax_amount_micros"]) -> typing.Optional[typing_extensions.Literal["tax_amount_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_total_amount_micros",b"_total_amount_micros"]) -> typing.Optional[typing_extensions.Literal["total_amount_micros"]]: ...
global___Invoice = Invoice
