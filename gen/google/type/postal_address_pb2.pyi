"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PostalAddress(google.protobuf.message.Message):
    """Represents a postal address, e.g. for postal delivery or payments addresses.
    Given a postal address, a postal service can deliver items to a premise, P.O.
    Box or similar.
    It is not intended to model geographical locations (roads, towns,
    mountains).

    In typical usage an address would be created via user input or from importing
    existing data, depending on the type of process.

    Advice on address input / editing:
     - Use an i18n-ready address widget such as
       https://github.com/google/libaddressinput)
    - Users should not be presented with UI elements for input or editing of
      fields outside countries where that field is used.

    For more guidance on how to use this schema, please see:
    https://support.google.com/business/answer/6397478
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REVISION_FIELD_NUMBER: builtins.int
    REGION_CODE_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    POSTAL_CODE_FIELD_NUMBER: builtins.int
    SORTING_CODE_FIELD_NUMBER: builtins.int
    ADMINISTRATIVE_AREA_FIELD_NUMBER: builtins.int
    LOCALITY_FIELD_NUMBER: builtins.int
    SUBLOCALITY_FIELD_NUMBER: builtins.int
    ADDRESS_LINES_FIELD_NUMBER: builtins.int
    RECIPIENTS_FIELD_NUMBER: builtins.int
    ORGANIZATION_FIELD_NUMBER: builtins.int
    revision: builtins.int = ...
    """The schema revision of the `PostalAddress`. This must be set to 0, which is
    the latest revision.

    All new revisions **must** be backward compatible with old revisions.
    """

    region_code: typing.Text = ...
    """Required. CLDR region code of the country/region of the address. This
    is never inferred and it is up to the user to ensure the value is
    correct. See http://cldr.unicode.org/ and
    http://www.unicode.org/cldr/charts/30/supplemental/territory_information.html
    for details. Example: "CH" for Switzerland.
    """

    language_code: typing.Text = ...
    """Optional. BCP-47 language code of the contents of this address (if
    known). This is often the UI language of the input form or is expected
    to match one of the languages used in the address' country/region, or their
    transliterated equivalents.
    This can affect formatting in certain countries, but is not critical
    to the correctness of the data and will never affect any validation or
    other non-formatting related operations.

    If this value is not known, it should be omitted (rather than specifying a
    possibly incorrect default).

    Examples: "zh-Hant", "ja", "ja-Latn", "en".
    """

    postal_code: typing.Text = ...
    """Optional. Postal code of the address. Not all countries use or require
    postal codes to be present, but where they are used, they may trigger
    additional validation with other parts of the address (e.g. state/zip
    validation in the U.S.A.).
    """

    sorting_code: typing.Text = ...
    """Optional. Additional, country-specific, sorting code. This is not used
    in most regions. Where it is used, the value is either a string like
    "CEDEX", optionally followed by a number (e.g. "CEDEX 7"), or just a number
    alone, representing the "sector code" (Jamaica), "delivery area indicator"
    (Malawi) or "post office indicator" (e.g. Côte d'Ivoire).
    """

    administrative_area: typing.Text = ...
    """Optional. Highest administrative subdivision which is used for postal
    addresses of a country or region.
    For example, this can be a state, a province, an oblast, or a prefecture.
    Specifically, for Spain this is the province and not the autonomous
    community (e.g. "Barcelona" and not "Catalonia").
    Many countries don't use an administrative area in postal addresses. E.g.
    in Switzerland this should be left unpopulated.
    """

    locality: typing.Text = ...
    """Optional. Generally refers to the city/town portion of the address.
    Examples: US city, IT comune, UK post town.
    In regions of the world where localities are not well defined or do not fit
    into this structure well, leave locality empty and use address_lines.
    """

    sublocality: typing.Text = ...
    """Optional. Sublocality of the address.
    For example, this can be neighborhoods, boroughs, districts.
    """

    @property
    def address_lines(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Unstructured address lines describing the lower levels of an address.

        Because values in address_lines do not have type information and may
        sometimes contain multiple values in a single field (e.g.
        "Austin, TX"), it is important that the line order is clear. The order of
        address lines should be "envelope order" for the country/region of the
        address. In places where this can vary (e.g. Japan), address_language is
        used to make it explicit (e.g. "ja" for large-to-small ordering and
        "ja-Latn" or "en" for small-to-large). This way, the most specific line of
        an address can be selected based on the language.

        The minimum permitted structural representation of an address consists
        of a region_code with all remaining information placed in the
        address_lines. It would be possible to format such an address very
        approximately without geocoding, but no semantic reasoning could be
        made about any of the address components until it was at least
        partially resolved.

        Creating an address only containing a region_code and address_lines, and
        then geocoding is the recommended way to handle completely unstructured
        addresses (as opposed to guessing which parts of the address should be
        localities or administrative areas).
        """
        pass
    @property
    def recipients(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Optional. The recipient at the address.
        This field may, under certain circumstances, contain multiline information.
        For example, it might contain "care of" information.
        """
        pass
    organization: typing.Text = ...
    """Optional. The name of the organization at the address."""

    def __init__(self,
        *,
        revision : builtins.int = ...,
        region_code : typing.Text = ...,
        language_code : typing.Text = ...,
        postal_code : typing.Text = ...,
        sorting_code : typing.Text = ...,
        administrative_area : typing.Text = ...,
        locality : typing.Text = ...,
        sublocality : typing.Text = ...,
        address_lines : typing.Optional[typing.Iterable[typing.Text]] = ...,
        recipients : typing.Optional[typing.Iterable[typing.Text]] = ...,
        organization : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address_lines",b"address_lines","administrative_area",b"administrative_area","language_code",b"language_code","locality",b"locality","organization",b"organization","postal_code",b"postal_code","recipients",b"recipients","region_code",b"region_code","revision",b"revision","sorting_code",b"sorting_code","sublocality",b"sublocality"]) -> None: ...
global___PostalAddress = PostalAddress
