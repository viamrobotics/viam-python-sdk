from typing import Any, Mapping, Optional, Protocol, runtime_checkable


@runtime_checkable
class Reconfigurable(Protocol):
    """The Reconfigurable protocol defines the requirements for making a resource Reconfigurable"""


@runtime_checkable
class Stoppable(Protocol):
    """
    The Stoppable protocol defines the requirements for making a resource Stoppable.

    All resources that physically move should be Stoppable.
    """

    def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs): ...
