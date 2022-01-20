"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Distribution(google.protobuf.message.Message):
    """`Distribution` contains summary statistics for a population of values. It
    optionally contains a histogram representing the distribution of those values
    across a set of buckets.

    The summary statistics are the count, mean, sum of the squared deviation from
    the mean, the minimum, and the maximum of the set of population of values.
    The histogram is based on a sequence of buckets and gives a count of values
    that fall into each bucket. The boundaries of the buckets are given either
    explicitly or by formulas for buckets of fixed or exponentially increasing
    widths.

    Although it is not forbidden, it is generally a bad idea to include
    non-finite values (infinities or NaNs) in the population of values, as this
    will render the `mean` and `sum_of_squared_deviation` fields meaningless.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Range(google.protobuf.message.Message):
        """The range of the population values."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        MIN_FIELD_NUMBER: builtins.int
        MAX_FIELD_NUMBER: builtins.int
        min: builtins.float = ...
        """The minimum of the population values."""

        max: builtins.float = ...
        """The maximum of the population values."""

        def __init__(self,
            *,
            min : builtins.float = ...,
            max : builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["max",b"max","min",b"min"]) -> None: ...

    class BucketOptions(google.protobuf.message.Message):
        """`BucketOptions` describes the bucket boundaries used to create a histogram
        for the distribution. The buckets can be in a linear sequence, an
        exponential sequence, or each bucket can be specified explicitly.
        `BucketOptions` does not include the number of values in each bucket.

        A bucket has an inclusive lower bound and exclusive upper bound for the
        values that are counted for that bucket. The upper bound of a bucket must
        be strictly greater than the lower bound. The sequence of N buckets for a
        distribution consists of an underflow bucket (number 0), zero or more
        finite buckets (number 1 through N - 2) and an overflow bucket (number N -
        1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the
        same as the upper bound of bucket i - 1. The buckets span the whole range
        of finite values: lower bound of the underflow bucket is -infinity and the
        upper bound of the overflow bucket is +infinity. The finite buckets are
        so-called because both bounds are finite.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class Linear(google.protobuf.message.Message):
            """Specifies a linear sequence of buckets that all have the same width
            (except overflow and underflow). Each bucket represents a constant
            absolute uncertainty on the specific value in the bucket.

            There are `num_finite_buckets + 2` (= N) buckets. Bucket `i` has the
            following boundaries:

               Upper bound (0 <= i < N-1):     offset + (width * i).
               Lower bound (1 <= i < N):       offset + (width * (i - 1)).
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            NUM_FINITE_BUCKETS_FIELD_NUMBER: builtins.int
            WIDTH_FIELD_NUMBER: builtins.int
            OFFSET_FIELD_NUMBER: builtins.int
            num_finite_buckets: builtins.int = ...
            """Must be greater than 0."""

            width: builtins.float = ...
            """Must be greater than 0."""

            offset: builtins.float = ...
            """Lower bound of the first bucket."""

            def __init__(self,
                *,
                num_finite_buckets : builtins.int = ...,
                width : builtins.float = ...,
                offset : builtins.float = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["num_finite_buckets",b"num_finite_buckets","offset",b"offset","width",b"width"]) -> None: ...

        class Exponential(google.protobuf.message.Message):
            """Specifies an exponential sequence of buckets that have a width that is
            proportional to the value of the lower bound. Each bucket represents a
            constant relative uncertainty on a specific value in the bucket.

            There are `num_finite_buckets + 2` (= N) buckets. Bucket `i` has the
            following boundaries:

               Upper bound (0 <= i < N-1):     scale * (growth_factor ^ i).
               Lower bound (1 <= i < N):       scale * (growth_factor ^ (i - 1)).
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            NUM_FINITE_BUCKETS_FIELD_NUMBER: builtins.int
            GROWTH_FACTOR_FIELD_NUMBER: builtins.int
            SCALE_FIELD_NUMBER: builtins.int
            num_finite_buckets: builtins.int = ...
            """Must be greater than 0."""

            growth_factor: builtins.float = ...
            """Must be greater than 1."""

            scale: builtins.float = ...
            """Must be greater than 0."""

            def __init__(self,
                *,
                num_finite_buckets : builtins.int = ...,
                growth_factor : builtins.float = ...,
                scale : builtins.float = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["growth_factor",b"growth_factor","num_finite_buckets",b"num_finite_buckets","scale",b"scale"]) -> None: ...

        class Explicit(google.protobuf.message.Message):
            """Specifies a set of buckets with arbitrary widths.

            There are `size(bounds) + 1` (= N) buckets. Bucket `i` has the following
            boundaries:

               Upper bound (0 <= i < N-1):     bounds[i]
               Lower bound (1 <= i < N);       bounds[i - 1]

            The `bounds` field must contain at least one element. If `bounds` has
            only one element, then there are no finite buckets, and that single
            element is the common boundary of the overflow and underflow buckets.
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            BOUNDS_FIELD_NUMBER: builtins.int
            @property
            def bounds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
                """The values must be monotonically increasing."""
                pass
            def __init__(self,
                *,
                bounds : typing.Optional[typing.Iterable[builtins.float]] = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["bounds",b"bounds"]) -> None: ...

        LINEAR_BUCKETS_FIELD_NUMBER: builtins.int
        EXPONENTIAL_BUCKETS_FIELD_NUMBER: builtins.int
        EXPLICIT_BUCKETS_FIELD_NUMBER: builtins.int
        @property
        def linear_buckets(self) -> global___Distribution.BucketOptions.Linear:
            """The linear bucket."""
            pass
        @property
        def exponential_buckets(self) -> global___Distribution.BucketOptions.Exponential:
            """The exponential buckets."""
            pass
        @property
        def explicit_buckets(self) -> global___Distribution.BucketOptions.Explicit:
            """The explicit buckets."""
            pass
        def __init__(self,
            *,
            linear_buckets : typing.Optional[global___Distribution.BucketOptions.Linear] = ...,
            exponential_buckets : typing.Optional[global___Distribution.BucketOptions.Exponential] = ...,
            explicit_buckets : typing.Optional[global___Distribution.BucketOptions.Explicit] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["explicit_buckets",b"explicit_buckets","exponential_buckets",b"exponential_buckets","linear_buckets",b"linear_buckets","options",b"options"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["explicit_buckets",b"explicit_buckets","exponential_buckets",b"exponential_buckets","linear_buckets",b"linear_buckets","options",b"options"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["options",b"options"]) -> typing.Optional[typing_extensions.Literal["linear_buckets","exponential_buckets","explicit_buckets"]]: ...

    class Exemplar(google.protobuf.message.Message):
        """Exemplars are example points that may be used to annotate aggregated
        distribution values. They are metadata that gives information about a
        particular value added to a Distribution bucket, such as a trace ID that
        was active when a value was added. They may contain further information,
        such as a example values and timestamps, origin, etc.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        VALUE_FIELD_NUMBER: builtins.int
        TIMESTAMP_FIELD_NUMBER: builtins.int
        ATTACHMENTS_FIELD_NUMBER: builtins.int
        value: builtins.float = ...
        """Value of the exemplar point. This value determines to which bucket the
        exemplar belongs.
        """

        @property
        def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """The observation (sampling) time of the above value."""
            pass
        @property
        def attachments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
            """Contextual information about the example value. Examples are:

              Trace: type.googleapis.com/google.monitoring.v3.SpanContext

              Literal string: type.googleapis.com/google.protobuf.StringValue

              Labels dropped during aggregation:
                type.googleapis.com/google.monitoring.v3.DroppedLabels

            There may be only a single attachment of any given message type in a
            single exemplar, and this is enforced by the system.
            """
            pass
        def __init__(self,
            *,
            value : builtins.float = ...,
            timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
            attachments : typing.Optional[typing.Iterable[google.protobuf.any_pb2.Any]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["attachments",b"attachments","timestamp",b"timestamp","value",b"value"]) -> None: ...

    COUNT_FIELD_NUMBER: builtins.int
    MEAN_FIELD_NUMBER: builtins.int
    SUM_OF_SQUARED_DEVIATION_FIELD_NUMBER: builtins.int
    RANGE_FIELD_NUMBER: builtins.int
    BUCKET_OPTIONS_FIELD_NUMBER: builtins.int
    BUCKET_COUNTS_FIELD_NUMBER: builtins.int
    EXEMPLARS_FIELD_NUMBER: builtins.int
    count: builtins.int = ...
    """The number of values in the population. Must be non-negative. This value
    must equal the sum of the values in `bucket_counts` if a histogram is
    provided.
    """

    mean: builtins.float = ...
    """The arithmetic mean of the values in the population. If `count` is zero
    then this field must be zero.
    """

    sum_of_squared_deviation: builtins.float = ...
    """The sum of squared deviations from the mean of the values in the
    population. For values x_i this is:

        Sum[i=1..n]((x_i - mean)^2)

    Knuth, "The Art of Computer Programming", Vol. 2, page 232, 3rd edition
    describes Welford's method for accumulating this sum in one pass.

    If `count` is zero then this field must be zero.
    """

    @property
    def range(self) -> global___Distribution.Range:
        """If specified, contains the range of the population values. The field
        must not be present if the `count` is zero.
        """
        pass
    @property
    def bucket_options(self) -> global___Distribution.BucketOptions:
        """Defines the histogram bucket boundaries. If the distribution does not
        contain a histogram, then omit this field.
        """
        pass
    @property
    def bucket_counts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """The number of values in each bucket of the histogram, as described in
        `bucket_options`. If the distribution does not have a histogram, then omit
        this field. If there is a histogram, then the sum of the values in
        `bucket_counts` must equal the value in the `count` field of the
        distribution.

        If present, `bucket_counts` should contain N values, where N is the number
        of buckets specified in `bucket_options`. If you supply fewer than N
        values, the remaining values are assumed to be 0.

        The order of the values in `bucket_counts` follows the bucket numbering
        schemes described for the three bucket types. The first value must be the
        count for the underflow bucket (number 0). The next N-2 values are the
        counts for the finite buckets (number 1 through N-2). The N'th value in
        `bucket_counts` is the count for the overflow bucket (number N-1).
        """
        pass
    @property
    def exemplars(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Distribution.Exemplar]:
        """Must be in increasing order of `value` field."""
        pass
    def __init__(self,
        *,
        count : builtins.int = ...,
        mean : builtins.float = ...,
        sum_of_squared_deviation : builtins.float = ...,
        range : typing.Optional[global___Distribution.Range] = ...,
        bucket_options : typing.Optional[global___Distribution.BucketOptions] = ...,
        bucket_counts : typing.Optional[typing.Iterable[builtins.int]] = ...,
        exemplars : typing.Optional[typing.Iterable[global___Distribution.Exemplar]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bucket_options",b"bucket_options","range",b"range"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bucket_counts",b"bucket_counts","bucket_options",b"bucket_options","count",b"count","exemplars",b"exemplars","mean",b"mean","range",b"range","sum_of_squared_deviation",b"sum_of_squared_deviation"]) -> None: ...
global___Distribution = Distribution
