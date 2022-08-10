from typing import Optional

from grpclib.client import Channel
from viam.proto.api.common import PoseInFrame, ResourceName, WorldState
from viam.proto.api.service.motion import (
    GetPoseRequest,
    GetPoseResponse,
    MotionServiceStub,
    MoveSingleComponentRequest,
    MoveSingleComponentResponse,
    PlanAndMoveRequest,
    PlanAndMoveResponse,
)


class MotionClient:
    """Motion is a Viam service that coordinates motion planning across all of the components in a given robot.

    The motion planning service calculates a valid path that avoids self collision by default. If additional constraints are supplied in the
    `world_state` message, the motion planning service will also account for those.
    """

    def __init__(self, channel: Channel):
        self.client = MotionServiceStub(channel)

    async def plan_and_move(self, component_name: ResourceName, destination: PoseInFrame, world_state: Optional[WorldState] = None) -> bool:
        """Plan and execute a movement to move the component specified to its goal destination.


        Args:
            component_name (ResourceName): Name of a component on a given robot.
            destination (PoseInFrame): The destination to move to, expressed as a `Pose` and the frame in which it was observed.
            world_state (WorldState): When supplied, the motion service will create a plan that obeys any contraints expressed in the
                WorldState message.

        Returns:
            bool: Whether the move was successful
        """
        request = PlanAndMoveRequest(destination=destination, component_name=component_name, world_state=world_state)
        response: PlanAndMoveResponse = await self.client.PlanAndMove(request)
        return response.success

    async def move_single_component(
        self, component_name: ResourceName, destination: PoseInFrame, world_state: Optional[WorldState] = None
    ) -> bool:
        """
        This function will pass through a move command to a component with a `move_to_position` method that takes a `Pose`. `Arm`s are the
        only component that support this. This method will transform the destination pose, given in an arbitrary frame, into the pose of the
        arm. The arm will then move its most distal link to that pose. If you instead wish to move any other component than the arm end to
        that pose, then you must manually adjust the given destination by the transform from the arm end to the intended component.

        Args:
            component_name (ResourceName): Name of a component on a given robot.
            destination (PoseInFrame): The destination to move to, expressed as a `Pose` and the frame in which it was observed.
            world_state (WorldState): When supplied, the motion service will create a plan that obeys any contraints expressed in the
                WorldState message.

        Returns:
            bool: Whether the move was successful
        """
        request = MoveSingleComponentRequest(destination=destination, component_name=component_name, world_state=world_state)
        response: MoveSingleComponentResponse = await self.client.MoveSingleComponent(request)
        return response.success

    async def get_pose(self, component_name: ResourceName, destination_frame: str) -> PoseInFrame:
        """
        Get the Pose and observer frame for any given component on a robot.

        Args:
            component_name (ResourceName): Name of a component on a robot.
            destination_frame (str): Name of the desired reference frame.

        Returns:
            `Pose` (PoseInFrame): Pose of the given component and the frame in which it was observed.
        """
        request = GetPoseRequest(component_name=component_name, destination_frame=destination_frame)
        response: GetPoseResponse = await self.client.GetPose(request)
        return response.pose
