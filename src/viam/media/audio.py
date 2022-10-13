from dataclasses import dataclass

from viam.media.media import MediaReader, MediaStream
from viam.proto.component.audioinput import AudioChunk, AudioChunkInfo


@dataclass
class Audio:
    """A block of audio data containing information about the block and the audio data"""

    info: AudioChunkInfo
    chunk: AudioChunk


AudioReader = MediaReader[Audio]
AudioStream = MediaStream[Audio]
