import pytest
from grpclib.client import Channel
from grpclib.testing import ChannelFor

from viam.resource.registry import Registry
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK
from viam.rpc.dial import ViamChannel

from .mocks import components  # noqa: F401


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
        for api, registration in Registry.REGISTERED_APIS().items():
            if api.namespace == RESOURCE_NAMESPACE_RDK:
                client = registration.create_rpc_client("client", channel)
                assert isinstance(client, ReconfigurableResourceRPCClientBase)


async def test_viam_channel_closing():
    def release():
        nonlocal did_release
        did_release = True

    # Non-error case
    did_release = False
    channel = await ChannelFor([]).__aenter__()
    v_channel = ViamChannel(channel=channel, release=release)
    assert v_channel._closed is False
    assert did_release is False
    v_channel.close()
    assert v_channel._closed is True
    assert did_release is True
    await channel.__aexit__(None, None, None)

    # Error case
    def close():
        raise Exception("FAILURE")

    did_release = False
    channel = await ChannelFor([]).__aenter__()
    old_close = channel.close
    channel.close = close
    v_channel = ViamChannel(channel=channel, release=release)
    assert v_channel._closed is False
    assert did_release is False
    with pytest.raises(Exception):
        v_channel.close()
    assert v_channel._closed is True
    assert did_release is True
    channel.close = old_close
    await channel.__aexit__(None, None, None)
