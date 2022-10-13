import warnings

from viam.media.video import CameraMimeType, RawImage  # noqa: F401

warnings.warn("The types module is deprecated. Please find the appropriate types in the media package", DeprecationWarning)
