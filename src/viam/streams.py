import sys

if sys.version_info >= (3, 9):
    from collections.abc import AsyncIterator
else:
    from typing import AsyncIterator

from typing import Protocol, TypeVar

StreamType = TypeVar("StreamType", covariant=True)


class Stream(Protocol[StreamType]):
    async def next(self) -> StreamType:
        ...

    def __aiter__(self) -> AsyncIterator:
        return self

    async def __anext__(self) -> StreamType:
        return await self.next()


class StreamReader(Protocol[StreamType]):
    async def read(self) -> StreamType:
        ...


class StreamSource(Protocol[StreamType]):
    async def stream(self) -> Stream[StreamType]:
        ...


class StreamWithIterator(Stream[StreamType]):
    _stream: AsyncIterator[StreamType]

    def __init__(self, stream: AsyncIterator[StreamType]):
        self._stream = stream

    async def next(self) -> StreamType:
        return await self._stream.__anext__()

    def __aiter__(self):
        return self._stream

    async def __anext__(self) -> StreamType:
        return await self._stream.__anext__()
