import json
from datetime import datetime
from typing import Any, AsyncIterator, List, Literal, Mapping, Optional, Tuple, Union

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.app._logs import _LogsStream, _LogsStreamWithIterator
from viam.proto.app import (
    AddRoleRequest,
    APIKeyWithAuthorizations,
    AppServiceStub,
    Authorization,
    AuthorizedPermissions,
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
    CreateRobotPartSecretRequest,
    CreateRobotPartSecretResponse,
    DeleteFragmentRequest,
    DeleteLocationRequest,
    DeleteLocationSecretRequest,
    DeleteOrganizationInviteRequest,
    DeleteOrganizationMemberRequest,
    DeleteRobotPartRequest,
    DeleteRobotPartSecretRequest,
    DeleteRobotRequest,
)
from viam.proto.app import Fragment as FragmentPB
from viam.proto.app import (
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
    ListOrganizationsRequest,
    ListOrganizationsResponse,
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
    OrganizationInvite,
    OrganizationMember,
    OrgDetails,
    RemoveRoleRequest,
    ResendOrganizationInviteRequest,
    ResendOrganizationInviteResponse,
    Robot,
)
from viam.proto.app import RobotPart as RobotPartPB
from viam.proto.app import RobotPartHistoryEntry as RobotPartHistoryEntryPB
from viam.proto.app import (
    RoverRentalRobot,
    SharedSecret,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
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
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    UploadModuleFileRequest,
    Visibility,
)
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
        resource_id (str): ID of the resource the role applies to (i.e., either an organization, location, or robot ID).
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

    # TODO(RSDK-5569): this method will no longer be reliable when we're not authing as an org.
    # consider what assumptions we _can_ make (e.g., if `list_orgs` only returns a single org
    # then we can probably still rely on it for org id?), and also update other APIs to ask for
    # an org id (optionally?) instead of just assuming we'll get it from this method.
    async def _get_organization_id(self) -> str:
        return self._organization_id if self._organization_id is not None else await self._request_organization_id()

    async def _request_organization_id(self) -> str:
        organizations = await self.list_organizations()
        self._organization_id = organizations[0].id
        return self._organization_id

    async def _create_authorization(
        self,
        identity_id: str,
        identity_type: str,
        role: Union[Literal["owner"], Literal["operator"]],
        resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        resource_id: str,
    ) -> Authorization:
        organization_id = await self._get_organization_id()
        return Authorization(
            authorization_type="role",
            identity_id=identity_id,
            identity_type=identity_type,
            authorization_id=f"{resource_type}_{role}",
            resource_type=resource_type,
            resource_id=resource_id,
            organization_id=organization_id,
        )

    async def _create_authorization_for_new_api_key(self, auth: APIKeyAuthorization) -> Authorization:
        """Creates a new Authorization specifically for creating an API key."""
        return await self._create_authorization(
            identity_id="",  # setting `identity_id` when creating an API key results in an error
            identity_type="api-key",
            role=auth._role,  # type: ignore -- Ignoring because this is technically a `string`
            resource_type=auth._resource_type,  # type: ignore -- Ignoring because this is technically a `string`
            resource_id=auth._resource_id,
        )

    # TODO(RSDK-5569): implement
    async def create_organization(self, name: str) -> Organization:
        raise NotImplementedError()

    async def list_organizations(self) -> List[Organization]:
        """List the organization(s) the user is an authorized owner of.

        ::

            org_list = await cloud.list_organizations()

        Returns:
            List[viam.proto.app.Organization]: The list of organizations.
        """
        request = ListOrganizationsRequest()
        response: ListOrganizationsResponse = await self._app_client.ListOrganizations(request, metadata=self._metadata)
        return list(response.organizations)

    # TODO(RSDK-5569): implement
    async def list_organizations_by_user(self, user_id: str) -> List[OrgDetails]:
        raise NotImplementedError()

    async def get_organization(self, org_id: Optional[str] = None) -> Organization:
        """Return details about the requested organization.

        Args:
            org_id (Optional[str]): ID of the organization to query. If None, defaults to the
                currently-authed org.

        Raises:
            GRPCError: If the provided org_id is invalid, or not currently authed to.

        Returns:
            viam.proto.app.Organization: The requested organization.
        """
        org_id = org_id if org_id is not None else await self._get_organization_id()
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
            GRPCError: If an invalid namespace (e.g., "") is provided.

        Returns:
            bool: True if the provided namespace is available.
        """
        request = GetOrganizationNamespaceAvailabilityRequest(public_namespace=public_namespace)
        response: GetOrganizationNamespaceAvailabilityResponse = await self._app_client.GetOrganizationNamespaceAvailability(
            request, metadata=self._metadata
        )
        return response.available

    async def update_organization(
        self,
        name: Optional[str] = None,
        public_namespace: Optional[str] = None,
        region: Optional[str] = None,
        cid: Optional[str] = None,
    ) -> Organization:
        """Updates organization details.

        Args:
            name (Optional[str]): If provided, updates the org's name.
            public_namespace (Optional[str]): If provided, sets the org's namespace if it hasn't already been set.
            region (Optional[str]): If provided, updates the org's region.
            cid (Optional[str]): If provided, update's the org's CRM ID.

        Raises:
            GRPCError: If the org's namespace has already been set, or if the provided namespace is already taken.

        Returns:
            viam.proto.app.Organization: The updated organization.
        """
        organization_id = await self._get_organization_id()
        request = UpdateOrganizationRequest(
            organization_id=organization_id,
            public_namespace=public_namespace,
            region=region,
            cid=cid,
            name=name,
        )
        response: UpdateOrganizationResponse = await self._app_client.UpdateOrganization(request, metadata=self._metadata)
        return response.organization

    # TODO(RSDK-5569): implement
    async def delete_organization(self, org_id: Optional[str] = None) -> None:
        raise NotImplementedError()

    async def list_organization_members(self) -> Tuple[List[OrganizationMember], List[OrganizationInvite]]:
        """List the members and invites of the currently authed-to organization.

        ::

            member_list, invite_list = await cloud.list_organization_members()

        Returns:
            Tuple[List[viam.proto.app.OrganizationMember], List[viam.proto.app.OrganizationInvite]]: A tuple containing two lists; the first
                [0] of organization members, and the second [1] of organization invites.
        """
        organization_id = await self._get_organization_id()
        request = ListOrganizationMembersRequest(organization_id=organization_id)
        response: ListOrganizationMembersResponse = await self._app_client.ListOrganizationMembers(request, metadata=self._metadata)
        return list(response.members), list(response.invites)

    async def create_organization_invite(
        self, email: str, authorizations: Optional[List[Authorization]] = None, send_email_invite=True
    ) -> OrganizationInvite:
        """Creates an organization invite and sends it via email.

        ::

            await cloud.create_organization_invite("youremail@email.com")

        Args:
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
        """
        organization_id = await self._get_organization_id()
        request = CreateOrganizationInviteRequest(
            organization_id=organization_id, email=email, authorizations=authorizations, send_email_invite=send_email_invite
        )
        response: CreateOrganizationInviteResponse = await self._app_client.CreateOrganizationInvite(request, metadata=self._metadata)
        return response.invite

    async def update_organization_invite_authorizations(
        self,
        email: str,
        add_authorizations: Optional[List[Authorization]] = None,
        remove_authorizations: Optional[List[Authorization]] = None,
    ) -> OrganizationInvite:
        """Update the authorizations attached to an organization invite that has already been created.

        Note that an invite can only have one authorization at each resource (e.g., organization, location, robot, etc.) level and must have
        at least one authorization overall.

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
                email="notarealemail@viam.com",
                add_authorizations =[authorization_to_add]
            )

        Args:
            email (str): Email of the user the invite was sent to.
            add_authorizations (Optional[List[viam.proto.app.Authorization]]): Optional list of authorizations to add to the invite.
            remove_authorizations (Optional[List[viam.proto.app.Authorization]]): Optional list of authorizations to remove from the invite.

        Raises:
            GRPCError: If no authorizations are passed or if an invalid combination of authorizations is passed (e.g. an authorization to
                remove when the invite only contains one authorization).

        Returns:
            viam.proto.app.OrganizationInvite: The updated invite.
        """
        organization_id = await self._get_organization_id()
        request = UpdateOrganizationInviteAuthorizationsRequest(
            organization_id=organization_id, email=email, add_authorizations=add_authorizations, remove_authorizations=remove_authorizations
        )
        response: UpdateOrganizationInviteAuthorizationsResponse = await self._app_client.UpdateOrganizationInviteAuthorizations(
            request, metadata=self._metadata
        )
        return response.invite

    async def delete_organization_member(self, user_id: str) -> None:
        """Remove a member from the organization.

        ::

            member_list, invite_list = await cloud.list_organization_members()
            first_user_id = member_list[0].user_id

            await cloud.delete_organization_member(first_user_id)

        Args:
            user_id (str): The ID of the user to remove.
        """
        organization_id = await self._get_organization_id()
        request = DeleteOrganizationMemberRequest(organization_id=organization_id, user_id=user_id)
        await self._app_client.DeleteOrganizationMember(request, metadata=self._metadata)

    async def delete_organization_invite(self, email: str) -> None:
        """Deletes a pending organization invite.

        ::

            await cloud.delete_organization_invite("youremail@email.com")

        Args:
            email (str): The email address the pending invite was sent to.

        Raises:
            GRPCError: If no pending invite is associated with the provided email address.
        """
        organization_id = await self._get_organization_id()
        request = DeleteOrganizationInviteRequest(organization_id=organization_id, email=email)
        await self._app_client.DeleteOrganizationInvite(request, metadata=self._metadata)

    async def resend_organization_invite(self, email: str) -> OrganizationInvite:
        """Re-sends a pending organization invite email.

        ::

            await cloud.resend_organization_invite("youremail@email.com")

        Args:
            email (str): The email address associated with the invite.

        Raises:
            GRPCError: If no pending invite is associated with the provided email address.
        """
        organization_id = await self._get_organization_id()
        request = ResendOrganizationInviteRequest(organization_id=organization_id, email=email)
        response: ResendOrganizationInviteResponse = await self._app_client.ResendOrganizationInvite(request, metadata=self._metadata)
        return response.invite

    async def create_location(self, name: str, parent_location_id: Optional[str] = None) -> Location:
        """Create and name a location under the currently authed-to organization and the specified parent location.

        ::

            my_new_location = await cloud.create_location(name="Robotville",
                                                          parent_location_id="111ab12345")

        Args:
            name (str): Name of the location.
            parent_location_id (Optional[str]): Optional parent location to put the location under. Defaults to a root-level location if no
                location ID is provided.

        Raises:
            GRPCError: If either an invalid name (e.g., ""), or parent location ID (e.g., a nonexistent ID) is passed.

        Returns:
            viam.proto.app.Location: The newly created location.
        """
        organization_id = await self._get_organization_id()
        request = CreateLocationRequest(organization_id=organization_id, name=name, parent_location_id=parent_location_id)
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
            name (Optional[str]): Optional new name to be updated on the location. Defaults to the empty string "" (i.e., the name doesn't
                change).
            parent_location_id(Optional[str]): Optional ID of new parent location to move the location under. Defaults to the empty string
                "" (i.e., no new parent location is assigned).

        Raises:
            GRPCError: If either an invalid location ID, name, or parent location ID is passed.

        Returns:
            viam.proto.app.Location: The newly updated location.
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
        """
        request = DeleteLocationRequest(location_id=location_id)
        await self._app_client.DeleteLocation(request, metadata=self._metadata)

    async def list_locations(self) -> List[Location]:
        """Get a list of all locations under the currently authed-to organization.

        ::

            locations = await cloud.list_locations()

        Returns:
            List[viam.proto.app.Location]: The list of locations.
        """
        organization_id = await self._get_organization_id()
        request = ListLocationsRequest(organization_id=organization_id)
        response: ListLocationsResponse = await self._app_client.ListLocations(request, metadata=self._metadata)
        return list(response.locations)

    # TODO(RSDK-5569): implement
    async def share_location(self):
        raise NotImplementedError()

    # TODO(RSDK-5569): implement
    async def unshare_location(self):
        raise NotImplementedError()

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
        """
        request = GetRobotRequest(id=robot_id)
        response: GetRobotResponse = await self._app_client.GetRobot(request, metadata=self._metadata)
        return response.robot

    async def get_rover_rental_robots(self) -> List[RoverRentalRobot]:
        """Returns a list of rover rental robots within an org.

        ::

            rental_robots = await cloud.get_rover_rental_robots()

        Returns:
            List[viam.proto.app.RoverRentalRobot]: The list of rover rental robots.
        """
        organization_id = await self._get_organization_id()
        request = GetRoverRentalRobotsRequest(org_id=organization_id)
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
        errors_only: bool = True,
        num_log_entries: int = 100,
    ) -> List[LogEntry]:
        """Get the logs associated with a robot part.

        ::

            part_logs = await cloud.get_robot_part_logs(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22", num_log_entries=20)

        Args:
            robot_part_id (str): ID of the robot part to get logs from.
            filter (Optional[str]): Only include logs with messages that contain the string `filter`. Defaults to empty string "" (i.e., no
                filter).
            dest (Optional[str]): Optional filepath to write the log entries to.
            errors_only (bool): Boolean specifying whether or not to only include error logs. Defaults to True.
            num_log_entries (int): Number of log entries to return. Passing 0 returns all logs. Defaults to 100. All logs or the first
                `num_log_entries` logs will be returned, whichever comes first.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        Returns:
            List[viam.app.app_client.LogEntry]: The list of log entries.
        """
        if num_log_entries < 0:
            raise ValueError("'num_log_entries must be at least 0.")
        logs_left = num_log_entries
        errors_only = errors_only if errors_only else True
        page_token = ""
        logs = []

        while True:
            new_logs, next_page_token = await self._get_robot_part_logs(
                robot_part_id=robot_part_id, filter=filter if filter else "", errors_only=errors_only, page_token=page_token
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

    async def _get_robot_part_logs(self, robot_part_id: str, filter: str, errors_only: bool, page_token: str) -> Tuple[List[LogEntry], str]:
        request = GetRobotPartLogsRequest(id=robot_part_id, errors_only=errors_only, filter=filter, page_token=page_token)
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
            filter (Optional[str]): Only include logs with messages that contain the string `filter`. Defaults to empty string "" (i.e., no
                filter).

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
            robot_id (str): ID of the the robot to create a new part for.
            part_name (str): Name of the new part.

        Raises:
            GRPCError: If either an invalid robot ID or name is passed.

        Returns:
            str: The new robot part's ID.
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
        """
        request = DeleteRobotPartRequest(part_id=robot_part_id)
        await self._app_client.DeleteRobotPart(request, metadata=self._metadata)

    async def mark_part_as_main(self, robot_part_id: str) -> None:
        """Mark a robot part as the main part of a robot.

        ::

            await cloud.mark_part_as_main(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the robot part to mark as main.

        Raises:
            GRPCError: If an invalid robot part ID is passed.
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
        """
        request = ListRobotsRequest(location_id=location_id if location_id else self._location_id if self._location_id else "")
        response: ListRobotsResponse = await self._app_client.ListRobots(request, metadata=self._metadata)
        return list(response.robots)

    async def new_robot(self, name: str, location_id: Optional[str] = None) -> str:
        """Create a new robot.

        ::

            new_machine_id = await cloud.new_robot(name="beepboop")

        Args:
            name (str): Name of the new robot.
            location_id (Optional[str]): ID of the location under which to create the robot. Defaults to the current authorized location.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            str: The new robot's ID.
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
        """
        request = DeleteRobotRequest(id=robot_id)
        await self._app_client.DeleteRobot(request, metadata=self._metadata)

    async def list_fragments(self, show_public: bool = True) -> List[Fragment]:
        """Get a list of fragments under the currently authed-to organization.

        ::

            fragments_list = await cloud.list_fragments(show_public=False)

        Args:
            show_public: Optional boolean specifying whether or not to only show public fragments. If True, only public fragments will
                return. If False, only private fragments will return. Defaults to True.

        Returns:
            List[viam.app.app_client.Fragment]: The list of fragments.
        """
        organization_id = await self._get_organization_id()
        request = ListFragmentsRequest(organization_id=organization_id, show_public=show_public)
        response: ListFragmentsResponse = await self._app_client.ListFragments(request, metadata=self._metadata)
        return [Fragment.from_proto(fragment=fragment) for fragment in response.fragments]

    async def get_fragment(self, fragment_id: str) -> Fragment:
        """Get a fragment.

        ::

            # Get a fragment and print its name and when it was created.
            the_fragment = await cloud.get_fragment(
                fragment_id="12a12ab1-1234-5678-abcd-abcd01234567")
            print("Name: ", the_fragment.name, "\nCreated on: ", the_fragment.created_on)

        Args:
            fragment_id (str): ID of the fragment to get.

        Raises:
            GRPCError: If an invalid fragment ID is passed.

        Returns:
            viam.app.app_client.Fragment: The fragment.
        """
        request = GetFragmentRequest(id=fragment_id)
        response: GetFragmentResponse = await self._app_client.GetFragment(request, metadata=self._metadata)
        return Fragment.from_proto(fragment=response.fragment)

    async def create_fragment(self, name: str, config: Optional[Mapping[str, Any]] = None) -> Fragment:
        """Create a new private fragment.

        ::

            new_fragment = await cloud.create_fragment(
                name="cool_smart_machine_to_configure_several_of")

        Args:
            name (str): Name of the fragment.
            config (Optional[Mapping[str, Any]]): Optional Dictionary representation of new config to assign to specified fragment. Can be
                assigned by updating the fragment.

        Raises:
            GRPCError: If an invalid name is passed.

        Returns:
            viam.app.app_client.Fragment: The newly created fragment.
        """
        organization_id = await self._get_organization_id()
        request = CreateFragmentRequest(name=name, config=dict_to_struct(config) if config else None, organization_id=organization_id)
        response: CreateFragmentResponse = await self._app_client.CreateFragment(request, metadata=self._metadata)
        return Fragment.from_proto(response.fragment)

    async def update_fragment(
        self, fragment_id: str, name: str, config: Optional[Mapping[str, Any]] = None, public: Optional[bool] = None
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

        Raises:
            GRPCError: if an invalid ID, name, or config is passed.

        Returns:
            viam.app.app_client.Fragment: The newly updated fragment.
        """
        request = UpdateFragmentRequest(id=fragment_id, name=name, config=dict_to_struct(config) if config else None, public=public)
        response: UpdateFragmentResponse = await self._app_client.UpdateFragment(request, metadata=self._metadata)
        return Fragment.from_proto(response.fragment)

    async def delete_fragment(self, fragment_id) -> None:
        """Delete a fragment.

        ::

            await cloud.delete_fragment(
                fragment_id="12a12ab1-1234-5678-abcd-abcd01234567")

        Args:
            fragment_id (str): ID of the fragment to delete.

        Raises:
            GRPCError: If an invalid fragment ID is passed.
        """
        request = DeleteFragmentRequest(id=fragment_id)
        await self._app_client.DeleteFragment(request, metadata=self._metadata)

    async def add_role(
        self,
        identity_id: str,
        role: Union[Literal["owner"], Literal["operator"]],
        resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        resource_id: str,
    ) -> None:
        """Add a role under the currently authed-to organization.

        ::

            await cloud.add_role(
                identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                role="owner",
                resource_type="location",
                resource_id="111ab12345")

        Args:
            identity_id (str): ID of the entity the role belongs to (e.g., a user ID).
            role (Union[Literal["owner"], Literal["operator"]]): The role to add.
            resource_type (Union[Literal["organization"], Literal["location"], Literal["robot"]]): Type of the resource to add role to.
                Must match `resource_id`.
            resource_id (str): ID of the resource the role applies to (i.e., either an organization, location, or robot ID).

        Raises:
            GRPCError: If either an invalid identity ID, role ID, resource type, or resource ID is passed.
        """
        authorization = await self._create_authorization(
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
        identity_id: str,
        role: Union[Literal["owner"], Literal["operator"]],
        resource_type: Union[Literal["organization"], Literal["location"], Literal["robot"]],
        resource_id: str,
    ) -> None:
        """Remove a role under the currently authed-to organization.

        ::

            await cloud.remove_role(
                identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                role="owner",
                resource_type="location",
                resource_id="111ab12345")

        Args:
            identity_id (str): ID of the entity the role belongs to (e.g., a user ID).
            role (Union[Literal["owner"], Literal["operator"]]): The role to add.
            resource_type (Union[Literal["organization"], Literal["location"], Literal["robot"]]): Type of the resource to add role to.
                Must match `resource_id`.
            resource_id (str): ID of the resource the role applies to (i.e., either an organization, location, or robot ID).

        Raises:
            GRPCError: If either an invalid identity ID, role ID, resource type, or resource ID or is passed.
        """
        authorization = await self._create_authorization(
            identity_id=identity_id,
            identity_type="",
            role=role,
            resource_type=resource_type,
            resource_id=resource_id,
        )
        request = RemoveRoleRequest(authorization=authorization)
        await self._app_client.RemoveRole(request, metadata=self._metadata)

    async def list_authorizations(self, resource_ids: Optional[List[str]] = None) -> List[Authorization]:
        """List all authorizations under a specific resource (or resources) within the currently authed-to organization. If no resource IDs
        are provided, all resource authorizations within the organizations are returned.

        ::

            list_of_auths = await cloud.list_authorizations(
                resource_ids=["1a123456-x1yz-0ab0-a12xyzabc"])

        Args:
            resource_ids (Optional[List[str]]): IDs of the resources to retrieve authorizations from.
                If None, defaults to all resources.

        Raises:
            GRPCError: If an invalid resource ID is passed.

        Returns:
            List[viam.proto.app.Authorization]: The list of authorizations.
        """
        organization_id = await self._get_organization_id()
        request = ListAuthorizationsRequest(organization_id=organization_id, resource_ids=resource_ids)
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
                (e.g., "read_organization", "control_robot")

        Raises:
            GRPCError: If the list of permissions to validate is empty.

        Returns:
            List[viam.proto.app.AuthorizedPermissions]: The permissions argument, with invalid permissions filtered out.
        """
        request = CheckPermissionsRequest(permissions=permissions)
        response: CheckPermissionsResponse = await self._app_client.CheckPermissions(request, metadata=self._metadata)
        return list(response.authorized_permissions)

    async def create_module(self, name: str) -> Tuple[str, str]:
        """Create a module under the currently authed-to organization.

        ::

            new_module = await cloud.create_module(name="cool_new_hoverboard_module")
            print("Module ID:", new_module[0])

        Args:
            name (str): The name of the module. Must be unique within your organization.

        Raises:
            GRPCError: If an invalid name (e.g., "") is passed.

        Returns:
            Tuple[str, str]: A tuple containing the ID [0] of the new module and its URL [1].
        """
        organization_id = await self._get_organization_id()
        request = CreateModuleRequest(organization_id=organization_id, name=name)
        response: CreateModuleResponse = await self._app_client.CreateModule(request, metadata=self._metadata)
        return response.module_id, response.url

    async def update_module(
        self,
        module_id: str,
        url: str,
        description: str,
        models: Optional[List[Model]],
        entrypoint: str,
        organization_id: Optional[str] = None,
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
            module_id (str): ID of the module being updated, containing module name (e.g., "my-module") or namespace and module name (e.g.,
                "my-org:my-module").
            url (str): The url to reference for documentation and code (NOT the url of the module itself).
            description (str): A short description of the module that explains its purpose.
            models (Optional[List[viam.proto.app.Model]]): list of models that are available in the module.
            entrypoint (str): The executable to run to start the module program.
            public (bool): The visibility that should be set for the module. Defaults to False (private).

        Raises:
            GRPCError: If either an invalid module ID, URL, list of models, or organization ID is passed.

        Returns:
            str: The URL of the newly updated module.
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
        """
        request = GetModuleRequest(module_id=module_id)
        response: GetModuleResponse = await self._app_client.GetModule(request, metadata=self._metadata)
        return response.module

    async def list_modules(self) -> List[Module]:
        """List the modules under the currently authed-to organization.

        ::

            modules_list = await cloud.list_modules()

        Returns:
            List[viam.proto.app.Module]: The list of modules.
        """
        organization_id = await self._get_organization_id()
        request = ListModulesRequest(organization_id=organization_id)
        response: ListModulesResponse = await self._app_client.ListModules(request, metadata=self._metadata)
        return list(response.modules)

    # TODO(RSDK-5569): when user-based auth exists, make `name` default to `None` and let
    # app deal with setting a default.
    async def create_key(self, authorizations: List[APIKeyAuthorization], name: Optional[str] = None) -> Tuple[str, str]:
        """Creates a new API key.

        ::

            from viam.app.app_client import APIKeyAuthorization

            auth = APIKeyAuthorization(
            role="owner",
            resource_type="robot",
            resource_id="your-robot-id123"
            )

            api_key, api_key_id = cloud.create_key([auth], "my_key")

        Args:
            authorizations (List[viam.proto.app.Authorization]): A list of authorizations to associate
                with the key.
            name (Optional[str]): A name for the key. If None, defaults to the current timestamp.

        Raises:
            GRPCError: If the authorizations list is empty.

        Returns:
            Tuple[str, str]: The api key and api key ID.
        """
        name = name if name is not None else str(datetime.now())
        authorizations_pb = [await self._create_authorization_for_new_api_key(auth) for auth in authorizations]
        request = CreateKeyRequest(authorizations=authorizations_pb, name=name)
        response: CreateKeyResponse = await self._app_client.CreateKey(request, metadata=self._metadata)
        return (response.key, response.id)

    async def create_key_from_existing_key_authorizations(self, id: str) -> Tuple[str, str]:
        """Creates a new API key with an existing key's authorizations

        ::

            api_key, api_key_id = cloud.create_key_from_existing_key_authorizations(
                id="INSERT YOUR API KEY ID")

        Args:
            id (str): the ID of the API key to duplication authorizations from

        Returns:
            Tuple[str, str] The API key and API key id
        """
        request = CreateKeyFromExistingKeyAuthorizationsRequest(id=id)
        response: CreateKeyFromExistingKeyAuthorizationsResponse = await self._app_client.CreateKeyFromExistingKeyAuthorizations(
            request,
            metadata=self._metadata,
        )
        return (response.key, response.id)

    async def list_keys(self) -> List[APIKeyWithAuthorizations]:
        """Lists all keys for the currently-authed-to org.

        ::

            keys = cloud.list_keys()

        Returns:
            List[viam.proto.app.APIKeyWithAuthorizations]: The existing API keys and authorizations."""
        org_id = await self._get_organization_id()
        request = ListKeysRequest(org_id=org_id)
        response: ListKeysResponse = await self._app_client.ListKeys(request, metadata=self._metadata)
        return list(response.api_keys)
