from enum import Enum


class AudioCodec(str, Enum):
    """Common audio codec identifiers.

    These constants represent commonly supported audio codecs
    for audioin and audioout components.

    Example::

        from viam.components.codecs import AudioCodec
        from viam.proto.common import AudioInfo

        audio_info = AudioInfo(
            codec=AudioCodec.PCM16,
            sample_rate_hz=44100,
            num_channels=2
        )
    """

    PCM16 = "pcm16"
    PCM32 = "pcm32"
    PCM32_FLOAT = "pcm32_float"
    MP3 = "mp3"
    AAC = "aac"
    OPUS = "opus"
    FLAC = "flac"
