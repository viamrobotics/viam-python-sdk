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

class AdCustomizerPlaceholderFieldEnum(google.protobuf.message.Message):
    """Proto file describing Ad Customizer placeholder fields.

    Values for Ad Customizer placeholder fields.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AdCustomizerPlaceholderField:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AdCustomizerPlaceholderFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AdCustomizerPlaceholderField.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 0
        """Not specified."""

        UNKNOWN: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        INTEGER: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 2
        """Data Type: INT64. Integer value to be inserted."""

        PRICE: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 3
        """Data Type: STRING. Price value to be inserted."""

        DATE: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 4
        """Data Type: DATE_TIME. Date value to be inserted."""

        STRING: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 5
        """Data Type: STRING. String value to be inserted."""

    class AdCustomizerPlaceholderField(_AdCustomizerPlaceholderField, metaclass=_AdCustomizerPlaceholderFieldEnumTypeWrapper):
        """Possible values for Ad Customizers placeholder fields."""
        pass

    UNSPECIFIED: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 0
    """Not specified."""

    UNKNOWN: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    INTEGER: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 2
    """Data Type: INT64. Integer value to be inserted."""

    PRICE: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 3
    """Data Type: STRING. Price value to be inserted."""

    DATE: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 4
    """Data Type: DATE_TIME. Date value to be inserted."""

    STRING: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.ValueType = ...  # 5
    """Data Type: STRING. String value to be inserted."""


    def __init__(self,
        ) -> None: ...
global___AdCustomizerPlaceholderFieldEnum = AdCustomizerPlaceholderFieldEnum
