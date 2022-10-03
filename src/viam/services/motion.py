from typing import Any, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import PoseInFrame, ResourceName, WorldState
from viam.proto.service.motion import (
    GetPoseRequest,
    GetPoseResponse,
    MotionServiceStub,
    MoveRequest,
    MoveResponse,
    MoveSingleComponentRequest,
    MoveSingleComponentResponse,
)
from viam.services.service_client_base import ServiceClientBase
from viam.utils import dict_to_struct


class MotionServiceClient(ServiceClientBase):
    """Motion is a Viam service that coordinates motion planning across all of the components in a given robot.

    The motion planning service calculates a valid path that avoids self collision by default. If additional constraints are supplied in the
    `world_state` message, the motion planning service will also account for those.
    """

    SERVICE_TYPE = "motion"

    def __init__(self, name: str, channel: Channel):
        self.client = MotionServiceStub(channel)
        self.name = name

    async def move(
        self,
        component_name: ResourceName,
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None,
        extra: Optional[Mapping[str, Any]] = None,
    ) -> bool:
        """Plan and execute a movement to move the component specified to its goal destination.

        Note: Frames designated with respect to components can also be used as the `component_name` when calling for a move. This
        technique allows for planning and moving the frame itself to the `destination`. To do so, simply override the `name` attribute
        for a given resource with the originating ReferenceFrame. Then pass in the updated resource into the `component_name`. Ex:
            resource = Arm.get_resource_name("arm")
            resource.name = "externalFrame"
            success = await MotionServiceClient.move(resource, ...)

        Args:
            component_name (ResourceName): Name of a component on a given robot.
            destination (PoseInFrame): The destination to move to, expressed as a `Pose` and the frame in which it was observed.
            world_state (WorldState): When supplied, the motion service will create a plan that obeys any contraints expressed in the
                WorldState message.

        Returns:
            bool: Whether the move was successful
        """
        if extra is None:
            extra = {}
        request = MoveRequest(
            name=self.name,
            destination=destination,
            component_name=component_name,
            world_state=world_state,
            extra=dict_to_struct(extra),
        )
        response: MoveResponse = await self.client.Move(request)
        return response.success

    async def move_single_component(
        self,
        component_name: ResourceName,
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None,
        extra: Optional[Mapping[str, Any]] = None,
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
        if extra is None:
            extra = {}
        request = MoveSingleComponentRequest(
            name=self.name,
            destination=destination,
            component_name=component_name,
            world_state=world_state,
            extra=dict_to_struct(extra),
        )
        response: MoveSingleComponentResponse = await self.client.MoveSingleComponent(request)
        return response.success

    async def get_pose(
        self,
        component_name: ResourceName,
        destination_frame: str,
        extra: Optional[Mapping[str, Any]] = None,
    ) -> PoseInFrame:
        """
        Get the Pose and observer frame for any given component on a robot.

        Args:
            component_name (ResourceName): Name of a component on a robot.
            destination_frame (str): Name of the desired reference frame.

        Returns:
            `Pose` (PoseInFrame): Pose of the given component and the frame in which it was observed.
        """
        if extra is None:
            extra = {}
        request = GetPoseRequest(
            name=self.name,
            component_name=component_name,
            destination_frame=destination_frame,
            extra=dict_to_struct(extra),
        )
        response: GetPoseResponse = await self.client.GetPose(request)
        return response.pose
