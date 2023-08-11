from typing import Any, Dict, List, Mapping, Optional

from grpclib import GRPCError, Status
from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.generic import GenericServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, container_to_list, dict_to_struct, struct_to_dict

from .generic import Generic
from . import Geometry


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
        if extra is None:
            extra = {}
        request = GetGeometriesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetGeometriesResponse = await self.client.GetGeometries(request, timeout=timeout)
        return container_to_list(response.geometries)


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
