import json
from datetime import datetime
from enum import Enum
from typing import Any, AsyncIterator, List, Literal, Mapping, Optional, Tuple, Union

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.app._logs import _LogsStream, _LogsStreamWithIterator
from viam.proto.app import (
    AddRoleRequest,
    APIKeyWithAuthorizations,
    AppServiceStub,
    AuthenticatorInfo,
    Authorization,
    AuthorizedPermissions,
    ChangeRoleRequest,
    CheckPermissionsRequest,
    CheckPermissionsResponse,
    CreateFragmentRequest,
    CreateFragmentResponse,
    CreateKeyFromExistingKeyAuthorizationsRequest,
    CreateKeyFromExistingKeyAuthorizationsResponse,
    CreateKeyRequest,
    CreateKeyResponse,
    CreateLocationRequest,
    CreateLocationResponse,
    CreateLocationSecretRequest,
    CreateLocationSecretResponse,
    CreateModuleRequest,
    CreateModuleResponse,
    CreateOrganizationInviteRequest,
    CreateOrganizationInviteResponse,
    CreateOrganizationRequest,
    CreateOrganizationResponse,
    CreateRegistryItemRequest,
    CreateRobotPartSecretRequest,
    CreateRobotPartSecretResponse,
    DeleteFragmentRequest,
    DeleteKeyRequest,
    DeleteLocationRequest,
    DeleteLocationSecretRequest,
    DeleteOrganizationInviteRequest,
    DeleteOrganizationMemberRequest,
    DeleteOrganizationRequest,
    DeleteRegistryItemRequest,
    DeleteRobotPartRequest,
    DeleteRobotPartSecretRequest,
    DeleteRobotRequest,
)
from viam.proto.app import Fragment as FragmentPB
from viam.proto.app import FragmentHistoryEntry as FragmentHistoryEntryPB
from viam.proto.app import FragmentVisibility as FragmentVisibilityPB
from viam.proto.app import (
    GetFragmentHistoryRequest,
    GetFragmentHistoryResponse,
    GetFragmentRequest,
    GetFragmentResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetModuleRequest,
    GetModuleResponse,
    GetOrganizationNamespaceAvailabilityRequest,
    GetOrganizationNamespaceAvailabilityResponse,
    GetOrganizationRequest,
    GetOrganizationResponse,
    GetOrganizationsWithAccessToLocationRequest,
    GetOrganizationsWithAccessToLocationResponse,
    GetRegistryItemRequest,
    GetRegistryItemResponse,
    GetRobotAPIKeysRequest,
    GetRobotAPIKeysResponse,
    GetRobotPartHistoryRequest,
    GetRobotPartHistoryResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    GetRobotPartRequest,
    GetRobotPartResponse,
    GetRobotPartsRequest,
    GetRobotPartsResponse,
    GetRobotRequest,
    GetRobotResponse,
    GetRoverRentalRobotsRequest,
    GetRoverRentalRobotsResponse,
    GetUserIDByEmailRequest,
    GetUserIDByEmailResponse,
    ListAuthorizationsRequest,
    ListAuthorizationsResponse,
    ListFragmentsRequest,
    ListFragmentsResponse,
    ListKeysRequest,
    ListKeysResponse,
    ListLocationsRequest,
    ListLocationsResponse,
    ListModulesRequest,
    ListModulesResponse,
    ListOrganizationMembersRequest,
    ListOrganizationMembersResponse,
    ListOrganizationsByUserRequest,
    ListOrganizationsByUserResponse,
    ListOrganizationsRequest,
    ListOrganizationsResponse,
    ListRegistryItemsRequest,
    ListRegistryItemsResponse,
    ListRobotsRequest,
    ListRobotsResponse,
    Location,
    LocationAuth,
    LocationAuthRequest,
    LocationAuthResponse,
    MarkPartAsMainRequest,
    MarkPartForRestartRequest,
    Model,
    Module,
    ModuleFileInfo,
    NewRobotPartRequest,
    NewRobotPartResponse,
    NewRobotRequest,
    NewRobotResponse,
    Organization,
    OrganizationIdentity,
    OrganizationInvite,
    OrganizationMember,
    OrgDetails,
    RegistryItem,
    RegistryItemStatus,
    RemoveRoleRequest,
    ResendOrganizationInviteRequest,
    ResendOrganizationInviteResponse,
    Robot,
)
from viam.proto.app import RobotPart as RobotPartPB
from viam.proto.app import RobotPartHistoryEntry as RobotPartHistoryEntryPB
from viam.proto.app import (
    RotateKeyRequest,
    RotateKeyResponse,
    RoverRentalRobot,
    SharedSecret,
    ShareLocationRequest,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
    UnshareLocationRequest,
    UpdateFragmentRequest,
    UpdateFragmentResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateModuleRequest,
    UpdateModuleResponse,
    UpdateOrganizationInviteAuthorizationsRequest,
    UpdateOrganizationInviteAuthorizationsResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    UpdateRegistryItemRequest,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    UploadModuleFileRequest,
    Visibility,
)
from viam.proto.app.packages import PackageType
from viam.proto.common import LogEntry as LogEntryPB
from viam.utils import datetime_to_timestamp, dict_to_struct, struct_to_dict

LOGGER = logging.getLogger(__name__)


class RobotPart:
    """A class that mirrors the `RobotPart` proto message.

    Use this class to make the attributes of a `viam.proto.app.RobotPart` more accessible and easier to read/interpret.
    """

    @classmethod
    def from_proto(cls, robot_part: RobotPartPB) -> Self:
        """Create a `RobotPart` from the .proto defined `RobotPart`.

        Args:
            robot_part (viam.proto.app.RobotPart): The object to copy from.

        Returns:
            RobotPart: The `RobotPart`.
        """
        self = cls()
        self.id = robot_part.id
        self.name = robot_part.name
        self.dns_name = robot_part.dns_name
        self.secret = robot_part.secret
        self.robot = robot_part.robot
        self.location_id = robot_part.location_id
        self.robot_config = struct_to_dict(robot_part.robot_config) if robot_part.HasField("robot_config") else None
        self.last_access = robot_part.last_access.ToDatetime() if robot_part.HasField("last_access") else None
        self.user_supplied_info = struct_to_dict(robot_part.user_supplied_info) if robot_part.HasField("user_supplied_info") else None
        self.main_part = robot_part.main_part
        self.fqdn = robot_part.fqdn
        self.local_fqdn = robot_part.local_fqdn
        self.created_on = robot_part.created_on.ToDatetime() if robot_part.HasField("created_on") else None
        self.secrets = list(robot_part.secrets)
        return self

    id: str
    name: str
    dns_name: str
    secret: str
    robot: str
    location_id: str
    robot_config: Optional[Mapping[str, Any]]
    last_access: Optional[datetime]
    user_supplied_info: Optional[Mapping[str, Any]]
    main_part: bool
    fqdn: str
    local_fqdn: str
    created_on: Optional[datetime]
    secrets: Optional[List[SharedSecret]]

    @property
    def proto(self) -> RobotPartPB:
        return RobotPartPB(
            id=self.id,
            name=self.name,
            dns_name=self.dns_name,
            secret=self.secret,
            robot=self.robot,
            location_id=self.location_id,
            robot_config=dict_to_struct(self.robot_config) if self.robot_config else None,
            last_access=datetime_to_timestamp(self.last_access) if self.last_access else None,
            user_supplied_info=dict_to_struct(self.user_supplied_info) if self.user_supplied_info else None,
            main_part=self.main_part,
            fqdn=self.fqdn,
            local_fqdn=self.local_fqdn,
            created_on=datetime_to_timestamp(self.created_on) if self.created_on else None,
            secrets=self.secrets,
        )


class LogEntry:
    """A class that mirrors the `LogEntry` proto message.

    Use this class to make the attributes of a `viam.proto.app.LogEntry` more accessible and easier to read/interpret.
    """

    @classmethod
    def from_proto(cls, log_entry: LogEntryPB) -> Self:
        """Create a `LogEntry` from the .proto defined `LogEntry`.

        Args:
            log_entry (viam.proto.app.LogEntry): The object to copy from.

        Returns:
            LogEntry: The `LogEntry`.
        """
        self = cls()
        self.host = log_entry.host
        self.level = log_entry.level
        self.time = log_entry.time.ToDatetime() if log_entry.HasField("time") else None
        self.logger_name = log_entry.logger_name
        self.message = log_entry.message
        self.caller = struct_to_dict(log_entry.caller) if log_entry.HasField("caller") else None
        self.stack = log_entry.stack
        self.fields = [struct_to_dict(field) for field in log_entry.fields]
        return self

    host: str
    level: str
    time: Optional[datetime]
    logger_name: str
    message: str
    caller: Optional[Mapping[str, Any]]
    stack: str
    fields: Optional[List[Mapping[str, Any]]]

    @property
    def proto(self) -> LogEntryPB:
        return LogEntryPB(
            host=self.host,
            level=self.level,
            time=datetime_to_timestamp(self.time) if self.time else None,
            logger_name=self.logger_name,
            message=self.message,
            caller=dict_to_struct(self.caller) if self.caller else None,
            stack=self.stack,
            fields=[dict_to_struct(field) for field in self.fields] if self.fields else None,
        )


