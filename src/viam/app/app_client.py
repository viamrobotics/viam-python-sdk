import json
from datetime import datetime
from typing import Any, List, Mapping, Optional, Tuple

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.proto.app import (
    AddRoleRequest,
    AppServiceStub,
    Authorization,
    AuthorizedPermissions,
    CheckPermissionsRequest,
    CheckPermissionsResponse,
    CreateFragmentRequest,
    CreateFragmentResponse,
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
    GetUserIDByEmailRequest,
    GetUserIDByEmailResponse,
    ListAuthorizationsRequest,
    ListAuthorizationsResponse,
    ListFragmentsRequest,
    ListFragmentsResponse,
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
    ListRobotsRequest,
    ListRobotsResponse,
    Location,
    LocationAuth,
    LocationAuthRequest,
    LocationAuthResponse,
)
from viam.proto.app import LogEntry as LogEntryPB
from viam.proto.app import (
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
    SharedSecret,
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
)
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
    secrets: List[SharedSecret]

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
        self.fields = [struct_to_dict(struct) for struct in log_entry.fields]
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
            robo_part_history_entry (viam.proto.app.RobotPartHistoryEntry): The object to copy from.

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


class AppClient:
    """gRPC client for method calls to app.

    Constructor is used by `ViamClient` to instantiate relevant service stub. Calls to `AppClient`  methods should be made through
    `ViamClient`.
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

    def close(self) -> None:
        self._channel.close()

    # TODO: Nil error.
    async def get_user_id_by_email(self, email: str) -> str:
        """Get a user's ID using their email.

        Args:
            email (str): User's email.

        Raises:
            GRPCError: If an invalid email is passed.

        Returns:
            str: The ID.
        """
        request = GetUserIDByEmailRequest(email=email)
        response: GetUserIDByEmailResponse = await self._app_client.GetUserIDByEmail(request, metadata=self._metadata)
        return response.user_id

    # TODO: Nil error.
    async def create_organization(self, name: str) -> Organization:
        """Create an organization.

        Args:
            name (str): Name of the new organization.

        Raises:
            GRPCError: If an invalid name is passed.

        Returns:
            viam.proto.app.Organization: _description_
        """
        request = CreateOrganizationRequest(name=name)
        response: CreateOrganizationResponse = await self._app_client.CreateOrganization(request, metadata=self._metadata)
        return response.organization

    # TODO: Timestamp error. The returned timestamp is negative.
    async def list_organizations(self) -> List[Organization]:
        """List the organization(s) the user is an authorized owner of.

        Returns:
            List[viam.proto.app.Organization]: The list of organizations.
        """
        request = ListOrganizationsRequest()
        response: ListOrganizationsResponse = await self._app_client.ListOrganizations(request, metadata=self._metadata)
        return list(response.organizations)

    # TODO: Test.
    async def list_organizations_by_user(self, user_id: str) -> List[OrgDetails]:
        """List the organizations a user is a part of.

        Args:
            user_id (str): ID of the user

        Raises:
            GRPCError: If an invalid user ID is passed.

        Returns:
            List[viam.proto.app.Organization]: The list of organizations.
        """
        request = ListOrganizationsByUserRequest(user_id=user_id)
        response: ListOrganizationsByUserResponse = await self._app_client.ListOrganizationsByUser(request, metadata=self._metadata)
        return list(response.orgs)

    # TODO: Nil error when passing anything that isn't the currently auth'd organization's ID (i.e., an incorrect/mistyped ID or an
    # unauthenticated ID).
    async def get_organization(self, organization_id: str) -> Organization:
        """Get an organization.

        Args:
            organization_id (str): ID of the organization to get.

        Raises:
            GRPCError: If an invalid organization ID is passed.

        Returns:
            viam.proto.app.Organization: The organization.
        """
        request = GetOrganizationRequest(organization_id=organization_id)
        response: GetOrganizationResponse = await self._app_client.GetOrganization(request, metadata=self._metadata)
        return response.organization

    async def get_organization_namespace_availability(self, public_namespace: str) -> bool:
        """Check the availability of an organization namespace.

        Args:
            public_namespace (str): Organization namespace to check.

        Raises:
            GRPCError: If an invalid namespace is provided.

        Returns:
            bool: Boolean signifying if the provided namespace is available.
        """
        request = GetOrganizationNamespaceAvailabilityRequest(public_namespace=public_namespace)
        response: GetOrganizationNamespaceAvailabilityResponse = await self._app_client.GetOrganizationNamespaceAvailability(
            request, metadata=self._metadata
        )
        return response.available

    # TODO: Nil error only when trying to update name.
    async def update_organization(
        self, organization_id: str, name: Optional[str] = None, public_namespace: Optional[str] = None, region: Optional[str] = None
    ) -> Organization:
        """Update the name or GCS region associated with an organization or assign it a public namespace.

        Args:
            organization_id (str): ID of the organization to update.
            name (Optional[str]): New name to assign the organization. No name provided will simply leave the current name unchanged.
            public_namespace (Optional[str]): New public namespace to assign to the organization. No namespace provided will
                simply not assign a namespace. A namespace can only be assigned to an organization once (i.e., it is immutable).
            region (Optional[str]): New GCS region to associate the organization with. No region provided will simply leave the current
                region unchanged.

        Raises:
            GRPCError: If either an invalid organization ID, name, public namespace, or region is provided.

        Returns:
            viam.proto.app.Organization: The newly updated organization.
        """
        print(name)
        request = UpdateOrganizationRequest(organization_id=organization_id, name=name, public_namespace=public_namespace, region=region)
        response: UpdateOrganizationResponse = await self._app_client.UpdateOrganization(request, metadata=self._metadata)
        return response.organization

    # Not possible under current location-based authentication model.
    async def delete_organization(self, organization_id: str) -> None:
        raise NotImplementedError()

    # TODO: Nil error.
    async def list_organization_members(self, organization_id: str) -> Tuple[List[OrganizationMember], List[OrganizationInvite]]:
        """List the members of an organization.

        Args:
            organization_id (str): ID of the organization to retrieve members from.

        Raises:
            GRPCError: If an invalid organization ID is passed.

        Returns:
            Tuple[List[viam.proto.app.OrganizationMember], List[viam.proto.app.OrganizationInvite]]: A tuple containing two lists; the first
                [0] of organization members, and the second [1] contains organization invites.
        """
        request = ListOrganizationMembersRequest(organization_id=organization_id)
        response: ListOrganizationMembersResponse = await self._app_client.ListOrganizationMembers(request, metadata=self._metadata)
        return list(response.members), list(response.invites)

    # TODO: Test and add docstring.
    async def create_organization_invite(
        self, organization_id: str, email: str, authorizations: Optional[List[Authorization]]
    ) -> OrganizationInvite:
        """

        Args:
            organization_id (str):
            email (str):
            authorizations (Optional[List[Authorization]]):

        Returns:
            viam.proto.app.OrganizationInvite:
        """
        request = CreateOrganizationInviteRequest(organization_id=organization_id, email=email, authorizations=authorizations)
        response: CreateOrganizationInviteResponse = await self._app_client.CreateOrganizationInvite(request, metadata=self._metadata)
        return response.invite

    # TODO: Test, check optionality, and add docstring.
    async def update_organization_invite_authorizations(
        self,
        organization_id: str,
        email: str,
        add_authorizations: Optional[List[Authorization]],
        remove_authorizations: Optional[List[Authorization]],
    ) -> OrganizationInvite:
        """

        Args:
            organization_id (str):
            email (str):
            add_authorization (Optional[List[viam.proto.app.Authorization]]):
            remove_authorization (Optional[List[viam.proto.app.Authorization]]):

        Returns:
            viam.proto.app.OrganizationInvite: The updated invite.
        """
        request = UpdateOrganizationInviteAuthorizationsRequest(
            organization_id=organization_id, email=email, add_authorizations=add_authorizations, remove_authorizations=remove_authorizations
        )
        response: UpdateOrganizationInviteAuthorizationsResponse = await self._app_client.UpdateOrganizationInviteAuthorizations(
            request, metadata=self._metadata
        )
        return response.invite

    # TODO: Test.
    async def delete_organization_member(self, organization_id: str, user_id: str) -> None:
        """Delete an organization member.

        Args:
            organization_id (str): ID of the organization to delete the member from.
            user_id (str): ID of the user to delete.

        Raises:
            GRPCError: If either an invalid organization ID or user ID is passed.
        """
        request = DeleteOrganizationMemberRequest(organization_id=organization_id, user_id=user_id)
        await self._app_client.DeleteOrganizationMember(request, metadata=self._metadata)

    # TODO: Test.
    async def delete_organization_invite(self, organization_id: str, email: str) -> None:
        """Delete an organization invite

        Args:
            organization_id (str): ID of the organization the invite was sent from.
            email (str): Email the invite was sent to.

        Raises:
            GRPCError: If either an invalid organization ID or email is passed.
        """
        request = DeleteOrganizationInviteRequest(organization_id=organization_id, email=email)
        await self._app_client.DeleteOrganizationInvite(request, metadata=self._metadata)

    # TODO: Test.
    async def resend_organization_invite(self, organization_id: str, email: str) -> OrganizationInvite:
        """Resend an organization invite

        Args:
            organization_id (str): ID of the organization the invite was sent from.
            email (str): Email the invite was sent to.

        Raises:
            GRPCError: If either an invalid organization ID or email is passed.

        Returns:
            viam.app.proto.OrganizationInvite: The resent organization invite.
        """
        request = ResendOrganizationInviteRequest(organization_id=organization_id, email=email)
        response: ResendOrganizationInviteResponse = await self._app_client.ResendOrganizationInvite(request, metadata=self._metadata)
        return response.invite

    async def create_location(self, name: str, organization_id: str, parent_location_id: Optional[str] = None) -> Location:
        """Create and name a location under the specified organization and parent location.

        Args:
            name (str): Name of the location.
            organization_id (str): ID of the organization to create the location under.
            parent_location_id (Optional[str]): Optional parent location to put the location under. Defaults to a root-level location if no
                location ID is provided.

        Raises:
            GRPCError: If either an invalid organization ID, name, or parent location ID is passed.

        Returns:
            viam.proto.app.Location: The newly created location.
        """
        request = CreateLocationRequest(organization_id=organization_id, name=name, parent_location_id=parent_location_id)
        response: CreateLocationResponse = await self._app_client.CreateLocation(request, metadata=self._metadata)
        return response.location

    async def get_location(self, location_id: Optional[str] = None) -> Location:
        """Get a location.

        Args:
            location_id (Optional[str]): ID of the location to get. Defaults to the location ID provided at `AppClient` instantiation.
                If no default location ID was passed, a GRPCError will be thrown.

        Raises:
            GRPCError: If an invalid location ID is passed.

        Returns:
            viam.proto.app.Location: The location.
        """
        request = GetLocationRequest(location_id=location_id if location_id else self._location_id if self._location_id else "")
        response: GetLocationResponse = await self._app_client.GetLocation(request, metadata=self._metadata)
        return response.location

    async def update_location(self, location_id: str, name: Optional[str] = None, parent_location_id: Optional[str] = None) -> Location:
        """Change the name of a location and/or assign it a new parent location.

        Args:
            location_id (str): ID of the location to update.
            name (Optional[str]): Optional new name to be updated on the location. Defaults to the empty string "" (i.e., the name doesn't
                change).
            parent_location_id(Optional[str]): Optional new parent location to move the location under. Defaults to the empty string ""
                (i.e., no new parent location is assigned).

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

        Args:
            location_id (str): ID of the location to delete. Must be specified.

        Raises:
            GRPCError: If an invalid location ID is passed.
        """
        request = DeleteLocationRequest(location_id=location_id)
        await self._app_client.DeleteLocation(request, metadata=self._metadata)

    async def list_locations(self, organization_id: str) -> List[Location]:
        """Get a list of all locations under the specified organization.

        Args:
            organization_id (str): ID of the organization to retrieve the locations from.

        Raises:
            GRPCError: If an invalid organization ID is passed.

        Returns:
            List[viam.proto.app.Location]: The list of locations.
        """
        request = ListLocationsRequest(organization_id=organization_id)
        response: ListLocationsResponse = await self._app_client.ListLocations(request, metadata=self._metadata)
        return list(response.locations)

    async def share_location(self):
        raise NotImplementedError()

    async def unshare_location(self):
        raise NotImplementedError()

    async def location_auth(self, location_id: Optional[str] = None) -> LocationAuth:
        """Get a locations `LocationAuth` (location secret(s)).

        Args:
            location_id (str): ID of the location to retrieve `LocationAuth` from. Defaults to the location ID provided at `AppClient`
                instantiation.

        Raises:
            GRPCError: If an invalid location_id is passed or if one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            LocationAuth: The `LocationAuth` containing location secrets.
        """
        request = LocationAuthRequest(location_id=location_id if location_id else self._location_id if self._location_id else "")
        response: LocationAuthResponse = await self._app_client.LocationAuth(request, metadata=self._metadata)
        return response.auth

    async def create_location_secret(self, location_id: Optional[str] = None) -> LocationAuth:
        """Create a new location secret.

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

        Args:
            id (str): ID of the robot to get.

        Raises:
            GRPCError: If an invalid robot ID is passed.

        Returns:
            viam.proto.app.Robot: The robot.
        """
        request = GetRobotRequest(id=robot_id)
        response: GetRobotResponse = await self._app_client.GetRobot(request, metadata=self._metadata)
        return response.robot

    async def get_rover_rental_parts(self):
        raise NotImplementedError()

    async def get_robot_parts(self, robot_id: str) -> List[RobotPart]:
        """Get a list of all the parts under a specific robot.

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
            except Exception as e:
                LOGGER.error(f"Failed to write robot part from robot part with ID [{robot_part_id}]logs to file {dest}", exc_info=e)

        return logs

    async def _get_robot_part_logs(self, robot_part_id: str, filter: str, errors_only: bool, page_token: str) -> Tuple[List[LogEntry], str]:
        request = GetRobotPartLogsRequest(id=robot_part_id, errors_only=errors_only, filter=filter, page_token=page_token)
        response: GetRobotPartLogsResponse = await self._app_client.GetRobotPartLogs(request, metadata=self._metadata)
        return [LogEntry.from_proto(log) for log in response.logs], response.next_page_token

    # Unary-stream method.
    async def tail_robot_part_logs(self):
        raise NotImplementedError()

    async def get_robot_part_history(self, robot_part_id: str) -> List[RobotPartHistoryEntry]:
        """Get a list containing the history of a robot part.

        Args:
            robot_part_id (str): ID of the robot part to retrieve history from.

        Raises:
            GRPCError: If an invalid robot_part_id is provided.

        Returns:
            List[viam.app.app_client.RobotPartHistoryEntry]: The list of the robot part's history.
        """
        request = GetRobotPartHistoryRequest(id=robot_part_id)
        response: GetRobotPartHistoryResponse = await self._app_client.GetRobotPartHistory(request, metadata=self._metadata)
        return [RobotPartHistoryEntry.from_proto(part_history) for part_history in response.history]

    async def update_robot_part(self, robot_part_id: str, name: str, robot_config: Optional[Mapping[str, Any]] = None) -> RobotPart:
        """Change the name and assign an optional new configuration to a robot part.

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

        Args:
            robot_part_id (str): ID of the robot part to delete. Must be specified.

        Raises:
            GRPCError: If an invalid robot part ID is passed.
        """
        request = DeleteRobotPartRequest(part_id=robot_part_id)
        await self._app_client.DeleteRobotPart(request, metadata=self._metadata)

    async def mark_part_as_main(self, robot_part_id: str) -> None:
        """Mark a robot part as the main part of a robot.

        Args:
            robot_part_id (str): ID of the robot part to mark as main.

        Raises:
            GRPCError: If an invalid robot part ID is passed.
        """
        request = MarkPartAsMainRequest(part_id=robot_part_id)
        await self._app_client.MarkPartAsMain(request, metadata=self._metadata)

    async def mark_part_for_restart(self, robot_part_id: str) -> None:
        """Mark the specified robot part for restart.

        Args:
            robot_part_id (str): ID of the robot part to mark for restart.

        Raises:
            GRPCError: If an invalid robot part ID is passed.
        """
        request = MarkPartForRestartRequest(part_id=robot_part_id)
        await self._app_client.MarkPartForRestart(request, metadata=self._metadata)

    async def create_robot_part_secret(self, robot_part_id: str) -> RobotPart:
        """Create a robot part secret.

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

        Args:
            robot_id (str): ID of the robot to delete.

        Raises:
            GRPCError: If an invalid robot ID is passed.
        """
        request = DeleteRobotRequest(id=robot_id)
        await self._app_client.DeleteRobot(request, metadata=self._metadata)

    async def list_fragments(self, organization_id: str, show_public: bool = True) -> List[Fragment]:
        """Get a list of fragments under the specified organization.

        Args:
            organization_id (str): ID of the organization under which to list the fragments.
            show_public: Optional boolean specifiying whether or not to only show public fragments. If True, only public fragments will
                return. If False, only private fragments will return. Defaults to True.

        Raises:
            GRPCError: If an invalid organization ID is passed.

        Returns:
            List[viam.app.app_client.Fragment]: The list of fragments.
        """
        request = ListFragmentsRequest(organization_id=organization_id, show_public=show_public)
        response: ListFragmentsResponse = await self._app_client.ListFragments(request, metadata=self._metadata)
        return [Fragment.from_proto(fragment=fragment) for fragment in response.fragments]

    async def get_fragment(self, fragment_id: str) -> Fragment:
        """Get a fragment.

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

    # TODO: Fragments are currently able to have the empty string "" as a name.
    async def create_fragment(self, name: str, organization_id: str, config: Optional[Mapping[str, Any]] = None) -> Fragment:
        """Create a new private fragment.

        Args:
            name (str): Name of the fragment.
            config (Optional[Mapping[str, Any]]): _description_
            organization_id (str): ID of the organization to own the fragment.

        Raises:
            GRPCError: If an invalid organization ID is provided.

        Returns:
            viam.app.app_client.Fragment: The newly created fragment.
        """
        request = CreateFragmentRequest(name=name, config=dict_to_struct(config) if config else None, organization_id=organization_id)
        response: CreateFragmentResponse = await self._app_client.CreateFragment(request, metadata=self._metadata)
        return Fragment.from_proto(response.fragment)

    # TODO: It doesn't make sense that the name HAS to be updated and can't be empty.
    async def update_fragment(
        self, fragment_id: str, name: str, config: Optional[Mapping[str, Any]] = None, public: Optional[bool] = None
    ) -> Fragment:
        """Update a fragment name AND its

        Args:
            fragment_id (str): ID of the fragment to be updated.
            name (str): New name to associate with the fragment.
            config (Optional[Mapping[str, Any]]): Optional Dictionary representation of new config to assign to specified fragment. Not
                passing this parameter will leave it unchanged.
            public (bool): Boolean specifying whether the fragment is public. Not passing this parameter will leave it unchanged. A fragment
                is private by default when created.

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

        Args:
            fragment_id (str): ID of the fragment to delete.

        Raises:
            GRPCError: If an invalid fragment ID is passed.
        """
        request = DeleteFragmentRequest(id=fragment_id)
        await self._app_client.DeleteFragment(request, metadata=self._metadata)

    async def add_role(self, identity_id: str, role: str, resource_type: str, resource_id: str, organization_id: str) -> None:
        """Add a role under organization.

        Args:
            identity_id (str): ID of the entity the role belongs to (e.g., a user ID).
            role (str): The role to add (i.e., either "owner" or "operator").
            resource_type (str): Type of the resource to add role to (i.e., either "organization", "location", or "robot"). Must match
                `resource_id`.
            resource_id (str): ID of the resource the role applies to (i.e., either an organization, location, or robot ID).
            organization_id (str): ID of the organization the role will be housed under. Must be the organization caller is authenticated
                against.

        Raises:
            GRPCError: If either an invalid identity ID, role ID, resource type, resource ID, or organization ID is passed.
        """
        authorization = Authorization(
            identity_id=identity_id,
            authorization_id=f"{resource_type}_{role}",
            resource_type=resource_type,
            resource_id=resource_id,
            organization_id=organization_id
        )
        request = AddRoleRequest(authorization=authorization)
        await self._app_client.AddRole(request, metadata=self._metadata)

    async def remove_role(self, identity_id: str, role: str, resource_type: str, resource_id: str, organization_id: str) -> None:
        """Remove a role under organization.

        Args:
            identity_id (str): ID of the entity the role belongs to (e.g., a user ID).
            role (str): The role to remove (i.e., either "owner" or "operator").
            resource_type (str): Type of the resource to remove role from (i.e., either "organization", "location", or "robot"). Must match
                `resource_id`.
            resource_id (str): ID of the resource the role applies to (i.e., either an organization, location, or robot ID).
            organization_id (str): ID of the organization the role is housed under. Must be the organization caller is authenticated
                against.

        Raises:
            GRPCError: If either an invalid identity ID, role ID, resource type, resource ID, or organization ID is passed.
        """
        authorization = Authorization(
            identity_id=identity_id,
            authorization_id=f"{resource_type}_{role}",
            resource_type=resource_type,
            resource_id=resource_id,
            organization_id=organization_id
        )
        request = RemoveRoleRequest(authorization=authorization)
        await self._app_client.RemoveRole(request, metadata=self._metadata)

    # TODO: This method reveals user ID's.
    async def list_authorizations(self, organization_id: str, resource_ids: Optional[List[str]] = None) -> List[Authorization]:
        """List all authorizations under a specific resource (or resources) within an organization. If no resource IDs are provided, all
        resource authorizations within the organizations are returned.

        Args:
            organization_id (str): ID of the organization to retrieve resource authorizations from.
            resource_ids (Optional[List[str]]): IDs of the resources to retrieve authorizations from. Defaults to None.

        Raises:
            GRPCError: If an invalid organization ID or resource ID is passed.

        Returns:
            List[Authorization]: The list of authorizations.
        """
        request = ListAuthorizationsRequest(organization_id=organization_id, resource_ids=resource_ids)
        response: ListAuthorizationsResponse = await self._app_client.ListAuthorizations(request, metadata=self._metadata)
        return list(response.authorizations)

    # TODO: Test, check optionality, and finish docstring.
    async def check_permissions(self, permissions: Optional[List[AuthorizedPermissions]]) -> List[AuthorizedPermissions]:
        """

        Args:
            permissions (Optional[List[AuthorizedPermissions]]):

        Returns:
            List[viam.proto.app.AuthorizedPermissions]:
        """
        request = CheckPermissionsRequest(permissions=permissions)
        response: CheckPermissionsResponse = await self._app_client.CheckPermissions(request, metadata=self._metadata)
        return list(response.authorized_permissions)

    # TODO: Test
    async def create_module(self, organization_id: str, name: str) -> Tuple[str, str]:
        """Create a module

        Args:
            organization_id (str): The organization to create the module under.
            name (str): The name of the module, which must be unique within your organization.

        Raises:
            GRPCError: If either an invalid organization ID or name is passed.

        Returns:
            Tuple[str, str]: A tuple containing the ID [0] of the new module and its URL [1].
        """
        request = CreateModuleRequest(organization_id=organization_id, name=name)
        response: CreateModuleResponse = await self._app_client.CreateModule(request, metadata=self._metadata)
        return response.module_id, response.url

    # TODO: Test, check optionality, finish docstring, and figure out what visibility is.
    async def update_module(
        self,
        module_id: str,
        organization_id: Optional[str],
        visibility: Any,
        url: str,
        description: str,
        models: Optional[List[Model]],
        entrypoint: str,
    ) -> str:
        """

        Args:
            module_id (str): ID of the module being updated, containing module name or namespace and module name.
            organization_id (Optional[str]): ID of organization of the module being updated, required if no namespace exists in the
                module_id.
            visibility (Any): The visibility that should be set for the module.
            url (str): The url to reference for documentation and code.
            description (str): A short description of the module that explains its purpose.
            models (Optional[List[Model]]):
            entrypoint (str):

        Raises:
            GRPCError:

        Returns:
            str: The URL of the newly updated module.
        """
        request = UpdateModuleRequest(
            module_id=module_id,
            organization_id=organization_id,
            visibility=visibility,
            description=description,
            models=models,
            entrypoint=entrypoint,
        )
        response: UpdateModuleResponse = await self._app_client.UpdateModule(request, metadata=self._metadata)
        return response.url

    # Stream-unary method.
    async def upload_module_file(self, module_file_info: Optional[ModuleFileInfo], file: bytes) -> str:
        """Upload a module file

        Args:
            module_file_info (Optional[viam.proto.app.ModuleFileInfo]): Relevant metadata.
            file (bytes): Bytes of file to upload.

        Returns:
            str: ID of uploaded file.
        """
        request_metadata = UploadModuleFileRequest(module_file_info=module_file_info)
        request_file = UploadModuleFileRequest(file=file)
        async with self._app_client.UploadModuleFile.open(metadata=self._metadata) as stream:
            await stream.send_message(request_metadata)
            await stream.send_message(request_file)
            response = await stream.recv_message()
            assert response is not None
            return response.url

    # TODO: Test
    async def get_module(self, module_id: str, organization_id: str) -> Module:
        """Get a module.

        Args:
            module_id (str): ID of the module being retrieved, containing module name or namespace and module name.
            organization_id (str): ID of the organization of the module being retrieved, required if no namespace exists in the module_id.

        Raises:
            GRPCError: If either an invalid module ID or organization ID is passed.

        Returns:
            viam.proto.app.Module: The module.
        """
        request = GetModuleRequest(module_id=module_id, organization_id=organization_id)
        response: GetModuleResponse = await self._app_client.GetModule(request, metadata=self._metadata)
        return response.module

    async def list_modules(self, organization_id: str) -> List[Module]:
        """List the modules under an organization.

        Args:
            organization_id (str): ID of the organization to return private modules for.

        Raises:
            GRPCError: If an invalid of organization ID is passed.

        Returns:
            List[viam.proto.app.Module]: The list of modules.
        """
        request = ListModulesRequest(organization_id=organization_id)
        response: ListModulesResponse = await self._app_client.ListModules(request, metadata=self._metadata)
        return list(response.modules)

    @staticmethod
    def create_authorized_permission() -> AuthorizedPermissions:
        return AuthorizedPermissions()
