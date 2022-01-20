"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.common.keyword_plan_common_pb2
import google.ads.googleads.v9.enums.keyword_plan_keyword_annotation_pb2
import google.ads.googleads.v9.enums.keyword_plan_network_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GenerateKeywordIdeasRequest(google.protobuf.message.Message):
    """Request message for [KeywordPlanIdeaService.GenerateKeywordIdeas][google.ads.googleads.v9.services.KeywordPlanIdeaService.GenerateKeywordIdeas]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    LANGUAGE_FIELD_NUMBER: builtins.int
    GEO_TARGET_CONSTANTS_FIELD_NUMBER: builtins.int
    INCLUDE_ADULT_KEYWORDS_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    KEYWORD_PLAN_NETWORK_FIELD_NUMBER: builtins.int
    KEYWORD_ANNOTATION_FIELD_NUMBER: builtins.int
    AGGREGATE_METRICS_FIELD_NUMBER: builtins.int
    HISTORICAL_METRICS_OPTIONS_FIELD_NUMBER: builtins.int
    KEYWORD_AND_URL_SEED_FIELD_NUMBER: builtins.int
    KEYWORD_SEED_FIELD_NUMBER: builtins.int
    URL_SEED_FIELD_NUMBER: builtins.int
    SITE_SEED_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """The ID of the customer with the recommendation."""

    language: typing.Text = ...
    """The resource name of the language to target.
    Required
    """

    @property
    def geo_target_constants(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The resource names of the location to target.
        Max 10
        """
        pass
    include_adult_keywords: builtins.bool = ...
    """If true, adult keywords will be included in response.
    The default value is false.
    """

    page_token: typing.Text = ...
    """Token of the page to retrieve. If not specified, the first
    page of results will be returned. To request next page of results use the
    value obtained from `next_page_token` in the previous response.
    The request fields must match across pages.
    """

    page_size: builtins.int = ...
    """Number of results to retrieve in a single page.
    A maximum of 10,000 results may be returned, if the page_size
    exceeds this, it is ignored.
    If unspecified, at most 10,000 results will be returned.
    The server may decide to further limit the number of returned resources.
    If the response contains fewer than 10,000 results it may not be assumed
    as last page of results.
    """

    keyword_plan_network: google.ads.googleads.v9.enums.keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork.ValueType = ...
    """Targeting network."""

    @property
    def keyword_annotation(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[google.ads.googleads.v9.enums.keyword_plan_keyword_annotation_pb2.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation.ValueType]:
        """The keyword annotations to include in response."""
        pass
    @property
    def aggregate_metrics(self) -> google.ads.googleads.v9.common.keyword_plan_common_pb2.KeywordPlanAggregateMetrics:
        """The aggregate fields to include in response."""
        pass
    @property
    def historical_metrics_options(self) -> google.ads.googleads.v9.common.keyword_plan_common_pb2.HistoricalMetricsOptions:
        """The options for historical metrics data."""
        pass
    @property
    def keyword_and_url_seed(self) -> global___KeywordAndUrlSeed:
        """A Keyword and a specific Url to generate ideas from
        e.g. cars, www.example.com/cars.
        """
        pass
    @property
    def keyword_seed(self) -> global___KeywordSeed:
        """A Keyword or phrase to generate ideas from, e.g. cars."""
        pass
    @property
    def url_seed(self) -> global___UrlSeed:
        """A specific url to generate ideas from, e.g. www.example.com/cars."""
        pass
    @property
    def site_seed(self) -> global___SiteSeed:
        """The site to generate ideas from, e.g. www.example.com."""
        pass
    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        language : typing.Optional[typing.Text] = ...,
        geo_target_constants : typing.Optional[typing.Iterable[typing.Text]] = ...,
        include_adult_keywords : builtins.bool = ...,
        page_token : typing.Text = ...,
        page_size : builtins.int = ...,
        keyword_plan_network : google.ads.googleads.v9.enums.keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork.ValueType = ...,
        keyword_annotation : typing.Optional[typing.Iterable[google.ads.googleads.v9.enums.keyword_plan_keyword_annotation_pb2.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation.ValueType]] = ...,
        aggregate_metrics : typing.Optional[google.ads.googleads.v9.common.keyword_plan_common_pb2.KeywordPlanAggregateMetrics] = ...,
        historical_metrics_options : typing.Optional[google.ads.googleads.v9.common.keyword_plan_common_pb2.HistoricalMetricsOptions] = ...,
        keyword_and_url_seed : typing.Optional[global___KeywordAndUrlSeed] = ...,
        keyword_seed : typing.Optional[global___KeywordSeed] = ...,
        url_seed : typing.Optional[global___UrlSeed] = ...,
        site_seed : typing.Optional[global___SiteSeed] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_language",b"_language","aggregate_metrics",b"aggregate_metrics","historical_metrics_options",b"historical_metrics_options","keyword_and_url_seed",b"keyword_and_url_seed","keyword_seed",b"keyword_seed","language",b"language","seed",b"seed","site_seed",b"site_seed","url_seed",b"url_seed"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_language",b"_language","aggregate_metrics",b"aggregate_metrics","customer_id",b"customer_id","geo_target_constants",b"geo_target_constants","historical_metrics_options",b"historical_metrics_options","include_adult_keywords",b"include_adult_keywords","keyword_and_url_seed",b"keyword_and_url_seed","keyword_annotation",b"keyword_annotation","keyword_plan_network",b"keyword_plan_network","keyword_seed",b"keyword_seed","language",b"language","page_size",b"page_size","page_token",b"page_token","seed",b"seed","site_seed",b"site_seed","url_seed",b"url_seed"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_language",b"_language"]) -> typing.Optional[typing_extensions.Literal["language"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["seed",b"seed"]) -> typing.Optional[typing_extensions.Literal["keyword_and_url_seed","keyword_seed","url_seed","site_seed"]]: ...
global___GenerateKeywordIdeasRequest = GenerateKeywordIdeasRequest

class KeywordAndUrlSeed(google.protobuf.message.Message):
    """Keyword And Url Seed"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    URL_FIELD_NUMBER: builtins.int
    KEYWORDS_FIELD_NUMBER: builtins.int
    url: typing.Text = ...
    """The URL to crawl in order to generate keyword ideas."""

    @property
    def keywords(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Requires at least one keyword."""
        pass
    def __init__(self,
        *,
        url : typing.Optional[typing.Text] = ...,
        keywords : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_url",b"_url","url",b"url"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_url",b"_url","keywords",b"keywords","url",b"url"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_url",b"_url"]) -> typing.Optional[typing_extensions.Literal["url"]]: ...
global___KeywordAndUrlSeed = KeywordAndUrlSeed

class KeywordSeed(google.protobuf.message.Message):
    """Keyword Seed"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEYWORDS_FIELD_NUMBER: builtins.int
    @property
    def keywords(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Requires at least one keyword."""
        pass
    def __init__(self,
        *,
        keywords : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keywords",b"keywords"]) -> None: ...
global___KeywordSeed = KeywordSeed

class SiteSeed(google.protobuf.message.Message):
    """Site Seed"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SITE_FIELD_NUMBER: builtins.int
    site: typing.Text = ...
    """The domain name of the site. If the customer requesting the ideas doesn't
    own the site provided only public information is returned.
    """

    def __init__(self,
        *,
        site : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_site",b"_site","site",b"site"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_site",b"_site","site",b"site"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_site",b"_site"]) -> typing.Optional[typing_extensions.Literal["site"]]: ...
global___SiteSeed = SiteSeed

class UrlSeed(google.protobuf.message.Message):
    """Url Seed"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    URL_FIELD_NUMBER: builtins.int
    url: typing.Text = ...
    """The URL to crawl in order to generate keyword ideas."""

    def __init__(self,
        *,
        url : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_url",b"_url","url",b"url"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_url",b"_url","url",b"url"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_url",b"_url"]) -> typing.Optional[typing_extensions.Literal["url"]]: ...
global___UrlSeed = UrlSeed

class GenerateKeywordIdeaResponse(google.protobuf.message.Message):
    """Response message for [KeywordPlanIdeaService.GenerateKeywordIdeas][google.ads.googleads.v9.services.KeywordPlanIdeaService.GenerateKeywordIdeas]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULTS_FIELD_NUMBER: builtins.int
    AGGREGATE_METRIC_RESULTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GenerateKeywordIdeaResult]:
        """Results of generating keyword ideas."""
        pass
    @property
    def aggregate_metric_results(self) -> google.ads.googleads.v9.common.keyword_plan_common_pb2.KeywordPlanAggregateMetricResults:
        """The aggregate metrics for all keyword ideas."""
        pass
    next_page_token: typing.Text = ...
    """Pagination token used to retrieve the next page of results.
    Pass the content of this string as the `page_token` attribute of
    the next request.
    `next_page_token` is not returned for the last page.
    """

    total_size: builtins.int = ...
    """Total number of results available."""

    def __init__(self,
        *,
        results : typing.Optional[typing.Iterable[global___GenerateKeywordIdeaResult]] = ...,
        aggregate_metric_results : typing.Optional[google.ads.googleads.v9.common.keyword_plan_common_pb2.KeywordPlanAggregateMetricResults] = ...,
        next_page_token : typing.Text = ...,
        total_size : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["aggregate_metric_results",b"aggregate_metric_results"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregate_metric_results",b"aggregate_metric_results","next_page_token",b"next_page_token","results",b"results","total_size",b"total_size"]) -> None: ...
global___GenerateKeywordIdeaResponse = GenerateKeywordIdeaResponse

class GenerateKeywordIdeaResult(google.protobuf.message.Message):
    """The result of generating keyword ideas."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TEXT_FIELD_NUMBER: builtins.int
    KEYWORD_IDEA_METRICS_FIELD_NUMBER: builtins.int
    KEYWORD_ANNOTATIONS_FIELD_NUMBER: builtins.int
    text: typing.Text = ...
    """Text of the keyword idea.
    As in Keyword Plan historical metrics, this text may not be an actual
    keyword, but the canonical form of multiple keywords.
    See KeywordPlanKeywordHistoricalMetrics message in KeywordPlanService.
    """

    @property
    def keyword_idea_metrics(self) -> google.ads.googleads.v9.common.keyword_plan_common_pb2.KeywordPlanHistoricalMetrics:
        """The historical metrics for the keyword."""
        pass
    @property
    def keyword_annotations(self) -> google.ads.googleads.v9.common.keyword_plan_common_pb2.KeywordAnnotations:
        """The annotations for the keyword.
        The annotation data is only provided if requested.
        """
        pass
    def __init__(self,
        *,
        text : typing.Optional[typing.Text] = ...,
        keyword_idea_metrics : typing.Optional[google.ads.googleads.v9.common.keyword_plan_common_pb2.KeywordPlanHistoricalMetrics] = ...,
        keyword_annotations : typing.Optional[google.ads.googleads.v9.common.keyword_plan_common_pb2.KeywordAnnotations] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_text",b"_text","keyword_annotations",b"keyword_annotations","keyword_idea_metrics",b"keyword_idea_metrics","text",b"text"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_text",b"_text","keyword_annotations",b"keyword_annotations","keyword_idea_metrics",b"keyword_idea_metrics","text",b"text"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_text",b"_text"]) -> typing.Optional[typing_extensions.Literal["text"]]: ...
global___GenerateKeywordIdeaResult = GenerateKeywordIdeaResult
