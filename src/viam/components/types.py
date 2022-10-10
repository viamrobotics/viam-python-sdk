from dataclasses import dataclass
from enum import Enum, auto
import enum
from io import BytesIO
from typing import NamedTuple, Type, Union
from typing_extensions import Self

from PIL.Image import Image

from viam.proto.component import audioinput


class RawImage(NamedTuple):
    """A raw bytes representation of an image.

    When requesting `CameraMimeType.RAW` or if the camera returns a mime type that is not supported,
    the returned type will be this RawImage type.
    """

    data: bytes
    """The raw data of the image"""

    mime_type: str
    """The mimetype of the image"""

    width: int
    """The width of the image"""

    height: int
    """The height of the image"""

    def close(self):
        """Close the image and release resources. For RawImage, this is a noop."""
        return


class CameraMimeType(str, Enum):
    RAW = "image/vnd.viam.rgba"
    JPEG = "image/jpeg"
    PNG = "image/png"
    PCD = "pointcloud/pcd"

    def encode_image(self, image: Union[Image, RawImage]) -> bytes:
        if isinstance(image, RawImage):
            return image.data
        if self == CameraMimeType.JPEG:
            buf = BytesIO()
            image.save(buf, format="JPEG")
            return buf.getvalue()
        if self == CameraMimeType.PNG:
            buf = BytesIO()
            image.save(buf, format="PNG")
            return buf.getvalue()
        else:
            raise ValueError(f"Cannot encode image to {self}")

    @classmethod
    def is_supported(cls, mime_type: str) -> bool:
        """Check if the provided mime_type is supported

        Args:
            mime_type (str): The mime_type to check

        Returns:
            bool: Whether the mime_type is supported
        """
        return mime_type in set(item.value for item in cls)


@dataclass
class Audio:
    """A block of audio data containing information about the block and the audio data"""

    # class SampleFormat(str, enum.Enum):
    #     UNSPECIFIED = "SAMPLE_FORMAT_UNSPECIFIED"
    #     INT16_INTERLEAVED = "SAMPLE_FORMAT_INT16_INTERLEAVED"
    #     FLOAT32_INTERLEAVED = "SAMPLE_FORMAT_FLOAT32_INTERLEAVED"

    #     # @property
    #     # def type(self) -> Type:
    #     #     if self == Audio.SampleFormat.UNSPECIFIED:

    #     @property
    #     def proto(self) -> audioinput.SampleFormat:
    #         if self == Audio.SampleFormat.UNSPECIFIED:
    #             return audioinput.SampleFormat.SAMPLE_FORMAT_UNSPECIFIED
    #         if self == Audio.SampleFormat.INT16_INTERLEAVED:
    #             return audioinput.SampleFormat.SAMPLE_FORMAT_INT16_INTERLEAVED
    #         if self == Audio.SampleFormat.FLOAT32_INTERLEAVED:
    #             return audioinput.SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED
    #         raise Exception("SampleFormat not implemented")

    @dataclass
    class Info:
        sample_format: audioinput.SampleFormat
        channels: int
        sample_rate: int

        @property
        def proto(self) -> audioinput.AudioChunkInfo:
            return audioinput.AudioChunkInfo(sample_format=self.sample_format, channels=self.channels, sampling_rate=self.sample_rate)

        @classmethod
        def from_proto(cls, proto: audioinput.AudioChunkInfo) -> Self:
            return cls(sample_format=proto.sample_format, channels=proto.channels, sample_rate=proto.sampling_rate)

    @dataclass
    class Chunk:
        data: bytes
        length: int

        @property
        def proto(self) -> audioinput.AudioChunk:
            return audioinput.AudioChunk(data=self.data, length=self.length)

        @classmethod
        def from_proto(cls, proto: audioinput.AudioChunk) -> Self:
            return cls(data=proto.data, length=proto.length)

    info: Info
    chunk: Chunk
