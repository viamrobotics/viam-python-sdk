import abc

from ..component_base import ComponentBase


class ServoBase(ComponentBase):
    """
    Abstract representation of a physical servo.

    If you override the init function,
    you must call the super init function.
    """

    name: str

    @abc.abstractmethod
    async def move(self, angle: int):
        """
        Move the servo to the provided angle

        Args:
            angle (int): the desired angle of the servo in degrees
        """
        ...

    @abc.abstractmethod
    async def get_position(self) -> int:
        """
        Get the current angle (degrees) of the servo

        Returns:
            int: The current angle of the servo in degrees
        """
        ...
