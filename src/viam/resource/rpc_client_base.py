from typing import Any, Protocol, runtime_checkable

from grpclib.client import Channel

from viam.rpc.types import RPCServiceStubBase


@runtime_checkable
class ResourceRPCClientBase(Protocol):
    """
    Base RPC client for a resource.
    Resource RPC clients must inherit from this class
    """

    channel: Channel
    client: Any


class ReconfigurableResourceRPCClientBase(ResourceRPCClientBase):
    """A base RPC client that can reset its channel.

    Useful if connection is lost and then regained.
    """

    def reset_channel(self, channel: Channel):
        """Called when the RPC channel was reset. Passes in the new channel.

        Args:
            channel (Channel): The new RPC Channel
        """
        self.channel = channel
        if isinstance(self.client, RPCServiceStubBase):
            self.client = self.client.__class__(channel)
