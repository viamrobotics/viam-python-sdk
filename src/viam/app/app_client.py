import json
from collections.abc import AsyncIterator, Mapping
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Literal, TypeAlias

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
    DeleteDevicePushTokenRequest,
    DeleteDevicePushTokenResponse,
    DeleteFirebaseConfigRequest,
    DeleteFirebaseConfigResponse,
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
    FragmentImport,
    FragmentImportList,
    GetDevicePushTokensRequest,
    GetDevicePushTokensResponse,
    GetFirebaseConfigRequest,
    GetFirebaseConfigResponse,
    GetFragmentHistoryRequest,
    GetFragmentHistoryResponse,
    GetFragmentRequest,
    GetFragmentResponse,
    GetLocationMetadataRequest,
    GetLocationMetadataResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetModuleRequest,
    GetModuleResponse,
    GetOrganizationMetadataRequest,
    GetOrganizationMetadataResponse,
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
    GetRobotMetadataRequest,
    GetRobotMetadataResponse,
    GetRobotPartHistoryRequest,
    GetRobotPartHistoryResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    GetRobotPartMetadataRequest,
    GetRobotPartMetadataResponse,
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
    RotateKeyRequest,
    RotateKeyResponse,
    RoverRentalRobot,
    SetFirebaseConfigRequest,
    SetFirebaseConfigResponse,
    SharedSecret,
    ShareLocationRequest,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
    UnshareLocationRequest,
    UpdateFragmentRequest,
    UpdateFragmentResponse,
    UpdateLocationMetadataRequest,
    UpdateLocationMetadataResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateModuleRequest,
    UpdateModuleResponse,
    UpdateOrganizationInviteAuthorizationsRequest,
    UpdateOrganizationInviteAuthorizationsResponse,
    UpdateOrganizationMetadataRequest,
    UpdateOrganizationMetadataResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    UpdateRegistryItemRequest,
    UpdateRobotMetadataRequest,
    UpdateRobotMetadataResponse,
    UpdateRobotPartMetadataRequest,
    UpdateRobotPartMetadataResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    UploadDevicePushTokenRequest,
    UploadDevicePushTokenResponse,
    UploadModuleFileRequest,
    Visibility,
)
from viam.proto.app import Fragment as FragmentPB
from viam.proto.app import FragmentHistoryEntry as FragmentHistoryEntryPB
from viam.proto.app import FragmentVisibility as FragmentVisibilityPB
from viam.proto.app import RobotPart as RobotPartPB
from viam.proto.app import RobotPartHistoryEntry as RobotPartHistoryEntryPB
from viam.proto.app.packages import PackageType
from viam.proto.common import LogEntry as LogEntryPB
from viam.utils import ValueTypes, datetime_to_timestamp, dict_to_struct, struct_to_dict

LOGGER = logging.getLogger(__name__)

_ROLE_TYPE: TypeAlias = Literal["owner", "operator"]
_RESOURCE_TYPE_TYPE: TypeAlias = Literal["organization", "location", "robot"]


@dataclass
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
        self = cls(
            id=robot_part.id,
            name=robot_part.name,
            dns_name=robot_part.dns_name,
            secret=robot_part.secret,
            robot=robot_part.robot,
            location_id=robot_part.location_id,
            robot_config=struct_to_dict(robot_part.robot_config) if robot_part.HasField("robot_config") else None,
            last_access=robot_part.last_access.ToDatetime() if robot_part.HasField("last_access") else None,
            user_supplied_info=struct_to_dict(robot_part.user_supplied_info) if robot_part.HasField("user_supplied_info") else None,
            main_part=robot_part.main_part,
            fqdn=robot_part.fqdn,
            local_fqdn=robot_part.local_fqdn,
            created_on=robot_part.created_on.ToDatetime() if robot_part.HasField("created_on") else None,
            secrets=list(robot_part.secrets),
            last_updated=robot_part.last_updated.ToDatetime() if robot_part.HasField("last_updated") else None,
            robot_config_json=robot_part.robot_config_json if robot_part.HasField("robot_config_json") else None,
        )
        return self

    id: str
    name: str
    dns_name: str
    secret: str
    robot: str
    location_id: str
    robot_config: Mapping[str, ValueTypes] | None
    last_access: datetime | None
    user_supplied_info: Mapping[str, ValueTypes] | None
    main_part: bool
    fqdn: str
    local_fqdn: str
    created_on: datetime | None
    secrets: list[SharedSecret] | None
    last_updated: datetime | None
    robot_config_json: str | None

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
            last_updated=datetime_to_timestamp(self.last_updated) if self.last_updated else None,
            robot_config_json=self.robot_config_json if self.robot_config_json else None,
        )


@dataclass
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
        return cls(
            host=log_entry.host,
            level=log_entry.level,
            time=log_entry.time.ToDatetime() if log_entry.HasField("time") else None,
            logger_name=log_entry.logger_name,
            message=log_entry.message,
            caller=struct_to_dict(log_entry.caller) if log_entry.HasField("caller") else None,
            stack=log_entry.stack,
            fields=[struct_to_dict(field) for field in log_entry.fields],
        )

    host: str
    level: str
    time: datetime | None
    logger_name: str
    message: str
    caller: Mapping[str, ValueTypes] | None
    stack: str
    fields: list[Mapping[str, ValueTypes]] | None

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


@dataclass
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
        return cls(
            id=fragment.id,
            name=fragment.name,
            fragment=struct_to_dict(fragment.fragment) if fragment.HasField("fragment") else None,
            organization_owner=fragment.organization_owner,
            public=fragment.public,
            created_on=fragment.created_on.ToDatetime() if fragment.HasField("created_on") else None,
            organization_name=fragment.organization_name,
            robot_part_count=fragment.robot_part_count,
            organization_count=fragment.organization_count,
            only_used_by_owner=fragment.only_used_by_owner,
            visibility=Fragment.Visibility.from_proto(fragment.visibility),
            last_updated=fragment.last_updated.ToDatetime() if fragment.HasField("last_updated") else None,
        )

    id: str
    name: str
    fragment: Mapping[str, ValueTypes] | None
    organization_owner: str
    public: bool
    created_on: datetime | None
    organization_name: str
    robot_part_count: int
    organization_count: int
    only_used_by_owner: bool
    visibility: "Fragment.Visibility"
    last_updated: datetime | None

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
            last_updated=datetime_to_timestamp(self.last_updated) if self.last_updated else None,
        )


@dataclass
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
        return cls(
            fragment=fragment_history_entry.fragment,
            edited_on=fragment_history_entry.edited_on.ToDatetime(),
            old=Fragment.from_proto(fragment_history_entry.old),
            edited_by=fragment_history_entry.edited_by,
        )

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


