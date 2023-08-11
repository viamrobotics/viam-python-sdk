import sys

if sys.version_info >= (3, 9):
    from collections.abc import AsyncIterator
else:
    from typing import AsyncIterator

from typing import Protocol, TypeVar

LogsType = TypeVar("LogsType", covariant=True)


class _LogsStream(Protocol[LogsType]):
    async def next(self) -> LogsType:
        ...

    async def close(self):
        ...

    def __aiter__(self):
        return self

    async def __anext__(self) -> LogsType:
        return await self.next()


class _LogsStreamWithIterator(_LogsStream[LogsType]):
    _stream: AsyncIterator[LogsType]

    def __init__(self, stream: AsyncIterator[LogsType]):
        self._stream = stream

    async def next(self) -> LogsType:
        return await self._stream.__anext__()

    def __aiter__(self):
        return self._stream

    async def __anext__(self) -> LogsType:
        return await self._stream.__anext__()

    async def close(self):
        return await super().close()
