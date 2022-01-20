"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class LatLng(google.protobuf.message.Message):
    """An object that represents a latitude/longitude pair. This is expressed as a
    pair of doubles to represent degrees latitude and degrees longitude. Unless
    specified otherwise, this must conform to the
    <a href="http://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf">WGS84
    standard</a>. Values must be within normalized ranges.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LATITUDE_FIELD_NUMBER: builtins.int
    LONGITUDE_FIELD_NUMBER: builtins.int
    latitude: builtins.float = ...
    """The latitude in degrees. It must be in the range [-90.0, +90.0]."""

    longitude: builtins.float = ...
    """The longitude in degrees. It must be in the range [-180.0, +180.0]."""

    def __init__(self,
        *,
        latitude : builtins.float = ...,
        longitude : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["latitude",b"latitude","longitude",b"longitude"]) -> None: ...
global___LatLng = LatLng