class Fragment:
    """A class that mirrors the `Fragment` proto message.

    Use this class to make the attributes of a `viam.proto.app.RobotPart` more accessible and easier to read/interpret.
    """

    class Visibility(str, Enum):
        """
        FragmentVisibility specifies who is permitted to view the fragment.
        """

        PRIVATE = "private"
        """
        Only visible to members in the fragment's organization.
        """

        PUBLIC = "public"
        """
        Visible to anyone and appears on the fragments page.
        """

        PUBLIC_UNLISTED = "public_unlisted"
        """
        Visible to anyone but does not appear on the fragments page.
        """

        UNSPECIFIED = "unspecified"
        """
        Uninitialized visibility.
        """

        @classmethod
        def from_proto(cls, visibility: FragmentVisibilityPB.ValueType) -> "Fragment.Visibility":
            if visibility == FragmentVisibilityPB.FRAGMENT_VISIBILITY_PRIVATE:
                return Fragment.Visibility.PRIVATE
            if visibility == FragmentVisibilityPB.FRAGMENT_VISIBILITY_PUBLIC:
                return Fragment.Visibility.PUBLIC
            if visibility == FragmentVisibilityPB.FRAGMENT_VISIBILITY_PUBLIC_UNLISTED:
                return Fragment.Visibility.PUBLIC_UNLISTED
            return Fragment.Visibility.UNSPECIFIED

        def to_proto(self) -> FragmentVisibilityPB.ValueType:
            if self == self.PRIVATE:
                return FragmentVisibilityPB.FRAGMENT_VISIBILITY_PRIVATE
            if self == self.PUBLIC:
                return FragmentVisibilityPB.FRAGMENT_VISIBILITY_PUBLIC
            if self == self.PUBLIC_UNLISTED:
                return FragmentVisibilityPB.FRAGMENT_VISIBILITY_PUBLIC_UNLISTED
            return FragmentVisibilityPB.FRAGMENT_VISIBILITY_UNSPECIFIED

    @classmethod
    def from_proto(cls, fragment: FragmentPB) -> Self:
        """Create a `Fragment` from the .proto defined `Fragment`.

        Args:
            fragment (viam.proto.app.Fragment): The object to copy from.

        Returns:
            Fragment: The `Fragment`.
        """
        self = cls()
        self.id = fragment.id
        self.name = fragment.name
        self.fragment = struct_to_dict(fragment.fragment) if fragment.HasField("fragment") else None
        self.organization_owner = fragment.organization_owner
        self.public = fragment.public
        self.created_on = fragment.created_on.ToDatetime() if fragment.HasField("created_on") else None
        self.organization_name = fragment.organization_name
        self.robot_part_count = fragment.robot_part_count
        self.organization_count = fragment.organization_count
        self.only_used_by_owner = fragment.only_used_by_owner
        self.visibility = Fragment.Visibility.from_proto(fragment.visibility)
        return self

    id: str
    name: str
    fragment: Optional[Mapping[str, Any]]
    organization_owner: str
    public: bool
    created_on: Optional[datetime]
    organization_name: str
    robot_part_count: int
    organization_count: int
    only_used_by_owner: bool
    visibility: Visibility

    @property
    def proto(self) -> FragmentPB:
        return FragmentPB(
            id=self.id,
            name=self.name,
            fragment=dict_to_struct(self.fragment) if self.fragment else None,
            organization_owner=self.organization_owner,
            public=self.public,
            created_on=datetime_to_timestamp(self.created_on) if self.created_on else None,
            organization_name=self.organization_name,
            robot_part_count=self.robot_part_count,
            organization_count=self.organization_count,
            only_used_by_owner=self.only_used_by_owner,
            visibility=self.visibility.to_proto(),
        )


class FragmentHistoryEntry:
    """A class that mirrors the `FragmentHistoryEntry` proto message.

    Use this class to make the attributes of a `viam.proto.app.FragmentHistoryEntry` more accessible and easier to read/interpret.
    """

    @classmethod
    def from_proto(cls, fragment_history_entry: FragmentHistoryEntryPB) -> Self:
        """Create a `FragmentHistoryEntry` from the .proto defined `FragmentHistoryEntry`.

        Args:
            fragment_history_entry (viam.proto.app.FragmentHistoryEntry): The object to copy from.

        Returns:
            FragmentHistoryEntry: The `FragmentHistoryEntry`.
        """
        self = cls()
        self.fragment = fragment_history_entry.fragment
        self.edited_on = fragment_history_entry.edited_on.ToDatetime()
        self.old = Fragment.from_proto(fragment_history_entry.old)
        self.edited_by = fragment_history_entry.edited_by
        return self

    fragment: str
    edited_on: datetime
    old: Fragment
    edited_by: AuthenticatorInfo

    @property
    def proto(self) -> FragmentHistoryEntryPB:
        return FragmentHistoryEntryPB(
            fragment=self.fragment,
            edited_on=datetime_to_timestamp(self.edited_on),
            edited_by=self.edited_by,
            old=self.old.proto if self.old else None,
        )


class RobotPartHistoryEntry:
    """A class that mirrors the `RobotPartHistoryEntry` proto message.

    Use this class to make the attributes of a `viam.proto.app.RobotPartHistoryEntry` more accessible and easier to read/interpret.
    """

    @classmethod
    def from_proto(cls, robot_part_history_entry: RobotPartHistoryEntryPB) -> Self:
        """Create a `RobotPartHistoryEntry` from the .proto defined `RobotPartHistoryEntry`.

        Args:
            robot_part_history_entry (viam.proto.app.RobotPartHistoryEntry): The object to copy from.

        Returns:
            RobotPartHistoryEntry: The `RobotPartHistoryEntry`.
        """
        self = cls()
        self.part = robot_part_history_entry.part
        self.robot = robot_part_history_entry.robot
        self.when = robot_part_history_entry.when.ToDatetime() if robot_part_history_entry.HasField("when") else None
        self.old = RobotPart.from_proto(robot_part_history_entry.old) if robot_part_history_entry.HasField("old") else None
        return self

    part: str
    robot: str
    when: Optional[datetime]
    old: Optional[RobotPart]

    @property
    def proto(self) -> RobotPartHistoryEntryPB:
        return RobotPartHistoryEntryPB(
            part=self.part,
            robot=self.robot,
            when=datetime_to_timestamp(self.when) if self.when else None,
            old=self.old.proto if self.old else None,
        )


class APIKeyAuthorization:
    """A class with the necessary authorization data for creating an API key.

    Use this class when constructing API key authorizations to minimize the risk of malformed or missing data.
    """

    def __init__(
        self,
        role: Union[Literal["owner"], Literal["operator"]],
        resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        resource_id: str,
    ):
        """role (Union[Literal["owner"], Literal["operator"]]): The role to add.
        resource_type (Union[Literal["organization"], Literal["location"], Literal["robot"]]): Type of the resource to add role to.
            Must match `resource_id`.
        resource_id (str): ID of the resource the role applies to (that is, either an organization, location, or robot ID).
        """
        self._role = role
        self._resource_type = resource_type
        self._resource_id = resource_id

    _role: str
    _resource_type: str
    _resource_id: str


