"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Page(google.protobuf.message.Message):
    """A Dialogflow CX conversation (session) can be described and visualized as a
    state machine. The states of a CX session are represented by pages.

    For each flow, you define many pages, where your combined pages can handle a
    complete conversation on the topics the flow is designed for. At any given
    moment, exactly one page is the current page, the current page is considered
    active, and the flow associated with that page is considered active. Every
    flow has a special start page. When a flow initially becomes active, the
    start page page becomes the current page. For each conversational turn, the
    current page will either stay the same or transition to another page.

    You configure each page to collect information from the end-user that is
    relevant for the conversational state represented by the page.

    For more information, see the
    [Page guide](https://cloud.google.com/dialogflow/cx/docs/concept/page).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    ENTRY_FULFILLMENT_FIELD_NUMBER: builtins.int
    FORM_FIELD_NUMBER: builtins.int
    TRANSITION_ROUTE_GROUPS_FIELD_NUMBER: builtins.int
    TRANSITION_ROUTES_FIELD_NUMBER: builtins.int
    EVENT_HANDLERS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The unique identifier of the page.
    Required for the [Pages.UpdatePage][google.cloud.dialogflow.cx.v3beta1.Pages.UpdatePage] method. [Pages.CreatePage][google.cloud.dialogflow.cx.v3beta1.Pages.CreatePage]
    populates the name automatically.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/pages/<Page ID>`.
    """

    display_name: typing.Text = ...
    """Required. The human-readable name of the page, unique within the agent."""

    @property
    def entry_fulfillment(self) -> google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2.Fulfillment:
        """The fulfillment to call when the session is entering the page."""
        pass
    @property
    def form(self) -> global___Form:
        """The form associated with the page, used for collecting parameters
        relevant to the page.
        """
        pass
    @property
    def transition_route_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Ordered list of [`TransitionRouteGroups`][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup] associated
        with the page. Transition route groups must be unique within a page.

        *   If multiple transition routes within a page scope refer to the same
            intent, then the precedence order is: page's transition route -> page's
            transition route group -> flow's transition routes.

        *   If multiple transition route groups within a page contain the same
            intent, then the first group in the ordered list takes precedence.

        Format:`projects/<Project ID>/locations/<Location ID>/agents/<Agent
        ID>/flows/<Flow ID>/transitionRouteGroups/<TransitionRouteGroup ID>`.
        """
        pass
    @property
    def transition_routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TransitionRoute]:
        """A list of transitions for the transition rules of this page.
        They route the conversation to another page in the same flow, or another
        flow.

        When we are in a certain page, the TransitionRoutes are evalauted in the
        following order:

        *   TransitionRoutes defined in the page with intent specified.
        *   TransitionRoutes defined in the
            [transition route groups][google.cloud.dialogflow.cx.v3beta1.Page.transition_route_groups] with intent
            specified.
        *   TransitionRoutes defined in flow with intent specified.
        *   TransitionRoutes defined in the
            [transition route groups][google.cloud.dialogflow.cx.v3beta1.Flow.transition_route_groups] with intent
            specified.
        *   TransitionRoutes defined in the page with only condition specified.
        *   TransitionRoutes defined in the
            [transition route groups][google.cloud.dialogflow.cx.v3beta1.Page.transition_route_groups] with only
            condition specified.
        """
        pass
    @property
    def event_handlers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventHandler]:
        """Handlers associated with the page to handle events such as webhook errors,
        no match or no input.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        entry_fulfillment : typing.Optional[google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2.Fulfillment] = ...,
        form : typing.Optional[global___Form] = ...,
        transition_route_groups : typing.Optional[typing.Iterable[typing.Text]] = ...,
        transition_routes : typing.Optional[typing.Iterable[global___TransitionRoute]] = ...,
        event_handlers : typing.Optional[typing.Iterable[global___EventHandler]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entry_fulfillment",b"entry_fulfillment","form",b"form"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name","entry_fulfillment",b"entry_fulfillment","event_handlers",b"event_handlers","form",b"form","name",b"name","transition_route_groups",b"transition_route_groups","transition_routes",b"transition_routes"]) -> None: ...
global___Page = Page

