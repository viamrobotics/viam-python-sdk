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

class ManagerLinkErrorEnum(google.protobuf.message.Message):
    """Proto file describing ManagerLink errors.

    Container for enum describing possible ManagerLink errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ManagerLinkError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ManagerLinkErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ManagerLinkError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 2
        """The manager and client have incompatible account types."""

        TOO_MANY_MANAGERS: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 3
        """Client is already linked to too many managers."""

        TOO_MANY_INVITES: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 4
        """Manager has too many pending invitations."""

        ALREADY_INVITED_BY_THIS_MANAGER: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 5
        """Client is already invited by this manager."""

        ALREADY_MANAGED_BY_THIS_MANAGER: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 6
        """The client is already managed by this manager."""

        ALREADY_MANAGED_IN_HIERARCHY: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 7
        """Client is already managed in hierarchy."""

        DUPLICATE_CHILD_FOUND: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 8
        """Manager and sub-manager to be linked have duplicate client."""

        CLIENT_HAS_NO_ADMIN_USER: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 9
        """Client has no active user that can access the client account."""

        MAX_DEPTH_EXCEEDED: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 10
        """Adding this link would exceed the maximum hierarchy depth."""

        CYCLE_NOT_ALLOWED: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 11
        """Adding this link will create a cycle."""

        TOO_MANY_ACCOUNTS: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 12
        """Manager account has the maximum number of linked clients."""

        TOO_MANY_ACCOUNTS_AT_MANAGER: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 13
        """Parent manager account has the maximum number of linked clients."""

        NON_OWNER_USER_CANNOT_MODIFY_LINK: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 14
        """The account is not authorized owner."""

        SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 15
        """Your manager account is suspended, and you are no longer allowed to link
        to clients.
        """

        CLIENT_OUTSIDE_TREE: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 16
        """You are not allowed to move a client to a manager that is not under your
        current hierarchy.
        """

        INVALID_STATUS_CHANGE: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 17
        """The changed status for mutate link is invalid."""

        INVALID_CHANGE: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 18
        """The change for mutate link is invalid."""

        CUSTOMER_CANNOT_MANAGE_SELF: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 19
        """You are not allowed to link a manager account to itself."""

        CREATING_ENABLED_LINK_NOT_ALLOWED: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 20
        """The link was created with status ACTIVE and not PENDING."""

    class ManagerLinkError(_ManagerLinkError, metaclass=_ManagerLinkErrorEnumTypeWrapper):
        """Enum describing possible ManagerLink errors."""
        pass

    UNSPECIFIED: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 2
    """The manager and client have incompatible account types."""

    TOO_MANY_MANAGERS: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 3
    """Client is already linked to too many managers."""

    TOO_MANY_INVITES: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 4
    """Manager has too many pending invitations."""

    ALREADY_INVITED_BY_THIS_MANAGER: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 5
    """Client is already invited by this manager."""

    ALREADY_MANAGED_BY_THIS_MANAGER: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 6
    """The client is already managed by this manager."""

    ALREADY_MANAGED_IN_HIERARCHY: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 7
    """Client is already managed in hierarchy."""

    DUPLICATE_CHILD_FOUND: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 8
    """Manager and sub-manager to be linked have duplicate client."""

    CLIENT_HAS_NO_ADMIN_USER: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 9
    """Client has no active user that can access the client account."""

    MAX_DEPTH_EXCEEDED: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 10
    """Adding this link would exceed the maximum hierarchy depth."""

    CYCLE_NOT_ALLOWED: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 11
    """Adding this link will create a cycle."""

    TOO_MANY_ACCOUNTS: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 12
    """Manager account has the maximum number of linked clients."""

    TOO_MANY_ACCOUNTS_AT_MANAGER: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 13
    """Parent manager account has the maximum number of linked clients."""

    NON_OWNER_USER_CANNOT_MODIFY_LINK: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 14
    """The account is not authorized owner."""

    SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 15
    """Your manager account is suspended, and you are no longer allowed to link
    to clients.
    """

    CLIENT_OUTSIDE_TREE: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 16
    """You are not allowed to move a client to a manager that is not under your
    current hierarchy.
    """

    INVALID_STATUS_CHANGE: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 17
    """The changed status for mutate link is invalid."""

    INVALID_CHANGE: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 18
    """The change for mutate link is invalid."""

    CUSTOMER_CANNOT_MANAGE_SELF: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 19
    """You are not allowed to link a manager account to itself."""

    CREATING_ENABLED_LINK_NOT_ALLOWED: ManagerLinkErrorEnum.ManagerLinkError.ValueType = ...  # 20
    """The link was created with status ACTIVE and not PENDING."""


    def __init__(self,
        ) -> None: ...
global___ManagerLinkErrorEnum = ManagerLinkErrorEnum
