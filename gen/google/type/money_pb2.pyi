"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Money(google.protobuf.message.Message):
    """Represents an amount of money with its currency type."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CURRENCY_CODE_FIELD_NUMBER: builtins.int
    UNITS_FIELD_NUMBER: builtins.int
    NANOS_FIELD_NUMBER: builtins.int
    currency_code: typing.Text = ...
    """The three-letter currency code defined in ISO 4217."""

    units: builtins.int = ...
    """The whole units of the amount.
    For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.
    """

    nanos: builtins.int = ...
    """Number of nano (10^-9) units of the amount.
    The value must be between -999,999,999 and +999,999,999 inclusive.
    If `units` is positive, `nanos` must be positive or zero.
    If `units` is zero, `nanos` can be positive, zero, or negative.
    If `units` is negative, `nanos` must be negative or zero.
    For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.
    """

    def __init__(self,
        *,
        currency_code : typing.Text = ...,
        units : builtins.int = ...,
        nanos : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["currency_code",b"currency_code","nanos",b"nanos","units",b"units"]) -> None: ...
global___Money = Money
