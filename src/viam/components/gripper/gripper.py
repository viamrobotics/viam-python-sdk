import abc
from typing import Any, Dict, Final, Optional

from viam.components.component_base import ComponentBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype


class Gripper(ComponentBase):
    """
    Gripper represents a physical robotic gripper.

    This acts as an abstract base class for any drivers representing specific
    gripper implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.gripper import Gripper

    For more information, see `Gripper component <https://docs.viam.com/components/gripper/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gripper"
    )

    @abc.abstractmethod
    async def open(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Open the gripper.

        ::

            my_gripper = Gripper.from_robot(robot=robot, name="my_gripper")

            # Open the gripper.
            await my_gripper.open()

        For more information, see `Gripper component <https://docs.viam.com/components/gripper/>`_.
        """
        ...

    @abc.abstractmethod
    async def grab(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> bool:
        """
        Instruct the gripper to grab.

        ::

            my_gripper = Gripper.from_robot(robot=robot, name="my_gripper")

            # Grab with the gripper.
            grabbed = await my_gripper.grab()

        Returns:
            bool: Indicates if the gripper grabbed something.

        For more information, see `Gripper component <https://docs.viam.com/components/gripper/>`_.
        """
        ...

    @abc.abstractmethod
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Stop the gripper. It is assumed the gripper stops immediately.

        ::

            my_gripper = Gripper.from_robot(robot=robot, name="my_gripper")

            # Stop the gripper.
            await my_gripper.stop()

        For more information, see `Gripper component <https://docs.viam.com/components/gripper/>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the gripper is currently moving.

        ::

            my_gripper = Gripper.from_robot(robot=robot, name="my_gripper")

            # Check whether the gripper is currently moving.
            moving = await my_gripper.is_moving()
            print('Moving:', moving)

        Returns:
            bool: Whether the gripper is moving.

        For more information, see `Gripper component <https://docs.viam.com/components/gripper/>`_.
        """
        ...
