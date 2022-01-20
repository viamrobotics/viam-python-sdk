"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.month_of_year_pb2
import google.ads.googleads.v8.resources.invoice_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ListInvoicesRequest(google.protobuf.message.Message):
    """Request message for fetching the invoices of a given billing setup that were
    issued during a given month.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    BILLING_SETUP_FIELD_NUMBER: builtins.int
    ISSUE_YEAR_FIELD_NUMBER: builtins.int
    ISSUE_MONTH_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer to fetch invoices for."""

    billing_setup: typing.Text = ...
    """Required. The billing setup resource name of the requested invoices.

    `customers/{customer_id}/billingSetups/{billing_setup_id}`
    """

    issue_year: typing.Text = ...
    """Required. The issue year to retrieve invoices, in yyyy format. Only
    invoices issued in 2019 or later can be retrieved.
    """

    issue_month: google.ads.googleads.v8.enums.month_of_year_pb2.MonthOfYearEnum.MonthOfYear.ValueType = ...
    """Required. The issue month to retrieve invoices."""

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        billing_setup : typing.Text = ...,
        issue_year : typing.Text = ...,
        issue_month : google.ads.googleads.v8.enums.month_of_year_pb2.MonthOfYearEnum.MonthOfYear.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["billing_setup",b"billing_setup","customer_id",b"customer_id","issue_month",b"issue_month","issue_year",b"issue_year"]) -> None: ...
global___ListInvoicesRequest = ListInvoicesRequest

class ListInvoicesResponse(google.protobuf.message.Message):
    """Response message for [InvoiceService.ListInvoices][google.ads.googleads.v8.services.InvoiceService.ListInvoices]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INVOICES_FIELD_NUMBER: builtins.int
    @property
    def invoices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.ads.googleads.v8.resources.invoice_pb2.Invoice]:
        """The list of invoices that match the billing setup and time period."""
        pass
    def __init__(self,
        *,
        invoices : typing.Optional[typing.Iterable[google.ads.googleads.v8.resources.invoice_pb2.Invoice]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["invoices",b"invoices"]) -> None: ...
global___ListInvoicesResponse = ListInvoicesResponse
