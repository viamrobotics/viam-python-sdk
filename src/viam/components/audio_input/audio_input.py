import abc
from dataclasses import dataclass
from datetime import timedelta

from google.protobuf.duration_pb2 import Duration
from typing_extensions import Self

from viam.media import MediaSource
from viam.media.audio import Audio, AudioStream
from viam.proto.component.audioinput import PropertiesResponse

from ..component_base import ComponentBase


class AudioInput(ComponentBase, MediaSource[Audio]):
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
    async def get_properties(self) -> Properties:
        """Get the properties of the audio input of the underlying robot

        Returns:
            Properties: The audio input properties
        """
        ...
