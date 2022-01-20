"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.hotel_reconciliation_status_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class HotelReconciliation(google.protobuf.message.Message):
    """Proto file describing the hotel reconciliation resource.

    A hotel reconciliation. It contains conversion information from Hotel
    bookings to reconcile with advertiser records. These rows may be updated
    or canceled before billing via Bulk Uploads.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    COMMISSION_ID_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    HOTEL_CENTER_ID_FIELD_NUMBER: builtins.int
    HOTEL_ID_FIELD_NUMBER: builtins.int
    CHECK_IN_DATE_FIELD_NUMBER: builtins.int
    CHECK_OUT_DATE_FIELD_NUMBER: builtins.int
    RECONCILED_VALUE_MICROS_FIELD_NUMBER: builtins.int
    BILLED_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the hotel reconciliation.
    Hotel reconciliation resource names have the form:

    `customers/{customer_id}/hotelReconciliations/{commission_id}`
    """

    commission_id: typing.Text = ...
    """Required. Output only. The commission ID is Google's ID for this booking. Every booking event is
    assigned a Commission ID to help you match it to a guest stay.
    """

    order_id: typing.Text = ...
    """Output only. The order ID is the identifier for this booking as provided in the
    'transaction_id' parameter of the conversion tracking tag.
    """

    hotel_center_id: builtins.int = ...
    """Output only. Identifier for the Hotel Center account which provides the rates for the
    Hotel campaign.
    """

    hotel_id: typing.Text = ...
    """Output only. Unique identifier for the booked property, as provided in the Hotel Center
    feed. The hotel ID comes from the 'ID' parameter of the conversion tracking
    tag.
    """

    check_in_date: typing.Text = ...
    """Output only. Check-in date recorded when the booking is made. If the check-in date is
    modified at reconciliation, the revised date will then take the place of
    the original date in this column. Format is YYYY-MM-DD.
    """

    check_out_date: typing.Text = ...
    """Output only. Check-out date recorded when the booking is made. If the check-in date is
    modified at reconciliation, the revised date will then take the place of
    the original date in this column. Format is YYYY-MM-DD.
    """

    reconciled_value_micros: builtins.int = ...
    """Required. Output only. Reconciled value is the final value of a booking as paid by the guest. If
    original booking value changes for any reason, such as itinerary changes or
    room upsells, the reconciled value should be the full final amount
    collected. If a booking is canceled, the reconciled value should include
    the value of any cancellation fees or non-refundable nights charged. Value
    is in millionths of the base unit currency. For example, $12.35 would be
    represented as 12350000. Currency unit is in the default customer currency.
    """

    billed: builtins.bool = ...
    """Output only. Whether a given booking has been billed. Once billed, a booking can't be
    modified.
    """

    status: google.ads.googleads.v9.enums.hotel_reconciliation_status_pb2.HotelReconciliationStatusEnum.HotelReconciliationStatus.ValueType = ...
    """Required. Output only. Current status of a booking with regards to reconciliation and billing.
    Bookings should be reconciled within 45 days after the check-out date.
    Any booking not reconciled within 45 days will be billed at its original
    value.
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        commission_id : typing.Text = ...,
        order_id : typing.Text = ...,
        hotel_center_id : builtins.int = ...,
        hotel_id : typing.Text = ...,
        check_in_date : typing.Text = ...,
        check_out_date : typing.Text = ...,
        reconciled_value_micros : builtins.int = ...,
        billed : builtins.bool = ...,
        status : google.ads.googleads.v9.enums.hotel_reconciliation_status_pb2.HotelReconciliationStatusEnum.HotelReconciliationStatus.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["billed",b"billed","check_in_date",b"check_in_date","check_out_date",b"check_out_date","commission_id",b"commission_id","hotel_center_id",b"hotel_center_id","hotel_id",b"hotel_id","order_id",b"order_id","reconciled_value_micros",b"reconciled_value_micros","resource_name",b"resource_name","status",b"status"]) -> None: ...
global___HotelReconciliation = HotelReconciliation
