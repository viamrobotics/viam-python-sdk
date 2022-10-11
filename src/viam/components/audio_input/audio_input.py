import abc
import asyncio
from collections.abc import AsyncIterator
from dataclasses import dataclass
from datetime import timedelta
from multiprocessing import Pipe
from multiprocessing.connection import Connection
from os import dup

# from multiprocessing.connection import PipeConnection
from typing import Callable, Generic, Protocol, TypeVar

from google.protobuf.duration_pb2 import Duration
from typing_extensions import Self

from viam.components.types import Audio
from viam.proto.component.audioinput import PropertiesResponse

from ..component_base import ComponentBase

MediaType = TypeVar("MediaType", covariant=True)


class MediaReader(Protocol[MediaType]):
    def read(self) -> MediaType:
        ...


class MediaStream(Protocol[MediaType]):
    async def next(self) -> MediaType:
        ...

    async def close(self):
        ...

    def __aiter__(self):
        return self

    async def __anext__(self) -> MediaType:
        return await self.next()


AudioReader = MediaReader[Audio]
AudioStream = MediaStream[Audio]


class MediaStreamWithPipe(MediaStream[MediaType]):
    def __init__(self) -> None:
        self._pipe_r, self.pipe = Pipe(duplex=False)
        self._media_available = asyncio.Event()
        asyncio.get_running_loop().add_reader(self._pipe_r, self._set_next)

    def _set_next(self):
        self._next: MediaType = self._pipe_r.recv()
        self._media_available.set()

    async def next(self) -> MediaType:
        await self._media_available.wait()
        media = self._next
        self._media_available.clear()
        return media

    async def close(self):
        asyncio.get_running_loop().remove_reader(self._pipe_r)
        self.pipe.close()
        self._pipe_r.close()

    async def __anext__(self) -> MediaType:
        try:
            return await self.next()
        except EOFError:
            await self.close()
            raise StopAsyncIteration


class AudioInput(ComponentBase):
    @dataclass
    class Properties:
        channel_count: int
        latency: timedelta
        sample_rate: int
        sample_size: int
        is_big_endian: bool
        is_float: bool
        is_interleaved: bool

        @property
        def proto(self) -> PropertiesResponse:
            latency = Duration()
            latency.FromTimedelta(self.latency)
            return PropertiesResponse(
                channel_count=self.channel_count,
                latency=latency,
                sample_rate=self.sample_rate,
                sample_size=self.sample_size,
                is_big_endian=self.is_big_endian,
                is_float=self.is_float,
                is_interleaved=self.is_interleaved,
            )

        @classmethod
        def from_proto(cls, proto: PropertiesResponse) -> Self:
            return cls(
                channel_count=proto.channel_count,
                latency=proto.latency.ToTimedelta(),
                sample_rate=proto.sample_rate,
                sample_size=proto.sample_size,
                is_big_endian=proto.is_big_endian,
                is_float=proto.is_float,
                is_interleaved=proto.is_interleaved,
            )

    @abc.abstractmethod
    async def stream(self) -> AudioStream:
        """Stream audio samples from the audio input of the underlying robot

        Returns:
            MediaStream[Audio]: The stream of audio chunks
        """
        ...

    @abc.abstractmethod
    async def properties(self) -> Properties:
        """Get the properties of the audio input of the underlying robot

        Returns:
            Properties: The audio input properties
        """
        ...
