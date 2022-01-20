"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.targeting_dimension_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TargetingSetting(google.protobuf.message.Message):
    """Proto file describing TargetingSetting

    Settings for the targeting-related features, at the campaign and ad group
    levels. For more details about the targeting setting, visit
    https://support.google.com/google-ads/answer/7365594
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TARGET_RESTRICTIONS_FIELD_NUMBER: builtins.int
    TARGET_RESTRICTION_OPERATIONS_FIELD_NUMBER: builtins.int
    @property
    def target_restrictions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TargetRestriction]:
        """The per-targeting-dimension setting to restrict the reach of your campaign
        or ad group.
        """
        pass
    @property
    def target_restriction_operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TargetRestrictionOperation]:
        """The list of operations changing the target restrictions.

        Adding a target restriction with a targeting dimension that already exists
        causes the existing target restriction to be replaced with the new value.
        """
        pass
    def __init__(self,
        *,
        target_restrictions : typing.Optional[typing.Iterable[global___TargetRestriction]] = ...,
        target_restriction_operations : typing.Optional[typing.Iterable[global___TargetRestrictionOperation]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_restriction_operations",b"target_restriction_operations","target_restrictions",b"target_restrictions"]) -> None: ...
global___TargetingSetting = TargetingSetting

class TargetRestriction(google.protobuf.message.Message):
    """The list of per-targeting-dimension targeting settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TARGETING_DIMENSION_FIELD_NUMBER: builtins.int
    BID_ONLY_FIELD_NUMBER: builtins.int
    targeting_dimension: google.ads.googleads.v8.enums.targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension.ValueType = ...
    """The targeting dimension that these settings apply to."""

    bid_only: builtins.bool = ...
    """Indicates whether to restrict your ads to show only for the criteria you
    have selected for this targeting_dimension, or to target all values for
    this targeting_dimension and show ads based on your targeting in other
    TargetingDimensions. A value of `true` means that these criteria will only
    apply bid modifiers, and not affect targeting. A value of `false` means
    that these criteria will restrict targeting as well as applying bid
    modifiers.
    """

    def __init__(self,
        *,
        targeting_dimension : google.ads.googleads.v8.enums.targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension.ValueType = ...,
        bid_only : typing.Optional[builtins.bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_bid_only",b"_bid_only","bid_only",b"bid_only"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_bid_only",b"_bid_only","bid_only",b"bid_only","targeting_dimension",b"targeting_dimension"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_bid_only",b"_bid_only"]) -> typing.Optional[typing_extensions.Literal["bid_only"]]: ...
global___TargetRestriction = TargetRestriction

class TargetRestrictionOperation(google.protobuf.message.Message):
    """Operation to be performed on a target restriction list in a mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Operator:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OperatorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Operator.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: TargetRestrictionOperation.Operator.ValueType = ...  # 0
        """Unspecified."""

        UNKNOWN: TargetRestrictionOperation.Operator.ValueType = ...  # 1
        """Used for return value only. Represents value unknown in this version."""

        ADD: TargetRestrictionOperation.Operator.ValueType = ...  # 2
        """Add the restriction to the existing restrictions."""

        REMOVE: TargetRestrictionOperation.Operator.ValueType = ...  # 3
        """Remove the restriction from the existing restrictions."""

    class Operator(_Operator, metaclass=_OperatorEnumTypeWrapper):
        """The operator."""
        pass

    UNSPECIFIED: TargetRestrictionOperation.Operator.ValueType = ...  # 0
    """Unspecified."""

    UNKNOWN: TargetRestrictionOperation.Operator.ValueType = ...  # 1
    """Used for return value only. Represents value unknown in this version."""

    ADD: TargetRestrictionOperation.Operator.ValueType = ...  # 2
    """Add the restriction to the existing restrictions."""

    REMOVE: TargetRestrictionOperation.Operator.ValueType = ...  # 3
    """Remove the restriction from the existing restrictions."""


    OPERATOR_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    operator: global___TargetRestrictionOperation.Operator.ValueType = ...
    """Type of list operation to perform."""

    @property
    def value(self) -> global___TargetRestriction:
        """The target restriction being added to or removed from the list."""
        pass
    def __init__(self,
        *,
        operator : global___TargetRestrictionOperation.Operator.ValueType = ...,
        value : typing.Optional[global___TargetRestriction] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["operator",b"operator","value",b"value"]) -> None: ...
global___TargetRestrictionOperation = TargetRestrictionOperation
