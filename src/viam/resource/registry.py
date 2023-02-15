from dataclasses import dataclass
from typing import Any, Callable, Coroutine, Dict, Generic, Mapping, Type, TypeVar
from threading import Lock

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel

from viam.components.component_base import ComponentBase
from viam.components.service_base import ComponentServiceBase
from viam.errors import DuplicateResourceError, ResourceNotFoundError
from viam.proto.robot import Status

from .types import Subtype, Model, ComponentCreator

Component = TypeVar("Component", bound=ComponentBase)


async def default_create_status(component: ComponentBase) -> Status:
    return Status(name=component.get_resource_name(component.name), status=Struct())


@dataclass
class ComponentRegistration(Generic[Component]):
    """An object representing a component to be registered.

    This object is generic over the component, and it includes various functionality for the component, such as creating its RPC client
    or status.

    If creating a custom Component type, you should register the component by creating a ``ComponentRegistration`` object and registering it
    to the ``Registry``.
    """

    component_type: Type[Component]
    """The type of the Component to be registered
    """

    rpc_service: Type[ComponentServiceBase]
    """The RPC service of the component. This must extend from ``ComponentServiceBase``
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
    component using ``Registry.register(...)``.
    """

    _SUBTYPES: Dict[Subtype, ComponentRegistration] = {}
    _COMPONENTS: Dict[str, ComponentCreator]
    _lock: Lock = Lock()

    @classmethod
    def register_subtype(cls, registration: ComponentRegistration[Component]):
        """Register a Subtype with the Registry

        Args:
            registration (ComponentRegistration): Object containing registration data for the subtype

        Raises:
            DuplicateResourceError: Raised if the Subtype to register is already in the registry
        """
        with cls._lock:
            if registration.component_type.SUBTYPE in cls._SUBTYPES:
                raise DuplicateResourceError(str(registration.component_type.SUBTYPE))
            cls._SUBTYPES[registration.component_type.SUBTYPE] = registration

    @classmethod
    def register_component(cls, subtype: Subtype, model: Model, component: ComponentCreator):
        """Register a specific ```Model``` for the specific ```Subtype``` with the Registry

        Args:
            subtype (Subtype): The Subtype of the component
            model (Model): The Model of the component
            component (ComponentCreator): A function that can create a component given a mapping of dependencies (```ResourceName``` to
                                          ```ComponentBase```)

        Raises:
            ResourceNotFoundError: _description_

        Returns:
            _type_: _description_
        """

    @classmethod
    def lookup(cls, subtype: Subtype) -> ComponentRegistration:
        """Lookup and retrieve a registered component by its name

        Args:
            component_name (str): The name of the component

        Raises:
            ComponentNotFoundError: Raised if the component type is not registered

        Returns:
            ComponentRegistration: The registration object of the component
        """
        with cls._lock:
            try:
                return cls._SUBTYPES[subtype]
            except KeyError:
                raise ResourceNotFoundError(subtype.resource_type, subtype.resource_subtype)

    @classmethod
    def REGISTERED_RESOURCES(cls) -> Mapping[Subtype, ComponentRegistration]:
        """The dictionary of all registered resources
        - Key: Subtype of the resource
        - Value: The registration object for the resource

        Returns:
            Mapping[Subtype, ComponentRegistration]: All registered resources
        """
        with cls._lock:
            return cls._SUBTYPES.copy()
