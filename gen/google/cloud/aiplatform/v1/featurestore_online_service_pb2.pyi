"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.aiplatform.v1.feature_selector_pb2
import google.cloud.aiplatform.v1.types_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ReadFeatureValuesRequest(google.protobuf.message.Message):
    """Request message for [FeaturestoreOnlineServingService.ReadFeatureValues][google.cloud.aiplatform.v1.FeaturestoreOnlineServingService.ReadFeatureValues]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    ENTITY_ID_FIELD_NUMBER: builtins.int
    FEATURE_SELECTOR_FIELD_NUMBER: builtins.int
    entity_type: typing.Text = ...
    """Required. The resource name of the EntityType for the entity being read.
    Value format:
    `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`.
    For example, for a machine learning model predicting user clicks on a
    website, an EntityType ID could be `user`.
    """

    entity_id: typing.Text = ...
    """Required. ID for a specific entity. For example,
    for a machine learning model predicting user clicks on a website, an entity
    ID could be `user_123`.
    """

    @property
    def feature_selector(self) -> google.cloud.aiplatform.v1.feature_selector_pb2.FeatureSelector:
        """Required. Selector choosing Features of the target EntityType."""
        pass
    def __init__(self,
        *,
        entity_type : typing.Text = ...,
        entity_id : typing.Text = ...,
        feature_selector : typing.Optional[google.cloud.aiplatform.v1.feature_selector_pb2.FeatureSelector] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["feature_selector",b"feature_selector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_id",b"entity_id","entity_type",b"entity_type","feature_selector",b"feature_selector"]) -> None: ...
global___ReadFeatureValuesRequest = ReadFeatureValuesRequest

class ReadFeatureValuesResponse(google.protobuf.message.Message):
    """Response message for [FeaturestoreOnlineServingService.ReadFeatureValues][google.cloud.aiplatform.v1.FeaturestoreOnlineServingService.ReadFeatureValues]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class FeatureDescriptor(google.protobuf.message.Message):
        """Metadata for requested Features."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ID_FIELD_NUMBER: builtins.int
        id: typing.Text = ...
        """Feature ID."""

        def __init__(self,
            *,
            id : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...

    class Header(google.protobuf.message.Message):
        """Response header with metadata for the requested
        [ReadFeatureValuesRequest.entity_type][google.cloud.aiplatform.v1.ReadFeatureValuesRequest.entity_type] and Features.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ENTITY_TYPE_FIELD_NUMBER: builtins.int
        FEATURE_DESCRIPTORS_FIELD_NUMBER: builtins.int
        entity_type: typing.Text = ...
        """The resource name of the EntityType from the
        [ReadFeatureValuesRequest][google.cloud.aiplatform.v1.ReadFeatureValuesRequest]. Value format:
        `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`.
        """

        @property
        def feature_descriptors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ReadFeatureValuesResponse.FeatureDescriptor]:
            """List of Feature metadata corresponding to each piece of
            [ReadFeatureValuesResponse.data][].
            """
            pass
        def __init__(self,
            *,
            entity_type : typing.Text = ...,
            feature_descriptors : typing.Optional[typing.Iterable[global___ReadFeatureValuesResponse.FeatureDescriptor]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["entity_type",b"entity_type","feature_descriptors",b"feature_descriptors"]) -> None: ...

    class EntityView(google.protobuf.message.Message):
        """Entity view with Feature values."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class Data(google.protobuf.message.Message):
            """Container to hold value(s), successive in time, for one Feature from the
            request.
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            VALUE_FIELD_NUMBER: builtins.int
            VALUES_FIELD_NUMBER: builtins.int
            @property
            def value(self) -> global___FeatureValue:
                """Feature value if a single value is requested."""
                pass
            @property
            def values(self) -> global___FeatureValueList:
                """Feature values list if values, successive in time, are requested.
                If the requested number of values is greater than the number of
                existing Feature values, nonexistent values are omitted instead of
                being returned as empty.
                """
                pass
            def __init__(self,
                *,
                value : typing.Optional[global___FeatureValue] = ...,
                values : typing.Optional[global___FeatureValueList] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["data",b"data","value",b"value","values",b"values"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["data",b"data","value",b"value","values",b"values"]) -> None: ...
            def WhichOneof(self, oneof_group: typing_extensions.Literal["data",b"data"]) -> typing.Optional[typing_extensions.Literal["value","values"]]: ...

        ENTITY_ID_FIELD_NUMBER: builtins.int
        DATA_FIELD_NUMBER: builtins.int
        entity_id: typing.Text = ...
        """ID of the requested entity."""

        @property
        def data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ReadFeatureValuesResponse.EntityView.Data]:
            """Each piece of data holds the k
            requested values for one requested Feature. If no values
            for the requested Feature exist, the corresponding cell will be empty.
            This has the same size and is in the same order as the features from the
            header [ReadFeatureValuesResponse.header][google.cloud.aiplatform.v1.ReadFeatureValuesResponse.header].
            """
            pass
        def __init__(self,
            *,
            entity_id : typing.Text = ...,
            data : typing.Optional[typing.Iterable[global___ReadFeatureValuesResponse.EntityView.Data]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["data",b"data","entity_id",b"entity_id"]) -> None: ...

    HEADER_FIELD_NUMBER: builtins.int
    ENTITY_VIEW_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___ReadFeatureValuesResponse.Header:
        """Response header."""
        pass
    @property
    def entity_view(self) -> global___ReadFeatureValuesResponse.EntityView:
        """Entity view with Feature values. This may be the entity in the
        Featurestore if values for all Features were requested, or a projection
        of the entity in the Featurestore if values for only some Features were
        requested.
        """
        pass
    def __init__(self,
        *,
        header : typing.Optional[global___ReadFeatureValuesResponse.Header] = ...,
        entity_view : typing.Optional[global___ReadFeatureValuesResponse.EntityView] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity_view",b"entity_view","header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_view",b"entity_view","header",b"header"]) -> None: ...
global___ReadFeatureValuesResponse = ReadFeatureValuesResponse

class StreamingReadFeatureValuesRequest(google.protobuf.message.Message):
    """Request message for
    [FeaturestoreOnlineServingService.StreamingFeatureValuesRead][].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    ENTITY_IDS_FIELD_NUMBER: builtins.int
    FEATURE_SELECTOR_FIELD_NUMBER: builtins.int
    entity_type: typing.Text = ...
    """Required. The resource name of the entities' type.
    Value format:
    `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`.
    For example,
    for a machine learning model predicting user clicks on a website, an
    EntityType ID could be `user`.
    """

    @property
    def entity_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. IDs of entities to read Feature values of. The maximum number of IDs is
        100. For example, for a machine learning model predicting user clicks on a
        website, an entity ID could be `user_123`.
        """
        pass
    @property
    def feature_selector(self) -> google.cloud.aiplatform.v1.feature_selector_pb2.FeatureSelector:
        """Required. Selector choosing Features of the target EntityType. Feature IDs will be
        deduplicated.
        """
        pass
    def __init__(self,
        *,
        entity_type : typing.Text = ...,
        entity_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        feature_selector : typing.Optional[google.cloud.aiplatform.v1.feature_selector_pb2.FeatureSelector] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["feature_selector",b"feature_selector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_ids",b"entity_ids","entity_type",b"entity_type","feature_selector",b"feature_selector"]) -> None: ...
global___StreamingReadFeatureValuesRequest = StreamingReadFeatureValuesRequest

class FeatureValue(google.protobuf.message.Message):
    """Value for a feature.
    NEXT ID: 15
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Metadata(google.protobuf.message.Message):
        """Metadata of feature value."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        GENERATE_TIME_FIELD_NUMBER: builtins.int
        @property
        def generate_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """Feature generation timestamp. Typically, it is provided by user at
            feature ingestion time. If not, feature store
            will use the system timestamp when the data is ingested into feature
            store. For streaming ingestion, the time, aligned by days, must be no
            older than five years (1825 days) and no later than one year (366 days)
            in the future.
            """
            pass
        def __init__(self,
            *,
            generate_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["generate_time",b"generate_time"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["generate_time",b"generate_time"]) -> None: ...

    BOOL_VALUE_FIELD_NUMBER: builtins.int
    DOUBLE_VALUE_FIELD_NUMBER: builtins.int
    INT64_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    BOOL_ARRAY_VALUE_FIELD_NUMBER: builtins.int
    DOUBLE_ARRAY_VALUE_FIELD_NUMBER: builtins.int
    INT64_ARRAY_VALUE_FIELD_NUMBER: builtins.int
    STRING_ARRAY_VALUE_FIELD_NUMBER: builtins.int
    BYTES_VALUE_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    bool_value: builtins.bool = ...
    """Bool type feature value."""

    double_value: builtins.float = ...
    """Double type feature value."""

    int64_value: builtins.int = ...
    """Int64 feature value."""

    string_value: typing.Text = ...
    """String feature value."""

    @property
    def bool_array_value(self) -> google.cloud.aiplatform.v1.types_pb2.BoolArray:
        """A list of bool type feature value."""
        pass
    @property
    def double_array_value(self) -> google.cloud.aiplatform.v1.types_pb2.DoubleArray:
        """A list of double type feature value."""
        pass
    @property
    def int64_array_value(self) -> google.cloud.aiplatform.v1.types_pb2.Int64Array:
        """A list of int64 type feature value."""
        pass
    @property
    def string_array_value(self) -> google.cloud.aiplatform.v1.types_pb2.StringArray:
        """A list of string type feature value."""
        pass
    bytes_value: builtins.bytes = ...
    """Bytes feature value."""

    @property
    def metadata(self) -> global___FeatureValue.Metadata:
        """Metadata of feature value."""
        pass
    def __init__(self,
        *,
        bool_value : builtins.bool = ...,
        double_value : builtins.float = ...,
        int64_value : builtins.int = ...,
        string_value : typing.Text = ...,
        bool_array_value : typing.Optional[google.cloud.aiplatform.v1.types_pb2.BoolArray] = ...,
        double_array_value : typing.Optional[google.cloud.aiplatform.v1.types_pb2.DoubleArray] = ...,
        int64_array_value : typing.Optional[google.cloud.aiplatform.v1.types_pb2.Int64Array] = ...,
        string_array_value : typing.Optional[google.cloud.aiplatform.v1.types_pb2.StringArray] = ...,
        bytes_value : builtins.bytes = ...,
        metadata : typing.Optional[global___FeatureValue.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bool_array_value",b"bool_array_value","bool_value",b"bool_value","bytes_value",b"bytes_value","double_array_value",b"double_array_value","double_value",b"double_value","int64_array_value",b"int64_array_value","int64_value",b"int64_value","metadata",b"metadata","string_array_value",b"string_array_value","string_value",b"string_value","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bool_array_value",b"bool_array_value","bool_value",b"bool_value","bytes_value",b"bytes_value","double_array_value",b"double_array_value","double_value",b"double_value","int64_array_value",b"int64_array_value","int64_value",b"int64_value","metadata",b"metadata","string_array_value",b"string_array_value","string_value",b"string_value","value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["bool_value","double_value","int64_value","string_value","bool_array_value","double_array_value","int64_array_value","string_array_value","bytes_value"]]: ...
global___FeatureValue = FeatureValue

class FeatureValueList(google.protobuf.message.Message):
    """Container for list of values."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeatureValue]:
        """A list of feature values. All of them should be the same data type."""
        pass
    def __init__(self,
        *,
        values : typing.Optional[typing.Iterable[global___FeatureValue]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values",b"values"]) -> None: ...
global___FeatureValueList = FeatureValueList
