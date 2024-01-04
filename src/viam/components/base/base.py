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

        Args:
            distance (int): The distance (in millimeters) to move.
                Negative implies backwards.
            velocity (float): The velocity (in millimeters per second) to move.
                Negative implies backwards.
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

        Args:
            angle (float): The angle (in degrees) to spin.
            velocity (float): The angular velocity (in degrees per second)
                to spin.
                Given a positive angle and a positive velocity, the base will turn to the left.
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
        When ``linear`` is 0, the the base will spin.
        When ``angular`` is 0, the the base will move in a straight line.
        When both ``linear`` and ``angular`` are 0, the base will stop.
        When ``linear`` and ``angular`` are both nonzero, the base will move in an arc,
        with a tighter radius if angular power is greater than linear power.

        Args:
            linear (Vector3): The linear component. Only the Y component is used
                for wheeled base. Positive implies forwards.
            angular (Vector3): The angular component. Only the Z component is used
                for wheeled base. Positive turns left; negative turns right.
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


        Args:
            linear (Vector3): Velocity in mm/sec
            angular (Vector3): Velocity in deg/sec
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
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the base is currently moving.

        Returns:
            bool: Whether the base is moving.
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:
        """
        Get the base width and turning radius

        Returns:
            Properties: The properties of the base
        """
        ...