class Form(google.protobuf.message.Message):
    """A form is a data model that groups related parameters that can be collected
    from the user. The process in which the agent prompts the user and collects
    parameter values from the user is called form filling. A form can be added to
    a [page][google.cloud.dialogflow.cx.v3beta1.Page]. When form filling is done, the filled parameters will be
    written to the [session][google.cloud.dialogflow.cx.v3beta1.SessionInfo.parameters].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Parameter(google.protobuf.message.Message):
        """Represents a form parameter."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class FillBehavior(google.protobuf.message.Message):
            """Configuration for how the filling of a parameter should be handled."""
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            INITIAL_PROMPT_FULFILLMENT_FIELD_NUMBER: builtins.int
            REPROMPT_EVENT_HANDLERS_FIELD_NUMBER: builtins.int
            @property
            def initial_prompt_fulfillment(self) -> google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2.Fulfillment:
                """Required. The fulfillment to provide the initial prompt that the agent
                can present to the user in order to fill the parameter.
                """
                pass
            @property
            def reprompt_event_handlers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventHandler]:
                """The handlers for parameter-level events, used to provide reprompt for
                the parameter or transition to a different page/flow. The supported
                events are:
                *   `sys.no-match-<N>`, where N can be from 1 to 6
                *   `sys.no-match-default`
                *   `sys.no-input-<N>`, where N can be from 1 to 6
                *   `sys.no-input-default`
                *   `sys.invalid-parameter`

                `initial_prompt_fulfillment` provides the first prompt for the
                parameter.

                If the user's response does not fill the parameter, a
                no-match/no-input event will be triggered, and the fulfillment
                associated with the `sys.no-match-1`/`sys.no-input-1` handler (if
                defined) will be called to provide a prompt. The
                `sys.no-match-2`/`sys.no-input-2` handler (if defined) will respond to
                the next no-match/no-input event, and so on.

                A `sys.no-match-default` or `sys.no-input-default` handler will be used
                to handle all following no-match/no-input events after all numbered
                no-match/no-input handlers for the parameter are consumed.

                A `sys.invalid-parameter` handler can be defined to handle the case
                where the parameter values have been `invalidated` by webhook. For
                example, if the user's response fill the parameter, however the
                parameter was invalidated by webhook, the fulfillment associated with
                the `sys.invalid-parameter` handler (if defined) will be called to
                provide a prompt.

                If the event handler for the corresponding event can't be found on the
                parameter, `initial_prompt_fulfillment` will be re-prompted.
                """
                pass
            def __init__(self,
                *,
                initial_prompt_fulfillment : typing.Optional[google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2.Fulfillment] = ...,
                reprompt_event_handlers : typing.Optional[typing.Iterable[global___EventHandler]] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["initial_prompt_fulfillment",b"initial_prompt_fulfillment"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["initial_prompt_fulfillment",b"initial_prompt_fulfillment","reprompt_event_handlers",b"reprompt_event_handlers"]) -> None: ...

        DISPLAY_NAME_FIELD_NUMBER: builtins.int
        REQUIRED_FIELD_NUMBER: builtins.int
        ENTITY_TYPE_FIELD_NUMBER: builtins.int
        IS_LIST_FIELD_NUMBER: builtins.int
        FILL_BEHAVIOR_FIELD_NUMBER: builtins.int
        DEFAULT_VALUE_FIELD_NUMBER: builtins.int
        REDACT_FIELD_NUMBER: builtins.int
        display_name: typing.Text = ...
        """Required. The human-readable name of the parameter, unique within the
        form.
        """

        required: builtins.bool = ...
        """Indicates whether the parameter is required. Optional parameters will not
        trigger prompts; however, they are filled if the user specifies them.
        Required parameters must be filled before form filling concludes.
        """

        entity_type: typing.Text = ...
        """Required. The entity type of the parameter.
        Format: `projects/-/locations/-/agents/-/entityTypes/<System Entity Type
        ID>` for system entity types (for example,
        `projects/-/locations/-/agents/-/entityTypes/sys.date`), or
        `projects/<Project ID>/locations/<Location ID>/agents/<Agent
        ID>/entityTypes/<Entity Type ID>` for developer entity types.
        """

        is_list: builtins.bool = ...
        """Indicates whether the parameter represents a list of values."""

        @property
        def fill_behavior(self) -> global___Form.Parameter.FillBehavior:
            """Required. Defines fill behavior for the parameter."""
            pass
        @property
        def default_value(self) -> google.protobuf.struct_pb2.Value:
            """The default value of an optional parameter. If the parameter is required,
            the default value will be ignored.
            """
            pass
        redact: builtins.bool = ...
        """Indicates whether the parameter content should be redacted in log.  If
        redaction is enabled, the parameter content will be replaced by parameter
        name during logging.
        Note: the parameter content is subject to redaction if either parameter
        level redaction or [entity type level redaction][google.cloud.dialogflow.cx.v3beta1.EntityType.redact] is
        enabled.
        """

        def __init__(self,
            *,
            display_name : typing.Text = ...,
            required : builtins.bool = ...,
            entity_type : typing.Text = ...,
            is_list : builtins.bool = ...,
            fill_behavior : typing.Optional[global___Form.Parameter.FillBehavior] = ...,
            default_value : typing.Optional[google.protobuf.struct_pb2.Value] = ...,
            redact : builtins.bool = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["default_value",b"default_value","fill_behavior",b"fill_behavior"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["default_value",b"default_value","display_name",b"display_name","entity_type",b"entity_type","fill_behavior",b"fill_behavior","is_list",b"is_list","redact",b"redact","required",b"required"]) -> None: ...

    PARAMETERS_FIELD_NUMBER: builtins.int
    @property
    def parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Form.Parameter]:
        """Parameters to collect from the user."""
        pass
    def __init__(self,
        *,
        parameters : typing.Optional[typing.Iterable[global___Form.Parameter]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> None: ...
global___Form = Form

class EventHandler(google.protobuf.message.Message):
    """An event handler specifies an [event][google.cloud.dialogflow.cx.v3beta1.EventHandler.event] that can be handled
    during a session. When the specified event happens, the following actions are
    taken in order:

    *   If there is a
    [`trigger_fulfillment`][google.cloud.dialogflow.cx.v3beta1.EventHandler.trigger_fulfillment] associated with
    the event, it will be called.
    *   If there is a [`target_page`][google.cloud.dialogflow.cx.v3beta1.EventHandler.target_page] associated
    with the event, the session will transition into the specified page.
    *   If there is a [`target_flow`][google.cloud.dialogflow.cx.v3beta1.EventHandler.target_flow] associated
    with the event, the session will transition into the specified flow.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    TRIGGER_FULFILLMENT_FIELD_NUMBER: builtins.int
    TARGET_PAGE_FIELD_NUMBER: builtins.int
    TARGET_FLOW_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The unique identifier of this event handler."""

    event: typing.Text = ...
    """Required. The name of the event to handle."""

    @property
    def trigger_fulfillment(self) -> google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2.Fulfillment:
        """The fulfillment to call when the event occurs.
        Handling webhook errors with a fulfillment enabled with webhook could
        cause infinite loop. It is invalid to specify such fulfillment for a
        handler handling webhooks.
        """
        pass
    target_page: typing.Text = ...
    """The target page to transition to.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/pages/<Page ID>`.
    """

    target_flow: typing.Text = ...
    """The target flow to transition to.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        event : typing.Text = ...,
        trigger_fulfillment : typing.Optional[google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2.Fulfillment] = ...,
        target_page : typing.Text = ...,
        target_flow : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["target",b"target","target_flow",b"target_flow","target_page",b"target_page","trigger_fulfillment",b"trigger_fulfillment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["event",b"event","name",b"name","target",b"target","target_flow",b"target_flow","target_page",b"target_page","trigger_fulfillment",b"trigger_fulfillment"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["target",b"target"]) -> typing.Optional[typing_extensions.Literal["target_page","target_flow"]]: ...
global___EventHandler = EventHandler

class TransitionRoute(google.protobuf.message.Message):
    """A transition route specifies a [intent][google.cloud.dialogflow.cx.v3beta1.Intent] that can be matched and/or a
    data condition that can be evaluated during a session. When a specified
    transition is matched, the following actions are taken in order:

    *   If there is a
    [`trigger_fulfillment`][google.cloud.dialogflow.cx.v3beta1.TransitionRoute.trigger_fulfillment] associated with
    the transition, it will be called.
    *   If there is a [`target_page`][google.cloud.dialogflow.cx.v3beta1.TransitionRoute.target_page] associated
    with the transition, the session will transition into the specified page.
    *   If there is a [`target_flow`][google.cloud.dialogflow.cx.v3beta1.TransitionRoute.target_flow] associated
    with the transition, the session will transition into the specified flow.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    INTENT_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    TRIGGER_FULFILLMENT_FIELD_NUMBER: builtins.int
    TARGET_PAGE_FIELD_NUMBER: builtins.int
    TARGET_FLOW_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The unique identifier of this transition route."""

    intent: typing.Text = ...
    """The unique identifier of an [Intent][google.cloud.dialogflow.cx.v3beta1.Intent].
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/intents/<Intent ID>`.
    Indicates that the transition can only happen when the given intent is
    matched.
    At least one of `intent` or `condition` must be specified. When both
    `intent` and `condition` are specified, the transition can only happen
    when both are fulfilled.
    """

    condition: typing.Text = ...
    """The condition to evaluate against [form parameters][google.cloud.dialogflow.cx.v3beta1.Form.parameters] or
    [session parameters][google.cloud.dialogflow.cx.v3beta1.SessionInfo.parameters].

    See the [conditions
    reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition).
    At least one of `intent` or `condition` must be specified. When both
    `intent` and `condition` are specified, the transition can only happen
    when both are fulfilled.
    """

    @property
    def trigger_fulfillment(self) -> google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2.Fulfillment:
        """The fulfillment to call when the condition is satisfied. At least one of
        `trigger_fulfillment` and `target` must be specified. When both are
        defined, `trigger_fulfillment` is executed first.
        """
        pass
    target_page: typing.Text = ...
    """The target page to transition to.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/pages/<Page ID>`.
    """

    target_flow: typing.Text = ...
    """The target flow to transition to.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        intent : typing.Text = ...,
        condition : typing.Text = ...,
        trigger_fulfillment : typing.Optional[google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2.Fulfillment] = ...,
        target_page : typing.Text = ...,
        target_flow : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["target",b"target","target_flow",b"target_flow","target_page",b"target_page","trigger_fulfillment",b"trigger_fulfillment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["condition",b"condition","intent",b"intent","name",b"name","target",b"target","target_flow",b"target_flow","target_page",b"target_page","trigger_fulfillment",b"trigger_fulfillment"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["target",b"target"]) -> typing.Optional[typing_extensions.Literal["target_page","target_flow"]]: ...
global___TransitionRoute = TransitionRoute

class ListPagesRequest(google.protobuf.message.Message):
    """The request message for [Pages.ListPages][google.cloud.dialogflow.cx.v3beta1.Pages.ListPages]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The flow to list all pages for.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    language_code: typing.Text = ...
    """The language to list pages for. The following fields are language
    dependent:

    *  `Page.entry_fulfillment.messages`
    *  `Page.entry_fulfillment.conditional_cases`
    *  `Page.event_handlers.trigger_fulfillment.messages`
    *  `Page.event_handlers.trigger_fulfillment.conditional_cases`
    *  `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages`
    *
    `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases`
    *  `Page.form.parameters.fill_behavior.reprompt_event_handlers.messages`
    *
    `Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases`
    *  `Page.transition_routes.trigger_fulfillment.messages`
    *  `Page.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    page_size: builtins.int = ...
    """The maximum number of items to return in a single page. By default 100 and
    at most 1000.
    """

    page_token: typing.Text = ...
    """The next_page_token value returned from a previous list request."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        language_code : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListPagesRequest = ListPagesRequest

class ListPagesResponse(google.protobuf.message.Message):
    """The response message for [Pages.ListPages][google.cloud.dialogflow.cx.v3beta1.Pages.ListPages]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PAGES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def pages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Page]:
        """The list of pages. There will be a maximum number of items returned based
        on the page_size field in the request.
        """
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results, or empty if there are no more
    results in the list.
    """

    def __init__(self,
        *,
        pages : typing.Optional[typing.Iterable[global___Page]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","pages",b"pages"]) -> None: ...
global___ListPagesResponse = ListPagesResponse

class GetPageRequest(google.protobuf.message.Message):
    """The request message for [Pages.GetPage][google.cloud.dialogflow.cx.v3beta1.Pages.GetPage]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the page.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/pages/<Page ID>`.
    """

    language_code: typing.Text = ...
    """The language to retrieve the page for. The following fields are language
    dependent:

    *  `Page.entry_fulfillment.messages`
    *  `Page.entry_fulfillment.conditional_cases`
    *  `Page.event_handlers.trigger_fulfillment.messages`
    *  `Page.event_handlers.trigger_fulfillment.conditional_cases`
    *  `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages`
    *
    `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases`
    *  `Page.form.parameters.fill_behavior.reprompt_event_handlers.messages`
    *
    `Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases`
    *  `Page.transition_routes.trigger_fulfillment.messages`
    *  `Page.transition_routes.trigger_fulfillment.conditional_cases`

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
global___GetPageRequest = GetPageRequest

class CreatePageRequest(google.protobuf.message.Message):
    """The request message for [Pages.CreatePage][google.cloud.dialogflow.cx.v3beta1.Pages.CreatePage]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The flow to create a page for.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    @property
    def page(self) -> global___Page:
        """Required. The page to create."""
        pass
    language_code: typing.Text = ...
    """The language of the following fields in `page`:

    *  `Page.entry_fulfillment.messages`
    *  `Page.entry_fulfillment.conditional_cases`
    *  `Page.event_handlers.trigger_fulfillment.messages`
    *  `Page.event_handlers.trigger_fulfillment.conditional_cases`
    *  `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages`
    *
    `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases`
    *  `Page.form.parameters.fill_behavior.reprompt_event_handlers.messages`
    *
    `Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases`
    *  `Page.transition_routes.trigger_fulfillment.messages`
    *  `Page.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page : typing.Optional[global___Page] = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page",b"page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","page",b"page","parent",b"parent"]) -> None: ...
global___CreatePageRequest = CreatePageRequest

class UpdatePageRequest(google.protobuf.message.Message):
    """The request message for [Pages.UpdatePage][google.cloud.dialogflow.cx.v3beta1.Pages.UpdatePage]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PAGE_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def page(self) -> global___Page:
        """Required. The page to update."""
        pass
    language_code: typing.Text = ...
    """The language of the following fields in `page`:

    *  `Page.entry_fulfillment.messages`
    *  `Page.entry_fulfillment.conditional_cases`
    *  `Page.event_handlers.trigger_fulfillment.messages`
    *  `Page.event_handlers.trigger_fulfillment.conditional_cases`
    *  `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages`
    *
    `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases`
    *  `Page.form.parameters.fill_behavior.reprompt_event_handlers.messages`
    *
    `Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases`
    *  `Page.transition_routes.trigger_fulfillment.messages`
    *  `Page.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The mask to control which fields get updated. If the mask is not present,
        all fields will be updated.
        """
        pass
    def __init__(self,
        *,
        page : typing.Optional[global___Page] = ...,
        language_code : typing.Text = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page",b"page","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","page",b"page","update_mask",b"update_mask"]) -> None: ...
global___UpdatePageRequest = UpdatePageRequest

class DeletePageRequest(google.protobuf.message.Message):
    """The request message for [Pages.DeletePage][google.cloud.dialogflow.cx.v3beta1.Pages.DeletePage]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FORCE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the page to delete.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/Flows/<flow ID>/pages/<Page ID>`.
    """

    force: builtins.bool = ...
    """This field has no effect for pages with no incoming transitions.
    For pages with incoming transitions:

    *  If `force` is set to false, an error will be returned with message
       indicating the incoming transitions.
    *  If `force` is set to true, Dialogflow will remove the page, as well as
       any transitions to the page (i.e. [Target
       page][EventHandler.target_page] in event handlers or [Target
       page][TransitionRoute.target_page] in transition routes that point to
       this page will be cleared).
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        force : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["force",b"force","name",b"name"]) -> None: ...
global___DeletePageRequest = DeletePageRequest
