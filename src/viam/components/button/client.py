from typing import Any, Mapping, Optional

from grpclib.client import Channel

from viam.gen.component.button.v1.button_pb2 import PushRequest
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
)
from viam.proto.component.button import ButtonServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import (
    ValueTypes,
    dict_to_struct,
    struct_to_dict,
)

from .button import Button


class ButtonClient(Button, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for Button component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = ButtonServiceStub(channel)
        super().__init__(name)

    async def push(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> None:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = PushRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Push(request, timeout=timeout, metadata=md)

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
