from typing import List

from grpclib.client import Channel
from viam.components import ComponentType
from viam.proto.api.common import GeometriesInFrame, PoseInFrame, WorldState
from viam.proto.api.service.motion import (GetPoseRequest, GetPoseResponse,
                                           MotionServiceStub, MoveRequest,
                                           MoveResponse)
from viam.utils import resource_name_for_component_name_type


class MotionClient:

    def __init__(self, channel: Channel):
        self.client = MotionServiceStub(channel)

    async def move(
        self,
        component_type: ComponentType,
        component_name: str,
        destination: PoseInFrame,
        obstacles: List[GeometriesInFrame]
    ) -> bool:
        request = MoveRequest(
            destination=destination,
            component_name=resource_name_for_component_name_type(
                component_name,
                component_type
            ),
            world_state=WorldState(obstacles=obstacles)
        )
        response: MoveResponse = await self.client.Move(request)
        return response.success

    async def get_pose(
        self,
        component_type: ComponentType,
        component_name: str,
        destination_frame: str
    ) -> PoseInFrame:
        request = GetPoseRequest(
            component_name=resource_name_for_component_name_type(
                component_name,
                component_type
            ),
            destination_frame=destination_frame
        )
        response: GetPoseResponse = await self.client.GetPose(request)
        return response.pose
