import abc

from viam.proto.api.common import Vector3

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
    ):
        """
        Move the base in a straight line the given `distance`, expressed in millimeters,
        at the given `velocity`, expressed in millimeters per second.
        When `distance` or `velocity` is 0, the base will stop.
        This method blocks until completed or cancelled

        Args:
            distance (int): The distance (in millimeters) to move.
                Negative implies backwards.
            velocity (float): The velocity (in millimeters per second) to move.
                Negative implies backwards.
        """
        ...

    @abc.abstractmethod
    async def spin(self, angle: float, velocity: float):
        """
        Spin the base in place `angle` degrees, at the given angular `velocity`,
        expressed in degrees per second.
        When `velocity` is 0, the base will stop.
        This method blocks until completed or cancelled

        Args:
            angle (float): The angle (in degrees) to spin.
                Negative implies backwards.
            velocity (float): The angular velocity (in degrees per second).
                to spin. Negative implies backwards.
        """
        ...

    @abc.abstractmethod
    async def set_power(self, linear: Vector3, angular: Vector3):
        """Set the linear and angular velocity of the Base
        When `linear` is 0, the the base will spin.
        When `angular` is 0, the the base will move in a straight line.
        When both `linear` and `angular` are 0, the base will stop.
        This method blocks until completed or cancelled

        Args:
            linear (Vector3): The linear velocity
            angular (Vector3): The angular velocity
        """
        ...

    @abc.abstractmethod
    async def set_velocity(self, linear: Vector3, angular: Vector3):
        """
        Set the linear and angular velocities of the base.


        Args:
            linear (Vector3): Velocity in mm/sec
            angular (Vector3): Velocity in deg/sec
        """

    @abc.abstractmethod
    async def stop(self):
        """
        Stop the base.
        """
        ...
