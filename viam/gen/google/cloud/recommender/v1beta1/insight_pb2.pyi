"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Insight(google.protobuf.message.Message):
    """An insight along with the information used to derive the insight. The insight
    may have associated recomendations as well.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Category:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CategoryEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Category.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        CATEGORY_UNSPECIFIED: Insight.Category.ValueType = ...  # 0
        """Unspecified category."""

        COST: Insight.Category.ValueType = ...  # 1
        """The insight is related to cost."""

        SECURITY: Insight.Category.ValueType = ...  # 2
        """The insight is related to security."""

        PERFORMANCE: Insight.Category.ValueType = ...  # 3
        """The insight is related to performance."""

        MANAGEABILITY: Insight.Category.ValueType = ...  # 4
        """This insight is related to manageability."""

    class Category(_Category, metaclass=_CategoryEnumTypeWrapper):
        """Insight category."""
        pass

    CATEGORY_UNSPECIFIED: Insight.Category.ValueType = ...  # 0
    """Unspecified category."""

    COST: Insight.Category.ValueType = ...  # 1
    """The insight is related to cost."""

    SECURITY: Insight.Category.ValueType = ...  # 2
    """The insight is related to security."""

    PERFORMANCE: Insight.Category.ValueType = ...  # 3
    """The insight is related to performance."""

    MANAGEABILITY: Insight.Category.ValueType = ...  # 4
    """This insight is related to manageability."""


    class _Severity:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SeverityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Severity.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        SEVERITY_UNSPECIFIED: Insight.Severity.ValueType = ...  # 0
        """Insight has unspecified severity."""

        LOW: Insight.Severity.ValueType = ...  # 1
        """Insight has low severity."""

        MEDIUM: Insight.Severity.ValueType = ...  # 2
        """Insight has medium severity."""

        HIGH: Insight.Severity.ValueType = ...  # 3
        """Insight has high severity."""

        CRITICAL: Insight.Severity.ValueType = ...  # 4
        """Insight has critical severity."""

    class Severity(_Severity, metaclass=_SeverityEnumTypeWrapper):
        """Insight severity levels."""
        pass

    SEVERITY_UNSPECIFIED: Insight.Severity.ValueType = ...  # 0
    """Insight has unspecified severity."""

    LOW: Insight.Severity.ValueType = ...  # 1
    """Insight has low severity."""

    MEDIUM: Insight.Severity.ValueType = ...  # 2
    """Insight has medium severity."""

    HIGH: Insight.Severity.ValueType = ...  # 3
    """Insight has high severity."""

    CRITICAL: Insight.Severity.ValueType = ...  # 4
    """Insight has critical severity."""


    class RecommendationReference(google.protobuf.message.Message):
        """Reference to an associated recommendation."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        RECOMMENDATION_FIELD_NUMBER: builtins.int
        recommendation: typing.Text = ...
        """Recommendation resource name, e.g.
        `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/recommendations/[RECOMMENDATION_ID]`
        """

        def __init__(self,
            *,
            recommendation : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["recommendation",b"recommendation"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TARGET_RESOURCES_FIELD_NUMBER: builtins.int
    INSIGHT_SUBTYPE_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    LAST_REFRESH_TIME_FIELD_NUMBER: builtins.int
    OBSERVATION_PERIOD_FIELD_NUMBER: builtins.int
    STATE_INFO_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    SEVERITY_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    ASSOCIATED_RECOMMENDATIONS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the insight."""

    description: typing.Text = ...
    """Free-form human readable summary in English. The maximum length is 500
    characters.
    """

    @property
    def target_resources(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Fully qualified resource names that this insight is targeting."""
        pass
    insight_subtype: typing.Text = ...
    """Insight subtype. Insight content schema will be stable for a given subtype."""

    @property
    def content(self) -> google.protobuf.struct_pb2.Struct:
        """A struct of custom fields to explain the insight.
        Example: "grantedPermissionsCount": "1000"
        """
        pass
    @property
    def last_refresh_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp of the latest data used to generate the insight."""
        pass
    @property
    def observation_period(self) -> google.protobuf.duration_pb2.Duration:
        """Observation period that led to the insight. The source data used to
        generate the insight ends at last_refresh_time and begins at
        (last_refresh_time - observation_period).
        """
        pass
    @property
    def state_info(self) -> global___InsightStateInfo:
        """Information state and metadata."""
        pass
    category: global___Insight.Category.ValueType = ...
    """Category being targeted by the insight."""

    severity: global___Insight.Severity.ValueType = ...
    """Insight's severity."""

    etag: typing.Text = ...
    """Fingerprint of the Insight. Provides optimistic locking when updating
    states.
    """

    @property
    def associated_recommendations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Insight.RecommendationReference]:
        """Recommendations derived from this insight."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        description : typing.Text = ...,
        target_resources : typing.Optional[typing.Iterable[typing.Text]] = ...,
        insight_subtype : typing.Text = ...,
        content : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        last_refresh_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        observation_period : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        state_info : typing.Optional[global___InsightStateInfo] = ...,
        category : global___Insight.Category.ValueType = ...,
        severity : global___Insight.Severity.ValueType = ...,
        etag : typing.Text = ...,
        associated_recommendations : typing.Optional[typing.Iterable[global___Insight.RecommendationReference]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["content",b"content","last_refresh_time",b"last_refresh_time","observation_period",b"observation_period","state_info",b"state_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["associated_recommendations",b"associated_recommendations","category",b"category","content",b"content","description",b"description","etag",b"etag","insight_subtype",b"insight_subtype","last_refresh_time",b"last_refresh_time","name",b"name","observation_period",b"observation_period","severity",b"severity","state_info",b"state_info","target_resources",b"target_resources"]) -> None: ...
global___Insight = Insight

class InsightStateInfo(google.protobuf.message.Message):
    """Information related to insight state."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: InsightStateInfo.State.ValueType = ...  # 0
        """Unspecified state."""

        ACTIVE: InsightStateInfo.State.ValueType = ...  # 1
        """Insight is active. Content for ACTIVE insights can be updated by Google.
        ACTIVE insights can be marked DISMISSED OR ACCEPTED.
        """

        ACCEPTED: InsightStateInfo.State.ValueType = ...  # 2
        """Some action has been taken based on this insight. Insights become
        accepted when a recommendation derived from the insight has been marked
        CLAIMED, SUCCEEDED, or FAILED. ACTIVE insights can also be marked
        ACCEPTED explicitly. Content for ACCEPTED insights is immutable. ACCEPTED
        insights can only be marked ACCEPTED (which may update state metadata).
        """

        DISMISSED: InsightStateInfo.State.ValueType = ...  # 3
        """Insight is dismissed. Content for DISMISSED insights can be updated by
        Google. DISMISSED insights can be marked as ACTIVE.
        """

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Represents insight state."""
        pass

    STATE_UNSPECIFIED: InsightStateInfo.State.ValueType = ...  # 0
    """Unspecified state."""

    ACTIVE: InsightStateInfo.State.ValueType = ...  # 1
    """Insight is active. Content for ACTIVE insights can be updated by Google.
    ACTIVE insights can be marked DISMISSED OR ACCEPTED.
    """

    ACCEPTED: InsightStateInfo.State.ValueType = ...  # 2
    """Some action has been taken based on this insight. Insights become
    accepted when a recommendation derived from the insight has been marked
    CLAIMED, SUCCEEDED, or FAILED. ACTIVE insights can also be marked
    ACCEPTED explicitly. Content for ACCEPTED insights is immutable. ACCEPTED
    insights can only be marked ACCEPTED (which may update state metadata).
    """

    DISMISSED: InsightStateInfo.State.ValueType = ...  # 3
    """Insight is dismissed. Content for DISMISSED insights can be updated by
    Google. DISMISSED insights can be marked as ACTIVE.
    """


    class StateMetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    STATE_FIELD_NUMBER: builtins.int
    STATE_METADATA_FIELD_NUMBER: builtins.int
    state: global___InsightStateInfo.State.ValueType = ...
    """Insight state."""

    @property
    def state_metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """A map of metadata for the state, provided by user or automations systems."""
        pass
    def __init__(self,
        *,
        state : global___InsightStateInfo.State.ValueType = ...,
        state_metadata : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["state",b"state","state_metadata",b"state_metadata"]) -> None: ...
global___InsightStateInfo = InsightStateInfo
