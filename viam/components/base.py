import abc


class ComponentBase(abc.ABC):
    """
    Base component.
    All components must inherit from this class.
    """

    name: str

    def __init__(self, name: str):
        self.name = name


class ComponentServiceBase(abc.ABC):
    """
    Base component service.
    All component services must inherit from this class.
    """
    from viam.components.resource_manager import ResourceManager

    manager: ResourceManager

    def __init__(self, manager: ResourceManager):
        self.manager = manager
