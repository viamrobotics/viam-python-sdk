"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ListLocationsRequest(google.protobuf.message.Message):
    """The request message for [Locations.ListLocations][google.cloud.location.Locations.ListLocations]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource that owns the locations collection, if applicable."""

    filter: typing.Text = ...
    """The standard list filter."""

    page_size: builtins.int = ...
    """The standard list page size."""

    page_token: typing.Text = ...
    """The standard list page token."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","name",b"name","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListLocationsRequest = ListLocationsRequest

class ListLocationsResponse(google.protobuf.message.Message):
    """The response message for [Locations.ListLocations][google.cloud.location.Locations.ListLocations]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOCATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def locations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Location]:
        """A list of locations that matches the specified filter in the request."""
        pass
    next_page_token: typing.Text = ...
    """The standard List next-page token."""

    def __init__(self,
        *,
        locations : typing.Optional[typing.Iterable[global___Location]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locations",b"locations","next_page_token",b"next_page_token"]) -> None: ...
global___ListLocationsResponse = ListLocationsResponse

class GetLocationRequest(google.protobuf.message.Message):
    """The request message for [Locations.GetLocation][google.cloud.location.Locations.GetLocation]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Resource name for the location."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetLocationRequest = GetLocationRequest

class Location(google.protobuf.message.Message):
    """A resource that represents Google Cloud Platform location."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Resource name for the location, which may vary between implementations.
    For example: `"projects/example-project/locations/us-east1"`
    """

    location_id: typing.Text = ...
    """The canonical id for this location. For example: `"us-east1"`."""

    display_name: typing.Text = ...
    """The friendly name for this location, typically a nearby city name.
    For example, "Tokyo".
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Cross-service attributes for the location. For example

            {"cloud.googleapis.com/region": "us-east1"}
        """
        pass
    @property
    def metadata(self) -> google.protobuf.any_pb2.Any:
        """Service-specific metadata. For example the available capacity at the given
        location.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        location_id : typing.Text = ...,
        display_name : typing.Text = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        metadata : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata",b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name","labels",b"labels","location_id",b"location_id","metadata",b"metadata","name",b"name"]) -> None: ...
global___Location = Location
