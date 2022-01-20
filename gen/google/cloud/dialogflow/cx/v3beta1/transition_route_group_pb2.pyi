"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.dialogflow.cx.v3beta1.page_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TransitionRouteGroup(google.protobuf.message.Message):
    """An TransitionRouteGroup represents a group of
    [`TransitionRoutes`][google.cloud.dialogflow.cx.v3beta1.TransitionRoute] to be used by a [Page][google.cloud.dialogflow.cx.v3beta1.Page].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    TRANSITION_ROUTES_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The unique identifier of the transition route group.
    [TransitionRouteGroups.CreateTransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.CreateTransitionRouteGroup] populates the name
    automatically.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/transitionRouteGroups/<Transition Route Group ID>`.
    """

    display_name: typing.Text = ...
    """Required. The human-readable name of the transition route group, unique within
    the [Agent][google.cloud.dialogflow.cx.v3beta1.Agent]. The display name can be no longer than 30 characters.
    """

    @property
    def transition_routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.dialogflow.cx.v3beta1.page_pb2.TransitionRoute]:
        """Transition routes associated with the [TransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup]."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        transition_routes : typing.Optional[typing.Iterable[google.cloud.dialogflow.cx.v3beta1.page_pb2.TransitionRoute]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name","name",b"name","transition_routes",b"transition_routes"]) -> None: ...
global___TransitionRouteGroup = TransitionRouteGroup

class ListTransitionRouteGroupsRequest(google.protobuf.message.Message):
    """The request message for [TransitionRouteGroups.ListTransitionRouteGroups][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.ListTransitionRouteGroups]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The flow to list all transition route groups for.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    page_size: builtins.int = ...
    """The maximum number of items to return in a single page. By default 100 and
    at most 1000.
    """

    page_token: typing.Text = ...
    """The next_page_token value returned from a previous list request."""

    language_code: typing.Text = ...
    """The language to list transition route groups for. The following fields are
    language dependent:

    *  `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages`
    *
    `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases`

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
global___ListTransitionRouteGroupsRequest = ListTransitionRouteGroupsRequest

class ListTransitionRouteGroupsResponse(google.protobuf.message.Message):
    """The response message for [TransitionRouteGroups.ListTransitionRouteGroups][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.ListTransitionRouteGroups]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRANSITION_ROUTE_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def transition_route_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TransitionRouteGroup]:
        """The list of transition route groups. There will be a maximum number of
        items returned based on the page_size field in the request. The list may in
        some cases be empty or contain fewer entries than page_size even if this
        isn't the last page.
        """
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results, or empty if there are no more
    results in the list.
    """

    def __init__(self,
        *,
        transition_route_groups : typing.Optional[typing.Iterable[global___TransitionRouteGroup]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","transition_route_groups",b"transition_route_groups"]) -> None: ...
global___ListTransitionRouteGroupsResponse = ListTransitionRouteGroupsResponse

class GetTransitionRouteGroupRequest(google.protobuf.message.Message):
    """The request message for [TransitionRouteGroups.GetTransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.GetTransitionRouteGroup]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the [TransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup].
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/transitionRouteGroups/<Transition Route Group ID>`.
    """

    language_code: typing.Text = ...
    """The language to retrieve the transition route group for. The following
    fields are language dependent:

    *  `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages`
    *
    `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases`

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
global___GetTransitionRouteGroupRequest = GetTransitionRouteGroupRequest

class CreateTransitionRouteGroupRequest(google.protobuf.message.Message):
    """The request message for [TransitionRouteGroups.CreateTransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.CreateTransitionRouteGroup]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    TRANSITION_ROUTE_GROUP_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The flow to create an [TransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup] for.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>`.
    """

    @property
    def transition_route_group(self) -> global___TransitionRouteGroup:
        """Required. The transition route group to create."""
        pass
    language_code: typing.Text = ...
    """The language of the following fields in `TransitionRouteGroup`:

    *  `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages`
    *
    `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        transition_route_group : typing.Optional[global___TransitionRouteGroup] = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["transition_route_group",b"transition_route_group"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","parent",b"parent","transition_route_group",b"transition_route_group"]) -> None: ...
global___CreateTransitionRouteGroupRequest = CreateTransitionRouteGroupRequest

class UpdateTransitionRouteGroupRequest(google.protobuf.message.Message):
    """The request message for [TransitionRouteGroups.UpdateTransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.UpdateTransitionRouteGroup]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRANSITION_ROUTE_GROUP_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    @property
    def transition_route_group(self) -> global___TransitionRouteGroup:
        """Required. The transition route group to update."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The mask to control which fields get updated."""
        pass
    language_code: typing.Text = ...
    """The language of the following fields in `TransitionRouteGroup`:

    *  `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages`
    *
    `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases`

    If not specified, the agent's default language is used.
    [Many
    languages](https://cloud.google.com/dialogflow/cx/docs/reference/language)
    are supported.
    Note: languages must be enabled in the agent before they can be used.
    """

    def __init__(self,
        *,
        transition_route_group : typing.Optional[global___TransitionRouteGroup] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["transition_route_group",b"transition_route_group","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","transition_route_group",b"transition_route_group","update_mask",b"update_mask"]) -> None: ...
global___UpdateTransitionRouteGroupRequest = UpdateTransitionRouteGroupRequest

class DeleteTransitionRouteGroupRequest(google.protobuf.message.Message):
    """The request message for [TransitionRouteGroups.DeleteTransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.DeleteTransitionRouteGroup]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FORCE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the [TransitionRouteGroup][google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroup] to delete.
    Format: `projects/<Project ID>/locations/<Location ID>/agents/<Agent
    ID>/flows/<Flow ID>/transitionRouteGroups/<Transition Route Group ID>`.
    """

    force: builtins.bool = ...
    """This field has no effect for transition route group that no page is using.
    If the transition route group is referenced by any page:

    *  If `force` is set to false, an error will be returned with message
       indicating pages that reference the transition route group.
    *  If `force` is set to true, Dialogflow will remove the transition route
       group, as well as any reference to it.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        force : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["force",b"force","name",b"name"]) -> None: ...
global___DeleteTransitionRouteGroupRequest = DeleteTransitionRouteGroupRequest
