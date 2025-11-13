import abc
import sys
from typing import Final, Optional

from viam.proto.common import GetPropertiesResponse
from viam.proto.component.audioin import GetAudioResponse
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT
from viam.streams import Stream

from ..component_base import ComponentBase

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


class AudioIn(ComponentBase):
    """AudioIn represents a component that can capture audio.

    This acts as an abstract base class for any drivers representing specific
    audio input implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "audio_in"
    )

    Properties: "TypeAlias" = GetPropertiesResponse
    AudioResponse: "TypeAlias" = GetAudioResponse
    AudioStream = Stream[AudioResponse]

    @abc.abstractmethod
    async def get_audio(
        self, codec: str, duration_seconds: float, previous_timestamp_ns: int, *, timeout: Optional[float] = None, **kwargs
    ) -> AudioStream:
        """
        Get a stream of audio from the device

        ::

            my_audio_in = AudioIn.from_robot(robot=machine, name="my_audio_in")

            stream = await my_audio_in.get_audio(
                codec=AudioCodec.PCM16,
                duration_seconds=10.0,
                previous_timestamp_ns=0
            )

        Args:
            codec (str): The desired codec of the returned audio data
            duration_seconds (float): duration of the stream. 0 = indefinite stream
            previous_timestamp_ns (int): starting timestamp in nanoseconds for recording continuity.
            Set to 0 to begin recording from the current time.
        Returns:
            AudioStream: stream of audio chunks.
        ...
        """

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:
        """
        Get the audio device's properties

        ::

            my_audio_in = AudioIn.from_robot(robot=machine, name="my_audio_in")
            properties = await my_audio_in.get_properties()

        Returns:
            Properties: The properties of the audio in device.
        ...
        """
