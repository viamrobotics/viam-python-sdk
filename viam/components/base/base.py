import abc
from ..component_base import ComponentBase


class Base(ComponentBase):
    """
    Base represents a physical base of a robot.

    This acts as an abstract base class for any drivers representing specific 
    base implementations. This cannot be used on its own. If the `__init__()` function is
    overriden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def move_straight(
        self,
        distance: int,
        velocity: float,
        blocking: bool
    ):
        """
        Move the base in a straight line the given `distance`, expressed in millimeters,
        at the given `velocity`, expressed in millimeters per second.
        If `blocking` is true, the method not return until the move is complete.
        If `distance` or `velocity` is 0, the base will stop.

        Args:
            distance (int): the distance (in millimeters) to move.
                Negative implies backwards.
            velocity (float): the velocity (in millimeters per second) to move.
                Negative implies backwards.
            blocking (bool): whether this method should be blocking.
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
        Move the base in an arc the given `distance`, expressed in millimeters,
        at the given `velocity`, expressed in millimeters per second, turning `angle`
        degrees in the process.
        If `blocking` is true, the method not return until the move is complete.
        If `distance` is 0, the the base will spin.
        If `angle` is 0, the the base will move in a straight line.
        If `velocity` is 0, the base will stop.

        Args:
            distance (int): The distance (in millimeters) to move
                Negative implies backwards.
            velocity (float): The velocity (in millimeters per second) to move
                Negative implies backwards.
            angle (float): The angle (in degrees) to move
                Negative implies backwards.
            blocking (bool): Whether this method should be blocking
        """
        ...

    @abc.abstractmethod
    async def spin(self, angle: float, velocity: float, blocking: bool):
        """
        Spin the base in place `angle` degrees, at the given angular `velocity`,
        expressed in degrees per second.
        If `blocking` is true, the method not return until the move is complete.
        If `velocity` is 0, the base will stop.

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
        Stop the base.
        """
        ...
