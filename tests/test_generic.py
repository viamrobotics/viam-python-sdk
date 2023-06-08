import pytest
from grpclib import GRPCError
from grpclib.testing import ChannelFor

from viam.components.generic import GenericClient, GenericRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest
from viam.proto.component.generic import GenericServiceStub
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockGeneric


class TestGeneric:
    generic = MockGeneric(name="generic")

    @pytest.mark.asyncio
    async def test_do(self):
        result = await self.generic.do_command({"command": "args"}, timeout=1.82)
        assert result == {"command": True}
        assert self.generic.timeout == loose_approx(1.82)


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "generic"
        cls.generic = MockGeneric(name=cls.name)
        cls.manager = ResourceManager([cls.generic])
        cls.service = GenericRPCService(cls.manager)

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericServiceStub(channel)
            request = DoCommandRequest(name=self.name, command=dict_to_struct({"command": "args"}))
            response: DoCommandResponse = await client.DoCommand(request, timeout=4.4)
            result = struct_to_dict(response.result)
            assert result == {"command": True}
            assert self.generic.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericServiceStub(channel)
            request = GetGeometriesRequest()
            with pytest.raises(GRPCError, match=r"Method [a-zA-Z]+ not implemented"):
                await client.GetGeometries(request)


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "generic"
        cls.generic = MockGeneric(name=cls.name)
        cls.manager = ResourceManager([cls.generic])
        cls.service = GenericRPCService(cls.manager)

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericClient(self.name, channel)
            result = await client.do_command({"command": "args"}, timeout=7.86)
            assert result == {"command": True}
            assert self.generic.timeout == loose_approx(7.86)
