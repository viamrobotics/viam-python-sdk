from grpclib.testing import ChannelFor

from viam.components.generic import GenericClient, GenericRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.generic import GenericServiceStub
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import expected_grpc_timeout
from .mocks.components import GEOMETRIES, MockGenericComponent


class TestGenericComponent:
    generic = MockGenericComponent(name="generic")

    async def test_do(self):
        result = await self.generic.do_command({"command": "args"}, timeout=1.82)
        assert result == {"command": True}
        assert self.generic.timeout == expected_grpc_timeout(1.82)

    async def test_get_geometries(self):
        geometries = await self.generic.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "generic"
        cls.generic = MockGenericComponent(name=cls.name)
        cls.manager = ResourceManager([cls.generic])
        cls.service = GenericRPCService(cls.manager)

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericServiceStub(channel)
            request = DoCommandRequest(name=self.name, command=dict_to_struct({"command": "args"}))
            response: DoCommandResponse = await client.DoCommand(request, timeout=4.4)
            result = struct_to_dict(response.result)
            assert result == {"command": True}
            assert self.generic.timeout == expected_grpc_timeout(4.4)

    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericServiceStub(channel)
            request = GetGeometriesRequest(name=self.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "generic"
        cls.generic = MockGenericComponent(name=cls.name)
        cls.manager = ResourceManager([cls.generic])
        cls.service = GenericRPCService(cls.manager)

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericClient(self.name, channel)
            result = await client.do_command({"command": "args"}, timeout=7.86)
            assert result == {"command": True}
            assert self.generic.timeout == expected_grpc_timeout(7.86)

    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericClient(self.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES
