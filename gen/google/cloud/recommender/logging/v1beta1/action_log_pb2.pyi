"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.recommender.v1beta1.insight_pb2
import google.cloud.recommender.v1beta1.recommendation_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ActionLog(google.protobuf.message.Message):
    """Log content of an action on a recommendation. This includes Mark* actions."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
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

    ACTOR_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    STATE_METADATA_FIELD_NUMBER: builtins.int
    RECOMMENDATION_NAME_FIELD_NUMBER: builtins.int
    actor: typing.Text = ...
    """Required. User that executed this action. Eg, foo@gmail.com"""

    state: google.cloud.recommender.v1beta1.recommendation_pb2.RecommendationStateInfo.State.ValueType = ...
    """Required. State change that was made by the actor. Eg, SUCCEEDED."""

    @property
    def state_metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Optional. Metadata that was included with the action that was taken."""
        pass
    recommendation_name: typing.Text = ...
    """Required. Name of the recommendation which was acted on. Eg, :
    'projects/foo/locations/global/recommenders/roleReco/recommendations/r1'
    """

    def __init__(self,
        *,
        actor : typing.Text = ...,
        state : google.cloud.recommender.v1beta1.recommendation_pb2.RecommendationStateInfo.State.ValueType = ...,
        state_metadata : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        recommendation_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["actor",b"actor","recommendation_name",b"recommendation_name","state",b"state","state_metadata",b"state_metadata"]) -> None: ...
global___ActionLog = ActionLog

class InsightActionLog(google.protobuf.message.Message):
    """Log content of an action on an insight. This includes Mark* actions."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
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

    ACTOR_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    STATE_METADATA_FIELD_NUMBER: builtins.int
    INSIGHT_FIELD_NUMBER: builtins.int
    actor: typing.Text = ...
    """Required. User that executed this action. Eg, foo@gmail.com"""

    state: google.cloud.recommender.v1beta1.insight_pb2.InsightStateInfo.State.ValueType = ...
    """Required. State change that was made by the actor. Eg, ACCEPTED."""

    @property
    def state_metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Optional. Metadata that was included with the action that was taken."""
        pass
    insight: typing.Text = ...
    """Required. Name of the insight which was acted on. Eg, :
    'projects/foo/locations/global/insightTypes/roleInsight/insights/i1'
    """

    def __init__(self,
        *,
        actor : typing.Text = ...,
        state : google.cloud.recommender.v1beta1.insight_pb2.InsightStateInfo.State.ValueType = ...,
        state_metadata : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        insight : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["actor",b"actor","insight",b"insight","state",b"state","state_metadata",b"state_metadata"]) -> None: ...
global___InsightActionLog = InsightActionLog
