import abc
from dataclasses import dataclass
from typing import Any, Dict, Final, Optional

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase
from . import Vector3


class Base(ComponentBase):
    """
    Base represents a physical base of a robot.

    This acts as an abstract base class for any drivers representing specific
    base implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.base import Base

    For more information, see `Base component <https://docs.viam.com/components/base/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "base"
    )

    @dataclass
    class Properties:
        width_meters: float
        turning_radius_meters: float
        wheel_circumference_meters: float

    @abc.abstractmethod
    async def move_straight(
        self,
        distance: int,
        velocity: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move the base in a straight line the given ``distance``, expressed in millimeters,
        at the given ``velocity``, expressed in millimeters per second.
        When ``distance`` or ``velocity`` is 0, the base will stop.
        This method blocks until completed or cancelled.

        ::

            my_base = Base.from_robot(robot=robot, name="my_base")

            # Move the base 40 mm at a velocity of 90 mm/s, forward.
            await my_base.move_straight(distance=40, velocity=90)

            # Move the base 40 mm at a velocity of -90 mm/s, backward.
            await my_base.move_straight(distance=40, velocity=-90)

        Args:
            distance (int): The distance (in millimeters) to move.
                Negative implies backwards.
            velocity (float): The velocity (in millimeters per second) to move.
                Negative implies backwards.

        For more information, see `Base component <https://docs.viam.com/components/base/>`_.
        """
        ...

    @abc.abstractmethod
    async def spin(
        self,
        angle: float,
        velocity: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Spin the base in place ``angle`` degrees, at the given angular ``velocity``,
        expressed in degrees per second.
        When ``velocity`` is 0, the base will stop.
        This method blocks until completed or cancelled.

        ::

            my_base = Base.from_robot(robot=robot, name="my_base")

            # Spin the base 10 degrees at an angular velocity of 15 deg/sec.
            await my_base.spin(angle=10, velocity=15)

        Args:
            angle (float): The angle (in degrees) to spin.
            velocity (float): The angular velocity (in degrees per second)
                to spin.
                Given a positive angle and a positive velocity, the base will turn to the left.

        For more information, see `Base component <https://docs.viam.com/components/base/>`_.
        """
        ...

    @abc.abstractmethod
    async def set_power(
        self,
        linear: Vector3,
        angular: Vector3,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """Set the linear and angular velocity of the Base
        When ``linear`` is 0, the base will spin.
        When ``angular`` is 0, the base will move in a straight line.
        When both ``linear`` and ``angular`` are 0, the base will stop.
        When ``linear`` and ``angular`` are both nonzero, the base will move in an arc,
        with a tighter radius if angular power is greater than linear power.

        ::

            my_base = Base.from_robot(robot=robot, name="my_base")

            # Make your wheeled base move forward. Set linear power to 75%.
            print("move forward")
            await my_base.set_power(
                linear=Vector3(x=0, y=-.75, z=0),
                angular=Vector3(x=0, y=0, z=0))

            # Make your wheeled base move backward. Set linear power to -100%.
            print("move backward")
            await my_base.set_power(
                linear=Vector3(x=0, y=-1.0, z=0),
                angular=Vector3(x=0, y=0, z=0))

            # Make your wheeled base spin left. Set angular power to 100%.
            print("spin left")
            await my_base.set_power(
                linear=Vector3(x=0, y=0, z=0),
                angular=Vector3(x=0, y=0, z=1))

            # Make your wheeled base spin right. Set angular power to -75%.
            print("spin right")
            await my_base.set_power(
                linear=Vector3(x=0, y=0, z=0),
                angular=Vector3(x=0, y=0, z=-.75))

        Args:
            linear (Vector3): The linear component. Only the Y component is used
                for wheeled base. Positive implies forwards.
            angular (Vector3): The angular component. Only the Z component is used
                for wheeled base. Positive turns left; negative turns right.

        For more information, see `Base component <https://docs.viam.com/components/base/>`_.
        """
        ...

    @abc.abstractmethod
    async def set_velocity(
        self,
        linear: Vector3,
        angular: Vector3,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Set the linear and angular velocities of the base.

        ::

            my_base = Base.from_robot(robot=robot, name="my_base")

            # Set the linear velocity to 50 mm/sec and the angular velocity to
            # 15 degree/sec.
            await my_base.set_velocity(
                linear=Vector3(x=0, y=50, z=0), angular=Vector3(x=0, y=0, z=15))

        Args:
            linear (Vector3): Velocity in mm/sec
            angular (Vector3): Velocity in deg/sec

        For more information, see `Base component <https://docs.viam.com/components/base/>`_.
        """

    @abc.abstractmethod
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Stop the base.

        ::

            my_base = Base.from_robot(robot=robot, name="my_base")

            # Move the base forward 10 mm at a velocity of 50 mm/s.
            await my_base.move_straight(distance=10, velocity=50)

            # Stop the base.
            await my_base.stop()

        For more information, see `Base component <https://docs.viam.com/components/base/>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the base is currently moving.

        ::

            my_base = Base.from_robot(robot=robot, name="my_base")

            # Check whether the base is currently moving.
            moving = await my_base.is_moving()
            print('Moving: ', moving)

        Returns:
            bool: Whether the base is moving.

        For more information, see `Base component <https://docs.viam.com/components/base/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:
        """
        Get the base width and turning radius

        ::

            my_base = Base.from_robot(robot=robot, name="my_base")

            # Get the width and turning radius of the base
            properties = await my_base.get_properties()

            # Get the width
            print(f"Width of base: {properties.width_meters}")

            # Get the turning radius
            print(f"Turning radius of base: {properties.turning_radius_meters}")

            # Get the wheel circumference
            print(f"Wheel circumference of base: {properties.wheel_circumference_meters}")

        Returns:
            Properties: The properties of the base

        For more information, see `Base component <https://docs.viam.com/components/base/>`_.
        """
        ...
