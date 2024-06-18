import abc
from dataclasses import dataclass
from typing import Any, Dict, Final, Optional, Tuple

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase


class Motor(ComponentBase):
    """Motor represents a physical motor.

    This acts as an abstract base class for any drivers representing specific
    motor implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.motor import Motor

    For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
    """

    @dataclass
    class Properties:
        position_reporting: bool

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "motor"
    )

    @abc.abstractmethod
    async def set_power(
        self,
        power: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Sets the "percentage" of power the motor should employ between -1 and 1.
        When ``power`` is negative, the rotation will be in the backward direction.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Set the power to 40% forwards.
            await my_motor.set_power(power=0.4)

        Args:
            power (float): Power between -1 and 1
                (negative implies backwards).

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...

    @abc.abstractmethod
    async def go_for(
        self,
        rpm: float,
        revolutions: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Spin the motor the specified number of ``revolutions`` at specified ``rpm``.
        When ``rpm`` or ``revolutions`` is a negative value, the rotation will be in the backward direction.
        Note: if both ``rpm`` and ``revolutions`` are negative, the motor will spin in the forward direction.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Turn the motor 7.2 revolutions at 60 RPM.
            await my_motor.go_for(rpm=60, revolutions=7.2)

        Args:
            rpm (float): Speed at which the motor should move in rotations per minute
                (negative implies backwards).
            revolutions (float): Number of revolutions the motor should run for
                (negative implies backwards).

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...

    @abc.abstractmethod
    async def go_to(
        self,
        rpm: float,
        position_revolutions: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Spin the motor to the specified position (provided in revolutions from home/zero),
        at the specified speed, in revolutions per minute.
        Regardless of the directionality of the ``rpm`` this function will move
        the motor towards the specified position.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Turn the motor to 8.3 revolutions from home at 75 RPM.
            await my_motor.go_to(rpm=75, revolutions=8.3)

        Args:
            rpm (float): Speed at which the motor should rotate (absolute value).
            position_revolutions (float): Target position relative to home/zero, in revolutions.

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...

    @abc.abstractmethod
    async def set_rpm(
        self,
        rpm: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Spin the motor indefinitely at the specified speed, in revolutions per minute.
        Positive ``rpm`` will result in forward movement and negative ``rpm`` will result in backwards movement

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Spin the motor at 75 RPM.
            await my_motor.set_rpm(rpm=75)

        Args:
            rpm (float): Speed at which the motor should rotate.

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...

    @abc.abstractmethod
    async def reset_zero_position(
        self,
        offset: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Set the current position (modified by ``offset``) to be the new zero (home) position.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Set the current position as the new home position with no offset.
            await my_motor.reset_zero_position(offset=0.0)

        Args:
            offset (float): The offset from the current position to new home/zero position.

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> float:
        """
        Report the position of the motor based on its encoder.
        The value returned is the number of revolutions relative to its zero position.
        This method will raise an exception if position reporting is not supported by the motor.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Get the current position of the motor.
            position = await my_motor.get_position()

        Returns:
            float: Number of revolutions the motor is away from zero/home.

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Properties:
        """
        Report a dictionary mapping optional properties to
        whether it is supported by this motor.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Report a dictionary mapping optional properties to whether it is supported by
            # this motor.
            properties = await my_motor.get_properties()

            # Print out the properties.
            print(f'Properties: {properties}')

        Returns:
            Properties: Map of feature names to supported status.

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
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
        Stop the motor immediately, without any gradual step down.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Stop the motor.
            await my_motor.stop()

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...

    @abc.abstractmethod
    async def is_powered(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[bool, float]:
        """
        Returns whether or not the motor is currently running.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Check whether the motor is currently running.
            powered = await my_motor.is_powered()

            print('Powered: ', powered)

        Returns:
            Tuple[bool, float]: A tuple containing two values; the first [0] value indicates whether the motor is currently powered, and
                the second [1] value indicates the current power percentage of the motor.

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the motor is currently moving.

        ::

            my_motor = Motor.from_robot(robot=robot, name="my_motor")

            # Check whether the motor is currently moving.
            moving = await my_motor.is_moving()
            print('Moving: ', moving)

        Returns:
            bool: Whether the motor is moving.

        For more information, see `Motor component <https://docs.viam.com/components/motor/>`_.
        """
        ...
