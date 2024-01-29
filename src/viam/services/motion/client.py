from typing import Any, Final, List, Mapping, Optional, Sequence

from grpclib.client import Channel

from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GeoObstacle,
    GeoPoint,
    Pose,
    PoseInFrame,
    ResourceName,
    Transform,
    WorldState,
)
from viam.proto.service.motion import (
    Constraints,
    GetPlanRequest,
    GetPlanResponse,
    GetPoseRequest,
    GetPoseResponse,
    ListPlanStatusesRequest,
    ListPlanStatusesResponse,
    MotionConfiguration,
    MotionServiceStub,
    MoveOnGlobeRequest,
    MoveOnGlobeResponse,
    MoveOnMapRequest,
    MoveOnMapResponse,
    MoveRequest,
    MoveResponse,
    StopPlanRequest,
    StopPlanResponse,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_client_base import ServiceClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict


class MotionClient(ServiceClientBase, ReconfigurableResourceRPCClientBase):
    """Motion is a Viam service that coordinates motion planning across all of the components in a given robot.

    The motion planning service calculates a valid path that avoids self collision by default. If additional constraints are supplied in the
    ``world_state`` message, the motion planning service will also account for those.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "motion"
    )
    client: MotionServiceStub

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
            component_name (viam.proto.common.ResourceName): Name of a component on a given robot.
            destination (viam.proto.common.PoseInFrame): The destination to move to, expressed as a ``Pose`` and the frame in which it was
                observed.
            world_state (viam.proto.common.WorldState): When supplied, the motion service will create a plan that obeys any contraints
                expressed in the WorldState message.
            constraints (viam.proto.service.motion.Constraints): When supplied, the motion service will create a plan that obeys any
                specified constraints

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

    async def move_on_globe(
        self,
        component_name: ResourceName,
        destination: GeoPoint,
        movement_sensor_name: ResourceName,
        obstacles: Optional[Sequence[GeoObstacle]] = None,
        heading: Optional[float] = None,
        configuration: Optional[MotionConfiguration] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> str:
        """Move a component to a specific latitude and longitude, using a ``MovementSensor`` to check the location.

        ``move_on_globe()`` is non blocking, meaning the motion service will move the component to the destination
        GPS point after ``move_on_globe()`` returns.

        Each successful ``move_on_globe()`` call retuns a unique ExectionID which you can use to identify all plans
        generated durring the ``move_on_globe()`` call.

        You can monitor the progress of the ``move_on_globe()`` call by querying ``get_plan()`` and ``list_plan_statuses()``.

        Args:
            component_name (ResourceName): The ResourceName of the base to move.
            destination (GeoPoint): The location of the component’s destination, represented in geographic notation as a
            GeoPoint (lat, lng).
            movement_sensor_name (ResourceName): The ResourceName of the movement sensor that you want to use to check
            the machine’s location.
            obstacles (Optional[Sequence[GeoObstacle]]): Obstacles to consider when planning the motion of the component,
            with each represented as a GeoObstacle.
                - Default: None
            heading (Optional[float]): The compass heading, in degrees, that the machine’s movement sensor should report
            at the destination point.
                Range: [0-360) 0: North, 90: East, 180: South, 270: West
                Default: None
            configuration (Optional[MotionConfiguration]): The configuration you want to set across this machine for this
            motion service. This parameter and each of its fields are optional.
                obstacle_detectors (Iterable[ObstacleDetector]): The names of each vision service and camera resource pair
                you want to use for transient obstacle avoidance.
                position_polling_frequency_hz (float): The frequency in hz to poll the position of the machine.
                obstacle_polling_frequency_hz (float): The frequency in hz to poll the vision service for new obstacles.
                plan_deviation_m (float): The distance in meters that the machine can deviate from the motion plan.
                linear_m_per_sec (float): Linear velocity this machine should target when moving.
                angular_degs_per_sec (float): Angular velocity this machine should target when turning.
            extra (Optional[Dict[str, Any]]): Extra options to pass to the underlying RPC call.
            timeout (Optional[float]): An option to set how long to wait (in seconds) before calling a time-out and closing
            the underlying RPC call.


        Returns:
            str: ExecutionID of the ``move_on_globe()`` call, which can be used to track execution progress.
        """
        if extra is None:
            extra = {}
        request = MoveOnGlobeRequest(
            name=self.name,
            component_name=component_name,
            destination=destination,
            movement_sensor_name=movement_sensor_name,
            obstacles=obstacles,
            heading=heading,
            motion_configuration=configuration,
            extra=dict_to_struct(extra),
        )
        response: MoveOnGlobeResponse = await self.client.MoveOnGlobe(request, timeout=timeout)
        return response.execution_id

    async def move_on_map(
        self,
        component_name: ResourceName,
        destination: Pose,
        slam_service_name: ResourceName,
        configuration: Optional[MotionConfiguration] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> str:
        """
        Move a component to a specific pose, using a ``SlamService`` for the SLAM map, using a ``SLAM Service`` to check the location.

        ``move_on_map()`` is non blocking, meaning the motion service will move the component to the destination
        Pose point after ``move_on_map()`` returns.

        Each successful ``move_on_map()`` call retuns a unique ExectionID which you can use to identify all plans
        generated durring the ``move_on_map()`` call.

        You can monitor the progress of the ``move_on_map()`` call by querying ``get_plan()`` and ``list_plan_statuses()``.

        Args:
            component_name (ResourceName): The ResourceName of the base to move.
            destination (Pose): The destination, which can be any Pose with respect to the SLAM map’s origin.
            slam_service_name (ResourceName): The ResourceName of the SLAM service from which the SLAM map is requested.
            configuration (Optional[MotionConfiguration]): The configuration you want to set across this machine for this motion service.
            This parameter and each of its fields are optional.
                obstacle_detectors (Iterable[ObstacleDetector]): The names of each vision service and camera resource pair you want to use
                for transient obstacle avoidance.
                position_polling_frequency_hz (float): The frequency in hz to poll the position of the machine.
                obstacle_polling_frequency_hz (float): The frequency in hz to poll the vision service for new obstacles.
                plan_deviation_m (float): The distance in meters that the machine can deviate from the motion plan.
                linear_m_per_sec (float): Linear velocity this machine should target when moving.
                angular_degs_per_sec (float): Angular velocity this machine should target when turning.
            extra (Optional[Dict[str, Any]]): Extra options to pass to the underlying RPC call.
            timeout (Optional[float]): An option to set how long to wait (in seconds) before calling a time-out and closing the underlying
            RPC call.

        Returns:
            str: ExecutionID of the ``move_on_map()`` call, which can be used to track execution progress.
        """
        if extra is None:
            extra = {}
        request = MoveOnMapRequest(
            name=self.name,
            destination=destination,
            component_name=component_name,
            slam_service_name=slam_service_name,
            motion_configuration=configuration,
            extra=dict_to_struct(extra),
        )
        response: MoveOnMapResponse = await self.client.MoveOnMap(request, timeout=timeout)
        return response.execution_id

    async def stop_plan(
        self,
        component_name: ResourceName,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ):
        """Stop a component being moved by an in progress ``move_on_globe()`` or ``move_on_map()`` call.

        Args:
            component_name (ResourceName): The component to stop

        Returns:
            None
        """
        if extra is None:
            extra = {}

        request = StopPlanRequest(
            name=self.name,
            component_name=component_name,
            extra=dict_to_struct(extra),
        )
        _: StopPlanResponse = await self.client.StopPlan(request, timeout=timeout)
        return

    async def get_plan(
        self,
        component_name: ResourceName,
        last_plan_only: bool = False,
        execution_id: Optional[str] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> GetPlanResponse:
        """By default: returns the plan history of the most recent ``move_on_globe()`` or ``move_on_map()``call to move a component.

        The plan history for executions before the most recent can be requested by providing an ExecutionID in the request.

        Returns a result if both of the following conditions are met:

        - the execution (call to ``move_on_globe()`` or ``move_on_map()``) is still executing **or** changed state within the last 24 hours
        - the robot has not reinitialized

        Plans never change.

        Replans always create new plans.

        Replans share the ExecutionID of the previously executing plan.

        All repeated fields are in time ascending order.

        Args:
            component_name (ResourceName): The component to stop
            last_plan_only (Optional[bool]): If supplied, the response will only return the last plan for the component / execution
            execution_id (Optional[str]): If supplied, the response will only return plans with the provided execution_id

        Returns:
            ``GetPlanResponse`` (GetPlanResponse): The current PlanWithStatus & replan history which matches the request
        """
        if extra is None:
            extra = {}

        request = GetPlanRequest(
            name=self.name,
            component_name=component_name,
            last_plan_only=last_plan_only,
            execution_id=execution_id,
            extra=dict_to_struct(extra),
        )
        response: GetPlanResponse = await self.client.GetPlan(request, timeout=timeout)
        return response

    async def list_plan_statuses(
        self,
        only_active_plans: bool = False,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> ListPlanStatusesResponse:
        """Returns the statuses of plans created by `move_on_globe()` or ``move_on_map()`` calls that meet at least one of the following
        conditions since the motion service initialized:

        - the plan's status is in progress
        - the plan's status changed state within the last 24 hours

        All repeated fields are in chronological order.

        Args:
            only_active_plans (Optional[bool]):  If supplied, the response will filter out any plans that are not executing

        Returns:
            ``ListPlanStatusesResponse`` (ListPlanStatusesResponse): List of last known statuses with the
            associated IDs of all plans within the TTL ordered by timestamp in ascending order
        """
        if extra is None:
            extra = {}

        request = ListPlanStatusesRequest(
            name=self.name,
            only_active_plans=only_active_plans,
            extra=dict_to_struct(extra),
        )
        response: ListPlanStatusesResponse = await self.client.ListPlanStatuses(request, timeout=timeout)
        return response

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
            component_name (viam.proto.common.ResourceName): Name of a component on a robot.
            destination_frame (str): Name of the desired reference frame.
            supplemental_transforms (Optional[List[viam.proto.common.Transform]]): Transforms used to augment the robot's frame while
                calculating pose.

        Returns:
            ``Pose`` (PoseInFrame): Pose of the given component and the frame in which it was observed.
        """
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

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **__) -> Mapping[str, ValueTypes]:
        """Send/receive arbitrary commands

        Args:
            command (Dict[str, ValueTypes]): The command to execute

        Returns:
            Dict[str, ValueTypes]: Result of the executed command
        """
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
