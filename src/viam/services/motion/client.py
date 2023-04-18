from typing import Any, Final, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, PoseInFrame, ResourceName, Transform, WorldState
from viam.proto.service.motion import (
    Constraints,
    GetPoseRequest,
    GetPoseResponse,
    MotionServiceStub,
    MoveRequest,
    MoveResponse,
    MoveSingleComponentRequest,
    MoveSingleComponentResponse,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_client_base import ServiceClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict


class MotionServiceClient(ServiceClientBase, ReconfigurableResourceRPCClientBase):
    """Motion is a Viam service that coordinates motion planning across all of the components in a given robot.

    The motion planning service calculates a valid path that avoids self collision by default. If additional constraints are supplied in the
    ``world_state`` message, the motion planning service will also account for those.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "motion")

    def __init__(self, name: str, channel: Channel):
        super().__init__(name, channel)
        self.client = MotionServiceStub(channel)

    async def move(
        self,
        component_name: ResourceName,
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None,
        constraints: Optional[Constraints] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> bool:
        """Plan and execute a movement to move the component specified to its goal destination.

        Note: Frames designated with respect to components can also be used as the ``component_name`` when calling for a move. This
        technique allows for planning and moving the frame itself to the ``destination``. To do so, simply create a resource name with
        originating ReferenceFrame's name. Then pass in the resource name into ``component_name``. Ex::

            resource_name = Arm.get_resource_name("externalFrame")
            success = await MotionServiceClient.move(resource_name, ...)

        Args:
            component_name (ResourceName): Name of a component on a given robot.
            destination (PoseInFrame): The destination to move to, expressed as a ``Pose`` and the frame in which it was observed.
            world_state (WorldState): When supplied, the motion service will create a plan that obeys any contraints expressed in the
                WorldState message.
            constraints (Constraints): When supplied, the motion service will create a plan that obeys any specified constraints

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
            constraints=constraints,
            extra=dict_to_struct(extra),
        )
        response: MoveResponse = await self.client.Move(request, timeout=timeout)
        return response.success

    async def move_single_component(
        self,
        component_name: ResourceName,
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> bool:
        """
        This function will pass through a move command to a component with a ``move_to_position`` method that takes a ``Pose``. ``Arm`` is
        the only component that support this. This method will transform the destination pose, given in an arbitrary frame, into the pose of
        the arm. The arm will then move its most distal link to that pose. If you instead wish to move any other component than the arm end
        to that pose, then you must manually adjust the given destination by the transform from the arm end to the intended component.

        Args:
            component_name (ResourceName): Name of a component on a given robot.
            destination (PoseInFrame): The destination to move to, expressed as a ``Pose`` and the frame in which it was observed.
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
        response: MoveSingleComponentResponse = await self.client.MoveSingleComponent(request, timeout=timeout)
        return response.success

    async def get_pose(
        self,
        component_name: ResourceName,
        destination_frame: str,
        supplemental_transforms: Optional[List[Transform]] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> PoseInFrame:
        """
        Get the Pose and observer frame for any given component on a robot. A ``component_name`` can be created like this::

            component_name = Arm.get_resource_name("arm")

        Note that the example uses the ``Arm`` class, but any component class that inherits from ``ComponentBase`` will work
        (``Base``, ``Gripper``, etc).


        Args:
            component_name (ResourceName): Name of a component on a robot.
            destination_frame (str): Name of the desired reference frame.
            supplemental_transforms (Optional[List[Transforms]]): Transforms used to augment the robot's frame while calculating pose.

        Returns:
            ``Pose`` (PoseInFrame): Pose of the given component and the frame in which it was observed.
        """
        if supplemental_transforms is None:
            supplemental_transforms = []
        if extra is None:
            extra = {}
        request = GetPoseRequest(
            name=self.name,
            component_name=component_name,
            destination_frame=destination_frame,
            supplemental_transforms=supplemental_transforms,
            extra=dict_to_struct(extra),
        )
        response: GetPoseResponse = await self.client.GetPose(request, timeout=timeout)
        return response.pose

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        """Send/receive arbitrary commands

        Args:
            command (Dict[str, ValueTypes]): The command to execute

        Returns:
            Dict[str, ValueTypes]: Result of the executed command
        """
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
