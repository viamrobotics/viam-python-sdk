import abc
from typing import Final, List, Mapping, Optional

from viam.proto.app.robot import ComponentConfig
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE
from viam.utils import ValueTypes

from ..service_base import ServiceBase


class Discovery(ServiceBase):
    """
    Discovery represents a Discovery service.

    This acts as an abstract base class for any drivers representing specific
    discovery implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "discovery"
    )

    @abc.abstractmethod
    async def discover_resources(
        self,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> List[ComponentConfig]:
        """Get all component configs of discovered resources on a machine

        ::

            my_discovery = DiscoveryClient.from_robot(machine, "my_discovery")

            # Get the discovered resources
            result = await my_discovery.discover_resources(
                "my_discovery",
            )
            discoveries = result.discoveries

        Args:
            name (str): The name of the discover service

        Returns:
            List[ComponentConfig]: A list of ComponentConfigs that describe
            the components found by a discover service

        """
        ...
