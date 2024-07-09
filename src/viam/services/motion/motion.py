import abc
import sys
from typing import Any, Final, Mapping, Optional, Sequence

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from viam.proto.common import GeoGeometry, Geometry, GeoPoint, Pose, PoseInFrame, ResourceName, Transform, WorldState
from viam.proto.service.motion import Constraints, GetPlanResponse, MotionConfiguration, PlanStatusWithID
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.utils import ValueTypes

from ..service_base import ServiceBase


class Motion(ServiceBase):
    """Motion is a Viam service that coordinates motion planning across all of the components in a given robot.

    The motion planning service calculates a valid path that avoids self collision by default. If additional constraints are supplied in the
    ``world_state`` message, the motion planning service will also account for those.

    For more information, see `Motion service <https://docs.viam.com/services/motion/>`_.
    """

    Plan: "TypeAlias" = GetPlanResponse

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "motion"
    )

    @abc.abstractmethod
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

        ::

            motion = MotionClient.from_robot(robot=robot, name="builtin")

            # Assumes a gripper configured with name "my_gripper" on the machine
            gripper_name = Gripper.get_resource_name("my_gripper")
            my_frame = "my_gripper_offset"

            goal_pose = Pose(x=0, y=0, z=300, o_x=0, o_y=0, o_z=1, theta=0)

            # Move the gripper
            moved = await motion.move(component_name=gripper_name,
                                  destination=PoseInFrame(reference_frame="myFrame",
                                                          pose=goal_pose),
                                  world_state=worldState,
                                  constraints={},
                                  extra={})

        Args:
            component_name (viam.proto.common.ResourceName): Name of a component on a given robot.
            destination (viam.proto.common.PoseInFrame): The destination to move to, expressed as a ``Pose`` and the frame in which it was
                observed.
            world_state (viam.proto.common.WorldState): When supplied, the motion service will create a plan that obeys any constraints
                expressed in the WorldState message.
            constraints (viam.proto.service.motion.Constraints): When supplied, the motion service will create a plan that obeys any
                specified constraints.

        Returns:
            bool: Whether the move was successful.

        For more information, see `Motion service <https://docs.viam.com/services/motion/>`_.
        """
        ...

    @abc.abstractmethod
    async def move_on_globe(
        self,
        component_name: ResourceName,
        destination: GeoPoint,
        movement_sensor_name: ResourceName,
        obstacles: Optional[Sequence[GeoGeometry]] = None,
        heading: Optional[float] = None,
        configuration: Optional[MotionConfiguration] = None,
        *,
        bounding_regions: Optional[Sequence[GeoGeometry]] = None,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> str:
        """Move a component to a specific latitude and longitude, using a ``MovementSensor`` to check the location.

        ``move_on_globe()`` is non blocking, meaning the motion service will move the component to the destination
        GPS point after ``move_on_globe()`` returns.

        Each successful ``move_on_globe()`` call returns a unique ExecutionID which you can use to identify all plans
        generated during the ``move_on_globe()`` call.

        You can monitor the progress of the ``move_on_globe()`` call by querying ``get_plan()`` and ``list_plan_statuses()``.

        ::

            motion = MotionClient.from_robot(robot=robot, name="builtin")

            # Get the ResourceNames of the base and movement sensor
            my_base_resource_name = Base.get_resource_name("my_base")
            mvmnt_sensor_resource_name = MovementSensor.get_resource_name(
                "my_movement_sensor")
            #  Define a destination GeoPoint at the GPS coordinates [0, 0]
            my_destination = movement_sensor.GeoPoint(latitude=0, longitude=0)

            # Move the base component to the designated geographic location, as reported by the movement sensor
            execution_id = await motion.move_on_globe(
                component_name=my_base_resource_name,
                destination=my_destination,
                movement_sensor_name=mvmnt_sensor_resource_name)

        Args:
            component_name (ResourceName): The ResourceName of the base to move.
            destination (GeoPoint): The location of the component's destination, represented in geographic notation as a
                GeoPoint (lat, lng).
            movement_sensor_name (ResourceName): The ResourceName of the movement sensor that you want to use to check
                the machine's location.
            obstacles (Optional[Sequence[GeoGeometry]]): Obstacles to consider when planning the motion of the component,
                with each represented as a GeoGeometry. Default: None
            heading (Optional[float]): The compass heading, in degrees, that the machine's movement sensor should report
                at the destination point. Range: [0-360) 0: North, 90: East, 180: South, 270: West. Default: None
            configuration (Optional[MotionConfiguration]): The configuration you want to set across this machine for this
                motion service. This parameter and each of its fields are optional.

                - obstacle_detectors (Sequence[ObstacleDetector]): The names of each vision service and camera resource pair
                you want to use for transient obstacle avoidance.

                - position_polling_frequency_hz (float): The frequency in Hz to poll the position of the machine.
                - obstacle_polling_frequency_hz (float): The frequency in Hz to poll the vision service for new obstacles.
                - plan_deviation_m (float): The distance in meters that the machine can deviate from the motion plan.
                - linear_m_per_sec (float): Linear velocity this machine should target when moving.
                - angular_degs_per_sec (float): Angular velocity this machine should target when turning.
            bounding_regions (Optional[Sequence[GeoGeometry]]): Set of obstacles which the robot must remain within while navigating
            extra (Optional[Dict[str, Any]]): Extra options to pass to the underlying RPC call.
            timeout (Optional[float]): An option to set how long to wait (in seconds) before calling a time-out and closing
                the underlying RPC call.


        Returns:
            str: ExecutionID of the ``move_on_globe()`` call, which can be used to track execution progress.

        For more information, see `Motion service <https://docs.viam.com/services/motion/>`_.
        """
        ...

    @abc.abstractmethod
    async def move_on_map(
        self,
        component_name: ResourceName,
        destination: Pose,
        slam_service_name: ResourceName,
        configuration: Optional[MotionConfiguration] = None,
        obstacles: Optional[Sequence[Geometry]] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> str:
        """
        Move a component to a specific pose, using a ``SlamService`` for the SLAM map, using a ``SLAM Service`` to check the location.

        ``move_on_map()`` is non blocking, meaning the motion service will move the component to the destination
        Pose point after ``move_on_map()`` returns.

        Each successful ``move_on_map()`` call returns a unique ExecutionID which you can use to identify all plans
        generated during the ``move_on_map()`` call.

        You can monitor the progress of the ``move_on_map()`` call by querying ``get_plan()`` and ``list_plan_statuses()``.

        ::

            motion = MotionClient.from_robot(robot=robot, name="builtin")

            # Get the ResourceNames of the base component and SLAM service
            my_base_resource_name = Base.get_resource_name("my_base")
            my_slam_service_name = SLAMClient.get_resource_name("my_slam_service")

            # Define a destination pose with respect to the origin of the map from the SLAM service "my_slam_service"
            my_pose = Pose(y=10)

            # Move the base component to the destination pose of Y=10, a location of
            # (0, 10, 0) in respect to the origin of the map
            execution_id = await motion.move_on_map(component_name=my_base_resource_name,
                                                    destination=my_pose,
                                                    slam_service_name=my_slam_service_name)

        Args:
            component_name (ResourceName): The ResourceName of the base to move.
            destination (Pose): The destination, which can be any Pose with respect to the SLAM map's origin.
            slam_service_name (ResourceName): The ResourceName of the SLAM service from which the SLAM map is requested.
            configuration (Optional[MotionConfiguration]): The configuration you want to set across this machine for this motion service.
                This parameter and each of its fields are optional.

                - obstacle_detectors (Sequence[ObstacleDetector]): The names of each vision service and camera resource pair you want to use
                for transient obstacle avoidance.

                - position_polling_frequency_hz (float): The frequency in hz to poll the position of the machine.
                - obstacle_polling_frequency_hz (float): The frequency in hz to poll the vision service for new obstacles.
                - plan_deviation_m (float): The distance in meters that the machine can deviate from the motion plan.
                - linear_m_per_sec (float): Linear velocity this machine should target when moving.
                - angular_degs_per_sec (float): Angular velocity this machine should target when turning.
            obstacles (Optional[Sequence[Geometry]]): Obstacles to be considered for motion planning.
            extra (Optional[Dict[str, Any]]): Extra options to pass to the underlying RPC call.
            timeout (Optional[float]): An option to set how long to wait (in seconds) before calling a time-out and closing the underlying
                RPC call.

        Returns:
            str: ExecutionID of the ``move_on_map()`` call, which can be used to track execution progress.

        For more information, see `Motion service <https://docs.viam.com/services/motion/>`_.
        """
        ...

    @abc.abstractmethod
    async def stop_plan(
        self,
        component_name: ResourceName,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ):
        """Stop a component being moved by an in progress ``move_on_globe()`` or ``move_on_map()`` call.

        ::

            # Assuming a `move_on_globe()` started the execution
            # Stop the base component which was instructed to move by `move_on_globe()`
            # or `move_on_map()`
            my_base_resource_name = Base.get_resource_name("my_base")
            await motion.stop_plan(component_name=mvmnt_sensor)

        Args:
            component_name (ResourceName): The component to stop

        For more information, see `Motion service <https://docs.viam.com/services/motion/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_plan(
        self,
        component_name: ResourceName,
        last_plan_only: bool = False,
        execution_id: Optional[str] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> Plan:
        """By default: returns the plan history of the most recent ``move_on_globe()`` or ``move_on_map()`` call to move a component.

        The plan history for executions before the most recent can be requested by providing an ExecutionID in the request.

        Returns a result if both of the following conditions are met:

        - the execution (call to ``move_on_globe()`` or ``move_on_map()``) is still executing **or** changed state within the last 24 hours
        - the robot has not reinitialized

        Plans never change.

        Replans always create new plans.

        Replans share the ExecutionID of the previously executing plan.

        All repeated fields are in time ascending order.

        ::

            motion = MotionClient.from_robot(robot=robot, name="builtin")
            my_base_resource_name = Base.get_resource_name("my_base")
            # Get the plan(s) of the base component which was instructed to move by `MoveOnGlobe()` or `MoveOnMap()`
            resp = await motion.get_plan(component_name=my_base_resource_name)

        Args:
            component_name (ResourceName): The component to stop
            last_plan_only (Optional[bool]): If supplied, the response will only return the last plan for the component / execution.
            execution_id (Optional[str]): If supplied, the response will only return plans with the provided execution_id.

        Returns:
            ``GetPlanResponse`` (GetPlanResponse): The current PlanWithStatus & replan history which matches the request

        For more information, see `Motion service <https://docs.viam.com/services/motion/>`_.
        """
        ...

    @abc.abstractmethod
    async def list_plan_statuses(
        self,
        only_active_plans: bool = False,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> Sequence[PlanStatusWithID]:
        """Returns the statuses of plans created by `move_on_globe()` or ``move_on_map()`` calls that meet at least one of the following
        conditions since the motion service initialized:

        - the plan's status is in progress
        - the plan's status changed state within the last 24 hours

        All repeated fields are in chronological order.

        ::

            motion = MotionClient.from_robot(robot=robot, name="builtin")
            # List the plan statuses of the motion service within the TTL
            resp = await motion.list_plan_statuses()

        Args:
            only_active_plans (Optional[bool]):  If supplied, the response will filter out any plans that are not executing.

        Returns:
            ``ListPlanStatusesResponse`` (ListPlanStatusesResponse): List of last known statuses with the
            associated IDs of all plans within the TTL ordered by timestamp in ascending order.

        For more information, see `Motion service <https://docs.viam.com/services/motion/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_pose(
        self,
        component_name: ResourceName,
        destination_frame: str,
        supplemental_transforms: Optional[Sequence[Transform]] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> PoseInFrame:
        """
        Get the Pose and observer frame for any given component on a robot.

        ::

            # Note that the example uses the ``Arm`` class, but any component class that inherits from ``ComponentBase`` will work
            # (``Base``, ``Gripper``, etc).

            # Create a `component_name`:
            component_name = Arm.get_resource_name("arm")

            from viam.components.gripper import Gripper
            from viam.services.motion import MotionClient

            # Assume that the connect function is written and will return a valid machine.
            robot = await connect()

            motion = MotionClient.from_robot(robot=robot, name="builtin")
            gripperName = Gripper.get_resource_name("my_gripper")
            gripperPoseInWorld = await motion.get_pose(component_name=gripperName,
                                                    destination_frame="world")

        Args:
            component_name (viam.proto.common.ResourceName): Name of a component on a robot.
            destination_frame (str): Name of the desired reference frame.
            supplemental_transforms (Optional[List[viam.proto.common.Transform]]): Transforms used to augment the robot's frame while
                calculating pose.

        Returns:
            ``Pose`` (PoseInFrame): Pose of the given component and the frame in which it was observed.

        For more information, see `Motion service <https://docs.viam.com/services/motion/>`_.
        """
        ...
