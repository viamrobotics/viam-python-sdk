from ..component_base import ComponentBase


class Generic(ComponentBase):
    """
    Generic component, which represents any type of component that can executs arbitrary commands

    This acts as an abstract base class for any drivers representing generic components.
    This cannot be used on its own. If the `__init__()` function is overriden, it must call the `super().__init__()` function.
    """
