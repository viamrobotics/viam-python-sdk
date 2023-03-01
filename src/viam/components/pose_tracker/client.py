from typing import Any, SupportsBytes, Dict, SupportsFloat, SupportsInt, List, Mapping, Optional, Union

from grpclib.client import Channel

from viam.proto.common import PoseInFrame, DoCommandRequest, DoCommandResponse
from viam.proto.component.posetracker import (
    GetPosesRequest,
    GetPosesResponse,
    PoseTrackerServiceStub,
)
from viam.utils import dict_to_struct, struct_to_dict

from .pose_tracker import PoseTracker


DoCommandTypes = Union[bool, SupportsBytes, SupportsFloat, SupportsInt, List, Mapping, str, None]


class PoseTrackerClient(PoseTracker):
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
    ) -> Dict[str, PoseInFrame]:
        if extra is None:
            extra = {}
        request = GetPosesRequest(name=self.name, body_names=body_names, extra=dict_to_struct(extra))
        response: GetPosesResponse = await self.client.GetPoses(request, timeout=timeout)
        return {key: response.body_poses[key] for key in response.body_poses.keys()}

    async def do_command(self, command: Dict[str, DoCommandTypes], *, timeout: Optional[float] = None) -> Dict[str, DoCommandTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
