import abc

from viam.components.component_base import ComponentBase


class Gripper(ComponentBase):
    """
    Gripper represents a physical robotic gripper.

    This acts as an abstract base class for any drivers representing specific 
    gripper implementations. This cannot be used on its own. If the `__init__()` function is
    overriden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def open(self):
        """
        Open the gripper.
        """
        ...

    @abc.abstractmethod
    async def grab(self) -> bool:
        """
        Instruct the gripper to grab.

        Returns:
            bool: Indicates if the gripper grabbed something.
        """
        ...
