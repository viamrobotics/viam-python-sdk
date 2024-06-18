from dataclasses import dataclass
from threading import Lock
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Coroutine, Dict, Generic, Mapping, Type, TypeVar

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel

from viam.errors import DuplicateResourceError, ResourceNotFoundError, ValidationError
from viam.proto.robot import Status

from .base import ResourceBase

if TYPE_CHECKING:
    from .rpc_service_base import ResourceRPCServiceBase
    from .types import Model, ResourceCreator, Subtype, Validator

Resource = TypeVar("Resource", bound=ResourceBase)


async def default_create_status(resource: ResourceBase) -> Status:
    return Status(name=resource.get_resource_name(resource.name), status=Struct())


@dataclass
class ResourceCreatorRegistration:
    """An object representing a resource creator to be registered.

    If creating a custom Resource creator, you should register the creator by creating a ``ResourceCreatorRegistration`` object and
    registering it to the ``Registry``.
    """

    creator: "ResourceCreator"
    """A function that can create a resource given a mapping of dependencies (``ResourceName`` to ``ResourceBase``
    """

    validator: "Validator" = lambda x: []
    """A function that can validate a resource and return implicit dependencies.

    If called without a validator function, default to a function returning an empty Sequence
    """


@dataclass
class ResourceRegistration(Generic[Resource]):
    """An object representing a resource to be registered.

    This object is generic over the ``ResourceBase``, and it includes various functionality for the resource,
    such as creating its RPC client or status.

    If creating a custom Resource type, you should register the resource by creating a ``ResourceRegistration`` object and registering it
    to the ``Registry``.
    """

    resource_type: Type[Resource]
    """The type of the Resource to be registered
    """

    rpc_service: Type["ResourceRPCServiceBase"]
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

    The Registry keeps track of the types of Resources that are available on robots using this SDK. All the base resource types are
    pre-registered (for example Arm, Motor).

    If you create a new resource type that is not an extension of any of the existing base resource types, then you must register said
    resource using ``Registry.register(...)``.
    """

    _SUBTYPES: ClassVar[Dict["Subtype", ResourceRegistration]] = {}
    _RESOURCES: ClassVar[Dict[str, ResourceCreatorRegistration]] = {}
    _lock: ClassVar[Lock] = Lock()

    @classmethod
    def register_subtype(cls, registration: ResourceRegistration[Resource]):
        """Register a Subtype with the Registry

        Args:
            registration (ResourceRegistration): Object containing registration data for the subtype

        Raises:
            DuplicateResourceError: Raised if the Subtype to register is already in the registry
            ValidationError: Raised if registration is missing any necessary parameters
        """
        with cls._lock:
            if registration.resource_type.SUBTYPE in cls._SUBTYPES:
                raise DuplicateResourceError(str(registration.resource_type.SUBTYPE))

            if registration.resource_type and registration.rpc_service and registration.create_rpc_client:
                cls._SUBTYPES[registration.resource_type.SUBTYPE] = registration
            else:
                raise ValidationError("Passed resource registration does not have correct parameters")

    @classmethod
    def register_resource_creator(cls, subtype: "Subtype", model: "Model", registration: ResourceCreatorRegistration):
        """Register a specific ``Model`` and validator function for the specific resource ``Subtype`` with the Registry

        Args:
            subtype (Subtype): The Subtype of the resource
            model (Model): The Model of the resource
            registration (ResourceCreatorRegistration): The registration functions of the model

        Raises:
            DuplicateResourceError: Raised if the Subtype and Model pairing is already registered
            ValidationError: Raised if registration does not have creator
        """
        key = f"{subtype}/{model}"
        with cls._lock:
            if key in cls._RESOURCES:
                raise DuplicateResourceError(key)

            if registration.creator:
                cls._RESOURCES[key] = registration
            else:
                raise ValidationError("A creator function was not provided")

    @classmethod
    def lookup_subtype(cls, subtype: "Subtype") -> ResourceRegistration:
        """Lookup and retrieve a registered Subtype by its name

        Args:
            subtype (str): The subtype of the resource

        Raises:
            ResourceNotFoundError: Raised if the Subtype is not registered

        Returns:
            ResourceRegistration: The registration object of the resource
        """
        with cls._lock:
            try:
                return cls._SUBTYPES[subtype]
            except KeyError:
                raise ResourceNotFoundError(subtype.resource_type, subtype.resource_subtype)

    @classmethod
    def lookup_resource_creator(cls, subtype: "Subtype", model: "Model") -> "ResourceCreator":
        """Lookup and retrieve a registered resource creator by its subtype and model

        Args:
            subtype (Subtype): The Subtype of the resource
            model (Model): The Model of the resource

        Raises:
            ResourceNotFoundError: Raised if the Subtype Model pairing is not registered

        Returns:
            ResourceCreator: The function to create the resource
        """
        with cls._lock:
            try:
                return cls._RESOURCES[f"{subtype}/{model}"].creator
            except KeyError:
                raise ResourceNotFoundError(subtype.resource_type, subtype.resource_subtype)

    @classmethod
    def lookup_validator(cls, subtype: "Subtype", model: "Model") -> "Validator":
        """Lookup and retrieve a registered validator function by its subtype and model. If there is none, return None

        Args:
            subtype (Subtype): The Subtype of the resource
            model (Model): The Model of the resource

        Returns:
            Validator: The function to validate the resource
        """
        try:
            return cls._RESOURCES[f"{subtype}/{model}"].validator
        except AttributeError:
            return lambda x: []
        except KeyError:
            raise ResourceNotFoundError(subtype.resource_type, subtype.resource_subtype)

    @classmethod
    def REGISTERED_SUBTYPES(cls) -> Mapping["Subtype", ResourceRegistration]:
        """The dictionary of all registered resources
        - Key: Subtype of the resource
        - Value: The registration object for the resource

        Returns:
            Mapping[Subtype, ResourceRegistration]: All registered resources
        """
        with cls._lock:
            return cls._SUBTYPES.copy()

    @classmethod
    def REGISTERED_RESOURCE_CREATORS(cls) -> Mapping[str, "ResourceCreatorRegistration"]:
        """The dictionary of all registered resources
        - Key: subtype/model
        - Value: The ResourceCreatorRegistration for the resource

        Returns:
            Mapping[str, ResourceCreatorRegistration]: All registered resources
        """
        with cls._lock:
            return cls._RESOURCES.copy()
