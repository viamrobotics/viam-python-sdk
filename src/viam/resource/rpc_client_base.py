from random import choice
from string import ascii_lowercase
from typing import Any, Dict, Protocol, runtime_checkable

from grpclib.client import Channel

from viam.rpc.types import RPCServiceStubBase


@runtime_checkable
class ResourceRPCClientBase(Protocol):
    """
    Base RPC client for a resource.
    Resource RPC clients must inherit from this class
    """

    class Metadata:
        metadata: Dict[str, str] = {}

        def enable_debug_logging(self, key: str = ""):
            """Enables server-side debug logging for resource methods.

            Args:
                key (str): The key to associate debug logs with. If not provided, will default to a randomly generated string value.
            """
            if key == "":
                key = "".join(choice(ascii_lowercase) for i in range(6))
            self.metadata["dtname"] = key

        def disable_debug_logging(self):
            """Disables server-side debug logging for resource methods."""
            del self.metadata["dtname"]

        def add_metadata(self, key: str, value: str):
            """Adds a key-value pair to the metadata"""
            self.metadata[key] = value

        def delete_metadata(self, key: str):
            """Removes a key-value pair from the metadata by key"""
            del self.metadata[key]

        @property
        def proto(self):
            """Returns metadata in a gRPC-appropriate form"""
            return [(k, v) for k, v in self.metadata.items()]

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
