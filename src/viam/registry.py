from dataclasses import dataclass
from typing import Any, Callable, Coroutine, Dict, Generic, Mapping, Type, TypeVar

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel

from viam.components.component_base import ComponentBase
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError, DuplicateComponentError
from viam.proto.robot import Status

Component = TypeVar("Component", bound=ComponentBase)


async def default_create_status(component: ComponentBase) -> Status:
    return Status(name=component.get_resource_name(component.name), status=Struct())


@dataclass
class ComponentRegistration(Generic[Component]):
    """An object representing a component to be registered.

    This object is generic over the component, and it includes various functionality for the component, such as creating its RPC client
    or status.

    If creating a custom Component type, you should register the component by creating a `ComponentRegistration` object and registering it
    to the `Registry`.
    """

    component_type: Type[Component]
    """The type of the Component to be registered
    """

    name: str
    """The name of the Component type
    """

    rpc_service: Type[ComponentServiceBase]
    """The RPC service of the component. This must extend from `ComponentServiceBase`
    """

    create_rpc_client: Callable[[str, Channel], Component]
    """A function that will create the RPC client for this component
    """

    create_status: Callable[[Component], Coroutine[Any, Any, Status]] = default_create_status
    """A function to create a Status object for this component.

    If the Component does not provide a custom status type, the default implementation can be used.
    """


class Registry:
    """The global registry of robotic parts.

    **NB** The Registry should almost never be used directly

    The Registry keeps track of the types of Components that are available on robots using this SDK. All the base component types are
    pre-registered (e.g. Arm, Motor).

    If you create a new component type that is not an extension of any of the existing base component types, then you must register said
    component using `Registry.register(...)`.
    """

    _COMPONENTS: Dict[str, ComponentRegistration] = {}

    @classmethod
    def register(cls, registration: ComponentRegistration):
        """Register a Component with the Registry

        Args:
            registration (ComponentRegistration): Object containing registration data for the component

        Raises:
            DuplicateComponentError: Raised if the Component to register is already in the registry
        """
        if registration.name in cls._COMPONENTS:
            raise DuplicateComponentError(registration.name)
        cls._COMPONENTS[registration.name] = registration

    @classmethod
    def lookup(cls, component_name: str) -> ComponentRegistration:
        """Lookup and retrieve a registered component by its name

        Args:
            component_name (str): The name of the component

        Raises:
            ComponentNotFoundError: Raised if the component type is not registered

        Returns:
            ComponentRegistration: The registration object of the component
        """
        try:
            return cls._COMPONENTS[component_name]
        except KeyError:
            raise ComponentNotFoundError("component", component_name)

    @classmethod
    @property
    def REGISTERED_COMPONENTS(cls) -> Mapping[str, ComponentRegistration]:
        """The dictionary of all registered components
        - Key: Name of the component type
        - Value: The registration object for the component type

        Returns:
            Mapping[str, ComponentRegistration]: All registered components
        """
        return cls._COMPONENTS.copy()
