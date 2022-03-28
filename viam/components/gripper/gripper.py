import abc

from viam.components.component_base import ComponentBase


class Gripper(ComponentBase):
    """
    Abstract representation of a physical robotic gripper
    """

    @abc.abstractmethod
    async def open(self):
        """
        Open the gripper
        """
        ...

    @abc.abstractmethod
    async def grab(self) -> bool:
        """
        Instruct the gripper to grab.

        Returns:
            bool: If the gripper grabbed something
        """
        ...
