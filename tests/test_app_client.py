from datetime import datetime

import pytest
from grpclib.testing import ChannelFor

from viam.app.app_client import APIKeyAuthorization, AppClient, Fragment, FragmentVisibilityPB
from viam.proto.app import (
    APIKey,
    APIKeyWithAuthorizations,
    AuthenticatorInfo,
    Authorization,
    AuthorizationDetails,
    AuthorizedPermissions,
    FragmentHistoryEntry,
    Location,
    LocationAuth,
    Model,
    Module,
    ModuleFileInfo,
    ModuleMetadata,
    Organization,
    OrganizationInvite,
    OrganizationMember,
    RegistryItem,
    RegistryItemStatus,
    Robot,
    RobotPart,
    RobotPartHistoryEntry,
    RoverRentalRobot,
    Visibility,
)
from viam.proto.app import Fragment as FragmentPB
from viam.proto.app.packages import PackageType
from viam.proto.common import LogEntry
from viam.utils import datetime_to_timestamp, struct_to_dict

from .mocks.services import MockApp

METADATA = {"key": "value"}

ID = "id"
IDS = [ID]
NAME = "name"
CID = "cid"
PAGE_TOKEN = "123"
PAGE_LIMIT = 20
TIME = datetime_to_timestamp(datetime.now())
PUBLIC_NAMESPACE = "public_namespace"
DEFAULT_REGION = "default_region"
ORGANIZATION = Organization(
    id=ID,
    name=NAME,
    created_on=TIME,
    public_namespace=PUBLIC_NAMESPACE,
    default_region=DEFAULT_REGION,
)
ORGANIZATIONS = [ORGANIZATION]
NUM = 1
LOCATION = Location(
    id=ID,
    name=NAME,
    parent_location_id=ID,
    auth=None,
    organizations=None,
    created_on=TIME,
    robot_count=NUM,
    config=None,
)
ROBOT = Robot(id=ID, name=NAME, location=ID, last_access=TIME, created_on=TIME)
DNS_NAME = "dns_name"
SECRET = "secret"
MAIN_PART = True
FQDN = "fqdn"
LOCAL_FQDN = "local_fqdn"
ROBOT_PART = RobotPart(
    id=ID,
    name=NAME,
    dns_name=DNS_NAME,
    secret=SECRET,
    robot=ID,
    location_id=ID,
    robot_config=None,
    last_access=TIME,
    user_supplied_info=None,
    main_part=MAIN_PART,
    fqdn=FQDN,
    local_fqdn=LOCAL_FQDN,
    created_on=TIME,
    secrets=None,
)
ROBOT_PARTS = [ROBOT_PART]
ROVER_RENTAL_ROBOT = RoverRentalRobot(
    robot_id=ID,
    location_id="location",
    robot_name=NAME,
    robot_main_part_id=ID,
)
ROVER_RENTAL_ROBOTS = [ROVER_RENTAL_ROBOT]
FILTER = "filter"
ERRORS_ONLY = True
LOG_LEVELS = ["error", "warn"]
HOST = "host"
LEVEL = "level"
LOGGER_NAME = "logger_name"
MESSAGE = "message"
STACK = "stack"
LOG_ENTRY = LogEntry(host=HOST, level=LEVEL, time=TIME, logger_name=LOGGER_NAME, message=MESSAGE, caller=None, stack=STACK, fields=None)
LOG_ENTRIES = [LOG_ENTRY]
ROBOT_CONFIG = {"key": "value"}
FRAGMENT_VISIBILITY = [Fragment.Visibility.PUBLIC]
FRAGMENT_VISIBILITY_PB = [FragmentVisibilityPB.FRAGMENT_VISIBILITY_PUBLIC]
ORGANIZATION_OWNER = "organization_owner"
PUBLIC = True
ORGANIZATION_NAME = "organization_name"
ONLY_USED_BY_OWNER = True
FRAGMENT = FragmentPB(
    id=ID,
    name=NAME,
    fragment=None,
    organization_owner=ORGANIZATION_OWNER,
    public=PUBLIC,
    created_on=TIME,
    organization_name=ORGANIZATION_NAME,
    robot_part_count=NUM,
    only_used_by_owner=ONLY_USED_BY_OWNER,
)
NAMESPACE = "namespace"
AVAILABLE = True
LOCATION_AUTH = LocationAuth(secret=SECRET, location_id=ID, secrets=None)
PART = "part"
ROBOT_PART_HISTORY_ENTRY = RobotPartHistoryEntry(part=PART, robot=ID, when=TIME, old=None)
ROBOT_PART_HISTORY = [ROBOT_PART_HISTORY_ENTRY]
AUTHENTICATOR_INFO = AuthenticatorInfo(value="value", is_deactivated=True, type=1)
FRAGMENT_HISTORY_ENTRY = FragmentHistoryEntry(fragment=ID, edited_by=AUTHENTICATOR_INFO, old=FRAGMENT, edited_on=TIME)
FRAGMENT_HISTORY = [FRAGMENT_HISTORY_ENTRY]
TYPE = "robot"
ROLE = "operator"
API_KEY = "key"
API_KEY_AUTHORIZATION = APIKeyAuthorization(role=ROLE, resource_type=TYPE, resource_id=ID)
API_KEY_AUTHORIZATIONS = [API_KEY_AUTHORIZATION]
AUTHORIZATION = Authorization(
    authorization_type=TYPE, authorization_id=ID, resource_type=TYPE, resource_id=ID, identity_id=ID, organization_id=ID
)
AUTHORIZATION_DETAIL = AuthorizationDetails(authorization_type=TYPE, authorization_id=ID, resource_type=TYPE, resource_id=ID, org_id=ID)
AUTHORIZATION_DETAILS = [AUTHORIZATION_DETAIL]
AUTHORIZATIONS = [AUTHORIZATION]
API_KEY_WITH_AUTHORIZATIONS = APIKeyWithAuthorizations(
    api_key=APIKey(id=ID, key=API_KEY, name=NAME),
    authorizations=AUTHORIZATION_DETAILS,
)
API_KEYS_WITH_AUTHORIZATIONS = [API_KEY_WITH_AUTHORIZATIONS]
PERMISSION = AuthorizedPermissions(
    resource_type=TYPE,
    resource_id=ID,
    permissions=["control_robot"],
)
PERMISSIONS = [PERMISSION]
VISIBILITY = Visibility.VISIBILITY_PUBLIC
URL = "url"
DESCRIPTION = "description"
USAGE = 100
MODULE_METADATA = ModuleMetadata()
MODEL = "model"
API = "api"
MODELS = [Model(api=API, model=MODEL)]
ENTRYPOINT = "entrypoint"
PACKAGE_TYPE = PackageType.PACKAGE_TYPE_UNSPECIFIED
STATUS = RegistryItemStatus.REGISTRY_ITEM_STATUS_UNSPECIFIED
ITEM = RegistryItem(
    item_id=ID,
    organization_id=ID,
    public_namespace=PUBLIC_NAMESPACE,
    name=NAME,
    type=PACKAGE_TYPE,
    visibility=VISIBILITY,
    url=URL,
    description=DESCRIPTION,
    total_robot_usage=USAGE,
    total_external_robot_usage=USAGE,
    total_organization_usage=USAGE,
    total_external_organization_usage=USAGE,
)
ITEMS = [ITEM]
MODULE = Module(
    module_id=ID,
    organization_id=ID,
    name=NAME,
    visibility=VISIBILITY,
    versions=None,
    url=URL,
    description=DESCRIPTION,
    models=MODELS,
    entrypoint=ENTRYPOINT,
    total_robot_usage=NUM,
    total_organization_usage=NUM,
)
MODULES = [MODULE]
EMAIL = "email"
EMAILS = [EMAIL]
MEMBER = OrganizationMember(user_id=ID, emails=EMAILS, date_added=TIME)
MEMBERS = [MEMBER]
INVITE = OrganizationInvite(organization_id=ID, email=EMAIL, created_on=TIME)
INVITES = [INVITE]
VERSION = "version"
PLATFORM = "platform"
MODULE_FILE_INFO = ModuleFileInfo(module_id=ID, version=VERSION, platform=PLATFORM)
FILE = b"file"
USER_DEFINED_METADATA = {"number": 0, "string": "string"}


