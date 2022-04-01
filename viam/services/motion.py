from typing import Optional

from grpclib.client import Channel
from viam.proto.api.common import PoseInFrame, ResourceName, WorldState
from viam.proto.api.service.motion import (GetPoseRequest, GetPoseResponse,
                                           MotionServiceStub, MoveRequest,
                                           MoveResponse)


class MotionClient:

    def __init__(self, channel: Channel):
        self.client = MotionServiceStub(channel)

    async def move(
        self,
        resource_name: ResourceName,
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None
    ) -> bool:
        request = MoveRequest(
            destination=destination,
            component_name=resource_name,
            world_state=world_state
        )
        response: MoveResponse = await self.client.Move(request)
        return response.success

    async def get_pose(
        self,
        resource_name: ResourceName,
        destination_frame: str
    ) -> PoseInFrame:
        request = GetPoseRequest(
            component_name=resource_name,
            destination_frame=destination_frame
        )
        response: GetPoseResponse = await self.client.GetPose(request)
        return response.pose
