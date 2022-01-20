"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.export_evaluated_data_items_config_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AutoMlForecasting(google.protobuf.message.Message):
    """A TrainingJob that trains and uploads an AutoML Forecasting Model."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INPUTS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    @property
    def inputs(self) -> global___AutoMlForecastingInputs:
        """The input parameters of this TrainingJob."""
        pass
    @property
    def metadata(self) -> global___AutoMlForecastingMetadata:
        """The metadata information."""
        pass
    def __init__(self,
        *,
        inputs : typing.Optional[global___AutoMlForecastingInputs] = ...,
        metadata : typing.Optional[global___AutoMlForecastingMetadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["inputs",b"inputs","metadata",b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["inputs",b"inputs","metadata",b"metadata"]) -> None: ...
global___AutoMlForecasting = AutoMlForecasting

class AutoMlForecastingInputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Transformation(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class AutoTransformation(google.protobuf.message.Message):
            """Training pipeline will infer the proper transformation based on the
            statistic of dataset.
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            COLUMN_NAME_FIELD_NUMBER: builtins.int
            column_name: typing.Text = ...
            def __init__(self,
                *,
                column_name : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["column_name",b"column_name"]) -> None: ...

        class NumericTransformation(google.protobuf.message.Message):
            """Training pipeline will perform following transformation functions.

            *  The value converted to float32.

            *  The z_score of the value.

            *  log(value+1) when the value is greater than or equal to 0. Otherwise,
               this transformation is not applied and the value is considered a
               missing value.

            *  z_score of log(value+1) when the value is greater than or equal to 0.
               Otherwise, this transformation is not applied and the value is
               considered a missing value.

            *  A boolean value that indicates whether the value is valid.
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            COLUMN_NAME_FIELD_NUMBER: builtins.int
            column_name: typing.Text = ...
            def __init__(self,
                *,
                column_name : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["column_name",b"column_name"]) -> None: ...

        class CategoricalTransformation(google.protobuf.message.Message):
            """Training pipeline will perform following transformation functions.

            *  The categorical string as is--no change to case, punctuation,
               spelling, tense, and so on.

            *  Convert the category name to a dictionary lookup index and generate an
               embedding for each index.

            *  Categories that appear less than 5 times in the training dataset are
               treated as the "unknown" category. The "unknown" category gets its own
               special lookup index and resulting embedding.
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            COLUMN_NAME_FIELD_NUMBER: builtins.int
            column_name: typing.Text = ...
            def __init__(self,
                *,
                column_name : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["column_name",b"column_name"]) -> None: ...

        class TimestampTransformation(google.protobuf.message.Message):
            """Training pipeline will perform following transformation functions.

            *  Apply the transformation functions for Numerical columns.

            *  Determine the year, month, day,and weekday. Treat each value from the
               timestamp as a Categorical column.

            *  Invalid numerical values (for example, values that fall outside of a
               typical timestamp range, or are extreme values) receive no special
               treatment and are not removed.
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            COLUMN_NAME_FIELD_NUMBER: builtins.int
            TIME_FORMAT_FIELD_NUMBER: builtins.int
            column_name: typing.Text = ...
            time_format: typing.Text = ...
            """The format in which that time field is expressed. The time_format must
            either be one of:

            * `unix-seconds`

            * `unix-milliseconds`

            * `unix-microseconds`

            * `unix-nanoseconds`

            (for respectively number of seconds, milliseconds, microseconds and
            nanoseconds since start of the Unix epoch);

            or be written in `strftime` syntax.

            If time_format is not set, then the
            default format is RFC 3339 `date-time` format, where
            `time-offset` = `"Z"` (e.g. 1985-04-12T23:20:50.52Z)
            """

            def __init__(self,
                *,
                column_name : typing.Text = ...,
                time_format : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["column_name",b"column_name","time_format",b"time_format"]) -> None: ...

        class TextTransformation(google.protobuf.message.Message):
            """Training pipeline will perform following transformation functions.

            *  The text as is--no change to case, punctuation, spelling, tense, and
               so on.

            *  Convert the category name to a dictionary lookup index and generate an
               embedding for each index.
            """
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            COLUMN_NAME_FIELD_NUMBER: builtins.int
            column_name: typing.Text = ...
            def __init__(self,
                *,
                column_name : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["column_name",b"column_name"]) -> None: ...

        AUTO_FIELD_NUMBER: builtins.int
        NUMERIC_FIELD_NUMBER: builtins.int
        CATEGORICAL_FIELD_NUMBER: builtins.int
        TIMESTAMP_FIELD_NUMBER: builtins.int
        TEXT_FIELD_NUMBER: builtins.int
        @property
        def auto(self) -> global___AutoMlForecastingInputs.Transformation.AutoTransformation: ...
        @property
        def numeric(self) -> global___AutoMlForecastingInputs.Transformation.NumericTransformation: ...
        @property
        def categorical(self) -> global___AutoMlForecastingInputs.Transformation.CategoricalTransformation: ...
        @property
        def timestamp(self) -> global___AutoMlForecastingInputs.Transformation.TimestampTransformation: ...
        @property
        def text(self) -> global___AutoMlForecastingInputs.Transformation.TextTransformation: ...
        def __init__(self,
            *,
            auto : typing.Optional[global___AutoMlForecastingInputs.Transformation.AutoTransformation] = ...,
            numeric : typing.Optional[global___AutoMlForecastingInputs.Transformation.NumericTransformation] = ...,
            categorical : typing.Optional[global___AutoMlForecastingInputs.Transformation.CategoricalTransformation] = ...,
            timestamp : typing.Optional[global___AutoMlForecastingInputs.Transformation.TimestampTransformation] = ...,
            text : typing.Optional[global___AutoMlForecastingInputs.Transformation.TextTransformation] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["auto",b"auto","categorical",b"categorical","numeric",b"numeric","text",b"text","timestamp",b"timestamp","transformation_detail",b"transformation_detail"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["auto",b"auto","categorical",b"categorical","numeric",b"numeric","text",b"text","timestamp",b"timestamp","transformation_detail",b"transformation_detail"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["transformation_detail",b"transformation_detail"]) -> typing.Optional[typing_extensions.Literal["auto","numeric","categorical","timestamp","text"]]: ...

    class Granularity(google.protobuf.message.Message):
        """A duration of time expressed in time granularity units."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        UNIT_FIELD_NUMBER: builtins.int
        QUANTITY_FIELD_NUMBER: builtins.int
        unit: typing.Text = ...
        """The time granularity unit of this time period.
        The supported units are:

         * "minute"

         * "hour"

         * "day"

         * "week"

         * "month"

         * "year"
        """

        quantity: builtins.int = ...
        """The number of granularity_units between data points in the training
        data. If `granularity_unit` is `minute`,
        can be 1, 5, 10, 15, or 30. For all other values of `granularity_unit`,
        must be 1.
        """

        def __init__(self,
            *,
            unit : typing.Text = ...,
            quantity : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["quantity",b"quantity","unit",b"unit"]) -> None: ...

    TARGET_COLUMN_FIELD_NUMBER: builtins.int
    TIME_SERIES_IDENTIFIER_COLUMN_FIELD_NUMBER: builtins.int
    TIME_COLUMN_FIELD_NUMBER: builtins.int
    TRANSFORMATIONS_FIELD_NUMBER: builtins.int
    OPTIMIZATION_OBJECTIVE_FIELD_NUMBER: builtins.int
    TRAIN_BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: builtins.int
    WEIGHT_COLUMN_FIELD_NUMBER: builtins.int
    TIME_SERIES_ATTRIBUTE_COLUMNS_FIELD_NUMBER: builtins.int
    UNAVAILABLE_AT_FORECAST_COLUMNS_FIELD_NUMBER: builtins.int
    AVAILABLE_AT_FORECAST_COLUMNS_FIELD_NUMBER: builtins.int
    DATA_GRANULARITY_FIELD_NUMBER: builtins.int
    FORECAST_HORIZON_FIELD_NUMBER: builtins.int
    CONTEXT_WINDOW_FIELD_NUMBER: builtins.int
    EXPORT_EVALUATED_DATA_ITEMS_CONFIG_FIELD_NUMBER: builtins.int
    QUANTILES_FIELD_NUMBER: builtins.int
    VALIDATION_OPTIONS_FIELD_NUMBER: builtins.int
    ADDITIONAL_EXPERIMENTS_FIELD_NUMBER: builtins.int
    target_column: typing.Text = ...
    """The name of the column that the model is to predict."""

    time_series_identifier_column: typing.Text = ...
    """The name of the column that identifies the time series."""

    time_column: typing.Text = ...
    """The name of the column that identifies time order in the time series."""

    @property
    def transformations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AutoMlForecastingInputs.Transformation]:
        """Each transformation will apply transform function to given input column.
        And the result will be used for training.
        When creating transformation for BigQuery Struct column, the column should
        be flattened using "." as the delimiter.
        """
        pass
    optimization_objective: typing.Text = ...
    """Objective function the model is optimizing towards. The training process
    creates a model that optimizes the value of the objective
    function over the validation set.

    The supported optimization objectives:

      * "minimize-rmse" (default) - Minimize root-mean-squared error (RMSE).

      * "minimize-mae" - Minimize mean-absolute error (MAE).

      * "minimize-rmsle" - Minimize root-mean-squared log error (RMSLE).

      * "minimize-rmspe" - Minimize root-mean-squared percentage error (RMSPE).

      * "minimize-wape-mae" - Minimize the combination of weighted absolute
        percentage error (WAPE) and mean-absolute-error (MAE).

      * "minimize-quantile-loss" - Minimize the quantile loss at the quantiles
        defined in `quantiles`.
    """

    train_budget_milli_node_hours: builtins.int = ...
    """Required. The train budget of creating this model, expressed in milli node
    hours i.e. 1,000 value in this field means 1 node hour.

    The training cost of the model will not exceed this budget. The final cost
    will be attempted to be close to the budget, though may end up being (even)
    noticeably smaller - at the backend's discretion. This especially may
    happen when further model training ceases to provide any improvements.

    If the budget is set to a value known to be insufficient to train a
    model for the given dataset, the training won't be attempted and
    will error.

    The train budget must be between 1,000 and 72,000 milli node hours,
    inclusive.
    """

    weight_column: typing.Text = ...
    """Column name that should be used as the weight column.
    Higher values in this column give more importance to the row
    during model training. The column must have numeric values between 0 and
    10000 inclusively; 0 means the row is ignored for training. If weight
    column field is not set, then all rows are assumed to have equal weight
    of 1.
    """

    @property
    def time_series_attribute_columns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Column names that should be used as attribute columns.
        The value of these columns does not vary as a function of time.
        For example, store ID or item color.
        """
        pass
    @property
    def unavailable_at_forecast_columns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Names of columns that are unavailable when a forecast is requested.
        This column contains information for the given entity (identified
        by the time_series_identifier_column) that is unknown before the forecast
        For example, actual weather on a given day.
        """
        pass
    @property
    def available_at_forecast_columns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Names of columns that are available and provided when a forecast
        is requested. These columns
        contain information for the given entity (identified by the
        time_series_identifier_column column) that is known at forecast.
        For example, predicted weather for a specific day.
        """
        pass
    @property
    def data_granularity(self) -> global___AutoMlForecastingInputs.Granularity:
        """Expected difference in time granularity between rows in the data."""
        pass
    forecast_horizon: builtins.int = ...
    """The amount of time into the future for which forecasted values for the
    target are returned. Expressed in number of units defined by the
    `data_granularity` field.
    """

    context_window: builtins.int = ...
    """The amount of time into the past training and prediction data is used
    for model training and prediction respectively. Expressed in number of
    units defined by the `data_granularity` field.
    """

    @property
    def export_evaluated_data_items_config(self) -> google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.export_evaluated_data_items_config_pb2.ExportEvaluatedDataItemsConfig:
        """Configuration for exporting test set predictions to a BigQuery table. If
        this configuration is absent, then the export is not performed.
        """
        pass
    @property
    def quantiles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Quantiles to use for minimize-quantile-loss `optimization_objective`. Up to
        5 quantiles are allowed of values between 0 and 1, exclusive. Required if
        the value of optimization_objective is minimize-quantile-loss. Represents
        the percent quantiles to use for that objective. Quantiles must be unique.
        """
        pass
    validation_options: typing.Text = ...
    """Validation options for the data validation component. The available options
    are:

      * "fail-pipeline" - default, will validate against the validation and
         fail the pipeline if it fails.

      * "ignore-validation" - ignore the results of the validation and continue
    """

    @property
    def additional_experiments(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Additional experiment flags for the time series forcasting training."""
        pass
    def __init__(self,
        *,
        target_column : typing.Text = ...,
        time_series_identifier_column : typing.Text = ...,
        time_column : typing.Text = ...,
        transformations : typing.Optional[typing.Iterable[global___AutoMlForecastingInputs.Transformation]] = ...,
        optimization_objective : typing.Text = ...,
        train_budget_milli_node_hours : builtins.int = ...,
        weight_column : typing.Text = ...,
        time_series_attribute_columns : typing.Optional[typing.Iterable[typing.Text]] = ...,
        unavailable_at_forecast_columns : typing.Optional[typing.Iterable[typing.Text]] = ...,
        available_at_forecast_columns : typing.Optional[typing.Iterable[typing.Text]] = ...,
        data_granularity : typing.Optional[global___AutoMlForecastingInputs.Granularity] = ...,
        forecast_horizon : builtins.int = ...,
        context_window : builtins.int = ...,
        export_evaluated_data_items_config : typing.Optional[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.export_evaluated_data_items_config_pb2.ExportEvaluatedDataItemsConfig] = ...,
        quantiles : typing.Optional[typing.Iterable[builtins.float]] = ...,
        validation_options : typing.Text = ...,
        additional_experiments : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data_granularity",b"data_granularity","export_evaluated_data_items_config",b"export_evaluated_data_items_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["additional_experiments",b"additional_experiments","available_at_forecast_columns",b"available_at_forecast_columns","context_window",b"context_window","data_granularity",b"data_granularity","export_evaluated_data_items_config",b"export_evaluated_data_items_config","forecast_horizon",b"forecast_horizon","optimization_objective",b"optimization_objective","quantiles",b"quantiles","target_column",b"target_column","time_column",b"time_column","time_series_attribute_columns",b"time_series_attribute_columns","time_series_identifier_column",b"time_series_identifier_column","train_budget_milli_node_hours",b"train_budget_milli_node_hours","transformations",b"transformations","unavailable_at_forecast_columns",b"unavailable_at_forecast_columns","validation_options",b"validation_options","weight_column",b"weight_column"]) -> None: ...
global___AutoMlForecastingInputs = AutoMlForecastingInputs

class AutoMlForecastingMetadata(google.protobuf.message.Message):
    """Model metadata specific to AutoML Forecasting."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRAIN_COST_MILLI_NODE_HOURS_FIELD_NUMBER: builtins.int
    train_cost_milli_node_hours: builtins.int = ...
    """Output only. The actual training cost of the model, expressed in milli
    node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed
    to not exceed the train budget.
    """

    def __init__(self,
        *,
        train_cost_milli_node_hours : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["train_cost_milli_node_hours",b"train_cost_milli_node_hours"]) -> None: ...
global___AutoMlForecastingMetadata = AutoMlForecastingMetadata
