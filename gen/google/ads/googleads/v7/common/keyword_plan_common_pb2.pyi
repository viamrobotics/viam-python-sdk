"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.common.dates_pb2
import google.ads.googleads.v7.enums.device_pb2
import google.ads.googleads.v7.enums.keyword_plan_aggregate_metric_type_pb2
import google.ads.googleads.v7.enums.keyword_plan_competition_level_pb2
import google.ads.googleads.v7.enums.keyword_plan_concept_group_type_pb2
import google.ads.googleads.v7.enums.month_of_year_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class KeywordPlanHistoricalMetrics(google.protobuf.message.Message):
    """Proto file describing Keyword Planner messages.

    Historical metrics specific to the targeting options selected.
    Targeting options include geographies, network, etc.
    Refer to https://support.google.com/google-ads/answer/3022575 for more
    details.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AVG_MONTHLY_SEARCHES_FIELD_NUMBER: builtins.int
    MONTHLY_SEARCH_VOLUMES_FIELD_NUMBER: builtins.int
    COMPETITION_FIELD_NUMBER: builtins.int
    COMPETITION_INDEX_FIELD_NUMBER: builtins.int
    LOW_TOP_OF_PAGE_BID_MICROS_FIELD_NUMBER: builtins.int
    HIGH_TOP_OF_PAGE_BID_MICROS_FIELD_NUMBER: builtins.int
    avg_monthly_searches: builtins.int = ...
    """Approximate number of monthly searches on this query averaged
    for the past 12 months.
    """

    @property
    def monthly_search_volumes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MonthlySearchVolume]:
        """Approximate number of searches on this query for the past twelve months."""
        pass
    competition: google.ads.googleads.v7.enums.keyword_plan_competition_level_pb2.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel.ValueType = ...
    """The competition level for the query."""

    competition_index: builtins.int = ...
    """The competition index for the query in the range [0, 100].
    Shows how competitive ad placement is for a keyword.
    The level of competition from 0-100 is determined by the number of ad slots
    filled divided by the total number of ad slots available. If not enough
    data is available, null is returned.
    """

    low_top_of_page_bid_micros: builtins.int = ...
    """Top of page bid low range (20th percentile) in micros for the keyword."""

    high_top_of_page_bid_micros: builtins.int = ...
    """Top of page bid high range (80th percentile) in micros for the keyword."""

    def __init__(self,
        *,
        avg_monthly_searches : typing.Optional[builtins.int] = ...,
        monthly_search_volumes : typing.Optional[typing.Iterable[global___MonthlySearchVolume]] = ...,
        competition : google.ads.googleads.v7.enums.keyword_plan_competition_level_pb2.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel.ValueType = ...,
        competition_index : typing.Optional[builtins.int] = ...,
        low_top_of_page_bid_micros : typing.Optional[builtins.int] = ...,
        high_top_of_page_bid_micros : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_avg_monthly_searches",b"_avg_monthly_searches","_competition_index",b"_competition_index","_high_top_of_page_bid_micros",b"_high_top_of_page_bid_micros","_low_top_of_page_bid_micros",b"_low_top_of_page_bid_micros","avg_monthly_searches",b"avg_monthly_searches","competition_index",b"competition_index","high_top_of_page_bid_micros",b"high_top_of_page_bid_micros","low_top_of_page_bid_micros",b"low_top_of_page_bid_micros"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_avg_monthly_searches",b"_avg_monthly_searches","_competition_index",b"_competition_index","_high_top_of_page_bid_micros",b"_high_top_of_page_bid_micros","_low_top_of_page_bid_micros",b"_low_top_of_page_bid_micros","avg_monthly_searches",b"avg_monthly_searches","competition",b"competition","competition_index",b"competition_index","high_top_of_page_bid_micros",b"high_top_of_page_bid_micros","low_top_of_page_bid_micros",b"low_top_of_page_bid_micros","monthly_search_volumes",b"monthly_search_volumes"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_avg_monthly_searches",b"_avg_monthly_searches"]) -> typing.Optional[typing_extensions.Literal["avg_monthly_searches"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_competition_index",b"_competition_index"]) -> typing.Optional[typing_extensions.Literal["competition_index"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_high_top_of_page_bid_micros",b"_high_top_of_page_bid_micros"]) -> typing.Optional[typing_extensions.Literal["high_top_of_page_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_low_top_of_page_bid_micros",b"_low_top_of_page_bid_micros"]) -> typing.Optional[typing_extensions.Literal["low_top_of_page_bid_micros"]]: ...
global___KeywordPlanHistoricalMetrics = KeywordPlanHistoricalMetrics

class HistoricalMetricsOptions(google.protobuf.message.Message):
    """Historical metrics options."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    YEAR_MONTH_RANGE_FIELD_NUMBER: builtins.int
    @property
    def year_month_range(self) -> google.ads.googleads.v7.common.dates_pb2.YearMonthRange:
        """The year month range for historical metrics. If not specified the searches
        will be returned for past 12 months.
        Searches data is available for the past 4 years. If the search volume is
        not available for the entire year_month_range provided, the subset of the
        year month range for which search volume is available will be returned.
        """
        pass
    def __init__(self,
        *,
        year_month_range : typing.Optional[google.ads.googleads.v7.common.dates_pb2.YearMonthRange] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_year_month_range",b"_year_month_range","year_month_range",b"year_month_range"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_year_month_range",b"_year_month_range","year_month_range",b"year_month_range"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_year_month_range",b"_year_month_range"]) -> typing.Optional[typing_extensions.Literal["year_month_range"]]: ...
global___HistoricalMetricsOptions = HistoricalMetricsOptions

class MonthlySearchVolume(google.protobuf.message.Message):
    """Monthly search volume."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    YEAR_FIELD_NUMBER: builtins.int
    MONTH_FIELD_NUMBER: builtins.int
    MONTHLY_SEARCHES_FIELD_NUMBER: builtins.int
    year: builtins.int = ...
    """The year of the search volume (e.g. 2020)."""

    month: google.ads.googleads.v7.enums.month_of_year_pb2.MonthOfYearEnum.MonthOfYear.ValueType = ...
    """The month of the search volume."""

    monthly_searches: builtins.int = ...
    """Approximate number of searches for the month.
    A null value indicates the search volume is unavailable for
    that month.
    """

    def __init__(self,
        *,
        year : typing.Optional[builtins.int] = ...,
        month : google.ads.googleads.v7.enums.month_of_year_pb2.MonthOfYearEnum.MonthOfYear.ValueType = ...,
        monthly_searches : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_monthly_searches",b"_monthly_searches","_year",b"_year","monthly_searches",b"monthly_searches","year",b"year"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_monthly_searches",b"_monthly_searches","_year",b"_year","month",b"month","monthly_searches",b"monthly_searches","year",b"year"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_monthly_searches",b"_monthly_searches"]) -> typing.Optional[typing_extensions.Literal["monthly_searches"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_year",b"_year"]) -> typing.Optional[typing_extensions.Literal["year"]]: ...
global___MonthlySearchVolume = MonthlySearchVolume

class KeywordPlanAggregateMetrics(google.protobuf.message.Message):
    """The aggregate metrics specification of the request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AGGREGATE_METRIC_TYPES_FIELD_NUMBER: builtins.int
    @property
    def aggregate_metric_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[google.ads.googleads.v7.enums.keyword_plan_aggregate_metric_type_pb2.KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType.ValueType]:
        """The list of aggregate metrics to fetch data."""
        pass
    def __init__(self,
        *,
        aggregate_metric_types : typing.Optional[typing.Iterable[google.ads.googleads.v7.enums.keyword_plan_aggregate_metric_type_pb2.KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType.ValueType]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregate_metric_types",b"aggregate_metric_types"]) -> None: ...
global___KeywordPlanAggregateMetrics = KeywordPlanAggregateMetrics

class KeywordPlanAggregateMetricResults(google.protobuf.message.Message):
    """The aggregated historical metrics for keyword plan keywords."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_SEARCHES_FIELD_NUMBER: builtins.int
    @property
    def device_searches(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeywordPlanDeviceSearches]:
        """The aggregate searches for all the keywords segmented by device
        for the specified time.
        Supports the following device types: MOBILE, TABLET, DESKTOP.

        This is only set when KeywordPlanAggregateMetricTypeEnum.DEVICE is set
        in the KeywordPlanAggregateMetrics field in the request.
        """
        pass
    def __init__(self,
        *,
        device_searches : typing.Optional[typing.Iterable[global___KeywordPlanDeviceSearches]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["device_searches",b"device_searches"]) -> None: ...
global___KeywordPlanAggregateMetricResults = KeywordPlanAggregateMetricResults

class KeywordPlanDeviceSearches(google.protobuf.message.Message):
    """The total searches for the device type during the specified time period."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_FIELD_NUMBER: builtins.int
    SEARCH_COUNT_FIELD_NUMBER: builtins.int
    device: google.ads.googleads.v7.enums.device_pb2.DeviceEnum.Device.ValueType = ...
    """The device type."""

    search_count: builtins.int = ...
    """The total searches for the device."""

    def __init__(self,
        *,
        device : google.ads.googleads.v7.enums.device_pb2.DeviceEnum.Device.ValueType = ...,
        search_count : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_search_count",b"_search_count","search_count",b"search_count"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_search_count",b"_search_count","device",b"device","search_count",b"search_count"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_search_count",b"_search_count"]) -> typing.Optional[typing_extensions.Literal["search_count"]]: ...
global___KeywordPlanDeviceSearches = KeywordPlanDeviceSearches

class KeywordAnnotations(google.protobuf.message.Message):
    """The Annotations for the Keyword plan keywords."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONCEPTS_FIELD_NUMBER: builtins.int
    @property
    def concepts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeywordConcept]:
        """The list of concepts for the keyword."""
        pass
    def __init__(self,
        *,
        concepts : typing.Optional[typing.Iterable[global___KeywordConcept]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["concepts",b"concepts"]) -> None: ...
global___KeywordAnnotations = KeywordAnnotations

class KeywordConcept(google.protobuf.message.Message):
    """The concept for the keyword."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    CONCEPT_GROUP_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The concept name for the keyword in the concept_group."""

    @property
    def concept_group(self) -> global___ConceptGroup:
        """The concept group of the concept details."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        concept_group : typing.Optional[global___ConceptGroup] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["concept_group",b"concept_group"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["concept_group",b"concept_group","name",b"name"]) -> None: ...
global___KeywordConcept = KeywordConcept

class ConceptGroup(google.protobuf.message.Message):
    """The concept group for the keyword concept."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The concept group name."""

    type: google.ads.googleads.v7.enums.keyword_plan_concept_group_type_pb2.KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType.ValueType = ...
    """The concept group type."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        type : google.ads.googleads.v7.enums.keyword_plan_concept_group_type_pb2.KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","type",b"type"]) -> None: ...
global___ConceptGroup = ConceptGroup
