from typing import Dict, List, Type, TypeVar

from viam.proto.common import ResourceName

from ..errors import DuplicateComponentError, ResourceNotFoundError
from .component_base import ComponentBase

ResourceType = TypeVar("ResourceType", bound=ComponentBase)


class ResourceManager:
    """
    Registry containing all components registered to this server.
    """

    components: Dict[ResourceName, ComponentBase]

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
        rnames: Dict[ResourceName, ComponentBase] = {}
        for subtype in component.__class__.mro():
            if subtype is ComponentBase:
                continue
            if hasattr(subtype, "get_resource_name"):
                rn = subtype.get_resource_name(component.name)  # type: ignore
                rnames[rn] = component

        if rnames.keys() & self.components.keys():
            raise DuplicateComponentError(component.name)

        self.components.update(rnames)

    def get_component(self, of_type: Type[ResourceType], name: ResourceName) -> ResourceType:
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

        raise ResourceNotFoundError(name.subtype, name.name)

    def _component_by_name_only(self, name: str) -> ComponentBase:
        for rname, component in self.components.items():
            if rname.name == name:
                return component
        raise ResourceNotFoundError("component", name)
