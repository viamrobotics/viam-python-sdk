from dataclasses import dataclass

from viam.streams import Stream, StreamReader
from viam.proto.component.audioinput import AudioChunk, AudioChunkInfo


@dataclass
class Audio:
    """A block of audio data containing information about the block and the audio data"""

    info: AudioChunkInfo
    chunk: AudioChunk


AudioReader = StreamReader[Audio]
AudioStream = Stream[Audio]
