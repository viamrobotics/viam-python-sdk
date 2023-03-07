from dataclasses import dataclass
from threading import Lock
from typing import (
    Any,
    Callable,
    ClassVar,
    Coroutine,
    Dict,
    Generic,
    Mapping,
    Type,
    TypeVar,
)

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel

from viam.errors import DuplicateResourceError, ResourceNotFoundError
from viam.proto.robot import Status
from viam.rpc.types import RPCServiceBase

from .types import ComponentCreator, Model, ResourceBase, Subtype

Resource = TypeVar("Resource", bound=ResourceBase)


async def default_create_status(resource: ResourceBase) -> Status:
    return Status(name=resource.get_resource_name(resource.name), status=Struct())


@dataclass
class ResourceRegistration(Generic[Resource]):
    """An object representing a resource to be registered.

    This object is generic over the ``ResourceBase``, and it includes various functionality for the resource,
    such as creating its RPC client or status.

    If creating a custom Resource type, you should register the resource by creating a ``ResourceRegistration`` object and registering it
    to the ``Registry``.
    """

    component_type: Type[Resource]
    """The type of the Resource to be registered
    """

    rpc_service: Type[RPCServiceBase]
    """The type of the RPC service of the resource. This must extend from ``RPCServiceBase``
    """

    create_rpc_client: Callable[[str, Channel], Resource]
    """A function that will create the RPC client for this resource
    """

    create_status: Callable[[Resource], Coroutine[Any, Any, Status]] = default_create_status
    """A function to create a Status object for this resource.

    If the resource does not provide a custom status type, the default implementation can be used.
    """


class Registry:
    """The global registry of robotic parts.

    **NB** The Registry should almost never be used directly

    The Registry keeps track of the types of Components that are available on robots using this SDK. All the base component types are
    pre-registered (e.g. Arm, Motor).

    If you create a new component type that is not an extension of any of the existing base component types, then you must register said
    component using ``Registry.register(...)``.
    """

    _SUBTYPES: ClassVar[Dict[Subtype, ResourceRegistration]] = {}
    _COMPONENTS: ClassVar[Dict[str, ComponentCreator]] = {}
    _lock: ClassVar[Lock] = Lock()

    @classmethod
    def register_subtype(cls, registration: ResourceRegistration[Resource]):
        """Register a Subtype with the Registry

        Args:
            registration (ResourceRegistration): Object containing registration data for the subtype

        Raises:
            DuplicateResourceError: Raised if the Subtype to register is already in the registry
        """
        with cls._lock:
            if registration.component_type.SUBTYPE in cls._SUBTYPES:
                raise DuplicateResourceError(str(registration.component_type.SUBTYPE))
            cls._SUBTYPES[registration.component_type.SUBTYPE] = registration

    @classmethod
    def register_component_model(cls, subtype: Subtype, model: Model, component: ComponentCreator):
        """Register a specific ```Model``` for the specific ```Subtype``` with the Registry

        Args:
            subtype (Subtype): The Subtype of the component
            model (Model): The Model of the component
            component (ComponentCreator): A function that can create a component given a mapping of dependencies (```ResourceName``` to
                                          ```ComponentBase```)

        Raises:
            DuplicateResourceError: Raised if the Subtype and Model pairing is already registered
        """
        key = f"{subtype}/{model}"
        with cls._lock:
            if key in cls._COMPONENTS:
                raise DuplicateResourceError(key)
            cls._COMPONENTS[key] = component

    @classmethod
    def lookup_subtype(cls, subtype: Subtype) -> ResourceRegistration:
        """Lookup and retrieve a registered Subtype by its name

        Args:
            subtype (str): The subtype of the resource

        Raises:
            ResourceNotFoundError: Raised if the Subtype is not registered

        Returns:
            ComponentRegistration: The registration object of the component
        """
        with cls._lock:
            try:
                return cls._SUBTYPES[subtype]
            except KeyError:
                raise ResourceNotFoundError(subtype.resource_type, subtype.resource_subtype)

    @classmethod
    def lookup_component(cls, subtype: Subtype, model: Model) -> ComponentCreator:
        """Lookup and retrieve a registered component by its name

        Args:
            subtype (Subtype): The Subtype of the component
            model (Model): The Model of the component

        Raises:
            ResourceNotFoundError: Raised if the Subtype Model pairing is not registered

        Returns:
            ComponentCreator: The function to create the component
        """
        with cls._lock:
            try:
                return cls._COMPONENTS[f"{subtype}/{model}"]
            except KeyError:
                raise ResourceNotFoundError(subtype.resource_type, subtype.resource_subtype)

    @classmethod
    def REGISTERED_RESOURCES(cls) -> Mapping[Subtype, ResourceRegistration]:
        """The dictionary of all registered resources
        - Key: Subtype of the resource
        - Value: The registration object for the resource

        Returns:
            Mapping[Subtype, ComponentRegistration]: All registered resources
        """
        with cls._lock:
            return cls._SUBTYPES.copy()

    @classmethod
    def REGISTERED_COMPONENTS(cls) -> Mapping[str, ComponentCreator]:
        with cls._lock:
            return cls._COMPONENTS.copy()
