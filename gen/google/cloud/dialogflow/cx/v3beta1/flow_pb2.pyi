"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.dialogflow.cx.v3beta1.page_pb2
import google.cloud.dialogflow.cx.v3beta1.validation_message_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class NluSettings(google.protobuf.message.Message):
    """Settings related to NLU."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ModelType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ModelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ModelType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        MODEL_TYPE_UNSPECIFIED: NluSettings.ModelType.ValueType = ...  # 0
        """Not specified. `MODEL_TYPE_STANDARD` will be used."""

        MODEL_TYPE_STANDARD: NluSettings.ModelType.ValueType = ...  # 1
        """Use standard NLU model."""

        MODEL_TYPE_ADVANCED: NluSettings.ModelType.ValueType = ...  # 3
        """Use advanced NLU model."""

    class ModelType(_ModelType, metaclass=_ModelTypeEnumTypeWrapper):
        """NLU model type."""
        pass

    MODEL_TYPE_UNSPECIFIED: NluSettings.ModelType.ValueType = ...  # 0
    """Not specified. `MODEL_TYPE_STANDARD` will be used."""

    MODEL_TYPE_STANDARD: NluSettings.ModelType.ValueType = ...  # 1
    """Use standard NLU model."""

    MODEL_TYPE_ADVANCED: NluSettings.ModelType.ValueType = ...  # 3
    """Use advanced NLU model."""


    class _ModelTrainingMode:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ModelTrainingModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ModelTrainingMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        MODEL_TRAINING_MODE_UNSPECIFIED: NluSettings.ModelTrainingMode.ValueType = ...  # 0
        """Not specified. `MODEL_TRAINING_MODE_AUTOMATIC` will be used."""

        MODEL_TRAINING_MODE_AUTOMATIC: NluSettings.ModelTrainingMode.ValueType = ...  # 1
        """NLU model training is automatically triggered when a flow gets modified.
        User can also manually trigger model training in this mode.
        """

        MODEL_TRAINING_MODE_MANUAL: NluSettings.ModelTrainingMode.ValueType = ...  # 2
        """User needs to manually trigger NLU model training. Best for large flows
        whose models take long time to train.
        """

    class ModelTrainingMode(_ModelTrainingMode, metaclass=_ModelTrainingModeEnumTypeWrapper):
        """NLU model training mode."""
        pass

    MODEL_TRAINING_MODE_UNSPECIFIED: NluSettings.ModelTrainingMode.ValueType = ...  # 0
    """Not specified. `MODEL_TRAINING_MODE_AUTOMATIC` will be used."""

    MODEL_TRAINING_MODE_AUTOMATIC: NluSettings.ModelTrainingMode.ValueType = ...  # 1
    """NLU model training is automatically triggered when a flow gets modified.
    User can also manually trigger model training in this mode.
    """

    MODEL_TRAINING_MODE_MANUAL: NluSettings.ModelTrainingMode.ValueType = ...  # 2
    """User needs to manually trigger NLU model training. Best for large flows
    whose models take long time to train.
    """


    MODEL_TYPE_FIELD_NUMBER: builtins.int
    CLASSIFICATION_THRESHOLD_FIELD_NUMBER: builtins.int
    MODEL_TRAINING_MODE_FIELD_NUMBER: builtins.int
    model_type: global___NluSettings.ModelType.ValueType = ...
    """Indicates the type of NLU model."""

    classification_threshold: builtins.float = ...
    """To filter out false positive results and still get variety in matched
    natural language inputs for your agent, you can tune the machine learning
    classification threshold. If the returned score value is less than the
    threshold value, then a no-match event will be triggered. The score values
    range from 0.0 (completely uncertain) to 1.0 (completely certain). If set
    to 0.0, the default of 0.3 is used.
    """

    model_training_mode: global___NluSettings.ModelTrainingMode.ValueType = ...
    """Indicates NLU model training mode."""

    def __init__(self,
        *,
        model_type : global___NluSettings.ModelType.ValueType = ...,
        classification_threshold : builtins.float = ...,
        model_training_mode : global___NluSettings.ModelTrainingMode.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["classification_threshold",b"classification_threshold","model_training_mode",b"model_training_mode","model_type",b"model_type"]) -> None: ...
global___NluSettings = NluSettings

class Flow(google.protobuf.message.Message):
    """Flows represents the conversation flows when you build your chatbot agent.

    A flow consists of many pages connected by the transition routes.
    Conversations always start with the built-in Start Flow (with an all-0 ID).
    Transition routes can direct the conversation session from the current flow
    (parent flow) to another flow (sub flow). When the sub flow is finished,
    Dialogflow will bring the session back to the parent flow, where the sub flow
    is started.

    Usually, when a transition route is followed by a matched intent, the intent
    will be "consumed". This means the intent won't activate more transition
    routes. However, when the followed transition route moves the conversation
    session into a different flow, the matched intent can be carried over and to
    be consumed in the target flow.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TRANSITION_ROUTES_FIELD_NUMBER: builtins.int
    EVENT_HANDLERS_FIELD_NUMBER: builtins.int
    TRANSITION_ROUTE_GROUPS_FIELD_NUMBER: builtins.int
    NLU_SETTINGS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The unique identifier of the flow.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    display_name: typing.Text = ...
    """Required. The human-readable name of the flow."""

    description: typing.Text = ...
    """The description of the flow. The maximum length is 500 characters. If
    exceeded, the request is rejected.
    """

    @property
    def transition_routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.dialogflow.cx.v3beta1.page_pb2.TransitionRoute]:
        """A flow's transition routes serve two purposes:

        *   They are responsible for matching the user's first utterances in the
        flow.
        *   They are inherited by every page's [transition
        routes][Page.transition_routes] and can support use cases such as the user
        saying "help" or "can I talk to a human?", which can be handled in a common
        way regardless of the current page. Transition routes defined in the page
        have higher priority than those defined in the flow.

        TransitionRoutes are evalauted in the following order:

        *   TransitionRoutes with intent specified..
        *   TransitionRoutes with only condition specified.

        TransitionRoutes with intent specified are inherited by pages in the flow.
        """
        pass
    @property
    def event_handlers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.dialogflow.cx.v3beta1.page_pb2.EventHandler]:
        """A flow's event handlers serve two purposes:

        *   They are responsible for handling events (e.g. no match,
        webhook errors) in the flow.
        *   They are inherited by every page's [event
        handlers][Page.event_handlers], which can be used to handle common events
        regardless of the current page. Event handlers defined in the page
        have higher priority than those defined in the flow.

        Unlike [transition_routes][google.cloud.dialogflow.cx.v3beta1.Flow.transition_routes], these handlers are
        evaluated on a first-match basis. The first one that matches the event
        get executed, with the rest being ignored.
        """
        pass
    @property
    def transition_route_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """A flow's transition route group serve two purposes:

        *   They are responsible for matching the user's first utterances in the
        flow.
        *   They are inherited by every page's [transition
        route groups][Page.transition_route_groups]. Transition route groups
        defined in the page have higher priority than those defined in the flow.

        Format:`projects/<Project ID>/locations/<Location ID>/agents/<Agent
        ID>/flows/<Flow ID>/transitionRouteGroups/<TransitionRouteGroup ID>`.
        """
        pass
    @property
    def nlu_settings(self) -> global___NluSettings:
        """NLU related settings of the flow."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        description : typing.Text = ...,
        transition_routes : typing.Optional[typing.Iterable[google.cloud.dialogflow.cx.v3beta1.page_pb2.TransitionRoute]] = ...,
        event_handlers : typing.Optional[typing.Iterable[google.cloud.dialogflow.cx.v3beta1.page_pb2.EventHandler]] = ...,
        transition_route_groups : typing.Optional[typing.Iterable[typing.Text]] = ...,
        nlu_settings : typing.Optional[global___NluSettings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["nlu_settings",b"nlu_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","display_name",b"display_name","event_handlers",b"event_handlers","name",b"name","nlu_settings",b"nlu_settings","transition_route_groups",b"transition_route_groups","transition_routes",b"transition_routes"]) -> None: ...
global___Flow = Flow

class CreateFlowRequest(google.protobuf.message.Message):
    """The request message for [Flows.CreateFlow][google.cloud.dialogflow.cx.v3beta1.Flows.CreateFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FLOW_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The agent to create a flow for.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>`.
    """

    @property
    def flow(self) -> global___Flow:
        """Required. The flow to create."""
        pass
    language_code: typing.Text = ...
    """The language of the following fields in `flow`:

    *  `Flow.event_handlers.trigger_fulfillment.messages`
    *  `Flow.event_handlers.trigger_fulfillment.conditional_cases`
    *  `Flow.transition_routes.trigger_fulfillment.messages`
    *  `Flow.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        flow : typing.Optional[global___Flow] = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["flow",b"flow"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["flow",b"flow","language_code",b"language_code","parent",b"parent"]) -> None: ...
global___CreateFlowRequest = CreateFlowRequest

class DeleteFlowRequest(google.protobuf.message.Message):
    """The request message for [Flows.DeleteFlow][google.cloud.dialogflow.cx.v3beta1.Flows.DeleteFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FORCE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the flow to delete.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    force: builtins.bool = ...
    """This field has no effect for flows with no incoming transitions.
    For flows with incoming transitions:

    *  If `force` is set to false, an error will be returned with message
       indicating the incoming transitions.
    *  If `force` is set to true, Dialogflow will remove the flow, as well as
       any transitions to the flow (i.e. [Target
       flow][EventHandler.target_flow] in event handlers or [Target
       flow][TransitionRoute.target_flow] in transition routes that point to
       this flow will be cleared).
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        force : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["force",b"force","name",b"name"]) -> None: ...
global___DeleteFlowRequest = DeleteFlowRequest

