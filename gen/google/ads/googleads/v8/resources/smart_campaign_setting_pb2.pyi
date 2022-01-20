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

class SmartCampaignSetting(google.protobuf.message.Message):
    """Proto file describing the Smart campaign setting resource.

    Settings for configuring Smart campaigns.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PhoneNumber(google.protobuf.message.Message):
        """Phone number and country code in smart campaign settings."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        PHONE_NUMBER_FIELD_NUMBER: builtins.int
        COUNTRY_CODE_FIELD_NUMBER: builtins.int
        phone_number: typing.Text = ...
        """Phone number of the smart campaign."""

        country_code: typing.Text = ...
        """Upper-case, two-letter country code as defined by ISO-3166."""

        def __init__(self,
            *,
            phone_number : typing.Optional[typing.Text] = ...,
            country_code : typing.Optional[typing.Text] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["_country_code",b"_country_code","_phone_number",b"_phone_number","country_code",b"country_code","phone_number",b"phone_number"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["_country_code",b"_country_code","_phone_number",b"_phone_number","country_code",b"country_code","phone_number",b"phone_number"]) -> None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_country_code",b"_country_code"]) -> typing.Optional[typing_extensions.Literal["country_code"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_phone_number",b"_phone_number"]) -> typing.Optional[typing_extensions.Literal["phone_number"]]: ...

    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CAMPAIGN_FIELD_NUMBER: builtins.int
    PHONE_NUMBER_FIELD_NUMBER: builtins.int
    FINAL_URL_FIELD_NUMBER: builtins.int
    ADVERTISING_LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    BUSINESS_NAME_FIELD_NUMBER: builtins.int
    BUSINESS_LOCATION_ID_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the Smart campaign setting.
    Smart campaign setting resource names have the form:

    `customers/{customer_id}/smartCampaignSettings/{campaign_id}`
    """

    campaign: typing.Text = ...
    """Output only. The campaign to which these settings apply."""

    @property
    def phone_number(self) -> global___SmartCampaignSetting.PhoneNumber:
        """Phone number and country code."""
        pass
    final_url: typing.Text = ...
    """Landing page url given by user for this Campaign."""

    advertising_language_code: typing.Text = ...
    """The ISO-639-1 language code to advertise in."""

    business_name: typing.Text = ...
    """The name of the business."""

    business_location_id: builtins.int = ...
    """The ID of the Business Profile location.
    The location ID can be fetched by Business Profile API with its form:
    accounts/{accountId}/locations/{locationId}. The last {locationId}
    component from the Business Profile API represents the
    business_location_id. See the [Business Profile API]
    (https://developers.google.com/my-business/reference/rest/v4/accounts.locations)
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        campaign : typing.Text = ...,
        phone_number : typing.Optional[global___SmartCampaignSetting.PhoneNumber] = ...,
        final_url : typing.Text = ...,
        advertising_language_code : typing.Text = ...,
        business_name : typing.Text = ...,
        business_location_id : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["business_location_id",b"business_location_id","business_name",b"business_name","business_setting",b"business_setting","phone_number",b"phone_number"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["advertising_language_code",b"advertising_language_code","business_location_id",b"business_location_id","business_name",b"business_name","business_setting",b"business_setting","campaign",b"campaign","final_url",b"final_url","phone_number",b"phone_number","resource_name",b"resource_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["business_setting",b"business_setting"]) -> typing.Optional[typing_extensions.Literal["business_name","business_location_id"]]: ...
global___SmartCampaignSetting = SmartCampaignSetting
