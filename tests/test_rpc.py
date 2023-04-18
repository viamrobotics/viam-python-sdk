import pytest
from grpclib.client import Channel
from grpclib.testing import ChannelFor

from viam.resource.registry import Registry
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK

from .mocks import components  # noqa: F401


@pytest.mark.asyncio
async def test_reset_channel():
    class TestStub:
        def __init__(self, channel: Channel) -> None:
            self.channel = channel

    class TestClient(ReconfigurableResourceRPCClientBase):
        def __init__(self, channel: Channel) -> None:
            self.channel = channel
            self.client = TestStub(channel)

    async with ChannelFor([]) as channel:
        client = TestClient(channel)
        assert client.channel == channel
        async with ChannelFor([]) as channel2:
            client.reset_channel(channel2)
            assert client.channel == channel2
            assert channel != channel2


async def test_builtin_clients_are_reconfigurable():
    async with ChannelFor([]) as channel:
        for subtype, registration in Registry.REGISTERED_SUBTYPES().items():
            if subtype.namespace == RESOURCE_NAMESPACE_RDK:
                client = registration.create_rpc_client("client", channel)
                assert isinstance(client, ReconfigurableResourceRPCClientBase)
