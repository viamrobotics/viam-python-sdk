"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.devtools.resultstore.v2.common_pb2
import google.devtools.resultstore.v2.file_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ConfiguredTarget(google.protobuf.message.Message):
    """Each ConfiguredTarget represents data for a given configuration of a given
    target in a given Invocation.
    Every ConfiguredTarget should have at least one Action as a child resource
    before the invocation is finalized. Refer to the Action's documentation for
    more info on this.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Id(google.protobuf.message.Message):
        """The resource ID components that identify the ConfiguredTarget."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        INVOCATION_ID_FIELD_NUMBER: builtins.int
        TARGET_ID_FIELD_NUMBER: builtins.int
        CONFIGURATION_ID_FIELD_NUMBER: builtins.int
        invocation_id: typing.Text = ...
        """The Invocation ID."""

        target_id: typing.Text = ...
        """The Target ID."""

        configuration_id: typing.Text = ...
        """The Configuration ID."""

        def __init__(self,
            *,
            invocation_id : typing.Text = ...,
            target_id : typing.Text = ...,
            configuration_id : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["configuration_id",b"configuration_id","invocation_id",b"invocation_id","target_id",b"target_id"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    STATUS_ATTRIBUTES_FIELD_NUMBER: builtins.int
    TIMING_FIELD_NUMBER: builtins.int
    TEST_ATTRIBUTES_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    FILES_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource name.  Its format must be:
    invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIG_ID)}
    where ${CONFIG_ID} must match the ID of an existing Configuration under
    this Invocation.
    """

    @property
    def id(self) -> global___ConfiguredTarget.Id:
        """The resource ID components that identify the ConfiguredTarget. They must
        match the resource name after proper encoding.
        """
        pass
    @property
    def status_attributes(self) -> google.devtools.resultstore.v2.common_pb2.StatusAttributes:
        """The aggregate status for this configuration of this target. If testing
        was not requested, set this to the build status (e.g. BUILT or
        FAILED_TO_BUILD).
        """
        pass
    @property
    def timing(self) -> google.devtools.resultstore.v2.common_pb2.Timing:
        """Captures the start time and duration of this configured target."""
        pass
    @property
    def test_attributes(self) -> global___ConfiguredTestAttributes:
        """Test specific attributes for this ConfiguredTarget."""
        pass
    @property
    def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.devtools.resultstore.v2.common_pb2.Property]:
        """Arbitrary name-value pairs.
        This is implemented as a multi-map. Multiple properties are allowed with
        the same key. Properties will be returned in lexicographical order by key.
        """
        pass
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.devtools.resultstore.v2.file_pb2.File]:
        """A list of file references for configured target level files.
        The file IDs must be unique within this list. Duplicate file IDs will
        result in an error. Files will be returned in lexicographical order by ID.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        id : typing.Optional[global___ConfiguredTarget.Id] = ...,
        status_attributes : typing.Optional[google.devtools.resultstore.v2.common_pb2.StatusAttributes] = ...,
        timing : typing.Optional[google.devtools.resultstore.v2.common_pb2.Timing] = ...,
        test_attributes : typing.Optional[global___ConfiguredTestAttributes] = ...,
        properties : typing.Optional[typing.Iterable[google.devtools.resultstore.v2.common_pb2.Property]] = ...,
        files : typing.Optional[typing.Iterable[google.devtools.resultstore.v2.file_pb2.File]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id",b"id","status_attributes",b"status_attributes","test_attributes",b"test_attributes","timing",b"timing"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["files",b"files","id",b"id","name",b"name","properties",b"properties","status_attributes",b"status_attributes","test_attributes",b"test_attributes","timing",b"timing"]) -> None: ...
global___ConfiguredTarget = ConfiguredTarget

class ConfiguredTestAttributes(google.protobuf.message.Message):
    """Attributes that apply only to test actions under this configured target."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_RUN_COUNT_FIELD_NUMBER: builtins.int
    TOTAL_SHARD_COUNT_FIELD_NUMBER: builtins.int
    TIMEOUT_DURATION_FIELD_NUMBER: builtins.int
    total_run_count: builtins.int = ...
    """Total number of test runs. For example, in bazel this is specified with
    --runs_per_test. Zero if runs_per_test is not used.
    """

    total_shard_count: builtins.int = ...
    """Total number of test shards. Zero if shard count was not specified."""

    @property
    def timeout_duration(self) -> google.protobuf.duration_pb2.Duration:
        """How long test is allowed to run."""
        pass
    def __init__(self,
        *,
        total_run_count : builtins.int = ...,
        total_shard_count : builtins.int = ...,
        timeout_duration : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timeout_duration",b"timeout_duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["timeout_duration",b"timeout_duration","total_run_count",b"total_run_count","total_shard_count",b"total_shard_count"]) -> None: ...
global___ConfiguredTestAttributes = ConfiguredTestAttributes
