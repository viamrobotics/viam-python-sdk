"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class EducationPlaceholderFieldEnum(google.protobuf.message.Message):
    """Proto file describing Education placeholder fields.

    Values for Education placeholder fields.
    For more information about dynamic remarketing feeds, see
    https://support.google.com/google-ads/answer/6053288.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _EducationPlaceholderField:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _EducationPlaceholderFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EducationPlaceholderField.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        PROGRAM_ID: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 2
        """Data Type: STRING. Required. Combination of PROGRAM ID and LOCATION ID
        must be unique per offer.
        """

        LOCATION_ID: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 3
        """Data Type: STRING. Combination of PROGRAM ID and LOCATION ID must be
        unique per offer.
        """

        PROGRAM_NAME: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 4
        """Data Type: STRING. Required. Main headline with program name to be shown
        in dynamic ad.
        """

        AREA_OF_STUDY: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 5
        """Data Type: STRING. Area of study that can be shown in dynamic ad."""

        PROGRAM_DESCRIPTION: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 6
        """Data Type: STRING. Description of program that can be shown in dynamic
        ad.
        """

        SCHOOL_NAME: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 7
        """Data Type: STRING. Name of school that can be shown in dynamic ad."""

        ADDRESS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 8
        """Data Type: STRING. Complete school address, including postal code."""

        THUMBNAIL_IMAGE_URL: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 9
        """Data Type: URL. Image to be displayed in ads."""

        ALTERNATIVE_THUMBNAIL_IMAGE_URL: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 10
        """Data Type: URL. Alternative hosted file of image to be used in the ad."""

        FINAL_URLS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 11
        """Data Type: URL_LIST. Required. Final URLs to be used in ad when using
        Upgraded URLs; the more specific the better (e.g. the individual URL of a
        specific program and its location).
        """

        FINAL_MOBILE_URLS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 12
        """Data Type: URL_LIST. Final mobile URLs for the ad when using Upgraded
        URLs.
        """

        TRACKING_URL: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 13
        """Data Type: URL. Tracking template for the ad when using Upgraded URLs."""

        CONTEXTUAL_KEYWORDS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 14
        """Data Type: STRING_LIST. Keywords used for product retrieval."""

        ANDROID_APP_LINK: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 15
        """Data Type: STRING. Android app link. Must be formatted as:
        android-app://{package_id}/{scheme}/{host_path}.
        The components are defined as follows:
        package_id: app ID as specified in Google Play.
        scheme: the scheme to pass to the application. Can be HTTP, or a custom
          scheme.
        host_path: identifies the specific content within your application.
        """

        SIMILAR_PROGRAM_IDS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 16
        """Data Type: STRING_LIST. List of recommended program IDs to show together
        with this item.
        """

        IOS_APP_LINK: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 17
        """Data Type: STRING. iOS app link."""

        IOS_APP_STORE_ID: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 18
        """Data Type: INT64. iOS app store ID."""

    class EducationPlaceholderField(_EducationPlaceholderField, metaclass=_EducationPlaceholderFieldEnumTypeWrapper):
        """Possible values for Education placeholder fields."""
        pass

    UNSPECIFIED: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    PROGRAM_ID: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 2
    """Data Type: STRING. Required. Combination of PROGRAM ID and LOCATION ID
    must be unique per offer.
    """

    LOCATION_ID: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 3
    """Data Type: STRING. Combination of PROGRAM ID and LOCATION ID must be
    unique per offer.
    """

    PROGRAM_NAME: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 4
    """Data Type: STRING. Required. Main headline with program name to be shown
    in dynamic ad.
    """

    AREA_OF_STUDY: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 5
    """Data Type: STRING. Area of study that can be shown in dynamic ad."""

    PROGRAM_DESCRIPTION: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 6
    """Data Type: STRING. Description of program that can be shown in dynamic
    ad.
    """

    SCHOOL_NAME: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 7
    """Data Type: STRING. Name of school that can be shown in dynamic ad."""

    ADDRESS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 8
    """Data Type: STRING. Complete school address, including postal code."""

    THUMBNAIL_IMAGE_URL: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 9
    """Data Type: URL. Image to be displayed in ads."""

    ALTERNATIVE_THUMBNAIL_IMAGE_URL: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 10
    """Data Type: URL. Alternative hosted file of image to be used in the ad."""

    FINAL_URLS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 11
    """Data Type: URL_LIST. Required. Final URLs to be used in ad when using
    Upgraded URLs; the more specific the better (e.g. the individual URL of a
    specific program and its location).
    """

    FINAL_MOBILE_URLS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 12
    """Data Type: URL_LIST. Final mobile URLs for the ad when using Upgraded
    URLs.
    """

    TRACKING_URL: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 13
    """Data Type: URL. Tracking template for the ad when using Upgraded URLs."""

    CONTEXTUAL_KEYWORDS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 14
    """Data Type: STRING_LIST. Keywords used for product retrieval."""

    ANDROID_APP_LINK: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 15
    """Data Type: STRING. Android app link. Must be formatted as:
    android-app://{package_id}/{scheme}/{host_path}.
    The components are defined as follows:
    package_id: app ID as specified in Google Play.
    scheme: the scheme to pass to the application. Can be HTTP, or a custom
      scheme.
    host_path: identifies the specific content within your application.
    """

    SIMILAR_PROGRAM_IDS: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 16
    """Data Type: STRING_LIST. List of recommended program IDs to show together
    with this item.
    """

    IOS_APP_LINK: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 17
    """Data Type: STRING. iOS app link."""

    IOS_APP_STORE_ID: EducationPlaceholderFieldEnum.EducationPlaceholderField.ValueType = ...  # 18
    """Data Type: INT64. iOS app store ID."""


    def __init__(self,
        ) -> None: ...
global___EducationPlaceholderFieldEnum = EducationPlaceholderFieldEnum
