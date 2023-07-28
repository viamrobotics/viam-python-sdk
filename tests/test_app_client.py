from datetime import datetime
import pytest

from grpclib.testing import ChannelFor

from viam.app.app_client import AppClient
from viam.utils import datetime_to_timestamp, struct_to_dict
from viam.proto.app import Organization, Location, Robot, RobotPart, LogEntry, Fragment

from .mocks.services import MockApp

METADATA = {"key": "value"}
LOCATION_ID = "location_id"

ID = "id"
NAME = "name"
CREATED_ON = datetime_to_timestamp(datetime.now())
PUBLIC_NAMESPACE = "public_namespace"
DEFAULT_REGION = "default_region"
ORGANIZATION = Organization(
    id=ID,
    name=NAME,
    created_on=CREATED_ON,
    public_namespace=PUBLIC_NAMESPACE,
    default_region=DEFAULT_REGION,
)
ORGANIZATIONS = [ORGANIZATION]
ORGANIZATION_ID = "organization_id"
PARENT_LOCATION_ID = "parent_location_id"
ROBOT_COUNT = 1
LOCATION = Location(
    id=ID,
    name=NAME,
    parent_location_id=PARENT_LOCATION_ID,
    auth=None,
    organizations=None,
    created_on=CREATED_ON,
    robot_count=ROBOT_COUNT,
    config=None,
)
ROBOT_ID = "robot_id"
LAST_ACCESS = datetime_to_timestamp(datetime.now())
ROBOT = Robot(id=ID, name=NAME, location=LOCATION_ID, last_access=LAST_ACCESS, created_on=CREATED_ON)
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
    robot=ROBOT_ID,
    location_id=LOCATION_ID,
    robot_config=None,
    last_access=LAST_ACCESS,
    user_supplied_info=None,
    main_part=MAIN_PART,
    fqdn=FQDN,
    local_fqdn=LOCAL_FQDN,
    created_on=CREATED_ON,
    secrets=None,
)
ROBOT_PARTS = [ROBOT_PART]
ROBOT_PART_ID = "robot_part_id"
DEST = "dest"
INDENT = 1
FILTER = "filter"
ERRORS_ONLY = True
NUM_PAGES = 1
HOST = "host"
LEVEL = "level"
TIME = datetime_to_timestamp(datetime.now())
LOGGER_NAME = "logger_name"
MESSAGE = "message"
STACK = "stack"
LOG_ENTRY = LogEntry(host=HOST, level=LEVEL, time=TIME, logger_name=LOGGER_NAME, message=MESSAGE, caller=None, stack=STACK, fields=None)
LOG_ENTRIES = [LOG_ENTRY]
ROBOT_CONFIG = {"key": "value"}
SHOW_PUBLIC = True
FRAGMENT_ID = "fragment_id"
ORGANIZATION_OWNER = "organization_ownder"
PUBLIC = True
ORGANIZATION_NAME = "organization_name"
ROBOT_PART_COUNT = 1
ONLY_USED_BY_OWNER = True
FRAGMENT = Fragment(
    id=ID,
    name=NAME,
    fragment=None,
    organization_owner=ORGANIZATION_OWNER,
    public=PUBLIC,
    created_on=CREATED_ON,
    organization_name=ORGANIZATION_NAME,
    robot_part_count=ROBOT_PART_COUNT,
    only_used_by_owner=ONLY_USED_BY_OWNER,
)


@pytest.fixture(scope="function")
def service() -> MockApp:
    return MockApp(
        organizations=ORGANIZATIONS, location=LOCATION, robot=ROBOT, robot_part=ROBOT_PART, log_entry=LOG_ENTRY, id=ID, fragment=FRAGMENT
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_list_organizations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            organizations = await client.list_organizations()
            assert organizations == ORGANIZATIONS

    @pytest.mark.asyncio
    async def test_create_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            new_location = await client.create_location(organization_id=ORGANIZATION_ID, name=NAME, parent_location_id=PARENT_LOCATION_ID)
            assert service.organization_id == ORGANIZATION_ID
            assert service.name == NAME
            assert service.parent_location_id == PARENT_LOCATION_ID
            assert new_location == LOCATION

    @pytest.mark.asyncio
    async def test_get_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            location = await client.get_location(location_id=LOCATION_ID)
            assert service.location_id == LOCATION_ID
            assert location == LOCATION

    @pytest.mark.asyncio
    async def test_update_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            updated_location = await client.update_location(location_id=LOCATION_ID, name=NAME, parent_location_id=PARENT_LOCATION_ID)
            assert service.location_id == LOCATION_ID
            assert service.name == NAME
            assert service.parent_location_id == PARENT_LOCATION_ID
            assert updated_location == LOCATION

    @pytest.mark.asyncio
    async def test_delete_location(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            await client.delete_location(location_id=LOCATION_ID)
            assert service.location_id == LOCATION_ID

    @pytest.mark.asyncio
    async def test_list_locations(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            locations = await client.list_locations(organization_id=ORGANIZATION_ID)
            assert service.organization_id == ORGANIZATION_ID
            assert locations == locations

    @pytest.mark.asyncio
    async def test_get_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            robot = await client.get_robot(robot_id=ROBOT_ID)
            assert service.robot_id == ROBOT_ID
            assert robot == ROBOT

    @pytest.mark.asyncio
    async def test_get_robot_parts(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            robot_parts = await client.get_robot_parts(robot_id=ROBOT_ID)
            assert service.robot_id == ROBOT_ID
            assert [robot_part.proto for robot_part in robot_parts] == ROBOT_PARTS

    @pytest.mark.asyncio
    async def test_get_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            robot_part = await client.get_robot_part(robot_part_id=ROBOT_PART_ID, dest=DEST, indent=INDENT)
            assert service.robot_part_id == ROBOT_PART_ID
            assert robot_part.proto == ROBOT_PART

    @pytest.mark.asyncio
    async def test_get_robot_part_logs(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            log_entries = await client.get_robot_part_logs(
                robot_part_id=ROBOT_PART_ID, filter=FILTER, dest=DEST, errors_only=ERRORS_ONLY, num_pages=NUM_PAGES
            )
            assert service.robot_part_id == ROBOT_PART_ID
            assert service.filter == FILTER
            assert service.errors_only == ERRORS_ONLY
            assert [log_entry.proto for log_entry in log_entries] == LOG_ENTRIES

    @pytest.mark.asyncio
    async def test_update_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            updated_robot_part = await client.update_robot_part(robot_part_id=ROBOT_PART_ID, name=NAME, robot_config=ROBOT_CONFIG)
            assert service.robot_part_id == ROBOT_PART_ID
            assert service.name == NAME
            assert struct_to_dict(service.robot_config) == ROBOT_CONFIG
            assert updated_robot_part.proto == ROBOT_PART

    @pytest.mark.asyncio
    async def test_new_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            new_robot_part_id = await client.new_robot_part(robot_id=ROBOT_ID, part_name=NAME)
            assert service.robot_id == ROBOT_ID
            assert service.part_name == NAME
            assert new_robot_part_id == ID

    @pytest.mark.asyncio
    async def test_delete_robot_part(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            await client.delete_robot_part(robot_part_id=ROBOT_PART_ID)
            assert service.robot_part_id == ROBOT_PART_ID

    @pytest.mark.asyncio
    async def test_mark_part_for_restart(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            await client.mark_part_for_restart(robot_part_id=ROBOT_PART_ID)
            assert service.robot_part_id == ROBOT_PART_ID

    @pytest.mark.asyncio
    async def test_list_robots(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            robots = await client.list_robots(location_id=LOCATION_ID)
            assert service.location_id == LOCATION_ID
            assert robots == [ROBOT]

    @pytest.mark.asyncio
    async def test_new_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            new_robot_id = await client.new_robot(name=NAME, location_id=LOCATION_ID)
            assert service.name == NAME
            assert service.location_id == LOCATION_ID
            assert new_robot_id == ID

    @pytest.mark.asyncio
    async def test_update_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            updated_robot = await client.update_robot(robot_id=ROBOT_ID, name=NAME, location_id=LOCATION_ID)
            assert service.robot_id == ROBOT_ID
            assert service.name == NAME
            assert service.location_id == LOCATION_ID
            assert updated_robot == ROBOT

    @pytest.mark.asyncio
    async def test_delete_robot(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            await client.delete_robot(robot_id=ROBOT_ID)
            assert service.robot_id == ROBOT_ID

    @pytest.mark.asyncio
    async def test_list_fragments(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            fragments = await client.list_fragments(organization_id=ORGANIZATION_ID, show_public=SHOW_PUBLIC)
            assert service.organization_id == ORGANIZATION_ID
            assert service.show_public == SHOW_PUBLIC
            assert [fragment.proto for fragment in fragments] == [FRAGMENT]

    @pytest.mark.asyncio
    async def test_get_fragment(self, service: MockApp):
        async with ChannelFor([service]) as channel:
            client = AppClient(channel, METADATA, LOCATION_ID)
            fragment = await client.get_fragment(fragment_id=FRAGMENT_ID)
            assert service.fragment_id == FRAGMENT_ID
            assert fragment.proto == FRAGMENT
