import abc
from typing import Any, Dict, Final, List, Optional

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase


class Gantry(ComponentBase):
    """
    Gantry represents a physical Gantry and can be used for controlling gantries of N axes.

    This acts as an abstract base class for any drivers representing specific
    gantry implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.gantry import Gantry

    For more information, see `Gantry component <https://docs.viam.com/components/gantry/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gantry"
    )

    @abc.abstractmethod
    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        """
        Get the positions of the axes of the gantry in millimeters.

        ::

            my_gantry = Gantry.from_robot(robot=robot, name="my_gantry")

            # Get the current positions of the axes of the gantry in millimeters.
            positions = await my_gantry.get_position()

        Returns:
            List[float]: A list of the position of the axes of the gantry in millimeters.

        For more information, see `Gantry component <https://docs.viam.com/components/gantry/>`_.
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        positions: List[float],
        speeds: List[float],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move the axes of the gantry to the desired positions (mm) at the requested speeds (mm/sec).

        ::

            my_gantry = Gantry.from_robot(robot=robot, name="my_gantry")

            # Create a list of positions for the axes of the gantry to move to. Assume in
            # this example that the gantry is multi-axis, with 3 axes.
            examplePositions = [1, 2, 3]

            exampleSpeeds = [3, 9, 12]

            # Move the axes of the gantry to the positions specified.
            await my_gantry.move_to_position(
                positions=examplePositions, speeds=exampleSpeeds)

        Args:
            positions (List[float]): A list of positions for the axes of the gantry to move to, in millimeters.
            speeds (List[float]): A list of speeds in millimeters per second for the gantry to move at respective to each axis.

        For more information, see `Gantry component <https://docs.viam.com/components/gantry/>`_.
        """
        ...

    @abc.abstractmethod
    async def home(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> bool:
        """
        Run the homing sequence of the gantry to re-calibrate the axes with respect to the limit switches.

        ::

            my_gantry = Gantry.from_robot(robot=robot, name="my_gantry")

            await my_gantry.home()

        Returns:
            bool: Whether the gantry has run the homing sequence successfully.

        For more information, see `Gantry component <https://docs.viam.com/components/gantry/>`_.
        """

    @abc.abstractmethod
    async def get_lengths(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        """
        Get the lengths of the axes of the gantry in millimeters.

        ::

            my_gantry = Gantry.from_robot(robot=robot, name="my_gantry")

            # Get the lengths of the axes of the gantry in millimeters.
            lengths_mm = await my_gantry.get_lengths()

        Returns:
            List[float]: A list of the lengths of the axes of the gantry in millimeters.

        For more information, see `Gantry component <https://docs.viam.com/components/gantry/>`_.
        """
        ...

    @abc.abstractmethod
    async def stop(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        """
        Stop all motion of the gantry. It is assumed that the gantry stops immediately.

        ::

            my_gantry = Gantry.from_robot(robot=robot, name="my_gantry")

            # Stop all motion of the gantry. It is assumed that the gantry stops
            # immediately.
            await my_gantry.stop()

        For more information, see `Gantry component <https://docs.viam.com/components/gantry/>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the gantry is currently moving.

        ::

            my_gantry = Gantry.from_robot(robot=robot, name="my_gantry")

            # Stop all motion of the gantry. It is assumed that the
            # gantry stops immediately.
            await my_gantry.stop()

            # Print if the gantry is currently moving.
            print(my_gantry.is_moving())

        Returns:
            bool: Whether the gantry is moving.

        For more information, see `Gantry component <https://docs.viam.com/components/gantry/>`_.
        """
        ...
