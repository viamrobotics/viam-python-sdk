from typing import Any, Dict, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry
from viam.proto.component.gripper import (
    GrabRequest,
    GrabResponse,
    GripperServiceStub,
    IsMovingRequest,
    IsMovingResponse,
    OpenRequest,
    StopRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from .gripper import Gripper


class GripperClient(Gripper, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Gripper component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = GripperServiceStub(channel)
        super().__init__(name)

    async def open(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ):
        if extra is None:
            extra = {}
        request = OpenRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Open(request, timeout=timeout)

    async def grab(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> bool:
        if extra is None:
            extra = {}
        request = GrabRequest(name=self.name, extra=dict_to_struct(extra))
        response: GrabResponse = await self.client.Grab(request, timeout=timeout)
        return response.success

    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ):
        if extra is None:
            extra = {}
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request, timeout=timeout)

    async def is_moving(self, *, timeout: Optional[float] = None) -> bool:
        request = IsMovingRequest(name=self.name)
        response: IsMovingResponse = await self.client.IsMoving(request, timeout=timeout)
        return response.is_moving

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **__,
    ) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        return await get_geometries(self.client, self.name, extra, timeout)
