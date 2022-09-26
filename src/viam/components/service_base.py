import abc
from typing import Generic, Type

from viam.components.resource_manager import ResourceManager, ResourceType


class ComponentServiceBase(Generic[ResourceType], abc.ABC):
    """
    Base component service.
    All component services must inherit from this class.
    """

    RESOURCE_TYPE = Type

    def __init__(self, manager: ResourceManager):
        self.manager = manager

    def get_component(self, name: str) -> ResourceType:
        """
        Return the component with the given name if it exists in the registry.
        If the component does not exist in the registry,
        this function will raise an error

        Args:
            name (str): Name of the component

        Raises:
            ComponentNotFoundError

        Returns:
            ResourceType: The component
        """
        return self.manager.get_component(self.RESOURCE_TYPE, name)
