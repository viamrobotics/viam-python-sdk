import abc
from typing import TYPE_CHECKING, Generic, Type

from viam.components.component_base import ComponentBase
from viam.errors import ResourceNotFoundError
from viam.resource.manager import ResourceType
from viam.rpc.types import RPCServiceBase
from viam.services.service_base import ServiceBase

from .base import ResourceBase

if TYPE_CHECKING:
    from viam.resource.manager import ResourceManager


class ResourceRPCServiceBase(abc.ABC, RPCServiceBase, Generic[ResourceType]):
    """
    Base RPC service for a resource.
    All resource RPC services must inherit from this class.
    """

    RESOURCE_TYPE = Type
    manager: "ResourceManager"

    def __init__(self, manager: "ResourceManager"):
        self.manager = manager

    def get_resource(self, name: str) -> ResourceType:
        """
        Return the resource with the given name if it exists in the registry.
        If the resource does not exist in the registry,
        this function will raise an error

        Args:
            name (str): Name of the resource

        Raises:
            GRPCError with the status code Status.NOT_FOUND

        Returns:
            ResourceType: The resource
        """
        try:
            if self.RESOURCE_TYPE == ComponentBase or self.RESOURCE_TYPE == ResourceBase or self.RESOURCE_TYPE == ServiceBase:
                return self.manager._resource_by_name_only(name)  # type: ignore
            return self.manager.get_resource(self.RESOURCE_TYPE, self.RESOURCE_TYPE.get_resource_name(name))  # type: ignore
        except ResourceNotFoundError as e:
            raise e.grpc_error
