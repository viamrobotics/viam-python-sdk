from grpclib.testing import ChannelFor

from viam.components.generic import GenericClient, GenericRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.generic import GenericServiceStub
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import expected_grpc_timeout
from .mocks.services import MockGenericService


class TestGenericService:
    generic = MockGenericService(name="generic")

    async def test_do(self):
        result = await self.generic.do_command({"command": "args"}, timeout=1.82)
        assert result == {"command": True}
        assert self.generic.timeout == expected_grpc_timeout(1.82)


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "generic"
        cls.generic = MockGenericService(name=cls.name)
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


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "generic"
        cls.generic = MockGenericService(name=cls.name)
        cls.manager = ResourceManager([cls.generic])
        cls.service = GenericRPCService(cls.manager)

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericClient(self.name, channel)
            result = await client.do_command({"command": "args"}, timeout=7.86)
            assert result == {"command": True}
            assert self.generic.timeout == expected_grpc_timeout(7.86)
