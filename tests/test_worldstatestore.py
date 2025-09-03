import pytest
from grpclib.testing import ChannelFor

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.worldstatestore import (
    GetTransformRequest,
    GetTransformResponse,
    ListUUIDsRequest,
    ListUUIDsResponse,
    WorldStateStoreServiceStub,
)
from viam.resource.manager import ResourceManager
from viam.services.worldstatestore import WorldStateStoreClient
from viam.services.worldstatestore.service import WorldStateStoreService
from viam.utils import dict_to_struct, struct_to_dict

from .mocks.services import MockWorldStateStore

WORLDSTATESTORE_SERVICE_NAME = "worldstatestore1"


@pytest.fixture(scope="function")
def worldstatestore() -> MockWorldStateStore:
    return MockWorldStateStore(WORLDSTATESTORE_SERVICE_NAME)


@pytest.fixture(scope="function")
def service(worldstatestore: MockWorldStateStore) -> WorldStateStoreService:
    return WorldStateStoreService(ResourceManager([worldstatestore]))


class TestWorldStateStore:
    async def test_list_uuids(self, worldstatestore: MockWorldStateStore):
        extra = {"foo": "worldstatestore"}
        timeout = 1.0
        response = await worldstatestore.list_uuids(extra=extra, timeout=timeout)
        assert worldstatestore.extra == extra
        assert worldstatestore.timeout == timeout
        assert response == [b"uuid1", b"uuid2", b"uuid3"]

    async def test_get_transform(self, worldstatestore: MockWorldStateStore):
        uuid = b"test_uuid"
        extra = {"foo": "worldstatestore"}
        timeout = 2.0
        response = await worldstatestore.get_transform(uuid=uuid, extra=extra, timeout=timeout)
        assert worldstatestore.uuid == uuid
        assert worldstatestore.extra == extra
        assert worldstatestore.timeout == timeout
        assert response.uuid == uuid
        assert response.reference_frame == "test_frame"

    async def test_stream_transform_changes(self, worldstatestore: MockWorldStateStore):
        extra = {"foo": "worldstatestore"}
        timeout = 3.0
        changes = []
        async for change in worldstatestore.stream_transform_changes(extra=extra, timeout=timeout):
            changes.append(change)
        assert worldstatestore.extra == extra
        assert worldstatestore.timeout == timeout
        assert len(changes) == 2
        assert changes[0].change_type == 1  # TRANSFORM_CHANGE_TYPE_ADDED
        assert changes[1].change_type == 3  # TRANSFORM_CHANGE_TYPE_UPDATED

    async def test_do_command(self, worldstatestore: MockWorldStateStore):
        command = {"command": "args"}
        timeout = 4.0
        response = await worldstatestore.do_command(command, timeout=timeout)
        assert worldstatestore.timeout == timeout
        assert response["cmd"] == command


class TestService:
    async def test_list_uuids(self, worldstatestore: MockWorldStateStore, service: WorldStateStoreService):
        async with ChannelFor([service]) as channel:
            client = WorldStateStoreServiceStub(channel)
            extra = {"cmd": "worldstatestore"}
            request = ListUUIDsRequest(name=worldstatestore.name, extra=dict_to_struct(extra))
            response: ListUUIDsResponse = await client.ListUUIDs(request)
            assert worldstatestore.extra == extra
            assert list(response.uuids) == [b"uuid1", b"uuid2", b"uuid3"]

    async def test_get_transform(self, worldstatestore: MockWorldStateStore, service: WorldStateStoreService):
        async with ChannelFor([service]) as channel:
            client = WorldStateStoreServiceStub(channel)
            uuid = b"test_uuid"
            extra = {"cmd": "worldstatestore"}
            request = GetTransformRequest(name=worldstatestore.name, uuid=uuid, extra=dict_to_struct(extra))
            response: GetTransformResponse = await client.GetTransform(request)
            assert worldstatestore.uuid == uuid
            assert worldstatestore.extra == extra
            assert response.transform.uuid == uuid
            assert response.transform.reference_frame == "test_frame"

    async def test_stream_transform_changes(self, worldstatestore: MockWorldStateStore, service: WorldStateStoreService):
        async with ChannelFor([service]) as channel:
            client = WorldStateStoreClient(WORLDSTATESTORE_SERVICE_NAME, channel)
            extra = {"cmd": "worldstatestore"}
            changes = []
            async for change in client.stream_transform_changes(extra=extra):
                changes.append(change)
            assert worldstatestore.extra == extra
            assert len(changes) == 2
            assert changes[0].change_type == 1  # TRANSFORM_CHANGE_TYPE_ADDED
            assert changes[1].change_type == 3  # TRANSFORM_CHANGE_TYPE_UPDATED

    async def test_do_command(self, worldstatestore: MockWorldStateStore, service: WorldStateStoreService):
        async with ChannelFor([service]) as channel:
            client = WorldStateStoreServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=worldstatestore.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            assert struct_to_dict(response.result)["cmd"] == command


class TestClient:
    async def test_list_uuids(self, worldstatestore: MockWorldStateStore, service: WorldStateStoreService):
        async with ChannelFor([service]) as channel:
            client = WorldStateStoreClient(WORLDSTATESTORE_SERVICE_NAME, channel)
            extra = {"foo": "worldstatestore"}
            response = await client.list_uuids(extra=extra)
            assert response == [b"uuid1", b"uuid2", b"uuid3"]
            assert worldstatestore.extra == extra

    async def test_get_transform(self, worldstatestore: MockWorldStateStore, service: WorldStateStoreService):
        async with ChannelFor([service]) as channel:
            client = WorldStateStoreClient(WORLDSTATESTORE_SERVICE_NAME, channel)
            uuid = b"test_uuid"
            extra = {"foo": "worldstatestore"}
            response = await client.get_transform(uuid=uuid, extra=extra)
            assert response.uuid == uuid
            assert response.reference_frame == "test_frame"
            assert worldstatestore.uuid == uuid
            assert worldstatestore.extra == extra

    async def test_stream_transform_changes(self, worldstatestore: MockWorldStateStore, service: WorldStateStoreService):
        async with ChannelFor([service]) as channel:
            client = WorldStateStoreClient(WORLDSTATESTORE_SERVICE_NAME, channel)
            extra = {"foo": "worldstatestore"}
            changes = []
            async for change in client.stream_transform_changes(extra=extra):
                changes.append(change)
            assert len(changes) == 2
            assert changes[0].change_type == 1  # TRANSFORM_CHANGE_TYPE_ADDED
            assert changes[1].change_type == 3  # TRANSFORM_CHANGE_TYPE_UPDATED
            assert worldstatestore.extra == extra

    async def test_do_command(self, worldstatestore: MockWorldStateStore, service: WorldStateStoreService):
        async with ChannelFor([service]) as channel:
            client = WorldStateStoreClient(WORLDSTATESTORE_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response["cmd"] == command
