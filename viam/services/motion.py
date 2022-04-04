from typing import Optional

from grpclib.client import Channel
from viam.proto.api.common import PoseInFrame, ResourceName, WorldState
from viam.proto.api.service.motion import (GetPoseRequest, GetPoseResponse,
                                           MotionServiceStub, MoveRequest,
                                           MoveResponse)


class MotionClient:
    """ Motion is a Viam service that coordinates motion planning across all of the components in a given robot.

    The motion planning service calculates a valid path that avoids self collision by default. If additional constraints are supplied in the
    `world_state` message, the motion planning service will also account for those.
     """

    def __init__(self, channel: Channel):
        self.client = MotionServiceStub(channel)

    async def move(
        self,
        resource_name: ResourceName,
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None
    ) -> bool:
        """
        Move a component on the robot to a given destination, obey any constraints (transforms or obstacles) if supplied in WorldState.

        Args:
            resource_name (ResourceName): Name of a component on a given robot.
            destination (PoseInFrame): The destination to move to, expressed as a `Pose` and the frame in which it was observed.
            world_state (WorldState): When supplied, the motion service will create a plan that obeys any contraints expressed in the
                WorldState message.
        """
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
        """
        Get the Pose and observer frame for any given component on a robot.

        Args:
            component_name(ResourceName): Name of a component on a robot.
            destination_frame(str):

        Returns:
            Pose(PoseInFrame): Pose of the given component and the frame in which it was observed.
        """
        request = GetPoseRequest(
            component_name=resource_name,
            destination_frame=destination_frame
        )
        response: GetPoseResponse = await self.client.GetPose(request)
        return response.pose
