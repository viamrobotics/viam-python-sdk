"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.geo_targeting_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GeographicView(google.protobuf.message.Message):
    """Proto file describing the geographic view resource.

    A geographic view.

    Geographic View includes all metrics aggregated at the country level,
    one row per country. It reports metrics at either actual physical location of
    the user or an area of interest. If other segment fields are used, you may
    get more than one row per country.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    LOCATION_TYPE_FIELD_NUMBER: builtins.int
    COUNTRY_CRITERION_ID_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Output only. The resource name of the geographic view.
    Geographic view resource names have the form:

    `customers/{customer_id}/geographicViews/{country_criterion_id}~{location_type}`
    """

    location_type: google.ads.googleads.v9.enums.geo_targeting_type_pb2.GeoTargetingTypeEnum.GeoTargetingType.ValueType = ...
    """Output only. Type of the geo targeting of the campaign."""

    country_criterion_id: builtins.int = ...
    """Output only. Criterion Id for the country."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        location_type : google.ads.googleads.v9.enums.geo_targeting_type_pb2.GeoTargetingTypeEnum.GeoTargetingType.ValueType = ...,
        country_criterion_id : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_country_criterion_id",b"_country_criterion_id","country_criterion_id",b"country_criterion_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_country_criterion_id",b"_country_criterion_id","country_criterion_id",b"country_criterion_id","location_type",b"location_type","resource_name",b"resource_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_country_criterion_id",b"_country_criterion_id"]) -> typing.Optional[typing_extensions.Literal["country_criterion_id"]]: ...
global___GeographicView = GeographicView
