import sys

if sys.version_info >= (3, 9):
    from collections.abc import AsyncIterator
else:
    from typing import AsyncIterator

from typing import Protocol, TypeVar

MediaType = TypeVar("MediaType", covariant=True)
StreamType = TypeVar("StreamType", covariant=True)


class Stream(Protocol[StreamType]):
    async def next(self) -> StreamType:
        ...

    def __aiter__(self) -> AsyncIterator:
        return self

    async def __anext__(self) -> StreamType:
        return await self.next()


class MediaReader(Protocol[MediaType]):
    async def read(self) -> MediaType:
        ...


class MediaSource(Protocol[MediaType]):
    async def stream(self) -> Stream[MediaType]:
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
