"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.aiplatform.v1.tensorboard_time_series_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TimeSeriesData(google.protobuf.message.Message):
    """All the data stored in a TensorboardTimeSeries."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TENSORBOARD_TIME_SERIES_ID_FIELD_NUMBER: builtins.int
    VALUE_TYPE_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    tensorboard_time_series_id: typing.Text = ...
    """Required. The ID of the TensorboardTimeSeries, which will become the final component
    of the TensorboardTimeSeries' resource name
    """

    value_type: google.cloud.aiplatform.v1.tensorboard_time_series_pb2.TensorboardTimeSeries.ValueType.ValueType = ...
    """Required. Immutable. The value type of this time series. All the values in this time series data
    must match this value type.
    """

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TimeSeriesDataPoint]:
        """Required. Data points in this time series."""
        pass
    def __init__(self,
        *,
        tensorboard_time_series_id : typing.Text = ...,
        value_type : google.cloud.aiplatform.v1.tensorboard_time_series_pb2.TensorboardTimeSeries.ValueType.ValueType = ...,
        values : typing.Optional[typing.Iterable[global___TimeSeriesDataPoint]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tensorboard_time_series_id",b"tensorboard_time_series_id","value_type",b"value_type","values",b"values"]) -> None: ...
global___TimeSeriesData = TimeSeriesData

class TimeSeriesDataPoint(google.protobuf.message.Message):
    """A TensorboardTimeSeries data point."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SCALAR_FIELD_NUMBER: builtins.int
    TENSOR_FIELD_NUMBER: builtins.int
    BLOBS_FIELD_NUMBER: builtins.int
    WALL_TIME_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    @property
    def scalar(self) -> global___Scalar:
        """A scalar value."""
        pass
    @property
    def tensor(self) -> global___TensorboardTensor:
        """A tensor value."""
        pass
    @property
    def blobs(self) -> global___TensorboardBlobSequence:
        """A blob sequence value."""
        pass
    @property
    def wall_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Wall clock timestamp when this data point is generated by the end user."""
        pass
    step: builtins.int = ...
    """Step index of this data point within the run."""

    def __init__(self,
        *,
        scalar : typing.Optional[global___Scalar] = ...,
        tensor : typing.Optional[global___TensorboardTensor] = ...,
        blobs : typing.Optional[global___TensorboardBlobSequence] = ...,
        wall_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        step : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["blobs",b"blobs","scalar",b"scalar","tensor",b"tensor","value",b"value","wall_time",b"wall_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["blobs",b"blobs","scalar",b"scalar","step",b"step","tensor",b"tensor","value",b"value","wall_time",b"wall_time"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["scalar","tensor","blobs"]]: ...
global___TimeSeriesDataPoint = TimeSeriesDataPoint

class Scalar(google.protobuf.message.Message):
    """One point viewable on a scalar metric plot."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.float = ...
    """Value of the point at this step / timestamp."""

    def __init__(self,
        *,
        value : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___Scalar = Scalar

class TensorboardTensor(google.protobuf.message.Message):
    """One point viewable on a tensor metric plot."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUE_FIELD_NUMBER: builtins.int
    VERSION_NUMBER_FIELD_NUMBER: builtins.int
    value: builtins.bytes = ...
    """Required. Serialized form of
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/tensor.proto
    """

    version_number: builtins.int = ...
    """Optional. Version number of TensorProto used to serialize [value][google.cloud.aiplatform.v1.TensorboardTensor.value]."""

    def __init__(self,
        *,
        value : builtins.bytes = ...,
        version_number : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value","version_number",b"version_number"]) -> None: ...
global___TensorboardTensor = TensorboardTensor

class TensorboardBlobSequence(google.protobuf.message.Message):
    """One point viewable on a blob metric plot, but mostly just a wrapper message
    to work around repeated fields can't be used directly within `oneof` fields.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorboardBlob]:
        """List of blobs contained within the sequence."""
        pass
    def __init__(self,
        *,
        values : typing.Optional[typing.Iterable[global___TensorboardBlob]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["values",b"values"]) -> None: ...
global___TensorboardBlobSequence = TensorboardBlobSequence

class TensorboardBlob(google.protobuf.message.Message):
    """One blob (e.g, image, graph) viewable on a blob metric plot."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    """Output only. A URI safe key uniquely identifying a blob. Can be used to locate the blob
    stored in the Cloud Storage bucket of the consumer project.
    """

    data: builtins.bytes = ...
    """Optional. The bytes of the blob is not present unless it's returned by the
    ReadTensorboardBlobData endpoint.
    """

    def __init__(self,
        *,
        id : typing.Text = ...,
        data : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data",b"data","id",b"id"]) -> None: ...
global___TensorboardBlob = TensorboardBlob
