from typing import Any, Dict, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry, PoseInFrame
from viam.proto.component.posetracker import GetPosesRequest, GetPosesResponse, PoseTrackerServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from .pose_tracker import PoseTracker


class PoseTrackerClient(PoseTracker, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the PoseTracker component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = PoseTrackerServiceStub(channel)
        super().__init__(name)

    async def get_poses(
        self,
        body_names: List[str],
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> Dict[str, PoseInFrame]:
        if extra is None:
            extra = {}
        request = GetPosesRequest(name=self.name, body_names=body_names, extra=dict_to_struct(extra))
        response: GetPosesResponse = await self.client.GetPoses(request, timeout=timeout)
        return {key: response.body_poses[key] for key in response.body_poses.keys()}

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
