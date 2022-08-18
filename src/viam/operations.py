import asyncio
import time
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

    async def is_cancelled(self) -> bool:
        if self._cancelled:
            return self._cancelled
        if self._cancel_event.is_set():
            self._cancelled = True
            return self._cancelled
        try:
            await asyncio.sleep(0)
            return False
        except asyncio.CancelledError:
            self._cancelled = True
            return True

    async def complete(self):
        if await self.is_cancelled():
            raise asyncio.CancelledError

    def __str__(self) -> str:
        return f"Operation {self.id} : {self.method}"
