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

class OfflineUserDataJobErrorEnum(google.protobuf.message.Message):
    """Proto file describing offline user data job errors.

    Container for enum describing possible offline user data job errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _OfflineUserDataJobError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OfflineUserDataJobErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OfflineUserDataJobError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        INVALID_USER_LIST_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 3
        """The user list ID provided for the job is invalid."""

        INVALID_USER_LIST_TYPE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 4
        """Type of the user list is not applicable for the job."""

        NOT_ON_ALLOWLIST_FOR_USER_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 33
        """Customer is not allowisted for using user ID in upload data."""

        INCOMPATIBLE_UPLOAD_KEY_TYPE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 6
        """Upload data is not compatible with the upload key type of the associated
        user list.
        """

        MISSING_USER_IDENTIFIER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 7
        """The user identifier is missing valid data."""

        INVALID_MOBILE_ID_FORMAT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 8
        """The mobile ID is malformed."""

        TOO_MANY_USER_IDENTIFIERS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 9
        """Maximum number of user identifiers allowed per request is 100,000."""

        NOT_ON_ALLOWLIST_FOR_STORE_SALES_DIRECT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 31
        """Customer is not on the allow-list for store sales direct data."""

        NOT_ON_ALLOWLIST_FOR_UNIFIED_STORE_SALES: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 32
        """Customer is not on the allow-list for unified store sales data."""

        INVALID_PARTNER_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 11
        """The partner ID in store sales direct metadata is invalid."""

        INVALID_ENCODING: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 12
        """The data in user identifier should not be encoded."""

        INVALID_COUNTRY_CODE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 13
        """The country code is invalid."""

        INCOMPATIBLE_USER_IDENTIFIER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 14
        """Incompatible user identifier when using third_party_user_id for store
        sales direct first party data or not using third_party_user_id for store
        sales third party data.
        """

        FUTURE_TRANSACTION_TIME: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 15
        """A transaction time in the future is not allowed."""

        INVALID_CONVERSION_ACTION: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 16
        """The conversion_action specified in transaction_attributes is used to
        report conversions to a conversion action configured in Google Ads. This
        error indicates there is no such conversion action in the account.
        """

        MOBILE_ID_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 17
        """Mobile ID is not supported for store sales direct data."""

        INVALID_OPERATION_ORDER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 18
        """When a remove-all operation is provided, it has to be the first operation
        of the operation list.
        """

        CONFLICTING_OPERATION: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 19
        """Mixing creation and removal of offline data in the same job is not
        allowed.
        """

        EXTERNAL_UPDATE_ID_ALREADY_EXISTS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 21
        """The external update ID already exists."""

        JOB_ALREADY_STARTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 22
        """Once the upload job is started, new operations cannot be added."""

        REMOVE_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 23
        """Remove operation is not allowed for store sales direct updates."""

        REMOVE_ALL_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 24
        """Remove-all is not supported for certain offline user data job types."""

        INVALID_SHA256_FORMAT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 25
        """The SHA256 encoded value is malformed."""

        CUSTOM_KEY_DISABLED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 26
        """The custom key specified is not enabled for the unified store sales
        upload.
        """

        CUSTOM_KEY_NOT_PREDEFINED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 27
        """The custom key specified is not predefined through the Google Ads UI."""

        CUSTOM_KEY_NOT_SET: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 29
        """The custom key specified is not set in the upload."""

        CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 30
        """The customer has not accepted the customer data terms in the conversion
        settings page.
        """

        ATTRIBUTES_NOT_APPLICABLE_FOR_CUSTOMER_MATCH_USER_LIST: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 34
        """User attributes cannot be uploaded into a user list."""

        LIFETIME_VALUE_BUCKET_NOT_IN_RANGE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 35
        """Lifetime value bucket must be a number from 1-10, except for remove
        operation where 0 will be accepted.
        """

        INCOMPATIBLE_USER_IDENTIFIER_FOR_ATTRIBUTES: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 36
        """Identifiers not supported for Customer Match attributes. User attributes
        can only be provided with contact info (email, phone, address) user
        identifiers.
        """

    class OfflineUserDataJobError(_OfflineUserDataJobError, metaclass=_OfflineUserDataJobErrorEnumTypeWrapper):
        """Enum describing possible request errors."""
        pass

    UNSPECIFIED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    INVALID_USER_LIST_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 3
    """The user list ID provided for the job is invalid."""

    INVALID_USER_LIST_TYPE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 4
    """Type of the user list is not applicable for the job."""

    NOT_ON_ALLOWLIST_FOR_USER_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 33
    """Customer is not allowisted for using user ID in upload data."""

    INCOMPATIBLE_UPLOAD_KEY_TYPE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 6
    """Upload data is not compatible with the upload key type of the associated
    user list.
    """

    MISSING_USER_IDENTIFIER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 7
    """The user identifier is missing valid data."""

    INVALID_MOBILE_ID_FORMAT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 8
    """The mobile ID is malformed."""

    TOO_MANY_USER_IDENTIFIERS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 9
    """Maximum number of user identifiers allowed per request is 100,000."""

    NOT_ON_ALLOWLIST_FOR_STORE_SALES_DIRECT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 31
    """Customer is not on the allow-list for store sales direct data."""

    NOT_ON_ALLOWLIST_FOR_UNIFIED_STORE_SALES: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 32
    """Customer is not on the allow-list for unified store sales data."""

    INVALID_PARTNER_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 11
    """The partner ID in store sales direct metadata is invalid."""

    INVALID_ENCODING: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 12
    """The data in user identifier should not be encoded."""

    INVALID_COUNTRY_CODE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 13
    """The country code is invalid."""

    INCOMPATIBLE_USER_IDENTIFIER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 14
    """Incompatible user identifier when using third_party_user_id for store
    sales direct first party data or not using third_party_user_id for store
    sales third party data.
    """

    FUTURE_TRANSACTION_TIME: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 15
    """A transaction time in the future is not allowed."""

    INVALID_CONVERSION_ACTION: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 16
    """The conversion_action specified in transaction_attributes is used to
    report conversions to a conversion action configured in Google Ads. This
    error indicates there is no such conversion action in the account.
    """

    MOBILE_ID_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 17
    """Mobile ID is not supported for store sales direct data."""

    INVALID_OPERATION_ORDER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 18
    """When a remove-all operation is provided, it has to be the first operation
    of the operation list.
    """

    CONFLICTING_OPERATION: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 19
    """Mixing creation and removal of offline data in the same job is not
    allowed.
    """

    EXTERNAL_UPDATE_ID_ALREADY_EXISTS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 21
    """The external update ID already exists."""

    JOB_ALREADY_STARTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 22
    """Once the upload job is started, new operations cannot be added."""

    REMOVE_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 23
    """Remove operation is not allowed for store sales direct updates."""

    REMOVE_ALL_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 24
    """Remove-all is not supported for certain offline user data job types."""

    INVALID_SHA256_FORMAT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 25
    """The SHA256 encoded value is malformed."""

    CUSTOM_KEY_DISABLED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 26
    """The custom key specified is not enabled for the unified store sales
    upload.
    """

    CUSTOM_KEY_NOT_PREDEFINED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 27
    """The custom key specified is not predefined through the Google Ads UI."""

    CUSTOM_KEY_NOT_SET: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 29
    """The custom key specified is not set in the upload."""

    CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 30
    """The customer has not accepted the customer data terms in the conversion
    settings page.
    """

    ATTRIBUTES_NOT_APPLICABLE_FOR_CUSTOMER_MATCH_USER_LIST: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 34
    """User attributes cannot be uploaded into a user list."""

    LIFETIME_VALUE_BUCKET_NOT_IN_RANGE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 35
    """Lifetime value bucket must be a number from 1-10, except for remove
    operation where 0 will be accepted.
    """

    INCOMPATIBLE_USER_IDENTIFIER_FOR_ATTRIBUTES: OfflineUserDataJobErrorEnum.OfflineUserDataJobError.ValueType = ...  # 36
    """Identifiers not supported for Customer Match attributes. User attributes
    can only be provided with contact info (email, phone, address) user
    identifiers.
    """


    def __init__(self,
        ) -> None: ...
global___OfflineUserDataJobErrorEnum = OfflineUserDataJobErrorEnum
