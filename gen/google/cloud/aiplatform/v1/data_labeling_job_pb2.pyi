"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.aiplatform.v1.encryption_spec_pb2
import google.cloud.aiplatform.v1.job_state_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.type.money_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class DataLabelingJob(google.protobuf.message.Message):
    """DataLabelingJob is used to trigger a human labeling job on unlabeled data
    from the following Dataset:
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class AnnotationLabelsEntry(google.protobuf.message.Message):
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

    class LabelsEntry(google.protobuf.message.Message):
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

    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DATASETS_FIELD_NUMBER: builtins.int
    ANNOTATION_LABELS_FIELD_NUMBER: builtins.int
    LABELER_COUNT_FIELD_NUMBER: builtins.int
    INSTRUCTION_URI_FIELD_NUMBER: builtins.int
    INPUTS_SCHEMA_URI_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    LABELING_PROGRESS_FIELD_NUMBER: builtins.int
    CURRENT_SPEND_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SPECIALIST_POOLS_FIELD_NUMBER: builtins.int
    ENCRYPTION_SPEC_FIELD_NUMBER: builtins.int
    ACTIVE_LEARNING_CONFIG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. Resource name of the DataLabelingJob."""

    display_name: typing.Text = ...
    """Required. The user-defined name of the DataLabelingJob.
    The name can be up to 128 characters long and can be consist of any UTF-8
    characters.
    Display name of a DataLabelingJob.
    """

    @property
    def datasets(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. Dataset resource names. Right now we only support labeling from a single
        Dataset.
        Format:
        `projects/{project}/locations/{location}/datasets/{dataset}`
        """
        pass
    @property
    def annotation_labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Labels to assign to annotations generated by this DataLabelingJob.

        Label keys and values can be no longer than 64 characters
        (Unicode codepoints), can only contain lowercase letters, numeric
        characters, underscores and dashes. International characters are allowed.
        See https://goo.gl/xmQnxf for more information and examples of labels.
        System reserved label keys are prefixed with "aiplatform.googleapis.com/"
        and are immutable.
        """
        pass
    labeler_count: builtins.int = ...
    """Required. Number of labelers to work on each DataItem."""

    instruction_uri: typing.Text = ...
    """Required. The Google Cloud Storage location of the instruction pdf. This pdf is
    shared with labelers, and provides detailed description on how to label
    DataItems in Datasets.
    """

    inputs_schema_uri: typing.Text = ...
    """Required. Points to a YAML file stored on Google Cloud Storage describing the
    config for a specific type of DataLabelingJob.
    The schema files that can be used here are found in the
    https://storage.googleapis.com/google-cloud-aiplatform bucket in the
    /schema/datalabelingjob/inputs/ folder.
    """

    @property
    def inputs(self) -> google.protobuf.struct_pb2.Value:
        """Required. Input config parameters for the DataLabelingJob."""
        pass
    state: google.cloud.aiplatform.v1.job_state_pb2.JobState.ValueType = ...
    """Output only. The detailed state of the job."""

    labeling_progress: builtins.int = ...
    """Output only. Current labeling job progress percentage scaled in interval [0, 100],
    indicating the percentage of DataItems that has been finished.
    """

    @property
    def current_spend(self) -> google.type.money_pb2.Money:
        """Output only. Estimated cost(in US dollars) that the DataLabelingJob has incurred to
        date.
        """
        pass
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Timestamp when this DataLabelingJob was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Timestamp when this DataLabelingJob was updated most recently."""
        pass
    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """Output only. DataLabelingJob errors. It is only populated when job's state is
        `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.
        """
        pass
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """The labels with user-defined metadata to organize your DataLabelingJobs.

        Label keys and values can be no longer than 64 characters
        (Unicode codepoints), can only contain lowercase letters, numeric
        characters, underscores and dashes. International characters are allowed.

        See https://goo.gl/xmQnxf for more information and examples of labels.
        System reserved label keys are prefixed with "aiplatform.googleapis.com/"
        and are immutable. Following system labels exist for each DataLabelingJob:

        * "aiplatform.googleapis.com/schema": output only, its value is the
          [inputs_schema][google.cloud.aiplatform.v1.DataLabelingJob.inputs_schema_uri]'s title.
        """
        pass
    @property
    def specialist_pools(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The SpecialistPools' resource names associated with this job."""
        pass
    @property
    def encryption_spec(self) -> google.cloud.aiplatform.v1.encryption_spec_pb2.EncryptionSpec:
        """Customer-managed encryption key spec for a DataLabelingJob. If set, this
        DataLabelingJob will be secured by this key.

        Note: Annotations created in the DataLabelingJob are associated with
        the EncryptionSpec of the Dataset they are exported to.
        """
        pass
    @property
    def active_learning_config(self) -> global___ActiveLearningConfig:
        """Parameters that configure the active learning pipeline. Active learning
        will label the data incrementally via several iterations. For every
        iteration, it will select a batch of data based on the sampling strategy.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        datasets : typing.Optional[typing.Iterable[typing.Text]] = ...,
        annotation_labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        labeler_count : builtins.int = ...,
        instruction_uri : typing.Text = ...,
        inputs_schema_uri : typing.Text = ...,
        inputs : typing.Optional[google.protobuf.struct_pb2.Value] = ...,
        state : google.cloud.aiplatform.v1.job_state_pb2.JobState.ValueType = ...,
        labeling_progress : builtins.int = ...,
        current_spend : typing.Optional[google.type.money_pb2.Money] = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        specialist_pools : typing.Optional[typing.Iterable[typing.Text]] = ...,
        encryption_spec : typing.Optional[google.cloud.aiplatform.v1.encryption_spec_pb2.EncryptionSpec] = ...,
        active_learning_config : typing.Optional[global___ActiveLearningConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["active_learning_config",b"active_learning_config","create_time",b"create_time","current_spend",b"current_spend","encryption_spec",b"encryption_spec","error",b"error","inputs",b"inputs","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_learning_config",b"active_learning_config","annotation_labels",b"annotation_labels","create_time",b"create_time","current_spend",b"current_spend","datasets",b"datasets","display_name",b"display_name","encryption_spec",b"encryption_spec","error",b"error","inputs",b"inputs","inputs_schema_uri",b"inputs_schema_uri","instruction_uri",b"instruction_uri","labeler_count",b"labeler_count","labeling_progress",b"labeling_progress","labels",b"labels","name",b"name","specialist_pools",b"specialist_pools","state",b"state","update_time",b"update_time"]) -> None: ...
global___DataLabelingJob = DataLabelingJob

class ActiveLearningConfig(google.protobuf.message.Message):
    """Parameters that configure the active learning pipeline. Active learning will
     label the data incrementally by several iterations. For every iteration, it
     will select a batch of data based on the sampling strategy.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAX_DATA_ITEM_COUNT_FIELD_NUMBER: builtins.int
    MAX_DATA_ITEM_PERCENTAGE_FIELD_NUMBER: builtins.int
    SAMPLE_CONFIG_FIELD_NUMBER: builtins.int
    TRAINING_CONFIG_FIELD_NUMBER: builtins.int
    max_data_item_count: builtins.int = ...
    """Max number of human labeled DataItems."""

    max_data_item_percentage: builtins.int = ...
    """Max percent of total DataItems for human labeling."""

    @property
    def sample_config(self) -> global___SampleConfig:
        """Active learning data sampling config. For every active learning labeling
        iteration, it will select a batch of data based on the sampling strategy.
        """
        pass
    @property
    def training_config(self) -> global___TrainingConfig:
        """CMLE training config. For every active learning labeling iteration, system
        will train a machine learning model on CMLE. The trained model will be used
        by data sampling algorithm to select DataItems.
        """
        pass
    def __init__(self,
        *,
        max_data_item_count : builtins.int = ...,
        max_data_item_percentage : builtins.int = ...,
        sample_config : typing.Optional[global___SampleConfig] = ...,
        training_config : typing.Optional[global___TrainingConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["human_labeling_budget",b"human_labeling_budget","max_data_item_count",b"max_data_item_count","max_data_item_percentage",b"max_data_item_percentage","sample_config",b"sample_config","training_config",b"training_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["human_labeling_budget",b"human_labeling_budget","max_data_item_count",b"max_data_item_count","max_data_item_percentage",b"max_data_item_percentage","sample_config",b"sample_config","training_config",b"training_config"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["human_labeling_budget",b"human_labeling_budget"]) -> typing.Optional[typing_extensions.Literal["max_data_item_count","max_data_item_percentage"]]: ...
global___ActiveLearningConfig = ActiveLearningConfig

class SampleConfig(google.protobuf.message.Message):
    """Active learning data sampling config. For every active learning labeling
    iteration, it will select a batch of data based on the sampling strategy.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _SampleStrategy:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SampleStrategyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SampleStrategy.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        SAMPLE_STRATEGY_UNSPECIFIED: SampleConfig.SampleStrategy.ValueType = ...  # 0
        """Default will be treated as UNCERTAINTY."""

        UNCERTAINTY: SampleConfig.SampleStrategy.ValueType = ...  # 1
        """Sample the most uncertain data to label."""

    class SampleStrategy(_SampleStrategy, metaclass=_SampleStrategyEnumTypeWrapper):
        """Sample strategy decides which subset of DataItems should be selected for
        human labeling in every batch.
        """
        pass

    SAMPLE_STRATEGY_UNSPECIFIED: SampleConfig.SampleStrategy.ValueType = ...  # 0
    """Default will be treated as UNCERTAINTY."""

    UNCERTAINTY: SampleConfig.SampleStrategy.ValueType = ...  # 1
    """Sample the most uncertain data to label."""


    INITIAL_BATCH_SAMPLE_PERCENTAGE_FIELD_NUMBER: builtins.int
    FOLLOWING_BATCH_SAMPLE_PERCENTAGE_FIELD_NUMBER: builtins.int
    SAMPLE_STRATEGY_FIELD_NUMBER: builtins.int
    initial_batch_sample_percentage: builtins.int = ...
    """The percentage of data needed to be labeled in the first batch."""

    following_batch_sample_percentage: builtins.int = ...
    """The percentage of data needed to be labeled in each following batch
    (except the first batch).
    """

    sample_strategy: global___SampleConfig.SampleStrategy.ValueType = ...
    """Field to choose sampling strategy. Sampling strategy will decide which data
    should be selected for human labeling in every batch.
    """

    def __init__(self,
        *,
        initial_batch_sample_percentage : builtins.int = ...,
        following_batch_sample_percentage : builtins.int = ...,
        sample_strategy : global___SampleConfig.SampleStrategy.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["following_batch_sample_percentage",b"following_batch_sample_percentage","following_batch_sample_size",b"following_batch_sample_size","initial_batch_sample_percentage",b"initial_batch_sample_percentage","initial_batch_sample_size",b"initial_batch_sample_size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["following_batch_sample_percentage",b"following_batch_sample_percentage","following_batch_sample_size",b"following_batch_sample_size","initial_batch_sample_percentage",b"initial_batch_sample_percentage","initial_batch_sample_size",b"initial_batch_sample_size","sample_strategy",b"sample_strategy"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["following_batch_sample_size",b"following_batch_sample_size"]) -> typing.Optional[typing_extensions.Literal["following_batch_sample_percentage"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["initial_batch_sample_size",b"initial_batch_sample_size"]) -> typing.Optional[typing_extensions.Literal["initial_batch_sample_percentage"]]: ...
global___SampleConfig = SampleConfig

class TrainingConfig(google.protobuf.message.Message):
    """CMLE training config. For every active learning labeling iteration, system
    will train a machine learning model on CMLE. The trained model will be used
    by data sampling algorithm to select DataItems.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIMEOUT_TRAINING_MILLI_HOURS_FIELD_NUMBER: builtins.int
    timeout_training_milli_hours: builtins.int = ...
    """The timeout hours for the CMLE training job, expressed in milli hours
    i.e. 1,000 value in this field means 1 hour.
    """

    def __init__(self,
        *,
        timeout_training_milli_hours : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["timeout_training_milli_hours",b"timeout_training_milli_hours"]) -> None: ...
global___TrainingConfig = TrainingConfig
