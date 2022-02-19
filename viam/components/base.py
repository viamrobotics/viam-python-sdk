import abc


class ComponentBase(abc.ABC):
    """
    Base component.
    All components must inherit from this class.
    """

    name: str

    def __init__(self, name: str):
        self.name = name


class ComponentServerBase(abc.ABC):
    """
    Base component server.
    All component servers must inherit from this class.
    """
    from viam.components.registry import RegistryManager

    manager: RegistryManager

    def __init__(self, manager: RegistryManager):
        self.manager = manager
