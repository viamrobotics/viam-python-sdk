import sys

if sys.version_info >= (3, 9):
    from collections.abc import AsyncIterator
else:
    from typing import AsyncIterator

from typing import Protocol, TypeVar

MediaType = TypeVar("MediaType", covariant=True)


class MediaStream(Protocol[MediaType]):
    async def next(self) -> MediaType:
        ...

    async def close(self):
        ...

    def __aiter__(self) -> AsyncIterator:
        return self

    async def __anext__(self) -> MediaType:
        return await self.next()


class MediaReader(Protocol[MediaType]):
    async def read(self) -> MediaType:
        ...


class MediaSource(Protocol[MediaType]):
    async def stream(self) -> MediaStream[MediaType]:
        ...


class MediaStreamWithIterator(MediaStream[MediaType]):
    _stream: AsyncIterator[MediaType]

    def __init__(self, stream: AsyncIterator[MediaType]):
        self._stream = stream

    async def next(self) -> MediaType:
        return await self._stream.__anext__()

    def __aiter__(self):
        return self._stream

    async def __anext__(self) -> MediaType:
        return await self._stream.__anext__()

    async def close(self):
        return await super().close()