@dataclass
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
        return cls(
            part=robot_part_history_entry.part,
            robot=robot_part_history_entry.robot,
            when=robot_part_history_entry.when.ToDatetime() if robot_part_history_entry.HasField("when") else None,
            old=RobotPart.from_proto(robot_part_history_entry.old) if robot_part_history_entry.HasField("old") else None,
        )

    part: str
    robot: str
    when: datetime | None
    old: RobotPart | None

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
        role: _ROLE_TYPE,
        resource_type: _RESOURCE_TYPE_TYPE,
        resource_id: str,
    ):
        """role (_ROLE_TYPE): The role to add.
        resource_type (_RESOURCE_TYPE_TYPE): Type of the resource to add role to.
            Must match `resource_id`.
        resource_id (str): ID of the resource the role applies to (that is, either an organization, location, or robot ID).
        """
        self._role = role
        self._resource_type = resource_type
        self._resource_id = resource_id

    _role: _ROLE_TYPE
    _resource_type: _RESOURCE_TYPE_TYPE
    _resource_id: str

    @property
    def role(self) -> _ROLE_TYPE:
        return self._role

    @property
    def resource_type(self) -> _RESOURCE_TYPE_TYPE:
        return self._resource_type

    @property
    def resource_id(self) -> str:
        return self._resource_id


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
            async with await connect() as viam_client:
                # Instantiate an AppClient called "cloud" to run cloud app API methods on
                cloud = viam_client.app_client

        if __name__ == '__main__':
            asyncio.run(main())

    For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/>`_.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create an `AppClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._app_client = AppServiceStub(channel)
        self._channel = channel

    _app_client: AppServiceStub
    _metadata: Mapping[str, str]
    _channel: Channel
    _organization_id: str | None = None

    async def _create_authorization(
        self,
        organization_id: str,
        identity_id: str,
        identity_type: str,
        role: _ROLE_TYPE,
        resource_type: _RESOURCE_TYPE_TYPE,
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
            role=auth.role,
            resource_type=auth.resource_type,
            resource_id=auth.resource_id,
        )

    async def get_user_id_by_email(self, email: str) -> str:
        """Get the ID of a user by email.

        ::

            id = await cloud.get_user_id_by_email("youremail@email.com")

        Args:
            email (str): The email of the user.

        Returns:
            str: The ID of the user.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getuseridbyemail>`_.
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

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createorganization>`_.
        """
        request = CreateOrganizationRequest(name=name)
        response: CreateOrganizationResponse = await self._app_client.CreateOrganization(request, metadata=self._metadata)
        return response.organization

    async def list_organizations(self) -> list[Organization]:
        """List the organization(s) the user is an authorized owner of.

        ::

            org_list = await cloud.list_organizations()

        Returns:
            list[viam.proto.app.Organization]: The list of organizations.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listorganizations>`_.
        """
        request = ListOrganizationsRequest()
        response: ListOrganizationsResponse = await self._app_client.ListOrganizations(request, metadata=self._metadata)
        return list(response.organizations)

    async def get_organizations_with_access_to_location(self, location_id: str) -> list[OrganizationIdentity]:
        """Get all organizations that have access to a location.

        ::

            org_list = await cloud.get_organizations_with_access_to_location("location-id")

        Args:
            location_id (str): The ID of the location.

        Returns:
            list[viam.proto.app.OrganizationIdentity]: The list of organizations.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getorganizationswithaccesstolocation>`_.
        """
        request = GetOrganizationsWithAccessToLocationRequest(location_id=location_id)
        response: GetOrganizationsWithAccessToLocationResponse = await self._app_client.GetOrganizationsWithAccessToLocation(
            request, metadata=self._metadata
        )
        return list(response.organization_identities)

    async def list_organizations_by_user(self, user_id: str) -> list[OrgDetails]:
        """List the organizations a user belongs to.

        ::

            org_list = await cloud.list_organizations_by_user("<YOUR-USER-ID>")

        Args:
            user_id (str): The ID of the user. You can retrieve this with the get_user_id_by_email() method.

        Returns:
            list[OrgDetails]: The list of organizations.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listorganizationsbyuser>`_.
        """
        request = ListOrganizationsByUserRequest(user_id=user_id)
        response: ListOrganizationsByUserResponse = await self._app_client.ListOrganizationsByUser(request, metadata=self._metadata)
        return list(response.orgs)

    async def get_organization(self, org_id: str) -> Organization:
        """Retrieve the organization object for the requested organization containing the organization's ID,
        name, public namespace, and more.

        ::

            org = await cloud.get_organization("<YOUR-ORG-ID>")

        Args:
            org_id (str): The ID of the organization to query. You can retrieve this from the organization settings page.

        Raises:
            GRPCError: If the provided org_id is invalid, or not currently authed to.

        Returns:
            viam.proto.app.Organization: The requested organization.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getorganization>`_.
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
            public_namespace (str): Organization namespace to check. Namespaces can only contain lowercase alphanumeric and dash
                characters.

        Raises:
            GRPCError: If an invalid namespace (for example, "") is provided.

        Returns:
            bool: True if the provided namespace is available.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getorganizationnamespaceavailability>`_.
        """
        request = GetOrganizationNamespaceAvailabilityRequest(public_namespace=public_namespace)
        response: GetOrganizationNamespaceAvailabilityResponse = await self._app_client.GetOrganizationNamespaceAvailability(
            request, metadata=self._metadata
        )
        return response.available

    async def update_organization(
        self,
        org_id: str,
        name: str | None = None,
        public_namespace: str | None = None,
        region: str | None = None,
        cid: str | None = None,
        default_fragments: list[FragmentImport] | None = None,
    ) -> Organization:
        """Updates organization details.

        ::

            organization = await cloud.update_organization(
                org_id="<YOUR-ORG-ID>",
                name="Artoo's Org",
                public_namespace="artoo"
            )

        Args:
            org_id (str): The ID of the organization to update.
            name (str | None): If provided, updates the org's name.
            public_namespace (str | None): If provided, sets the org's namespace if it hasn't already been set.
            region (str | None): If provided, updates the org's region.
            cid (str | None): If provided, update's the org's CRM ID.

        Raises:
            GRPCError: If the org's namespace has already been set, or if the provided namespace is already taken.

        Returns:
            viam.proto.app.Organization: The updated organization.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#updateorganization>`_.
        """
        request = UpdateOrganizationRequest(
            organization_id=org_id,
            public_namespace=public_namespace,
            region=region,
            cid=cid,
            name=name,
            default_fragments=(FragmentImportList(fragments=default_fragments) if default_fragments is not None else None),
        )
        response: UpdateOrganizationResponse = await self._app_client.UpdateOrganization(request, metadata=self._metadata)
        return response.organization

    async def delete_organization(self, org_id: str) -> None:
        """Delete an organization

        ::

            await cloud.delete_organization("<YOUR-ORG-ID>")

        Args:
            org_id (str): The ID of the organization.
                You can obtain your organization ID from the organization settings page.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deleteorganization>`_.
        """
        request = DeleteOrganizationRequest(organization_id=org_id)
        await self._app_client.DeleteOrganization(request, metadata=self._metadata)

    async def list_organization_members(self, org_id: str) -> tuple[list[OrganizationMember], list[OrganizationInvite]]:
        """List the members and invites of the currently authed-to organization.

        ::

            member_list, invite_list = await cloud.list_organization_members("<YOUR-ORG-ID>")

        Args:
            org_id (str): The ID of the organization to list members of.
                You can obtain your organization ID from the organization settings page.

        Returns:
            tuple[list[viam.proto.app.OrganizationMember], list[viam.proto.app.OrganizationInvite]]: A tuple containing two lists; the first
            [0] of organization members, and the second [1] of organization invites.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listorganizationmembers>`_.
        """
        request = ListOrganizationMembersRequest(organization_id=org_id)
        response: ListOrganizationMembersResponse = await self._app_client.ListOrganizationMembers(request, metadata=self._metadata)
        return list(response.members), list(response.invites)

    async def create_organization_invite(
        self,
        org_id: str,
        email: str,
        authorizations: list[Authorization] | None = None,
        send_email_invite: bool = True,
    ) -> OrganizationInvite:
        """Creates an organization invite and sends it via email.

        ::

            await cloud.create_organization_invite("<YOUR-ORG-ID>", "youremail@email.com")

        Args:
            org_id (str): The ID of the organization to create an invite for.
                You can obtain your organization ID from the organization settings page.
            email (str): The email address to send the invite to.
            authorizations (list[viam.proto.app.Authorization] | None): Specifications of the
                authorizations to include in the invite. If not provided, full owner permissions will
                be granted.
            send_email_invite (bool | None): Whether or not an email should be sent to the recipient of an invite.
                The user must accept the email to be added to the associated authorizations.
                When set to false, the user automatically receives the associated authorization
                on the next login of the user with the associated email address.

        Raises:
            GRPCError: if an invalid email is provided, or if the user is already a member of the org.

        Returns:
            OrganizationInvite: The organization invite.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createorganizationinvite>`_.
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
        add_authorizations: list[Authorization] | None = None,
        remove_authorizations: list[Authorization] | None = None,
    ) -> OrganizationInvite:
        """Update the authorizations attached to an organization invite that has already been created.

        Note that an invite can only have one authorization at each resource (for example, organization, location, robot, etc.) level and
        must have at least one authorization overall.

        ::

            from viam.proto.app import Authorization

            auth = Authorization(
                authorization_type="role",
                authorization_id="location_owner",
                resource_type="location", # "robot", "location", or "organization"
                resource_id="012456lni0", # machine id, location id or org id
                identity_id="",
                organization_id="<YOUR-ORG-ID>",
                identity_type=""
            )

            update_invite = await cloud.update_organization_invite_authorizations(
                org_id="<YOUR-ORG-ID>",
                email="notarealemail@viam.com",
                add_authorizations=[auth]
            )

        Args:
            org_id (str): The ID of the organization that the invite is for.
                You can obtain your organization ID from the organization settings page.
            email (str): Email of the user the invite was sent to.
            add_authorizations (list[viam.proto.app.Authorization] | None): Optional list of authorizations to add to the invite.
            remove_authorizations (list[viam.proto.app.Authorization] | None): Optional list of authorizations to remove from the invite.

        Raises:
            GRPCError: If no authorizations are passed or if an invalid combination of authorizations is passed (for example an
                authorization to remove when the invite only contains one authorization).

        Returns:
            viam.proto.app.OrganizationInvite: The updated invite.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#updateorganizationinviteauthorizations>`_.
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

            member_list, invite_list = await cloud.list_organization_members(org_id="<YOUR-ORG-ID>")
            first_user_id = member_list[0].user_id

            await cloud.delete_organization_member(org_id="org_id", user_id=first_user_id)

        Args:
            org_id (str): The ID of the org to remove the user from.
                You can obtain your organization ID from the organization settings page.
            user_id (str): The ID of the user to remove.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deleteorganizationmember>`_.
        """
        request = DeleteOrganizationMemberRequest(organization_id=org_id, user_id=user_id)
        await self._app_client.DeleteOrganizationMember(request, metadata=self._metadata)

    async def delete_organization_invite(self, org_id: str, email: str) -> None:
        """Deletes a pending organization invite.

        ::

            await cloud.delete_organization_invite("<YOUR-ORG-ID>", "youremail@email.com")

        Args:
            org_id (str): The ID of the organization that the invite to delete was for.
                You can obtain your organization ID from the organization settings page.
            email (str): The email address the pending invite was sent to.

        Raises:
            GRPCError: If no pending invite is associated with the provided email address.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deleteorganizationinvite>`_.
        """
        request = DeleteOrganizationInviteRequest(organization_id=org_id, email=email)
        await self._app_client.DeleteOrganizationInvite(request, metadata=self._metadata)

    async def resend_organization_invite(self, org_id: str, email: str) -> OrganizationInvite:
        """Re-sends a pending organization invite email.

        ::

            org_invite = await cloud.resend_organization_invite("<YOUR-ORG-ID>", "youremail@email.com")

        Args:
            org_id (str): The ID of the organization that the invite to resend was for.
                You can obtain your organization ID from the organization settings page.
            email (str): The email address associated with the invite.

        Raises:
            GRPCError: If no pending invite is associated with the provided email address.

        Returns:
            viam.proto.app.OrganizationInvite: The organization invite sent.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#resendorganizationinvite>`_.
        """
        request = ResendOrganizationInviteRequest(organization_id=org_id, email=email)
        response: ResendOrganizationInviteResponse = await self._app_client.ResendOrganizationInvite(request, metadata=self._metadata)
        return response.invite

    async def create_location(self, org_id: str, name: str, parent_location_id: str | None = None) -> Location:
        """Create and name a location under the currently authed-to organization and the specified parent location.

        ::

            my_new_location = await cloud.create_location(org_id="<YOUR-ORG-ID>", name="Robotville", parent_location_id="111ab12345")

        Args:
            org_id (str): The ID of the organization to create the location under.
                You can obtain your organization ID from the organization settings page.
            name (str): Name of the location.
            parent_location_id (str | None): Optional parent location to put the location under. Defaults to a root-level location if no
                location ID is provided.

        Raises:
            GRPCError: If either an invalid name (for example, ""), or parent location ID (for example, a nonexistent ID) is passed.

        Returns:
            viam.proto.app.Location: The newly created location.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createlocation>`_.
        """
        request = CreateLocationRequest(organization_id=org_id, name=name, parent_location_id=parent_location_id)
        response: CreateLocationResponse = await self._app_client.CreateLocation(request, metadata=self._metadata)
        return response.location

    async def get_location(self, location_id: str | None = None) -> Location:
        """Get a location.

        ::

            location = await cloud.get_location(location_id="123ab12345")

        Args:
            location_id (str | None): ID of the location to get. Defaults to the location ID provided at `AppClient` instantiation.

        Raises:
            GRPCError: If an invalid location ID is passed or if one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            viam.proto.app.Location: The location.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getlocation>`_.
        """
        request = GetLocationRequest(location_id=location_id if location_id else "")
        response: GetLocationResponse = await self._app_client.GetLocation(request, metadata=self._metadata)
        return response.location

    async def update_location(self, location_id: str, name: str | None = None, parent_location_id: str | None = None) -> Location:
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
            name (str | None): Optional new name to be updated on the location. Defaults to the empty string "" (that is, the name
                doesn't change).
            parent_location_id(str | None): Optional ID of new parent location to move the location under. Defaults to the empty string
                "" (that is, no new parent location is assigned).

        Raises:
            GRPCError: If either an invalid location ID, name, or parent location ID is passed.

        Returns:
            viam.proto.app.Location: The newly updated location.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#updatelocation>`_.
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

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deletelocation>`_.
        """
        request = DeleteLocationRequest(location_id=location_id)
        await self._app_client.DeleteLocation(request, metadata=self._metadata)

    async def list_locations(self, org_id: str) -> list[Location]:
        """Get a list of all locations under the currently authed-to organization.

        ::

            locations = await cloud.list_locations("<YOUR-ORG-ID>")

        Args:
            org_id (str): The ID of the org to list locations for.
                You can obtain your organization ID from the organization settings page.

        Returns:
            list[viam.proto.app.Location]: The list of locations.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listlocations>`_.
        """
        request = ListLocationsRequest(organization_id=org_id)
        response: ListLocationsResponse = await self._app_client.ListLocations(request, metadata=self._metadata)
        return list(response.locations)

    async def share_location(self, organization_id: str, location_id: str) -> None:
        """Share a location with an organization.

        ::

            await cloud.share_location("<YOUR-ORG-ID>", "<YOUR-LOCATION-ID>")

        Args:
            organization_id (str): The ID of the organization.
            location_id (str): The ID of the location.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#sharelocation>`_.
        """
        request = ShareLocationRequest(location_id=location_id, organization_id=organization_id)
        await self._app_client.ShareLocation(request, metadata=self._metadata)

    async def unshare_location(self, organization_id: str, location_id: str) -> None:
        """Stop sharing a location with an organization.

        ::

            await cloud.unshare_location("<YOUR-ORG-ID>", "<YOUR-LOCATION-ID>")

        Args:
            organization_id (str): The ID of the organization.
            location_id (str): The ID of the location.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#unsharelocation>`_.
        """
        request = UnshareLocationRequest(location_id=location_id, organization_id=organization_id)
        await self._app_client.UnshareLocation(request, metadata=self._metadata)

    async def location_auth(self, location_id: str | None = None) -> LocationAuth:
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

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#locationauth>`_.
        """
        request = LocationAuthRequest(location_id=location_id if location_id else "")
        response: LocationAuthResponse = await self._app_client.LocationAuth(request, metadata=self._metadata)
        return response.auth

    async def create_location_secret(self, location_id: str | None = None) -> LocationAuth:
        """Create a new location secret.

        ::

            new_loc_auth = await cloud.create_location_secret(location_id="123xy12345")

        Args:
            location_id (str | None): ID of the location to generate a new secret for. Defaults to the location ID provided at
                `AppClient` instantiation.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            viam.proto.app.LocationAuth: The specified location's `LocationAuth` containing the newly created secret.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createlocationsecret>`_.
        """
        request = CreateLocationSecretRequest(location_id=location_id if location_id else "")
        response: CreateLocationSecretResponse = await self._app_client.CreateLocationSecret(request, metadata=self._metadata)
        return response.auth

    async def delete_location_secret(self, secret_id: str, location_id: str | None = None) -> None:
        """Delete a location secret.

        ::

            await cloud.delete_location_secret(
                secret_id="abcd123-456-7890ab-cxyz98-989898xyzxyz",
                location_id="123xy12345"
            )

        Args:
            location_id (str): ID of the location to delete secret from. Defaults to the location ID provided at `AppClient` instantiation.
            secret_id (str): ID of the secret to delete.

        Raises:
            GRPCError: If either an invalid location ID or secret ID is passed or a location ID isn't passed and there was no location
                ID provided at `AppClient` instantiation.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deletelocationsecret>`_.
        """
        request = DeleteLocationSecretRequest(location_id=location_id if location_id else "", secret_id=secret_id)
        await self._app_client.DeleteLocationSecret(request, metadata=self._metadata)

    async def get_robot(self, robot_id: str) -> Robot:
        """Get a machine.

        ::

            machine = await cloud.get_robot(robot_id="1a123456-x1yz-0ab0-a12xyzabc")

        Args:
            robot_id (str): ID of the machine to get. You can copy this value from the URL of the machine's page.

        Raises:
            GRPCError: If an invalid machine ID is passed.

        Returns:
            viam.proto.app.Robot: The machine.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getrobot>`_.
        """
        request = GetRobotRequest(id=robot_id)
        response: GetRobotResponse = await self._app_client.GetRobot(request, metadata=self._metadata)
        return response.robot

    async def get_rover_rental_robots(self, org_id: str) -> list[RoverRentalRobot]:
        """Returns a list of rover rental robots within an org.

        ::

            rental_robots = await cloud.get_rover_rental_robots()

        Args:
            org_id (str): The ID of the organization to list rover rental robots for.
                You can obtain your organization ID from the organization settings page.

        Returns:
            list[viam.proto.app.RoverRentalRobot]: The list of rover rental robots.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/>`_.
        """
        request = GetRoverRentalRobotsRequest(org_id=org_id)
        response: GetRoverRentalRobotsResponse = await self._app_client.GetRoverRentalRobots(request, metadata=self._metadata)
        return list(response.robots)

    async def get_robot_parts(self, robot_id: str) -> list[RobotPart]:
        """Get a list of all the parts under a specific machine.

        ::

            list_of_parts = await cloud.get_robot_parts(
                robot_id="1a123456-x1yz-0ab0-a12xyzabc"
            )

        Args:
            robot_id (str): ID of the machine to get parts from.

        Raises:
            GRPCError: If an invalid machine ID is passed.

        Returns:
            list[viam.app.app_client.RobotPart]: The list of machine parts.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getrobotparts>`_.
        """
        request = GetRobotPartsRequest(robot_id=robot_id)
        response: GetRobotPartsResponse = await self._app_client.GetRobotParts(request, metadata=self._metadata)
        return [RobotPart.from_proto(robot_part=part) for part in response.parts]

    async def get_robot_part(self, robot_part_id: str, dest: str | None = None, indent: int = 4) -> RobotPart:
        """Get a machine part including its part config, part address, and other information.

        ::

            my_robot_part = await cloud.get_robot_part(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22"
            )
            # Get the part's config
            machine_part_config = my_robot_part.robot_config
            # Get the part's address
            address = my_robot_part.fqdn
            # Check if machine is live (last access time less than 10 sec ago)
            if (time.time() - my_robot_part.last_access.timestamp()) <= 10:
                print("Machine is live.")

        Args:
            robot_part_id (str): ID of the machine part to get. You can retrieve this value by navigating to the machine's page,
                clicking on the part status dropdown, and clicking the copy icon next to Part ID.
            dest (str | None): Optional filepath to write the machine part's config file in JSON format to.
            indent (int): Size (in number of spaces) of indent when writing config to `dest`. Defaults to 4.

        Raises:
            GRPCError: If an invalid machine part ID is passed.

        Returns:
            viam.app.app_client.RobotPart: The machine part.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getrobotpart>`_.
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
        filter: str | None = None,
        dest: str | None = None,
        log_levels: list[str] = [],
        num_log_entries: int = 100,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> list[LogEntry]:
        """Get the logs associated with a robot part.

        ::

            part_logs = await cloud.get_robot_part_logs(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22",
                num_log_entries=20
            )

        Args:
            robot_part_id (str): ID of the machine part to get logs from.
            filter (str | None): Only include logs with messages that contain the string `filter`. Defaults to empty string "" (that is,
                no filter).
            dest (str | None): Optional filepath to write the log entries to.
            log_levels (list[str]): List of log levels for which entries should be returned. Defaults to empty list, which returns all logs.
            num_log_entries (int): Number of log entries to return. Passing 0 returns all logs. Defaults to 100. All logs or the first
                `num_log_entries` logs will be returned, whichever comes first.
            start (datetime | None): Optional start time for log retrieval. Only logs created after this time will be returned.
            end (datetime | None): Optional end time for log retrieval. Only logs created before this time will be returned.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        Returns:
            list[viam.app.app_client.LogEntry]: The list of log entries.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getrobotpartlogs>`_.
        """
        if num_log_entries < 0:
            raise ValueError("'num_log_entries must be at least 0.")
        logs_left = num_log_entries
        page_token = ""
        logs = []

        while True:
            new_logs, next_page_token = await self._get_robot_part_logs(
                robot_part_id=robot_part_id,
                filter=filter if filter else "",
                page_token=page_token,
                log_levels=log_levels,
                start=start,
                end=end,
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
        self,
        robot_part_id: str,
        filter: str,
        page_token: str,
        log_levels: list[str],
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> tuple[list[LogEntry], str]:
        request = GetRobotPartLogsRequest(
            id=robot_part_id,
            filter=filter,
            page_token=page_token,
            levels=log_levels,
            start=datetime_to_timestamp(start),
            end=datetime_to_timestamp(end),
        )
        response: GetRobotPartLogsResponse = await self._app_client.GetRobotPartLogs(request, metadata=self._metadata)
        return [LogEntry.from_proto(log) for log in response.logs], response.next_page_token

    async def tail_robot_part_logs(
        self, robot_part_id: str, errors_only: bool = True, filter: str | None = None
    ) -> _LogsStream[list[LogEntry]]:
        """Get an asynchronous iterator that receives live machine part logs.

        ::

            logs_stream = await cloud.tail_robot_part_logs(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22"
            )

        Args:
            robot_part_id (str): ID of the machine part to retrieve logs from.
            errors_only (bool): Boolean specifying whether or not to only include error logs. Defaults to True.
            filter (str | None): Only include logs with messages that contain the string `filter`. Defaults to empty string "" (that is,
                no filter).

        Returns:
            _LogsStream[list[LogEntry]]: The asynchronous iterator receiving live machine part logs.
        """

        async def read() -> AsyncIterator[list[LogEntry]]:
            async with self._app_client.TailRobotPartLogs.open(metadata=self._metadata) as stream:
                await stream.send_message(
                    TailRobotPartLogsRequest(id=robot_part_id, errors_only=errors_only, filter=filter if filter else "")
                )

                while True:
                    response: TailRobotPartLogsResponse | None = await stream.recv_message()
                    if response is None or len(response.logs) == 0:
                        break
                    logs = [LogEntry.from_proto(log) for log in response.logs]
                    yield logs

        return _LogsStreamWithIterator(read())

    async def get_robot_part_history(self, robot_part_id: str) -> list[RobotPartHistoryEntry]:
        """Get a list containing the history of a machine part.

        ::

            part_history = await cloud.get_robot_part_history(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22"
            )

        Args:
            robot_part_id (str): ID of the machine part to retrieve history from.

        Raises:
            GRPCError: If an invalid machine part ID is provided.

        Returns:
            list[viam.app.app_client.RobotPartHistoryEntry]: The list of the machine part's history.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getrobotapikeys>`_.
        """
        request = GetRobotPartHistoryRequest(id=robot_part_id)
        response: GetRobotPartHistoryResponse = await self._app_client.GetRobotPartHistory(request, metadata=self._metadata)
        return [RobotPartHistoryEntry.from_proto(part_history) for part_history in response.history]

    async def update_robot_part(
        self,
        robot_part_id: str,
        name: str,
        robot_config: Mapping[str, ValueTypes] | None = None,
        last_known_update: datetime | None = None,
        robot_config_json: str | None = None,
    ) -> RobotPart:
        """Change the name and assign an optional new configuration to a machine part.

        ::

            my_machine_part = await cloud.update_robot_part(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22"
            )

        Args:
            robot_part_id (str): ID of the robot part to update.
            name (str): New name to be updated on the robot part.
            robot_config (Mapping[str, ValueTypes]): Optional new config represented as a dictionary to be updated on the machine part. The machine
                part's config will remain as is (no change) if one isn't passed.
            last_known_update (datetime): Optional time of the last known update to this part's config. If provided, this will result in a
                GRPCError if the upstream config has changed since this time, indicating that the local config is out of date. Omitting this
                parameter will result in an overwrite of the upstream config.
            robot_config_json (str): Optional raw JSON string of the robot config, preserving user-defined key order.
                When set, this takes precedence over robot_config for storage purposes.
        Raises:
            GRPCError: If either an invalid machine part ID, name, or config is passed, or if the upstream config has changed since
                last_known_update.
        Returns:
            viam.app.app_client.RobotPart: The newly updated robot part.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#updaterobotpart>`_.
        """
        request = UpdateRobotPartRequest(
            id=robot_part_id,
            name=name,
            robot_config=dict_to_struct(robot_config) if robot_config else None,
            last_known_update=datetime_to_timestamp(last_known_update),
            robot_config_json=robot_config_json if robot_config_json else None,
        )
        response: UpdateRobotPartResponse = await self._app_client.UpdateRobotPart(request, metadata=self._metadata)
        return RobotPart.from_proto(robot_part=response.part)

    async def new_robot_part(self, robot_id: str, part_name: str) -> str:
        """Create a new machine part.

        ::

            new_part_id = await cloud.new_robot_part(
                robot_id="1a123456-x1yz-0ab0-a12xyzabc", part_name="myNewSubPart"
            )

        Args:
            robot_id (str): ID of the machine to create a new part for.
            part_name (str): Name of the new part.

        Raises:
            GRPCError: If either an invalid machine ID or name is passed.

        Returns:
            str: The new machine part's ID.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#newrobotpart>`_.
        """
        request = NewRobotPartRequest(robot_id=robot_id, part_name=part_name)
        response: NewRobotPartResponse = await self._app_client.NewRobotPart(request, metadata=self._metadata)
        return response.part_id

    async def delete_robot_part(self, robot_part_id: str) -> None:
        """Delete the specified machine part.

        ::

            await cloud.delete_robot_part(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22"
            )

        Args:
            robot_part_id (str): ID of the machine part to delete. Must be specified.

        Raises:
            GRPCError: If an invalid machine part ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deleterobotpart>`_.
        """
        request = DeleteRobotPartRequest(part_id=robot_part_id)
        await self._app_client.DeleteRobotPart(request, metadata=self._metadata)

    async def get_robot_api_keys(self, robot_id: str) -> list[APIKeyWithAuthorizations]:
        """Gets the API Keys for the machine.

        ::

            api_keys = await cloud.get_robot_api_keys(robot_id="robot-id")

        Args:
            robot_id (str): The ID of the machine.

        Returns:
            list[APIKeyWithAuthorizations]: The list of API keys.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getrobotapikeys>`_.
        """
        request = GetRobotAPIKeysRequest(robot_id=robot_id)
        response: GetRobotAPIKeysResponse = await self._app_client.GetRobotAPIKeys(request, metadata=self._metadata)
        return list(response.api_keys)

    async def mark_part_as_main(self, robot_part_id: str) -> None:
        """Mark a machine part as the main part of a machine.

        ::

            await cloud.mark_part_as_main(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the machine part to mark as main.

        Raises:
            GRPCError: If an invalid machine part ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#markpartasmain>`_.
        """
        request = MarkPartAsMainRequest(part_id=robot_part_id)
        await self._app_client.MarkPartAsMain(request, metadata=self._metadata)

    async def mark_part_for_restart(self, robot_part_id: str) -> None:
        """Mark the specified machine part for restart.

        ::

            await cloud.mark_part_for_restart(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the machine part to mark for restart.

        Raises:
            GRPCError: If an invalid machine part ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#markpartforrestart>`_.
        """
        request = MarkPartForRestartRequest(part_id=robot_part_id)
        await self._app_client.MarkPartForRestart(request, metadata=self._metadata)

    async def create_robot_part_secret(self, robot_part_id: str) -> RobotPart:
        """Create a machine part secret.

        ::

            part_with_new_secret = await cloud.create_robot_part_secret(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22")

        Args:
            robot_part_id (str): ID of the machine part to create a secret for.

        Raises:
            GRPCError: If an invalid machine part ID is passed.

        Returns:
            viam.app.app_client.RobotPart: The machine part the new secret was generated for.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createrobotpartsecret>`_.
        """
        request = CreateRobotPartSecretRequest(part_id=robot_part_id)
        response: CreateRobotPartSecretResponse = await self._app_client.CreateRobotPartSecret(request, metadata=self._metadata)
        return RobotPart.from_proto(response.part)

    async def delete_robot_part_secret(self, robot_part_id: str, secret_id: str) -> None:
        """Delete a machine part secret.

        ::

            await cloud.delete_robot_part_secret(
                robot_part_id="abc12345-1a23-1234-ab12-a22a22a2aa22",
                secret_id="123xyz12-abcd-4321-12ab-12xy1xyz12xy")

        Args:
            robot_part_id (str): ID of the machine part to delete the secret from.
            secret_id (str): ID of the secret to delete.

        Raises:
            GRPCError: If an invalid machine part ID or secret ID is passed.

        For more information, see `Fleet Management API <hhttps://docs.viam.com/dev/reference/apis/fleet/#deleterobotpartsecret>`_.
        """
        request = DeleteRobotPartSecretRequest(part_id=robot_part_id, secret_id=secret_id)
        await self._app_client.DeleteRobotPartSecret(request, metadata=self._metadata)

    async def list_robots(self, location_id: str | None = None) -> list[Robot]:
        """Get a list of all machines under the specified location.

        ::

            list_of_machines = await cloud.list_robots(location_id="123ab12345")

        Args:
            location_id (str | None): ID of the location to retrieve the machines from. Defaults to the location ID provided at
                `AppClient` instantiation.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            list[viam.proto.app.Robot]: The list of robots.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listrobots>`_.
        """
        request = ListRobotsRequest(location_id=location_id if location_id else "")
        response: ListRobotsResponse = await self._app_client.ListRobots(request, metadata=self._metadata)
        return list(response.robots)

    async def new_robot(self, name: str, location_id: str | None = None) -> str:
        """Create a new machine.

        ::

            new_machine_id = await cloud.new_robot(name="beepboop", location_id="my-location-id")

        Args:
            name (str): Name of the new machine.
            location_id (str | None): ID of the location under which to create the machine. Defaults to the current authorized location.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            str: The new robot's ID.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#newrobot>`_.
        """
        request = NewRobotRequest(location=location_id if location_id else "", name=name)
        response: NewRobotResponse = await self._app_client.NewRobot(request, metadata=self._metadata)
        return response.id

    async def update_robot(self, robot_id: str, name: str, location_id: str | None = None) -> Robot:
        """Change the name of an existing machine.

        ::

            updated_robot = await cloud.update_robot(
                robot_id="1a123456-x1yz-0ab0-a12xyzabc",
                name="Orange-Robot",
                location_id="23ab12345"
            )

        Args:
            robot_id (str): ID of the machine to update.
            name (str): New name to be updated on the machine.
            location_id (str | None): ID of the location under which the machine exists. Defaults to the location ID provided at
                `AppClient` instantiation

        Raises:
            GRPCError: If either an invalid machine ID, name, or location ID is passed or a location ID isn't passed and there was no
                location ID provided at `AppClient` instantiation.

        Returns:
            viam.proto.app.Robot: The newly updated machine.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#updaterobot>`_.
        """
        request = UpdateRobotRequest(id=robot_id, name=name, location=location_id if location_id else "")
        response: UpdateRobotResponse = await self._app_client.UpdateRobot(request, metadata=self._metadata)
        return response.robot

    async def delete_robot(self, robot_id: str) -> None:
        """Delete the specified machine.

        ::

            await cloud.delete_robot(robot_id="1a123456-x1yz-0ab0-a12xyzabc")

        Args:
            robot_id (str): ID of the machine to delete.

        Raises:
            GRPCError: If an invalid machine ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deleterobot>`_.
        """
        request = DeleteRobotRequest(id=robot_id)
        await self._app_client.DeleteRobot(request, metadata=self._metadata)

    async def list_fragments(
        self, org_id: str, show_public: bool = True, visibilities: list[Fragment.Visibility] | None = None
    ) -> list[Fragment]:
        """Get a list of fragments under the currently authed-to organization.

        ::

            fragments_list = await cloud.list_fragments(org_id="org-id", visibilities=[])

        Args:
            org_id (str): The ID of the organization to list fragments for.
                You can obtain your organization ID from the organization settings page.
            show_public (bool): Optional boolean specifying whether or not to only show public fragments. If True, only public fragments
                will return. If False, only private fragments will return. Defaults to True.

                .. deprecated:: 0.25.0
                    Use ``visibilities`` instead.
            visibilities (list[Fragment.Visibility] | None): List of FragmentVisibilities specifying which types of fragments to include
                in the results. If empty, by default only public fragments will be returned.

        Returns:
            list[viam.app.app_client.Fragment]: The list of fragments.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listfragments>`_.
        """
        request = ListFragmentsRequest(
            organization_id=org_id,
            fragment_visibility=map(Fragment.Visibility.to_proto, visibilities if visibilities else []),
            show_public=show_public,
        )
        response: ListFragmentsResponse = await self._app_client.ListFragments(request, metadata=self._metadata)
        return [Fragment.from_proto(fragment=fragment) for fragment in response.fragments]

    async def get_fragment(self, fragment_id: str, version: str | None = None) -> Fragment:
        """Get a fragment.

        ::

            # Get a fragment and print its name and when it was created.
            the_fragment = await cloud.get_fragment(
                fragment_id="12a12ab1-1234-5678-abcd-abcd01234567")
            print("Name: ", the_fragment.name, "\\nCreated on: ", the_fragment.created_on)

        Args:
            fragment_id (str): ID of the fragment to get.
            version (str): Optional specification of the fragment version to get (revision or tag).

        Raises:
            GRPCError: If an invalid fragment ID is passed.

        Returns:
            viam.app.app_client.Fragment: The fragment.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getfragment>`_.
        """
        request = GetFragmentRequest(id=fragment_id, version=version)
        response: GetFragmentResponse = await self._app_client.GetFragment(request, metadata=self._metadata)
        return Fragment.from_proto(fragment=response.fragment)

    async def create_fragment(self, org_id: str, name: str, config: Mapping[str, ValueTypes] | None = None) -> Fragment:
        """Create a new private fragment.

        ::

            new_fragment = await cloud.create_fragment(org_id="org-id", name="cool_smart_machine_to_configure_several_of")

        Args:
            org_id (str): The ID of the organization to create the fragment within.
                You can obtain your organization ID from the organization settings page.
            name (str): Name of the fragment.
            config (Mapping[str, ValueTypes] | None): Optional Dictionary representation of new config to assign to specified fragment. Can be
                assigned by updating the fragment.

        Raises:
            GRPCError: If an invalid name is passed.

        Returns:
            viam.app.app_client.Fragment: The newly created fragment.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createfragment>`_.
        """
        request = CreateFragmentRequest(name=name, config=dict_to_struct(config) if config else None, organization_id=org_id)
        response: CreateFragmentResponse = await self._app_client.CreateFragment(request, metadata=self._metadata)
        return Fragment.from_proto(response.fragment)

    async def update_fragment(
        self,
        fragment_id: str,
        name: str,
        config: Mapping[str, ValueTypes] | None = None,
        public: bool | None = None,
        visibility: Fragment.Visibility | None = None,
        last_known_update: datetime | None = None,
    ) -> Fragment:
        """Update a fragment name AND its config and/or visibility.

        ::

            updated_fragment = await cloud.update_fragment(
                fragment_id="12a12ab1-1234-5678-abcd-abcd01234567",
                name="better_name")

        Args:
            fragment_id (str): ID of the fragment to update.
            name (str): New name to associate with the fragment.
            config (Mapping[str, ValueTypes] | None): Optional Dictionary representation of new config to assign to specified fragment. Not
                passing this parameter will leave the fragment's config unchanged.
            public (bool): Boolean specifying whether the fragment is public. Not passing this parameter will leave the fragment's
                visibility unchanged. A fragment is private by default when created.

                .. deprecated:: 0.25.0
                    Use ``visibility`` instead.
            visibility (Fragment.Visibility | None): Optional FragmentVisibility list specifying who should be allowed
                to view the fragment. Not passing this parameter will leave the fragment's visibility unchanged.
                A fragment is private by default when created.
            last_known_update (datetime): Optional time of the last known update to this fragment's config. If provided, this will result in
                a GRPCError if the upstream config has changed since this time, indicating that the local config is out of date. Omitting
                this parameter will result in an overwrite of the upstream config.
        Raises:
            GRPCError: if an invalid ID, name, or config is passed, or if the upstream fragment config has changed since last_known_update.

        Returns:
            viam.app.app_client.Fragment: The newly updated fragment.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#updatefragment>`_.
        """
        request = UpdateFragmentRequest(
            id=fragment_id,
            name=name,
            config=dict_to_struct(config) if config else None,
            public=public,
            visibility=visibility.to_proto() if visibility else None,
            last_known_update=datetime_to_timestamp(last_known_update),
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

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deletefragment>`_.
        """
        request = DeleteFragmentRequest(id=fragment_id)
        await self._app_client.DeleteFragment(request, metadata=self._metadata)

    async def get_fragment_history(self, id: str, page_token: str | None = "", page_limit: int | None = 10) -> list[FragmentHistoryEntry]:
        """Get fragment history.

        ::

            fragment_history = await cloud.get_fragment_history(
                id = "12a12ab1-1234-5678-abcd-abcd01234567",
                page_token = "pg-token",
                page_limit = 10
            )

        Args:
            id (str): ID of the fragment to fetch history for.
            page_token (str | None): the page token for the fragment history collection
            page_limit (int | None): the number of fragment history documents to return in the result.
                The default page limit is 10.

        Raises:
            GRPCError: if an invalid fragment id, page token or page limit is passed.

        Returns:
            viam.app.app_client.FragmentHistoryResponse: A list of documents with the fragment history.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getfragmenthistory>`_.
        """

        request = GetFragmentHistoryRequest(id=id, page_token=page_token, page_limit=page_limit)
        response: GetFragmentHistoryResponse = await self._app_client.GetFragmentHistory(request, metadata=self._metadata)
        return [FragmentHistoryEntry.from_proto(fragment_history) for fragment_history in response.history]

    async def add_role(
        self,
        org_id: str,
        identity_id: str,
        role: _ROLE_TYPE,
        resource_type: _RESOURCE_TYPE_TYPE,
        resource_id: str,
    ) -> None:
        """Add a role under the currently authed-to organization.

        ::

            await cloud.add_role(
                org_id="<YOUR-ORG-ID>",
                identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                role="owner",
                resource_type="location",
                resource_id="111ab12345"
            )

        Args:
            org_id (str): The ID of the organization to create the role in.
                You can obtain your organization ID from the organization settings page.
            identity_id (str): ID of the entity the role belongs to (for example, a user ID).
            role (_ROLE_TYPE): The role to add.
            resource_type (_RESOURCE_TYPE_TYPE): Type of the resource to add role to.
                Must match `resource_id`.
            resource_id (str): ID of the resource the role applies to (that is, either an organization, location, or robot ID).

        Raises:
            GRPCError: If either an invalid identity ID, role ID, resource type, or resource ID is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#addrole>`_.
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
        role: _ROLE_TYPE,
        resource_type: _RESOURCE_TYPE_TYPE,
        resource_id: str,
    ) -> None:
        """Remove a role under the currently authed-to organization.

        ::

            await cloud.remove_role(
                org_id="<YOUR-ORG-ID>",
                identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                role="owner",
                resource_type="location",
                resource_id="111ab12345"
            )

        Args:
            org_id (str): The ID of the organization the role exists in.
                You can obtain your organization ID from the organization settings page.
            identity_id (str): ID of the entity the role belongs to (for example, a user ID).
            role (_ROLE_TYPE): The role to remove.
            resource_type (_RESOURCE_TYPE_TYPE): Type of the resource the role is being
                removed from. Must match `resource_id`.
            resource_id (str): ID of the resource the role applies to (that is, either an organization, location, or robot ID).

        Raises:
            GRPCError: If either an invalid identity ID, role ID, resource type, or resource ID or is passed.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#removerole>`_.
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
        old_role: _ROLE_TYPE,
        old_resource_type: _RESOURCE_TYPE_TYPE,
        old_resource_id: str,
        new_identity_id: str,
        new_role: _ROLE_TYPE,
        new_resource_type: _RESOURCE_TYPE_TYPE,
        new_resource_id: str,
    ) -> None:
        """Changes a role to a new role.

        ::

            await cloud.change_role(
                organization_id="<YOUR-ORG-ID>",
                old_identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                old_role="operator",
                old_resource_type="location",
                old_resource_id="111ab12345",
                new_identity_id="abc01234-0123-4567-ab12-a11a00a2aa22",
                new_role="owner",
                new_resource_type="organization",
                new_resource_id="abc12345"
            )

        Args:
            organization_id (str): ID of the organization
            old_identity_id (str): ID of the entity the role belongs to (for example, a user ID).
            old_role (_ROLE_TYPE): The role to be changed.
            old_resource_type (_RESOURCE_TYPE_TYPE): Type of the resource the role is
                added to. Must match `old_resource_id`.
            old_resource_id (str): ID of the resource the role applies to (that is, either an organization, location, or robot ID).

            new_identity_id (str): New ID of the entity the role belongs to (for example, a user ID).
            new_role (_ROLE_TYPE): The new role.
            new_resource_type (_RESOURCE_TYPE_TYPE): Type of the resource to add role to.
                Must match `new_resource_id`.
            new_resource_id (str): New ID of the resource the role applies to (that is, either an organization, location, or robot ID).

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#changerole>`_.
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

    async def list_authorizations(self, org_id: str, resource_ids: list[str] | None = None) -> list[Authorization]:
        """List all authorizations under a specific resource (or resources) within the currently authed-to organization. If no resource IDs
        are provided, all resource authorizations within the organizations are returned.

        ::

            list_of_auths = await cloud.list_authorizations(
                org_id="<YOUR-ORG-ID>",
                resource_ids=["1a123456-x1yz-0ab0-a12xyzabc"])

        Args:
            org_id: The ID of the organization to list authorizations for.
            resource_ids (list[str] | None): IDs of the resources to retrieve authorizations from.
                If None, defaults to all resources.

        Raises:
            GRPCError: If an invalid resource ID is passed.

        Returns:
            list[viam.proto.app.Authorization]: The list of authorizations.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listauthorizations>`_.
        """
        request = ListAuthorizationsRequest(organization_id=org_id, resource_ids=resource_ids)
        response: ListAuthorizationsResponse = await self._app_client.ListAuthorizations(request, metadata=self._metadata)
        return list(response.authorizations)

    async def check_permissions(self, permissions: list[AuthorizedPermissions]) -> list[AuthorizedPermissions]:
        """Checks validity of a list of permissions.

        ::

            from viam.proto.app import AuthorizedPermissions

            # Check whether the entity you're currently authenticated to has permission to control and/or
            # read logs from robots in the "organization-identifier123" org
            permissions = [AuthorizedPermissions(resource_type="organization",
                                                 resource_id="<YOUR-ORG-ID>",
                                                 permissions=["control_robot",
                                                              "read_robot_logs"])]

            filtered_permissions = await cloud.check_permissions(permissions)

        Args:
            permissions (list[viam.proto.app.AuthorizedPermissions]): the permissions to validate
                (for example, "read_organization", "control_robot")

        Raises:
            GRPCError: If the list of permissions to validate is empty.

        Returns:
            list[viam.proto.app.AuthorizedPermissions]: The permissions argument, with invalid permissions filtered out.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#checkpermissions>`_.
        """
        request = CheckPermissionsRequest(permissions=permissions)
        response: CheckPermissionsResponse = await self._app_client.CheckPermissions(request, metadata=self._metadata)
        return list(response.authorized_permissions)

    async def get_registry_item(self, item_id: str, include_markdown_documentation: bool = False) -> RegistryItem:
        """Get registry item by ID.

        ::

            item = await cloud.get_registry_item("item-id")

        Args:
            item_id (str): The ID of the registry item. This is the namespace and name of the item in the
                form `namespace:name`. For example, `Viam's csi-cam-pi module's <https://app.viam.com/module/viam/csi-cam-pi>`_ item ID
                would be `viam:csi-cam-pi`. You can also use `org-id:name`. For example,
                `abc01234-0123-4567-ab12-a11a00a2aa22:training-script`.

        Returns:
            RegistryItem: The registry item.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getregistryitem>`_.
        """
        request = GetRegistryItemRequest(item_id=item_id, include_markdown_documentation=include_markdown_documentation)
        response: GetRegistryItemResponse = await self._app_client.GetRegistryItem(request, metadata=self._metadata)
        return response.item

    async def create_registry_item(self, organization_id: str, name: str, type: PackageType.ValueType) -> None:
        """Create a registry item

        ::

            from viam.proto.app.packages import PackageType

            await cloud.create_registry_item("<YOUR-ORG-ID>", "name", PackageType.PACKAGE_TYPE_ML_MODEL)

        Args:
            organization_id (str): The organization to create the registry item under.
            name (str): The name of the registry item, which must be unique within your org.
            type (PackageType.ValueType): The type of the item in the registry.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createregistryitem>`_.
        """
        request = CreateRegistryItemRequest(organization_id=organization_id, name=name, type=type)
        await self._app_client.CreateRegistryItem(request, metadata=self._metadata)

    async def update_registry_item(
        self, item_id: str, type: PackageType.ValueType, description: str, visibility: Visibility.ValueType
    ) -> None:
        """Update a registry item.

        ::

            from viam.proto.app.packages import PackageType
            from viam.proto.app import Visibility

            await cloud.update_registry_item(
                "your-namespace:your-name",
                PackageType.PACKAGE_TYPE_ML_TRAINING,
                "description",
                Visibility.VISIBILITY_PUBLIC
            )

        Args:
            item_id (str): The ID of the registry item, containing either the namespace and module name
                (for example, `my-org:my-module`) or organization ID and module name (`org-id:my-module`).
            type (PackageType.ValueType): The type of the item in the registry.
            description (str): The description of the registry item.
            visibility (Visibility.ValueType): The visibility of the registry item.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#updateregistryitem>`_.
        """

        request = UpdateRegistryItemRequest(item_id=item_id, type=type, description=description, visibility=visibility)
        await self._app_client.UpdateRegistryItem(request, metadata=self._metadata)

    async def list_registry_items(
        self,
        organization_id: str,
        types: list[PackageType.ValueType],
        visibilities: list[Visibility.ValueType],
        platforms: list[str],
        statuses: list[RegistryItemStatus.ValueType],
        search_term: str | None = None,
        page_token: str | None = None,
    ) -> list[RegistryItem]:
        """List the registry items in an organization.

        ::

            from viam.proto.app.packages import PackageType
            from viam.proto.app import Visibility, RegistryItemStatus

            # List private, published ml training scripts in your organization
            registry_items = await cloud.list_registry_items(
                organization_id="<YOUR-ORG-ID>",
                types=[PackageType.PACKAGE_TYPE_ML_TRAINING],
                visibilities=[Visibility.VISIBILITY_PRIVATE],
                platforms=[""],
                statuses=[RegistryItemStatus.REGISTRY_ITEM_STATUS_PUBLISHED]
            )

            # List public, published linux modules in all organizations
            registry_items = await cloud.list_registry_items(
                organization_id="",
                types=[PackageType.PACKAGE_TYPE_MODULE],
                visibilities=[Visibility.VISIBILITY_PUBLIC],
                platforms=["linux/any"],
                statuses=[RegistryItemStatus.REGISTRY_ITEM_STATUS_PUBLISHED]
            )

        Args:
            organization_id (str): The ID of the organization to return registry items for.
            types (list[PackageType.ValueType]): The types of registry items.
            visibilities (list[Visibility.ValueType]): The visibilities of registry items.
            platforms (list[str]): The platforms of registry items.
            statuses (list[RegistryItemStatus.ValueType]): The types of the items in the registry.
            search_term (str | None): The search term of the registry items.
            page_token (str | None): The page token of the registry items.

        Returns:
            list[RegistryItem]: The list of registry items.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listregistryitems>`_.
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

            await cloud.delete_registry_item("your-namespace:your-name")

        Args:
            item_id (str): The ID of the deleted registry item, containing either the namespace and module name
                (for example, `my-org:my-module`) or organization ID and module name (`org-id:my-module`).

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deleteregistryitem>`_.
        """
        request = DeleteRegistryItemRequest(item_id=item_id)
        await self._app_client.DeleteRegistryItem(request, metadata=self._metadata)

    async def create_module(self, org_id: str, name: str) -> tuple[str, str]:
        """Create a module under the currently authed-to organization.

        ::

            new_module = await cloud.create_module(org_id="org-id", name="cool_new_hoverboard_module")
            print("Module ID:", new_module[0])

        Args:
            org_id (str): The ID of the organization to create the module under.
                You can obtain your organization ID from the organization settings page.
            name (str): The name of the module. Must be unique within your organization.

        Raises:
            GRPCError: If an invalid name (for example, "") is passed.

        Returns:
            tuple[str, str]: A tuple containing the ID [0] of the new module and its URL [1].

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createmodule>`_.
        """
        request = CreateModuleRequest(organization_id=org_id, name=name)
        response: CreateModuleResponse = await self._app_client.CreateModule(request, metadata=self._metadata)
        return response.module_id, response.url

    async def update_module(
        self,
        module_id: str,
        url: str,
        description: str,
        models: list[Model] | None,
        entrypoint: str,
        public: bool = False,
    ) -> str:
        """Update the documentation URL, description, models, entrypoint, and/or the visibility of a module.

        ::

            from viam.proto.app import Model

            model = Model(
                api="rdk:component:base",
                model="my-group:cool_new_hoverboard_module:wheeled"
            )

            url_of_my_module = await cloud.update_module(
                module_id="my-group:cool_new_hoverboard_module",
                url="https://docsformymodule.viam.com",
                models=[model],
                description="A base to support hoverboards.",
                entrypoint="exec"
            )

        Args:
            module_id (str): ID of the module being updated, containing either the namespace and module name
                (for example, `my-org:my-module`) or organization ID and module name (`org-id:my-module`).
            url (str): The url to reference for documentation and code (NOT the url of the module itself).
            description (str): A short description of the module that explains its purpose.
            models (list[viam.proto.app.Model]): list of models that are available in the module.
            entrypoint (str): The executable to run to start the module program.
            public (bool): The visibility that should be set for the module. Defaults to False (private).

        Raises:
            GRPCError: If either an invalid module ID, URL, list of models, or organization ID is passed.

        Returns:
            str: The URL of the newly updated module.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#updatemodule>`_.
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

    async def upload_module_file(self, module_file_info: ModuleFileInfo, file: bytes) -> str:
        """Upload a module file

        ::

            from viam.proto.app import ModuleFileInfo

            module_file_info = ModuleFileInfo(
                module_id = "sierra:cool_new_hoverboard_module",
                version = "1.0.0",
                platform = "darwin/arm64"
            )

            file_id = await cloud.upload_module_file(
                module_file_info=module_file_info,
                file=b"<file>"
            )

        Args:
            module_file_info (viam.proto.app.ModuleFileInfo): Relevant metadata.
            file (bytes): Bytes of file to upload.

        Returns:
            str: URL of uploaded file.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#uploadmodulefile>`_.
        """
        request_module_file_info = UploadModuleFileRequest(module_file_info=module_file_info)
        request_file = UploadModuleFileRequest(file=file)
        async with self._app_client.UploadModuleFile.open(metadata=self._metadata) as stream:
            await stream.send_message(request_module_file_info)
            await stream.send_message(request_file, end=True)
            response: UploadModuleFileRequest | None = await stream.recv_message()
            if not response:
                await stream.recv_trailing_metadata()  # causes us to throw appropriate gRPC error.
                raise TypeError("Response cannot be empty")  # we should never get here, but for typechecking
            return response.url

    async def get_module(self, module_id: str) -> Module:
        """Get a module.

        ::

            the_module = await cloud.get_module(module_id="my-group:my-cool-modular-base")

        Args:
            module_id (str): ID of the module being retrieved, containing either the namespace and module name
                (for example, `my-org:my-module`) or organization ID and module name (`org-id:my-module`).

        Raises:
            GRPCError: If an invalid module ID is passed.

        Returns:
            viam.proto.app.Module: The module.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#getmodule>`_.
        """
        request = GetModuleRequest(module_id=module_id)
        response: GetModuleResponse = await self._app_client.GetModule(request, metadata=self._metadata)
        return response.module

    async def list_modules(self, org_id: str) -> list[Module]:
        """List the modules under the currently authed-to organization.

        ::

            modules_list = await cloud.list_modules("<YOUR-ORG-ID>")

        Args:
            org_id (str): The ID of the organization to list modules for.
                You can obtain your organization ID from the organization settings page.

        Returns:
            list[viam.proto.app.Module]: The list of modules.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listmodules>`_.
        """
        request = ListModulesRequest(organization_id=org_id)
        response: ListModulesResponse = await self._app_client.ListModules(request, metadata=self._metadata)
        return list(response.modules)

    # TODO(RSDK-5569): when user-based auth exists, make `name` default to `None` and let
    # app deal with setting a default.
    async def create_key(self, org_id: str, authorizations: list[APIKeyAuthorization], name: str | None = None) -> tuple[str, str]:
        """Creates a new API key.

        ::

            from viam.app.app_client import APIKeyAuthorization

            auth = APIKeyAuthorization(
                role="owner",
                resource_type="robot",
                resource_id="your-machine-id123"
            )

            api_key, api_key_id = cloud.create_key(
                org_id="<YOUR-ORG-ID>",
                authorizations=[auth],
                name="my_key"
            )

        Args:
            org_id (str): The ID of the organization to create the key for.
                You can obtain your organization ID from the organization settings page.
            authorizations (list[viam.proto.app.Authorization]): A list of authorizations to associate
                with the key.
            name (str | None): A name for the key. If None, defaults to the current timestamp.

        Raises:
            GRPCError: If the authorizations list is empty.

        Returns:
            tuple[str, str]: The api key and api key ID.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createkey>`_.
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

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#deletekey>`_.
        """
        request = DeleteKeyRequest(id=id)
        await self._app_client.DeleteKey(request, metadata=self._metadata)

    async def create_key_from_existing_key_authorizations(self, id: str) -> tuple[str, str]:
        """Creates a new API key with an existing key's authorizations

        ::

            api_key, api_key_id = await cloud.create_key_from_existing_key_authorizations(
                id="INSERT YOUR API KEY ID")

        Args:
            id (str): the ID of the API key to duplication authorizations from

        Returns:
            tuple[str, str]: The API key and API key id

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#createkeyfromexistingkeyauthorizations>`_.
        """
        request = CreateKeyFromExistingKeyAuthorizationsRequest(id=id)
        response: CreateKeyFromExistingKeyAuthorizationsResponse = await self._app_client.CreateKeyFromExistingKeyAuthorizations(
            request,
            metadata=self._metadata,
        )
        return (response.key, response.id)

    async def list_keys(self, org_id: str) -> list[APIKeyWithAuthorizations]:
        """Lists all keys for the currently-authed-to org.

        ::

            keys = await cloud.list_keys(org_id="<YOUR-ORG-ID>")

        Args:
            org_id (str): The ID of the organization to list API keys for.
                You can obtain your organization ID from the organization settings page.

        Returns:
            list[viam.proto.app.APIKeyWithAuthorizations]: The existing API keys and authorizations.

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#listkeys>`_.
        """
        request = ListKeysRequest(org_id=org_id)
        response: ListKeysResponse = await self._app_client.ListKeys(request, metadata=self._metadata)
        return list(response.api_keys)

    async def rotate_key(self, id: str) -> tuple[str, str]:
        """Rotate an API key.

        ::

            key, id = await cloud.rotate_key("key-id")

        Args:
            id (str): The ID of the key to be rotated.

        Returns:
            tuple[str, str]: The API key and API key id

        For more information, see `Fleet Management API <https://docs.viam.com/dev/reference/apis/fleet/#rotatekey>`_.
        """
        request = RotateKeyRequest(id=id)
        response: RotateKeyResponse = await self._app_client.RotateKey(request, metadata=self._metadata)
        return response.key, response.id

    async def get_organization_metadata(self, org_id: str) -> Mapping[str, Any]:
        """Get an organization's user-defined metadata.

        ::

            metadata = await cloud.get_organization_metadata(org_id="<YOUR-ORG-ID>")

        Args:
            org_id (str): The ID of the organization with which the user-defined metadata is associated.
                You can obtain your organization ID from the organization settings page.

        Returns:
            Mapping[str, Any]: The user-defined metadata converted from JSON to a Python dictionary
        """
        request = GetOrganizationMetadataRequest(organization_id=org_id)
        response: GetOrganizationMetadataResponse = await self._app_client.GetOrganizationMetadata(request, metadata=self._metadata)
        return struct_to_dict(response.data)

    async def update_organization_metadata(self, org_id: str, metadata: Mapping[str, Any]) -> None:
        """Update an organization's user-defined metadata.

        ::

             await cloud.update_organization_metadata(org_id="<YOUR-ORG-ID>", metadata={
                 "TEST_API_KEY": "ABC123",
             })

        Args:
            organization_id (str): The ID of the organization with which to associate the user-defined metadata.
                You can obtain your organization ID from the organization settings page.
            metadata (Mapping[str, Any]): The user-defined metadata to upload as a Python dictionary.
        """
        request = UpdateOrganizationMetadataRequest(organization_id=org_id, data=dict_to_struct(metadata))
        _: UpdateOrganizationMetadataResponse = await self._app_client.UpdateOrganizationMetadata(request, metadata=self._metadata)

    async def get_location_metadata(self, location_id: str) -> Mapping[str, Any]:
        """Get a location's user-defined metadata.

        ::

            metadata = await cloud.get_location_metadata(location_id="<YOUR-LOCATION-ID>")

        Args:
            location_id (str): The ID of the location with which the user-defined metadata is associated.
                You can obtain your location ID from the location's page.

        Returns:
            Mapping[str, Any]: The user-defined metadata converted from JSON to a Python dictionary.
        """
        request = GetLocationMetadataRequest(location_id=location_id)
        response: GetLocationMetadataResponse = await self._app_client.GetLocationMetadata(request, metadata=self._metadata)
        return struct_to_dict(response.data)

    async def update_location_metadata(self, location_id: str, metadata: Mapping[str, Any]) -> None:
        """Update a location's user-defined metadata.

        ::

             await cloud.update_location_metadata(location_id="<YOUR-LOCATION-ID>", metadata={
                 "TEST_API_KEY": "ABC123",
             })

        Args:
            location_id (str): The ID of the location with which to associate the user-defined metadata.
                You can obtain your location ID from the location's page.
            metadata (Mapping[str, Any]): The user-defined metadata converted from JSON to a Python dictionary.
        """
        request = UpdateLocationMetadataRequest(location_id=location_id, data=dict_to_struct(metadata))
        _: UpdateLocationMetadataResponse = await self._app_client.UpdateLocationMetadata(request, metadata=self._metadata)

    async def get_robot_metadata(self, robot_id: str) -> Mapping[str, Any]:
        """Get a robot's user-defined metadata.

        ::

            metadata = await cloud.get_robot_metadata(robot_id="<YOUR-ROBOT-ID>")

        Args:
            robot_id (str): The ID of the robot with which the user-defined metadata is associated.
                You can obtain your robot ID from the machine page.

        Returns:
            Mapping[str, Any]: The user-defined metadata converted from JSON to a Python dictionary.
        """
        request = GetRobotMetadataRequest(id=robot_id)
        response: GetRobotMetadataResponse = await self._app_client.GetRobotMetadata(request, metadata=self._metadata)
        return struct_to_dict(response.data)

    async def update_robot_metadata(self, robot_id: str, metadata: Mapping[str, Any]) -> None:
        """Update a robot's user-defined metadata.

        ::

             await cloud.update_robot_metadata(robot_id="<YOUR-ROBOT-ID>", metadata={
                 "TEST_API_KEY": "ABC123",
             })

        Args:
            robot_id (str): The ID of the robot with which to associate the user-defined metadata.
                You can obtain your robot ID from the machine page.
            metadata (Mapping[str, Any]): The user-defined metadata converted from JSON to a Python dictionary.
        """
        request = UpdateRobotMetadataRequest(id=robot_id, data=dict_to_struct(metadata))
        _: UpdateRobotMetadataResponse = await self._app_client.UpdateRobotMetadata(request, metadata=self._metadata)

    async def get_robot_part_metadata(self, robot_part_id: str) -> Mapping[str, Any]:
        """Get a robot part's user-defined metadata.

        ::

            metadata = await cloud.get_robot_part_metadata(robot_part_id="<YOUR-ROBOT-PART-ID>")

        Args:
            robot_part_id (str): The ID of the robot part with which the user-defined metadata is associated.
                You can obtain your robot part ID from the machine page.

        Returns:
            Mapping[str, Any]: The user-defined metadata converted from JSON to a Python dictionary.
        """
        request = GetRobotPartMetadataRequest(id=robot_part_id)
        response: GetRobotPartMetadataResponse = await self._app_client.GetRobotPartMetadata(request, metadata=self._metadata)
        return struct_to_dict(response.data)

    async def update_robot_part_metadata(self, robot_part_id: str, metadata: Mapping[str, Any]) -> None:
        """Update a robot part's user-defined metadata.

        ::

             await cloud.update_robot_part_metadata(robot_part_id="<YOUR-ROBOT-PART-ID>", metadata={
                 "TEST_API_KEY": "ABC123",
             })

        Args:
            robot_id (str): The ID of the robot part with which to associate the user-defined metadata.
                You can obtain your robot part ID from the machine page.
            metadata (Mapping[str, Any]): The user-defined metadata converted from JSON to a Python dictionary.
        """
        request = UpdateRobotPartMetadataRequest(id=robot_part_id, data=dict_to_struct(metadata))
        _: UpdateRobotPartMetadataResponse = await self._app_client.UpdateRobotPartMetadata(request, metadata=self._metadata)

    async def upload_device_push_token(self, app_id: str, device_token: str, device_uuid: str, timeout: float | None = None) -> None:
        """Upload a device push token for mobile notifications.

        Args:
            app_id (str): The Firebase app ID.
            device_token (str): The device push notification token.
            device_uuid (str): The unique identifier for the device.
            timeout (float | None): An option to set how long to wait (in seconds) before calling a time-out and closing the underlying RPC call.
        """
        request = UploadDevicePushTokenRequest(app_id=app_id, device_token=device_token, device_uuid=device_uuid)
        _: UploadDevicePushTokenResponse = await self._app_client.UploadDevicePushToken(request, metadata=self._metadata, timeout=timeout)

    async def delete_device_push_token(self, app_id: str, device_uuid: str, timeout: float | None = None) -> None:
        """Delete a device push token.

        Args:
            app_id (str): The Firebase app ID.
            device_uuid (str): The unique identifier for the device.
            timeout (float | None): An option to set how long to wait (in seconds) before calling a time-out and closing the underlying RPC call.
        """
        request = DeleteDevicePushTokenRequest(app_id=app_id, device_uuid=device_uuid)
        _: DeleteDevicePushTokenResponse = await self._app_client.DeleteDevicePushToken(request, metadata=self._metadata, timeout=timeout)

    async def get_device_push_tokens(self, app_id: str, timeout: float | None = None) -> list[str]:
        """Get all device push tokens for an app.

        Args:
            app_id (str): The Firebase app ID.
            timeout (float | None): An option to set how long to wait (in seconds) before calling a time-out and closing the underlying RPC call.

        Returns:
            list[str]: The list of device push tokens.
        """
        request = GetDevicePushTokensRequest(app_id=app_id)
        response: GetDevicePushTokensResponse = await self._app_client.GetDevicePushTokens(
            request, metadata=self._metadata, timeout=timeout
        )
        return list(response.device_tokens)

    async def set_firebase_config(self, org_id: str, app_id: str, config_json: str, timeout: float | None = None) -> None:
        """Set the Firebase configuration for an organization.

        Args:
            org_id (str): The organization ID.
            app_id (str): The Firebase app ID.
            config_json (str): The Firebase configuration JSON as a string.
            timeout (float | None): An option to set how long to wait (in seconds) before calling a time-out and closing the underlying RPC call.
        """
        request = SetFirebaseConfigRequest(org_id=org_id, app_id=app_id, config_json=config_json)
        _: SetFirebaseConfigResponse = await self._app_client.SetFirebaseConfig(request, metadata=self._metadata, timeout=timeout)

    async def get_firebase_config(self, org_id: str, timeout: float | None = None) -> str:
        """Get the Firebase app ID for an organization.

        Args:
            org_id (str): The organization ID.
            timeout (float | None): An option to set how long to wait (in seconds) before calling a time-out and closing the underlying RPC call.

        Returns:
            str: The Firebase app ID.
        """
        request = GetFirebaseConfigRequest(org_id=org_id)
        response: GetFirebaseConfigResponse = await self._app_client.GetFirebaseConfig(request, metadata=self._metadata, timeout=timeout)
        return response.app_id

    async def delete_firebase_config(self, org_id: str, app_id: str, timeout: float | None = None) -> None:
        """Delete the Firebase configuration for an organization.

        Args:
            org_id (str): The organization ID.
            app_id (str): The Firebase app ID.
            timeout (float | None): An option to set how long to wait (in seconds) before calling a time-out and closing the underlying RPC call.
        """
        request = DeleteFirebaseConfigRequest(org_id=org_id, app_id=app_id)
        _: DeleteFirebaseConfigResponse = await self._app_client.DeleteFirebaseConfig(request, metadata=self._metadata, timeout=timeout)