@pytest.fixture(scope="function")
def service() -> MockApp:
    return MockApp(
        organizations=ORGANIZATIONS,
        location=LOCATION,
        robot=ROBOT,
        robot_part=ROBOT_PART,
        log_entry=LOG_ENTRY,
        id=ID,
        name=NAME,
        fragment=FRAGMENT,
        available=AVAILABLE,
        location_auth=LOCATION_AUTH,
        robot_part_history=ROBOT_PART_HISTORY,
        fragment_history=FRAGMENT_HISTORY,
        authorizations=AUTHORIZATIONS,
        url=URL,
        module=MODULE,
        members=MEMBERS,
        invite=INVITE,
        rover_rental_robots=ROVER_RENTAL_ROBOTS,
        api_key=API_KEY,
        api_keys_with_authorizations=API_KEYS_WITH_AUTHORIZATIONS,
        items=[ITEM],
        package_type=PACKAGE_TYPE,
    )


class TestClient:
    async def test_get_user_id_by_email(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            id = await client.get_user_id_by_email(EMAIL)
            assert id == ID

    async def test_create_organization(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            org = await client.create_organization(NAME)
            assert org == ORGANIZATION

    async def test_get_organizations_with_access_to_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            orgs = await client.get_organizations_with_access_to_location(ID)
            assert orgs[0].name == NAME
            assert orgs[0].id == ID

    async def test_list_organizations_by_user(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            orgs = await client.list_organizations_by_user(ID)
            assert orgs[0].org_name == NAME
            assert orgs[0].org_id == ID

    async def test_get_organization(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            org = await client.get_organization(org_id=ID)
            assert org == ORGANIZATION
            available = await client.get_organization_namespace_availability(public_namespace=NAMESPACE)
            assert available == AVAILABLE
            assert service.namespace == NAMESPACE

    async def test_get_organization_namespace_availability(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            available = await client.get_organization_namespace_availability(public_namespace=NAMESPACE)
            assert available == AVAILABLE
            assert service.namespace == NAMESPACE

    async def test_list_organization_members(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            members, invites = await client.list_organization_members(org_id=ID)
            assert members == MEMBERS
            assert invites == INVITES

    async def test_list_organizations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            organizations = await client.list_organizations()
            assert organizations == ORGANIZATIONS

    async def test_update_organization(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            org = await client.update_organization(org_id=ID, name=NAME, public_namespace=PUBLIC_NAMESPACE, region=DEFAULT_REGION, cid=CID)
            assert org == ORGANIZATION
            assert service.update_region == DEFAULT_REGION
            assert service.update_cid == CID
            assert service.update_name == NAME
            assert service.update_namespace == PUBLIC_NAMESPACE

    async def test_update_organization_invite_authorizations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            invite = await client.update_organization_invite_authorizations(
                org_id=ID, email=EMAIL, add_authorizations=AUTHORIZATIONS, remove_authorizations=AUTHORIZATIONS
            )
            assert invite == INVITE
            assert service.email == EMAIL
            assert service.add_authorizations == AUTHORIZATIONS
            assert service.remove_authorizations == AUTHORIZATIONS

    async def test_delete_organization(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_organization(ID)
            assert service.delete_org_called is True

    async def test_delete_organization_member(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_organization_member(org_id=ID, user_id=ID)
            assert service.deleted_member_id == ID

    async def test_create_organization_invite(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            invite = await client.create_organization_invite(org_id=ID, email=EMAIL, authorizations=AUTHORIZATIONS)
            assert invite == INVITE
            assert service.send_email_invite is True

            await client.create_organization_invite(org_id=ID, email=EMAIL, authorizations=AUTHORIZATIONS, send_email_invite=False)
            assert service.send_email_invite is False

    async def test_delete_organization_invite(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_organization_invite(org_id=ID, email=EMAIL)
            assert service.deleted_invite_email == EMAIL

    async def test_resend_organization_invite(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.resend_organization_invite(org_id=ID, email=EMAIL)
            assert service.resent_invite_email == EMAIL

    async def test_create_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            new_location = await client.create_location(org_id=ID, name=NAME, parent_location_id=ID)
            assert service.name == NAME
            assert service.parent_location_id == ID
            assert new_location == LOCATION

    async def test_get_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            location = await client.get_location(location_id=ID)
            assert service.location_id == ID
            assert location == LOCATION

    async def test_update_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            updated_location = await client.update_location(location_id=ID, name=NAME, parent_location_id=ID)
            assert service.location_id == ID
            assert service.name == NAME
            assert service.parent_location_id == ID
            assert updated_location == LOCATION

    async def test_delete_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_location(location_id=ID)
            assert service.location_id == ID

    async def test_list_locations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            locations = await client.list_locations(org_id=ID)
            assert locations == locations

    async def test_share_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.share_location(organization_id=ID, location_id=ID)
            assert service.location_id == ID
            assert service.organization_id == ID

    async def test_unshare_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.unshare_location(organization_id=ID, location_id=ID)
            assert service.location_id == ID
            assert service.organization_id == ID

    async def test_location_auth(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            location_auth = await client.location_auth(location_id=ID)
            assert location_auth == LOCATION_AUTH
            assert service.location_id == ID

    async def test_create_location_secret(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            location_auth = await client.create_location_secret(location_id=ID)
            assert location_auth == LOCATION_AUTH
            assert service.location_id == ID

    async def test_delete_location_secret(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_location_secret(secret_id=ID, location_id=ID)
            assert service.secret_id == ID
            assert service.location_id == ID

    async def test_get_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot = await client.get_robot(robot_id=ID)
            assert service.robot_id == ID
            assert robot == ROBOT

    async def test_get_rover_rental_robots(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robots = await client.get_rover_rental_robots(org_id=ID)
            assert robots == ROVER_RENTAL_ROBOTS

    async def test_get_robot_parts(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot_parts = await client.get_robot_parts(robot_id=ID)
            assert service.robot_id == ID
            assert [robot_part.proto for robot_part in robot_parts] == ROBOT_PARTS

    async def test_get_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot_part = await client.get_robot_part(robot_part_id=ID, indent=NUM)
            assert service.robot_part_id == ID
            assert robot_part.proto == ROBOT_PART

    async def test_get_robot_part_logs(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            log_entries = await client.get_robot_part_logs(robot_part_id=ID, filter=FILTER, log_levels=LOG_LEVELS, num_log_entries=NUM)
            assert service.robot_part_id == ID
            assert service.filter == FILTER
            assert service.levels == LOG_LEVELS
            assert [log_entry.proto for log_entry in log_entries] == LOG_ENTRIES

    async def test_tail_robot_part_logs(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            logs_stream = await client.tail_robot_part_logs(robot_part_id=ID, errors_only=ERRORS_ONLY, filter=FILTER)
            [logs async for logs in logs_stream]  # Iterate over returned value to implicitly call __anext__() so server runs properly.
            assert service.robot_part_id == ID
            assert service.errors_only == ERRORS_ONLY
            assert service.filter == FILTER

    async def test_get_robot_part_history(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot_part_history = await client.get_robot_part_history(robot_part_id=ID)
            assert service.robot_part_id == ID
            assert len(robot_part_history) == len(ROBOT_PART_HISTORY)
            for i in range(len(ROBOT_PART_HISTORY)):
                assert robot_part_history[i].proto == ROBOT_PART_HISTORY[i]

    async def test_update_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            updated_robot_part = await client.update_robot_part(robot_part_id=ID, name=NAME, robot_config=ROBOT_CONFIG)
            assert service.robot_part_id == ID
            assert service.name == NAME
            assert struct_to_dict(service.robot_config) == ROBOT_CONFIG
            assert updated_robot_part.proto == ROBOT_PART

    async def test_new_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            new_robot_part_id = await client.new_robot_part(robot_id=ID, part_name=NAME)
            assert service.robot_id == ID
            assert service.part_name == NAME
            assert new_robot_part_id == ID

    async def test_delete_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_robot_part(robot_part_id=ID)
            assert service.robot_part_id == ID

    async def test_get_robot_api_keys(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            keys = await client.get_robot_api_keys(ID)
            assert keys[0].api_key == API_KEY_WITH_AUTHORIZATIONS.api_key
            assert keys[0].authorizations[0] == AUTHORIZATION_DETAIL

    async def test_mark_part_as_main(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.mark_part_as_main(robot_part_id=ID)
            assert service.robot_part_id == ID

    async def test_mark_part_for_restart(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.mark_part_for_restart(robot_part_id=ID)
            assert service.robot_part_id == ID

    async def test_create_robot_part_secret(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot_part = await client.create_robot_part_secret(robot_part_id=ID)
            assert service.robot_part_id == ID
            assert robot_part.proto == ROBOT_PART

    async def test_delete_robot_part_secret(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_robot_part_secret(robot_part_id=ID, secret_id=ID)
            assert service.robot_part_id == ID
            assert service.secret_id == ID

    async def test_list_robots(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robots = await client.list_robots(location_id=ID)
            assert service.location_id == ID
            assert robots == [ROBOT]

    async def test_new_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            new_robot_id = await client.new_robot(name=NAME, location_id=ID)
            assert service.name == NAME
            assert service.location_id == ID
            assert new_robot_id == ID

    async def test_update_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            updated_robot = await client.update_robot(robot_id=ID, name=NAME, location_id=ID)
            assert service.robot_id == ID
            assert service.name == NAME
            assert service.location_id == ID
            assert updated_robot == ROBOT

    async def test_delete_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_robot(robot_id=ID)
            assert service.robot_id == ID

    async def test_list_fragments(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragments = await client.list_fragments(org_id=ID, visibilities=FRAGMENT_VISIBILITY)
            assert service.fragment_visibility == FRAGMENT_VISIBILITY_PB
            assert [fragment.proto for fragment in fragments] == [FRAGMENT]

    async def test_get_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragment = await client.get_fragment(fragment_id=ID)
            assert service.fragment_id == ID
            assert fragment.proto == FRAGMENT

    async def test_create_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragment = await client.create_fragment(org_id=ID, name=NAME)
            assert service.name == NAME
            assert fragment.proto == FRAGMENT

    async def test_update_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragment = await client.update_fragment(fragment_id=ID, name=NAME, public=PUBLIC)
            assert service.fragment_id == ID
            assert service.name == NAME
            assert service.public == PUBLIC
            assert fragment.proto == FRAGMENT

    async def test_delete_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_fragment(fragment_id=ID)
            assert service.id == ID

    async def test_get_fragment_history(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragment_history = await client.get_fragment_history(id=ID, page_token=PAGE_TOKEN, page_limit=PAGE_LIMIT)
            assert service.fragment.id == ID
            assert len(fragment_history) == len(FRAGMENT_HISTORY)
            assert service.id == ID
            assert service.page_token == PAGE_TOKEN
            assert service.page_limit == PAGE_LIMIT
            for i in range(len(FRAGMENT_HISTORY)):
                assert fragment_history[i].proto == FRAGMENT_HISTORY[i]

    async def test_add_role(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.add_role(org_id=ID, identity_id=ID, role=ROLE, resource_type=TYPE, resource_id=ID)
            assert service.identity_id == ID
            assert service.role == ROLE
            assert service.resource_type == TYPE
            assert service.resource_id == ID

    async def test_remove_role(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.remove_role(org_id=ID, identity_id=ID, role=ROLE, resource_type=TYPE, resource_id=ID)
            assert service.identity_id == ID
            assert service.role == ROLE
            assert service.resource_type == TYPE
            assert service.resource_id == ID

    async def test_change_role(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.change_role(
                organization_id=ID,
                old_identity_id=ID,
                old_role=ROLE,
                old_resource_type=TYPE,
                old_resource_id=ID,
                new_identity_id=ID,
                new_role=ROLE,
                new_resource_type=TYPE,
                new_resource_id=ID,
            )
            assert service.change_role_called is True

    async def test_check_permissions(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            permissions = await client.check_permissions(permissions=PERMISSIONS)
            assert permissions == PERMISSIONS

    async def test_list_authorizations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            authorizations = await client.list_authorizations(org_id=ID, resource_ids=IDS)
            assert service.resource_ids == IDS
            assert authorizations == AUTHORIZATIONS

    async def test_get_registry_item(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            item = await client.get_registry_item(ID)
            assert item.item_id == ITEM.item_id
            assert item.name == ITEM.name
            assert item.visibility == ITEM.visibility
            assert item.total_robot_usage == ITEM.total_robot_usage

    async def test_create_registry_item(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.create_registry_item(ID, NAME, PACKAGE_TYPE)
            assert service.name == NAME
            assert service.package_type == PACKAGE_TYPE
            assert service.organization_id == ID

    async def test_update_registry_item(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.update_registry_item(ID, PACKAGE_TYPE, DESCRIPTION, VISIBILITY)
            assert service.id == ID
            assert service.package_type == PACKAGE_TYPE
            assert service.description == DESCRIPTION
            assert service.visibility == VISIBILITY

    async def test_list_registry_items(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            items = await client.list_registry_items(ID, [PACKAGE_TYPE], [VISIBILITY], [PLATFORM], [STATUS])
            assert items[0].item_id == ID
            assert items[0].public_namespace == PUBLIC_NAMESPACE
            assert items[0].total_external_organization_usage == USAGE

    async def test_delete_registry_item(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_registry_item(ID)
            assert service.id == ID
            assert service.delete_item_called is True

    async def test_create_module(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            id, url = await client.create_module(org_id=ID, name=NAME)
            assert service.name == NAME
            assert id == ID
            assert url == URL

    async def test_update_module(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            url = await client.update_module(
                module_id=ID, url=URL, description=DESCRIPTION, models=MODELS, entrypoint=ENTRYPOINT, public=PUBLIC
            )
            assert url == URL
            assert service.module_id == ID
            assert service.module_url == URL
            assert service.description == DESCRIPTION
            assert service.models == MODELS
            assert service.entrypoint == ENTRYPOINT
            assert service.visibility == VISIBILITY

    async def test_created_module(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            url = await client.update_module(module_id=ID, url=URL, description=DESCRIPTION, models=MODELS, entrypoint=ENTRYPOINT)
            assert service.module_id == ID
            assert service.description == DESCRIPTION
            assert service.models == MODELS
            assert service.entrypoint == ENTRYPOINT
            assert url == URL

    async def test_upload_module_file(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            id = await client.upload_module_file(module_file_info=MODULE_FILE_INFO, file=FILE)
            assert id == ID
            assert service.module_file_info == MODULE_FILE_INFO
            assert service.file == FILE

    async def test_get_module(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            module = await client.get_module(module_id=ID)
            assert service.module_id == ID
            assert module == MODULE

    async def test_list_modules(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            modules = await client.list_modules(org_id=ID)
            assert modules == MODULES

    async def test_create_key(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            api_key = await client.create_key(org_id=ID, authorizations=API_KEY_AUTHORIZATIONS, name=NAME)
            assert (API_KEY, ID) == api_key

    async def test_delete_key(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_key(ID)
            assert service.id == ID
            assert service.delete_key_called is True

    async def test_create_key_from_existing_key_authorizations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            api_key = await client.create_key_from_existing_key_authorizations(id=ID)
            assert (API_KEY, ID) == api_key

    async def list_keys(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            api_keys = await client.list_keys(org_id=ID)
            assert api_keys == API_KEYS_WITH_AUTHORIZATIONS

    async def test_rotate_key(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            key, id = await client.rotate_key(ID)
            assert key == API_KEY
            assert id == ID

    async def test_get_organization_metadata(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)

            try:
                await client.update_organization_metadata(ID, USER_DEFINED_METADATA)
            except Exception as e:
                print("1")
                print(e)


            try:
                user_defined_metadata = await client.get_organization_metadata(ID)
            except Exception as e:
                print("2")
                print(e)
                user_defined_metadata = None

            assert user_defined_metadata == USER_DEFINED_METADATA

    # async def test_get_and_update_organization_metadata(self, service: MockApp):
    #     async with ChannelFor([service]) as channel:
    #         client = AppClient(channel, METADATA, ID)
    #         await client.update_organization_metadata(ID, USER_DEFINED_METADATA)
    #         user_defined_metadata = await client.get_organization_metadata(ID)
    #         assert user_defined_metadata == USER_DEFINED_METADATA
    #
    # async def test_get_and_update_location_metadata(self, service: MockApp):
    #     async with ChannelFor([service]) as channel:
    #         client = AppClient(channel, METADATA, ID)
    #         await client.update_location_metadata(ID, USER_DEFINED_METADATA)
    #         user_defined_metadata = await client.get_location_metadata(ID)
    #         assert user_defined_metadata == USER_DEFINED_METADATA
    #
    # async def test_get_and_update_robot_metadata(self, service: MockApp):
    #     async with ChannelFor([service]) as channel:
    #         client = AppClient(channel, METADATA, ID)
    #         await client.update_robot_metadata(ID, USER_DEFINED_METADATA)
    #         user_defined_metadata = await client.get_robot_metadata(ID)
    #         assert user_defined_metadata == USER_DEFINED_METADATA
    #
    # async def test_get_and_update_robot_part_metadata(self, service: MockApp):
    #     async with ChannelFor([service]) as channel:
    #         client = AppClient(channel, METADATA, ID)
    #         await client.update_robot_part_metadata(ID, USER_DEFINED_METADATA)
    #         user_defined_metadata = await client.get_robot_part_metadata(ID)
    #         assert user_defined_metadata == USER_DEFINED_METADATA
