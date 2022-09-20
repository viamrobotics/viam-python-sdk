from typing import Any, Dict
from grpclib import GRPCError, Status
from grpclib.client import Channel
from viam.proto.component.generic import GenericServiceStub, DoCommandRequest, DoCommandResponse
from viam.utils import dict_to_struct, struct_to_dict

from .generic import Generic


class GenericClient(Generic):
    """
    gRPC client for the Generic component.
    """

    def __init__(self, name: str, channel: Channel):
        self.client = GenericServiceStub(channel)
        super().__init__(name)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        try:
            response: DoCommandResponse = await self.client.DoCommand(request)
        except GRPCError as e:
            if e.status == Status.UNIMPLEMENTED:
                raise NotImplementedError()
            raise e

        return struct_to_dict(response.result)


async def do_command(channel: Channel, name: str, command: Dict[str, Any]) -> Dict[str, Any]:
    """Convenience method to allow component clients to execute `do_command` functions

    Args:
        channel (Channel): A gRPC channel
        name (str): The name of the component
        command (Dict[str, Any]): The command to execute

    Returns:
        Dict[str, Any]: The result of the executed command
    """
    client = GenericClient(name, channel)
    return await client.do_command(command)
