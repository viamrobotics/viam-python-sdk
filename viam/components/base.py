import abc


class ComponentBase(abc.ABC):
    """
    Base component.
    All components must inherit from this class.
    """

    name: str

    def __init__(self, name: str):
        self.name = name
