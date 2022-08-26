import asyncio
import time
from typing_extensions import Self
from uuid import UUID, uuid4


class Operation:
    id: UUID
    method: str
    time_started: float
    _cancel_event: asyncio.Event
    _cancelled: bool

    def __init__(self, method: str, cancel_event: asyncio.Event) -> None:
        self.id = uuid4()
        self.method = method
        self.time_started = time.time()
        self._cancel_event = cancel_event
        self._cancelled = False

    def is_cancelled(self) -> bool:
        if self._cancelled:
            return self._cancelled
        if self._cancel_event.is_set():
            self._cancelled = True
            return self._cancelled
        return False

    def complete(self):
        if self.is_cancelled():
            raise asyncio.CancelledError

    def __str__(self) -> str:
        return f"Operation {self.id} : {self.method}"

    @classmethod
    def _noop(cls) -> Self:
        """Obtain a noop Operation.
        This operation will always return `False` for `is_cancelled()`
        """
        return cls("noop-operation", asyncio.Event())
