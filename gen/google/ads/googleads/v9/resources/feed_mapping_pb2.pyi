"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.ad_customizer_placeholder_field_pb2
import google.ads.googleads.v9.enums.affiliate_location_placeholder_field_pb2
import google.ads.googleads.v9.enums.app_placeholder_field_pb2
import google.ads.googleads.v9.enums.call_placeholder_field_pb2
import google.ads.googleads.v9.enums.callout_placeholder_field_pb2
import google.ads.googleads.v9.enums.custom_placeholder_field_pb2
import google.ads.googleads.v9.enums.dsa_page_feed_criterion_field_pb2
import google.ads.googleads.v9.enums.education_placeholder_field_pb2
import google.ads.googleads.v9.enums.feed_mapping_criterion_type_pb2
import google.ads.googleads.v9.enums.feed_mapping_status_pb2
import google.ads.googleads.v9.enums.flight_placeholder_field_pb2
import google.ads.googleads.v9.enums.hotel_placeholder_field_pb2
import google.ads.googleads.v9.enums.image_placeholder_field_pb2
import google.ads.googleads.v9.enums.job_placeholder_field_pb2
import google.ads.googleads.v9.enums.local_placeholder_field_pb2
import google.ads.googleads.v9.enums.location_extension_targeting_criterion_field_pb2
import google.ads.googleads.v9.enums.location_placeholder_field_pb2
import google.ads.googleads.v9.enums.message_placeholder_field_pb2
import google.ads.googleads.v9.enums.placeholder_type_pb2
import google.ads.googleads.v9.enums.price_placeholder_field_pb2
import google.ads.googleads.v9.enums.promotion_placeholder_field_pb2
import google.ads.googleads.v9.enums.real_estate_placeholder_field_pb2
import google.ads.googleads.v9.enums.sitelink_placeholder_field_pb2
import google.ads.googleads.v9.enums.structured_snippet_placeholder_field_pb2
import google.ads.googleads.v9.enums.travel_placeholder_field_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FeedMapping(google.protobuf.message.Message):
    """Proto file describing the FeedMapping resource.

    A feed mapping.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    FEED_FIELD_NUMBER: builtins.int
    ATTRIBUTE_FIELD_MAPPINGS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PLACEHOLDER_TYPE_FIELD_NUMBER: builtins.int
    CRITERION_TYPE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the feed mapping.
    Feed mapping resource names have the form:

    `customers/{customer_id}/feedMappings/{feed_id}~{feed_mapping_id}`
    """

    feed: typing.Text = ...
    """Immutable. The feed of this feed mapping."""

    @property
    def attribute_field_mappings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AttributeFieldMapping]:
        """Immutable. Feed attributes to field mappings. These mappings are a one-to-many
        relationship meaning that 1 feed attribute can be used to populate
        multiple placeholder fields, but 1 placeholder field can only draw
        data from 1 feed attribute. Ad Customizer is an exception, 1 placeholder
        field can be mapped to multiple feed attributes. Required.
        """
        pass
    status: google.ads.googleads.v9.enums.feed_mapping_status_pb2.FeedMappingStatusEnum.FeedMappingStatus.ValueType = ...
    """Output only. Status of the feed mapping.
    This field is read-only.
    """

    placeholder_type: google.ads.googleads.v9.enums.placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType.ValueType = ...
    """Immutable. The placeholder type of this mapping (i.e., if the mapping maps feed
    attributes to placeholder fields).
    """

    criterion_type: google.ads.googleads.v9.enums.feed_mapping_criterion_type_pb2.FeedMappingCriterionTypeEnum.FeedMappingCriterionType.ValueType = ...
    """Immutable. The criterion type of this mapping (i.e., if the mapping maps feed
    attributes to criterion fields).
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        feed : typing.Optional[typing.Text] = ...,
        attribute_field_mappings : typing.Optional[typing.Iterable[global___AttributeFieldMapping]] = ...,
        status : google.ads.googleads.v9.enums.feed_mapping_status_pb2.FeedMappingStatusEnum.FeedMappingStatus.ValueType = ...,
        placeholder_type : google.ads.googleads.v9.enums.placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType.ValueType = ...,
        criterion_type : google.ads.googleads.v9.enums.feed_mapping_criterion_type_pb2.FeedMappingCriterionTypeEnum.FeedMappingCriterionType.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_feed",b"_feed","criterion_type",b"criterion_type","feed",b"feed","placeholder_type",b"placeholder_type","target",b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_feed",b"_feed","attribute_field_mappings",b"attribute_field_mappings","criterion_type",b"criterion_type","feed",b"feed","placeholder_type",b"placeholder_type","resource_name",b"resource_name","status",b"status","target",b"target"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_feed",b"_feed"]) -> typing.Optional[typing_extensions.Literal["feed"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["target",b"target"]) -> typing.Optional[typing_extensions.Literal["placeholder_type","criterion_type"]]: ...
global___FeedMapping = FeedMapping

class AttributeFieldMapping(google.protobuf.message.Message):
    """Maps from feed attribute id to a placeholder or criterion field id."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FEED_ATTRIBUTE_ID_FIELD_NUMBER: builtins.int
    FIELD_ID_FIELD_NUMBER: builtins.int
    SITELINK_FIELD_FIELD_NUMBER: builtins.int
    CALL_FIELD_FIELD_NUMBER: builtins.int
    APP_FIELD_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_FIELD_NUMBER: builtins.int
    AFFILIATE_LOCATION_FIELD_FIELD_NUMBER: builtins.int
    CALLOUT_FIELD_FIELD_NUMBER: builtins.int
    STRUCTURED_SNIPPET_FIELD_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_FIELD_NUMBER: builtins.int
    PRICE_FIELD_FIELD_NUMBER: builtins.int
    PROMOTION_FIELD_FIELD_NUMBER: builtins.int
    AD_CUSTOMIZER_FIELD_FIELD_NUMBER: builtins.int
    DSA_PAGE_FEED_FIELD_FIELD_NUMBER: builtins.int
    LOCATION_EXTENSION_TARGETING_FIELD_FIELD_NUMBER: builtins.int
    EDUCATION_FIELD_FIELD_NUMBER: builtins.int
    FLIGHT_FIELD_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_FIELD_NUMBER: builtins.int
    HOTEL_FIELD_FIELD_NUMBER: builtins.int
    REAL_ESTATE_FIELD_FIELD_NUMBER: builtins.int
    TRAVEL_FIELD_FIELD_NUMBER: builtins.int
    LOCAL_FIELD_FIELD_NUMBER: builtins.int
    JOB_FIELD_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_FIELD_NUMBER: builtins.int
    feed_attribute_id: builtins.int = ...
    """Immutable. Feed attribute from which to map."""

    field_id: builtins.int = ...
    """Output only. The placeholder field ID. If a placeholder field enum is not published in
    the current API version, then this field will be populated and the field
    oneof will be empty.
    This field is read-only.
    """

    sitelink_field: google.ads.googleads.v9.enums.sitelink_placeholder_field_pb2.SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.ValueType = ...
    """Immutable. Sitelink Placeholder Fields."""

    call_field: google.ads.googleads.v9.enums.call_placeholder_field_pb2.CallPlaceholderFieldEnum.CallPlaceholderField.ValueType = ...
    """Immutable. Call Placeholder Fields."""

    app_field: google.ads.googleads.v9.enums.app_placeholder_field_pb2.AppPlaceholderFieldEnum.AppPlaceholderField.ValueType = ...
    """Immutable. App Placeholder Fields."""

    location_field: google.ads.googleads.v9.enums.location_placeholder_field_pb2.LocationPlaceholderFieldEnum.LocationPlaceholderField.ValueType = ...
    """Output only. Location Placeholder Fields. This field is read-only."""

    affiliate_location_field: google.ads.googleads.v9.enums.affiliate_location_placeholder_field_pb2.AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField.ValueType = ...
    """Output only. Affiliate Location Placeholder Fields. This field is read-only."""

    callout_field: google.ads.googleads.v9.enums.callout_placeholder_field_pb2.CalloutPlaceholderFieldEnum.CalloutPlaceholderField.ValueType = ...
    """Immutable. Callout Placeholder Fields."""

    structured_snippet_field: google.ads.googleads.v9.enums.structured_snippet_placeholder_field_pb2.StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.ValueType = ...
    """Immutable. Structured Snippet Placeholder Fields."""

    message_field: google.ads.googleads.v9.enums.message_placeholder_field_pb2.MessagePlaceholderFieldEnum.MessagePlaceholderField.ValueType = ...
    """Immutable. Message Placeholder Fields."""

    price_field: google.ads.googleads.v9.enums.price_placeholder_field_pb2.PricePlaceholderFieldEnum.PricePlaceholderField.ValueType = ...
    """Immutable. Price Placeholder Fields."""

    promotion_field: google.ads.googleads.v9.enums.promotion_placeholder_field_pb2.PromotionPlaceholderFieldEnum.PromotionPlaceholderField.ValueType = ...
    """Immutable. Promotion Placeholder Fields."""

    ad_customizer_field: google.ads.googleads.v9.enums.ad_customizer_placeholder_field_pb2.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...
    """Immutable. Ad Customizer Placeholder Fields"""

    dsa_page_feed_field: google.ads.googleads.v9.enums.dsa_page_feed_criterion_field_pb2.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.ValueType = ...
    """Immutable. Dynamic Search Ad Page Feed Fields."""

    location_extension_targeting_field: google.ads.googleads.v9.enums.location_extension_targeting_criterion_field_pb2.LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField.ValueType = ...
    """Immutable. Location Target Fields."""

    education_field: google.ads.googleads.v9.enums.education_placeholder_field_pb2.EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...
    """Immutable. Education Placeholder Fields"""

    flight_field: google.ads.googleads.v9.enums.flight_placeholder_field_pb2.FlightPlaceholderFieldEnum.FlightPlaceholderField.ValueType = ...
    """Immutable. Flight Placeholder Fields"""

    custom_field: google.ads.googleads.v9.enums.custom_placeholder_field_pb2.CustomPlaceholderFieldEnum.CustomPlaceholderField.ValueType = ...
    """Immutable. Custom Placeholder Fields"""

    hotel_field: google.ads.googleads.v9.enums.hotel_placeholder_field_pb2.HotelPlaceholderFieldEnum.HotelPlaceholderField.ValueType = ...
    """Immutable. Hotel Placeholder Fields"""

    real_estate_field: google.ads.googleads.v9.enums.real_estate_placeholder_field_pb2.RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField.ValueType = ...
    """Immutable. Real Estate Placeholder Fields"""

    travel_field: google.ads.googleads.v9.enums.travel_placeholder_field_pb2.TravelPlaceholderFieldEnum.TravelPlaceholderField.ValueType = ...
    """Immutable. Travel Placeholder Fields"""

    local_field: google.ads.googleads.v9.enums.local_placeholder_field_pb2.LocalPlaceholderFieldEnum.LocalPlaceholderField.ValueType = ...
    """Immutable. Local Placeholder Fields"""

    job_field: google.ads.googleads.v9.enums.job_placeholder_field_pb2.JobPlaceholderFieldEnum.JobPlaceholderField.ValueType = ...
    """Immutable. Job Placeholder Fields"""

    image_field: google.ads.googleads.v9.enums.image_placeholder_field_pb2.ImagePlaceholderFieldEnum.ImagePlaceholderField.ValueType = ...
    """Immutable. Image Placeholder Fields"""

    def __init__(self,
        *,
        feed_attribute_id : typing.Optional[builtins.int] = ...,
        field_id : typing.Optional[builtins.int] = ...,
        sitelink_field : google.ads.googleads.v9.enums.sitelink_placeholder_field_pb2.SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.ValueType = ...,
        call_field : google.ads.googleads.v9.enums.call_placeholder_field_pb2.CallPlaceholderFieldEnum.CallPlaceholderField.ValueType = ...,
        app_field : google.ads.googleads.v9.enums.app_placeholder_field_pb2.AppPlaceholderFieldEnum.AppPlaceholderField.ValueType = ...,
        location_field : google.ads.googleads.v9.enums.location_placeholder_field_pb2.LocationPlaceholderFieldEnum.LocationPlaceholderField.ValueType = ...,
        affiliate_location_field : google.ads.googleads.v9.enums.affiliate_location_placeholder_field_pb2.AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField.ValueType = ...,
        callout_field : google.ads.googleads.v9.enums.callout_placeholder_field_pb2.CalloutPlaceholderFieldEnum.CalloutPlaceholderField.ValueType = ...,
        structured_snippet_field : google.ads.googleads.v9.enums.structured_snippet_placeholder_field_pb2.StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.ValueType = ...,
        message_field : google.ads.googleads.v9.enums.message_placeholder_field_pb2.MessagePlaceholderFieldEnum.MessagePlaceholderField.ValueType = ...,
        price_field : google.ads.googleads.v9.enums.price_placeholder_field_pb2.PricePlaceholderFieldEnum.PricePlaceholderField.ValueType = ...,
        promotion_field : google.ads.googleads.v9.enums.promotion_placeholder_field_pb2.PromotionPlaceholderFieldEnum.PromotionPlaceholderField.ValueType = ...,
        ad_customizer_field : google.ads.googleads.v9.enums.ad_customizer_placeholder_field_pb2.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...,
        dsa_page_feed_field : google.ads.googleads.v9.enums.dsa_page_feed_criterion_field_pb2.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.ValueType = ...,
        location_extension_targeting_field : google.ads.googleads.v9.enums.location_extension_targeting_criterion_field_pb2.LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField.ValueType = ...,
        education_field : google.ads.googleads.v9.enums.education_placeholder_field_pb2.EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...,
        flight_field : google.ads.googleads.v9.enums.flight_placeholder_field_pb2.FlightPlaceholderFieldEnum.FlightPlaceholderField.ValueType = ...,
        custom_field : google.ads.googleads.v9.enums.custom_placeholder_field_pb2.CustomPlaceholderFieldEnum.CustomPlaceholderField.ValueType = ...,
        hotel_field : google.ads.googleads.v9.enums.hotel_placeholder_field_pb2.HotelPlaceholderFieldEnum.HotelPlaceholderField.ValueType = ...,
        real_estate_field : google.ads.googleads.v9.enums.real_estate_placeholder_field_pb2.RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField.ValueType = ...,
        travel_field : google.ads.googleads.v9.enums.travel_placeholder_field_pb2.TravelPlaceholderFieldEnum.TravelPlaceholderField.ValueType = ...,
        local_field : google.ads.googleads.v9.enums.local_placeholder_field_pb2.LocalPlaceholderFieldEnum.LocalPlaceholderField.ValueType = ...,
        job_field : google.ads.googleads.v9.enums.job_placeholder_field_pb2.JobPlaceholderFieldEnum.JobPlaceholderField.ValueType = ...,
        image_field : google.ads.googleads.v9.enums.image_placeholder_field_pb2.ImagePlaceholderFieldEnum.ImagePlaceholderField.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_feed_attribute_id",b"_feed_attribute_id","_field_id",b"_field_id","ad_customizer_field",b"ad_customizer_field","affiliate_location_field",b"affiliate_location_field","app_field",b"app_field","call_field",b"call_field","callout_field",b"callout_field","custom_field",b"custom_field","dsa_page_feed_field",b"dsa_page_feed_field","education_field",b"education_field","feed_attribute_id",b"feed_attribute_id","field",b"field","field_id",b"field_id","flight_field",b"flight_field","hotel_field",b"hotel_field","image_field",b"image_field","job_field",b"job_field","local_field",b"local_field","location_extension_targeting_field",b"location_extension_targeting_field","location_field",b"location_field","message_field",b"message_field","price_field",b"price_field","promotion_field",b"promotion_field","real_estate_field",b"real_estate_field","sitelink_field",b"sitelink_field","structured_snippet_field",b"structured_snippet_field","travel_field",b"travel_field"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_feed_attribute_id",b"_feed_attribute_id","_field_id",b"_field_id","ad_customizer_field",b"ad_customizer_field","affiliate_location_field",b"affiliate_location_field","app_field",b"app_field","call_field",b"call_field","callout_field",b"callout_field","custom_field",b"custom_field","dsa_page_feed_field",b"dsa_page_feed_field","education_field",b"education_field","feed_attribute_id",b"feed_attribute_id","field",b"field","field_id",b"field_id","flight_field",b"flight_field","hotel_field",b"hotel_field","image_field",b"image_field","job_field",b"job_field","local_field",b"local_field","location_extension_targeting_field",b"location_extension_targeting_field","location_field",b"location_field","message_field",b"message_field","price_field",b"price_field","promotion_field",b"promotion_field","real_estate_field",b"real_estate_field","sitelink_field",b"sitelink_field","structured_snippet_field",b"structured_snippet_field","travel_field",b"travel_field"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_feed_attribute_id",b"_feed_attribute_id"]) -> typing.Optional[typing_extensions.Literal["feed_attribute_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_field_id",b"_field_id"]) -> typing.Optional[typing_extensions.Literal["field_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["field",b"field"]) -> typing.Optional[typing_extensions.Literal["sitelink_field","call_field","app_field","location_field","affiliate_location_field","callout_field","structured_snippet_field","message_field","price_field","promotion_field","ad_customizer_field","dsa_page_feed_field","location_extension_targeting_field","education_field","flight_field","custom_field","hotel_field","real_estate_field","travel_field","local_field","job_field","image_field"]]: ...
global___AttributeFieldMapping = AttributeFieldMapping
