import abc
from typing import TypedDict

from ..base import ComponentBase


class MotorBase(ComponentBase):

    class Features(TypedDict):
        position_reporting: bool

    """
    Abstract representation of a physical Motor

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def set_power(self, power: float):
        """
        Sets the percentage of power the motor should employ between -1 and 1.
        Negative power implies a backward directional rotation

        Args:
            power (float): Power percentage between -1 and 1
                (negative implies backwards)
        """
        ...

    @abc.abstractmethod
    async def go_for(self, rpm: float, revolutions: float):
        """
        Instructs the motor to go in a specific direction for a specific
        amount of revolutions at a given speed in revolutions per minute.
        Both the RPM and the revolutions can be assigned negative values
        to move in a backwards direction.
        Note: if both RPM and revolustions are negative,
        the motor will spin in the forward direction

        Args:
            rpm (float): Speed at which the motor should move
                (negative implies backwards)
            revolutions (float): Number of revolutions the motor should run
                (negative implies backwards)
        """
        ...

    @abc.abstractmethod
    async def go_to(self, rpm: float, position_revolutions: float):
        """
        Instructs the motor to go to a specific position (provided in
        revolutions from home/zero), at a specific speed.
        Regardless of the directionality of the RPM this function will move
        the motor towards the specified target/position

        Args:
            rpm (float): Speed at which the motor should move (absolute value)
            position_revolutions (float): Target position relative to home/zero
        """
        ...

    @abc.abstractmethod
    async def reset_zero_position(self, offset: float):
        """
        Set the current position (+/- offset)
        to be the new zero (home) position.

        Args:
            offset (float): The new home/zero position
        """
        ...

    @abc.abstractmethod
    async def get_position(self) -> float:
        """
        Reports the position of the motor based on its encoder.
        The unit returned is the number of revolutions relative
        to its zero position.
        This method will raise an exception if position reporting is
        not supported.

        Returns:
            float: position of the motor relative to zero/home
        """
        ...

    @abc.abstractmethod
    async def get_features(self) -> Features:
        """
        Reports a dictionary mapping optional features to
        whether it is supported by this motor

        Returns:
            Features: map of feature names to supported status
        """
        ...

    async def is_powered(self) -> bool:
        """
        Returns whether or not the motor is currently running

        Returns:
            bool: The power state of the motor
        """
        ...
