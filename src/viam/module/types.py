from typing import Any, Mapping, Optional, Protocol, runtime_checkable
import warnings


@runtime_checkable
class Reconfigurable(Protocol):
    """The Reconfigurable protocol defines the requirements for making a resource Reconfigurable"""
    def __init_subclass__(*args, **kwargs):
        warnings.warn("Reconfigure is deprecated, and resources will always rebuild. It is not necessary to implement Reconfigurable.", DeprecationWarning, stacklevel=2)


@runtime_checkable
class Stoppable(Protocol):
    """
    The Stoppable protocol defines the requirements for making a resource Stoppable.

    All resources that physically move should be Stoppable.
    """

    def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs): ...
