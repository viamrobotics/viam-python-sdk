import abc
from dataclasses import dataclass
from datetime import timedelta
from typing import Final, Optional

from google.protobuf.duration_pb2 import Duration
from typing_extensions import Self

from viam.media.audio import Audio, AudioStream
from viam.proto.component.audioinput import PropertiesResponse
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype
from viam.streams import StreamSource

from ..component_base import ComponentBase


class AudioInput(ComponentBase, StreamSource[Audio]):
    """AudioInput represents a component that can capture audio.

    This acts as an abstract base class for any drivers representing specific
    audio input implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "audio_input"
    )

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
    async def stream(self, *, timeout: Optional[float] = None, **kwargs) -> AudioStream:
        """Stream audio samples from the audio input of the underlying robot

        Returns:
            Stream[Audio]: The stream of audio chunks
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:
        """Get the properties of the audio input of the underlying robot

        Returns:
            Properties: The audio input properties
        """
        ...
