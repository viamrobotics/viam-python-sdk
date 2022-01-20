"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.common.asset_types_pb2
import google.ads.googleads.v7.common.custom_parameter_pb2
import google.ads.googleads.v7.common.policy_pb2
import google.ads.googleads.v7.enums.asset_type_pb2
import google.ads.googleads.v7.enums.policy_approval_status_pb2
import google.ads.googleads.v7.enums.policy_review_status_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Asset(google.protobuf.message.Message):
    """Proto file describing the asset resource.

    Asset is a part of an ad which can be shared across multiple ads.
    It can be an image (ImageAsset), a video (YoutubeVideoAsset), etc.
    Assets are immutable and cannot be removed. To stop an asset from serving,
    remove the asset from the entity that is using it.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    FINAL_URLS_FIELD_NUMBER: builtins.int
    FINAL_MOBILE_URLS_FIELD_NUMBER: builtins.int
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: builtins.int
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: builtins.int
    FINAL_URL_SUFFIX_FIELD_NUMBER: builtins.int
    POLICY_SUMMARY_FIELD_NUMBER: builtins.int
    YOUTUBE_VIDEO_ASSET_FIELD_NUMBER: builtins.int
    MEDIA_BUNDLE_ASSET_FIELD_NUMBER: builtins.int
    IMAGE_ASSET_FIELD_NUMBER: builtins.int
    TEXT_ASSET_FIELD_NUMBER: builtins.int
    LEAD_FORM_ASSET_FIELD_NUMBER: builtins.int
    BOOK_ON_GOOGLE_ASSET_FIELD_NUMBER: builtins.int
    PROMOTION_ASSET_FIELD_NUMBER: builtins.int
    CALLOUT_ASSET_FIELD_NUMBER: builtins.int
    STRUCTURED_SNIPPET_ASSET_FIELD_NUMBER: builtins.int
    SITELINK_ASSET_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the asset.
    Asset resource names have the form:

    `customers/{customer_id}/assets/{asset_id}`
    """

    id: builtins.int = ...
    """Output only. The ID of the asset."""

    name: typing.Text = ...
    """Optional name of the asset."""

    type: google.ads.googleads.v7.enums.asset_type_pb2.AssetTypeEnum.AssetType.ValueType = ...
    """Output only. Type of the asset."""

    @property
    def final_urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """A list of possible final URLs after all cross domain redirects."""
        pass
    @property
    def final_mobile_urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """A list of possible final mobile URLs after all cross domain redirects."""
        pass
    tracking_url_template: typing.Text = ...
    """URL template for constructing a tracking URL."""

    @property
    def url_custom_parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.ads.googleads.v7.common.custom_parameter_pb2.CustomParameter]:
        """A list of mappings to be used for substituting URL custom parameter tags in
        the tracking_url_template, final_urls, and/or final_mobile_urls.
        """
        pass
    final_url_suffix: typing.Text = ...
    """URL template for appending params to landing page URLs served with parallel
    tracking.
    """

    @property
    def policy_summary(self) -> global___AssetPolicySummary:
        """Output only. Policy information for the asset."""
        pass
    @property
    def youtube_video_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.YoutubeVideoAsset:
        """Immutable. A YouTube video asset."""
        pass
    @property
    def media_bundle_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.MediaBundleAsset:
        """Immutable. A media bundle asset."""
        pass
    @property
    def image_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.ImageAsset:
        """Output only. An image asset."""
        pass
    @property
    def text_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.TextAsset:
        """Output only. A text asset."""
        pass
    @property
    def lead_form_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.LeadFormAsset:
        """A lead form asset."""
        pass
    @property
    def book_on_google_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.BookOnGoogleAsset:
        """A book on google asset."""
        pass
    @property
    def promotion_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.PromotionAsset:
        """A promotion asset."""
        pass
    @property
    def callout_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.CalloutAsset:
        """A callout asset."""
        pass
    @property
    def structured_snippet_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.StructuredSnippetAsset:
        """A structured snippet asset."""
        pass
    @property
    def sitelink_asset(self) -> google.ads.googleads.v7.common.asset_types_pb2.SitelinkAsset:
        """A sitelink asset."""
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : typing.Optional[builtins.int] = ...,
        name : typing.Optional[typing.Text] = ...,
        type : google.ads.googleads.v7.enums.asset_type_pb2.AssetTypeEnum.AssetType.ValueType = ...,
        final_urls : typing.Optional[typing.Iterable[typing.Text]] = ...,
        final_mobile_urls : typing.Optional[typing.Iterable[typing.Text]] = ...,
        tracking_url_template : typing.Optional[typing.Text] = ...,
        url_custom_parameters : typing.Optional[typing.Iterable[google.ads.googleads.v7.common.custom_parameter_pb2.CustomParameter]] = ...,
        final_url_suffix : typing.Optional[typing.Text] = ...,
        policy_summary : typing.Optional[global___AssetPolicySummary] = ...,
        youtube_video_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.YoutubeVideoAsset] = ...,
        media_bundle_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.MediaBundleAsset] = ...,
        image_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.ImageAsset] = ...,
        text_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.TextAsset] = ...,
        lead_form_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.LeadFormAsset] = ...,
        book_on_google_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.BookOnGoogleAsset] = ...,
        promotion_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.PromotionAsset] = ...,
        callout_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.CalloutAsset] = ...,
        structured_snippet_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.StructuredSnippetAsset] = ...,
        sitelink_asset : typing.Optional[google.ads.googleads.v7.common.asset_types_pb2.SitelinkAsset] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_final_url_suffix",b"_final_url_suffix","_id",b"_id","_name",b"_name","_tracking_url_template",b"_tracking_url_template","asset_data",b"asset_data","book_on_google_asset",b"book_on_google_asset","callout_asset",b"callout_asset","final_url_suffix",b"final_url_suffix","id",b"id","image_asset",b"image_asset","lead_form_asset",b"lead_form_asset","media_bundle_asset",b"media_bundle_asset","name",b"name","policy_summary",b"policy_summary","promotion_asset",b"promotion_asset","sitelink_asset",b"sitelink_asset","structured_snippet_asset",b"structured_snippet_asset","text_asset",b"text_asset","tracking_url_template",b"tracking_url_template","youtube_video_asset",b"youtube_video_asset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_final_url_suffix",b"_final_url_suffix","_id",b"_id","_name",b"_name","_tracking_url_template",b"_tracking_url_template","asset_data",b"asset_data","book_on_google_asset",b"book_on_google_asset","callout_asset",b"callout_asset","final_mobile_urls",b"final_mobile_urls","final_url_suffix",b"final_url_suffix","final_urls",b"final_urls","id",b"id","image_asset",b"image_asset","lead_form_asset",b"lead_form_asset","media_bundle_asset",b"media_bundle_asset","name",b"name","policy_summary",b"policy_summary","promotion_asset",b"promotion_asset","resource_name",b"resource_name","sitelink_asset",b"sitelink_asset","structured_snippet_asset",b"structured_snippet_asset","text_asset",b"text_asset","tracking_url_template",b"tracking_url_template","type",b"type","url_custom_parameters",b"url_custom_parameters","youtube_video_asset",b"youtube_video_asset"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_final_url_suffix",b"_final_url_suffix"]) -> typing.Optional[typing_extensions.Literal["final_url_suffix"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_tracking_url_template",b"_tracking_url_template"]) -> typing.Optional[typing_extensions.Literal["tracking_url_template"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["asset_data",b"asset_data"]) -> typing.Optional[typing_extensions.Literal["youtube_video_asset","media_bundle_asset","image_asset","text_asset","lead_form_asset","book_on_google_asset","promotion_asset","callout_asset","structured_snippet_asset","sitelink_asset"]]: ...
global___Asset = Asset

class AssetPolicySummary(google.protobuf.message.Message):
    """Contains policy information for an asset."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    POLICY_TOPIC_ENTRIES_FIELD_NUMBER: builtins.int
    REVIEW_STATUS_FIELD_NUMBER: builtins.int
    APPROVAL_STATUS_FIELD_NUMBER: builtins.int
    @property
    def policy_topic_entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.ads.googleads.v7.common.policy_pb2.PolicyTopicEntry]:
        """Output only. The list of policy findings for this asset."""
        pass
    review_status: google.ads.googleads.v7.enums.policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus.ValueType = ...
    """Output only. Where in the review process this asset is."""

    approval_status: google.ads.googleads.v7.enums.policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus.ValueType = ...
    """Output only. The overall approval status of this asset, calculated based on the status
    of its individual policy topic entries.
    """

    def __init__(self,
        *,
        policy_topic_entries : typing.Optional[typing.Iterable[google.ads.googleads.v7.common.policy_pb2.PolicyTopicEntry]] = ...,
        review_status : google.ads.googleads.v7.enums.policy_review_status_pb2.PolicyReviewStatusEnum.PolicyReviewStatus.ValueType = ...,
        approval_status : google.ads.googleads.v7.enums.policy_approval_status_pb2.PolicyApprovalStatusEnum.PolicyApprovalStatus.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["approval_status",b"approval_status","policy_topic_entries",b"policy_topic_entries","review_status",b"review_status"]) -> None: ...
global___AssetPolicySummary = AssetPolicySummary
