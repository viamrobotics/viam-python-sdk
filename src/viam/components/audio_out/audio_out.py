import abc
from typing import Any, AsyncIterable, Dict, Final, Optional, TypeAlias

from viam.proto.common import GetPropertiesResponse
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT

from ..component_base import ComponentBase
from . import AudioInfo


class AudioOut(ComponentBase):
    """AudioOut represents a component that can play audio.

    This acts as an abstract base class for any drivers representing specific
    audio output implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "audio_out"
    )

    Properties: "TypeAlias" = GetPropertiesResponse

    @abc.abstractmethod
    async def play(
        self,
        data: bytes,
        info: Optional[AudioInfo] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> None:
        """
        Play the given audio data.

        ::

            my_audio_out = AudioOut.from_robot(robot=machine, name="my_audio_out")

            # With audio info
            audio_info = AudioInfo(codec=AudioCodec.PCM16, sample_rate_hz=44100, num_channels=2)
            await my_audio_out.play(audio_data, audio_info)

            # Without audio info (when codec encodes information within audio_data)
            await my_audio_out.play(audio_data)

        Args:
            data: audio bytes to play
            info: (optional) information about the audio data such as codec, sample rate, and channel count
        """

    @abc.abstractmethod
    async def play_stream(
        self,
        info: AudioInfo,
        chunks: AsyncIterable[bytes],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> None:
        """
        Stream audio chunks to the audio output device for playback.

        The caller provides an async iterable of raw audio bytes. Each chunk
        must match the codec and format described by ``info``. Implementations
        consume the iterable until it is exhausted, playing chunks as they arrive.

        ::

            async def chunk_source():
                for chunk in pcm_chunks:
                    yield chunk

            audio_info = AudioInfo(codec="pcm16", sample_rate_hz=22050, num_channels=1)
            await my_audio_out.play_stream(audio_info, chunk_source())

        Args:
            info: information about the audio stream such as codec, sample rate, and channel count
            chunks: async iterable of audio bytes to play in order
        """

    @abc.abstractmethod
    async def get_properties(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Properties:
        """
        Get the audio output device's properties.

        ::

            my_audio_out = AudioOut.from_robot(robot=machine, name="my_audio_out")
            properties = await my_audio_out.get_properties()

        Returns:
            Properties: The properties of the audio output device
        """
