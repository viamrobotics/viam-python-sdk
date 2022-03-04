import abc
from ..component_base import ComponentBase


class Base(ComponentBase):
    """
    Abstract representation of a physical base of a robot.

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def move_straight(
        self,
        distance: int,
        velocity: float,
        blocking: bool
    ):
        """
        Instructs the robot to move a robot's base in a straight line
        by a given distance, expressed in millimeters,
        and a given speed, expressed in millimeters per second.
        The method can be requested to block until the move is complete.
        If a distance or speed of zero is given, the base will stop.

        Args:
            distance (int): The distance (in millimeters) to move.
                Negative implies backwards.
            velocity (float): The speed (in millimeters per second) to move.
                Negative implies backwards.
            blocking (bool): Whether this method should be blocking
        """
        ...

    @abc.abstractmethod
    async def move_arc(
        self,
        distance: int,
        velocity: float,
        angle: float,
        blocking: bool
    ):
        """
        Instructs the robot to move its base in an arc
        by a given distance, expressed in millimeters,
        a given speed, expressed in millimeters per second of movement,
        and a given angle, expressed in degrees.
        If a distance of 0 is given the resultant motion is a spin
        and if velocity of 0 is given the base will stop.

        Args:
            distance (int): The distance (in millimeters) to move
                Negative implies backwards.
            velocity (float): The speed (in millimeters per second) to move
                Negative implies backwards.
            angle (float): The angle (in degrees) to move
                Negative implies backwards.
            blocking (bool): Whether this method should be blocking
        """
        ...

    @abc.abstractmethod
    async def spin(self, angle: float, velocity: float, blocking: bool):
        """
        Instructs the robot to spin by the given angle in degrees,
        expressed in degrees, at a given angular speed, expressed
        in degrees per second.
        The method can be requested to block until the move is complete.
        If a speed of 0 is given the base will stop.

        Args:
            angle (float): The angle (in degrees) to spin
                Negative implies backwards.
            velocity (float): The angular velocity (in degrees per second)
                to spin. Negative implies backwards.
            blocking (bool): Whether this method should be blocking
        """
        ...

    @abc.abstractmethod
    async def stop(self):
        """
        Instructs the robot to stop its base
        """
        ...
