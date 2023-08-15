from typing import Any, Mapping, Optional, Protocol, runtime_checkable

from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase


@runtime_checkable
class Reconfigurable(Protocol):
    """The Reconfigurable protocol defines the requirements for making a resource Reconfigurable"""

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        ...


@runtime_checkable
class Stoppable(Protocol):
    """
    The Stoppable protocol defines the requirements for making a resource Stoppable.

    All resources that physically move should be Stoppable.
    """

    def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        ...
