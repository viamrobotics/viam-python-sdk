"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Agent(google.protobuf.message.Message):
    """A Dialogflow agent is a virtual agent that handles conversations with your
    end-users. It is a natural language understanding module that understands the
    nuances of human language. Dialogflow translates end-user text or audio
    during a conversation to structured data that your apps and services can
    understand. You design and build a Dialogflow agent to handle the types of
    conversations required for your system.

    For more information about agents, see the
    [Agent guide](https://cloud.google.com/dialogflow/docs/agents-overview).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _MatchMode:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _MatchModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MatchMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        MATCH_MODE_UNSPECIFIED: Agent.MatchMode.ValueType = ...  # 0
        """Not specified."""

        MATCH_MODE_HYBRID: Agent.MatchMode.ValueType = ...  # 1
        """Best for agents with a small number of examples in intents and/or wide
        use of templates syntax and composite entities.
        """

        MATCH_MODE_ML_ONLY: Agent.MatchMode.ValueType = ...  # 2
        """Can be used for agents with a large number of examples in intents,
        especially the ones using @sys.any or very large custom entities.
        """

    class MatchMode(_MatchMode, metaclass=_MatchModeEnumTypeWrapper):
        """Match mode determines how intents are detected from user queries."""
        pass

    MATCH_MODE_UNSPECIFIED: Agent.MatchMode.ValueType = ...  # 0
    """Not specified."""

    MATCH_MODE_HYBRID: Agent.MatchMode.ValueType = ...  # 1
    """Best for agents with a small number of examples in intents and/or wide
    use of templates syntax and composite entities.
    """

    MATCH_MODE_ML_ONLY: Agent.MatchMode.ValueType = ...  # 2
    """Can be used for agents with a large number of examples in intents,
    especially the ones using @sys.any or very large custom entities.
    """


    class _ApiVersion:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ApiVersionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ApiVersion.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        API_VERSION_UNSPECIFIED: Agent.ApiVersion.ValueType = ...  # 0
        """Not specified."""

        API_VERSION_V1: Agent.ApiVersion.ValueType = ...  # 1
        """Legacy V1 API."""

        API_VERSION_V2: Agent.ApiVersion.ValueType = ...  # 2
        """V2 API."""

        API_VERSION_V2_BETA_1: Agent.ApiVersion.ValueType = ...  # 3
        """V2beta1 API."""

    class ApiVersion(_ApiVersion, metaclass=_ApiVersionEnumTypeWrapper):
        """API version for the agent."""
        pass

    API_VERSION_UNSPECIFIED: Agent.ApiVersion.ValueType = ...  # 0
    """Not specified."""

    API_VERSION_V1: Agent.ApiVersion.ValueType = ...  # 1
    """Legacy V1 API."""

    API_VERSION_V2: Agent.ApiVersion.ValueType = ...  # 2
    """V2 API."""

    API_VERSION_V2_BETA_1: Agent.ApiVersion.ValueType = ...  # 3
    """V2beta1 API."""


    class _Tier:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TierEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Tier.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TIER_UNSPECIFIED: Agent.Tier.ValueType = ...  # 0
        """Not specified. This value should never be used."""

        TIER_STANDARD: Agent.Tier.ValueType = ...  # 1
        """Trial Edition, previously known as Standard Edition."""

        TIER_ENTERPRISE: Agent.Tier.ValueType = ...  # 2
        """Essentials Edition, previously known as Enterprise Essential Edition."""

        TIER_ENTERPRISE_PLUS: Agent.Tier.ValueType = ...  # 3
        """Essentials Edition (same as TIER_ENTERPRISE), previously known as
        Enterprise Plus Edition.
        """

    class Tier(_Tier, metaclass=_TierEnumTypeWrapper):
        """Represents the agent tier."""
        pass

    TIER_UNSPECIFIED: Agent.Tier.ValueType = ...  # 0
    """Not specified. This value should never be used."""

    TIER_STANDARD: Agent.Tier.ValueType = ...  # 1
    """Trial Edition, previously known as Standard Edition."""

    TIER_ENTERPRISE: Agent.Tier.ValueType = ...  # 2
    """Essentials Edition, previously known as Enterprise Essential Edition."""

    TIER_ENTERPRISE_PLUS: Agent.Tier.ValueType = ...  # 3
    """Essentials Edition (same as TIER_ENTERPRISE), previously known as
    Enterprise Plus Edition.
    """


    PARENT_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DEFAULT_LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    SUPPORTED_LANGUAGE_CODES_FIELD_NUMBER: builtins.int
    TIME_ZONE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    AVATAR_URI_FIELD_NUMBER: builtins.int
    ENABLE_LOGGING_FIELD_NUMBER: builtins.int
    MATCH_MODE_FIELD_NUMBER: builtins.int
    CLASSIFICATION_THRESHOLD_FIELD_NUMBER: builtins.int
    API_VERSION_FIELD_NUMBER: builtins.int
    TIER_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project of this agent.
    Format: `projects/<Project ID>`.
    """

    display_name: typing.Text = ...
    """Required. The name of this agent."""

    default_language_code: typing.Text = ...
    """Required. The default language of the agent as a language tag. See
    [Language
    Support](https://cloud.google.com/dialogflow/docs/reference/language)
    for a list of the currently supported language codes. This field cannot be
    set by the `Update` method.
    """

    @property
    def supported_language_codes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Optional. The list of all languages supported by this agent (except for the
        `default_language_code`).
        """
        pass
    time_zone: typing.Text = ...
    """Required. The time zone of this agent from the
    [time zone database](https://www.iana.org/time-zones), e.g.,
    America/New_York, Europe/Paris.
    """

    description: typing.Text = ...
    """Optional. The description of this agent.
    The maximum length is 500 characters. If exceeded, the request is rejected.
    """

    avatar_uri: typing.Text = ...
    """Optional. The URI of the agent's avatar.
    Avatars are used throughout the Dialogflow console and in the self-hosted
    [Web
    Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo)
    integration.
    """

    enable_logging: builtins.bool = ...
    """Optional. Determines whether this agent should log conversation queries."""

    match_mode: global___Agent.MatchMode.ValueType = ...
    """Optional. Determines how intents are detected from user queries."""

    classification_threshold: builtins.float = ...
    """Optional. To filter out false positive results and still get variety in
    matched natural language inputs for your agent, you can tune the machine
    learning classification threshold. If the returned score value is less than
    the threshold value, then a fallback intent will be triggered or, if there
    are no fallback intents defined, no intent will be triggered. The score
    values range from 0.0 (completely uncertain) to 1.0 (completely certain).
    If set to 0.0, the default of 0.3 is used.
    """

    api_version: global___Agent.ApiVersion.ValueType = ...
    """Optional. API version displayed in Dialogflow console. If not specified,
    V2 API is assumed. Clients are free to query different service endpoints
    for different API versions. However, bots connectors and webhook calls will
    follow the specified API version.
    """

    tier: global___Agent.Tier.ValueType = ...
    """Optional. The agent tier. If not specified, TIER_STANDARD is assumed."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        display_name : typing.Text = ...,
        default_language_code : typing.Text = ...,
        supported_language_codes : typing.Optional[typing.Iterable[typing.Text]] = ...,
        time_zone : typing.Text = ...,
        description : typing.Text = ...,
        avatar_uri : typing.Text = ...,
        enable_logging : builtins.bool = ...,
        match_mode : global___Agent.MatchMode.ValueType = ...,
        classification_threshold : builtins.float = ...,
        api_version : global___Agent.ApiVersion.ValueType = ...,
        tier : global___Agent.Tier.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version",b"api_version","avatar_uri",b"avatar_uri","classification_threshold",b"classification_threshold","default_language_code",b"default_language_code","description",b"description","display_name",b"display_name","enable_logging",b"enable_logging","match_mode",b"match_mode","parent",b"parent","supported_language_codes",b"supported_language_codes","tier",b"tier","time_zone",b"time_zone"]) -> None: ...
global___Agent = Agent

class GetAgentRequest(google.protobuf.message.Message):
    """The request message for [Agents.GetAgent][google.cloud.dialogflow.v2.Agents.GetAgent]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project that the agent to fetch is associated with.
    Format: `projects/<Project ID>`.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent"]) -> None: ...
global___GetAgentRequest = GetAgentRequest

class SetAgentRequest(google.protobuf.message.Message):
    """The request message for [Agents.SetAgent][google.cloud.dialogflow.v2.Agents.SetAgent]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AGENT_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def agent(self) -> global___Agent:
        """Required. The agent to update."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""
        pass
    def __init__(self,
        *,
        agent : typing.Optional[global___Agent] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["agent",b"agent","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["agent",b"agent","update_mask",b"update_mask"]) -> None: ...
global___SetAgentRequest = SetAgentRequest

class DeleteAgentRequest(google.protobuf.message.Message):
    """The request message for [Agents.DeleteAgent][google.cloud.dialogflow.v2.Agents.DeleteAgent]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project that the agent to delete is associated with.
    Format: `projects/<Project ID>`.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent"]) -> None: ...
global___DeleteAgentRequest = DeleteAgentRequest

class SearchAgentsRequest(google.protobuf.message.Message):
    """The request message for [Agents.SearchAgents][google.cloud.dialogflow.v2.Agents.SearchAgents]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project to list agents from.
    Format: `projects/<Project ID or '-'>`.
    """

    page_size: builtins.int = ...
    """Optional. The maximum number of items to return in a single page. By
    default 100 and at most 1000.
    """

    page_token: typing.Text = ...
    """The next_page_token value returned from a previous list request."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___SearchAgentsRequest = SearchAgentsRequest

class SearchAgentsResponse(google.protobuf.message.Message):
    """The response message for [Agents.SearchAgents][google.cloud.dialogflow.v2.Agents.SearchAgents]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AGENTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def agents(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Agent]:
        """The list of agents. There will be a maximum number of items returned based
        on the page_size field in the request.
        """
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        agents : typing.Optional[typing.Iterable[global___Agent]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["agents",b"agents","next_page_token",b"next_page_token"]) -> None: ...
global___SearchAgentsResponse = SearchAgentsResponse

class TrainAgentRequest(google.protobuf.message.Message):
    """The request message for [Agents.TrainAgent][google.cloud.dialogflow.v2.Agents.TrainAgent]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project that the agent to train is associated with.
    Format: `projects/<Project ID>`.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent"]) -> None: ...
global___TrainAgentRequest = TrainAgentRequest

class ExportAgentRequest(google.protobuf.message.Message):
    """The request message for [Agents.ExportAgent][google.cloud.dialogflow.v2.Agents.ExportAgent]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    AGENT_URI_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project that the agent to export is associated with.
    Format: `projects/<Project ID>`.
    """

    agent_uri: typing.Text = ...
    """Required. The [Google Cloud Storage](https://cloud.google.com/storage/docs/)
    URI to export the agent to.
    The format of this URI must be `gs://<bucket-name>/<object-name>`.
    If left unspecified, the serialized agent is returned inline.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        agent_uri : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["agent_uri",b"agent_uri","parent",b"parent"]) -> None: ...
global___ExportAgentRequest = ExportAgentRequest

class ExportAgentResponse(google.protobuf.message.Message):
    """The response message for [Agents.ExportAgent][google.cloud.dialogflow.v2.Agents.ExportAgent]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AGENT_URI_FIELD_NUMBER: builtins.int
    AGENT_CONTENT_FIELD_NUMBER: builtins.int
    agent_uri: typing.Text = ...
    """The URI to a file containing the exported agent. This field is populated
    only if `agent_uri` is specified in `ExportAgentRequest`.
    """

    agent_content: builtins.bytes = ...
    """Zip compressed raw byte content for agent."""

    def __init__(self,
        *,
        agent_uri : typing.Text = ...,
        agent_content : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["agent",b"agent","agent_content",b"agent_content","agent_uri",b"agent_uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["agent",b"agent","agent_content",b"agent_content","agent_uri",b"agent_uri"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["agent",b"agent"]) -> typing.Optional[typing_extensions.Literal["agent_uri","agent_content"]]: ...
global___ExportAgentResponse = ExportAgentResponse

class ImportAgentRequest(google.protobuf.message.Message):
    """The request message for [Agents.ImportAgent][google.cloud.dialogflow.v2.Agents.ImportAgent]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    AGENT_URI_FIELD_NUMBER: builtins.int
    AGENT_CONTENT_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project that the agent to import is associated with.
    Format: `projects/<Project ID>`.
    """

    agent_uri: typing.Text = ...
    """The URI to a Google Cloud Storage file containing the agent to import.
    Note: The URI must start with "gs://".
    """

    agent_content: builtins.bytes = ...
    """Zip compressed raw byte content for agent."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        agent_uri : typing.Text = ...,
        agent_content : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["agent",b"agent","agent_content",b"agent_content","agent_uri",b"agent_uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["agent",b"agent","agent_content",b"agent_content","agent_uri",b"agent_uri","parent",b"parent"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["agent",b"agent"]) -> typing.Optional[typing_extensions.Literal["agent_uri","agent_content"]]: ...
global___ImportAgentRequest = ImportAgentRequest

class RestoreAgentRequest(google.protobuf.message.Message):
    """The request message for [Agents.RestoreAgent][google.cloud.dialogflow.v2.Agents.RestoreAgent]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    AGENT_URI_FIELD_NUMBER: builtins.int
    AGENT_CONTENT_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project that the agent to restore is associated with.
    Format: `projects/<Project ID>`.
    """

    agent_uri: typing.Text = ...
    """The URI to a Google Cloud Storage file containing the agent to restore.
    Note: The URI must start with "gs://".
    """

    agent_content: builtins.bytes = ...
    """Zip compressed raw byte content for agent."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        agent_uri : typing.Text = ...,
        agent_content : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["agent",b"agent","agent_content",b"agent_content","agent_uri",b"agent_uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["agent",b"agent","agent_content",b"agent_content","agent_uri",b"agent_uri","parent",b"parent"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["agent",b"agent"]) -> typing.Optional[typing_extensions.Literal["agent_uri","agent_content"]]: ...
global___RestoreAgentRequest = RestoreAgentRequest

class GetValidationResultRequest(google.protobuf.message.Message):
    """The request message for [Agents.GetValidationResult][google.cloud.dialogflow.v2.Agents.GetValidationResult]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project that the agent is associated with.
    Format: `projects/<Project ID>`.
    """

    language_code: typing.Text = ...
    """Optional. The language for which you want a validation result. If not
    specified, the agent's default language is used. [Many
    languages](https://cloud.google.com/dialogflow/docs/reference/language)
    are supported. Note: languages must be enabled in the agent before they can
    be used.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","parent",b"parent"]) -> None: ...
global___GetValidationResultRequest = GetValidationResultRequest
