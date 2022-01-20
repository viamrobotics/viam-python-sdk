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

class AuthorizationErrorEnum(google.protobuf.message.Message):
    """Proto file describing authorization errors.

    Container for enum describing possible authorization errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AuthorizationError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AuthorizationErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AuthorizationError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        USER_PERMISSION_DENIED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 2
        """User doesn't have permission to access customer. Note: If you're
        accessing a client customer, the manager's customer ID must be set in the
        `login-customer-id` header. Learn more at
        https://developers.google.com/google-ads/api/docs/concepts/call-structure#cid
        """

        DEVELOPER_TOKEN_NOT_ON_ALLOWLIST: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 13
        """The developer token is not on the allow-list."""

        DEVELOPER_TOKEN_PROHIBITED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 4
        """The developer token is not allowed with the project sent in the request."""

        PROJECT_DISABLED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 5
        """The Google Cloud project sent in the request does not have permission to
        access the api.
        """

        AUTHORIZATION_ERROR: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 6
        """Authorization of the client failed."""

        ACTION_NOT_PERMITTED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 7
        """The user does not have permission to perform this action
        (e.g., ADD, UPDATE, REMOVE) on the resource or call a method.
        """

        INCOMPLETE_SIGNUP: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 8
        """Signup not complete."""

        CUSTOMER_NOT_ENABLED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 24
        """The customer can't be used because it isn't enabled."""

        MISSING_TOS: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 9
        """The developer must sign the terms of service. They can be found here:
        ads.google.com/aw/apicenter
        """

        DEVELOPER_TOKEN_NOT_APPROVED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 10
        """The developer token is not approved. Non-approved developer tokens can
        only be used with test accounts.
        """

        INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 11
        """The login customer specified does not have access to the account
        specified, so the request is invalid.
        """

        SERVICE_ACCESS_DENIED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 12
        """The developer specified does not have access to the service."""

        ACCESS_DENIED_FOR_ACCOUNT_TYPE: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 25
        """The customer (or login customer) isn't in Google Ads. It belongs to
        another ads system.
        """

    class AuthorizationError(_AuthorizationError, metaclass=_AuthorizationErrorEnumTypeWrapper):
        """Enum describing possible authorization errors."""
        pass

    UNSPECIFIED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    USER_PERMISSION_DENIED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 2
    """User doesn't have permission to access customer. Note: If you're
    accessing a client customer, the manager's customer ID must be set in the
    `login-customer-id` header. Learn more at
    https://developers.google.com/google-ads/api/docs/concepts/call-structure#cid
    """

    DEVELOPER_TOKEN_NOT_ON_ALLOWLIST: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 13
    """The developer token is not on the allow-list."""

    DEVELOPER_TOKEN_PROHIBITED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 4
    """The developer token is not allowed with the project sent in the request."""

    PROJECT_DISABLED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 5
    """The Google Cloud project sent in the request does not have permission to
    access the api.
    """

    AUTHORIZATION_ERROR: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 6
    """Authorization of the client failed."""

    ACTION_NOT_PERMITTED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 7
    """The user does not have permission to perform this action
    (e.g., ADD, UPDATE, REMOVE) on the resource or call a method.
    """

    INCOMPLETE_SIGNUP: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 8
    """Signup not complete."""

    CUSTOMER_NOT_ENABLED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 24
    """The customer can't be used because it isn't enabled."""

    MISSING_TOS: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 9
    """The developer must sign the terms of service. They can be found here:
    ads.google.com/aw/apicenter
    """

    DEVELOPER_TOKEN_NOT_APPROVED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 10
    """The developer token is not approved. Non-approved developer tokens can
    only be used with test accounts.
    """

    INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 11
    """The login customer specified does not have access to the account
    specified, so the request is invalid.
    """

    SERVICE_ACCESS_DENIED: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 12
    """The developer specified does not have access to the service."""

    ACCESS_DENIED_FOR_ACCOUNT_TYPE: AuthorizationErrorEnum.AuthorizationError.ValueType = ...  # 25
    """The customer (or login customer) isn't in Google Ads. It belongs to
    another ads system.
    """


    def __init__(self,
        ) -> None: ...
global___AuthorizationErrorEnum = AuthorizationErrorEnum
