import abc
from dataclasses import dataclass
from typing import Any, Dict, Optional

from viam.errors import NotSupportedError

from ..component_base import ComponentBase


class Motor(ComponentBase):
    @dataclass
    class Properties:
        position_reporting: bool

    """
    Motor represents a physical motor.

    This acts as an abstract base class for any drivers representing specific
    motor implementations. This cannot be used on its own. If the `__init__()` function is
    overridden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def set_power(self, power: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Sets the "percentage" of power the motor should employ between -1 and 1.
        When `power` is negative, the rotation will be in the backward direction.

        Args:
            power (float): Power between -1 and 1
                (negative implies backwards).
        """
        ...

    @abc.abstractmethod
    async def go_for(self, rpm: float, revolutions: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Spin the motor the specified number of `revolutions` at specified `rpm`.
        When `rpm` or `revolutions` is a negative value, the rotation will be in the backward direction.
        Note: if both `rpm` and `revolutions` are negative, the motor will spin in the forward direction.

        Args:
            rpm (float): Speed at which the motor should move in rotations per minute
                (negative implies backwards).
            revolutions (float): Number of revolutions the motor should run for
                (negative implies backwards).
        """
        ...

    @abc.abstractmethod
    async def go_to(self, rpm: float, position_revolutions: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Spin the motor to the specified position (provided in revolutions from home/zero),
        at the specified speed, in revolutions per minute.
        Regardless of the directionality of the `rpm` this function will move
        the motor towards the specified position.

        Args:
            rpm (float): Speed at which the motor should rotate (absolute value).
            position_revolutions (float): Target position relative to home/zero, in revolutions.
        """
        ...

    @abc.abstractmethod
    async def reset_zero_position(self, offset: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Set the current position (modified by `offset`) to be the new zero (home) position.

        Args:
            offset (float): The offset from the current position to new home/zero position.
        """
        ...

    @abc.abstractmethod
    async def get_position(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> float:
        """
        Report the position of the motor based on its encoder.
        The value returned is the number of revolutions relative to its zero position.
        This method will raise an exception if position reporting is not supported by the motor.

        Returns:
            float: Number of revolutions the motor is away from zero/home.
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Properties:
        """
        Report a dictionary mapping optional properties to
        whether it is supported by this motor.

        Returns:
            Properties: Map of feature names to supported status.
        """
        ...

    @abc.abstractmethod
    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Stop the motor immediately, without any gradual step down.
        """
        ...

    @abc.abstractmethod
    async def is_powered(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> bool:
        """
        Returns whether or not the motor is currently running.

        Returns:
            bool: Indicates whether the motor is currently powered.
        """
        ...

    async def is_moving(self) -> bool:
        """
        Get if the motor is currently moving.

        Returns:
            bool: Whether the motor is moving.
        """
        raise NotSupportedError(f"Motor named {self.name} does not support returning whether it is moving")
