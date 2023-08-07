from datetime import datetime
import pytest

from grpclib.testing import ChannelFor

from viam.app.app_client import AppClient
from viam.utils import datetime_to_timestamp, struct_to_dict
from viam.proto.app import (
    Organization,
    Location,
    Robot,
    RobotPart,
    LogEntry,
    Fragment,
    LocationAuth,
    RobotPartHistoryEntry,
    Authorization
)

from .mocks.services import MockApp

METADATA = {"key": "value"}

ID = "id"
IDS = [ID]
NAME = "name"
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
COUNT = 1
LOCATION = Location(
    id=ID,
    name=NAME,
    parent_location_id=ID,
    auth=None,
    organizations=None,
    created_on=TIME,
    robot_count=COUNT,
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
INDENT = 1
FILTER = "filter"
ERRORS_ONLY = True
NUM_LOGS = 1
HOST = "host"
LEVEL = "level"
LOGGER_NAME = "logger_name"
MESSAGE = "message"
STACK = "stack"
LOG_ENTRY = LogEntry(host=HOST, level=LEVEL, time=TIME, logger_name=LOGGER_NAME, message=MESSAGE, caller=None, stack=STACK, fields=None)
LOG_ENTRIES = [LOG_ENTRY]
ROBOT_CONFIG = {"key": "value"}
SHOW_PUBLIC = True
ORGANIZATION_OWNER = "organization_owner"
PUBLIC = True
ORGANIZATION_NAME = "organization_name"
ONLY_USED_BY_OWNER = True
FRAGMENT = Fragment(
    id=ID,
    name=NAME,
    fragment=None,
    organization_owner=ORGANIZATION_OWNER,
    public=PUBLIC,
    created_on=TIME,
    organization_name=ORGANIZATION_NAME,
    robot_part_count=COUNT,
    only_used_by_owner=ONLY_USED_BY_OWNER,
)
NAMESPACE = "namespace"
AVAILABLE = True
LOCATION_AUTH = LocationAuth(
    secret=SECRET,
    location_id=ID,
    secrets=None
)
PART = "part"
ROBOT_PART_HISTORY_ENTRY = RobotPartHistoryEntry(
    part=PART,
    robot=ID,
    when=TIME,
    old=None
)
ROBOT_PART_HISTORY = [ROBOT_PART_HISTORY_ENTRY]
TYPE = "type"
ROLE = "role"
AUTHORIZATION = Authorization(
    authorization_type=TYPE,
    authorization_id=ID,
    resource_type=TYPE,
    resource_id=ID,
    identity_id=ID,
    organization_id=ID
)
AUTHORIZATIONS = [AUTHORIZATION]


@pytest.fixture(scope="function")
def service() -> MockApp:
    return MockApp(
        organizations=ORGANIZATIONS,
        location=LOCATION,
        robot=ROBOT,
        robot_part=ROBOT_PART,
        log_entry=LOG_ENTRY,
        id=ID,
        fragment=FRAGMENT,
        available=AVAILABLE,
        location_auth=LOCATION_AUTH,
        robot_part_history=ROBOT_PART_HISTORY,
        authorizations=AUTHORIZATIONS
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_get_organization_namespace_availability(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            available = await client.get_organization_namespace_availability(public_namespace=NAMESPACE)
            assert available == AVAILABLE
            assert service.namespace == NAMESPACE

    @pytest.mark.asyncio
    async def test_list_organizations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            organizations = await client.list_organizations()
            assert organizations == ORGANIZATIONS

    @pytest.mark.asyncio
    async def test_create_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            new_location = await client.create_location(name=NAME, parent_location_id=ID)
            assert service.name == NAME
            assert service.parent_location_id == ID
            assert new_location == LOCATION

    @pytest.mark.asyncio
    async def test_get_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            location = await client.get_location(location_id=ID)
            assert service.location_id == ID
            assert location == LOCATION

    @pytest.mark.asyncio
    async def test_update_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            updated_location = await client.update_location(location_id=ID, name=NAME, parent_location_id=ID)
            assert service.location_id == ID
            assert service.name == NAME
            assert service.parent_location_id == ID
            assert updated_location == LOCATION

    @pytest.mark.asyncio
    async def test_delete_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_location(location_id=ID)
            assert service.location_id == ID

    @pytest.mark.asyncio
    async def test_list_locations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            locations = await client.list_locations()
            assert locations == locations

    @pytest.mark.asyncio
    async def test_location_auth(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            location_auth = await client.location_auth(location_id=ID)
            assert location_auth == LOCATION_AUTH
            assert service.location_id == ID

    @pytest.mark.asyncio
    async def test_create_location_secret(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            location_auth = await client.create_location_secret(location_id=ID)
            assert location_auth == LOCATION_AUTH
            assert service.location_id == ID

    @pytest.mark.asyncio
    async def test_delete_location_secret(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_location_secret(secret_id=ID, location_id=ID)
            assert service.secret_id == ID
            assert service.location_id == ID

    @pytest.mark.asyncio
    async def test_get_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot = await client.get_robot(robot_id=ID)
            assert service.robot_id == ID
            assert robot == ROBOT

    @pytest.mark.asyncio
    async def test_get_robot_parts(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot_parts = await client.get_robot_parts(robot_id=ID)
            assert service.robot_id == ID
            assert [robot_part.proto for robot_part in robot_parts] == ROBOT_PARTS

    @pytest.mark.asyncio
    async def test_get_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot_part = await client.get_robot_part(robot_part_id=ID, indent=INDENT)
            assert service.robot_part_id == ID
            assert robot_part.proto == ROBOT_PART

    @pytest.mark.asyncio
    async def test_get_robot_part_logs(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            log_entries = await client.get_robot_part_logs(
                robot_part_id=ID, filter=FILTER, errors_only=ERRORS_ONLY, num_log_entries=NUM_LOGS
            )
            assert service.robot_part_id == ID
            assert service.filter == FILTER
            assert service.errors_only == ERRORS_ONLY
            assert [log_entry.proto for log_entry in log_entries] == LOG_ENTRIES

    @pytest.mark.asyncio
    async def test_tail_robot_part_logs(self, service: MockApp):
        pass

    @pytest.mark.asyncio
    async def test_get_robot_part_history(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot_part_history = await client.get_robot_part_history(robot_part_id=ID)
            assert service.robot_part_id == ID
            assert len(robot_part_history) == len(ROBOT_PART_HISTORY)
            for i in range(len(ROBOT_PART_HISTORY)):
                assert robot_part_history[i].proto == ROBOT_PART_HISTORY[i]

    @pytest.mark.asyncio
    async def test_update_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            updated_robot_part = await client.update_robot_part(robot_part_id=ID, name=NAME, robot_config=ROBOT_CONFIG)
            assert service.robot_part_id == ID
            assert service.name == NAME
            assert struct_to_dict(service.robot_config) == ROBOT_CONFIG
            assert updated_robot_part.proto == ROBOT_PART

    @pytest.mark.asyncio
    async def test_new_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            new_robot_part_id = await client.new_robot_part(robot_id=ID, part_name=NAME)
            assert service.robot_id == ID
            assert service.part_name == NAME
            assert new_robot_part_id == ID

    @pytest.mark.asyncio
    async def test_delete_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_robot_part(robot_part_id=ID)
            assert service.robot_part_id == ID

    @pytest.mark.asyncio
    async def test_mark_part_as_main(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.mark_part_as_main(robot_part_id=ID)
            assert service.robot_part_id == ID

    @pytest.mark.asyncio
    async def test_mark_part_for_restart(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.mark_part_for_restart(robot_part_id=ID)
            assert service.robot_part_id == ID

    @pytest.mark.asyncio
    async def test_create_robot_part_secret(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robot_part = await client.create_robot_part_secret(robot_part_id=ID)
            assert service.robot_part_id == ID
            assert robot_part.proto == ROBOT_PART

    @pytest.mark.asyncio
    async def test_delete_robot_part_secret(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_robot_part_secret(robot_part_id=ID, secret_id=ID)
            assert service.robot_part_id == ID
            assert service.secret_id == ID

    @pytest.mark.asyncio
    async def test_list_robots(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            robots = await client.list_robots(location_id=ID)
            assert service.location_id == ID
            assert robots == [ROBOT]

    @pytest.mark.asyncio
    async def test_new_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            new_robot_id = await client.new_robot(name=NAME, location_id=ID)
            assert service.name == NAME
            assert service.location_id == ID
            assert new_robot_id == ID

    @pytest.mark.asyncio
    async def test_update_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            updated_robot = await client.update_robot(robot_id=ID, name=NAME, location_id=ID)
            assert service.robot_id == ID
            assert service.name == NAME
            assert service.location_id == ID
            assert updated_robot == ROBOT

    @pytest.mark.asyncio
    async def test_delete_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_robot(robot_id=ID)
            assert service.robot_id == ID

    @pytest.mark.asyncio
    async def test_list_fragments(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragments = await client.list_fragments(show_public=SHOW_PUBLIC)
            assert service.show_public == SHOW_PUBLIC
            assert [fragment.proto for fragment in fragments] == [FRAGMENT]

    @pytest.mark.asyncio
    async def test_get_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragment = await client.get_fragment(fragment_id=ID)
            assert service.fragment_id == ID
            assert fragment.proto == FRAGMENT

    @pytest.mark.asyncio
    async def test_create_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragment = await client.create_fragment(name=NAME)
            assert service.name == NAME
            assert fragment.proto == FRAGMENT

    @pytest.mark.asyncio
    async def test_update_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            fragment = await client.update_fragment(fragment_id=ID, name=NAME, public=PUBLIC)
            assert service.fragment_id == ID
            assert service.name == NAME
            assert service.public == PUBLIC
            assert fragment.proto == FRAGMENT

    @pytest.mark.asyncio
    async def test_delete_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.delete_fragment(fragment_id=ID)
            assert service.id == ID

    @pytest.mark.asyncio
    async def test_add_role(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.add_role(identity_id=ID, role=ROLE, resource_type=TYPE, resource_id=ID)
            assert service.identity_id == ID
            assert service.role == ROLE
            assert service.resource_type == TYPE
            assert service.resource_id == ID

    @pytest.mark.asyncio
    async def test_remove_role(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            await client.remove_role(identity_id=ID, role=ROLE, resource_type=TYPE, resource_id=ID)
            assert service.identity_id == ID
            assert service.role == ROLE
            assert service.resource_type == TYPE
            assert service.resource_id == ID

    @pytest.mark.asyncio
    async def test_list_authorizations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, ID)
            authorizations = await client.list_authorizations(resource_ids=IDS)
            assert service.resource_ids == IDS
            assert authorizations == AUTHORIZATIONS
