"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.enums.account_link_status_pb2
import google.ads.googleads.v7.enums.linked_account_type_pb2
import google.ads.googleads.v7.enums.mobile_app_vendor_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AccountLink(google.protobuf.message.Message):
    """Represents the data sharing connection between a Google Ads account and
    another account
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ACCOUNT_LINK_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    THIRD_PARTY_APP_ANALYTICS_FIELD_NUMBER: builtins.int
    DATA_PARTNER_FIELD_NUMBER: builtins.int
    GOOGLE_ADS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. Resource name of the account link.
    AccountLink resource names have the form:
    `customers/{customer_id}/accountLinks/{account_link_id}`
    """

    account_link_id: builtins.int = ...
    """Output only. The ID of the link.
    This field is read only.
    """

    status: google.ads.googleads.v7.enums.account_link_status_pb2.AccountLinkStatusEnum.AccountLinkStatus.ValueType = ...
    """The status of the link."""

    type: google.ads.googleads.v7.enums.linked_account_type_pb2.LinkedAccountTypeEnum.LinkedAccountType.ValueType = ...
    """Output only. The type of the linked account."""

    @property
    def third_party_app_analytics(self) -> global___ThirdPartyAppAnalyticsLinkIdentifier:
        """Immutable. A third party app analytics link."""
        pass
    @property
    def data_partner(self) -> global___DataPartnerLinkIdentifier:
        """Output only. Data partner link."""
        pass
    @property
    def google_ads(self) -> global___GoogleAdsLinkIdentifier:
        """Output only. Google Ads link."""
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        account_link_id : typing.Optional[builtins.int] = ...,
        status : google.ads.googleads.v7.enums.account_link_status_pb2.AccountLinkStatusEnum.AccountLinkStatus.ValueType = ...,
        type : google.ads.googleads.v7.enums.linked_account_type_pb2.LinkedAccountTypeEnum.LinkedAccountType.ValueType = ...,
        third_party_app_analytics : typing.Optional[global___ThirdPartyAppAnalyticsLinkIdentifier] = ...,
        data_partner : typing.Optional[global___DataPartnerLinkIdentifier] = ...,
        google_ads : typing.Optional[global___GoogleAdsLinkIdentifier] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_account_link_id",b"_account_link_id","account_link_id",b"account_link_id","data_partner",b"data_partner","google_ads",b"google_ads","linked_account",b"linked_account","third_party_app_analytics",b"third_party_app_analytics"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_account_link_id",b"_account_link_id","account_link_id",b"account_link_id","data_partner",b"data_partner","google_ads",b"google_ads","linked_account",b"linked_account","resource_name",b"resource_name","status",b"status","third_party_app_analytics",b"third_party_app_analytics","type",b"type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_account_link_id",b"_account_link_id"]) -> typing.Optional[typing_extensions.Literal["account_link_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["linked_account",b"linked_account"]) -> typing.Optional[typing_extensions.Literal["third_party_app_analytics","data_partner","google_ads"]]: ...
global___AccountLink = AccountLink

class ThirdPartyAppAnalyticsLinkIdentifier(google.protobuf.message.Message):
    """The identifiers of a Third Party App Analytics Link."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    APP_ANALYTICS_PROVIDER_ID_FIELD_NUMBER: builtins.int
    APP_ID_FIELD_NUMBER: builtins.int
    APP_VENDOR_FIELD_NUMBER: builtins.int
    app_analytics_provider_id: builtins.int = ...
    """Immutable. The ID of the app analytics provider.
    This field should not be empty when creating a new third
    party app analytics link. It is unable to be modified after the creation of
    the link.
    """

    app_id: typing.Text = ...
    """Immutable. A string that uniquely identifies a mobile application from which the data
    was collected to the Google Ads API. For iOS, the ID string is the 9 digit
    string that appears at the end of an App Store URL (e.g., "422689480" for
    "Gmail" whose App Store link is
    https://apps.apple.com/us/app/gmail-email-by-google/id422689480). For
    Android, the ID string is the application's package name (e.g.,
    "com.google.android.gm" for "Gmail" given Google Play link
    https://play.google.com/store/apps/details?id=com.google.android.gm)
    This field should not be empty when creating a new third
    party app analytics link. It is unable to be modified after the creation of
    the link.
    """

    app_vendor: google.ads.googleads.v7.enums.mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor.ValueType = ...
    """Immutable. The vendor of the app.
    This field should not be empty when creating a new third
    party app analytics link. It is unable to be modified after the creation of
    the link.
    """

    def __init__(self,
        *,
        app_analytics_provider_id : typing.Optional[builtins.int] = ...,
        app_id : typing.Optional[typing.Text] = ...,
        app_vendor : google.ads.googleads.v7.enums.mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_app_analytics_provider_id",b"_app_analytics_provider_id","_app_id",b"_app_id","app_analytics_provider_id",b"app_analytics_provider_id","app_id",b"app_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_app_analytics_provider_id",b"_app_analytics_provider_id","_app_id",b"_app_id","app_analytics_provider_id",b"app_analytics_provider_id","app_id",b"app_id","app_vendor",b"app_vendor"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_app_analytics_provider_id",b"_app_analytics_provider_id"]) -> typing.Optional[typing_extensions.Literal["app_analytics_provider_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_app_id",b"_app_id"]) -> typing.Optional[typing_extensions.Literal["app_id"]]: ...
global___ThirdPartyAppAnalyticsLinkIdentifier = ThirdPartyAppAnalyticsLinkIdentifier

class DataPartnerLinkIdentifier(google.protobuf.message.Message):
    """The identifier for Data Partner account."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_PARTNER_ID_FIELD_NUMBER: builtins.int
    data_partner_id: builtins.int = ...
    """Immutable. The customer ID of the Data partner account.
    This field is required and should not be empty when creating a new
    data partner link. It is unable to be modified after the creation of
    the link.
    """

    def __init__(self,
        *,
        data_partner_id : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_data_partner_id",b"_data_partner_id","data_partner_id",b"data_partner_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_data_partner_id",b"_data_partner_id","data_partner_id",b"data_partner_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_data_partner_id",b"_data_partner_id"]) -> typing.Optional[typing_extensions.Literal["data_partner_id"]]: ...
global___DataPartnerLinkIdentifier = DataPartnerLinkIdentifier

class GoogleAdsLinkIdentifier(google.protobuf.message.Message):
    """The identifier for Google Ads account."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_FIELD_NUMBER: builtins.int
    customer: typing.Text = ...
    """Immutable. The resource name of the Google Ads account.
    This field is required and should not be empty when creating a new
    Google Ads link. It is unable to be modified after the creation of
    the link.
    """

    def __init__(self,
        *,
        customer : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_customer",b"_customer","customer",b"customer"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_customer",b"_customer","customer",b"customer"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_customer",b"_customer"]) -> typing.Optional[typing_extensions.Literal["customer"]]: ...
global___GoogleAdsLinkIdentifier = GoogleAdsLinkIdentifier
