from typing import Any, List, Mapping, Optional, Sequence

from grpclib.client import Channel

from viam.proto.common import PoseInFrame, Transform
from viam.proto.robot import (
    FrameSystemConfig,
    FrameSystemConfigRequest,
    FrameSystemConfigResponse,
    GetPoseRequest,
    GetPoseResponse,
    RobotServiceStub,
    TransformPCDRequest,
    TransformPCDResponse,
    TransformPoseRequest,
    TransformPoseResponse,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import dict_to_struct

from .framesystem import FrameSystem


class FrameSystemClient(FrameSystem, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the machine's frame system.

    The frame system RPCs are served by viam-server on the robot service, so this client talks to ``RobotService`` over the given channel
    rather than to a service registered under its own name.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = RobotServiceStub(channel)
        super().__init__(name)

    async def get_frame_system_config(
        self,
        additional_transforms: Optional[Sequence[Transform]] = None,
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> List[FrameSystemConfig]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = FrameSystemConfigRequest(supplemental_transforms=additional_transforms)
        response: FrameSystemConfigResponse = await self.client.FrameSystemConfig(request, timeout=timeout, metadata=md)
        return list(response.frame_system_configs)

    async def get_pose(
        self,
        component_name: str,
        destination_frame: str = "",
        supplemental_transforms: Optional[Sequence[Transform]] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> PoseInFrame:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPoseRequest(
            component_name=component_name,
            destination_frame=destination_frame,
            supplemental_transforms=supplemental_transforms,
            extra=dict_to_struct(extra),
        )
        response: GetPoseResponse = await self.client.GetPose(request, timeout=timeout, metadata=md)
        return response.pose

    async def transform_pose(
        self,
        query: PoseInFrame,
        destination: str,
        additional_transforms: Optional[Sequence[Transform]] = None,
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> PoseInFrame:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = TransformPoseRequest(source=query, destination=destination, supplemental_transforms=additional_transforms)
        response: TransformPoseResponse = await self.client.TransformPose(request, timeout=timeout, metadata=md)
        return response.pose

    async def transform_pcd(
        self,
        point_cloud_pcd: bytes,
        source: str,
        destination: str,
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> bytes:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = TransformPCDRequest(point_cloud_pcd=point_cloud_pcd, source=source, destination=destination)
        response: TransformPCDResponse = await self.client.TransformPCD(request, timeout=timeout, metadata=md)
        return response.point_cloud_pcd
