from typing import Any, Dict, List, Mapping, Optional

from grpclib import GRPCError, Status
from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry
from viam.proto.component.generic import GenericServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from .generic import Generic


class GenericClient(Generic, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Generic component.
    """

    def __init__(self, name: str, channel: Channel):
        self.client = GenericServiceStub(channel)
        super().__init__(name)

    async def do_command(self, command: Mapping[str, Any], *, timeout: Optional[float] = None) -> Mapping[str, Any]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        try:
            response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        except GRPCError as e:
            if e.status == Status.UNIMPLEMENTED:
                raise NotImplementedError()
            raise e

        return struct_to_dict(response.result)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        return await get_geometries(self.client, self.name, extra, timeout)


async def do_command(
    channel: Channel, name: str, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None
) -> Mapping[str, ValueTypes]:
    """Convenience method to allow component clients to execute ``do_command`` functions

    Args:
        channel (Channel): A gRPC channel
        name (str): The name of the component
        command (Dict[str, Any]): The command to execute

    Returns:
        Dict[str, Any]: The result of the executed command
    """
    client = GenericClient(name, channel)
    return await client.do_command(command, timeout=timeout)
