import abc

from ..component_base import ComponentBase


class Servo(ComponentBase):
    """
    Servo represents a physical servo.

    This acts as an abstract base class for any drivers representing specific
    servo implementations. This cannot be used on its own. If the `__init__()` function is
    overriden, it must call the `super().__init__()` function.
    """

    name: str

    @abc.abstractmethod
    async def move(self, angle: int):
        """
        Move the servo to the provided angle.

        Args:
            angle (int): The desired angle of the servo in degrees.
        """
        ...

    @abc.abstractmethod
    async def get_position(self) -> int:
        """
        Get the current angle (degrees) of the servo.

        Returns:
            int: The current angle of the servo in degrees.
        """
        ...

    @abc.abstractmethod
    async def stop(self):
        """
        Stop the servo. It is assumed that the servo stops immediately.
        """
        ...
