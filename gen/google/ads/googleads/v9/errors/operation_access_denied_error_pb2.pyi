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

class OperationAccessDeniedErrorEnum(google.protobuf.message.Message):
    """Proto file describing operation access denied errors.

    Container for enum describing possible operation access denied errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _OperationAccessDeniedError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OperationAccessDeniedErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OperationAccessDeniedError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        ACTION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 2
        """Unauthorized invocation of a service's method (get, mutate, etc.)"""

        CREATE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 3
        """Unauthorized CREATE operation in invoking a service's mutate method."""

        REMOVE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 4
        """Unauthorized REMOVE operation in invoking a service's mutate method."""

        UPDATE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 5
        """Unauthorized UPDATE operation in invoking a service's mutate method."""

        MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 6
        """A mutate action is not allowed on this resource, from this client."""

        OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 7
        """This operation is not permitted on this campaign type"""

        CREATE_AS_REMOVED_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 8
        """A CREATE operation may not set status to REMOVED."""

        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 9
        """This operation is not allowed because the resource is removed."""

        OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 10
        """This operation is not permitted on this ad group type."""

        MUTATE_NOT_PERMITTED_FOR_CUSTOMER: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 11
        """The mutate is not allowed for this customer."""

    class OperationAccessDeniedError(_OperationAccessDeniedError, metaclass=_OperationAccessDeniedErrorEnumTypeWrapper):
        """Enum describing possible operation access denied errors."""
        pass

    UNSPECIFIED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    ACTION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 2
    """Unauthorized invocation of a service's method (get, mutate, etc.)"""

    CREATE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 3
    """Unauthorized CREATE operation in invoking a service's mutate method."""

    REMOVE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 4
    """Unauthorized REMOVE operation in invoking a service's mutate method."""

    UPDATE_OPERATION_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 5
    """Unauthorized UPDATE operation in invoking a service's mutate method."""

    MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 6
    """A mutate action is not allowed on this resource, from this client."""

    OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 7
    """This operation is not permitted on this campaign type"""

    CREATE_AS_REMOVED_NOT_PERMITTED: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 8
    """A CREATE operation may not set status to REMOVED."""

    OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 9
    """This operation is not allowed because the resource is removed."""

    OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 10
    """This operation is not permitted on this ad group type."""

    MUTATE_NOT_PERMITTED_FOR_CUSTOMER: OperationAccessDeniedErrorEnum.OperationAccessDeniedError.ValueType = ...  # 11
    """The mutate is not allowed for this customer."""


    def __init__(self,
        ) -> None: ...
global___OperationAccessDeniedErrorEnum = OperationAccessDeniedErrorEnum
