"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.common.ad_type_infos_pb2
import google.ads.googleads.v8.common.custom_parameter_pb2
import google.ads.googleads.v8.common.final_app_url_pb2
import google.ads.googleads.v8.common.url_collection_pb2
import google.ads.googleads.v8.enums.ad_type_pb2
import google.ads.googleads.v8.enums.device_pb2
import google.ads.googleads.v8.enums.system_managed_entity_source_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Ad(google.protobuf.message.Message):
    """Proto file describing the ad type.

    An ad.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    FINAL_URLS_FIELD_NUMBER: builtins.int
    FINAL_APP_URLS_FIELD_NUMBER: builtins.int
    FINAL_MOBILE_URLS_FIELD_NUMBER: builtins.int
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: builtins.int
    FINAL_URL_SUFFIX_FIELD_NUMBER: builtins.int
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: builtins.int
    DISPLAY_URL_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ADDED_BY_GOOGLE_ADS_FIELD_NUMBER: builtins.int
    DEVICE_PREFERENCE_FIELD_NUMBER: builtins.int
    URL_COLLECTIONS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SYSTEM_MANAGED_RESOURCE_SOURCE_FIELD_NUMBER: builtins.int
    TEXT_AD_FIELD_NUMBER: builtins.int
    EXPANDED_TEXT_AD_FIELD_NUMBER: builtins.int
    CALL_AD_FIELD_NUMBER: builtins.int
    EXPANDED_DYNAMIC_SEARCH_AD_FIELD_NUMBER: builtins.int
    HOTEL_AD_FIELD_NUMBER: builtins.int
    SHOPPING_SMART_AD_FIELD_NUMBER: builtins.int
    SHOPPING_PRODUCT_AD_FIELD_NUMBER: builtins.int
    GMAIL_AD_FIELD_NUMBER: builtins.int
    IMAGE_AD_FIELD_NUMBER: builtins.int
    VIDEO_AD_FIELD_NUMBER: builtins.int
    VIDEO_RESPONSIVE_AD_FIELD_NUMBER: builtins.int
    RESPONSIVE_SEARCH_AD_FIELD_NUMBER: builtins.int
    LEGACY_RESPONSIVE_DISPLAY_AD_FIELD_NUMBER: builtins.int
    APP_AD_FIELD_NUMBER: builtins.int
    LEGACY_APP_INSTALL_AD_FIELD_NUMBER: builtins.int
    RESPONSIVE_DISPLAY_AD_FIELD_NUMBER: builtins.int
    LOCAL_AD_FIELD_NUMBER: builtins.int
    DISPLAY_UPLOAD_AD_FIELD_NUMBER: builtins.int
    APP_ENGAGEMENT_AD_FIELD_NUMBER: builtins.int
    SHOPPING_COMPARISON_LISTING_AD_FIELD_NUMBER: builtins.int
    SMART_CAMPAIGN_AD_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the ad.
    Ad resource names have the form:

    `customers/{customer_id}/ads/{ad_id}`
    """

    id: builtins.int = ...
    """Output only. The ID of the ad."""

    @property
    def final_urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The list of possible final URLs after all cross-domain redirects for the
        ad.
        """
        pass
    @property
    def final_app_urls(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.ads.googleads.v8.common.final_app_url_pb2.FinalAppUrl]:
        """A list of final app URLs that will be used on mobile if the user has the
        specific app installed.
        """
        pass
    @property
    def final_mobile_urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The list of possible final mobile URLs after all cross-domain redirects
        for the ad.
        """
        pass
    tracking_url_template: typing.Text = ...
    """The URL template for constructing a tracking URL."""

    final_url_suffix: typing.Text = ...
    """The suffix to use when constructing a final URL."""

    @property
    def url_custom_parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.ads.googleads.v8.common.custom_parameter_pb2.CustomParameter]:
        """The list of mappings that can be used to substitute custom parameter tags
        in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`.
        For mutates, please use url custom parameter operations.
        """
        pass
    display_url: typing.Text = ...
    """The URL that appears in the ad description for some ad formats."""

    type: google.ads.googleads.v8.enums.ad_type_pb2.AdTypeEnum.AdType.ValueType = ...
    """Output only. The type of ad."""

    added_by_google_ads: builtins.bool = ...
    """Output only. Indicates if this ad was automatically added by Google Ads and not by a
    user. For example, this could happen when ads are automatically created as
    suggestions for new ads based on knowledge of how existing ads are
    performing.
    """

    device_preference: google.ads.googleads.v8.enums.device_pb2.DeviceEnum.Device.ValueType = ...
    """The device preference for the ad. You can only specify a preference for
    mobile devices. When this preference is set the ad will be preferred over
    other ads when being displayed on a mobile device. The ad can still be
    displayed on other device types, e.g. if no other ads are available.
    If unspecified (no device preference), all devices are targeted.
    This is only supported by some ad types.
    """

    @property
    def url_collections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.ads.googleads.v8.common.url_collection_pb2.UrlCollection]:
        """Additional URLs for the ad that are tagged with a unique identifier that
        can be referenced from other fields in the ad.
        """
        pass
    name: typing.Text = ...
    """Immutable. The name of the ad. This is only used to be able to identify the ad. It
    does not need to be unique and does not affect the served ad. The name
    field is currently only supported for DisplayUploadAd, ImageAd,
    ShoppingComparisonListingAd and VideoAd.
    """

    system_managed_resource_source: google.ads.googleads.v8.enums.system_managed_entity_source_pb2.SystemManagedResourceSourceEnum.SystemManagedResourceSource.ValueType = ...
    """Output only. If this ad is system managed, then this field will indicate the source.
    This field is read-only.
    """

    @property
    def text_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.TextAdInfo:
        """Immutable. Details pertaining to a text ad."""
        pass
    @property
    def expanded_text_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.ExpandedTextAdInfo:
        """Details pertaining to an expanded text ad."""
        pass
    @property
    def call_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.CallAdInfo:
        """Details pertaining to a call ad."""
        pass
    @property
    def expanded_dynamic_search_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.ExpandedDynamicSearchAdInfo:
        """Immutable. Details pertaining to an Expanded Dynamic Search Ad.
        This type of ad has its headline, final URLs, and display URL
        auto-generated at serving time according to domain name specific
        information provided by `dynamic_search_ads_setting` linked at the
        campaign level.
        """
        pass
    @property
    def hotel_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.HotelAdInfo:
        """Details pertaining to a hotel ad."""
        pass
    @property
    def shopping_smart_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.ShoppingSmartAdInfo:
        """Details pertaining to a Smart Shopping ad."""
        pass
    @property
    def shopping_product_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.ShoppingProductAdInfo:
        """Details pertaining to a Shopping product ad."""
        pass
    @property
    def gmail_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.GmailAdInfo:
        """Immutable. Details pertaining to a Gmail ad."""
        pass
    @property
    def image_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.ImageAdInfo:
        """Immutable. Details pertaining to an Image ad."""
        pass
    @property
    def video_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.VideoAdInfo:
        """Details pertaining to a Video ad."""
        pass
    @property
    def video_responsive_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.VideoResponsiveAdInfo:
        """Details pertaining to a Video responsive ad."""
        pass
    @property
    def responsive_search_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.ResponsiveSearchAdInfo:
        """Details pertaining to a responsive search ad."""
        pass
    @property
    def legacy_responsive_display_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.LegacyResponsiveDisplayAdInfo:
        """Details pertaining to a legacy responsive display ad."""
        pass
    @property
    def app_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.AppAdInfo:
        """Details pertaining to an app ad."""
        pass
    @property
    def legacy_app_install_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.LegacyAppInstallAdInfo:
        """Immutable. Details pertaining to a legacy app install ad."""
        pass
    @property
    def responsive_display_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.ResponsiveDisplayAdInfo:
        """Details pertaining to a responsive display ad."""
        pass
    @property
    def local_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.LocalAdInfo:
        """Details pertaining to a local ad."""
        pass
    @property
    def display_upload_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.DisplayUploadAdInfo:
        """Details pertaining to a display upload ad."""
        pass
    @property
    def app_engagement_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.AppEngagementAdInfo:
        """Details pertaining to an app engagement ad."""
        pass
    @property
    def shopping_comparison_listing_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.ShoppingComparisonListingAdInfo:
        """Details pertaining to a Shopping Comparison Listing ad."""
        pass
    @property
    def smart_campaign_ad(self) -> google.ads.googleads.v8.common.ad_type_infos_pb2.SmartCampaignAdInfo:
        """Details pertaining to a Smart campaign ad."""
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : typing.Optional[builtins.int] = ...,
        final_urls : typing.Optional[typing.Iterable[typing.Text]] = ...,
        final_app_urls : typing.Optional[typing.Iterable[google.ads.googleads.v8.common.final_app_url_pb2.FinalAppUrl]] = ...,
        final_mobile_urls : typing.Optional[typing.Iterable[typing.Text]] = ...,
        tracking_url_template : typing.Optional[typing.Text] = ...,
        final_url_suffix : typing.Optional[typing.Text] = ...,
        url_custom_parameters : typing.Optional[typing.Iterable[google.ads.googleads.v8.common.custom_parameter_pb2.CustomParameter]] = ...,
        display_url : typing.Optional[typing.Text] = ...,
        type : google.ads.googleads.v8.enums.ad_type_pb2.AdTypeEnum.AdType.ValueType = ...,
        added_by_google_ads : typing.Optional[builtins.bool] = ...,
        device_preference : google.ads.googleads.v8.enums.device_pb2.DeviceEnum.Device.ValueType = ...,
        url_collections : typing.Optional[typing.Iterable[google.ads.googleads.v8.common.url_collection_pb2.UrlCollection]] = ...,
        name : typing.Optional[typing.Text] = ...,
        system_managed_resource_source : google.ads.googleads.v8.enums.system_managed_entity_source_pb2.SystemManagedResourceSourceEnum.SystemManagedResourceSource.ValueType = ...,
        text_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.TextAdInfo] = ...,
        expanded_text_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.ExpandedTextAdInfo] = ...,
        call_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.CallAdInfo] = ...,
        expanded_dynamic_search_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.ExpandedDynamicSearchAdInfo] = ...,
        hotel_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.HotelAdInfo] = ...,
        shopping_smart_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.ShoppingSmartAdInfo] = ...,
        shopping_product_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.ShoppingProductAdInfo] = ...,
        gmail_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.GmailAdInfo] = ...,
        image_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.ImageAdInfo] = ...,
        video_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.VideoAdInfo] = ...,
        video_responsive_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.VideoResponsiveAdInfo] = ...,
        responsive_search_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.ResponsiveSearchAdInfo] = ...,
        legacy_responsive_display_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.LegacyResponsiveDisplayAdInfo] = ...,
        app_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.AppAdInfo] = ...,
        legacy_app_install_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.LegacyAppInstallAdInfo] = ...,
        responsive_display_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.ResponsiveDisplayAdInfo] = ...,
        local_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.LocalAdInfo] = ...,
        display_upload_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.DisplayUploadAdInfo] = ...,
        app_engagement_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.AppEngagementAdInfo] = ...,
        shopping_comparison_listing_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.ShoppingComparisonListingAdInfo] = ...,
        smart_campaign_ad : typing.Optional[google.ads.googleads.v8.common.ad_type_infos_pb2.SmartCampaignAdInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_added_by_google_ads",b"_added_by_google_ads","_display_url",b"_display_url","_final_url_suffix",b"_final_url_suffix","_id",b"_id","_name",b"_name","_tracking_url_template",b"_tracking_url_template","ad_data",b"ad_data","added_by_google_ads",b"added_by_google_ads","app_ad",b"app_ad","app_engagement_ad",b"app_engagement_ad","call_ad",b"call_ad","display_upload_ad",b"display_upload_ad","display_url",b"display_url","expanded_dynamic_search_ad",b"expanded_dynamic_search_ad","expanded_text_ad",b"expanded_text_ad","final_url_suffix",b"final_url_suffix","gmail_ad",b"gmail_ad","hotel_ad",b"hotel_ad","id",b"id","image_ad",b"image_ad","legacy_app_install_ad",b"legacy_app_install_ad","legacy_responsive_display_ad",b"legacy_responsive_display_ad","local_ad",b"local_ad","name",b"name","responsive_display_ad",b"responsive_display_ad","responsive_search_ad",b"responsive_search_ad","shopping_comparison_listing_ad",b"shopping_comparison_listing_ad","shopping_product_ad",b"shopping_product_ad","shopping_smart_ad",b"shopping_smart_ad","smart_campaign_ad",b"smart_campaign_ad","text_ad",b"text_ad","tracking_url_template",b"tracking_url_template","video_ad",b"video_ad","video_responsive_ad",b"video_responsive_ad"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_added_by_google_ads",b"_added_by_google_ads","_display_url",b"_display_url","_final_url_suffix",b"_final_url_suffix","_id",b"_id","_name",b"_name","_tracking_url_template",b"_tracking_url_template","ad_data",b"ad_data","added_by_google_ads",b"added_by_google_ads","app_ad",b"app_ad","app_engagement_ad",b"app_engagement_ad","call_ad",b"call_ad","device_preference",b"device_preference","display_upload_ad",b"display_upload_ad","display_url",b"display_url","expanded_dynamic_search_ad",b"expanded_dynamic_search_ad","expanded_text_ad",b"expanded_text_ad","final_app_urls",b"final_app_urls","final_mobile_urls",b"final_mobile_urls","final_url_suffix",b"final_url_suffix","final_urls",b"final_urls","gmail_ad",b"gmail_ad","hotel_ad",b"hotel_ad","id",b"id","image_ad",b"image_ad","legacy_app_install_ad",b"legacy_app_install_ad","legacy_responsive_display_ad",b"legacy_responsive_display_ad","local_ad",b"local_ad","name",b"name","resource_name",b"resource_name","responsive_display_ad",b"responsive_display_ad","responsive_search_ad",b"responsive_search_ad","shopping_comparison_listing_ad",b"shopping_comparison_listing_ad","shopping_product_ad",b"shopping_product_ad","shopping_smart_ad",b"shopping_smart_ad","smart_campaign_ad",b"smart_campaign_ad","system_managed_resource_source",b"system_managed_resource_source","text_ad",b"text_ad","tracking_url_template",b"tracking_url_template","type",b"type","url_collections",b"url_collections","url_custom_parameters",b"url_custom_parameters","video_ad",b"video_ad","video_responsive_ad",b"video_responsive_ad"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_added_by_google_ads",b"_added_by_google_ads"]) -> typing.Optional[typing_extensions.Literal["added_by_google_ads"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_display_url",b"_display_url"]) -> typing.Optional[typing_extensions.Literal["display_url"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_final_url_suffix",b"_final_url_suffix"]) -> typing.Optional[typing_extensions.Literal["final_url_suffix"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_tracking_url_template",b"_tracking_url_template"]) -> typing.Optional[typing_extensions.Literal["tracking_url_template"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["ad_data",b"ad_data"]) -> typing.Optional[typing_extensions.Literal["text_ad","expanded_text_ad","call_ad","expanded_dynamic_search_ad","hotel_ad","shopping_smart_ad","shopping_product_ad","gmail_ad","image_ad","video_ad","video_responsive_ad","responsive_search_ad","legacy_responsive_display_ad","app_ad","legacy_app_install_ad","responsive_display_ad","local_ad","display_upload_ad","app_engagement_ad","shopping_comparison_listing_ad","smart_campaign_ad"]]: ...
global___Ad = Ad
