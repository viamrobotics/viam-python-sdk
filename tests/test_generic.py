import pytest
from grpclib.testing import ChannelFor
from viam.components.generic import GenericClient, GenericService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.component.generic import (DoRequest, DoResponse,
                                              GenericServiceStub)
from viam.utils import dict_to_struct, struct_to_dict

from .mocks.components import MockGeneric


class TestSensor:

    generic = MockGeneric(name='generic')

    @pytest.mark.asyncio
    async def test_do(self):
        result = await self.generic.do({'command': 'args'})
        assert result == {'command': True}


class TestService:

    name = 'generic'
    generic = MockGeneric(name=name)
    manager = ResourceManager([generic])
    service = GenericService(manager)

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericServiceStub(channel)
            request = DoRequest(name=self.name, command=dict_to_struct({'command': 'args'}))
            response: DoResponse = await client.Do(request)
            result = struct_to_dict(response.result)
            assert result == {'command': True}


class TestClient:

    name = 'generic'
    generic = MockGeneric(name=name)
    manager = ResourceManager([generic])
    service = GenericService(manager)

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GenericClient(self.name, channel)
            result = await client.do({'command': 'args'})
            assert result == {'command': True}
