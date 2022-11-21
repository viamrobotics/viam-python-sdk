import abc
from typing import Any, Mapping, Optional

from viam.errors import NotSupportedError

from ..component_base import ComponentBase


class Servo(ComponentBase):
    """
    Servo represents a physical servo.

    This acts as an abstract base class for any drivers representing specific
    servo implementations. This cannot be used on its own. If the `__init__()` function is
    overridden, it must call the `super().__init__()` function.
    """

    name: str

    @abc.abstractmethod
    async def move(self, angle: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        """
        Move the servo to the provided angle.

        Args:
            angle (int): The desired angle of the servo in degrees.
        """
        ...

    @abc.abstractmethod
    async def get_position(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        """
        Get the current angle (degrees) of the servo.

        Returns:
            int: The current angle of the servo in degrees.
        """
        ...

    @abc.abstractmethod
    async def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        """
        Stop the servo. It is assumed that the servo stops immediately.
        """
        ...

    async def is_moving(self) -> bool:
        """
        Get if the servo is currently moving.

        Returns:
            bool: Whether the servo is moving.
        """
        raise NotSupportedError(f"Servo named {self.name} does not support returning whether it is moving")
