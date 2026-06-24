import abc
from dataclasses import dataclass
from datetime import timedelta
from typing import Any, AsyncIterator, Dict, Final, List, Optional

from google.protobuf.duration_pb2 import Duration

from viam.components import KinematicsReturn
from viam.components.component_base import ComponentBase
from viam.proto.component.arm import (
    JointAccelerations,
    JointVelocities,
    MoveThroughJointPositionsStreamedResponse,
    TrajectoryPoint as TrajectoryPointPb,
)
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT
from viam.utils import dict_to_struct, struct_to_dict

from . import JointPositions, Pose


class Arm(ComponentBase):
    """
    Arm represents a physical robot arm that exists in three-dimensional space.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.arm import Arm
        # To use move_to_position:
        from viam.proto.common import Pose
        # To use move_to_joint_positions:
        from viam.proto.component.arm import JointPositions

    For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/>`_.
    """

    API: Final = API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "arm")  # pyright: ignore [reportIncompatibleVariableOverride]

    @dataclass
    class KinematicConstraints:
        """
        Optional per-waypoint kinematic constraints attached to a ``TrajectoryPoint``.

        Joint velocities are required; joint accelerations are optional. The presence
        of velocities is what unlocks the option to pass accelerations -- accelerations
        cannot be specified without velocities. Each list is ordered spatially from the
        base toward the end effector of the arm and must match the arm's DOF.
        """

        velocities: List[float]
        """Target joint velocities at this waypoint. Rotational values in degrees per second,
        translational values in mm per second."""

        accelerations: Optional[List[float]] = None
        """Optional target joint accelerations at this waypoint. Rotational values in
        degrees per second squared, translational values in mm per second squared."""

    @dataclass
    class TrajectoryPoint:
        """
        A single waypoint of a kinematized trajectory consumed by
        ``move_through_joint_positions_streamed``.

        Times across a streamed trajectory must be strictly monotonically increasing.
        The first point in a stream must have ``time`` equal to zero.
        """

        time: timedelta
        """Time at which this waypoint should be reached, measured from the start of the motion."""

        positions: List[float]
        """Joint positions at this waypoint. Rotational values in degrees, translational values in mm."""

        constraints: Optional["Arm.KinematicConstraints"] = None
        """Optional kinematic constraints at this waypoint."""

        def to_proto(self) -> TrajectoryPointPb:
            duration = Duration()
            duration.FromTimedelta(self.time)
            constraints_pb = None
            if self.constraints is not None:
                accelerations_pb = None
                if self.constraints.accelerations is not None:
                    accelerations_pb = JointAccelerations(values=self.constraints.accelerations)
                constraints_pb = TrajectoryPointPb.KinematicConstraints(
                    velocities=JointVelocities(values=self.constraints.velocities),
                    accelerations=accelerations_pb,
                )
            return TrajectoryPointPb(
                time=duration,
                positions=JointPositions(values=self.positions),
                constraints=constraints_pb,
            )

        @classmethod
        def from_proto(cls, proto: TrajectoryPointPb) -> "Arm.TrajectoryPoint":
            constraints = None
            if proto.HasField("constraints"):
                accelerations = None
                if proto.constraints.HasField("accelerations"):
                    accelerations = list(proto.constraints.accelerations.values)
                constraints = Arm.KinematicConstraints(
                    velocities=list(proto.constraints.velocities.values),
                    accelerations=accelerations,
                )
            return cls(
                time=proto.time.ToTimedelta(),
                positions=list(proto.positions.values),
                constraints=constraints,
            )

    @dataclass
    class Response:
        """
        Per-message response from ``move_through_joint_positions_streamed``.

        For the proof-of-concept the response payload is empty; the type exists so that
        callers can iterate the response stream today and pick up future per-batch
        status fields without an API reshape.
        """

        extra: Optional[Dict[str, Any]] = None
        """Arm-side reply data."""

        def to_proto(self) -> MoveThroughJointPositionsStreamedResponse:
            return MoveThroughJointPositionsStreamedResponse(extra=dict_to_struct(self.extra))

        @classmethod
        def from_proto(cls, proto: MoveThroughJointPositionsStreamedResponse) -> "Arm.Response":
            return cls(extra=struct_to_dict(proto.extra) if proto.HasField("extra") else None)

    @abc.abstractmethod
    async def get_end_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Pose:
        """
        Get the current position of the end of the arm expressed as a ``Pose``.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Get the end position of the arm as a Pose.
            pos = await my_arm.get_end_position()

        Returns:
            Pose: A representation of the arm's current position as a 6 DOF (six degrees of freedom) pose.
            The ``Pose`` is composed of values for location and orientation with respect to the origin.
            Location is expressed as distance, which is represented by x, y, and z coordinate values.
            Orientation is expressed as an orientation vector, which is represented by o_x, o_y, o_z, and theta values.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#getendposition>`_.
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        pose: Pose,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move the end of the arm to the Pose specified in ``pose``.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Create a Pose for the arm.
            examplePose = Pose(x=5, y=5, z=5, o_x=5, o_y=5, o_z=5, theta=20)

            # Move your arm to the Pose.
            await my_arm.move_to_position(pose=examplePose)

        Args:
            pose (Pose): The destination ``Pose`` for the arm. The ``Pose`` is composed of values for location and orientation
                with respect to the origin.
                Location is expressed as distance, which is represented by x, y, and z coordinate values.
                Orientation is expressed as an orientation vector, which is represented by o_x, o_y, o_z, and theta values.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#movetoposition>`_.
        """
        ...

    @abc.abstractmethod
    async def move_to_joint_positions(
        self,
        positions: JointPositions,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move each joint on the arm to the corresponding angle specified in ``positions``.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Declare a list of values with your desired rotational value for each joint on
            # the arm. This example is for a 5dof arm.
            degrees = [0.0, 45.0, 0.0, 0.0, 0.0]

            # Declare a new JointPositions with these values.
            jointPos = JointPositions(values=degrees)

            # Move each joint of the arm to the position these values specify.
            await my_arm.move_to_joint_positions(positions=jointPos)

        Args:
            positions (JointPositions): The destination ``JointPositions`` for the arm.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#movetojointpositions>`_.
        """
        ...

    @abc.abstractmethod
    async def move_through_joint_positions(
        self,
        positions: List[JointPositions],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move each joint on the arm to through the corresponding angles specified in each entry of ``positions``.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Declare a list of values with your desired rotational value for each joint on
            # the arm. This example is for a 5dof arm.
            degrees1 = [0.0, 45.0, 0.0, 0.0, 0.0]
            degrees2 = [0.0, 45.0, 45.0, 0.0, 0.0]

            # Declare a new JointPositions with these values.
            positions = [JointPositions(values=degrees1), JointPositions(values=degrees2)]

            # Move each joint of the arm to the position these values specify.
            await my_arm.move_through_joint_positions(positions=positions)

        Args:
            positions (JointPositions): A list of destination ``JointPositions`` for the arm.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#movethroughjointpositions>`_.
        """
        ...

    @abc.abstractmethod
    async def move_through_joint_positions_streamed(
        self,
        batches: AsyncIterator[List["Arm.TrajectoryPoint"]],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> AsyncIterator["Arm.Response"]:
        """
        Move the arm through a time-parameterized stream of joint waypoints.

        The caller supplies an asynchronous iterator of batches, where each batch is a
        ``list`` of ``TrajectoryPoint`` values. Each list yielded by the caller is sent
        as one wire ``TrajectoryBatch``; the caller therefore controls the wire cadence
        directly, and can pack enough points into the first send to ride out network
        jitter on tight-cadence trajectories. A caller that genuinely wants per-point
        granularity yields ``[point]`` for each point. Per-message responses are yielded
        back to the caller as they are produced by the arm. Arm-side errors raised
        during execution surface as a gRPC status on the response iteration -- the
        ``async for`` raises rather than returning.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            async def batches():
                yield [
                    Arm.TrajectoryPoint(time=timedelta(seconds=0.0), positions=[0.0, 0.0, 0.0, 0.0, 0.0]),
                    Arm.TrajectoryPoint(time=timedelta(seconds=1.0), positions=[10.0, 0.0, 0.0, 0.0, 0.0]),
                ]

            async for resp in my_arm.move_through_joint_positions_streamed(batches()):
                # Observe arm-side acknowledgements; errors raise out of this iteration.
                pass

        Args:
            batches: an asynchronous iterator of lists of ``TrajectoryPoint`` values.
                Each list maps to one wire ``TrajectoryBatch``. Point times must be
                strictly monotonically increasing across the entire stream (not just
                within each batch), and the first point of the very first batch must
                have time zero.

        Returns:
            AsyncIterator[Arm.Response]: a live stream of per-message responses.
        """
        ...

    @abc.abstractmethod
    async def get_joint_positions(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> JointPositions:
        """
        Get the JointPositions representing the current position of the arm.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Get the current position of each joint on the arm as JointPositions.
            pos = await my_arm.get_joint_positions()

        Returns:
            JointPositions: The current ``JointPositions`` for the arm.
            ``JointPositions`` can have one attribute, ``values``, a list of joint positions with rotational values (degrees)
            and translational values (mm).

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#getjointpositions>`_.
        """
        ...

    @abc.abstractmethod
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Stop all motion of the arm. It is assumed that the arm stops immediately.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Stop all motion of the arm. It is assumed that the arm stops immediately.
            await my_arm.stop()

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#stop>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the arm is currently moving.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Stop all motion of the arm. It is assumed that the arm stops immediately.
            await my_arm.stop()

            # Print if the arm is currently moving.
            print(await my_arm.is_moving())

        Returns:
            bool: Whether the arm is moving.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#ismoving>`_.
        """
        ...

    @abc.abstractmethod
    async def get_kinematics(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> KinematicsReturn:
        """
        Get the kinematics information associated with the arm.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Get the kinematics information associated with the arm.
            kinematics = await my_arm.get_kinematics()

            # Get the format of the kinematics file.
            k_file = kinematics[0]

            # Get the byte contents of the file.
            k_bytes = kinematics[1]

        Returns:
            Tuple[KinematicsFileFormat.ValueType, bytes]: A tuple containing two values; the first [0] value represents the format of the
            file, either in URDF format (``KinematicsFileFormat.KINEMATICS_FILE_FORMAT_URDF``) or
            Viam's kinematic parameter format (spatial vector algebra) (``KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA``),
            and the second [1] value represents the byte contents of the file.
            If available, a third [2] value provides meshes keyed by URDF filepath.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#getkinematics>`_.
        """
        ...