class ListFlowsRequest(google.protobuf.message.Message):
    """The request message for [Flows.ListFlows][google.cloud.dialogflow.cx.v3beta1.Flows.ListFlows]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The agent containing the flows.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>`.
    """

    page_size: builtins.int = ...
    """The maximum number of items to return in a single page. By default 100 and
    at most 1000.
    """

    page_token: typing.Text = ...
    """The next_page_token value returned from a previous list request."""

    language_code: typing.Text = ...
    """The language to list flows for. The following fields are language
    dependent:

    *  `Flow.event_handlers.trigger_fulfillment.messages`
    *  `Flow.event_handlers.trigger_fulfillment.conditional_cases`
    *  `Flow.transition_routes.trigger_fulfillment.messages`
    *  `Flow.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListFlowsRequest = ListFlowsRequest

class ListFlowsResponse(google.protobuf.message.Message):
    """The response message for [Flows.ListFlows][google.cloud.dialogflow.cx.v3beta1.Flows.ListFlows]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FLOWS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def flows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Flow]:
        """The list of flows. There will be a maximum number of items returned based
        on the page_size field in the request.
        """
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results, or empty if there are no more
    results in the list.
    """

    def __init__(self,
        *,
        flows : typing.Optional[typing.Iterable[global___Flow]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["flows",b"flows","next_page_token",b"next_page_token"]) -> None: ...
global___ListFlowsResponse = ListFlowsResponse

class GetFlowRequest(google.protobuf.message.Message):
    """The response message for [Flows.GetFlow][google.cloud.dialogflow.cx.v3beta1.Flows.GetFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the flow to get.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    language_code: typing.Text = ...
    """The language to retrieve the flow for. The following fields are language
    dependent:

    *  `Flow.event_handlers.trigger_fulfillment.messages`
    *  `Flow.event_handlers.trigger_fulfillment.conditional_cases`
    *  `Flow.transition_routes.trigger_fulfillment.messages`
    *  `Flow.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","name",b"name"]) -> None: ...
global___GetFlowRequest = GetFlowRequest

class UpdateFlowRequest(google.protobuf.message.Message):
    """The request message for [Flows.UpdateFlow][google.cloud.dialogflow.cx.v3beta1.Flows.UpdateFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FLOW_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    @property
    def flow(self) -> global___Flow:
        """Required. The flow to update."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The mask to control which fields get updated. If the mask is not present,
        all fields will be updated.
        """
        pass
    language_code: typing.Text = ...
    """The language of the following fields in `flow`:

    *  `Flow.event_handlers.trigger_fulfillment.messages`
    *  `Flow.event_handlers.trigger_fulfillment.conditional_cases`
    *  `Flow.transition_routes.trigger_fulfillment.messages`
    *  `Flow.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    def __init__(self,
        *,
        flow : typing.Optional[global___Flow] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["flow",b"flow","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["flow",b"flow","language_code",b"language_code","update_mask",b"update_mask"]) -> None: ...
global___UpdateFlowRequest = UpdateFlowRequest

class TrainFlowRequest(google.protobuf.message.Message):
    """The request message for [Flows.TrainFlow][google.cloud.dialogflow.cx.v3beta1.Flows.TrainFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The flow to train.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___TrainFlowRequest = TrainFlowRequest

class ValidateFlowRequest(google.protobuf.message.Message):
    """The request message for [Flows.ValidateFlow][google.cloud.dialogflow.cx.v3beta1.Flows.ValidateFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The flow to validate.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    language_code: typing.Text = ...
    """If not specified, the agent's default language is used."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","name",b"name"]) -> None: ...
global___ValidateFlowRequest = ValidateFlowRequest

class GetFlowValidationResultRequest(google.protobuf.message.Message):
    """The request message for [Flows.GetFlowValidationResult][google.cloud.dialogflow.cx.v3beta1.Flows.GetFlowValidationResult]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The flow name.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/validationResult`.
    """

    language_code: typing.Text = ...
    """If not specified, the agent's default language is used."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","name",b"name"]) -> None: ...
global___GetFlowValidationResultRequest = GetFlowValidationResultRequest

class FlowValidationResult(google.protobuf.message.Message):
    """The response message for [Flows.GetFlowValidationResult][google.cloud.dialogflow.cx.v3beta1.Flows.GetFlowValidationResult]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VALIDATION_MESSAGES_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The unique identifier of the flow validation result.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/validationResult`.
    """

    @property
    def validation_messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.dialogflow.cx.v3beta1.validation_message_pb2.ValidationMessage]:
        """Contains all validation messages."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Last time the flow was validated."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        validation_messages : typing.Optional[typing.Iterable[google.cloud.dialogflow.cx.v3beta1.validation_message_pb2.ValidationMessage]] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","update_time",b"update_time","validation_messages",b"validation_messages"]) -> None: ...
global___FlowValidationResult = FlowValidationResult

class ImportFlowRequest(google.protobuf.message.Message):
    """The request message for [Flows.ImportFlow][google.cloud.dialogflow.cx.v3beta1.Flows.ImportFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ImportOption:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ImportOptionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ImportOption.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        IMPORT_OPTION_UNSPECIFIED: ImportFlowRequest.ImportOption.ValueType = ...  # 0
        """Unspecified. Treated as `KEEP`."""

        KEEP: ImportFlowRequest.ImportOption.ValueType = ...  # 1
        """Always respect settings in exported flow content. It may cause a
        import failure if some settings (e.g. custom NLU) are not supported in
        the agent to import into.
        """

        FALLBACK: ImportFlowRequest.ImportOption.ValueType = ...  # 2
        """Fallback to default settings if some settings are not supported in the
        agent to import into. E.g. Standard NLU will be used if custom NLU is
        not available.
        """

    class ImportOption(_ImportOption, metaclass=_ImportOptionEnumTypeWrapper):
        """Import option."""
        pass

    IMPORT_OPTION_UNSPECIFIED: ImportFlowRequest.ImportOption.ValueType = ...  # 0
    """Unspecified. Treated as `KEEP`."""

    KEEP: ImportFlowRequest.ImportOption.ValueType = ...  # 1
    """Always respect settings in exported flow content. It may cause a
    import failure if some settings (e.g. custom NLU) are not supported in
    the agent to import into.
    """

    FALLBACK: ImportFlowRequest.ImportOption.ValueType = ...  # 2
    """Fallback to default settings if some settings are not supported in the
    agent to import into. E.g. Standard NLU will be used if custom NLU is
    not available.
    """


    PARENT_FIELD_NUMBER: builtins.int
    FLOW_URI_FIELD_NUMBER: builtins.int
    FLOW_CONTENT_FIELD_NUMBER: builtins.int
    IMPORT_OPTION_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The agent to import the flow into.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>`.
    """

    flow_uri: typing.Text = ...
    """The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI
    to import flow from. The format of this URI must be
    `gs://<bucket-name>/<object-name>`.
    """

    flow_content: builtins.bytes = ...
    """Uncompressed raw byte content for flow."""

    import_option: global___ImportFlowRequest.ImportOption.ValueType = ...
    """Flow import mode. If not specified, `KEEP` is assumed."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        flow_uri : typing.Text = ...,
        flow_content : builtins.bytes = ...,
        import_option : global___ImportFlowRequest.ImportOption.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["flow",b"flow","flow_content",b"flow_content","flow_uri",b"flow_uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["flow",b"flow","flow_content",b"flow_content","flow_uri",b"flow_uri","import_option",b"import_option","parent",b"parent"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["flow",b"flow"]) -> typing.Optional[typing_extensions.Literal["flow_uri","flow_content"]]: ...
global___ImportFlowRequest = ImportFlowRequest

class ImportFlowResponse(google.protobuf.message.Message):
    """The response message for [Flows.ImportFlow][google.cloud.dialogflow.cx.v3beta1.Flows.ImportFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FLOW_FIELD_NUMBER: builtins.int
    flow: typing.Text = ...
    """The unique identifier of the new flow.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    def __init__(self,
        *,
        flow : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["flow",b"flow"]) -> None: ...
global___ImportFlowResponse = ImportFlowResponse

class ExportFlowRequest(google.protobuf.message.Message):
    """The request message for [Flows.ExportFlow][google.cloud.dialogflow.cx.v3beta1.Flows.ExportFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FLOW_URI_FIELD_NUMBER: builtins.int
    INCLUDE_REFERENCED_FLOWS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the flow to export.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    flow_uri: typing.Text = ...
    """Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to
    export the flow to. The format of this URI must be
    `gs://<bucket-name>/<object-name>`.
    If left unspecified, the serialized flow is returned inline.
    """

    include_referenced_flows: builtins.bool = ...
    """Optional. Whether to export flows referenced by the specified flow."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        flow_uri : typing.Text = ...,
        include_referenced_flows : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["flow_uri",b"flow_uri","include_referenced_flows",b"include_referenced_flows","name",b"name"]) -> None: ...
global___ExportFlowRequest = ExportFlowRequest

class ExportFlowResponse(google.protobuf.message.Message):
    """The response message for [Flows.ExportFlow][google.cloud.dialogflow.cx.v3beta1.Flows.ExportFlow]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FLOW_URI_FIELD_NUMBER: builtins.int
    FLOW_CONTENT_FIELD_NUMBER: builtins.int
    flow_uri: typing.Text = ...
    """The URI to a file containing the exported flow. This field is populated
    only if `flow_uri` is specified in [ExportFlowRequest][google.cloud.dialogflow.cx.v3beta1.ExportFlowRequest].
    """

    flow_content: builtins.bytes = ...
    """Uncompressed raw byte content for flow."""

    def __init__(self,
        *,
        flow_uri : typing.Text = ...,
        flow_content : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["flow",b"flow","flow_content",b"flow_content","flow_uri",b"flow_uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["flow",b"flow","flow_content",b"flow_content","flow_uri",b"flow_uri"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["flow",b"flow"]) -> typing.Optional[typing_extensions.Literal["flow_uri","flow_content"]]: ...
global___ExportFlowResponse = ExportFlowResponse
