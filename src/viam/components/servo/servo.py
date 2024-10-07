import abc
from typing import Any, Final, Mapping, Optional

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase


class Servo(ComponentBase):
    """
    Servo represents a physical servo.

    This acts as an abstract base class for any drivers representing specific
    servo implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.servo import Servo

    For more information, see `Servo component <https://docs.viam.com/components/servo/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "servo"
    )

    @abc.abstractmethod
    async def move(self, angle: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        """
        Move the servo to the provided angle.

        ::

            my_servo = Servo.from_robot(robot=robot, name="my_servo")

            # Move the servo from its origin to the desired angle of 10 degrees.
            await my_servo.move(10)

            # Move the servo from its origin to the desired angle of 90 degrees.
            await my_servo.move(90)

        Args:
            angle (int): The desired angle of the servo in degrees.

        For more information, see `Servo component <https://docs.viam.com/components/servo/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_position(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        """
        Get the current angle (degrees) of the servo.

        ::

            my_servo = Servo.from_robot(robot=robot, name="my_servo")

            # Move the servo from its origin to the desired angle of 10 degrees.
            await my_servo.move(10)

            # Get the current set angle of the servo.
            pos1 = await my_servo.get_position()

            # Move the servo from its origin to the desired angle of 20 degrees.
            await my_servo.move(20)

            # Get the current set angle of the servo.
            pos2 = await my_servo.get_position()

        Returns:
            int: The current angle of the servo in degrees.

        For more information, see `Servo component <https://docs.viam.com/components/servo/>`_.
        """
        ...

    @abc.abstractmethod
    async def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        """
        Stop the servo. It is assumed that the servo stops immediately.

        ::

            my_servo = Servo.from_robot(robot=robot, name="my_servo")

            # Move the servo from its origin to the desired angle of 10 degrees.
            await my_servo.move(10)

            # Stop the servo. It is assumed that the servo stops moving immediately.
            await my_servo.stop()

        For more information, see `Servo component <https://docs.viam.com/components/servo/>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the servo is currently moving.

        ::

            my_servo = Servo.from_robot(robot=robot, name="my_servo")

            print(my_servo.is_moving())


        Returns:
            bool: Whether the servo is moving.

        For more information, see `Servo component <https://docs.viam.com/components/servo/>`_.
        """
        ...
