from dataclasses import dataclass
from threading import Lock
from typing import TYPE_CHECKING, Callable, ClassVar, Dict, Generic, Mapping, Type, TypeVar

from grpclib.client import Channel

from viam.errors import DuplicateResourceError, ResourceNotFoundError, ValidationError

from .base import ResourceBase

if TYPE_CHECKING:
    from .rpc_service_base import ResourceRPCServiceBase
    from .types import API, Model, ResourceCreator, Validator

Resource = TypeVar("Resource", bound=ResourceBase)


@dataclass
class ResourceCreatorRegistration:
    """An object representing a resource creator to be registered.

    If creating a custom Resource creator, you should register the creator by creating a ``ResourceCreatorRegistration`` object and
    registering it to the ``Registry``.
    """

    creator: "ResourceCreator"
    """A function that can create a resource given a mapping of dependencies (``ResourceName`` to ``ResourceBase``
    """

    validator: "Validator" = lambda x: ([], [])
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


class Registry:
    """The global registry of robotic parts.

    **NB** The Registry should almost never be used directly

    The Registry keeps track of the types of Resources that are available on robots using this SDK. All the base resource types are
    pre-registered (for example Arm, Motor).

    If you create a new resource type that is not an extension of any of the existing base resource types, then you must register said
    resource using ``Registry.register(...)``.
    """

    _APIS: ClassVar[Dict["API", ResourceRegistration]] = {}
    _RESOURCES: ClassVar[Dict[str, ResourceCreatorRegistration]] = {}
    _lock: ClassVar[Lock] = Lock()

    @classmethod
    def register_api(cls, registration: ResourceRegistration[Resource]):
        """Register a API with the Registry

        Args:
            registration (ResourceRegistration): Object containing registration data for the API

        Raises:
            DuplicateResourceError: Raised if the API to register is already in the registry
            ValidationError: Raised if registration is missing any necessary parameters
        """
        with cls._lock:
            if registration.resource_type.API in cls._APIS:
                raise DuplicateResourceError(str(registration.resource_type.API))

            if registration.resource_type and registration.rpc_service and registration.create_rpc_client:
                cls._APIS[registration.resource_type.API] = registration
            else:
                raise ValidationError("Passed resource registration does not have correct parameters")

    @classmethod
    def register_resource_creator(cls, api: "API", model: "Model", registration: ResourceCreatorRegistration):
        """Register a specific ``Model`` and validator function for the specific resource ``API`` with the Registry

        Args:
            api (API): The API of the resource
            model (Model): The Model of the resource
            registration (ResourceCreatorRegistration): The registration functions of the model

        Raises:
            DuplicateResourceError: Raised if the API and Model pairing is already registered
            ValidationError: Raised if registration does not have creator
        """
        key = f"{api}/{model}"
        with cls._lock:
            if key in cls._RESOURCES:
                raise DuplicateResourceError(key)

            if registration.creator:
                cls._RESOURCES[key] = registration
            else:
                raise ValidationError("A creator function was not provided")

    @classmethod
    def lookup_api(cls, api: "API") -> ResourceRegistration:
        """Lookup and retrieve a registered API by its name

        Args:
            api (str): The API of the resource

        Raises:
            ResourceNotFoundError: Raised if the API is not registered

        Returns:
            ResourceRegistration: The registration object of the resource
        """
        with cls._lock:
            try:
                return cls._APIS[api]
            except KeyError:
                raise ResourceNotFoundError(api.resource_type, api.resource_subtype)

    @classmethod
    def lookup_resource_creator(cls, api: "API", model: "Model") -> "ResourceCreator":
        """Lookup and retrieve a registered resource creator by its API and model

        Args:
            api (API): The API of the resource
            model (Model): The Model of the resource

        Raises:
            ResourceNotFoundError: Raised if the API Model pairing is not registered

        Returns:
            ResourceCreator: The function to create the resource
        """
        with cls._lock:
            try:
                return cls._RESOURCES[f"{api}/{model}"].creator
            except KeyError:
                raise ResourceNotFoundError(api.resource_type, api.resource_subtype)

    @classmethod
    def lookup_validator(cls, api: "API", model: "Model") -> "Validator":
        """Lookup and retrieve a registered validator function by its API and model. If there is none, return None

        Args:
            api (API): The API of the resource
            model (Model): The Model of the resource

        Returns:
            Validator: The function to validate the resource
        """
        try:
            return cls._RESOURCES[f"{api}/{model}"].validator
        except AttributeError:
            return lambda x: ([], [])
        except KeyError:
            raise ResourceNotFoundError(api.resource_type, api.resource_subtype)

    @classmethod
    def REGISTERED_APIS(cls) -> Mapping["API", ResourceRegistration]:
        """The dictionary of all registered resources
        - Key: API of the resource
        - Value: The registration object for the resource

        Returns:
            Mapping[API, ResourceRegistration]: All registered resources
        """
        with cls._lock:
            return cls._APIS.copy()

    @classmethod
    def REGISTERED_RESOURCE_CREATORS(cls) -> Mapping[str, "ResourceCreatorRegistration"]:
        """The dictionary of all registered resources
        - Key: API/model
        - Value: The ResourceCreatorRegistration for the resource

        Returns:
            Mapping[str, ResourceCreatorRegistration]: All registered resources
        """
        with cls._lock:
            return cls._RESOURCES.copy()
