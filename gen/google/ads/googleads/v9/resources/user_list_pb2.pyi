"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.common.user_lists_pb2
import google.ads.googleads.v9.enums.access_reason_pb2
import google.ads.googleads.v9.enums.user_list_access_status_pb2
import google.ads.googleads.v9.enums.user_list_closing_reason_pb2
import google.ads.googleads.v9.enums.user_list_membership_status_pb2
import google.ads.googleads.v9.enums.user_list_size_range_pb2
import google.ads.googleads.v9.enums.user_list_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class UserList(google.protobuf.message.Message):
    """Proto file describing the User List resource.

    A user list. This is a list of users a customer may target.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    READ_ONLY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    MEMBERSHIP_STATUS_FIELD_NUMBER: builtins.int
    INTEGRATION_CODE_FIELD_NUMBER: builtins.int
    MEMBERSHIP_LIFE_SPAN_FIELD_NUMBER: builtins.int
    SIZE_FOR_DISPLAY_FIELD_NUMBER: builtins.int
    SIZE_RANGE_FOR_DISPLAY_FIELD_NUMBER: builtins.int
    SIZE_FOR_SEARCH_FIELD_NUMBER: builtins.int
    SIZE_RANGE_FOR_SEARCH_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CLOSING_REASON_FIELD_NUMBER: builtins.int
    ACCESS_REASON_FIELD_NUMBER: builtins.int
    ACCOUNT_USER_LIST_STATUS_FIELD_NUMBER: builtins.int
    ELIGIBLE_FOR_SEARCH_FIELD_NUMBER: builtins.int
    ELIGIBLE_FOR_DISPLAY_FIELD_NUMBER: builtins.int
    MATCH_RATE_PERCENTAGE_FIELD_NUMBER: builtins.int
    CRM_BASED_USER_LIST_FIELD_NUMBER: builtins.int
    SIMILAR_USER_LIST_FIELD_NUMBER: builtins.int
    RULE_BASED_USER_LIST_FIELD_NUMBER: builtins.int
    LOGICAL_USER_LIST_FIELD_NUMBER: builtins.int
    BASIC_USER_LIST_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the user list.
    User list resource names have the form:

    `customers/{customer_id}/userLists/{user_list_id}`
    """

    id: builtins.int = ...
    """Output only. Id of the user list."""

    read_only: builtins.bool = ...
    """Output only. A flag that indicates if a user may edit a list. Depends on the list
    ownership and list type. For example, external remarketing user lists are
    not editable.

    This field is read-only.
    """

    name: typing.Text = ...
    """Name of this user list. Depending on its access_reason, the user list name
    may not be unique (e.g. if access_reason=SHARED)
    """

    description: typing.Text = ...
    """Description of this user list."""

    membership_status: google.ads.googleads.v9.enums.user_list_membership_status_pb2.UserListMembershipStatusEnum.UserListMembershipStatus.ValueType = ...
    """Membership status of this user list. Indicates whether a user list is open
    or active. Only open user lists can accumulate more users and can be
    targeted to.
    """

    integration_code: typing.Text = ...
    """An ID from external system. It is used by user list sellers to correlate
    IDs on their systems.
    """

    membership_life_span: builtins.int = ...
    """Number of days a user's cookie stays on your list since its most recent
    addition to the list. This field must be between 0 and 540 inclusive.
    However, for CRM based userlists, this field can be set to 10000 which
    means no expiration.

    It'll be ignored for logical_user_list.
    """

    size_for_display: builtins.int = ...
    """Output only. Estimated number of users in this user list, on the Google Display Network.
    This value is null if the number of users has not yet been determined.

    This field is read-only.
    """

    size_range_for_display: google.ads.googleads.v9.enums.user_list_size_range_pb2.UserListSizeRangeEnum.UserListSizeRange.ValueType = ...
    """Output only. Size range in terms of number of users of the UserList, on the Google
    Display Network.

    This field is read-only.
    """

    size_for_search: builtins.int = ...
    """Output only. Estimated number of users in this user list in the google.com domain.
    These are the users available for targeting in Search campaigns.
    This value is null if the number of users has not yet been determined.

    This field is read-only.
    """

    size_range_for_search: google.ads.googleads.v9.enums.user_list_size_range_pb2.UserListSizeRangeEnum.UserListSizeRange.ValueType = ...
    """Output only. Size range in terms of number of users of the UserList, for Search ads.

    This field is read-only.
    """

    type: google.ads.googleads.v9.enums.user_list_type_pb2.UserListTypeEnum.UserListType.ValueType = ...
    """Output only. Type of this list.

    This field is read-only.
    """

    closing_reason: google.ads.googleads.v9.enums.user_list_closing_reason_pb2.UserListClosingReasonEnum.UserListClosingReason.ValueType = ...
    """Indicating the reason why this user list membership status is closed. It is
    only populated on lists that were automatically closed due to inactivity,
    and will be cleared once the list membership status becomes open.
    """

    access_reason: google.ads.googleads.v9.enums.access_reason_pb2.AccessReasonEnum.AccessReason.ValueType = ...
    """Output only. Indicates the reason this account has been granted access to the list.
    The reason can be SHARED, OWNED, LICENSED or SUBSCRIBED.

    This field is read-only.
    """

    account_user_list_status: google.ads.googleads.v9.enums.user_list_access_status_pb2.UserListAccessStatusEnum.UserListAccessStatus.ValueType = ...
    """Indicates if this share is still enabled. When a UserList is shared with
    the user this field is set to ENABLED. Later the userList owner can decide
    to revoke the share and make it DISABLED.
    The default value of this field is set to ENABLED.
    """

    eligible_for_search: builtins.bool = ...
    """Indicates if this user list is eligible for Google Search Network."""

    eligible_for_display: builtins.bool = ...
    """Output only. Indicates this user list is eligible for Google Display Network.

    This field is read-only.
    """

    match_rate_percentage: builtins.int = ...
    """Output only. Indicates match rate for Customer Match lists. The range of this field is
    [0-100]. This will be null for other list types or when it's not possible
    to calculate the match rate.

    This field is read-only.
    """

    @property
    def crm_based_user_list(self) -> google.ads.googleads.v9.common.user_lists_pb2.CrmBasedUserListInfo:
        """User list of CRM users provided by the advertiser."""
        pass
    @property
    def similar_user_list(self) -> google.ads.googleads.v9.common.user_lists_pb2.SimilarUserListInfo:
        """Output only. User list which are similar to users from another UserList.
        These lists are readonly and automatically created by google.
        """
        pass
    @property
    def rule_based_user_list(self) -> google.ads.googleads.v9.common.user_lists_pb2.RuleBasedUserListInfo:
        """User list generated by a rule."""
        pass
    @property
    def logical_user_list(self) -> google.ads.googleads.v9.common.user_lists_pb2.LogicalUserListInfo:
        """User list that is a custom combination of user lists and user interests."""
        pass
    @property
    def basic_user_list(self) -> google.ads.googleads.v9.common.user_lists_pb2.BasicUserListInfo:
        """User list targeting as a collection of conversion or remarketing actions."""
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : typing.Optional[builtins.int] = ...,
        read_only : typing.Optional[builtins.bool] = ...,
        name : typing.Optional[typing.Text] = ...,
        description : typing.Optional[typing.Text] = ...,
        membership_status : google.ads.googleads.v9.enums.user_list_membership_status_pb2.UserListMembershipStatusEnum.UserListMembershipStatus.ValueType = ...,
        integration_code : typing.Optional[typing.Text] = ...,
        membership_life_span : typing.Optional[builtins.int] = ...,
        size_for_display : typing.Optional[builtins.int] = ...,
        size_range_for_display : google.ads.googleads.v9.enums.user_list_size_range_pb2.UserListSizeRangeEnum.UserListSizeRange.ValueType = ...,
        size_for_search : typing.Optional[builtins.int] = ...,
        size_range_for_search : google.ads.googleads.v9.enums.user_list_size_range_pb2.UserListSizeRangeEnum.UserListSizeRange.ValueType = ...,
        type : google.ads.googleads.v9.enums.user_list_type_pb2.UserListTypeEnum.UserListType.ValueType = ...,
        closing_reason : google.ads.googleads.v9.enums.user_list_closing_reason_pb2.UserListClosingReasonEnum.UserListClosingReason.ValueType = ...,
        access_reason : google.ads.googleads.v9.enums.access_reason_pb2.AccessReasonEnum.AccessReason.ValueType = ...,
        account_user_list_status : google.ads.googleads.v9.enums.user_list_access_status_pb2.UserListAccessStatusEnum.UserListAccessStatus.ValueType = ...,
        eligible_for_search : typing.Optional[builtins.bool] = ...,
        eligible_for_display : typing.Optional[builtins.bool] = ...,
        match_rate_percentage : typing.Optional[builtins.int] = ...,
        crm_based_user_list : typing.Optional[google.ads.googleads.v9.common.user_lists_pb2.CrmBasedUserListInfo] = ...,
        similar_user_list : typing.Optional[google.ads.googleads.v9.common.user_lists_pb2.SimilarUserListInfo] = ...,
        rule_based_user_list : typing.Optional[google.ads.googleads.v9.common.user_lists_pb2.RuleBasedUserListInfo] = ...,
        logical_user_list : typing.Optional[google.ads.googleads.v9.common.user_lists_pb2.LogicalUserListInfo] = ...,
        basic_user_list : typing.Optional[google.ads.googleads.v9.common.user_lists_pb2.BasicUserListInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_description",b"_description","_eligible_for_display",b"_eligible_for_display","_eligible_for_search",b"_eligible_for_search","_id",b"_id","_integration_code",b"_integration_code","_match_rate_percentage",b"_match_rate_percentage","_membership_life_span",b"_membership_life_span","_name",b"_name","_read_only",b"_read_only","_size_for_display",b"_size_for_display","_size_for_search",b"_size_for_search","basic_user_list",b"basic_user_list","crm_based_user_list",b"crm_based_user_list","description",b"description","eligible_for_display",b"eligible_for_display","eligible_for_search",b"eligible_for_search","id",b"id","integration_code",b"integration_code","logical_user_list",b"logical_user_list","match_rate_percentage",b"match_rate_percentage","membership_life_span",b"membership_life_span","name",b"name","read_only",b"read_only","rule_based_user_list",b"rule_based_user_list","similar_user_list",b"similar_user_list","size_for_display",b"size_for_display","size_for_search",b"size_for_search","user_list",b"user_list"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_description",b"_description","_eligible_for_display",b"_eligible_for_display","_eligible_for_search",b"_eligible_for_search","_id",b"_id","_integration_code",b"_integration_code","_match_rate_percentage",b"_match_rate_percentage","_membership_life_span",b"_membership_life_span","_name",b"_name","_read_only",b"_read_only","_size_for_display",b"_size_for_display","_size_for_search",b"_size_for_search","access_reason",b"access_reason","account_user_list_status",b"account_user_list_status","basic_user_list",b"basic_user_list","closing_reason",b"closing_reason","crm_based_user_list",b"crm_based_user_list","description",b"description","eligible_for_display",b"eligible_for_display","eligible_for_search",b"eligible_for_search","id",b"id","integration_code",b"integration_code","logical_user_list",b"logical_user_list","match_rate_percentage",b"match_rate_percentage","membership_life_span",b"membership_life_span","membership_status",b"membership_status","name",b"name","read_only",b"read_only","resource_name",b"resource_name","rule_based_user_list",b"rule_based_user_list","similar_user_list",b"similar_user_list","size_for_display",b"size_for_display","size_for_search",b"size_for_search","size_range_for_display",b"size_range_for_display","size_range_for_search",b"size_range_for_search","type",b"type","user_list",b"user_list"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_description",b"_description"]) -> typing.Optional[typing_extensions.Literal["description"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_eligible_for_display",b"_eligible_for_display"]) -> typing.Optional[typing_extensions.Literal["eligible_for_display"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_eligible_for_search",b"_eligible_for_search"]) -> typing.Optional[typing_extensions.Literal["eligible_for_search"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_integration_code",b"_integration_code"]) -> typing.Optional[typing_extensions.Literal["integration_code"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_match_rate_percentage",b"_match_rate_percentage"]) -> typing.Optional[typing_extensions.Literal["match_rate_percentage"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_membership_life_span",b"_membership_life_span"]) -> typing.Optional[typing_extensions.Literal["membership_life_span"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_read_only",b"_read_only"]) -> typing.Optional[typing_extensions.Literal["read_only"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_size_for_display",b"_size_for_display"]) -> typing.Optional[typing_extensions.Literal["size_for_display"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_size_for_search",b"_size_for_search"]) -> typing.Optional[typing_extensions.Literal["size_for_search"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["user_list",b"user_list"]) -> typing.Optional[typing_extensions.Literal["crm_based_user_list","similar_user_list","rule_based_user_list","logical_user_list","basic_user_list"]]: ...
global___UserList = UserList
