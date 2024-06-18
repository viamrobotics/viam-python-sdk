import asyncio
import functools
import sys
import time
from typing import Any, Callable, Coroutine, Mapping, Optional, TypeVar, cast
from uuid import UUID, uuid4

from typing_extensions import Self

if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec


class Operation:
    """An Operation represents a running operation.

    Every request made to a robot's components will create a new Operation on the server. For custom components built with this python-sdk,
    you should check whether the operation has been cancelled to prevent long-running tasks from leaking.
    """

    ARG_NAME = "viam_operation"

    id: UUID
    method: str
    time_started: float
    _cancel_event: asyncio.Event
    _cancelled: bool

    def __init__(self, method: str, cancel_event: asyncio.Event, opid: Optional[UUID] = None) -> None:
        self.id = uuid4() if opid is None else opid
        self.method = method
        self.time_started = time.time()
        self._cancel_event = cancel_event
        self._cancelled = False

    async def is_cancelled(self) -> bool:
        if self._cancelled:
            return self._cancelled
        if self._cancel_event.is_set():
            self._cancelled = True
            return self._cancelled
        try:
            await asyncio.sleep(0)
        except asyncio.CancelledError:
            self._cancelled = True
            return self._cancelled
        return False

    def __str__(self) -> str:
        return f"Operation {self.id} : {self.method}"

    @classmethod
    def _noop(cls) -> Self:
        """Obtain a noop Operation.
        This operation will always return ``False`` for ``is_cancelled()``
        """
        return cls("noop-operation", asyncio.Event())


P = ParamSpec("P")
T = TypeVar("T")

METADATA_KEY = "opid"


def opid_from_metadata(metadata: Optional[Mapping[str, str]]) -> Optional[UUID]:
    if metadata is None:
        return None

    opid = metadata.get(METADATA_KEY)
    if opid is None:
        return None

    return UUID(opid)


def run_with_operation(func: Callable[P, Coroutine[Any, Any, T]]) -> Callable[P, Coroutine[Any, Any, T]]:
    """Run a component function with an ``Operation``.
    Running a function with an Operation will allow the function
    to know if/when the calling task was cancelled and take appropriate action
    (for example stop long running tasks and exit early).

    If a timeout is provided to the function, the operation will cancel when the timeout is reached.

    An example use case is if a gRPC client disconnects after making a request.
    Rather than continue to run a task for a receiver that is no longer there,
    the component can cancel and clean up, saving resources.

    Args:
        func (Callable[..., Coroutine[Any, Any, T]]): The function to be called with an Operation.
                                                      This function MUST accept ``**kwargs``
                                                      or a parameter whose name is equal the value of ``Operation.ARG_NAME``

    Returns:
        T: The return of the function
    """

    @functools.wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        event = asyncio.Event()
        func_name = func.__qualname__
        arg_names = ", ".join([str(a) for a in args])
        kwarg_names = ", ".join([f"{key}={value}" for (key, value) in kwargs.items()])
        method = f"{func_name}({arg_names}{', ' if len(arg_names) else ''}{kwarg_names})"
        opid = opid_from_metadata(kwargs.get("metadata"))  # type: ignore
        operation = Operation(method, event, opid=opid)
        kwargs[Operation.ARG_NAME] = operation
        timeout = kwargs.get("timeout", None)
        timer: Optional[asyncio.TimerHandle] = None
        if timeout:
            timeout = cast(float, timeout)
            timer = asyncio.get_running_loop().call_later(timeout, event.set)
        try:
            return await asyncio.shield(func(*args, **kwargs))
        except asyncio.CancelledError:
            event.set()
            raise
        finally:
            if timer:
                timer.cancel()

    return wrapper
