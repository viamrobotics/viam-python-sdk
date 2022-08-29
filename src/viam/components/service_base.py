import abc
import asyncio
from typing import Any, Callable, Coroutine, Generic, Type, TypeVar

try:
    from typing import ParamSpec
except ImportError:
    from typing_extensions import ParamSpec

from viam.components.resource_manager import ResourceManager, ResourceType
from viam.operations import Operation


class ComponentServiceBase(Generic[ResourceType], abc.ABC):
    """
    Base component service.
    All component services must inherit from this class.
    """

    RESOURCE_TYPE = Type

    def __init__(self, manager: ResourceManager):
        self.manager = manager

    def get_component(self, name: str) -> ResourceType:
        """
        Return the component with the given name if it exists in the registry.
        If the component does not exist in the registry,
        this function will raise an error

        Args:
            name (str): Name of the component

        Raises:
            ComponentNotFoundError

        Returns:
            ResourceType: The component
        """
        return self.manager.get_component(self.RESOURCE_TYPE, name)

    P = ParamSpec("P")
    T = TypeVar("T")

    async def _run_with_operation(self, func: Callable[P, Coroutine[Any, Any, T]], *args: P.args, **kwargs: P.kwargs) -> T:
        """Run a component function with an `Operation`.
        Running a function with an Operation will allow the function
        to know if/when the calling task was cancelled and take appropriate action
        (.e.g. stop long running tasks and exit early).

        An example use case is if a gRPC client disconnects after making a request.
        Rather than continue to run a task for a receiver that is no longer there,
        the component can cancel and clean up, saving resources.


        Args:
            func (Callable[..., Coroutine[Any, Any, T]]): The function to be called with an Operation.
                                                          This function MUST accept `**kwargs` or an `operation` parameter

        Returns:
            T: The return of the function
        """
        event = asyncio.Event()
        func_name = func.__qualname__
        arg_names = ", ".join([str(a) for a in args])
        kwarg_names = ", ".join([f"{key}={value}" for (key, value) in kwargs.items()])
        operation = Operation(f"{func_name}({arg_names}{', ' if len(arg_names) else ''}{kwarg_names})", event)
        kwargs["operation"] = operation
        try:
            return await asyncio.shield(func(*args, **kwargs))
        except asyncio.CancelledError:
            event.set()
            raise
