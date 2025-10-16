import abc
import sys
from typing import Any, Dict, Final, Optional

from viam.proto.common import GetPropertiesResponse, AudioInfo
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT

from ..component_base import ComponentBase

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


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
    async def play(self,
                   data: bytes,
                   info: AudioInfo,
                   *,
                   extra: Optional[Dict[str, Any]] = None,
                   timeout: Optional[float] = None,
                   **kwargs) -> None:
        """
        Play the given audio data.

        ::

            my_audio_out = AudioOut.from_robot(robot=machine, name="my_audio_out")

            audio_info = AudioInfo(codec="pcm16", sample_rate=44100, num_channels=2)
            await my_audio_out.play(audio_data, audio_info)

        Args:
            data: Raw audio bytes to play
            info: Information about the audio data such as codec, sample rate, and channel count
        """

    @abc.abstractmethod
    async def get_properties(self,
                           *,
                           extra: Optional[Dict[str, Any]] = None,
                           timeout: Optional[float] = None,
                           **kwargs) -> Properties:
        """
        Get the audio output device's properties.

        ::

            my_audio_out = AudioOut.from_robot(robot=machine, name="my_audio_out")
            properties = await my_audio_out.get_properties()

        Returns:
            Properties: The properties of the audio output device
        """





