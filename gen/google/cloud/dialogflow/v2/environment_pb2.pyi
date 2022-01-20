"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.dialogflow.v2.audio_config_pb2
import google.cloud.dialogflow.v2.fulfillment_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Environment(google.protobuf.message.Message):
    """You can create multiple versions of your agent and publish them to separate
    environments.

    When you edit an agent, you are editing the draft agent. At any point, you
    can save the draft agent as an agent version, which is an immutable snapshot
    of your agent.

    When you save the draft agent, it is published to the default environment.
    When you create agent versions, you can publish them to custom environments.
    You can create a variety of custom environments for:

    - testing
    - development
    - production
    - etc.

    For more information, see the [versions and environments
    guide](https://cloud.google.com/dialogflow/docs/agents-versions).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: Environment.State.ValueType = ...  # 0
        """Not specified. This value is not used."""

        STOPPED: Environment.State.ValueType = ...  # 1
        """Stopped."""

        LOADING: Environment.State.ValueType = ...  # 2
        """Loading."""

        RUNNING: Environment.State.ValueType = ...  # 3
        """Running."""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Represents an environment state. When an environment is pointed to a new
        agent version, the environment is temporarily set to the `LOADING` state.
        During that time, the environment keeps on serving the previous version of
        the agent. After the new agent version is done loading, the environment is
        set back to the `RUNNING` state.
        """
        pass

    STATE_UNSPECIFIED: Environment.State.ValueType = ...  # 0
    """Not specified. This value is not used."""

    STOPPED: Environment.State.ValueType = ...  # 1
    """Stopped."""

    LOADING: Environment.State.ValueType = ...  # 2
    """Loading."""

    RUNNING: Environment.State.ValueType = ...  # 3
    """Running."""


    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    AGENT_VERSION_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    TEXT_TO_SPEECH_SETTINGS_FIELD_NUMBER: builtins.int
    FULFILLMENT_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The unique identifier of this agent environment.
    Supported formats:

    - `projects/<Project ID>/agent/environments/<Environment ID>`
    - `projects/<Project ID>/locations/<Location
      ID>/agent/environments/<Environment ID>`

    The environment ID for the default environment is `-`.
    """

    description: typing.Text = ...
    """Optional. The developer-provided description for this environment.
    The maximum length is 500 characters. If exceeded, the request is rejected.
    """

    agent_version: typing.Text = ...
    """Optional. The agent version loaded into this environment.
    Supported formats:

    - `projects/<Project ID>/agent/versions/<Version ID>`
    - `projects/<Project ID>/locations/<Location ID>/agent/versions/<Version
      ID>`
    """

    state: global___Environment.State.ValueType = ...
    """Output only. The state of this environment. This field is read-only, i.e., it cannot be
    set by create and update methods.
    """

    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The last update time of this environment. This field is read-only, i.e., it
        cannot be set by create and update methods.
        """
        pass
    @property
    def text_to_speech_settings(self) -> global___TextToSpeechSettings:
        """Optional. Text to speech settings for this environment."""
        pass
    @property
    def fulfillment(self) -> google.cloud.dialogflow.v2.fulfillment_pb2.Fulfillment:
        """Optional. The fulfillment settings to use for this environment."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        description : typing.Text = ...,
        agent_version : typing.Text = ...,
        state : global___Environment.State.ValueType = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        text_to_speech_settings : typing.Optional[global___TextToSpeechSettings] = ...,
        fulfillment : typing.Optional[google.cloud.dialogflow.v2.fulfillment_pb2.Fulfillment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fulfillment",b"fulfillment","text_to_speech_settings",b"text_to_speech_settings","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["agent_version",b"agent_version","description",b"description","fulfillment",b"fulfillment","name",b"name","state",b"state","text_to_speech_settings",b"text_to_speech_settings","update_time",b"update_time"]) -> None: ...
global___Environment = Environment

class TextToSpeechSettings(google.protobuf.message.Message):
    """Instructs the speech synthesizer on how to generate the output audio content."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class SynthesizeSpeechConfigsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> google.cloud.dialogflow.v2.audio_config_pb2.SynthesizeSpeechConfig: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[google.cloud.dialogflow.v2.audio_config_pb2.SynthesizeSpeechConfig] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ENABLE_TEXT_TO_SPEECH_FIELD_NUMBER: builtins.int
    OUTPUT_AUDIO_ENCODING_FIELD_NUMBER: builtins.int
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: builtins.int
    SYNTHESIZE_SPEECH_CONFIGS_FIELD_NUMBER: builtins.int
    enable_text_to_speech: builtins.bool = ...
    """Optional. Indicates whether text to speech is enabled. Even when this field is false,
    other settings in this proto are still retained.
    """

    output_audio_encoding: google.cloud.dialogflow.v2.audio_config_pb2.OutputAudioEncoding.ValueType = ...
    """Required. Audio encoding of the synthesized audio content."""

    sample_rate_hertz: builtins.int = ...
    """Optional. The synthesis sample rate (in hertz) for this audio. If not provided, then
    the synthesizer will use the default sample rate based on the audio
    encoding. If this is different from the voice's natural sample rate, then
    the synthesizer will honor this request by converting to the desired sample
    rate (which might result in worse audio quality).
    """

    @property
    def synthesize_speech_configs(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, google.cloud.dialogflow.v2.audio_config_pb2.SynthesizeSpeechConfig]:
        """Optional. Configuration of how speech should be synthesized, mapping from language
        (https://cloud.google.com/dialogflow/docs/reference/language) to
        SynthesizeSpeechConfig.
        """
        pass
    def __init__(self,
        *,
        enable_text_to_speech : builtins.bool = ...,
        output_audio_encoding : google.cloud.dialogflow.v2.audio_config_pb2.OutputAudioEncoding.ValueType = ...,
        sample_rate_hertz : builtins.int = ...,
        synthesize_speech_configs : typing.Optional[typing.Mapping[typing.Text, google.cloud.dialogflow.v2.audio_config_pb2.SynthesizeSpeechConfig]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enable_text_to_speech",b"enable_text_to_speech","output_audio_encoding",b"output_audio_encoding","sample_rate_hertz",b"sample_rate_hertz","synthesize_speech_configs",b"synthesize_speech_configs"]) -> None: ...
global___TextToSpeechSettings = TextToSpeechSettings

class ListEnvironmentsRequest(google.protobuf.message.Message):
    """The request message for [Environments.ListEnvironments][google.cloud.dialogflow.v2.Environments.ListEnvironments]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The agent to list all environments from.
    Format:

    - `projects/<Project ID>/agent`
    - `projects/<Project ID>/locations/<Location ID>/agent`
    """

    page_size: builtins.int = ...
    """Optional. The maximum number of items to return in a single page. By default 100 and
    at most 1000.
    """

    page_token: typing.Text = ...
    """Optional. The next_page_token value returned from a previous list request."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListEnvironmentsRequest = ListEnvironmentsRequest

class ListEnvironmentsResponse(google.protobuf.message.Message):
    """The response message for [Environments.ListEnvironments][google.cloud.dialogflow.v2.Environments.ListEnvironments]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENVIRONMENTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def environments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Environment]:
        """The list of agent environments. There will be a maximum number of items
        returned based on the page_size field in the request.
        """
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        environments : typing.Optional[typing.Iterable[global___Environment]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["environments",b"environments","next_page_token",b"next_page_token"]) -> None: ...
global___ListEnvironmentsResponse = ListEnvironmentsResponse

class GetEnvironmentRequest(google.protobuf.message.Message):
    """The request message for [Environments.GetEnvironment][google.cloud.dialogflow.v2.Environments.GetEnvironment]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the environment.
    Supported formats:

    - `projects/<Project ID>/agent/environments/<Environment ID>`
    - `projects/<Project ID>/locations/<Location
      ID>/agent/environments/<Environment ID>`

    The environment ID for the default environment is `-`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetEnvironmentRequest = GetEnvironmentRequest

class CreateEnvironmentRequest(google.protobuf.message.Message):
    """The request message for [Environments.CreateEnvironment][google.cloud.dialogflow.v2.Environments.CreateEnvironment]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    ENVIRONMENT_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The agent to create an environment for.
    Supported formats:

    - `projects/<Project ID>/agent`
    - `projects/<Project ID>/locations/<Location ID>/agent`
    """

    @property
    def environment(self) -> global___Environment:
        """Required. The environment to create."""
        pass
    environment_id: typing.Text = ...
    """Required. The unique id of the new environment."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        environment : typing.Optional[global___Environment] = ...,
        environment_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["environment",b"environment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["environment",b"environment","environment_id",b"environment_id","parent",b"parent"]) -> None: ...
global___CreateEnvironmentRequest = CreateEnvironmentRequest

class UpdateEnvironmentRequest(google.protobuf.message.Message):
    """The request message for [Environments.UpdateEnvironment][google.cloud.dialogflow.v2.Environments.UpdateEnvironment]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    ALLOW_LOAD_TO_DRAFT_AND_DISCARD_CHANGES_FIELD_NUMBER: builtins.int
    @property
    def environment(self) -> global___Environment:
        """Required. The environment to update."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Required. The mask to control which fields get updated."""
        pass
    allow_load_to_draft_and_discard_changes: builtins.bool = ...
    """Optional. This field is used to prevent accidental overwrite of the default
    environment, which is an operation that cannot be undone. To confirm that
    the caller desires this overwrite, this field must be explicitly set to
    true when updating the default environment (environment ID = `-`).
    """

    def __init__(self,
        *,
        environment : typing.Optional[global___Environment] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        allow_load_to_draft_and_discard_changes : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["environment",b"environment","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_load_to_draft_and_discard_changes",b"allow_load_to_draft_and_discard_changes","environment",b"environment","update_mask",b"update_mask"]) -> None: ...
global___UpdateEnvironmentRequest = UpdateEnvironmentRequest

class DeleteEnvironmentRequest(google.protobuf.message.Message):
    """The request message for [Environments.DeleteEnvironment][google.cloud.dialogflow.v2.Environments.DeleteEnvironment]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the environment to delete.
    / Format:

    - `projects/<Project ID>/agent/environments/<Environment ID>`
    - `projects/<Project ID>/locations/<Location
      ID>/agent/environments/<Environment ID>`

    The environment ID for the default environment is `-`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteEnvironmentRequest = DeleteEnvironmentRequest

class GetEnvironmentHistoryRequest(google.protobuf.message.Message):
    """The request message for [Environments.GetEnvironmentHistory][google.cloud.dialogflow.v2.Environments.GetEnvironmentHistory]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the environment to retrieve history for.
    Supported formats:

    - `projects/<Project ID>/agent/environments/<Environment ID>`
    - `projects/<Project ID>/locations/<Location
      ID>/agent/environments/<Environment ID>`

    The environment ID for the default environment is `-`.
    """

    page_size: builtins.int = ...
    """Optional. The maximum number of items to return in a single page. By default 100 and
    at most 1000.
    """

    page_token: typing.Text = ...
    """Optional. The next_page_token value returned from a previous list request."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___GetEnvironmentHistoryRequest = GetEnvironmentHistoryRequest

class EnvironmentHistory(google.protobuf.message.Message):
    """The response message for [Environments.GetEnvironmentHistory][google.cloud.dialogflow.v2.Environments.GetEnvironmentHistory]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Entry(google.protobuf.message.Message):
        """Represents an environment history entry."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        AGENT_VERSION_FIELD_NUMBER: builtins.int
        DESCRIPTION_FIELD_NUMBER: builtins.int
        CREATE_TIME_FIELD_NUMBER: builtins.int
        agent_version: typing.Text = ...
        """The agent version loaded into this environment history entry."""

        description: typing.Text = ...
        """The developer-provided description for this environment history entry."""

        @property
        def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """The creation time of this environment history entry."""
            pass
        def __init__(self,
            *,
            agent_version : typing.Text = ...,
            description : typing.Text = ...,
            create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["agent_version",b"agent_version","create_time",b"create_time","description",b"description"]) -> None: ...

    PARENT_FIELD_NUMBER: builtins.int
    ENTRIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Output only. The name of the environment this history is for.
    Supported formats:

    - `projects/<Project ID>/agent/environments/<Environment ID>`
    - `projects/<Project ID>/locations/<Location
       ID>/agent/environments/<Environment ID>`

    The environment ID for the default environment is `-`.
    """

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EnvironmentHistory.Entry]:
        """Output only. The list of agent environments. There will be a maximum number of items
        returned based on the page_size field in the request.
        """
        pass
    next_page_token: typing.Text = ...
    """Output only. Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        entries : typing.Optional[typing.Iterable[global___EnvironmentHistory.Entry]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entries",b"entries","next_page_token",b"next_page_token","parent",b"parent"]) -> None: ...
global___EnvironmentHistory = EnvironmentHistory
