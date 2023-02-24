from typing import Any, Mapping, Optional, Protocol, runtime_checkable

from viam.components.component_base import ComponentBase
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName


@runtime_checkable
class Reconfigurable(Protocol):
    """The Reconfigurable protocol defines the requirements for making a resource Reconfigurable"""

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ComponentBase]):
        ...


@runtime_checkable
class Stoppable(Protocol):
    """The Stoppable protocol defines the requirements for making a resource Stoppable.

    All resources that physically move should be Stoppable.
    """

    def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        ...
