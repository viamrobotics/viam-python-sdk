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

class CustomAudienceErrorEnum(google.protobuf.message.Message):
    """Proto file describing custom audience errors.

    Container for enum describing possible custom audience errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CustomAudienceError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CustomAudienceErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CustomAudienceError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        NAME_ALREADY_USED: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 2
        """New name in the custom audience is duplicated ignoring cases."""

        CANNOT_REMOVE_WHILE_IN_USE: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 3
        """Cannot remove a custom audience while it's still being used as targeting."""

        RESOURCE_ALREADY_REMOVED: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 4
        """Cannot update or remove a custom audience that is already removed."""

        MEMBER_TYPE_AND_PARAMETER_ALREADY_EXISTED: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 5
        """The pair of [type, value] already exists in members."""

        INVALID_MEMBER_TYPE: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 6
        """Member type is invalid."""

        MEMBER_TYPE_AND_VALUE_DOES_NOT_MATCH: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 7
        """Member type does not have associated value."""

        POLICY_VIOLATION: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 8
        """Custom audience contains a member that violates policy."""

        INVALID_TYPE_CHANGE: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 9
        """Change in custom audience type is not allowed."""

    class CustomAudienceError(_CustomAudienceError, metaclass=_CustomAudienceErrorEnumTypeWrapper):
        """Enum describing possible custom audience errors."""
        pass

    UNSPECIFIED: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    NAME_ALREADY_USED: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 2
    """New name in the custom audience is duplicated ignoring cases."""

    CANNOT_REMOVE_WHILE_IN_USE: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 3
    """Cannot remove a custom audience while it's still being used as targeting."""

    RESOURCE_ALREADY_REMOVED: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 4
    """Cannot update or remove a custom audience that is already removed."""

    MEMBER_TYPE_AND_PARAMETER_ALREADY_EXISTED: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 5
    """The pair of [type, value] already exists in members."""

    INVALID_MEMBER_TYPE: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 6
    """Member type is invalid."""

    MEMBER_TYPE_AND_VALUE_DOES_NOT_MATCH: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 7
    """Member type does not have associated value."""

    POLICY_VIOLATION: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 8
    """Custom audience contains a member that violates policy."""

    INVALID_TYPE_CHANGE: CustomAudienceErrorEnum.CustomAudienceError.ValueType = ...  # 9
    """Change in custom audience type is not allowed."""


    def __init__(self,
        ) -> None: ...
global___CustomAudienceErrorEnum = CustomAudienceErrorEnum
