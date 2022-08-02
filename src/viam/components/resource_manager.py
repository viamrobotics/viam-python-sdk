from typing import Dict, List, Type, TypeVar

from .component_base import ComponentBase
from ..errors import ComponentNotFoundError, DuplicateComponentError


ResourceType = TypeVar("ResourceType", bound=ComponentBase)


class ResourceManager:
    """
    Registry containing all components registered to this server.
    """

    components: Dict[str, ComponentBase]

    def __init__(self, components: List[ComponentBase] = []) -> None:
        self.components = {}
        for component in components:
            self.register(component)

    def register(self, component: ComponentBase):
        """
        Register a new component with the registry.
        Components may not have the same name.

        Raises:
            DuplicateComponentError: Error if attempting to register component
                                     with the name of an existing component

        Args:
            component (ComponentBase): The component to register
        """
        if component.name in self.components:
            raise DuplicateComponentError(component.name)
        self.components[component.name] = component

    def get_component(self, of_type: Type[ResourceType], name: str) -> ResourceType:
        """
        Return a component from the registry.

        Args:
            of_type (Type[ResourceType]): The type of the component
            name (str): The name of the component

        Raises:
            ComponentNotFoundError: Error if component with the given type
                                    and name does not exist in the registry

        Returns:
            ResourceType: The component
        """
        component = self.components.get(name, None)
        if component and isinstance(component, of_type):
            return component

        class_name = str(of_type)
        if len(class_name.split(".")) > 2:
            class_name = class_name.split(".")[2]
        raise ComponentNotFoundError(class_name, name)
