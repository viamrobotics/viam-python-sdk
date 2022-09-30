import abc

from viam.errors import NotSupportedError

from viam.components.component_base import ComponentBase


class Gripper(ComponentBase):
    """
    Gripper represents a physical robotic gripper.

    This acts as an abstract base class for any drivers representing specific
    gripper implementations. This cannot be used on its own. If the `__init__()` function is
    overridden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def open(self, **kwargs):
        """
        Open the gripper.
        """
        ...

    @abc.abstractmethod
    async def grab(self, **kwargs) -> bool:
        """
        Instruct the gripper to grab.

        Returns:
            bool: Indicates if the gripper grabbed something.
        """
        ...

    @abc.abstractmethod
    async def stop(self, **kwargs):
        """
        Stop the gripper. It is assumed the gripper stops immediately.
        """
        ...

    async def is_moving(self) -> bool:
        """
        Get if the gripper is currently moving.

        Returns:
            bool: Whether the gripper is moving.
        """
        raise NotSupportedError(f"Gripper named {self.name} does not support returning whether it is moving")
