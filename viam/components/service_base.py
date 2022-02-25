import abc

from viam.components.resource_manager import ResourceManager


class ComponentServiceBase(abc.ABC):
    """
    Base component service.
    All component services must inherit from this class.
    """

    manager: ResourceManager

    def __init__(self, manager: ResourceManager):
        self.manager = manager