class AppClient:
    """gRPC client for method calls to app.

    Constructor is used by `ViamClient` to instantiate relevant service stub. Calls to `AppClient`  methods should be made through
    `ViamClient`.

    Establish a Connection::

        import asyncio

        from viam.rpc.dial import DialOptions, Credentials
        from viam.app.viam_client import ViamClient


        async def connect() -> ViamClient:
            # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
            dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
            return await ViamClient.create_from_dial_options(dial_options)


        async def main():

            # Make a ViamClient
            viam_client = await connect()
            # Instantiate an AppClient called "cloud" to run cloud app API methods on
            cloud = viam_client.app_client

            viam_client.close()

        if __name__ == '__main__':
            asyncio.run(main())

    For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str], location_id: Optional[str] = None):
        """Create an `AppClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
            location_id (Optional[str]): Default location ID.
        """
        self._metadata = metadata
        self._app_client = AppServiceStub(channel)
        self._location_id = location_id
        self._channel = channel

    _app_client: AppServiceStub
    _metadata: Mapping[str, str]
    _location_id: Optional[str]
    _channel: Channel
    _organization_id: Optional[str] = None

    async def _create_authorization(
        self,
        organization_id: str,
        identity_id: str,
        identity_type: str,
        role: Union[Literal["owner"], Literal["operator"]],
        resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        resource_id: str,
    ) -> Authorization:
        return Authorization(
            authorization_type="role",
            identity_id=identity_id,
            identity_type=identity_type,
            authorization_id=f"{resource_type}_{role}",
            resource_type=resource_type,
            resource_id=resource_id,
            organization_id=organization_id,
        )

    async def _create_authorization_for_new_api_key(self, org_id: str, auth: APIKeyAuthorization) -> Authorization:
        """Creates a new Authorization specifically for creating an API key."""
        return await self._create_authorization(
            organization_id=org_id,
            identity_id="",  # setting `identity_id` when creating an API key results in an error
            identity_type="api-key",
            role=auth._role,  # type: ignore -- Ignoring because this is technically a `string`
            resource_type=auth._resource_type,  # type: ignore -- Ignoring because this is technically a `string`
            resource_id=auth._resource_id,
        )

    async def get_user_id_by_email(self, email: str) -> str:
        """Get the ID of a user by email.

        ::

            id = await cloud.get_user_id_by_email("youremail@email.com")

        Args:
            email (str): The email of the user.

        Returns:
            str: The ID of the user.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetUserIDByEmailRequest(email=email)
        response: GetUserIDByEmailResponse = await self._app_client.GetUserIDByEmail(request, metadata=self._metadata)
        return response.user_id

    async def create_organization(self, name: str) -> Organization:
        """Create an organization.

        ::

            organization = await cloud.create_organization("name")

        Args:
            name (str): The name of the organization.

        Returns:
            Organization: The created organization.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateOrganizationRequest(name=name)
        response: CreateOrganizationResponse = await self._app_client.CreateOrganization(request, metadata=self._metadata)
        return response.organization

    async def list_organizations(self) -> List[Organization]:
        """List the organization(s) the user is an authorized owner of.

        ::

            org_list = await cloud.list_organizations()

        Returns:
            List[viam.proto.app.Organization]: The list of organizations.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListOrganizationsRequest()
        response: ListOrganizationsResponse = await self._app_client.ListOrganizations(request, metadata=self._metadata)
        return list(response.organizations)

    async def get_organizations_with_access_to_location(self, location_id: str) -> List[OrganizationIdentity]:
        """Get all organizations that have access to a location.

        ::

            org_list = await cloud.get_organizations_with_access_to_location("location-id")

        Args:
            location_id (str): The ID of the location.

        Returns:
            List[viam.proto.app.OrganizationIdentity]: The list of organizations.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetOrganizationsWithAccessToLocationRequest(location_id=location_id)
        response: GetOrganizationsWithAccessToLocationResponse = await self._app_client.GetOrganizationsWithAccessToLocation(
            request, metadata=self._metadata
        )
        return list(response.organization_identities)

    async def list_organizations_by_user(self, user_id: str) -> List[OrgDetails]:
        """List the organizations a user belongs to.

        ::

            org_list = await cloud.list_organizations_by_user("user-id")

        Args:
            user_id (str): The ID of the user

        Returns:
            List[OrgDetails]: The list of organizations.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListOrganizationsByUserRequest(user_id=user_id)
        response: ListOrganizationsByUserResponse = await self._app_client.ListOrganizationsByUser(request, metadata=self._metadata)
        return list(response.orgs)

    async def get_organization(self, org_id: str) -> Organization:
        """Return details about the requested organization.

        Args:
            org_id (str): The ID of the organization to query.

        Raises:
            GRPCError: If the provided org_id is invalid, or not currently authed to.

        Returns:
            viam.proto.app.Organization: The requested organization.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetOrganizationRequest(organization_id=org_id)
        response: GetOrganizationResponse = await self._app_client.GetOrganization(request, metadata=self._metadata)
        return response.organization

    async def get_organization_namespace_availability(self, public_namespace: str) -> bool:
        """Check the availability of an organization namespace.

        ::

            available = await cloud.get_organization_namespace_availability(
                public_namespace="my-cool-organization")

        Args:
            public_namespace (str): Organization namespace to check. Namespaces can only contain lowercase lowercase alphanumeric and dash
                characters.

        Raises:
            GRPCError: If an invalid namespace (for example, "") is provided.

        Returns:
            bool: True if the provided namespace is available.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetOrganizationNamespaceAvailabilityRequest(public_namespace=public_namespace)
        response: GetOrganizationNamespaceAvailabilityResponse = await self._app_client.GetOrganizationNamespaceAvailability(
            request, metadata=self._metadata
        )
        return response.available

    async def update_organization(
        self,
        org_id: str,
        name: Optional[str] = None,
        public_namespace: Optional[str] = None,
        region: Optional[str] = None,
        cid: Optional[str] = None,
    ) -> Organization:
        """Updates organization details.

        Args:
            org_id (str): The ID of the organization to update.
            name (Optional[str]): If provided, updates the org's name.
            public_namespace (Optional[str]): If provided, sets the org's namespace if it hasn't already been set.
            region (Optional[str]): If provided, updates the org's region.
            cid (Optional[str]): If provided, update's the org's CRM ID.

        Raises:
            GRPCError: If the org's namespace has already been set, or if the provided namespace is already taken.

        Returns:
            viam.proto.app.Organization: The updated organization.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = UpdateOrganizationRequest(
            organization_id=org_id,
            public_namespace=public_namespace,
            region=region,
            cid=cid,
            name=name,
        )
        response: UpdateOrganizationResponse = await self._app_client.UpdateOrganization(request, metadata=self._metadata)
        return response.organization

    async def delete_organization(self, org_id: str) -> None:
        """Delete an organization

        ::

            await cloud.delete_organization("org-id")

        Args:
            org_id (str): The ID of the organization.
                You can obtain your organization ID from the Viam app's organization settings page.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteOrganizationRequest(organization_id=org_id)
        await self._app_client.DeleteOrganization(request, metadata=self._metadata)

    async def list_organization_members(self, org_id: str) -> Tuple[List[OrganizationMember], List[OrganizationInvite]]:
        """List the members and invites of the currently authed-to organization.

        ::

            member_list, invite_list = await cloud.list_organization_members("org-id")

        Args:
            org_id (str): The ID of the organization to list members of.
                You can obtain your organization ID from the Viam app's organization settings page.

        Returns:
            Tuple[List[viam.proto.app.OrganizationMember], List[viam.proto.app.OrganizationInvite]]: A tuple containing two lists; the first
            [0] of organization members, and the second [1] of organization invites.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListOrganizationMembersRequest(organization_id=org_id)
        response: ListOrganizationMembersResponse = await self._app_client.ListOrganizationMembers(request, metadata=self._metadata)
        return list(response.members), list(response.invites)

    async def create_organization_invite(
        self,
        org_id: str,
        email: str,
        authorizations: Optional[List[Authorization]] = None,
        send_email_invite: bool = True,
    ) -> OrganizationInvite:
        """Creates an organization invite and sends it via email.

        ::

            await cloud.create_organization_invite("org-id", "youremail@email.com")

        Args:
            org_id (str): The ID of the organization to create an invite for.
                You can obtain your organization ID from the Viam app's organization settings page.
            email (str): The email address to send the invite to.
            authorizations (Optional[List[viam.proto.app.Authorization]]): Specifications of the
                authorizations to include in the invite. If not provided, full owner permissions will
                be granted.
            send_email_invite (Optional[bool]): Whether or not an email should be sent to the recipient of an invite.
                The user must accept the email to be added to the associated authorizations.
                When set to false, the user automatically receives the associated authorization
                on the next login of the user with the associated email address.

        Raises:
            GRPCError: if an invalid email is provided, or if the user is already a member of the org.

        Returns:
            OrganizationInvite: The organization invite.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateOrganizationInviteRequest(
            organization_id=org_id, email=email, authorizations=authorizations, send_email_invite=send_email_invite
        )
        response: CreateOrganizationInviteResponse = await self._app_client.CreateOrganizationInvite(request, metadata=self._metadata)
        return response.invite

    async def update_organization_invite_authorizations(
        self,
        org_id: str,
        email: str,
        add_authorizations: Optional[List[Authorization]] = None,
        remove_authorizations: Optional[List[Authorization]] = None,
    ) -> OrganizationInvite:
        """Update the authorizations attached to an organization invite that has already been created.

        Note that an invite can only have one authorization at each resource (for example, organization, location, robot, etc.) level and
        must have at least one authorization overall.

        ::

            from viam.proto.app import Authorization

            authorization_to_add = Authorization(
                authorization_type="some type of auth",
                authorization_id="identifier",
                resource_type="abc",
                resource_id="resource-identifier123",
                identity_id="id12345",
                organization_id="org_id_123"
            )

            update_invite = await cloud.update_organization_invite_authorizations(
                org_id="org_id_123",
                email="notarealemail@viam.com",
                add_authorizations =[authorization_to_add]
            )

        Args:
            org_id (str): The ID of the organization that the invite is for.
                You can obtain your organization ID from the Viam app's organization settings page.
            email (str): Email of the user the invite was sent to.
            add_authorizations (Optional[List[viam.proto.app.Authorization]]): Optional list of authorizations to add to the invite.
            remove_authorizations (Optional[List[viam.proto.app.Authorization]]): Optional list of authorizations to remove from the invite.

        Raises:
            GRPCError: If no authorizations are passed or if an invalid combination of authorizations is passed (for example an
                authorization to remove when the invite only contains one authorization).

        Returns:
            viam.proto.app.OrganizationInvite: The updated invite.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = UpdateOrganizationInviteAuthorizationsRequest(
            organization_id=org_id, email=email, add_authorizations=add_authorizations, remove_authorizations=remove_authorizations
        )
        response: UpdateOrganizationInviteAuthorizationsResponse = await self._app_client.UpdateOrganizationInviteAuthorizations(
            request, metadata=self._metadata
        )
        return response.invite

    async def delete_organization_member(self, org_id: str, user_id: str) -> None:
        """Remove a member from the organization.

        ::

            member_list, invite_list = await cloud.list_organization_members()
            first_user_id = member_list[0].user_id

            await cloud.delete_organization_member(org_id="org_id", user_id=first_user_id)

        Args:
            org_id (str): The ID of the org to remove the user from.
                You can obtain your organization ID from the Viam app's organization settings page.
            user_id (str): The ID of the user to remove.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteOrganizationMemberRequest(organization_id=org_id, user_id=user_id)
        await self._app_client.DeleteOrganizationMember(request, metadata=self._metadata)

    async def delete_organization_invite(self, org_id: str, email: str) -> None:
        """Deletes a pending organization invite.

        ::

            await cloud.delete_organization_invite("org-id", "youremail@email.com")

        Args:
            org_id (str): The ID of the organization that the invite to delete was for.
                You can obtain your organization ID from the Viam app's organization settings page.
            email (str): The email address the pending invite was sent to.

        Raises:
            GRPCError: If no pending invite is associated with the provided email address.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteOrganizationInviteRequest(organization_id=org_id, email=email)
        await self._app_client.DeleteOrganizationInvite(request, metadata=self._metadata)

    async def resend_organization_invite(self, org_id: str, email: str) -> OrganizationInvite:
        """Re-sends a pending organization invite email.

        ::

            org_invite = await cloud.resend_organization_invite("org-id", "youremail@email.com")

        Args:
            org_id (str): The ID of the organization that the invite to resend was for.
                You can obtain your organization ID from the Viam app's organization settings page.
            email (str): The email address associated with the invite.

        Raises:
            GRPCError: If no pending invite is associated with the provided email address.

        Returns:
            viam.proto.app.OrganizationInvite: The organization invite sent.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ResendOrganizationInviteRequest(organization_id=org_id, email=email)
        response: ResendOrganizationInviteResponse = await self._app_client.ResendOrganizationInvite(request, metadata=self._metadata)
        return response.invite

    async def create_location(self, org_id: str, name: str, parent_location_id: Optional[str] = None) -> Location:
        """Create and name a location under the currently authed-to organization and the specified parent location.

        ::

            my_new_location = await cloud.create_location(org_id="org-id", name="Robotville", parent_location_id="111ab12345")

        Args:
            org_id (str): The ID of the organization to create the location under.
                You can obtain your organization ID from the Viam app's organization settings page.
            name (str): Name of the location.
            parent_location_id (Optional[str]): Optional parent location to put the location under. Defaults to a root-level location if no
                location ID is provided.

        Raises:
            GRPCError: If either an invalid name (for example, ""), or parent location ID (for example, a nonexistent ID) is passed.

        Returns:
            viam.proto.app.Location: The newly created location.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateLocationRequest(organization_id=org_id, name=name, parent_location_id=parent_location_id)
        response: CreateLocationResponse = await self._app_client.CreateLocation(request, metadata=self._metadata)
        return response.location

    async def get_location(self, location_id: Optional[str] = None) -> Location:
        """Get a location.

        ::

            location = await cloud.get_location(location_id="123ab12345")

        Args:
            location_id (Optional[str]): ID of the location to get. Defaults to the location ID provided at `AppClient` instantiation.

        Raises:
            GRPCError: If an invalid location ID is passed or if one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            viam.proto.app.Location: The location.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetLocationRequest(location_id=location_id if location_id else self._location_id if self._location_id else "")
        response: GetLocationResponse = await self._app_client.GetLocation(request, metadata=self._metadata)
        return response.location

    async def update_location(self, location_id: str, name: Optional[str] = None, parent_location_id: Optional[str] = None) -> Location:
        """Change the name of a location and/or assign it a new parent location.

        ::

            # The following line takes the location with ID "abc12abcde" and moves it to be a
            # sub-location of the location with ID "xyz34xxxxx"
            my_updated_location = await cloud.update_location(
                location_id="abc12abcde",
                name="",
                parent_location_id="xyz34xxxxx",
            )

            # The following line changes the name of the location without changing its parent location
            my_updated_location = await cloud.update_location(
                location_id="abc12abcde",
                name="Land Before Robots"
            )

            # The following line moves the location back up to be a top level location without changing its name
            my_updated_location = await cloud.update_location(
                location_id="abc12abcde",
                name="",
                parent_location_id=""
            )

        Args:
            location_id (str): ID of the location to update. Must be specified.
            name (Optional[str]): Optional new name to be updated on the location. Defaults to the empty string "" (that is, the name
                doesn't change).
            parent_location_id(Optional[str]): Optional ID of new parent location to move the location under. Defaults to the empty string
                "" (that is, no new parent location is assigned).

        Raises:
            GRPCError: If either an invalid location ID, name, or parent location ID is passed.

        Returns:
            viam.proto.app.Location: The newly updated location.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = UpdateLocationRequest(location_id=location_id, name=name, parent_location_id=parent_location_id)
        response: UpdateLocationResponse = await self._app_client.UpdateLocation(request, metadata=self._metadata)
        return response.location

    async def delete_location(self, location_id: str) -> None:
        """Delete a location.

        ::

            await cloud.delete_location(location_id="abc12abcde")

        Args:
            location_id (str): ID of the location to delete. Must be specified.

        Raises:
            GRPCError: If an invalid location ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteLocationRequest(location_id=location_id)
        await self._app_client.DeleteLocation(request, metadata=self._metadata)

    async def list_locations(self, org_id: str) -> List[Location]:
        """Get a list of all locations under the currently authed-to organization.

        ::

            locations = await cloud.list_locations("org-id")

        Args:
            org_id (str): The ID of the org to list locations for.
                You can obtain your organization ID from the Viam app's organization settings page.

        Returns:
            List[viam.proto.app.Location]: The list of locations.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListLocationsRequest(organization_id=org_id)
        response: ListLocationsResponse = await self._app_client.ListLocations(request, metadata=self._metadata)
        return list(response.locations)

    async def share_location(self, organization_id: str, location_id: str) -> None:
        """Share a location with an organization.

        ::

            await cloud.share_location("organization-id", "location-id")

        Args:
            organization_id (str): The ID of the organization.
            location_id (str): The ID of the location.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ShareLocationRequest(location_id=location_id, organization_id=organization_id)
        await self._app_client.ShareLocation(request, metadata=self._metadata)

    async def unshare_location(self, organization_id: str, location_id: str) -> None:
        """Stop sharing a location with an organization.

        ::

            await cloud.unshare_location("organization-id", "location-id")

        Args:
            organization_id (str): The ID of the organization.
            location_id (str): The ID of the location.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = UnshareLocationRequest(location_id=location_id, organization_id=organization_id)
        await self._app_client.UnshareLocation(request, metadata=self._metadata)

    async def location_auth(self, location_id: Optional[str] = None) -> LocationAuth:
        """Get a location's `LocationAuth` (location secret(s)).

        ::

            loc_auth = await cloud.location_auth(location_id="123xy12345")

        Args:
            location_id (str): ID of the location to retrieve `LocationAuth` from. Defaults to the location ID provided at `AppClient`
                instantiation.

        Raises:
            GRPCError: If an invalid location ID is passed or if one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            viam.proto.app.LocationAuth: The `LocationAuth` containing location secrets.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = LocationAuthRequest(location_id=location_id if location_id else self._location_id if self._location_id else "")
        response: LocationAuthResponse = await self._app_client.LocationAuth(request, metadata=self._metadata)
        return response.auth

    async def create_location_secret(self, location_id: Optional[str] = None) -> LocationAuth:
        """Create a new location secret.

        ::

            new_loc_auth = await cloud.create_location_secret()

        Args:
            location_id (Optional[str]): ID of the location to generate a new secret for. Defaults to the location ID provided at
                `AppClient` instantiation.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            viam.proto.app.LocationAuth: The specified location's `LocationAuth` containing the newly created secret.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateLocationSecretRequest(location_id=location_id if location_id else self._location_id if self._location_id else "")
        response: CreateLocationSecretResponse = await self._app_client.CreateLocationSecret(request, metadata=self._metadata)
        return response.auth

    async def delete_location_secret(self, secret_id: str, location_id: Optional[str] = None) -> None:
        """Delete a location secret.

        ::

            await cloud.delete_location_secret(
                secret_id="abcd123-456-7890ab-cxyz98-989898xyzxyz")

        Args:
            location_id (str): ID of the location to delete secret from. Defaults to the location ID provided at `AppClient` instantiation.
            secret_id (str): ID of the secret to delete.

        Raises:
            GRPCError: If either an invalid location ID or secret ID is passed or a location ID isn't passed and there was no location
                ID provided at `AppClient` instantiation.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteLocationSecretRequest(
            location_id=location_id if location_id else self._location_id if self._location_id else "", secret_id=secret_id
        )
        await self._app_client.DeleteLocationSecret(request, metadata=self._metadata)

    async def get_robot(self, robot_id: str) -> Robot:
        """Get a robot.

        ::

            robot = await cloud.get_robot(robot_id="1a123456-x1yz-0ab0-a12xyzabc")

        Args:
            robot_id (str): ID of the robot to get.

        Raises:
            GRPCError: If an invalid robot ID is passed.

        Returns:
            viam.proto.app.Robot: The robot.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetRobotRequest(id=robot_id)
        response: GetRobotResponse = await self._app_client.GetRobot(request, metadata=self._metadata)
        return response.robot

    async def get_rover_rental_robots(self, org_id: str) -> List[RoverRentalRobot]:
        """Returns a list of rover rental robots within an org.

        ::

            rental_robots = await cloud.get_rover_rental_robots()

        Args:
            org_id (str): The ID of the organization to list rover rental robots for.
                You can obtain your organization ID from the Viam app's organization settings page.

        Returns:
            List[viam.proto.app.RoverRentalRobot]: The list of rover rental robots.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetRoverRentalRobotsRequest(org_id=org_id)
        response: GetRoverRentalRobotsResponse = await self._app_client.GetRoverRentalRobots(request, metadata=self._metadata)
        return list(response.robots)

    async def get_robot_parts(self, robot_id: str) -> List[RobotPart]:
        """Get a list of all the parts under a specific robot.

        ::

            list_of_parts = await cloud.get_robot_parts(
                robot_id="1a123456-x1yz-0ab0-a12xyzabc")

        Args:
            robot_id (str): ID of the robot to get parts from.

        Raises:
            GRPCError: If an invalid robot ID is passed.

        Returns:
            List[viam.app.app_client.RobotPart]: The list of robot parts.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetRobotPartsRequest(robot_id=robot_id)
        response: GetRobotPartsResponse = await self._app_client.GetRobotParts(request, metadata=self._metadata)
        return [RobotPart.from_proto(robot_part=part) for part in response.parts]

    async def get_robot_part(self, robot_part_id: str, dest: Optional[str] = None, indent: int = 4) -> RobotPart:
        """Get a robot part.

        ::

            my_robot_part = await cloud.get_robot_part(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to get.
            dest (Optional[str]): Optional filepath to write the robot part's config file in JSON format to.
            indent (int): Size (in number of spaces) of indent when writing config to `dest`. Defaults to 4.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        Returns:
            viam.app.app_client.RobotPart: The robot part.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetRobotPartRequest(id=robot_part_id)
        response: GetRobotPartResponse = await self._app_client.GetRobotPart(request, metadata=self._metadata)

        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{json.dumps(json.loads(response.config_json), indent=indent)}")
                file.flush()
            except Exception as e:
                LOGGER.error(f"Failed to write config JSON to file {dest}", exc_info=e)

        return RobotPart.from_proto(robot_part=response.part)

    async def get_robot_part_logs(
        self,
        robot_part_id: str,
        filter: Optional[str] = None,
        dest: Optional[str] = None,
        log_levels: List[str] = [],
        num_log_entries: int = 100,
    ) -> List[LogEntry]:
        """Get the logs associated with a robot part.

        ::

            part_logs = await cloud.get_robot_part_logs(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22", num_log_entries=20)

        Args:
            robot_part_id (str): ID of the robot part to get logs from.
            filter (Optional[str]): Only include logs with messages that contain the string `filter`. Defaults to empty string "" (that is,
                no filter).
            dest (Optional[str]): Optional filepath to write the log entries to.
            log_levels (List[str]): List of log levels for which entries should be returned. Defaults to empty list, which returns all logs.
            num_log_entries (int): Number of log entries to return. Passing 0 returns all logs. Defaults to 100. All logs or the first
                `num_log_entries` logs will be returned, whichever comes first.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        Returns:
            List[viam.app.app_client.LogEntry]: The list of log entries.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        if num_log_entries < 0:
            raise ValueError("'num_log_entries must be at least 0.")
        logs_left = num_log_entries
        page_token = ""
        logs = []

        while True:
            new_logs, next_page_token = await self._get_robot_part_logs(
                robot_part_id=robot_part_id, filter=filter if filter else "", page_token=page_token, log_levels=log_levels
            )
            if num_log_entries != 0 and len(new_logs) > logs_left:
                logs += new_logs[0:logs_left]
                break
            logs += new_logs
            logs_left -= len(new_logs)
            if not next_page_token or next_page_token == "" or logs_left == 0:
                break
            page_token = next_page_token

        if dest:
            try:
                file = open(dest, "w")
                for log in logs:
                    time = log.time
                    level = log.level.upper()
                    logger_name = log.logger_name.split(".")[0]
                    file_name = log.caller["File"] + ":" + str(int(log.caller["Line"]))
                    message = log.message
                    file.write(f"{time}\t{level}\t{logger_name}\t{file_name:<64}{message}\n")
                    file.flush()
            except Exception as e:
                LOGGER.error(f"Failed to write robot part from robot part with ID [{robot_part_id}]logs to file {dest}", exc_info=e)

        return logs

    async def _get_robot_part_logs(
        self, robot_part_id: str, filter: str, page_token: str, log_levels: List[str]
    ) -> Tuple[List[LogEntry], str]:
        request = GetRobotPartLogsRequest(id=robot_part_id, filter=filter, page_token=page_token, levels=log_levels)
        response: GetRobotPartLogsResponse = await self._app_client.GetRobotPartLogs(request, metadata=self._metadata)
        return [LogEntry.from_proto(log) for log in response.logs], response.next_page_token

    async def tail_robot_part_logs(
        self, robot_part_id: str, errors_only: bool = True, filter: Optional[str] = None
    ) -> _LogsStream[List[LogEntry]]:
        """Get an asynchronous iterator that receives live robot part logs.

        ::

            logs_stream = await cloud.tail_robot_part_logs(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to retrieve logs from.
            errors_only (bool): Boolean specifying whether or not to only include error logs. Defaults to True.
            filter (Optional[str]): Only include logs with messages that contain the string `filter`. Defaults to empty string "" (that is,
                no filter).

        Returns:
            _LogsStream[List[LogEntry]]: The asynchronous iterator receiving live robot part logs.
        """

        async def read() -> AsyncIterator[List[LogEntry]]:
            async with self._app_client.TailRobotPartLogs.open(metadata=self._metadata) as stream:
                await stream.send_message(
                    TailRobotPartLogsRequest(id=robot_part_id, errors_only=errors_only, filter=filter if filter else "")
                )

                while True:
                    response: Optional[TailRobotPartLogsResponse] = await stream.recv_message()
                    if response is None or len(response.logs) == 0:
                        break
                    logs = [LogEntry.from_proto(log) for log in response.logs]
                    yield logs

        return _LogsStreamWithIterator(read())

    async def get_robot_part_history(self, robot_part_id: str) -> List[RobotPartHistoryEntry]:
        """Get a list containing the history of a robot part.

        ::

            part_history = await cloud.get_robot_part_history(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to retrieve history from.

        Raises:
            GRPCError: If an invalid robot part ID is provided.

        Returns:
            List[viam.app.app_client.RobotPartHistoryEntry]: The list of the robot part's history.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetRobotPartHistoryRequest(id=robot_part_id)
        response: GetRobotPartHistoryResponse = await self._app_client.GetRobotPartHistory(request, metadata=self._metadata)
        return [RobotPartHistoryEntry.from_proto(part_history) for part_history in response.history]

    async def update_robot_part(self, robot_part_id: str, name: str, robot_config: Optional[Mapping[str, Any]] = None) -> RobotPart:
        """Change the name and assign an optional new configuration to a robot part.

        ::

            my_robot_part = await cloud.update_robot_part(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to update.
            name (str): New name to be updated on the robot part.
            robot_config (Mapping[str, Any]): Optional new config represented as a dictionary to be updated on the robot part. The robot
                part's config will remain as is (no change) if one isn't passed.

        Raises:
            GRPCError: If either an invalid robot part ID, name, or config is passed.

        Returns:
            viam.app.app_client.RobotPart: The newly updated robot part.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = UpdateRobotPartRequest(id=robot_part_id, name=name, robot_config=dict_to_struct(robot_config) if robot_config else None)
        response: UpdateRobotPartResponse = await self._app_client.UpdateRobotPart(request, metadata=self._metadata)
        return RobotPart.from_proto(robot_part=response.part)

    async def new_robot_part(self, robot_id: str, part_name: str) -> str:
        """Create a new robot part.

        ::

            new_part_id = await cloud.new_robot_part(
                robot_id="1a123456-x1yz-0ab0-a12xyzabc", part_name="myNewSubPart")

        Args:
            robot_id (str): ID of the robot to create a new part for.
            part_name (str): Name of the new part.

        Raises:
            GRPCError: If either an invalid robot ID or name is passed.

        Returns:
            str: The new robot part's ID.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = NewRobotPartRequest(robot_id=robot_id, part_name=part_name)
        response: NewRobotPartResponse = await self._app_client.NewRobotPart(request, metadata=self._metadata)
        return response.part_id

    async def delete_robot_part(self, robot_part_id: str) -> None:
        """Delete the specified robot part.

        ::

            await cloud.delete_robot_part(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to delete. Must be specified.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteRobotPartRequest(part_id=robot_part_id)
        await self._app_client.DeleteRobotPart(request, metadata=self._metadata)

    async def get_robot_api_keys(self, robot_id: str) -> List[APIKeyWithAuthorizations]:
        """Gets the API Keys for the machine.

        ::

            await cloud.get_robot_api_keys(robot_id="robot-id")

        Args:
            robot_id (str): The ID of the robot

        Returns:
            List[APIKeyWithAuthorizations]: The list of API keys.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetRobotAPIKeysRequest(robot_id=robot_id)
        response: GetRobotAPIKeysResponse = await self._app_client.GetRobotAPIKeys(request, metadata=self._metadata)
        return list(response.api_keys)

    async def mark_part_as_main(self, robot_part_id: str) -> None:
        """Mark a robot part as the main part of a robot.

        ::

            await cloud.mark_part_as_main(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to mark as main.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = MarkPartAsMainRequest(part_id=robot_part_id)
        await self._app_client.MarkPartAsMain(request, metadata=self._metadata)

    async def mark_part_for_restart(self, robot_part_id: str) -> None:
        """Mark the specified robot part for restart.

        ::

            await cloud.mark_part_for_restart(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to mark for restart.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = MarkPartForRestartRequest(part_id=robot_part_id)
        await self._app_client.MarkPartForRestart(request, metadata=self._metadata)

    async def create_robot_part_secret(self, robot_part_id: str) -> RobotPart:
        """Create a robot part secret.

        ::

            part_with_new_secret = await cloud.create_robot_part_secret(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to create a secret for.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        Returns:
            viam.app.app_client.RobotPart: The robot part the new secret was generated for.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateRobotPartSecretRequest(part_id=robot_part_id)
        response: CreateRobotPartSecretResponse = await self._app_client.CreateRobotPartSecret(request, metadata=self._metadata)
        return RobotPart.from_proto(response.part)

    async def delete_robot_part_secret(self, robot_part_id: str, secret_id: str) -> None:
        """Delete a robot part secret.

        ::

            await cloud.delete_robot_part_secret(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22",
                secret_id="123xyz12-abcd-4321-12ab-12xy1xyz12xy")

        Args:
            robot_part_id (str): ID of the robot part to delete the secret from.
            secret_id (str): ID of the secret to delete.

        Raises:
            GRPCError: If an invalid robot part ID or secret ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteRobotPartSecretRequest(part_id=robot_part_id, secret_id=secret_id)
        await self._app_client.DeleteRobotPartSecret(request, metadata=self._metadata)

    async def list_robots(self, location_id: Optional[str] = None) -> List[Robot]:
        """Get a list of all robots under the specified location.

        ::

            list_of_machines = await cloud.list_robots(location_id="123ab12345")

        Args:
            location_id (Optional[str]): ID of the location to retrieve the robots from. Defaults to the location ID provided at
                `AppClient` instantiation.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            List[viam.proto.app.Robot]: The list of robots.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListRobotsRequest(location_id=location_id if location_id else self._location_id if self._location_id else "")
        response: ListRobotsResponse = await self._app_client.ListRobots(request, metadata=self._metadata)
        return list(response.robots)

    async def new_robot(self, name: str, location_id: Optional[str] = None) -> str:
        """Create a new robot.

        ::

            new_machine_id = await cloud.new_robot(name="beepboop", location_id="my-location-id")

        Args:
            name (str): Name of the new robot.
            location_id (Optional[str]): ID of the location under which to create the robot. Defaults to the current authorized location.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            str: The new robot's ID.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = NewRobotRequest(location=location_id if location_id else self._location_id if self._location_id else "", name=name)
        response: NewRobotResponse = await self._app_client.NewRobot(request, metadata=self._metadata)
        return response.id

    async def update_robot(self, robot_id: str, name: str, location_id: Optional[str] = None) -> Robot:
        """Change the name of an existing robot.

        ::

            updated_robot = await cloud.update_robot(
                robot_id="1a123456-x1yz-0ab0-a12xyzabc",
                name="Orange-Robot")

        Args:
            robot_id (str): ID of the robot to update.
            name (str): New name to be updated on the robot.
            location_id (Optional[str]): ID of the location under which the robot exists. Defaults to the location ID provided at
                `AppClient` instantiation

        Raises:
            GRPCError: If either an invalid robot ID, name, or location ID is passed or a location ID isn't passed and there was no location
                ID provided at `AppClient` instantiation.

        Returns:
            viam.proto.app.Robot: The newly updated robot.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = UpdateRobotRequest(
            id=robot_id, name=name, location=location_id if location_id else self._location_id if self._location_id else ""
        )
        response: UpdateRobotResponse = await self._app_client.UpdateRobot(request, metadata=self._metadata)
        return response.robot

    async def delete_robot(self, robot_id: str) -> None:
        """Delete the specified robot.

        ::

            await cloud.delete_robot(robot_id="1a123456-x1yz-0ab0-a12xyzabc")

        Args:
            robot_id (str): ID of the robot to delete.

        Raises:
            GRPCError: If an invalid robot ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteRobotRequest(id=robot_id)
        await self._app_client.DeleteRobot(request, metadata=self._metadata)

    async def list_fragments(
        self, org_id: str, show_public: bool = True, visibilities: Optional[List[Fragment.Visibility]] = None
    ) -> List[Fragment]:
        """Get a list of fragments under the currently authed-to organization.

        ::

            fragments_list = await cloud.list_fragments(org_id="org-id", visibilities=[])

        Args:
            org_id (str): The ID of the organization to list fragments for.
                You can obtain your organization ID from the Viam app's organization settings page.
            show_public (bool): Optional boolean specifying whether or not to only show public fragments. If True, only public fragments
                will return. If False, only private fragments will return. Defaults to True.

                .. deprecated:: 0.25.0
                    Use ``visibilities`` instead.
            visibilities (Optional[List[Fragment.Visibility]]): List of FragmentVisibilities specifying which types of fragments to include
                in the results. If empty, by default only public fragments will be returned.

        Returns:
            List[viam.app.app_client.Fragment]: The list of fragments.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListFragmentsRequest(
            organization_id=org_id,
            fragment_visibility=map(Fragment.Visibility.to_proto, visibilities if visibilities else []),
            show_public=show_public,
        )
        response: ListFragmentsResponse = await self._app_client.ListFragments(request, metadata=self._metadata)
        return [Fragment.from_proto(fragment=fragment) for fragment in response.fragments]

    async def get_fragment(self, fragment_id: str) -> Fragment:
        """Get a fragment.

        ::

            # Get a fragment and print its name and when it was created.
            the_fragment = await cloud.get_fragment(
                fragment_id="12a12ab1-1234-5678-abcd-abcd01234567")
            print("Name: ", the_fragment.name, "\\nCreated on: ", the_fragment.created_on)

        Args:
            fragment_id (str): ID of the fragment to get.

        Raises:
            GRPCError: If an invalid fragment ID is passed.

        Returns:
            viam.app.app_client.Fragment: The fragment.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetFragmentRequest(id=fragment_id)
        response: GetFragmentResponse = await self._app_client.GetFragment(request, metadata=self._metadata)
        return Fragment.from_proto(fragment=response.fragment)

    async def create_fragment(self, org_id: str, name: str, config: Optional[Mapping[str, Any]] = None) -> Fragment:
        """Create a new private fragment.

        ::

            new_fragment = await cloud.create_fragment(org_id="org-id", name="cool_smart_machine_to_configure_several_of")

        Args:
            org_id (str): The ID of the organization to create the fragment within.
                You can obtain your organization ID from the Viam app's organization settings page.
            name (str): Name of the fragment.
            config (Optional[Mapping[str, Any]]): Optional Dictionary representation of new config to assign to specified fragment. Can be
                assigned by updating the fragment.

        Raises:
            GRPCError: If an invalid name is passed.

        Returns:
            viam.app.app_client.Fragment: The newly created fragment.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateFragmentRequest(name=name, config=dict_to_struct(config) if config else None, organization_id=org_id)
        response: CreateFragmentResponse = await self._app_client.CreateFragment(request, metadata=self._metadata)
        return Fragment.from_proto(response.fragment)

    async def update_fragment(
        self,
        fragment_id: str,
        name: str,
        config: Optional[Mapping[str, Any]] = None,
        public: Optional[bool] = None,
        visibility: Optional[Fragment.Visibility] = None,
    ) -> Fragment:
        """Update a fragment name AND its config and/or visibility.

        ::

            updated_fragment = await cloud.update_fragment(
                fragment_id="12a12ab1-1234-5678-abcd-abcd01234567",
                name="better_name")

        Args:
            fragment_id (str): ID of the fragment to update.
            name (str): New name to associate with the fragment.
            config (Optional[Mapping[str, Any]]): Optional Dictionary representation of new config to assign to specified fragment. Not
                passing this parameter will leave the fragment's config unchanged.
            public (bool): Boolean specifying whether the fragment is public. Not passing this parameter will leave the fragment's
                visibility unchanged. A fragment is private by default when created.

                .. deprecated:: 0.25.0
                    Use ``visibility`` instead.
            visibility (Optional[FragmentVisibility]): Optional FragmentVisibility list specifying who should be allowed
                to view the fragment. Not passing this parameter will leave the fragment's visibility unchanged.
                A fragment is private by default when created.

        Raises:
            GRPCError: if an invalid ID, name, or config is passed.

        Returns:
            viam.app.app_client.Fragment: The newly updated fragment.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = UpdateFragmentRequest(
            id=fragment_id,
            name=name,
            config=dict_to_struct(config) if config else None,
            public=public,
            visibility=visibility.to_proto() if visibility else None,
        )
        response: UpdateFragmentResponse = await self._app_client.UpdateFragment(request, metadata=self._metadata)
        return Fragment.from_proto(response.fragment)

    async def delete_fragment(self, fragment_id: str) -> None:
        """Delete a fragment.

        ::

            await cloud.delete_fragment(
                fragment_id="12a12ab1-1234-5678-abcd-abcd01234567")

        Args:
            fragment_id (str): ID of the fragment to delete.

        Raises:
            GRPCError: If an invalid fragment ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteFragmentRequest(id=fragment_id)
        await self._app_client.DeleteFragment(request, metadata=self._metadata)

    async def get_fragment_history(
        self, id: str, page_token: Optional[str] = "", page_limit: Optional[int] = 10
    ) -> List[FragmentHistoryEntry]:
        """Get fragment history.

        ::

            fragment_history = await cloud.get_fragment_history(
                id = "12a12ab1-1234-5678-abcd-abcd01234567",
                page_token = "pg-token",
                page_limit = 10
            )

        Args:
            id (str): ID of the fragment to fetch history for.
            page_token (Optional[str]): the page token for the fragment history collection
            page_limit (Optional[int]): the number of fragment history documents to return in the result.
                The default page limit is 10.

        Raises:
            GRPCError: if an invalid fragment id, page token or page limit is passed.

        Returns:
            viam.app.app_client.FragmentHistoryResponse: A list of documents with the fragment history.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """

        request = GetFragmentHistoryRequest(id=id, page_token=page_token, page_limit=page_limit)
        response: GetFragmentHistoryResponse = await self._app_client.GetFragmentHistory(request, metadata=self._metadata)
        return [FragmentHistoryEntry.from_proto(fragment_history) for fragment_history in response.history]

    async def add_role(
        self,
        org_id: str,
        identity_id: str,
        role: Union[Literal["owner"], Literal["operator"]],
        resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        resource_id: str,
    ) -> None:
        """Add a role under the currently authed-to organization.

        ::

            await cloud.add_role(
                org_id="org-id",
                identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                role="owner",
                resource_type="location",
                resource_id="111ab12345")

        Args:
            org_id (str): The ID of the organization to create the role in.
                You can obtain your organization ID from the Viam app's organization settings page.
            identity_id (str): ID of the entity the role belongs to (for example, a user ID).
            role (Union[Literal["owner"], Literal["operator"]]): The role to add.
            resource_type (Union[Literal["organization"], Literal["location"], Literal["robot"]]): Type of the resource to add role to.
                Must match `resource_id`.
            resource_id (str): ID of the resource the role applies to (that is, either an organization, location, or robot ID).

        Raises:
            GRPCError: If either an invalid identity ID, role ID, resource type, or resource ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        authorization = await self._create_authorization(
            organization_id=org_id,
            identity_id=identity_id,
            identity_type="",
            role=role,
            resource_type=resource_type,
            resource_id=resource_id,
        )
        request = AddRoleRequest(authorization=authorization)
        await self._app_client.AddRole(request, metadata=self._metadata)

    async def remove_role(
        self,
        org_id: str,
        identity_id: str,
        role: Union[Literal["owner"], Literal["operator"]],
        resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        resource_id: str,
    ) -> None:
        """Remove a role under the currently authed-to organization.

        ::

            await cloud.remove_role(
                org_id="org-id",
                identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                role="owner",
                resource_type="location",
                resource_id="111ab12345")

        Args:
            org_id (str): The ID of the organization the role exists in.
                You can obtain your organization ID from the Viam app's organization settings page.
            identity_id (str): ID of the entity the role belongs to (for example, a user ID).
            role (Union[Literal["owner"], Literal["operator"]]): The role to remove.
            resource_type (Union[Literal["organization"], Literal["location"], Literal["robot"]]): Type of the resource the role is being
                removed from. Must match `resource_id`.
            resource_id (str): ID of the resource the role applies to (that is, either an organization, location, or robot ID).

        Raises:
            GRPCError: If either an invalid identity ID, role ID, resource type, or resource ID or is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        authorization = await self._create_authorization(
            organization_id=org_id,
            identity_id=identity_id,
            identity_type="",
            role=role,
            resource_type=resource_type,
            resource_id=resource_id,
        )
        request = RemoveRoleRequest(authorization=authorization)
        await self._app_client.RemoveRole(request, metadata=self._metadata)

    async def change_role(
        self,
        organization_id: str,
        old_identity_id: str,
        old_role: Union[Literal["owner"], Literal["operator"]],
        old_resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        old_resource_id: str,
        new_identity_id: str,
        new_role: Union[Literal["owner"], Literal["operator"]],
        new_resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        new_resource_id: str,
    ) -> None:
        """Changes a role to a new role.

        ::

            await cloud.change_role(
                organization_id="organization-id",
                old_identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                old_role="operator",
                old_resource_type="location",
                old_resource_id="111ab12345",
                new_identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                new_role="owner",s
                new_resource_type="organization",
                new_resource_id="abc12345")

        Args:
            organization_id (str): ID of the organization
            old_identity_id (str): ID of the entity the role belongs to (for example, a user ID).
            old_role (Union[Literal["owner"], Literal["operator"]]): The role to be changed.
            old_resource_type (Union[Literal["organization"], Literal["location"], Literal["robot"]]): Type of the resource the role is
                added to. Must match `old_resource_id`.
            old_resource_id (str): ID of the resource the role applies to (that is, either an organization, location, or robot ID).

            new_identity_id (str): New ID of the entity the role blongs to (for example, a user ID).
            new_role (Union[Literal["owner"], Literal["operator"]]): The new role.
            new_resource_type (Union[Literal["organization"], Literal["location"], Literal["robot"]]): Type of the resource to add role to.
                Must match `new_resource_id`.
            new_resource_id (str): New ID of the resource the role applies to (that is, either an organization, location, or robot ID).

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        old_authorization = await self._create_authorization(
            organization_id=organization_id,
            identity_id=old_identity_id,
            identity_type="",
            role=old_role,
            resource_type=old_resource_type,
            resource_id=old_resource_id,
        )
        new_authorization = await self._create_authorization(
            organization_id=organization_id,
            identity_id=new_identity_id,
            identity_type="",
            role=new_role,
            resource_type=new_resource_type,
            resource_id=new_resource_id,
        )
        request = ChangeRoleRequest(old_authorization=old_authorization, new_authorization=new_authorization)
        await self._app_client.ChangeRole(request, metadata=self._metadata)

    async def list_authorizations(self, org_id: str, resource_ids: Optional[List[str]] = None) -> List[Authorization]:
        """List all authorizations under a specific resource (or resources) within the currently authed-to organization. If no resource IDs
        are provided, all resource authorizations within the organizations are returned.

        ::

            list_of_auths = await cloud.list_authorizations(
                org_id="org-id",
                resource_ids=["1a123456-x1yz-0ab0-a12xyzabc"])

        Args:
            org_id: The ID of the organization to list authorizations for.
            resource_ids (Optional[List[str]]): IDs of the resources to retrieve authorizations from.
                If None, defaults to all resources.

        Raises:
            GRPCError: If an invalid resource ID is passed.

        Returns:
            List[viam.proto.app.Authorization]: The list of authorizations.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListAuthorizationsRequest(organization_id=org_id, resource_ids=resource_ids)
        response: ListAuthorizationsResponse = await self._app_client.ListAuthorizations(request, metadata=self._metadata)
        return list(response.authorizations)

    async def check_permissions(self, permissions: List[AuthorizedPermissions]) -> List[AuthorizedPermissions]:
        """Checks validity of a list of permissions.

        ::

            from viam.proto.app import AuthorizedPermissions

            # Check whether the entity you're currently authenticated to has permission to control and/or
            # read logs from robots in the "organization-identifier123" org
            permissions = [AuthorizedPermissions(resource_type="organization",
                                                 resource_id="organization-identifier123",
                                                 permissions=["control_robot",
                                                              "read_robot_logs"])]

            filtered_permissions = await cloud.check_permissions(permissions)

        Args:
            permissions (List[viam.proto.app.AuthorizedPermissions]): the permissions to validate
                (for example, "read_organization", "control_robot")

        Raises:
            GRPCError: If the list of permissions to validate is empty.

        Returns:
            List[viam.proto.app.AuthorizedPermissions]: The permissions argument, with invalid permissions filtered out.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CheckPermissionsRequest(permissions=permissions)
        response: CheckPermissionsResponse = await self._app_client.CheckPermissions(request, metadata=self._metadata)
        return list(response.authorized_permissions)

    async def get_registry_item(self, item_id: str) -> RegistryItem:
        """Get registry item by ID.

        ::

            item = await cloud.get_registry_item("item-id")

        Args:
            item_id (str): The ID of the registry item.

        Returns:
            RegistryItem: The registry item.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetRegistryItemRequest(item_id=item_id)
        response: GetRegistryItemResponse = await self._app_client.GetRegistryItem(request, metadata=self._metadata)
        return response.item

    async def create_registry_item(self, organization_id: str, name: str, type: PackageType.ValueType) -> None:
        """Create a registry item

        ::

            await cloud.create_registry_item("org-id", "name", PackageType.PACKAGE_TYPE_ML_MODEL)

        Args:
            organization_id (str): The organization to create the registry item under.
            name (str): The name of the registry item, which must be unique within your org.
            type (PackageType.ValueType): The type of the item in the registry.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateRegistryItemRequest(organization_id=organization_id, name=name, type=type)
        await self._app_client.CreateRegistryItem(request, metadata=self._metadata)

    async def update_registry_item(
        self, item_id: str, type: PackageType.ValueType, description: str, visibility: Visibility.ValueType
    ) -> None:
        """Update a registry item.

        ::

            await cloud.update_registry_item("item-id", PackageType.PACKAGE_TYPE_ML_TRAINING, "description", Visibility.VISIBILITY_PUBLIC)

        Args:
            item_id (str): The ID of the registry item.
            type (PackageType.ValueType): The type of the item in the registry.
            description (str): The description of the registry item.
            visibility (Visibility.ValueType): The visibility of the registry item.
        """

        request = UpdateRegistryItemRequest(item_id=item_id, type=type, description=description, visibility=visibility)
        await self._app_client.UpdateRegistryItem(request, metadata=self._metadata)

    async def list_registry_items(
        self,
        organization_id: str,
        types: List[PackageType.ValueType],
        visibilities: List[Visibility.ValueType],
        platforms: List[str],
        statuses: List[RegistryItemStatus.ValueType],
        search_term: Optional[str] = None,
        page_token: Optional[str] = None,
    ) -> List[RegistryItem]:
        """List the registry items in an organization.

        Args:
            organization_id (str): The ID of the organization to return registry items for.
            types (List[PackageType.ValueType]): The types of registry items.
            visibilities (List[Visibility.ValueType]): The visibilities of registry items.
            platforms (List[str]): The platforms of registry items.
            statuses (List[RegistryItemStatus.ValueType]): The types of the items in the registry.
            search_term (Optional[str]): The search term of the registry items.
            page_token (Optional[str]): The page token of the registry items.

        Returns:
            List[RegistryItem]: The list of registry items.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListRegistryItemsRequest(
            organization_id=organization_id,
            types=types,
            visibilities=visibilities,
            platforms=platforms,
            statuses=statuses,
            search_term=search_term if search_term is not None else "",
            page_token=page_token if page_token is not None else "",
        )
        response: ListRegistryItemsResponse = await self._app_client.ListRegistryItems(request, metadata=self._metadata)
        return list(response.items)

    async def delete_registry_item(self, item_id: str) -> None:
        """Delete a registry item

        ::

            await cloud.delete_registry_item("item-id")

        Args:
            item_id (str): The ID of the registry item.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteRegistryItemRequest(item_id=item_id)
        await self._app_client.DeleteRegistryItem(request, metadata=self._metadata)

    async def create_module(self, org_id: str, name: str) -> Tuple[str, str]:
        """Create a module under the currently authed-to organization.

        ::

            new_module = await cloud.create_module(org_id="org-id", name="cool_new_hoverboard_module")
            print("Module ID:", new_module[0])

        Args:
            org_id (str): The ID of the organization to create the module under.
                You can obtain your organization ID from the Viam app's organization settings page.
            name (str): The name of the module. Must be unique within your organization.

        Raises:
            GRPCError: If an invalid name (for example, "") is passed.

        Returns:
            Tuple[str, str]: A tuple containing the ID [0] of the new module and its URL [1].

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateModuleRequest(organization_id=org_id, name=name)
        response: CreateModuleResponse = await self._app_client.CreateModule(request, metadata=self._metadata)
        return response.module_id, response.url

    async def update_module(
        self,
        module_id: str,
        url: str,
        description: str,
        models: Optional[List[Model]],
        entrypoint: str,
        public: bool = False,
    ) -> str:
        """Update the documentation URL, description, models, entrypoint, and/or the visibility of a module.

        ::

            url_of_my_module = await cloud.update_module(
                module_id="my-group:cool_new_hoverboard_module",
                url="https://docsformymodule.viam.com",
                description="A base to support hoverboards.",
                entrypoint="exec")

        Args:
            module_id (str): ID of the module being updated, containing module name (for example, "my-module") or namespace and module name
                (for example, "my-org:my-module").
            url (str): The url to reference for documentation and code (NOT the url of the module itself).
            description (str): A short description of the module that explains its purpose.
            models (Optional[List[viam.proto.app.Model]]): list of models that are available in the module.
            entrypoint (str): The executable to run to start the module program.
            public (bool): The visibility that should be set for the module. Defaults to False (private).

        Raises:
            GRPCError: If either an invalid module ID, URL, list of models, or organization ID is passed.

        Returns:
            str: The URL of the newly updated module.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = UpdateModuleRequest(
            module_id=module_id,
            visibility=Visibility.VISIBILITY_PUBLIC if public else Visibility.VISIBILITY_PRIVATE,
            url=url,
            description=description,
            models=models,
            entrypoint=entrypoint,
        )
        response: UpdateModuleResponse = await self._app_client.UpdateModule(request, metadata=self._metadata)
        return response.url

    async def upload_module_file(self, module_file_info: Optional[ModuleFileInfo], file: bytes) -> str:
        """Upload a module file

        ::

            file_id = await cloud.upload_module_file(file=b"<file>")

        Args:
            module_file_info (Optional[viam.proto.app.ModuleFileInfo]): Relevant metadata.
            file (bytes): Bytes of file to upload.

        Returns:
            str: ID of uploaded file.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request_module_file_info = UploadModuleFileRequest(module_file_info=module_file_info)
        request_file = UploadModuleFileRequest(file=file)
        async with self._app_client.UploadModuleFile.open(metadata=self._metadata) as stream:
            await stream.send_message(request_module_file_info)
            await stream.send_message(request_file, end=True)
            response: Union[UploadModuleFileRequest, None] = await stream.recv_message()
            if not response:
                await stream.recv_trailing_metadata()  # causes us to throw appropriate gRPC error.
                raise TypeError("Response cannot be empty")  # we should never get here, but for typechecking
            return response.url

    async def get_module(self, module_id: str) -> Module:
        """Get a module.

        ::

            the_module = await cloud.get_module(module_id="my-cool-modular-base")

        Args:
            module_id (str): ID of the module being retrieved, containing module name or namespace and module name.

        Raises:
            GRPCError: If an invalid module ID is passed.

        Returns:
            viam.proto.app.Module: The module.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = GetModuleRequest(module_id=module_id)
        response: GetModuleResponse = await self._app_client.GetModule(request, metadata=self._metadata)
        return response.module

    async def list_modules(self, org_id: str) -> List[Module]:
        """List the modules under the currently authed-to organization.

        ::

            modules_list = await cloud.list_modules("org-id")

        Args:
            org_id (str): The ID of the organization to list modules for.
                You can obtain your organization ID from the Viam app's organization settings page.

        Returns:
            List[viam.proto.app.Module]: The list of modules.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = ListModulesRequest(organization_id=org_id)
        response: ListModulesResponse = await self._app_client.ListModules(request, metadata=self._metadata)
        return list(response.modules)

    # TODO(RSDK-5569): when user-based auth exists, make `name` default to `None` and let
    # app deal with setting a default.
    async def create_key(self, org_id: str, authorizations: List[APIKeyAuthorization], name: Optional[str] = None) -> Tuple[str, str]:
        """Creates a new API key.

        ::

            from viam.app.app_client import APIKeyAuthorization

            auth = APIKeyAuthorization(
                role="owner",
                resource_type="robot",
                resource_id="your-robot-id123"
            )

            api_key, api_key_id = cloud.create_key("your-org-id", [auth], "my_key")

        Args:
            org_id (str): The ID of the organization to create the key for.
                You can obtain your organization ID from the Viam app's organization settings page.
            authorizations (List[viam.proto.app.Authorization]): A list of authorizations to associate
                with the key.
            name (Optional[str]): A name for the key. If None, defaults to the current timestamp.

        Raises:
            GRPCError: If the authorizations list is empty.

        Returns:
            Tuple[str, str]: The api key and api key ID.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        name = name if name is not None else str(datetime.now())
        authorizations_pb = [await self._create_authorization_for_new_api_key(org_id, auth) for auth in authorizations]
        request = CreateKeyRequest(authorizations=authorizations_pb, name=name)
        response: CreateKeyResponse = await self._app_client.CreateKey(request, metadata=self._metadata)
        return (response.key, response.id)

    async def delete_key(self, id: str) -> None:
        """Delete a API key.

        ::

            await cloud.delete_key("key-id")

        Args:
            id (str): The ID of the API key.

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = DeleteKeyRequest(id=id)
        await self._app_client.DeleteKey(request, metadata=self._metadata)

    async def create_key_from_existing_key_authorizations(self, id: str) -> Tuple[str, str]:
        """Creates a new API key with an existing key's authorizations

        ::

            api_key, api_key_id = await cloud.create_key_from_existing_key_authorizations(
                id="INSERT YOUR API KEY ID")

        Args:
            id (str): the ID of the API key to duplication authorizations from

        Returns:
            Tuple[str, str]: The API key and API key id

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = CreateKeyFromExistingKeyAuthorizationsRequest(id=id)
        response: CreateKeyFromExistingKeyAuthorizationsResponse = await self._app_client.CreateKeyFromExistingKeyAuthorizations(
            request,
            metadata=self._metadata,
        )
        return (response.key, response.id)

    async def list_keys(self, org_id: str) -> List[APIKeyWithAuthorizations]:
        """Lists all keys for the currently-authed-to org.

        ::

            keys = await cloud.list_keys()

        Args:
            org_id (str): The ID of the organization to list API keys for.
                You can obtain your organization ID from the Viam app's organization settings page.

        Returns:
            List[viam.proto.app.APIKeyWithAuthorizations]: The existing API keys and authorizations."""
        request = ListKeysRequest(org_id=org_id)
        response: ListKeysResponse = await self._app_client.ListKeys(request, metadata=self._metadata)
        return list(response.api_keys)

    async def rotate_key(self, id: str) -> Tuple[str, str]:
        """Rotate an API key.

        ::

            id, key = await cloud.rotate_key("key-id")

        Args:
            id (str): The ID of the key to be rotated.

        Returns:
            Tuple[str, str]: The API key and API key id

        For more information, see `Fleet Management API <https://docs.viam.com/appendix/apis/fleet/>`_.
        """
        request = RotateKeyRequest(id=id)
        response: RotateKeyResponse = await self._app_client.RotateKey(request, metadata=self._metadata)
        return response.key, response.id
