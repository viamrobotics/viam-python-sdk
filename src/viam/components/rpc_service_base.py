import abc
from typing import Generic, Type

from viam.components.component_base import ComponentBase
from viam.resource.manager import ResourceManager, ResourceType
from viam.rpc.types import RPCServiceBase


class ComponentRPCServiceBase(abc.ABC, RPCServiceBase, Generic[ResourceType]):
    """
    Base component service.
    All component services must inherit from this class.
    """

    RESOURCE_TYPE = Type
    manager: ResourceManager

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
        if self.RESOURCE_TYPE == ComponentBase:
            return self.manager._resource_by_name_only(name)  # type: ignore
        return self.manager.get_resource(self.RESOURCE_TYPE, self.RESOURCE_TYPE.get_resource_name(name))  # type: ignore
