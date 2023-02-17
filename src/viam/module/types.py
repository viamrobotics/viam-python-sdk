from typing import Any, Mapping, Optional, Protocol, runtime_checkable

from viam.components.component_base import ComponentBase
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName


@runtime_checkable
class Reconfigurable(Protocol):
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ComponentBase]):
        ...


@runtime_checkable
class Stoppable(Protocol):
    def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        ...
