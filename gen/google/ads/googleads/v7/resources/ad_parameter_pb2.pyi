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

class AdParameter(google.protobuf.message.Message):
    """Proto file describing the ad parameter resource.

    An ad parameter that is used to update numeric values (such as prices or
    inventory levels) in any text line of an ad (including URLs). There can
    be a maximum of two AdParameters per ad group criterion. (One with
    parameter_index = 1 and one with parameter_index = 2.)
    In the ad the parameters are referenced by a placeholder of the form
    "{param#:value}". E.g. "{param1:$17}"
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    AD_GROUP_CRITERION_FIELD_NUMBER: builtins.int
    PARAMETER_INDEX_FIELD_NUMBER: builtins.int
    INSERTION_TEXT_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the ad parameter.
    Ad parameter resource names have the form:

    `customers/{customer_id}/adParameters/{ad_group_id}~{criterion_id}~{parameter_index}`
    """

    ad_group_criterion: typing.Text = ...
    """Immutable. The ad group criterion that this ad parameter belongs to."""

    parameter_index: builtins.int = ...
    """Immutable. The unique index of this ad parameter. Must be either 1 or 2."""

    insertion_text: typing.Text = ...
    """Numeric value to insert into the ad text. The following restrictions
     apply:
     - Can use comma or period as a separator, with an optional period or
       comma (respectively) for fractional values. For example, 1,000,000.00
       and 2.000.000,10 are valid.
     - Can be prepended or appended with a currency symbol. For example,
       $99.99 is valid.
     - Can be prepended or appended with a currency code. For example, 99.99USD
       and EUR200 are valid.
     - Can use '%'. For example, 1.0% and 1,0% are valid.
     - Can use plus or minus. For example, -10.99 and 25+ are valid.
     - Can use '/' between two numbers. For example 4/1 and 0.95/0.45 are
       valid.
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ad_group_criterion : typing.Optional[typing.Text] = ...,
        parameter_index : typing.Optional[builtins.int] = ...,
        insertion_text : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_ad_group_criterion",b"_ad_group_criterion","_insertion_text",b"_insertion_text","_parameter_index",b"_parameter_index","ad_group_criterion",b"ad_group_criterion","insertion_text",b"insertion_text","parameter_index",b"parameter_index"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_ad_group_criterion",b"_ad_group_criterion","_insertion_text",b"_insertion_text","_parameter_index",b"_parameter_index","ad_group_criterion",b"ad_group_criterion","insertion_text",b"insertion_text","parameter_index",b"parameter_index","resource_name",b"resource_name"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_ad_group_criterion",b"_ad_group_criterion"]) -> typing.Optional[typing_extensions.Literal["ad_group_criterion"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_insertion_text",b"_insertion_text"]) -> typing.Optional[typing_extensions.Literal["insertion_text"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_parameter_index",b"_parameter_index"]) -> typing.Optional[typing_extensions.Literal["parameter_index"]]: ...
global___AdParameter = AdParameter
