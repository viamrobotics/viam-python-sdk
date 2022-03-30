from typing import List

from grpclib.client import Channel
from viam.components import ComponentType
from viam.proto.api.common import (GeometriesInFrame, PoseInFrame,
                                   ResourceName, WorldState)
from viam.proto.api.service.motion import (GetPoseRequest, GetPoseResponse,
                                           MotionServiceStub, MoveRequest,
                                           MoveResponse)


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
            component_name=ResourceName(
                namespace='rdk',
                type='component',
                subtype=component_type.value,
                name=component_name
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
            component_name=ResourceName(
                namespace='rdk',
                type='component',
                subtype=component_type.value,
                name=component_name
            ),
            destination_frame=destination_frame
        )
        response: GetPoseResponse = await self.client.GetPose(request)
        return response.pose
